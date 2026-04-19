from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

# MAC address table
mac_to_port = {}

def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port
    dpid = event.dpid

    if not packet.parsed:
        log.warning("Ignoring incomplete packet")
        return

    src = packet.src
    dst = packet.dst

    log.info(f"Packet: {src} -> {dst} (switch {dpid})")

    # Learn MAC address
    mac_to_port[src] = in_port

    if dst in mac_to_port:
        out_port = mac_to_port[dst]
    else:
        out_port = of.OFPP_FLOOD

    # Install flow rule
    msg = of.ofp_flow_mod()
    msg.match.dl_src = src
    msg.match.dl_dst = dst
    msg.actions.append(of.ofp_action_output(port=out_port))

    event.connection.send(msg)

    # Send packet out
    msg = of.ofp_packet_out()
    msg.data = event.ofp
    msg.actions.append(of.ofp_action_output(port=out_port))
    msg.in_port = in_port

    event.connection.send(msg)


def launch():
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Delay Measurement POX Controller Running...")