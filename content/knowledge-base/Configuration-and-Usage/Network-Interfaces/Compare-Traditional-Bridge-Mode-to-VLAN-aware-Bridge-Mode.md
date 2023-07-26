---
title: Compare Traditional Bridge Mode to VLAN-aware Bridge Mode
author: NVIDIA
weight: 411
toc: 4
---

The Cumulus Linux bridge driver operates in two modes:
[VLAN-aware]({{<ref "/cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode" >}}) and a [traditional Linux mode]({{<ref "/cumulus-linux-43/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode" >}}). There are many minor syntax differences between the two modes, outlined below. However, the following behaviors apply no matter which mode you use for the driver:

- Network interfaces configuration is in the `/etc/network/interfaces` file.
- Both modes support [Spanning Tree Protocol]({{<ref "/cumulus-linux-43/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}}) (see the example below).
- You manage interfaces configured with both modes with `ifupdown` commands (`ifup bridge`, `ifdown bridge`).

The reasons why you would use VLAN-aware mode for bridges are:

- **Scale:** The VLAN-aware mode can support 2000 concurrent VLANs while the traditional mode supports only 200 concurrent VLANs.
- **Simplicity:** VLAN-aware mode has a simpler configuration.

The only reasons to use the traditional mode are:

- Familiarity with traditional Linux syntax.
- **VXLAN support:** As of Cumulus Linux 3.1, only VLAN-aware mode supports VXLANs. For VXLAN support on earlier releases, use traditional mode.
- **PVSTP+ interoperability:** The traditional mode currently runs an instance of spanning tree per bridge. The VLAN-aware STP mode is compatible with other types of spanning tree but only runs single instance MST. To achieve Per-VLAN STP/RSTP you must use the traditional bridge mode.

## Two Trunks Containing 200 VLANs for swp1 and swp2

| Traditional | VLAN-aware |
| ----------- | ---------- |
| <pre>auto br-vlan1<br>iface br-vlan1<br>  bridge-ports swp1 swp2<br><br>auto br-vlan2<br>iface br-vlan2<br>  bridge-ports swp1.2 swp2.2<br><br>auto br-vlan3<br>iface br-vlan3<br>  bridge-ports swp1.3 swp2.3<br> .<br> .<br><br>auto br-vlan200<br>iface br-vlan200<br>  bridge-ports swp1.200 swp2.200</pre> | <pre>auto bridge<br><br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports swp1 swp2<br>  bridge-vids 1-200<br>  bridge-pvid 1</pre> |

{{%notice note%}}
<!-- vale off -->
The output above is abbreviated. If you are creating a trunk in traditional mode, you must create 200 stanzas for the 200 interfaces. Remember, a bridge configured in traditional mode cannot have more than 200 VLANs.
<!-- vale on -->
{{%/notice%}}

## Creating an SVI

An SVI is a switch VLAN/virtual interface, also known as a layer 3 VLAN interface.

| Traditional | VLAN-aware |
| ----------- | ---------- |
| <pre>auto bridge<br>iface bridge<br>  bridge-ports swp1.10 swp2.10 address 192.168.10.1/24 address 2001:db8::1/32</pre> | <pre><code>auto bridge<br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports swp1 swp2<br>  bridge-vids 1-200<br>  bridge-pvid 1<br><br>auto bridge.10<br>iface bridge.10<br>  address 192.168.10.1/24<br>  address 2001:db8::1/32</pre> |

{{%notice note%}}

The comparison above is not exactly apples to apples. If the traditional mode configuration was the only configuration applied to the switch, you would only have VLAN 10 traffic for swp1 and swp2 as indicated by the tags. However the VLAN-aware bridge driver has two trunks for 200 VLANs. This behavior is very different.

{{%/notice%}}

## Creating Access Ports (AKA Untagged Ports)

| Traditional | VLAN-aware |
| ----------- | ---------- |
| <pre>auto bridge<br>iface bridge<br>  bridge-ports swp1 swp2</pre> |  <pre>auto bridge<br>iface bridge<br>  bridge-vlan-aware yes<br>  bridge-ports swp1 swp2<br>  bridge-vids 1-200<br>  bridge-pvid 1<br><br>auto swp1<br>iface swp1<br>  bridge-access 10<br><br>auto swp2<br>iface swp2<br>  bridge-access 10</pre> |

{{%notice note%}}

The above illustrates how the traditional mode has no concept of VLANs, just untagged or tagged traffic. It\'s basically identical to the previous example except there is no `.10` after the switch ports here.

{{%/notice%}}

## Two Trunks Containing Two VLANs with Spanning Tree Enabled

| Traditional | VLAN-aware |
| ----------- | ---------- |
| <pre>auto br-vlan100<br><br>iface br-vlan100<br>    bridge-ports swp1.100 swp2.100 bridge-stp on<br><br>auto br-vlan200<br>iface br-vlan200<br>    bridge-ports swp1.200 swp2.200 bridge-stp on</pre> | <pre>auto bridge<br><br>iface bridge<br>    bridge-vlan-aware yes<br>    bridge-ports swp1 swp2<br>    bridge-vids 100 200<br>    bridge-stp on</pre> |

{{%notice note%}}

The `bridge-stp on` option is identical for the two modes; however, you only need to specify it one time for VLAN-aware bridge mode.

{{%/notice%}}
