---
title: Glossary
author: NVIDIA
weight: 1150
toc: 3
---

## Common Cumulus Linux and NetQ Terminology

The following table covers some basic terms used throughout the NetQ
user documentation.

|Term|Definition|
|--- |--- |
|Agent|NetQ software that resides on a host server that provides metrics about the host to the NetQ Telemetry Server for network health analysis.|
|Bridge|Device that connects two communication networks or network segments. Occurs at OSI Model Layer 2, Data Link Layer.|
|Clos|Multistage circuit switching network used by the telecommunications industry, first formalized by Charles Clos in 1952.|
|Device|UI term referring to a switch, host, or chassis or combination of these. Typically used when describing hardware and components versus a software or network topology. See also Node.|
|Event|Change or occurrence in network or component that can trigger a notification. Events are categorized by severity: error or info.|
|Fabric|Network topology where a set of network nodes interconnects through one or more network switches.|
|Fresh|Node that has been silent for the last 90 seconds.|
|High Availability|Software used to provide a high percentage of uptime (running and available) for network devices.|
|Host|A device connected to a TCP/IP network. It can run one or more virtual machines.|
|Hypervisor|Software which creates and runs virtual machines. Also called a virtual machine monitor.|
|IP Address|An Internet Protocol address comprises a series of numbers assigned to a network device to uniquely identify it on a given network. Version 4 addresses are 32 bits and written in dotted decimal notation with 8-bit binary numbers separated by decimal points. Example: 10.10.10.255. Version 6 addresses are 128 bits and written in 16-bit hexadecimal numbers separated by colons. Example: 2018:3468:1B5F::6482:D673.|
|Leaf|An access layer switch in a Spine-Leaf or Clos topology. An Exit-Leaf is a switch that connects to services outside of the data center such as firewalls, load balancers, and internet routers. See also Spine, Clos, Top of Rack, and Access Switch.|
|Linux|Set of free and open-source software operating systems built around the Linux kernel. Cumulus Linux is one of the available distribution packages.|
|Node|UI term referring to a switch, host, or chassis in a topology.|
|Notification|Item that informs a user of an event. Notifications are received through third-party applications, such as email or Slack. |
|Peer link|Link, or bonded links, used to connect two switches in an MLAG pair.|
|Rotten|Node that has been silent for 90 seconds or more.|
|Router|Device that forwards data packets (directs traffic) from nodes on one communication network to nodes on another network. Occurs at the OSI Model Layer 3, Network Layer.|
|Spine|Used to describe the role of a switch in a Spine-Leaf or Clos topology. See also Aggregation switch, End of Row switch, and distribution switch.|
|Switch|High-speed device that receives data packets from one device or node and redirects them to other devices or nodes on a network.|
|Telemetry server|NetQ server that receives metrics and other data from NetQ agents on leaf and spine switches and hosts.|
|Top of Rack|Switch that connects to the network (versus internally); also known as a ToR switch.|
|Virtual Machine|Emulation of a computer system that provides all the functions of a particular architecture.|
|Web-scale|A network architecture designed to deliver capabilities of large cloud service providers within an enterprise IT environment.|
|Whitebox|Generic, off-the-shelf, switch or router hardware used in Software Defined Networks (SDN).|


## Common Cumulus Linux and NetQ Acronyms

The following table covers some common acronyms used throughout the NetQ
user documentation.

| Acronym                                              | Meaning                                                                                    |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ACL | Access Control Link |
| ARP | Address Resolution Protocol |
| ASN | Autonomous System Number |
| BGP/eBGP/iBGP | Border Gateway Protocol, External BGP, Internal BGP |
| CLAG | Cumulus multi-chassis Link Aggregation Group |
| DHCP | Dynamic Host Control Protocol |
| DNS | Domain Name Server |
| ECMP | Equal Cost Multi-Path routing |
| EVPN | Ethernet Virtual Private Network |
| FDB | Forwarding Data Base |
| GNU | "GNU's Not Linux" |
| HA | High Availability |
| IGMP | Internet Group Management Protocol |
| IPv4/IPv6 | Internet Protocol, version 4 or 6 |
| LACP | Link Aggregation Control Protocol |
| LAN | Local Area Network |
| LCM | Lifecycle Management |
| LLDP | Link Layer Data Protocol |
| MAC | Media Access Control |
| MIB | Management Information Base |
| MLAG | Multi-chassis Link Aggregation Group |
| MLD | Multicast Listener Discovery |
| NTP | Network Time Protocol |
| OOB | Out of Band (management) |
| OPTA | On-premises Telemetry Aggregator |
| OSPF | Open Shortest Path First |
| PTP | Precision Time Protocol |
| RFC | Remote Function Call |
| RoCE | RDMA over Converged Ethernet |
| SDN | Software-Defined Network |
| SNMP | Simple Network Management Protocol |
| STP | Spanning Tree Protocol |
| TCA | Threshold Crossing Alarms |
| TCP | Transport Control Protocol |
| ToR | Top of Rack |
| UDP | User Datagram Protocol |
| URL | Universal Resource Locator |
| USB | Universal Serial Bus |
| VLAN | Virtual Local Area Network |
| VNI | Virtual Network Instance |
| VPN | Virtual Private Network |
| VRF | Virtual Routing and Forwarding |
| VRR | Virtual Router Redundancy |
| VTEP | VXLAN Tunnel EndPoint  |
| VXLAN | Virtual Extensible Local Area Network |
| ZTP | Zero Touch Provisioning |
