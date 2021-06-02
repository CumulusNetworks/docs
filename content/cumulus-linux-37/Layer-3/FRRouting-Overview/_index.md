---
title: FRRouting Overview
author: NVIDIA
weight: 175
pageID: 8362917
---
Cumulus Linux uses FRRouting to provide the routing protocols for dynamic routing. FRRouting provides many routing  protocols, of which Cumulus Linux supports the following:

- Open Shortest Path First ({{<link url="Open-Shortest-Path-First-OSPF" text="v2">}} and {{<link url="Open-Shortest-Path-First-v3-OSPFv3" text="v3">}})
- {{<link url="Border-Gateway-Protocol-BGP" text="Border Gateway Protocol">}}

## Architecture

{{< img src = "/images/cumulus-linux/frrouting-overview-daemons.png" >}}

As shown in the figure above, the FRRouting suite consists of various protocol-specific daemons and a protocol-independent daemon called `zebra`. Each of the protocol-specific daemons are responsible for running the relevant protocol and building the routing table based on the information exchanged.

It is not uncommon to have more than one protocol daemon running at the same time. For example, at the edge of an enterprise, protocols internal to an enterprise (called IGP for Interior Gateway Protocol) such as {{<link url="Open-Shortest-Path-First-OSPF" text="OSPF">}} or RIP run alongside the protocols that connect an enterprise to the rest of the world (called EGP or Exterior Gateway Protocol) such as {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}}.

## About zebra

`zebra` is the daemon that resolves the routes provided by multiple protocols (including static routes specified by the user) and programs these routes in the Linux kernel via `netlink` (in Linux). `zebra` does more than this, of course. The {{<exlink url="http://docs.frrouting.org/en/latest/zebra.html" text="FRRouting documentation">}} defines `zebra` as the IP routing manager for FRRouting that "provides kernel routing table updates, interface lookups, and redistribution of routes
between different routing protocols."

## Related Information

- {{<exlink url="https://frrouting.org" text="frrouting.org">}}
- {{<exlink url="https://github.com/FRRouting/frr" text="FRR on GitHub">}}
