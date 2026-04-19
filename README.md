# Network-Delay-Measurement-Tool
Delay Measurement / Learning Switch using POX Controller

Objective
The objective of this project is to implement a basic Software Defined Networking (SDN) controller using the POX framework that handles packet forwarding, learns MAC addresses dynamically, and installs OpenFlow flow rules to enable efficient communication between hosts in a Mininet environment.

Tools Used

•	POX Controller – to implement SDN logic 
•	Mininet – to simulate network topology 
•	OpenFlow Protocol – communication between controller and switch 

Network Topology

A simple topology is used:
•	1 Switch 
•	3 Hosts (h1, h2, h3) 

Working Principle

1.	When a packet arrives at the switch, it generates a PacketIn event. 
2.	The controller handles this event using the _handle_PacketIn function. 
3.	The controller extracts: 
o	Source MAC address 
o	Destination MAC address 
o	Input port 
4.	The controller learns MAC-to-port mapping:
MAC address → Switch port
5.	If the destination MAC is known: 
o	Packet is forwarded to the correct port 
6.	If unknown: 
o	Packet is flooded to all ports 

Flow Rule Installation
The controller installs flow rules using:
of.ofp_flow_mod()

Flow Rule Details:
•	Match: Source MAC + Destination MAC 
•	Action: Forward to specific port 
 This ensures:
•	Future packets bypass controller 
•	Faster communication 

Packet Forwarding

The controller sends packets using:
of.ofp_packet_out()
This ensures immediate forwarding of the current packet.

Controller Logic

The controller performs:
•	Packet parsing 
•	MAC learning 
•	Flow rule installation 
•	Packet forwarding 

Testing and Validation

•	Command: h1 ping h2 
•	Result: Successful communication 
•	Observation: Controller logs packet flow and installs rules 
•	First packet is flooded 
•	After learning, direct forwarding occurs 

Output

Controller displays:
Packet: <src MAC> -> <dst MAC> (switch ID)

Conclusion

The project successfully demonstrates:
•	Handling of PacketIn events 
•	Dynamic MAC learning 
•	Installation of OpenFlow flow rules 
•	Efficient packet forwarding 
This implementation behaves as a learning switch in an SDN environment, improving network performance by reducing controller involvement after initial packet processing.
