---
title: VXLAN Routing
author: NVIDIA
weight: 610
toc: 3
---
VXLAN routing, sometimes referred to as *inter-VXLAN routing*, provides IP routing between VXLAN VNIs in overlay networks. The routing of traffic is based on the inner header or the overlay tenant IP address.

Because VXLAN routing is fundamentally routing, it is most commonly deployed with a control plane, such as Ethernet Virtual Private Network ({{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}). You can also set up static routing for MAC distribution and BUM handling.

This topic describes the platform and hardware considerations for VXLAN routing. For a detailed description of different VXLAN routing models and configuration examples, refer to {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}.

VXLAN routing supports full layer 3 multi-tenancy; all routing occurs in the context of a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}. Also, VXLAN routing is supported for dual-attached hosts where the associated VTEPs function in {{<link url="VXLAN-Active-active-Mode" text="active-active mode">}}.

## Supported Platforms

The following ASICs support VXLAN routing:

- Broadcom Trident II+, Trident3, and Maverick
- Broadcom Tomahawk and Tomahawk+, using an internal loopback on one or more switch ports
- Mellanox Spectrum

{{%notice note%}}

- Using ECMP with VXLAN routing is supported only on RIOT-capable Broadcom ASICs (Trident 3, Maverick, Trident 2+) in addition to Tomahawk, Tomahawk+ and Mellanox Spectrum-A1 ASICs.
- For additional restrictions and considerations for VXLAN routing with EVPN, refer to {{<link url="Ethernet-Virtual-Private-Network-EVPN">}}.

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

{{%notice note%}}

On Broadcom switches, high scale environments configured with VXLAN, MLAG, and bonds configured for LACP bypass mode might experience resource contention when bonds have not negotiated LACP. ARP and other broadcast traffic might experience forwarding problems when bonds remain in bypass mode.  

{{%/notice%}}

### Trident II

VXLAN routing is not supported on Trident II switches, and the external hyperloop workaround for RIOT on Trident II switches has been removed in Cumulus Linux 4.0.0. Use native VXLAN routing platforms and EVPN for network virtualization.

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

{{%link url="Configuring-switchd#restart-switchd" text="Restart `switchd`"%}} for the changes to take effect.

{{%notice note%}}

VXLAN routing with internal loopback is supported only with {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridges">}}; you cannot use a bridge in {{<link url="Traditional-Bridge-Mode" text="traditional mode">}}.

{{%/notice%}}

### Tomahawk+ and 25G Ports for Loopback

For VXLAN routing on a switch with the Tomahawk+ ASIC, if you use 25G ports as the internal loopback, you must configure all four ports in the same port group.

## VXLAN Routing Data Plane and Mellanox Spectrum ASICs

There is no special configuration required for VXLAN routing on Mellanox Spectrum ASICs.
