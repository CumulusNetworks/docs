---
title: Open Shortest Path First - OSPF
author: Cumulus Networks
weight: 880
toc: 3
---

Open Shortest Path First (OSPF) is a routing protocol used between routers to exchange information about the routes they know about and the cost for them to get there. Information about all of the routes in a network are learned by all of the OSPF routers within an *area*. Each OSPF router distributes information about its local state (usable interfaces and reachable neighbors, and the cost of using each interface) to other routers using a Link State Advertisement (LSA) message. Each router uses the received messages to build up an identical database that describes the topology of the AS. From this database, each router calculates its own routing table using a Shortest Path First (SPF) algorithm. This routing table contains all the destinations the routing protocol knows about, associated with a next hop IP address and outgoing interface.

During SPF computation for an area, if OSPF finds multiple paths with equal cost, all those paths are used for forwarding.

Cumulus Linux supports:
- {{<link url="Open-Shortest-Path-First-v2-OSPFv2">}} for IPv4.
- {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}} for IPv6.

## Scalability and Areas

The OSPF protocol advocates hierarchy as a *divide and conquer* approach to achieve high scale. You can divide the topology into areas, resulting in a two-level hierarchy. Area 0 (or 0.0.0.0), called the backbone area, is the top level of the hierarchy. Packets traveling from one non-zero area to another must go through the backbone area. For example, you can divide the leaf-spine topology into the following areas:

{{< img src = "/images/cumulus-linux/ospf-scalability-areas.png" >}}

{{%notice note%}}

- border01 and border02 are *area border routers* (ABRs). These routers have links to multiple areas and perform a set of specialized tasks, such as SPF computation per area and summarization of routes across areas.
- Most of the LSAs have an area-level flooding scope. These include router LSA, network LSA, and summary LSA.
- Where ABRs do not connect to multiple non-zero areas, you can use the same area address.

{{%/notice%}}
