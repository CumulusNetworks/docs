---
title: FRRouting Overview
author: Cumulus Networks
weight: 177
aliases:
 - /display/CL34/FRRouting+Overview
 - /pages/viewpage.action?pageId=7112656
pageID: 7112656
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
Cumulus Linux uses FRRouting to provide the routing protocols for
dynamic routing. FRRouting provides many routing protocols, of which
Cumulus Linux supports the following:

  - Open Shortest Path First
    ([v2](/version/cumulus-linux-343/Layer_Three/Open_Shortest_Path_First_-_OSPF_-_Protocol)
    and
    [v3](/version/cumulus-linux-343/Layer_Three/Open_Shortest_Path_First_v3_-_OSPFv3_-_Protocol))

  - [Border Gateway
    Protocol](/version/cumulus-linux-343/Layer_Three/Border_Gateway_Protocol_-_BGP)

## <span>Architecture</span>

{{% imgOld 0 %}}

As shown in the figure above, the FRRouting suite consists of various
protocol-specific daemons and a protocol-independent daemon called
`zebra`. Each of the protocol-specific daemons are responsible for
running the relevant protocol and building the routing table based on
the information exchanged.

It is not uncommon to have more than one protocol daemon running at the
same time. For example, at the edge of an enterprise, protocols internal
to an enterprise (called IGP for Interior Gateway Protocol) such as
[OSPF](/version/cumulus-linux-343/Layer_Three/Open_Shortest_Path_First_-_OSPF_-_Protocol)
or RIP run alongside the protocols that connect an enterprise to the
rest of the world (called EGP or Exterior Gateway Protocol) such as
[BGP](/version/cumulus-linux-343/Layer_Three/Border_Gateway_Protocol_-_BGP).

## <span>About zebra</span>

`zebra` is the daemon that resolves the routes provided by multiple
protocols (including static routes specified by the user) and programs
these routes in the Linux kernel via `netlink` (in Linux). `zebra` does
more than this, of course. The [FRRouting
documentation](https://frrouting.org/user-guide/Zebra.html#Zebra)
defines `zebra` as the IP routing manager for FRRouting that "provides
kernel routing table updates, interface lookups, and redistribution of
routes between different routing protocols."

## <span>Related Information</span>

  - [frrouting.org](https://frrouting.org)

  - [GitHub](https://github.com/FRRouting/frr)
