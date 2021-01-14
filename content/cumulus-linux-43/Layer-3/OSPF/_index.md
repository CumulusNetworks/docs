---
title: Open Shortest Path First - OSPF
author: NVIDIA
weight: 890
toc: 3
---
Open Shortest Path First (OSPF) is a link-state routing protocol used between routers to exchange information about routes and the cost to reach an intended destination. OSPF routers exchange information about their links, prefixes, and associated cost with Link State Advertisements (LSAs). This topology information is used to build a topology database. Each router within an area has an identical database and calculates its own routing table using the Shortest Path First (SPF) algorithm. The SPF algorithm is used any time there are changes to routing information in the network. OSPF uses the concept of areas to try and limit the size of the topology database on different routers. The routers that exist in more than one area are called Area Border Routers (ABRs) and they simplify the information contained within LSAs when advertising LSAs from one area to another. ABRs are the only routers in OSPF that are allowed to implement route filtering or route summarization.

Cumulus Linux supports:
- {{<link url="Open-Shortest-Path-First-v2-OSPFv2">}} for IPv4.
- {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}} for IPv6.
