---
title: Comparing NCLU and vtysh Commands
author: Cumulus Networks
weight: 403
aliases:
 - /display/DOCS/Comparing+NCLU+and+vtysh+Commands
 - /pages/viewpage.action?pageId=8366644
product: Cumulus Linux
version: '4.0'
---
Using [NCLU](../../../System-Configuration/Network-Command-Line-Utility-NCLU/) is the recommended way to [configure routing](../../Configuring-FRRouting/) in Cumulus Linux; however, you can use the `vtysh` modal CLI.

The following table shows the FRRouting commands and the equivalent Cumulus Linux NCLU commands.

| Action | NCLU Commands| FRRouting Commands |
|------- |--------------- |----------------- |
| Display the routing table | <pre>cumulus@switch:~$ net show route</pre> | <pre>switch# show ip route</pre> |
| Create a new neighbor | <pre>cumulus@switch:~$ net add bgp autonomous-system 65002<br>cumulus@switch:~$ net add bgp neighbor 14.0.0.22</pre> | <pre>switch(config)# router bgp 65002<br>switch(config-router)# neighbor 14.0.0.22</pre> |
| Redistribute routing information from static route entries into RIP tables | <pre>cumulus@switch:~$ net add bgp redistribute static</pre> | <pre>switch(config)# router bgp 65002<br>switch(config-router)# redistribute static</pre> |
| Define a [static route](../../Routing/) | <pre>cumulus@switch:~$ net add routing route 155.1.2.20/24 bridge 45</pre> | <pre>switch(config)# ip route 155.1.2.20/24 bridge 45</pre> |
| Configure an IPv6 address | <pre>cumulus@switch:~$ net add interface swp3 ipv6 address 3002:2123:1234:1abc::21/64</pre> | <pre>switch(config)# int swp3<br>switch(config-if)# ipv6 address 3002:2123:1234:1abc::21/64</pre> |
| Enable topology checking ([PTM](../../../Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM/)) |<pre>cumulus@switch:~$ net add routing ptm-enable</pre> | <pre>switch(config)# ptm-enable</pre> |
|Configure [MTU](../../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes#mtu) in IPv6 network discovery for an interface|<pre>cumulus@switch:~$ sudo cl-ra interface swp3 set mtu 9000</pre> | <pre>switch(config)# int swp3<br>switch(config-if)# ipv6 nd mtu 9000</pre> |
| Set the OSPF interface priority | <pre>cumulus@switch:~$ net add interface swp3 ospf6 priority 120</pre> |<pre>switch(config)# int swp3<br>switch(config-if)# ip ospf6 priority 120</pre> |
| Configure timing for OSPF SPF calculations | <pre>cumulus@switch:~$ net add ospf6 timers throttle spf 40 50 60</pre> | <pre>switch(config)# router ospf6<br>switch(config-ospf6)# timer throttle spf 40 50 60</pre> |
| Configure the OSPF Hello packet interval in number of seconds for an interface | <pre>cumulus@switch:~$ net add interface swp4 ospf6 hello-interval 60</pre> | <pre>switch(config)# int swp4<br>switch(config-if)# ipv6 ospf6 hello-interval  60</pre> |
| Display [BGP](../../Bidirectional-Forwarding-Detection-BFD/) information | <pre>cumulus@switch:~$ net show bgp summary</pre> | <pre>switch# show ip bgp summary</pre> |
| Display OSPF debugging status | <pre>cumulus@switch:~$ net show debugs</pre> | <pre>switch# show debugging ospf</pre> |
| Show information about the interfaces on the switch | <pre>cumulus@switch:~$ net show interface</pre> | <pre>switch# show interface</pre>To quickly check important information, such as IP address, VRF, and operational status, in easy to read tabular format:<pre>switch# show interface brief</pre> |
