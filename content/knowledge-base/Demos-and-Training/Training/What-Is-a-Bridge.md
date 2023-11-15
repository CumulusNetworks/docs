---
title: What Is a Bridge
author: NVIDIA
weight: 552
toc: 4
---

Bridges are layer 2 switches and an integral part of Linux-based networking. This article provides network engineers with a conceptual understanding of what a bridge is, and how you can use them within Cumulus Linux, as well as examples of the bridges hiding within the configuration of incumbent vendors.

## Introduction

The concept of bridging can be foreign to those working in an incumbent vendor environment (Cisco, Juniper, Arista); modern networking environments ignore the term *bridge*, aside from a brief mention in the history section of the curriculum. However, the importance of software-defined bridges in Linux, and their comparison to traditional switches, makes this an important concept to fully understand.

It can be difficult to deploy a modern network without the use of a bridge somewhere in the configuration, though most engineers might not realize a bridge is in use. This is due in part to the convoluted history between the terms *bridge* and *switch*.

The term *bridge* is typically only used when talking about the root bridge in the STP, or the Spanning Tree Protocol. Root bridges in STP are usually other switches &mdash; you could easily call them root switches &mdash; and the concept is the same, as a switch is a bridge.

Another common use case for the word bridge today is when you are looking at products like a wireless Ethernet bridge. In this instance, the behavior is the same as the classic bridge, with only two ports (one for wifi and the other for the physical Ethernet segment).

## Concept 1: A Bridge Is not a Hub

The key difference between a bridge and a hub is that bridges intelligently transmit frames around the network, while hubs have zero intelligence in how they transmit frames.

As layer 1 devices, hubs are essentially invisible to the network, because they do not use any intelligence when delivering traffic to their destination, and perform no filtration of data. While using a hub might be the simplest method for splitting an Ethernet connection, it can cut your data-rate throughput to almost nothing in a high traffic environment. This is because with a hub, a frame comes into one port, and replicates instantly across every port, regardless of whether the destination lives on a particular port. This potentially causes each port connected to the hub to talk at the same time, resulting in each having to wait its turn.

## Concept 2: Bridges Are not Limited to Two Ports

**Corollary: To bridge a frame or to switch a frame is the same thing.**

Unlike hubs, bridges listen to the frames that get sent across the network. Bridges participate in source MAC address learning for each frame they receive, and maintain a MAC address table that defines the port associated with each MAC address.

When discussing foundational networking concepts, bridges are briefly mentioned as a method to segregate a collision domain (but not to separate a broadcast domain like a router). The old view of a bridge was a dedicated physical appliance that contained only two ports; this is still taught today, because understanding that a bridge could only contain two ports helps to clarify that a switch is a multi-port bridge.

While the idea of a bridge having two ports is convenient for teaching purposes, and accurate in the historical sense of what was initially on the market under the term *bridge*, it is not technically accurate. No standard ever existed that defined a limit on the number of ports that could be members of a bridge. The original {{<exlink url="https://standards.ieee.org/standard/802_1D-2004.html" text="IEEE 802.1D standard">}} even includes a bridge with three ports.

Conceptually, switches and bridges are the same. When the term switch became the dominant term for a networking device in the LAN, engineers stopped talking about bridging, as they rebranded bridges as switches. Today, two port physical bridges are no longer in use, in favor of the 48+ port bridges, now commonly referred to as multi-port switches.

## Concept 3: Most Vendors Use Software Bridges without Explicitly Declaring Their Use

The example below compares two configurations, one from Cisco IOS and one from Cumulus Linux.

{{%notice note%}}

By default, ports specified by the `bridge-ports` configuration are trunks. The configuration below overrides the trunk at the port level, because it defines the ports to be access ports for their respective VLANs.

{{%/notice%}}

**In Cisco IOS**

``` western
vlan 100,200
interface ethernet0/1
    switchport mode access
    switchport access vlan 100
interface ethernet0/2
    switchport mode access
    switchport access vlan 200
```

**In Cumulus Linux (with VLAN-aware Bridge)**

``` western
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 100 200
    bridge-stp on

auto swp1
iface swp1
    bridge access 100
auto swp2
iface swp2
    bridge access 200
```

{{<img src="/images/knowledge-base/what-is-a-bridge-1.png" width="500">}}

The two pieces of configuration are functionally the same. However, there is an additional concept underneath the surface that is useful to highlight. The example below highlights the configuration on Cumulus Linux:

**In Cumulus Linux (with VLAN-aware Bridge)**

``` western
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports glob swp1-48 
    bridge-vids 100 200
    bridge-stp on

auto swp1
iface swp1
    bridge access 100

auto swp
iface swp2
    bridge access 200
```

Cisco does not allow the user to configure this. In Cisco switches, all ports are members of a single bridge or switch. Cisco's declaration of VLANs with the `vlan 100,200` statement allows all ports in their undeclared software bridge to use those VLANs, and is nearly identical to the `bridge-vids` statement that defines the list of VLANs supported on all the member ports of the bridge within Cumulus Linux.

The difference here is that not all ports are inherently a member of a single bridge in Cumulus Linux. This distinction allows for the next concept below.

## Concept 4: Bridges Behave Like Logically Isolated Switches in Linux

**Corollary: Linux allows you to have more than one logical switch (bridge) defined on a single physical switch.**

In Linux and, by extension, Cumulus Linux, not all ports are members of the same logical switch or bridge by default. This behavior is different from incumbent vendors.

In the example below, bridges act like isolated switches. Because of this, it is possible for the isolated reuse of VLANs, by defining the VLANs inside of different logical switches (bridges). You declare to use `vlan 100` on two separate bridges.
<!-- vale off -->
These bridges are isolated from one another by default, and as there is no layer 3 switched virtual interface (SVI) that would allow for routing between them, they are totally isolated instances of `vlan 100`, and behave like two isolated switches. The MAC address tables for `vlan 100` are unique to each bridge, and as a result, the hosts connected to `vlan 100` on `bridge1` cannot communicate with `vlan 100` hosts on `bridge2`.
<!-- vale on -->
{{%notice warning%}}

NVIDIA does not recommend this configuration. It is uncommon and untested, though possible within the confines of what bridges allow within Linux. The example below uses it only to highlight the concept of bridges as logical isolated switches.

{{%/notice%}}

**In Cumulus Linux (with VLAN-aware Bridge and Traditional Bridge)**

```
auto swp1
iface swp1

auto swp
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4

auto swp3.100
iface swp3.100

auto swp4.100
iface swp4.100

auto bridge1
iface bridge1
    bridge-vlan-aware yes
    bridge-ports swp1 swp2
    bridge-vids 100
    bridge-stp on

auto bridge2
iface bridge2
    bridge-ports swp3.100 swp4.100
    bridge-stp on
```

{{<img src="/images/knowledge-base/what-is-a-bridge-2.png" width="400">}}

{{%notice note%}}

You can declare only one VLAN-aware bridge per physical switch in Cumulus Linux. The example above uses a combination of VLAN-aware (`bridge1`) and traditional (`bridge2`) bridge configurations.

{{%/notice%}}

{{%notice note%}}

Adding an SVI to these two bridges for `vlan 100` would provide a router-on-a-stick configuration, where the two previously isolated vlan100s would then be able to communicate using layer 3 routing.

{{%/notice%}}
