---
title: VXLAN Routing
author: Cumulus Networks
weight: 147
aliases:
 - /display/DOCS/VXLAN+Routing
 - /pages/viewpage.action?pageId=8366471
product: Cumulus Linux
version: '4.0'
---
VXLAN routing, sometimes referred to as *inter-VXLAN routing*, provides IP routing between VXLAN VNIs in overlay networks. The routing of traffic is based on the inner header or the overlay tenant IP address.

Because VXLAN routing is fundamentally routing, it is most commonly deployed with a control plane, such as Ethernet Virtual Private Network ([EVPN](../Ethernet-Virtual-Private-Network-EVPN/)). You can also set up static routing for MAC distribution and BUM handling.

This topic describes the platform and hardware considerations for VXLAN routing. For a detailed description of different VXLAN routing models and configuration examples, refer to [EVPN](../Ethernet-Virtual-Private-Network-EVPN/).

VXLAN routing supports full layer 3 multi-tenancy; all routing occurs in the context of a [VRF](../../Layer-3/Virtual-Routing-and-Forwarding-VRF/). Also, VXLAN routing is supported for dual-attached hosts where the associated VTEPs function in [active-active mode](../VXLAN-Active-Active-Mode/).

## Supported Platforms

The following ASICs support VXLAN routing:

- Broadcom Trident II+, Trident3, and Maverick
- Broadcom Tomahawk and Tomahawk+, using an internal loopback on one or more switch ports
- Mellanox Spectrum

{{%notice note%}}

- Using ECMP with VXLAN routing is supported only on RIOT-capable Broadcom ASICs (Trident 3, Maverick, Trident 2+) in addition to Tomahawk, Tomahawk+ and Mellanox Spectrum-A1 ASICs.
- For additional restrictions and considerations for VXLAN routing with EVPN, refer to [Ethernet Virtual Private Network - EVPN](../Ethernet-Virtual-Private-Network-EVPN/).

{{%/notice%}}

## VXLAN Routing Data Plane and Broadcom Switches

### Trident II+, Trident3, and Maverick

The Trident II+, Trident3, and Maverick ASICs provide native support for VXLAN routing, also referred to as Routing In and Out of Tunnels (RIOT).

You can specify a VXLAN routing profile in the `vxlan_routing_overlay.profile` field of the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf` file to control the maximum number of overlay next hops (adjacency entries). The profile is one of the following:

- *default*: 15% of the underlay next hops are set apart for overlay (8k next hops are reserved)
- *mode-1*: 25% of the underlay next hops are set apart for overlay
- *mode-2*: 50% of the underlay next hops are set apart for overlay
- *mode-3*: 80% of the underlay next hops are set apart for overlay
- *disable*: disables VXLAN routing

The following shows an example of the *VXLAN Routing Profile* section of the `datapath.conf` file where the *default* profile is enabled.

```
...
# Specify a VxLan Routing Profile - the profile selected determines the
# maximum number of overlay next hops that can be allocated.
# This is supported only on TridentTwoPlus and Maverick
#
# Profile can be one of {'default', 'mode-1', 'mode-2', 'mode-3', 'disable'}
# default: 15% of the overall nexthops are for overlay.
# mode-1:  25% of the overall nexthops are for overlay.
# mode-2:  50% of the overall nexthops are for overlay.
# mode-3:  80% of the overall nexthops are for overlay.
# disable: VxLan Routing is disabled
#
# By default VxLan Routing is enabled with the default profile.
vxlan_routing_overlay.profile = default
```

The Trident II+ and Trident3 ASICs support a maximum of 48k underlay next hops.

For any profile you specify, you can allocate a *maximum* of 2K (2048) VXLAN SVI interfaces.

To disable VXLAN routing on a Trident II+ or Trident3 switch, set the `vxlan_routing_overlay.profile` field to *disable*.

### Tomahawk and Tomahawk+

The Tomahawk and Tomahawk+ ASICs do not support RIOT natively; you must configure the switch ports for VXLAN routing to use internal loopback (also referred to as *internal hyperloop)*. The internal loopback facilitates the recirculation of packets through the ingress pipeline to achieve VXLAN routing.

For routing **into** a VXLAN tunnel, the first pass of the ASIC performs routing and routing rewrites of the packet MAC source, destination address, and VLAN, then packets recirculate through the internal hyperloop for VXLAN encapsulation and underlay forwarding on the second pass.

For routing **out of** a VXLAN tunnel, the first pass performs VXLAN decapsulation, then packets recirculate through the hyperloop for routing on the second pass.

You only need to configure the switch ports that must be in internal loopback mode based on the amount of bandwidth required. No additional configuration is necessary.

To configure one or more switch ports for loopback mode, edit the `/etc/cumulus/ports.conf` file and change the port speed to *loopback*. In the example below, swp8 and swp9 are configured for loopback mode:

```
cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
...
7=4x10G
8=loopback
9=loopback
10=100G
...
```

[Restart `switchd`](../../System-Configuration/Configuring-switchd#restart-switchd) for the changes to take effect.

{{%notice note%}}

VXLAN routing with internal loopback is supported only with [VLAN-aware bridges](../../Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/); you cannot use a bridge in [traditional mode](../../Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/).

{{%/notice%}}

## VXLAN Routing Data Plane and the Mellanox Spectrum ASIC

There is no special configuration required for VXLAN routing on the Mellanox Spectrum ASIC.
