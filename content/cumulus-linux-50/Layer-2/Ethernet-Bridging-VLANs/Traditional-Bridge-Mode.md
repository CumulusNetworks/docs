---
title: Traditional Bridge Mode
author: NVIDIA
weight: 440
toc: 4
---
For {{<link url="Traditional-Bridge-Mode" text="traditional Linux bridges">}}, the kernel supports VLANs in the form of VLAN subinterfaces. Enabling bridging on multiple VLANs means configuring a bridge for each VLAN and, for each member port on a bridge, creating one or more VLAN subinterfaces out of that port. This mode can pose scalability challenges in terms of configuration size as well as boot time and run time state management, when the number of ports times the number of VLANs becomes large.

{{%notice note%}}

Use *{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode">}}* bridges instead of *traditional mode* bridges. The bridge driver in Cumulus Linux is capable of VLAN filtering, which allows for configurations that are similar to incumbent network devices. Use traditional mode bridges only if you need to run more than one bridge on the switch or if you need to use PVSTP+. For a comparison of traditional and VLAN-aware modes, read {{<exlink url="https://docs.cumulusnetworks.com/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode/" text="this knowledge base article">}}.

{{%/notice%}}

## Configure a Traditional Mode Bridge

The following examples show how to create a simple traditional mode bridge configuration on the switch and use some optional elements:

- You can add an IP address to provide IP access to the bridge interface.
- You can specify a range of interfaces.

To configure spanning tree options for a bridge interface, refer to {{<link title="Spanning Tree and Rapid Spanning Tree - STP">}}.

The following example commands configure a traditional mode bridge called my_bridge with IP address 10.10.10.10/24. swp1, swp2, swp3, and swp4 are members of the bridge.

{{< tabs "TabID20 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge my_bridge ports swp1-4
cumulus@switch:~$ net add bridge my_bridge ip address 10.10.10.10/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
...
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4

auto my_bridge
iface my_bridge
    address 10.10.10.10/24
    bridge-ports swp1 swp2 swp3 swp4
    bridge-vlan-aware no
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

The name of the bridge must be:

- Compliant with Linux interface naming conventions.
- Unique within the switch.
- Something other than *bridge*, as Cumulus Linux reserves that name for a single {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}}.

{{%/notice%}}

{{%notice warning%}}

Do not try to bridge the management port, eth0, with any switch ports (swp0, swp1, and so on). For example, if you create a bridge with eth0 and swp1, it does **not** work.

{{%/notice%}}

## Configure Multiple Traditional Mode Bridges

You can configure multiple bridges to logically divide a switch into multiple layer 2 domains. This allows for hosts to communicate with other hosts in the same domain, while separating them from hosts in other domains.

The diagram below shows a multiple bridge configuration, where host-1 and host-2 are connected to bridge-A, while host-3 and host-4 are connected to bridge-B:

- host-1 and host-2 can communicate with each other
- host-3 and host-4 can communicate with each other
- host-1 and host-2 cannot communicate with host-3 and host-4

{{< img src = "/images/cumulus-linux/ethernet-bridging-multiple-bridges.png" >}}

This example configuration looks like this in the `/etc/network/interfaces` file:

```
...
auto bridge-A
iface bridge-A
    bridge-ports swp1 swp2
    bridge-vlan-aware no

auto bridge-B
iface bridge-B
    bridge-ports swp3 swp4
    bridge-vlan-aware no
...
```

## Trunks in Traditional Bridge Mode

The {{<exlink url="http://www.ieee802.org/1/pages/802.1Q.html" text=" standard">}} for trunking is 802.1Q. The 802.1Q specification adds a 4 byte header within the Ethernet frame that identifies the VLAN of which the frame is a member.

802.1Q also identifies an *untagged* frame as belonging to the *native* VLAN (most network devices default their native VLAN to 1). In Cumulus Linux:

- A *trunk port* is a switch port configured to send and receive 802.1Q tagged frames.
- A switch sending an untagged (bare Ethernet) frame on a trunk port is sending from the native VLAN defined on the trunk port.
- A switch sending a tagged frame on a trunk port is sending to the VLAN identified by the 802.1Q tag.
- A switch receiving an untagged (bare Ethernet) frame on a trunk port places that frame in the native VLAN defined on the trunk port.
- A switch receiving a tagged frame on a trunk port places that frame in the VLAN identified by the 802.1Q tag.

A bridge in traditional mode has no concept of trunks, just tagged or untagged frames. With a trunk of 200 VLANs, there would need to be 199 bridges, each containing a tagged physical interface, and one bridge containing the native untagged VLAN.

{{%notice note%}}

The interaction of tagged and un-tagged frames on the same trunk often leads to undesired and unexpected behavior. A switch that uses VLAN 1 for the native VLAN might send frames to a switch that uses VLAN 2 for the native VLAN, merging those two VLANs and their spanning tree state.

{{%/notice%}}

### Trunk Example

{{< img src = "/images/cumulus-linux/ethernet-bridging-trunk1.png" >}}

To create the above example:

{{< tabs "TabID136 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge br-VLAN10 ports swp1.10,swp2.10
cumulus@switch:~$ net add bridge br-VLAN20 ports swp1.20,swp2.20
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Add the following configuration to the `/etc/network/interfaces` file:

```
...
auto br-VLAN10
iface br-VLAN10
   bridge-ports swp1.10 swp2.10

auto br-VLAN20
iface br-VLAN20
   bridge-ports swp1.20 swp2.20
...
```

{{< /tab >}}

{{< /tabs >}}

For more examples of VLAN tagging, see {{<link url="VLAN-Tagging" text="VLAN Tagging">}}.

### Configure ARP Timers

Cumulus Linux does not often interact directly with end systems as much as end systems interact with one another. Therefore, after a successful {{<exlink url="http://linux-ip.net/html/ether-arp.html" text="address resolution protocol">}} (ARP) places a neighbor into a reachable state, Cumulus Linux might not interact with the client again for a long enough period of time for the neighbor to move into a stale state. To keep neighbors in the reachable state, Cumulus Linux includes a background process (`/usr/bin/neighmgrd`). The background process tracks neighbors that move into a stale, delay, or probe state, and attempts to refresh their state before they are removed from the Linux kernel and from hardware forwarding. The `neighmgrd` process only adds a neighbor if the sender's IP in the ARP packet is in one of the SVI's subnets (you can disable this check by setting `subnet_checks` to *0* in the `/etc/cumulus/neighmgr.conf` file).

The ARP refresh timer defaults to 1080 seconds (18 minutes). To change this setting, follow the procedures outlined in this {{<link url="Address-Resolution-Protocol-ARP">}}.
