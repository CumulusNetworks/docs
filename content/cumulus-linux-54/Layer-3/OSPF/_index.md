---
title: Open Shortest Path First - OSPF
author: NVIDIA
weight: 890
toc: 3
---
<span style="background-color:#F5F5DC">[OSPF](## "Open Shortest Path First")</span> is a link-state routing protocol you use between routers to exchange information about routes and the cost to reach an intended destination. OSPF routers exchange information about their links, prefixes, and associated cost with <span style="background-color:#F5F5DC">[LSAs](## "Link State Advertisements")</span>. This topology information builds a topology database. Each router within an area has an identical database and calculates its own routing table using <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> algorithm. Cumulus Linux uses the SPF algorithm any time there are changes to routing information in the network. OSPF uses the concept of areas to try and limit the size of the topology database on different routers. The routers that exist in more than one area are <span style="background-color:#F5F5DC">[ABRs](## "Area Border Routers")</span>, which simplify the information in LSAs when advertising them from one area to another. ABRs are the routers in OSPF that implement route filtering or route summarization.

Cumulus Linux supports:
- {{<link url="Open-Shortest-Path-First-v2-OSPFv2">}} for IPv4.
- {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}} for IPv6.
