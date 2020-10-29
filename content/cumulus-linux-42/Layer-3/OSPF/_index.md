---
title: Open Shortest Path First - OSPF
author: Cumulus Networks
weight: 880
toc: 3
---

OSPF maintains the view of the network topology conceptually as a directed graph. Each router represents a vertex in the graph. Each link between neighboring routers represents a unidirectional edge and has an associated weight (called cost) that is either automatically derived from its bandwidth or administratively assigned. Using the weighted topology graph, each router computes a shortest path tree (SPT) with itself as the root, and applies the results to build its forwarding table. The computation is generally referred to as *SPF computation* and the resultant tree as the *SPF tree*.

An LSA (*link-state advertisement*) is the fundamental piece of information that OSPF routers exchange with each other. It seeds the graph building process on the node and triggers SPF computation. LSAs originated by a node are distributed to all the other nodes in the network through a mechanism called *flooding*. Flooding is done hop-by-hop. OSPF ensures reliability by using link state acknowledgement packets. The set of LSAs in a router's memory is termed *link-state database* (LSDB) and is a representation of the network graph. OSPF ensures a consistent view of the LSDB on each node in the network in a distributed fashion, which is key to the protocol's correctness.

Cumulus Linux supports:
- {{<link url="Open-Shortest-Path-First-v2-OSPFv2">}} for IPv4.
- {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}} for IPv6.

## Scalability and Areas

The OSPF protocol advocates hierarchy as a *divide and conquer* approach to achieve high scale. You can divide the topology into areas, resulting in a two-level hierarchy. Area 0 (or 0.0.0.0), called the backbone area, is the top level of the hierarchy. Packets traveling from one non-zero area to another must go through the backbone area. For example, you can divide the leaf-spine topology into the following areas:

{{< img src = "/images/cumulus-linux/ospf-areas.png" >}}

{{%notice note%}}

- Routers R3, R4, R5, R6 are *area border routers* (ABRs). These routers have links to multiple areas and perform a set of specialized tasks, such as SPF computation per area and summarization of routes across areas.
- Most of the LSAs have an area-level flooding scope. These include router LSA, network LSA, and summary LSA.
- Where ABRs do not connect to multiple non-zero areas, you can use the same area address.

{{%/notice%}}

## OSPF and ECMP

During SPF computation for an area, if OSPF finds multiple paths with equal cost, all those paths are used for forwarding.
