---
title: Open Shortest Path First - OSPF
author: Cumulus Networks
weight: 880
toc: 3
---

Open Shortest Path First (OSPF) is a protocol used between routers to exchange information about routes and the cost to reach an intended destination. All OSPF routers within an *area* learn about all of the routes in a network and each router distributes information about its local state (interfaces, reachable neighbors, and the cost of using each interface) to other routers using a Link State Advertisement (LSA) message. Each router uses the received messages to build up an identical database and calculates its own routing table using a Shortest Path First (SPF) algorithm. This routing table contains all the destinations that the routing protocol knows about, and the associated next hop IP address and outgoing interface.

Cumulus Linux supports:
- {{<link url="Open-Shortest-Path-First-v2-OSPFv2">}} for IPv4.
- {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}} for IPv6.
