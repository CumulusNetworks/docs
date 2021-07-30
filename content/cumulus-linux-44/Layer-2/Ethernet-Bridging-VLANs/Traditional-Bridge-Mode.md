---
title: Traditional Bridge Mode
author: NVIDIA
weight: 440
toc: 4
---
For {{<link url="Traditional-Bridge-Mode" text="traditional Linux bridges">}}, the kernel supports VLANs in the form of VLAN subinterfaces. Enabling bridging on multiple VLANs means configuring a bridge for each VLAN and, for each member port on a bridge, creating one or more VLAN subinterfaces out of that port. This mode can pose scalability challenges with configuration size as well as boot time and run time state management, when the number of ports times the number of VLANs becomes large.

{{%notice note%}}
Use *{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode">}}* bridges instead of *traditional mode* bridges. Use traditional mode bridges if you need to use PVSTP+.
{{%/notice%}}

## Configure a Traditional Mode Bridge

The following examples show how to create a simple traditional mode bridge configuration on the switch. The example uses some optional elements:

- You can add an IP address to provide IP access to the bridge interface.
- You can specify a range of interfaces.

To configure spanning tree options for a bridge interface, refer to {{<link title="Spanning Tree and Rapid Spanning Tree - STP">}}.

The following example commands configure a traditional mode bridge called `my_bridge` with IP address 10.10.10.10/24. swp1, swp2, swp3, and swp4 are members of the bridge.

{{< tabs "TabID24 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge my_bridge ports swp1-4
cumulus@switch:~$ net add bridge my_bridge ip address 10.10.10.10/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

NVUE commands are not supported.

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
- Do not bridge the management port, eth0, with any switch ports (swp0, swp1, and so on). For example, if you create a bridge with eth0 and swp1, it does **not** work.
- The name of the bridge must be compliant with Linux interface naming conventions and unique within the switch.
{{%/notice%}}

## Configure Multiple Traditional Mode Bridges

You can configure multiple bridges to logically divide a switch into multiple layer 2 domains. This allows for hosts to communicate with other hosts in the same domain, while separating them from hosts in other domains.

The example below shows a multiple bridge configuration, where host-1 and host-2 are connected to bridge-A, and host-3 and host-4 are connected to bridge-B:

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

The {{<exlink url="http://www.ieee802.org/1/pages/802.1Q.html" text=" standard">}} for trunking is 802.1Q. The 802.1Q specification adds a four byte header within the Ethernet frame that identifies the VLAN of which the frame is a member.

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

{{< img src = "/images/cumulus-linux/ethernet-bridging-trunk1.png" >}}

To create the above example:

{{< tabs "TabID128 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge br-VLAN10 ports swp1.10,swp2.10
cumulus@switch:~$ net add bridge br-VLAN20 ports swp1.20,swp2.20
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

NVUE commands are not supported.

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
