---
title: Traditional Bridge Mode
author: NVIDIA
weight: 460
toc: 4
---
Use a {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}} on your switch. Use traditional mode bridges only if you need to run more than one bridge on the switch or if you need to use PVSTP+.

## Configure a Traditional Mode Bridge

The following examples show how to create a simple traditional mode bridge configuration on the switch. The example also shows some optional elements:

- You can add an IP address to provide IP access to the bridge interface.
- You can specify a range of interfaces.

To configure spanning tree options for a bridge interface, refer to {{<link title="Spanning Tree and Rapid Spanning Tree">}}.

{{< tabs "TabID0" >}}

{{< tab "NCLU Commands" >}}

The following example commands configure a traditional mode bridge called my\_bridge with IP address 10.10.10.10/24. swp1, swp2, swp3, and swp4 are members of the bridge.

```
cumulus@switch:~$ net add bridge my_bridge ports swp1-4
cumulus@switch:~$ net add bridge my_bridge ip address 10.10.10.10/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands" >}}

Edit the `/etc/network/interfaces` file. The following example command configures a traditional mode bridge called my\_bridge with IP address 10.10.10.10/24. swp1, swp2, swp3, and swp4 are members of the bridge.

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

Run the `ifreload -a` command to reload the network configuration:

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

The name of the bridge must be:

- Compliant with Linux interface naming conventions.
- Unique within the switch.
- Something other than *bridge*, **** as Cumulus Linux reserves that name for a single {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge">}}.

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

802.1Q also identifies an *untagged* frame as belonging to the *native* VLAN (most network devices default their native VLAN to 1). The concept of native, non-native, tagged or untagged has generated confusion due to mixed terminology and vendor-specific implementations. In Cumulus Linux:

- A *trunk port* is a switch port configured to send and receive 802.1Q tagged frames.
- A switch sending an untagged (bare Ethernet) frame on a trunk port is sending from the native VLAN defined on the trunk port.
- A switch sending a tagged frame on a trunk port is sending to the VLAN identified by the 802.1Q tag.
- A switch receiving an untagged (bare Ethernet) frame on a trunk port places that frame in the native VLAN defined on the trunk port.
- A switch receiving a tagged frame on a trunk port places that frame in the VLAN identified by the 802.1Q tag.

A bridge in traditional mode has no concept of trunks, just tagged or untagged frames. With a trunk of 200 VLANs, there would need to be 199 bridges, each containing a tagged physical interface, and one bridge containing the native untagged VLAN. See the examples below for more information.

{{%notice note%}}

The interaction of tagged and un-tagged frames on the same trunk often leads to undesired and unexpected behavior. A switch that uses VLAN 1 for the native VLAN may send frames to a switch that uses VLAN 2 for the native VLAN, thus merging those two VLANs and their spanning tree state.

{{%/notice%}}

### Trunk Example

{{< img src = "/images/cumulus-linux/ethernet-bridging-trunk.png" >}}

To create the above example:

{{< tabs "TabID138 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bridge br-VLAN100 ports swp1.100,swp2.100
cumulus@switch:~$ net add bridge br-VLAN200 ports swp1.200,swp2.200
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux Commands ">}}

Add the following configuration to the `/etc/network/interfaces` file:

```
...
auto br-VLAN100
iface br-VLAN100
   bridge-ports swp1.100 swp2.100

auto br-VLAN200
iface br-VLAN200
   bridge-ports swp1.200 swp2.200
...
```

{{< /tab >}}

{{< /tabs >}}

### VLAN Tagging Examples

You can find more examples of VLAN tagging in {{<link url="VLAN-Tagging" text="the VLAN tagging chapter">}}.

## Caveats

On Broadcom switches, when two VLAN subinterfaces are bridged to each other in a traditional mode bridge, `switchd` does not assign an internal resource ID to the subinterface, which is expected for each VLAN subinterface. To work around this issue, add a VXLAN on the bridge so that it does not require a real tunnel IP address.
