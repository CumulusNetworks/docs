---
title: Routing
author: NVIDIA
weight: 720
toc: 3
---
Network routing is the process of selecting a path across one or more networks. When the switch receives a packet, it reads the packet headers to find out its intended destination. It then determines where to route the packet based on information in its routing tables, which can be static or dynamic.

Cumulus Linux supports both {{<link url="Static-Routing">}}, where you enter routes and specify the next hop manually and dynamic routing such as {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}, and {{<link url="Open-Shortest-Path-First-OSPF" text="OSP">}}, where you configure a routing protocol on your switch and the routing protocol learns about other routers automatically.

For the number of route table entries supported per platform, see {{<link title="Forwarding Table Size and Profiles">}}.