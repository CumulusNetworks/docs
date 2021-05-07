---
title: Comparing NCLU and vtysh Commands
author: NVIDIA
weight: 437
pageID: 8362390
---
Using
[NCLU](/cumulus-linux-36/System-Configuration/Network-Command-Line-Utility-NCLU/)
is the primary way to 
[configure routing](/cumulus-linux-36/Layer-3/Configuring-FRRouting/) 
in Cumulus Linux. However, an alternative exists in `vtysh` modal
CLI. The available commands are as follows:

## Comparing vtysh and NCLU Commands

The following table compares the various FRRouting commands with their
Cumulus Linux NCLU counterparts.

|Action|NCLU Commands|FRRouting Commands|
|--- |--- |--- |
|Display the routing table|```cumulus@switch:~$ net show route```|```switch# show ip route```|
|Create a new neighbor|```cumulus@switch:~$ net add bgp autonomous-system 65002```<br />```cumulus@switch:~$ net add bgp neighbor 14.0.0.22```|```switch(config)# router bgp 65002```<br />```switch(config-router)# neighbor 14.0.0.22```|
|Redistribute routing information from static route entries into RIP tables|```cumulus@switch:~$ net add bgp redistribute static```|```switch(config)# router bgp 65002```<br />```switch(config-router)# redistribute static```|
|Define a static route|```cumulus@switch:~$ net add routing route 155.1.2.20/24 bridge 45```|```switch(config)# ip route 155.1.2.20/24 bridge 45```|
|Configure an IPv6 address|```cumulus@switch:~$ net add interface swp3 ipv6 address 3002:2123:1234:1abc::21/64```|```switch(config)# int swp3```<br />```switch(config-if)# ipv6 address 3002:2123:1234:1abc::21/64```|
|Enable topology checking (PTM)|```cumulus@switch:~$ net add routing ptm-enable```|```switch(config)# ptm-enable```|
|Configure MTU in IPv6 network discovery for an interface|```cumulus@switch:~$ sudo cl-ra interface swp3 set mtu 9000```|```switch(config)# int swp3```<br />```switch(config-if)# ipv6 nd mtu 9000```|
|Set the OSPF interface priority|```cumulus@switch:~$ net add interface swp3 ospf6 priority 120```|```switch(config)# int swp3```<br />```switch(config-if)# ip ospf6 priority  120```|
|Configure timing for OSPF SPF calculations|```cumulus@switch:~$ net add ospf6 timers throttle spf 40 50 60```|```switch(config)# router ospf6```<br />```switch(config-ospf6)# timer throttle spf 40 50 60```|
|Configure the OSPF Hello packet interval in number of seconds for an interface|```cumulus@switch:~$ net add interface swp4 ospf6 hello-interval 60```|```switch(config)# int swp4```<br />```switch(config-if)# ipv6 ospf6 hello-interval  60```|
|Display BGP information|```cumulus@switch:~$ net show bgp summary```|```switch# show ip bgp summary```|
|Display OSPF debugging status|```cumulus@switch:~$ net show debugs```|```switch# show debugging ospf```|
