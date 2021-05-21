---
title: VXLAN Routing
author: NVIDIA
weight: 149
pageID: 8362747
---
VXLAN routing, sometimes referred to as *inter-VXLAN routing*, provides
IP routing between VXLAN VNIs in overlay networks. The routing of
traffic is based on the inner header or the overlay tenant IP address.

Because VXLAN routing is fundamentally routing, it is most commonly
deployed with a control plane, such as Ethernet Virtual Private Network
({{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}).
You can set up static routing too, either with or without the Cumulus
{{<link url="Lightweight-Network-Virtualization-Overview" text="Lightweight Network Virtualization">}}
(LNV) for MAC distribution and BUM handling.

This topic describes the platform and hardware considerations for VXLAN
routing. For a detailed description of different VXLAN routing models
and configuration examples, refer to
{{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}.

VXLAN routing supports full layer 3 multi-tenancy; all routing occurs in
the context of a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}.
Also, VXLAN routing is supported for dual-attached hosts where the
associated VTEPs function in {{<link url="VXLAN-Active-Active-Mode" text="active-active mode">}}.

## Supported Platforms

The following chipsets support VXLAN routing:

  - Broadcom Trident II+, Trident3, and Maverick
  - Broadcom Tomahawk and Tomahawk+, using an internal loopback on one
    or more switch ports
  - Mellanox Spectrum

{{%notice note%}}

  - Using ECMP with VXLAN routing is supported only on RIOT-capable
    Broadcom switches (Trident 3, Maverick, Trident 2+) in addition to
    Tomahawk, Tomahawk+ and Mellanox Spectrum-A1 switches.
  - For additional restrictions and considerations for VXLAN routing
    with EVPN, refer to the {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN chapter">}}.

{{%/notice%}}

## VXLAN Routing Data Plane and the Broadcom Trident II+, Trident3, Maverick, Tomahawk, and Tomahawk+ Platforms

### Trident II+, Trident3, and Maverick

The Trident II+, Trident3, and Maverick ASICs provide native support for
VXLAN routing, also referred to as Routing In and Out of Tunnels (RIOT).

You can specify a VXLAN routing profile in the
`vxlan_routing_overlay.profile` field of the
`/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf`
file to control the maximum number of overlay next hops (adjacency
entries). The profile is one of the following:

  - *default*: 15% of the underlay next hops are set apart for overlay
    (8k next hops are reserved)
  - *mode-1*: 25% of the underlay next hops are set apart for overlay
  - *mode-2*: 50% of the underlay next hops are set apart for overlay
  - *mode-3*: 80% of the underlay next hops are set apart for overlay
  - *disable*: disables VXLAN routing

The following shows an example of the *VXLAN Routing Profile* section of
the `datapath.conf` file where the *default* profile is enabled.

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

The Trident II+ and Trident3 ASICs support a maximum of 48k underlay
next hops.

For any profile you specify, you can allocate a *maximum* of 2K (2048)
VXLAN SVI interfaces.

To disable the VXLAN routing capability on a Trident II+ or Trident3
switch, set the `vxlan_routing_overlay.profile` field to *disable*.

## Tomahawk and Tomahawk+

The Tomahawk and Tomahawk+ ASICs do not support RIOT natively; you must
configure the switch ports for VXLAN routing to use internal loopback
(also referred to as *internal hyperloop)*. The internal loopback
facilitates the recirculation of packets through the ingress pipeline to
achieve VXLAN routing.

For routing **into** a VXLAN tunnel, the first pass of the ASIC performs routing
and routing rewrites of the packet MAC source and destination address and VLAN,
then packets recirculate through the internal hyperloop for VXLAN encapsulation
and underlay forwarding on the second pass.

For routing **out of** a VXLAN tunnel, the first pass performs VXLAN decapsulation,
then packets recirculate through the hyperloop for routing on the second pass.

You only need to configure a number of switch ports that must be in
internal loopback mode based on the amount of bandwidth required. No
additional configuration is necessary.

{{%notice info%}}

When one or more interfaces are used as an internal hyperloop, all front panel 25G interfaces in a port group must be configured for the same speed.

{{%/notice%}}

To configure one or more switch ports for loopback mode, edit the
`/etc/cumulus/ports.conf` file and change the port speed to *loopback*.
In the example below, swp8 and swp9 are configured for loopback mode:

    cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
    ...
     
    7=4x10G
    8=loopback
    9=loopback
    10=100G
    ...

After you save your changes to the `ports.conf` file,
{{<link url="Configuring-switchd#restart-switchd" text="restart `switchd`">}}
for the changes to take effect.

{{%notice note%}}

VXLAN routing using internal loopback is supported only with
{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridges">}};
you cannot use a bridge in
{{<link url="Traditional-Bridge-Mode" text="traditional mode">}}.

{{%/notice%}}

### Tomahawk+ and 25G Ports for Loopback

For VXLAN routing on a switch with the Tomahawk+ ASIC, if you use 25G ports as the internal loopback, you must configure all four ports in the same port group.

## VXLAN Routing Data Plane and Broadcom Trident II Platforms

{{%notice warning%}}

As of Cumulus Linux 3.7, the external hyperloop workaround for RIOT on Trident II switches has been deprecated. Support for this feature will be removed in Cumulus Linux 4.0. Use native VXLAN routing platforms and {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}} for network virtualization.

{{%/notice%}}

The Trident II ASIC does not support RIOT natively or VXLAN routing
using internal loopback. To achieve VXLAN routing in a deployment using
Trident II switches, use an external gateway. For routing without an
external gateway, you must loopback one or more switch ports using an
external loopback cable. This is also referred to as *external
hyperloop*.

{{%notice note%}}

On Broadcom Trident II switches, only static VXLAN routing is supported
with the use of external loopback.

{{%/notice%}}

External hyperloop is set up so that the port at one end of the loopback
is a layer 2 port attached to the bridge while the port at the other end
is configured with a layer 3 interface. The layer 3 interface is
configured with the gateway IP address for the corresponding VLAN/VNI.
Traffic exiting a VXLAN tunnel is bridged out the layer 2 port if it
needs to be routed (exactly as it would if it were going to an external
gateway) but at the other end, because traffic is addressed to the
gateway IP address, it gets regular routing treatment. For redundancy
and increased bandwidth, two or more pairs of ports are typically put
into an external hyperloop and bonded together.

The following diagram illustrates the configuration and operation of an
external hyperloop.

{{% img src="/images/old_doc_images/Screen-Shot-2017-03-09-at-12.39.53-PM.png" %}}

In the above diagram, VTEPs *exit01* and *exit02* are acting as VXLAN
layer 3 gateways. On *exit01*, two pairs of ports are externally looped
back (swp45, swp46) and (swp47, swp48). The ports swp46 and swp48 are
bonded together and act as the layer 2 end; therefore, this bond
interface (named *inside*) is a member of the bridge. The ports swp45
and swp47 are bonded together (named *outside*) and act as the layer 3
end with SVIs configured for VLANs 100 and 200 with the corresponding
gateway IP addresses. Because the two layer 3 gateways are in an
{{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}
configuration, they use a virtual IP address as the gateway IP. The
relevant interface configuration on *exit01* is as follows:

    ## some output removed for brevity (such as peerlink and host-facing bonds) ##
     
    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports inside server01 server02 vni-10 vni-20 peerlink
        bridge-vids 100 200
        bridge-pvid 1             # sets native VLAN to 1, an unused VLAN
        mstpctl-treeprio 8192
     
    auto outside
    iface outside
        bond-slaves swp45 swp47
        alias hyperloop outside
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
     
    auto inside
    iface inside
        bond-slaves swp46 swp48
        alias hyperloop inside
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes

    auto VLAN100GW
    iface VLAN100GW
        bridge-ports outside.100
        address 172.16.100.2/24
        address-virtual 44:38:39:FF:01:90 172.16.100.1/24
     
    auto VLAN200GW
    iface VLAN200GW
       bridge-ports outside.200
       address 172.16.200.2/24
       address-virtual 44:38:39:FF:02:90 172.16.200.1/24 
     
    auto vni-10
    iface vni-10
        vxlan-id 10
        vxlan-local-tunnelip 10.0.0.11
        bridge-access 100
     
    auto vni-20
    iface vni-20
        vxlan-id 20
        vxlan-local-tunnelip 10.0.0.11
        bridge-access 200

For the external hyperloop to work correctly, you must configure the
following `switchd` flag:

    cumulus@exit01:mgmt-vrf:/root$ sudo nano /etc/cumulus/switchd.conf
    hal.bcm.per_vlan_router_mac_lookup = TRUE

After you save your changes to the `switchd.conf` file,
{{<link url="Configuring-switchd/#restart-switchd" text="restart `switchd`">}}
for the change to take effect.

{{%notice warning%}}

Setting `hal.bcm.per_vlan_router_mac_lookup = TRUE` limits the Trident
II switch to a configurable 512 local IP addresses (SVIs and so forth),
so you should use this only as a last resort. This is only a limitation
on this specific ASIC type.

The `hal.bcm.per_vlan_router_mac_lookup` option is meant only for external
hyperloops. This option is not recommended for any other purpose or use case.

{{%/notice%}}

## VXLAN Routing Data Plane and the Mellanox Spectrum Platform

There is no special configuration required for VXLAN routing on the
Mellanox Spectrum platform.
