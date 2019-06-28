---
title: VXLAN Routing
author: Cumulus Networks
weight: 145
aliases:
 - /display/CL35/VXLAN+Routing
 - /pages/viewpage.action?pageId=8357513
pageID: 8357513
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
VXLAN routing, sometimes referred to as *inter-VXLAN routing*, provides
IP routing between VXLAN VNIs in overlay networks. The routing of
traffic is based on the inner header or the overlay tenant IP address.

Because VXLAN routing is fundamentally routing, it is most commonly
deployed with a control plane, such as Ethernet Virtual Private Network
([EVPN](/version/cumulus-linux-35/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN)).
You can set up static routing too, either with or without the Cumulus
[Lightweight Network
Virtualization](/version/cumulus-linux-35/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/)
(LNV) for MAC distribution and BUM handling.

This chapter describes the platform and hardware considerations for
VXLAN routing. For a detailed description of different VXLAN routing
models and configuration examples, refer to [the EVPN
chapter](/version/cumulus-linux-35/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN).

VXLAN routing supports full layer 3 multi-tenancy; all routing occurs in
the context of a
[VRF](/version/cumulus-linux-35/Layer_3/Virtual_Routing_and_Forwarding_-_VRF).
Also, VXLAN routing is supported for dual-attached hosts where the
associated VTEPs function in [active-active
mode](/version/cumulus-linux-35/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode).

## <span>Supported Platforms</span>

The following chipsets support VXLAN routing:

  - Broadcom Trident II+ and Maverick

  - Broadcom Tomahawk, using an internal loopback on one or more switch
    ports

  - Broadcom Trident II, static VXLAN routing only, using an external
    loopback on one or more switch ports

  - Mellanox Spectrum

{{%notice note%}}

  - Using ECMP with VXLAN routing is supported only on Broadcom Tomahawk
    and Mellanox Spectrum switches.

  - For additional restrictions and considerations for VXLAN routing
    with EVPN, refer to [the EVPN
    chapter](/version/cumulus-linux-35/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN).

{{%/notice%}}

## <span>VXLAN Routing Data Plane and the Broadcom Trident II+, Maverick and Tomahawk Platforms</span>

### <span>Trident II+ and Maverick</span>

The Trident II+ and Maverick ASICs provide native support for VXLAN
routing, also referred to as Routing In and Out of Tunnels (RIOT).

You can specify a VXLAN routing profile in the
`vxlan_routing_overlay.profile` field of the
`/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf`
file to control the maximum number of overlay next hops (adjacency
entries). The profile is one of the following:

  - *default*: 15% of the underlay next hops are set apart for overlay
    (8k next hops <span style="color: #222222;"> are reserved) </span>

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

The Trident II+ ASIC supports a maximum of 48k underlay next hops.

For any profile you specify, you can allocate a *maximum* of 2K (2048)
VXLAN SVI interfaces.

To disable the VXLAN routing capability on a Trident II+ switch, set the
`vxlan_routing_overlay.profile` field to *disable*.

### <span>Tomahawk</span>

The Tomahawk ASIC does not support RIOT natively; you must configure the
switch ports for VXLAN routing to use internal loopback (also referred
to as *internal hyperloop)*. The internal loopback facilitates the
recirculation of packets through the ingress pipeline to achieve VXLAN
routing.

F <span style="color: #222222;"> or routing **into** a VXLAN tunnel, the
first pass of the ASIC performs routing and routing rewrites of the
packet MAC source and destination address and VLAN, then packets
recirculate through the internal hyperloop for VXLAN encapsulation and
underlay forwarding on the second pass. </span>

<span style="color: #222222;"> For routing **out of** a VXLAN tunnel,
the first pass performs VXLAN decapsulation, then packets recirculate
through the hyperloop for routing on the second pass. </span>

You only need to configure a number of switch ports that must be in
internal loopback mode based on the amount of bandwidth required. No
additional configuration is necessary.

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

After you save your changes to the `ports.conf` file, [restart
`switchd`](Configuring_switchd.html#src-8357343_Configuringswitchd-restartswitchd)
for the changes to take effect.

{{%notice note%}}

VXLAN routing using internal loopback is supported only with [VLAN-aware
bridges](/version/cumulus-linux-35/Layer_1_and_2/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments);
you cannot use a bridge in [traditional
mode](/version/cumulus-linux-35/Layer_1_and_2/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges).

{{%/notice%}}

## <span id="src-8357513_VXLANRouting-t2" class="confluence-anchor-link"></span><span>VXLAN Routing Data Plane and Broadcom Trident II Platforms</span>

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

{{% imgOld 0 %}}

In the above diagram, VTEPs *exit01* and *exit02* are acting as VXLAN
layer 3 gateways. On *exit01*, two pairs of ports are externally looped
back (swp45, swp46) and (swp47, swp48). The ports swp46 and swp48 are
bonded together and act as the layer 2 end; therefore, this bond
interface (named *inside*) is a member of the bridge. The ports swp45
and swp47 are bonded together (named *outside*) and act as the layer 3
end with SVIs configured for VLANs 100 and 200 with the corresponding
gateway IP addresses. Because the two layer 3 gateways are in an
[MLAG](/version/cumulus-linux-35/Layer_1_and_2/Multi-Chassis_Link_Aggregation_-_MLAG)
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
        bridge_ports outside.100
        address 172.16.100.2/24
        address-virtual 44:38:39:FF:01:90 172.16.100.1/24
     
    auto VLAN200GW
    iface VLAN200GW
       bridge_ports outside.200
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

After you save your changes to the `switchd.conf` file, [restart
`switchd`](Configuring_switchd.html#src-8357343_Configuringswitchd-restartswitchd)
for the change to take effect.

{{%notice warning%}}

Setting `hal.bcm.per_vlan_router_mac_lookup = TRUE` limits the Trident
II switch to a configurable 512 local IP addresses (SVIs and so on). Use
this only as a last resort. This is only a limitation on this specific
ASIC.

{{%/notice%}}

## <span>VXLAN Routing Data Plane and the Mellanox Spectrum Platform</span>

There is no special configuration required for VXLAN routing on the
Mellanox Spectrum platform.
