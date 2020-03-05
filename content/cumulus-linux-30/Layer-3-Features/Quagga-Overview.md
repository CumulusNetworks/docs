---
title: Quagga Overview
author: Cumulus Networks
weight: 133
aliases:
 - /display/CL30/Quagga+Overview
 - /pages/viewpage.action?pageId=5118385
pageID: 5118385
---
Cumulus Linux uses `quagga`, an open source routing software suite, to
provide the routing protocols for dynamic routing. Cumulus Linux
supports the l atest Quagga version, <span style="color: #2c2d30;">
0.99.23.1+cl3.0 </span> . Quagga is a fork of the [GNU
Zebra](http://www.gnu.org/software/zebra/) project.

Quagga provides many routing protocols, of which Cumulus Linux supports
the following:

  - Open Shortest Path First
    ([v2](/cumulus-linux-30/Layer-3-Features/Open-Shortest-Path-First-OSPF-Protocol)
    and
    [v3](/cumulus-linux-30/Layer-3-Features/Open-Shortest-Path-First-v3-OSPFv3-Protocol))

  - [Border Gateway
    Protocol](/cumulus-linux-30/Layer-3-Features/Border-Gateway-Protocol-BGP)

## Architecture</span>

{{% imgOld 0 %}}

As shown in the figure above, the Quagga routing suite consists of
various protocol-specific daemons and a protocol-independent daemon
called ` zebra  `. Each of the protocol-specific daemons are responsible
for running the relevant protocol and building the routing table based
on the information exchanged.

It is not uncommon to have more than one protocol daemon running at the
same time. For example, at the edge of an enterprise, protocols internal
to an enterprise (called IGP for Interior Gateway Protocol) such as
[OSPF](/cumulus-linux-30/Layer-3-Features/Open-Shortest-Path-First-OSPF-Protocol)
or RIP run alongside the protocols that connect an enterprise to the
rest of the world (called EGP or Exterior Gateway Protocol) such as
[BGP](/cumulus-linux-30/Layer-3-Features/Border-Gateway-Protocol-BGP).

`zebra` is the daemon that resolves the routes provided by multiple
protocols (including static routes specified by the user) and programs
these routes in the Linux kernel via `netlink` (in Linux). `zebra` does
more than this, of course.

## Zebra</span>

The [Quagga
documentation](http://www.nongnu.org/quagga/docs/docs-info.html#Zebra)
defines `zebra` as the IP routing manager for `quagga` that "provides
kernel routing table updates, interface lookups, and redistribution of
routes between different routing protocols."

## Configuration Files</span>

  - /etc/quagga/bgpd.conf

  - /etc/quagga/debian.conf

  - /etc/quagga/ospf6d.conf

  - /etc/quagga/ospfd.conf

  - /etc/quagga/vtysh.conf

  - /etc/quagga/zebra.conf

## Useful Links</span>

  - <http://www.quagga.net/>

  - <http://packages.debian.org/quagga>

