---
title: Ethernet Virtual Private Network - EVPN
author: Cumulus Networks
weight: 143
aliases:
 - /display/DOCS/Ethernet+Virtual+Private+Network+-+EVPN
 - /pages/viewpage.action?pageId=8362732
pageID: 8362732
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
VXLAN is the de facto technology for implementing network virtualization
in the data center, enabling layer 2 segments to be extended over an IP
core (the underlay). The initial definition of VXLAN
([RFC 7348](https://tools.ietf.org/html/rfc7348)) did not include any
control plane and relied on a flood-and-learn approach for MAC address
learning. An alternate deployment model was to use a controller or a
technology such as [Lightweight Network Virtualization
(LNV)](/display/DOCS/Lightweight+Network+Virtualization+-+LNV+Overview)
in Cumulus Linux.

{{%notice note%}}

  - You cannot use EVPN and LNV at the same time.

  - When using EVPN, you *must* disable data plane MAC learning on all
    VXLAN interfaces. This is described in [Basic EVPN
    Configuration](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-BasicEVPNConfiguration),
    below.

{{%/notice%}}

Ethernet Virtual Private Network (EVPN) is a standards-based control
plane for VXLAN defined in
[RFC 7432](https://tools.ietf.org/html/rfc7432) and
[draft-ietf-bess-evpn-overlay](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-overlay/)
that allows for building and deploying VXLANs at scale. It relies on
multi-protocol BGP (MP-BGP) for exchanging information and is based on
BGP-MPLS IP VPNs ([RFC 4364](https://tools.ietf.org/html/rfc4364)). It
has provisions to enable not only bridging between end systems in the
same layer 2 segment but also routing between different segments
(subnets). There is also inherent support for multi-tenancy. EVPN is
often referred to as the means of implementing *controller-less VXLAN*.

Cumulus Linux fully supports EVPN as the control plane for VXLAN,
including for both intra-subnet bridging and inter-subnet routing. Key
features include:

  - VNI membership exchange between VTEPs using EVPN type-3 (Inclusive
    multicast Ethernet tag) routes.

  - Exchange of host MAC and IP addresses using EVPN type-2 (MAC/IP
    advertisement) routes.

  - Support for host/VM mobility (MAC and IP moves) through exchange of
    the MAC Mobility Extended community.

  - Support for dual-attached hosts via [VXLAN active-active
    mode](/cumulus-linux/Network_Virtualization/VXLAN_Active-Active_Mode).
    MAC synchronization between the peer switches is done using
    [MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG).

  - Support for ARP/ND suppression, which provides VTEPs with the
    ability to suppress ARP flooding over VXLAN tunnels.

  - Support for exchange of static (sticky) MAC addresses through EVPN.

  - Support for distributed symmetric routing between different subnets.

  - Support for distributed asymmetric routing between different
    subnets.

  - Support for centralized routing.

  - Support for prefix-based routing using EVPN type-5 routes (EVPN IP
    prefix route)

  - Support for layer 3 multi-tenancy.

  - Support for IPv6 tenant routing.

  - Symmetric routing, asymmetric routing and prefix-based routing are
    supported for both IPv4 and IPv6 hosts and prefixes.

  - ECMP (equal cost multipath) support for overlay networks on
    RIOT-capable Broadcom switches (Trident 3, Maverick, Trident 2+) in
    addition to Tomahawk and Mellanox Spectrum-A1 switches. No
    configuration is needed, ECMP occurs in the overlay when there are
    multiple next hops.

EVPN address-family is supported with both eBGP and iBGP peering. If the
underlay routing is provisioned using eBGP, the same eBGP session can
also be used to carry EVPN routes. For example, in a typical 2-tier Clos
network topology where the leaf switches are the VTEPs, if eBGP sessions
are in use between the leaf and spine switches for the underlay routing,
the same sessions can be used to exchange EVPN routes; the spine
switches merely act as "route forwarders" and do not install any
forwarding state as they are not VTEPs. When EVPN routes are exchanged
over iBGP peering, OSPF can be used as the IGP or the next hops can also
be resolved using iBGP.

You can provision and manage EVPN using
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU).

{{%notice note%}}

For Cumulus Linux 3.4 and later releases, the routing control plane
(including EVPN) is installed as part of the
[FRRouting](https://frrouting.org/) (FRR) package. For more information
about FRR, refer to the [FRR
Overview](/cumulus-linux/Layer_3/FRRouting_Overview/).

{{%/notice%}}

For information about VXLAN routing, including platform and hardware
limitations, see [VXLAN
Routing](/cumulus-linux/Network_Virtualization/VXLAN_Routing).

## <span>Basic EVPN Configuration</span>

The following steps represent the fundamental configuration to use EVPN
as the control plane for VXLAN. These steps are in addition to
configuring VXLAN interfaces, attaching them to a bridge, and mapping
VLANs to VNIs.

1.  Enable EVPN route exchange (that is, address-family layer 2
    VPN/EVPN) between BGP peers.

2.  Enable EVPN on the system to advertise VNIs and host reachability
    information (MAC addresses learned on associated VLANs) to BGP
    peers.

3.  Disable MAC learning on VXLAN interfaces as EVPN is responsible for
    installing remote MACs.

Additional configuration is necessary to enable ARP/ND suppression,
provision inter-subnet routing, and so on. The configuration depends on
the deployment scenario. You can also configure various other BGP
parameters.

### <span>Enable EVPN between BGP Neighbors</span>

You enable EVPN between
[BGP](/cumulus-linux/Layer_3/Border_Gateway_Protocol_-_BGP) neighbors by
adding the address family *evpn* to the existing neighbor address-family
activation command.

For a non-VTEP device that is merely participating in EVPN route
exchange, such as a spine switch (the network deployment uses hop-by-hop
eBGP or the switch is acting as an iBGP route reflector), activating the
interface for the EVPN address family is the fundamental configuration
needed in [FRRouting](/cumulus-linux/Layer_3/FRRouting_Overview/).
Additional configuration options for specific scenarios are described
later on in this chapter.

The other BGP neighbor address-family-specific configurations supported
for EVPN are `allowas-in` and `route-reflector-client`.

To configure an EVPN route exchange with a BGP peer, you must activate
the peer or peer-group within the EVPN address-family:

    cumulus@switch:~$ net add bgp autonomous-system 65000
    cumulus@switch:~$ net add bgp neighbor swp1 interface remote-as external
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp1 activate
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Adjust the `remote-as` above to be appropriate for your environment.

{{%/notice%}}

{{%notice note%}}

The command syntax `bgp evpn` is also permitted for backwards
compatibility with prior versions of Cumulus Linux, but the syntax `bgp
l2vpn evpn` is recommended to standardize the BGP address-family
configuration to the AFI/SAFI format.

{{%/notice%}}

The above commands create the following configuration snippet in the
`/etc/frr/frr.conf` file.

    router bgp 65000
     neighbor swp1 interface remote-as external
     address-family l2vpn evpn
      neighbor swp1 activate

The above configuration does not result in BGP knowing about the local
VNIs defined on the system and advertising them to peers. This requires
additional configuration, [as described
below](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-allvnis).

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-allvnis" class="confluence-anchor-link"></span><span>Advertise All VNIs</span>

A single configuration variable enables the BGP control plane for all
VNIs configured on the switch. Set the variable `advertise-all-vni` to
provision all locally configured VNIs to be advertised by the BGP
control plane. FRR is not aware of any local VNIs and MACs and hosts
(neighbors) associated with those VNIs until `advertise-all-vni` is
configured.

To build upon the previous example, run the following commands to
advertise all VNIs:

    cumulus@switch:~$ net add bgp autonomous-system 65000
    cumulus@switch:~$ net add bgp neighbor swp1 interface remote-as external
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp1 activate 
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Adjust the `remote-as` above to be appropriate for your environment.

{{%/notice%}}

The above commands create the following configuration snippet in the
`/etc/frr/frr.conf` file.

    router bgp 65000
     neighbor swp1 interface remote-as external
     address-family l2vpn evpn
      neighbor swp1 activate
      advertise-all-vni

{{%notice note%}}

This configuration is only needed on leaf switches that are VTEPs. EVPN
routes received from a BGP peer are accepted, even without this explicit
EVPN configuration. These routes are maintained in the global EVPN
routing table. However, they only become effective (that is, imported
into the per-VNI routing table and appropriate entries installed in the
kernel) when the VNI corresponding to the received route is locally
known.

{{%/notice%}}

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-RD-auto-derivation" class="confluence-anchor-link"></span><span>Auto-derivation of RDs and RTs</span>

When a local VNI is learned by FRR and there is no explicit
configuration for that VNI in FRR, the route distinguisher (RD) and
import and export route targets (RTs) for this VNI are automatically
derived — the RD uses “RouterId:VNI-Index” and the import and export RTs
use “AS:VNI”. The RD and RTs are used in the EVPN route exchange. The RD
disambiguates EVPN routes in different VNIs (as they may have the same
MAC and/or IP address) while the RTs describe the VPN membership for the
route. The "VNI-Index" used for the RD is a unique, internally generated
number for a VNI. It solely has local significance; on remote switches,
its only role is for route disambiguation. This number is used instead
of the VNI value itself because this number has to be less than or equal
to 65535. In the RT, the AS part is always encoded as a 2-byte value to
allow room for a large VNI. If the router has a 4-byte AS, only the
lower 2 bytes are used. This ensures a unique RT for different VNIs
while having the same RT for the same VNI across routers in the same AS.

For eBGP EVPN peering, the peers are in a different AS so using an
automatic RT of "AS:VNI" does not work for route import. Therefore, the
import RT is treated as "\*:VNI" to determine which received routes are
applicable to a particular VNI. This only applies when the import RT is
auto-derived and not configured.

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-RD-user-defined" class="confluence-anchor-link"></span><span>User-defined RDs and RTs</span>

EVPN also supports manual configuration of RDs and RTs, if you don't
want them derived automatically. To manually define RDs and RTs, use the
`vni` option within NCLU to configure the switch:

    cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 rd 172.16.100.1:20
    cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 route-target import 65100:20
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/frr/frr.conf` file.

``` 
 address-family l2vpn evpn
  advertise-all-vni
  vni 10200
   rd 172.16.100.1:20
   route-target import 65100:20
```

{{%notice note%}}

These commands are per VNI and must be specified under `address-family
l2vpn evpn` in BGP.

{{%/notice%}}

{{%notice note%}}

If you delete the RD or RT later, it reverts back to its corresponding
default value.

{{%/notice%}}

You can configure multiple RT values for import or export for a VNI. In
addition, you can configure both the import and export route targets
with a single command by using `route-target both`:

    cumulus@switch:~$ net add bgp evpn vni 10400 route-target import 100:400
    cumulus@switch:~$ net add bgp evpn vni 10400 route-target import 100:500
    cumulus@switch:~$ net add bgp evpn vni 10500 route-target both 65000:500
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The above commands create the following configuration snippet in the
`/etc/frr/frr.conf` file:

    address-family l2vpn evpn
      vni 10400
        route-target import 100:400
        route-target import 100:500
      vni 10500
        route-target import 65000:500
        route-target export 65000:500

### <span>Enable EVPN in an iBGP Environment with an OSPF Underlay</span>

EVPN can be deployed with an
[OSPF](/cumulus-linux/Layer_3/Open_Shortest_Path_First_-_OSPF) or static
route underlay if needed. This is a more complex configuration than
using eBGP. In this case, iBGP advertises EVPN routes directly between
VTEPs, and the spines are unaware of EVPN or BGP.

The leaf switches peer with each other in a full mesh within the EVPN
address family without using route reflectors. The leafs generally peer
to their loopback addresses, which are advertised in OSPF. The receiving
VTEP imports routes into a specific VNI with a matching route target
community.

    cumulus@switch:~$ net add bgp autonomous-system 65020
    cumulus@switch:~$ net add bgp evpn neighbor 10.1.1.2 remote-as internal
    cumulus@switch:~$ net add bgp evpn neighbor 10.1.1.3 remote-as internal
    cumulus@switch:~$ net add bgp evpn neighbor 10.1.1.4 remote-as internal
    cumulus@switch:~$ net add bgp evpn neighbor 10.1.1.2 activate 
    cumulus@switch:~$ net add bgp evpn neighbor 10.1.1.3 activate 
    cumulus@switch:~$ net add bgp evpn neighbor 10.1.1.4 activate 
    cumulus@switch:~$ net add bgp evpn advertise-all-vni
    cumulus@switch:~$ net add ospf router-id 10.1.1.1
    cumulus@switch:~$ net add loopback lo ospf area 0.0.0.0
    cumulus@switch:~$ net add ospf passive-interface lo
    cumulus@switch:~$ net add interface swp50 ospf area 0.0.0.0
    cumulus@switch:~$ net add interface swp51 ospf area 0.0.0.0
    cumulus@switch:~$ net add interface swp50 ospf network point-to-point
    cumulus@switch:~$ net add interface swp51 ospf network point-to-point
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/frr/frr.conf` file.

    interface lo
     ip ospf area 0.0.0.0
    !
    interface swp50
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     
    interface swp51
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
    !
    router bgp 65020
     neighbor 10.1.1.2 remote-as internal
     neighbor 10.1.1.3 remote-as internal
     neighbor 10.1.1.4 remote-as internal
     !
     address-family l2vpn evpn
      neighbor 10.1.1.2 activate
      neighbor 10.1.1.3 activate
      neighbor 10.1.1.4 activate
      advertise-all-vni
     exit-address-family
     !
    Router ospf
        Ospf router-id 10.1.1.1
        Passive-interface lo

### <span>Disable Data Plane MAC Learning over VXLAN Tunnels</span>

When EVPN is provisioned, you must disable data plane MAC learning for
VXLAN interfaces because the purpose of EVPN is to exchange MACs between
VTEPs in the control plane. In the `/etc/network/interfaces` file,
configure the `bridge-learning` value to *off*:

    cumulus@switch:~$ net add vxlan vni200 vxlan id 10200
    cumulus@switch:~$ net add vxlan vni200 vxlan local-tunnelip 10.0.0.1
    cumulus@switch:~$ net add vxlan vni200 bridge access 200
    cumulus@switch:~$ net add vxlan vni200 bridge learning off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet in the
`/etc/network/interfaces` file:

    auto vni200
    iface vni200
        bridge-access 200
        bridge-learning off
        vxlan-id 10200
        vxlan-local-tunnelip 10.0.0.1

{{%notice tip%}}

For a bridge in [traditional
mode](/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/Traditional_Bridge_Mode),
you must edit the bridge configuration in the `/etc/network/interfaces`
file using a text editor:

    auto bridge1
    iface bridge1
        bridge-ports swp3.100 swp4.100 vni100
        bridge-learning vni100=off

{{%/notice%}}

{{%notice note%}}

For a traditional-mode bridge on Broadcom switches, the `bridge
learning` setting is per physical port; you *cannot* control MAC
learning behavior based on subinterface. For example, you cannot set
`bridge learning off` on some subinterfaces and `on` for other
subinterfaces of the same physical interface.

{{%/notice%}}

{{%notice note%}}

Cumulus Linux does not support different `bridge-learning` settings for
different VNIs of VXLAN tunnels between 2 VTEPs.

{{%/notice%}}

### <span>BUM Traffic and Head End Replication</span>

<span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-head-end"></span>
<span style="color: #333333;"> With EVPN, the only method of generating
BUM traffic in hardware is *head end replication*. Head end replication
is enabled by default in Cumulus Linux. </span>

Broadcom switches with Tomahawk, Trident3, Trident II+, and Trident II
ASICs and Mellanox switches with Spectrum ASICs are capable of head end
replication. The most scalable solution available with EVPN is to have
each VTEP (top of rack switch) generate all of its own BUM traffic
instead of relying on an external service node.

Cumulus Linux supports up to 128 VTEPs with head end replication.

## <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-arp" class="confluence-anchor-link"></span><span>ARP and ND Suppression</span>

ARP suppression in an EVPN context refers to the ability of a VTEP to
suppress ARP flooding over VXLAN tunnels as much as possible. Instead, a
local proxy handles ARP requests received from locally attached hosts
for remote hosts. ARP suppression is the implementation for IPv4; ND
suppression is the implementation for IPv6.

{{%notice note%}}

Cumulus Networks recommends that you *enable* ARP and ND suppression in
all EVPN bridging and symmetric routing deployments to reduce flooding
of ARP/ND packets over VXLAN tunnels.

{{%/notice%}}

{{%notice note%}}

On switches with the Mellanox Spectrum chipset, ND suppression only
functions with the Spectrum A1 chip.

{{%/notice%}}

ARP and ND suppression are not enabled by default. You configure ARP/ND
suppression on a VXLAN interface. You also need to create an SVI for the
neighbor entry.

{{%notice tip%}}

When ARP and ND suppression are enabled, you need to configure layer 3
interfaces even if the switch is configured only for layer 2 (that is,
you are not using VXLAN routing). To avoid unnecessary layer 3
information from being installed, Cumulus Networks recommends you
configure the `ip forward off` or `ip6 forward off` options as
appropriate on the VLANs. See the example configuration below.

{{%/notice%}}

To configure ARP or ND suppression, use
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU).
Here is an example configuration using two VXLANs (10100 and 10200) and
two VLANs (100 and 200).

    cumulus@switch:~$ net add bridge bridge ports vni100,vni200
    cumulus@switch:~$ net add bridge bridge vids 100,200
    cumulus@switch:~$ net add vxlan vni100 vxlan id 10100
    cumulus@switch:~$ net add vxlan vni200 vxlan id 10200
    cumulus@switch:~$ net add vxlan vni100 bridge learning off
    cumulus@switch:~$ net add vxlan vni200 bridge learning off
    cumulus@switch:~$ net add vxlan vni100 bridge access 100
    cumulus@switch:~$ net add vxlan vni100 bridge arp-nd-suppress on
    cumulus@switch:~$ net add vxlan vni200 bridge arp-nd-suppress on
    cumulus@switch:~$ net add vxlan vni200 bridge access 200
    cumulus@switch:~$ net add vxlan vni100 vxlan local-tunnelip 10.0.0.1
    cumulus@switch:~$ net add vxlan vni200 vxlan local-tunnelip 10.0.0.1
    cumulus@switch:~$ net add vlan 100 ip forward off
    cumulus@switch:~$ net add vlan 100 ipv6 forward off
    cumulus@switch:~$ net add vlan 200 ip forward off
    cumulus@switch:~$ net add vlan 200 ipv6 forward off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-ports vni100 vni200
        bridge-stp on
        bridge-vids 100 200
        bridge-vlan-aware yes
     
    auto vlan100
    iface vlan100
        ip6-forward off
        ip-forward off
        vlan-id 100
        vlan-raw-device bridge
     
    auto vlan200
    iface vlan200
        ip6-forward off
        ip-forward off
        vlan-id 200
        vlan-raw-device bridge
     
    auto vni100
    iface vni100
        bridge-access 100
        bridge-arp-nd-suppress on
        bridge-learning off
        vxlan-id 10100
        vxlan-local-tunnelip 10.0.0.1
     
    auto vni200
    iface vni200
         bridge-learning off
         bridge-access 200
         bridge-arp-nd-suppress on
         vxlan-id 10200
         vxlan-local-tunnelip 10.0.0.1

{{%notice tip%}}

For a bridge in [traditional
mode](/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/Traditional_Bridge_Mode),
you must edit the bridge configuration in the `/etc/network/interfaces`
file using a text editor:

    auto bridge1
    iface bridge1
        bridge-ports swp3.100 swp4.100 vni100
        bridge-learning vni100=off
        bridge-arp-nd-suppress vni100=on
        ip6-forward off
        ip-forward off 

{{%/notice%}}

### <span>UFT Profiles Other than the Default</span>

When deploying EVPN and VXLAN using a hardware profile other than the
default UFT profile, ensure that the Linux kernel ARP sysctl settings
`gc_thresh2` and `gc_thresh3` are both set to a value larger than the
number of neighbor (ARP/ND) entries anticipated in the deployment.

To configure these settings, edit the `/etc/sysctl.d/neigh.conf` file.
If your network has more hosts than the values used in the example
below, change the sysctl entries accordingly.

    cumulus@switch:~$ sudo nano /etc/sysctl.d/neigh.conf
    ...
    net.ipv4.neigh.default.gc_thresh3=14336
    net.ipv6.neigh.default.gc_thresh3=16384
    net.ipv4.neigh.default.gc_thresh2=7168
    net.ipv6.neigh.default.gc_thresh2=8192
    ...

After you save your settings, reboot the switch to apply the new
configuration.

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-ND_extended_community" class="confluence-anchor-link"></span><span>Support for EVPN Neighbor Discovery (ND) Extended Community</span>

In an EVPN VXLAN deployment with ARP and ND suppression where the VTEPs
are only configured for layer 2, EVPN needs to carry additional
information for the attached devices so proxy ND can provide the correct
information to attached hosts. Without this information, hosts might not
be able to configure their default routers or might lose their existing
default router information.  
Cumulus Linux supports the EVPN Neighbor Discovery (ND) Extended
Community with a type field value of 0x06, a sub-type field value of
0x08 (ND Extended Community), and a router flag; this enables the switch
to determine if a particular IPv6-MAC pair belongs to a host or a
router.

#### <span>Router Flag</span>

The router flag (R-bit) is used in following scenarios:

  - In a centralized VXLAN routing configuration with a gateway router.

  - In a layer 2 switch deployment with ARP/ND suppression.

When the MAC/IP (type-2) route contains the IPv6-MAC pair and the R-bit
is set, the route belongs to a router. If the R-bit is set to zero, the
route belongs to a host. If the router is in a local LAN segment, the
switch implementing the proxy ND function learns of this information by
snooping on neighbor advertisement messages for the associated IPv6
address. This information is then exchanged with other EVPN peers by
using the ND extended community in BGP updates.

To show the EVPN arp-cache that gets populated by the neighbor table and
see if the IPv6-MAC entry belongs to a router, run this command:

    cumulus@switch:mgmt-vrf:~$ net show evpn arp-cache vni 101 ip fe80::202:ff:fe00:11
    IP: fe80::202:ff:fe00:11
     Type: remote
     State: active
     MAC: 00:02:00:00:00:11
     Remote VTEP: 10.0.0.134
     Flags: Router
     Local Seq: 0 Remote Seq: 0

To show the BGP routing table entry for the IPv6-MAC EVPN route with the
ND extended community, run this command:

    cumulus@switch:mgmt-vrf:~$ net show bgp l2vpn evpn route vni 101 mac 00:02:00:00:00:11 ip fe80::202:ff:fe00:11
    BGP routing table entry for [2]:[0]:[0]:[48]:[00:02:00:00:00:11]:[128]:[fe80::202:ff:fe00:11]
    Paths: (1 available, best #1)
      Not advertised to any peer
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:11]:[128]:[fe80::202:ff:fe00:11] VNI 101
      Imported from 1.1.1.2:2:[2]:[0]:[0]:[48]:[00:02:00:00:00:11]:[128]:[fe80::202:ff:fe00:11]
      65002
        10.0.0.134 from leaf2(swp53s0) (10.0.0.134)
           Origin IGP, valid, external, bestpath-from-AS 65002, best
           Extended Community: RT:65002:101 ET:8 ND:Router Flag
           AddPath ID: RX 0, TX 18
           Last update: Thu Aug 30 14:12:09 2018

## <span>EVPN and VXLAN Active-active Mode</span>

No additional EVPN-specific configuration is needed for [VXLAN
active-active
mode](/cumulus-linux/Network_Virtualization/VXLAN_Active-Active_Mode).
Both switches in the
[MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
pair establish EVPN peering with other EVPN speakers (for example, with
spine switches, if using hop-by-hop eBGP) and inform about their locally
known VNIs and MACs. When MLAG is active, both switches announce this
information with the shared anycast IP address.

The active-active configuration, make sure that:

  - The `clagd-vxlan-anycast-ip` parameter is under the [loopback
    stanza](VXLAN_Active-Active_Mode.html#src-8362725_VXLANActive-ActiveMode-anycast)
    on both peers.

  - The anycast address is advertised to the routed fabric from both
    peers.

  - The
    [VNIs](VXLAN_Active-Active_Mode.html#src-8362725_VXLANActive-ActiveMode-example)
    are configured identically on both peers. However,
    `vxlan-local-``tunnelip` must be sourced from unique loopback stanza
    IP address of the switch.

  - The
    [peerlink](VXLAN_Active-Active_Mode.html#src-8362725_VXLANActive-ActiveMode-example)
    must belong to the bridge.

MLAG synchronizes information between the two switches in the MLAG pair;
EVPN does not synchronize.

For information about active-active VTEPs and anycast IP behavior, and
for failure scenarios, read the [VXLAN Active-Active
Mode](/cumulus-linux/Network_Virtualization/VXLAN_Active-Active_Mode)
chapter.

## <span>Inter-subnet Routing</span>

There are multiple models in EVPN for routing between different subnets
(VLANs), also known as inter-VLAN routing. These models arise due to the
following considerations:

  - Does every VTEP act as a layer 3 gateway and do routing, or only
    specific VTEPs do routing?

  - Is routing done only at the ingress of the VXLAN tunnel or is it
    done at both the ingress and the egress of the VXLAN tunnel?

These models are:

  - **Centralized routing:** Specific VTEPs act as designated layer 3
    gateways and perform routing between subnets; other VTEPs just
    perform bridging.

  - **Distributed asymmetric routing:** Every VTEP participates in
    routing, but all routing is done at the ingress VTEP; the egress
    VTEP only performs bridging.

  - **Distributed symmetric routing:** Every VTEP participates in
    routing and routing is done at both the ingress VTEP and the egress
    VTEP.

Distributed routing — asymmetric or symmetric — is commonly deployed
with the VTEPs configured with an *anycast IP/MAC address* for each
subnet. That is, each VTEP that has a particular subnet is configured
with the same IP/MAC for that subnet. Such a model facilitates easy
host/VM mobility as there is no need to change the host/VM configuration
when it moves from one VTEP to another.

EVPN in Cumulus Linux supports all of the routing models listed above.
The models are described further in the following sections.

All routing happens in the context of a tenant VRF ([virtual routing and
forwarding](/cumulus-linux/Layer_3/Virtual_Routing_and_Forwarding_-_VRF)).
A VRF instance is provisioned for each tenant, and the subnets of the
tenant are associated with that VRF (the corresponding SVI is attached
to the VRF). Inter-subnet routing for each tenant occurs within the
context of that tenant's VRF and is separate from the routing for other
tenants.

{{%notice note%}}

When configuring [VXLAN
routing](/cumulus-linux/Network_Virtualization/VXLAN_Routing), Cumulus
Networks recommends enabling ARP suppression on all VXLAN interfaces.
Otherwise, when a locally attached host ARPs for the gateway, it will
receive multiple responses, one from each anycast gateway.

{{%/notice%}}

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-centralized" class="confluence-anchor-link"></span><span>Centralized Routing</span>

In centralized routing, a specific VTEP is configured to act as the
default gateway for all the hosts in a particular subnet throughout the
EVPN fabric. It is common to provision a pair of VTEPs in active-active
mode as the default gateway, using an anycast IP/MAC address for each
subnet. All subnets need to be configured on such gateway VTEP(s). When
a host in one subnet wants to communicate with a host in another subnet,
it addresses the packets to the gateway VTEP. The ingress VTEP (to which
the source host is attached) bridges the packets to the gateway VTEP
over the corresponding VXLAN tunnel. The gateway VTEP performs the
routing to the destination host and post-routing, the packet gets
bridged to the egress VTEP (to which the destination host is attached).
The egress VTEP then bridges the packet on to the destination host.

#### <span>Advertising the Default Gateway</span>

To enable centralized routing, you must configure the gateway VTEPs to
advertise their IP/MAC address. Use the `advertise-default-gw command`,
as shown below.

    cumulus@leaf01:~$ net add bgp autonomous-system 65000
    cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-default-gw
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following configuration snippet in the
`/etc/frr/frr.conf` file.

    router bgp 65000
      address-family l2vpn evpn
       advertise-default-gw
      exit-address-family

{{%notice note%}}

  - You can deploy centralized routing at the VNI level. Therefore, you
    can configure the `advertise-default-gw` command per VNI so that
    centralized routing is used for some VNIs while distributed routing
    (described below) is used for other VNIs. This type of configuration
    is not recommended unless the deployment requires it.

  - When centralized routing is in use, even if the source host and
    destination host are attached to the same VTEP, the packets travel
    to the gateway VTEP to get routed and then come back.

{{%/notice%}}

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-asymmetric" class="confluence-anchor-link"></span><span>Asymmetric Routing</span>

In distributed asymmetric routing, each VTEP acts as a layer 3 gateway,
performing routing for its attached hosts. The routing is called
asymmetric because only the ingress VTEP performs routing, the egress
VTEP only performs the bridging. Asymmetric routing is easy to deploy as
it can be achieved with only host routing and does not involve any
interconnecting VNIs. However, each VTEP must be provisioned with all
VLANs/VNIs — the subnets between which communication can take place;
this is required even if there are no locally-attached hosts for a
particular VLAN.

{{%notice tip%}}

The only additional configuration required to implement asymmetric
routing beyond the standard configuration for a layer 2 VTEP described
earlier is to ensure that each VTEP has all VLANs (and corresponding
VNIs) provisioned on it and the SVI for each such VLAN is configured
with an anycast IP/MAC address.

{{%/notice%}}

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-symmetric" class="confluence-anchor-link"></span><span>Symmetric Routing</span>

In distributed symmetric routing, each VTEP acts as a layer 3 gateway,
performing routing for its attached hosts. This is the same as in
asymmetric routing. The difference is that with symmetric routing, both
the ingress VTEP and egress VTEP route the packets. Therefore, it can be
compared to the traditional routing behavior of routing to a next hop
router. In the VXLAN encapsulated packet, the inner destination MAC
address is set to the router MAC address of the egress VTEP as an
indication that the egress VTEP is the next hop and also needs to
perform routing. All routing happens in the context of a tenant (VRF).
For a packet received by the ingress VTEP from a locally attached host,
the SVI interface corresponding to the VLAN determines the VRF. For a
packet received by the egress VTEP over the VXLAN tunnel, the VNI in the
packet has to specify the VRF. For symmetric routing, this is a VNI
corresponding to the tenant and is different from either the source VNI
or the destination VNI. This VNI is referred to as the layer 3 VNI or
interconnecting VNI; it has to be provisioned by the operator and is
exchanged through the EVPN control plane. In order to make the
distinction clear, the regular VNI, which is used to map a VLAN, is
referred to as the layer 2 VNI.

{{%notice note%}}

**L3-VNI**

  - There is a one-to-one mapping between a layer 3 VNI and a tenant
    (VRF).

  - The VRF to layer 3 VNI mapping has to be consistent across all
    VTEPs. The layer 3 VNI has to be provisioned by the operator.

  - Layer 3 VNI and layer 2 VNI cannot share the same number space; that
    is, you cannot have vlan10 and vxlan10 for example. Otherwise, the
    layer 2 VNI does not get created.

  - In an MLAG configuration, the SVI used for the layer 3 VNI cannot be
    part of the bridge. This ensures that traffic tagged with that VLAN
    ID is not forwarded on the peer link or other trunks.

{{%/notice%}}

In an EVPN symmetric routing configuration, when a type-2 (MAC/IP) route
is announced, in addition to containing two VNIs (the layer 2 VNI and
the layer 3 VNI), the route also contains separate RTs for layer 2 and
layer 3. The layer 3 RT associates the route with the tenant VRF. By
default, this is auto-derived in a similar way to the layer 2 RT, using
the layer 3 VNI instead of the layer 2 VNI; however you can also
explicitly configure it.

For EVPN symmetric routing, additional configuration is required:

1.  Configure a per-tenant VXLAN interface that specifies the layer 3
    VNI for the tenant. This VXLAN interface is part of the bridge and
    router MAC addresses of remote VTEPs is installed over this
    interface.

2.  Configure an SVI (layer 3 interface) corresponding to the per-tenant
    VXLAN interface. This is attached to the tenant's VRF. Remote host
    routes for symmetric routing are installed over this SVI.

3.  Specify the mapping of VRF to layer 3 VNI. This configuration is for
    the BGP control plane.

#### <span>VXLAN Interface Corresponding to the Layer 3 VNI</span>

    cumulus@leaf01:~$ net add vxlan vni104001 vxlan id 104001
    cumulus@leaf01:~$ net add vxlan vni104001 bridge access 4001
    cumulus@leaf01:~$ net add vxlan vni104001 vxlan local-tunnelip 10.0.0.11
    cumulus@leaf01:~$ net add vxlan vni104001 bridge learning off
    cumulus@leaf01:~$ net add vxlan vni104001 bridge arp-nd-suppress on
    cumulus@leaf01:~$ net add bridge bridge ports vni104001
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

The above commands create the following snippet in the
`/etc/network/interfaces` file:

    auto vni104001
    iface vni104001
        bridge-access 4001
        bridge-arp-nd-suppress on
        bridge-learning off
        vxlan-id 104001
        vxlan-local-tunnelip 10.0.0.11
     
    auto bridge
    iface bridge
        bridge-ports vni104001
        bridge-vlan-aware yes

#### <span>SVI for the Layer 3 VNI</span>

    cumulus@leaf01:~$ net add vlan 4001 vrf turtle
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following snippet in the
`/etc/network/interfaces` file:

    auto vlan4001
    iface vlan4001
        vlan-id 4001
        vlan-raw-device bridge
        vrf turtle

{{%notice note%}}

When two VTEPs are operating in VXLAN active-active mode and performing
symmetric routing, you need to configure the router MAC corresponding to
each layer 3 VNI to ensure both VTEPs use the same MAC address. Specify
the `hwaddress` (MAC address) for the SVI corresponding to the layer 3
VNI. Use the same address on both switches in the MLAG pair. Cumulus
Networks recommends you use the MLAG system MAC address.

    cumulus@leaf01:~$ net add vlan 4001 hwaddress 44:39:39:FF:40:94

This command creates the following snippet in the
`/etc/network/interfaces` file:

    auto vlan4001
    iface vlan4001
        hwaddress 44:39:39:FF:40:94
        vlan-id 4001
        vlan-raw-device bridge
        vrf turtle

{{%/notice%}}

#### <span>VRF to Layer 3 VNI Mapping</span>

    cumulus@leaf01:~$ net add vrf turtle vni 104001
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following configuration snippet in the
`/etc/frr/frr.conf` file.

    vrf turtle
     vni 104001
    !

#### <span>Configure RD and RTs for the Tenant VRF</span>

If you do not want the RD and RTs (layer 3 RTs) for the tenant VRF to be
derived automatically, you can configure them manually by specifying
them under the `l2vpn evpn` address family for that specific VRF. For
example:

    cumulus@switch:~$ net add bgp vrf tenant1 l2vpn evpn rd 172.16.100.1:20
    cumulus@switch:~$ net add bgp vrf tenant1 l2vpn evpn route-target import 65100:20
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`/etc/frr/frr.conf` file:

    router bgp <as> vrf tenant1
     address-family l2vpn evpn
      rd 172.16.100.1:20
      route-target import 65100:20

{{%notice note%}}

The tenant VRF RD and RTs are different from the RD and RTs for the
layer 2 VNI, which are described in [Auto-derivation of RDs and
RTs](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-RD-auto-derivation)
and [User-defined RDs and
RTs](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-RD-user-defined),
above.

{{%/notice%}}

#### <span>Advertise the Locally-attached Subnets</span>

Symmetric routing presents a problem in the presence of silent hosts. If
the ingress VTEP does not have the destination subnet and the host route
is not advertised for the destination host, the ingress VTEP cannot
route the packet to its destination. This problem can be overcome by
having VTEPs announce the subnet prefixes corresponding to their
connected subnets in addition to announcing host routes. These routes
will be announced as EVPN prefix (type-5) routes.

To advertise locally attached subnets, you must:

1.  Enable advertisement of EVPN prefix (type-5) routes. Refer to
    [Prefix-based Routing — EVPN Type-5
    Routes](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-PBR_type5),
    below.

2.  Ensure that the routes corresponding to the connected subnets are
    known in the BGP VRF routing table by injecting them using the
    `network` command or redistributing them using the `redistribute
    connected` command.

{{%notice note%}}

This configuration is recommended only if the deployment is known to
have silent hosts. It is also recommended that you enable on only one
VTEP per subnet, or two for redundancy.

{{%/notice%}}

{{%notice note%}}

An earlier version of this chapter referred to the `advertise-subnet`
command. That command is deprecated and should not be used.

{{%/notice%}}

## <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-PBR_type5" class="confluence-anchor-link"></span><span>Prefix-based Routing — EVPN Type-5 Routes</span>

EVPN in Cumulus Linux supports prefix-based routing using EVPN type-5
(prefix) routes. Type-5 routes (or prefix routes) are primarily used to
route to destinations outside of the data center fabric.

EVPN prefix routes carry the layer 3 VNI and router MAC address and
follow the symmetric routing model for routing to the destination
prefix.

{{%notice tip%}}

When connecting to a WAN edge router to reach destinations outside the
data center, it is highly recommended that specific border/exit leaf
switches be deployed to originate the type-5 routes.

{{%/notice%}}

{{%notice note%}}

On switches with the Mellanox Spectrum chipset, centralized routing,
symmetric routing and prefix-based routing only function with the
Spectrum A1 chip.

{{%/notice%}}

{{%notice note%}}

If you are using a Broadcom Trident II+ switch as a border/exit leaf,
see [caveats](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-caveats),
below for a necessary workaround; the workaround only applies to Trident
II+ switches, not Tomahawk or Spectrum.

{{%/notice%}}

### <span>Configure the Switch to Install EVPN Type-5 Routes</span>

For a switch to be able to install EVPN type-5 routes into the routing
table, it must be configured with the layer 3 VNI related information.
This configuration is the same as for symmetric routing. You need to:

1.  Configure a per-tenant VXLAN interface that specifies the layer 3
    VNI for the tenant. This VXLAN interface is part of the bridge;
    router MAC addresses of remote VTEPs are installed over this
    interface.

2.  Configure an SVI (layer 3 interface) corresponding to the per-tenant
    VXLAN interface. This is attached to the tenant's VRF. The remote
    prefix routes are installed over this SVI.

3.  Specify the mapping of the VRF to layer 3 VNI. This configuration is
    for the BGP control plane.

### <span>Announce EVPN Type-5 Routes</span>

The following configuration is needed in the tenant VRF to announce IP
prefixes in BGP's RIB as EVPN type-5 routes.

    cumulus@bl1:~$ net add bgp vrf vrf1 l2vpn evpn advertise ipv4 unicast
    cumulus@bl1:~$ net pending
    cumulus@bl1:~$ net commit

These commands create the following snippet in the `/etc/frr/frr.conf`
file:

    router bgp 65005 vrf vrf1
      address-family l2vpn evpn
        advertise ipv4 unicast
      exit-address-family
    end

### <span>EVPN Type-5 Routing with Asymmetric Routing</span>

Asymmetric routing is an ideal choice when all VLANs (subnets) are
configured on all leaf switches. It simplifies the routing configuration
and eliminates the potential need for advertising subnet routes to
handle silent hosts. However, most deployments need access to external
networks to reach the Internet or global destinations, or to do
subnet-based routing between pods or data centers; this requires EVPN
type-5 routes. <span style="color: #000000;"> </span>

<span style="color: #000000;"> Cumulus Linux </span> supports EVPN
type-5 routes for prefix-based routing in asymmetric configurations
within the pod or data center by providing an option to use the layer 3
VNI only for type-5 routes; type-2 routes (host routes) only use the
layer 2 VNI.

The following example commands show how to use the layer 3 VNI for
type-5 routes only:

    cumulus@leaf01:~$ net add vrf turtle vni 104001 prefix-routes-only
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following snippet in the `/etc/frr/frr.conf`
file:

    vrf turtle
      vni 104001 prefix-routes-only

### <span>Control Which RIB Routes Are Injected into EVPN</span>

By default, when announcing IP prefixes in the BGP RIB as EVPN type-5
routes, all routes in the BGP RIB are picked for advertisement as EVPN
type-5 routes. You can use a route map to allow selective advertisement
of routes from the BGP RIB as EVPN type-5 routes.

The following command adds a route map filter to IPv4 EVPN type-5 route
advertisement:

    cumulus@switch:~$ net add bgp vrf turtle l2vpn evpn advertise ipv4 unicast route-map map1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

### <span>Originate Default EVPN Type-5 Routes</span>

<span style="color: #000000;"> Cumulus Linux supports originating EVPN
default type-5 routes. The default type-5 route is originated from a
border (exit) leaf and advertised to all the other leafs within the pod.
Any leaf within the pod follows the default route towards the border
leaf for all external traffic (towards the Internet or a different pod).
</span>

<span style="color: #000000;"> <span style="color: #000000;"> To
originate a default type-5 route in EVPN, you need to execute
<span style="color: #000000;"> FRRouting </span> commands. The following
shows an example: </span> </span>

    switch(config)# router bgp 650030 vrf vrf1
    switch(config-router)# address-family l2vpn evpn
    switch(config-router-af)# default-originate ipv4
    switch(config-router-af)# default-originate ipv6
    switch(config-router-af)# exit
    switch(config-router)# exit
    switch(config)# exit
    switch# write memory

## <span>EVPN Enhancements</span>

### <span>Static (Sticky) MAC Addresses</span>

MAC addresses that are intended to be pinned to a particular VTEP can be
provisioned on the VTEP as a static bridge FDB entry. EVPN picks up
these MAC addresses and advertises them to peers as remote static MACs.
You configure static bridge FDB entries for sticky MACs under the bridge
configuration using NCLU:

    cumulus@switch:~$ net add bridge post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-ports swp1 vni10101
        bridge-vids 101
        bridge-vlan-aware yes
        post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static

{{%notice tip%}}

For a bridge in [traditional
mode](/cumulus-linux/Layer_2/Ethernet_Bridging_-_VLANs/Traditional_Bridge_Mode),
you must edit the bridge configuration in the `/etc/network/interfaces`
file using a text editor:

    auto br101
    iface br101
        bridge-ports swp1.101 vni10101
        bridge-learning vni10101=off
        post-up bridge fdb add 00:11:22:33:44:55 dev swp1.101 master static

{{%/notice%}}

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-filter_evpn_route_type" class="confluence-anchor-link"></span><span>Filter EVPN Routes Based on Type</span>

In many situations, it is desirable to only exchange EVPN routes of a
particular type. For example, a common deployment scenario for large
data centers is to sub-divide the data center into multiple pods with
full host mobility within a pod but only do prefix-based routing across
pods. This can be achieved by only exchanging EVPN type-5 routes across
pods.

To filter EVPN routes based on the route-type and allow only certain
types of EVPN routes to be advertised in the fabric, use these commands:

    net add routing route-map <route_map_name> (deny|permit) <1-65535> match evpn default-route
    net add routing route-map <route_map_name> (deny|permit) <1-65535> match evpn route-type (macip|prefix|multicast)

The following example command configures EVPN to advertise type-5 routes
only:

    cumulus@switch:~$ net add routing route-map map1 permit 1 match evpn route-type prefix
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

### <span>Advertise SVI IP Addresses</span>

In a typical EVPN deployment, you *reuse* SVI IP addresses on VTEPs
across multiple racks. However, if you use *unique* SVI IP addresses
across multiple racks and you want the local SVI IP address to be
reachable via remote VTEPs, you can enable the `advertise-svi-ip`
option. This option advertises the SVI IP/MAC address as a type-2 route
and eliminates the need for any flooding over VXLAN to reach the SVI IP
from a remote VTEP/rack.

{{%notice note%}}

**Notes**

  - The `advertise-svi-ip` option is available in Cumulus Linux 3.7.4
    and later.

  - When you enable the `advertise-svi-ip` option, the anycast IP/MAC
    address pair is not advertised. Be sure **not** to enable both the
    `advertise-svi-ip` option and the `advertise-default-gw` option at
    the same time. (The `advertise-default-gw` option configures the
    gateway VTEPs to advertise their IP/MAC address. See [Advertising
    the Default
    Gateway](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-centralized)).

{{%/notice%}}

To advertise *all* SVI IP/MAC addresses on the switch, run these
commands:

    cumulus@switch:~$ net add bgp evpn advertise-svi-ip
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands save the configuration in the`  /etc/frr/frr.conf ` file.
For example:

    cumulus@switch:~$ sudo cat /etc/frr/frr.conf
    ...
    address-family l2vpn evpn
     advertise-svi-ip
    exit-address-family
    ...

To advertise a *specific* SVI IP/MAC address, run these commands:

    cumulus@switch:~$ net add bgp evpn vni 10 advertise-svi-ip
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands save the configuration in the `/etc/frr/frr.conf` file.
For example:

    cumulus@switch:~$ sudo cat /etc/frr/frr.conf
    ...
    address-family l2vpn evpn
     vni 10
     advertise-svi-ip
    exit-address-family
    ...

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-MAC-mobility" class="confluence-anchor-link"></span><span>Extended Mobility</span>

Cumulus Linux support for host and virtual machine mobility in an EVPN
deployment has been enhanced to handle scenarios where the IP to MAC
binding for a host or virtual machine changes across the move. This is
referred to as *extended mobility*. The simple mobility scenario where a
host or virtual machine with a binding of `IP1`, `MAC1` moves from one
rack to another has been supported in previous releases of Cumulus
Linux. The EVPN enhancements support additional scenarios where a host
or virtual machine with a binding of `IP1`, `MAC1` moves and takes on a
new binding of `IP2`, `MAC1` or `IP1`, `MAC2`. The EVPN protocol
mechanism to handle extended mobility continues to use the MAC mobility
extended community and is the same as the standard mobility procedures.
Extended mobility defines how the sequence number in this attribute is
computed when binding changes occur.

Extended mobility not only supports virtual machine *moves*, but also a
scenario where one virtual machine shuts down and another is provisioned
on a different rack that uses the IP address or the MAC address of the
previous virtual machine. For example, in an EVPN deployment with
OpenStack, where virtual machines for a tenant are provisioned and shut
down very dynamically, a new virtual machine can use the same IP address
as an earlier virtual machine but with a different MAC address.

The support for extended mobility is enabled by default and does not
require any additional configuration.

You can examine the sequence numbers associated with a host or virtual
machine MAC address and IP address with NCLU commands. For example:

    cumulus@switch:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:42
    MAC: 00:02:00:00:00:42
     Remote VTEP: 10.0.0.2
     Local Seq: 0 Remote Seq: 3
     Neighbors:
        10.1.1.74 Active

    cumulus@switch:~$ net show evpn arp vni 10100 ip 10.1.1.74
    IP: 10.1.1.74
     Type: local
     State: active
     MAC: 44:39:39:ff:00:24
     Local Seq: 2 Remote Seq: 3

### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-dad" class="confluence-anchor-link"></span><span>Duplicate Address Detection</span>

Cumulus Linux 3.7.2 and later is able to detect duplicate MAC and
IPv4/IPv6 addresses on hosts or virtual machines in a VXLAN-EVPN
configuration. The Cumulus Linux switch (VTEP) considers a host MAC or
IP address to be duplicate if the address moves across the network more
than a certain number of times within a certain number of seconds (five
moves within 180 seconds by default). In addition to legitimate host or
VM mobility scenarios, address movement can occur when IP addresses are
misconfigured on hosts or when packet looping occurs in the network due
to faulty configuration or behavior.

Duplicate address detection is enabled by default and triggers when:

  - Two hosts have the same MAC address (the host IP addresses might be
    the same or different)

  - Two hosts have the same IP address but different MAC addresses

By default, when a duplicate address is detected, Cumulus Linux flags
the address as a duplicate and generates an error in syslog so that you
can troubleshoot the reason and address the fault, then clear the
duplicate address flag. No functional action is taken on the address.

{{%notice note%}}

<span style="color: #000000;"> If a MAC address is flagged as a
duplicate, all IP addresses associated with that MAC are flagged as
duplicates.**** </span>

{{%/notice%}}

{{%notice note%}}

**MLAG Deployments**

<span style="color: #000000;"> In an MLAG configuration, duplicate
address detection runs independently on each switch in the MLAG pair.
Based on the sequence in which local learn and/or route withdrawal from
the remote VTEP occurs, an IP address might be flagged as duplicate only
on one of the switches in the MLAG pair. In rare cases, neither switch
might flag the IP address as a duplicate. </span>

{{%/notice%}}

**<span style="color: #222222;"> When Does Duplicate Address Detection
Trigger? </span>**

<span style="color: #222222;"> The VTEP that sees an address move from
remote to local begins the detection process by starting a timer. E
</span> ach VTEP runs duplicate address detection independently.
Detection always starts with the first mobility event from *remote* to
*local*. If the address is initially remote, the detection count can
start with the very first move for the address. If the address is
initially local, the detection count starts only with the second or
higher move for the address <span style="color: #36424a;"> .
<span style="color: #222222;"> If an address is undergoing a mobility
event between remote VTEPs, duplicate detection is not started. </span>
</span>

The following illustration shows VTEP-A, VTEP-B, and VTEP-C in an EVPN
configuration. Duplicate address detection triggers on VTEP-A when there
is a duplicate MAC address for two hosts attached to VTEP-A and VTEP-B.
However, duplicate detection does *not* trigger on VTEP-A when mobility
events occur between two remote VTEPs (VTEP-B and VTEP-C).

<span style="color: #36424a;"> </span>

{{% imgOld 0 %}}

#### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-configure-dad" class="confluence-anchor-link"></span><span>Configure Duplicate Address Detection</span>

To change the threshold for MAC and IP address moves, run the `net add
bgp l2vpn evpn dup-addr-detection max-moves <number-of-events> time
<duration>` command. You can specify `max-moves` to be between 2 and
1000 and `time` to be between 2 and 1800 seconds.

The following example command sets the maximum number of address moves
allowed to 10 and the duplicate address detection time interval to 1200
seconds.

    cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection max-moves 10 time 1200 

To disable duplicate address detection, see [Disable Duplicate Address
Detection](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-disableDAD)
below.

#### <span>Example syslog Messages</span>

The following example shows the syslog message that is generated when
Cumulus Linux detects a MAC address as a duplicate during a local
update:

    2018/11/06 18:55:29.463327 ZEBRA: [EC 4043309149] VNI 1001: MAC 00:01:02:03:04:11 detected as duplicate during local update, last VTEP 172.16.0.16

<span style="color: #36424a;"> The following example shows the syslog
message that is generated when Cumulus Linux detects an IP address as a
duplicate during a remote update: </span> <span style="color: #36424a;">
</span>

    2018/11/09 22:47:15.071381 ZEBRA: [EC 4043309151] VNI 1002: MAC aa:22:aa:aa:aa:aa IP 10.0.0.9 detected as duplicate during remote update, from VTEP 172.16.0.16

#### <span>Freeze a Detected Duplicate Address</span>

Cumulus Linux 3.7.3 and later provides a *freeze* option that takes
action on a detected duplicate address. You can freeze the address
*permanently* (until you intervene) or for a *defined amount of time*,
after which it is cleared automatically.

When you enable the freeze option and a duplicate address is detected:

  - If the MAC or IP address is learned from a remote VTEP at the time
    it is frozen, the forwarding information in the kernel and hardware
    is not updated, leaving it in the prior state. Any future remote
    updates are processed but they are not reflected in the kernel
    entry. If the remote VTEP sends a MAC-IP route withdrawal, the local
    VTEP removes the frozen remote entry. Then, if the local VTEP has a
    locally-learned entry already present in its kernel, FRR will
    originate a corresponding MAC-IP route and advertise it to all
    remote VTEPs.

  - If the MAC or IP address is locally learned on this VTEP at the time
    it is frozen, the address is not advertised to remote VTEPs. Future
    local updates are processed but are not advertised to remote VTEPs.
    If FRR receives a local entry delete event, the frozen entry is
    removed from the FRR database. Any remote updates (from other VTEPs)
    change the state of the entry to remote but the entry is not
    installed in the kernel (until cleared).

**To recover from a freeze**, shut down the faulty host or VM or fix any
other misconfiguration in the network. If the address is frozen
*permanently,* issue the [clear
command](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-clearDuplicateAddress)
on the VTEP where the address is marked as duplicate. If the address is
frozen for a defined period of time, it is cleared automatically after
the timer expires (you can clear the duplicate address before the timer
expires with the [clear
command](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-clearDuplicateAddress)).

{{%notice note%}}

If you issue the [clear
command](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-clearDuplicateAddress)
or the timer expires before you address the fault, duplicate address
detection might occur repeatedly.

{{%/notice%}}

After you clear a frozen address, if it is present behind a remote VTEP,
the kernel and hardware forwarding tables are updated. If the address is
locally learned on this VTEP, the address is advertised to remote VTEPs.
All VTEPs get the correct address as soon as the host communicates.
Silent hosts are learned only after the faulty entries age out, or you
intervene and clear the faulty MAC and ARP table entries.

#### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-configure-dad" class="confluence-anchor-link"></span><span>Configure the Freeze Option</span>

To enable Cumulus Linux to *freeze* detected duplicate addresses, run
the `net add bgp l2vpn evpn dup-addr-detection freeze
<duration>|permanent` command. The duration can be any number of seconds
between 30 and 3600.

The following example command freezes duplicate addresses for a period
of <span style="color: #000000;"> 1000 seconds, after which it is
cleared automatically </span> :

    cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection freeze 1000

{{%notice note%}}

**Best Practice**

Cumulus Networks recommends you set the freeze timer to be three times
the duplicate address detection window. For example, if the duplicate
address detection window is set to the default of 180 seconds, set the
freeze timer to 540 seconds.

{{%/notice%}}

The following example command freezes duplicate addresses permanently
(until you issue the [clear
command](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-clearDuplicateAddress)):

    cumulus@switch:~$ net add bgp l2vpn evpn dup-addr-detection freeze permanent

#### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-clearDuplicateAddress" class="confluence-anchor-link"></span><span>Clear Duplicate Addresses</span>

To clear a duplicate MAC or IP address (and unfreeze a frozen address),
run the `net clear evpn dup-addr vni <vni_id> ip <mac/ip address>`
command. The following example command clears IP address 10.0.0.9 for
VNI 101.

    cumulus@switch:~$ net clear evpn dup-addr vni 101 ip 10.0.0.9

To clear duplicate addresses for all VNIs, run the following command:

    cumulus@switch:~$ net clear evpn dup-addr vni all

{{%notice note%}}

In an MLAG configuration, you need to run the [clear
command](#src-8362732_EthernetVirtualPrivateNetwork-EVPN-clearDuplicateAddress)
on both the MLAG primary and secondary switch.

{{%/notice%}}

{{%notice note%}}

When you clear a duplicate MAC address, all its associated IP addresses
are also cleared. However, you cannot clear an associated IP address if
its MAC address is still in a duplicate state.

{{%/notice%}}

#### <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-disableDAD" class="confluence-anchor-link"></span><span>Disable Duplicate Address Detection</span>

By default, duplicate address detection is enabled and a syslog error is
generated when a duplicate address is detected. To disable duplicate
address detection, run the following command.

    cumulus@switch:~$ net del bgp l2vpn evpn dup-addr-detection

When you disable duplicate address detection, Cumulus Linux clears the
configuration and all existing duplicate addresses.

#### <span>Show Detected Duplicate Address Information</span>

<span style="color: #000000;"> During the duplicate address detection
process, you can see the start time and current detection count with the
`net show evpn mac vni <vni_id> mac <mac_addr>` command. </span>
<span style="color: #000000;"> The following command example shows that
</span> detection started <span style="color: #000000;"> for MAC address
</span> 00:01:02:03:04:11 for VNI 1001 on Tuesday, Nov 6 at 18:55:05 and
the number of moves detected is 1.

    cumulus@switch:~$ net show evpn mac vni 1001 mac 00:01:02:03:04:11
    MAC: 00:01:02:03:04:11
     Intf: hostbond3(15) VLAN: 1001
     Local Seq: 1 Remote Seq: 0
     Duplicate detection started at Tue Nov  6 18:55:05 2018, detection count 1
     Neighbors:
        10.0.1.26 Active

After the duplicate MAC address is cleared, the `net show evpn mac vni
<vni_id> mac <mac_addr>` <span style="color: #000000;"> command shows:
</span>

    MAC: 00:01:02:03:04:11
     Remote VTEP: 172.16.0.16
     Local Seq: 13 Remote Seq: 14
     Duplicate, detected at Tue Nov  6 18:55:29 2018
     Neighbors:
        10.0.1.26 Active

To display information for a duplicate IP address, run the ` net show
evpn arp-cache vni <vni_id> ip <ip_addr>  `command. The following
command example shows information for IP address 10.0.0.9 for VNI 1001.

    cumulus@switch:~$ net show evpn arp-cache vni 1001 ip 10.0.0.9
    IP: 10.0.0.9
     Type: remote
     State: inactive
     MAC: 00:01:02:03:04:11
     Remote VTEP: 10.0.0.34
     Local Seq: 0 Remote Seq: 14
     Duplicate, detected at Tue Nov  6 18:55:29 2018

To show a list of MAC addresses detected as duplicate for a specific VNI
or for all VNIs, run the `net show evpn mac vni <vni-id|all> duplicate`
command. The following example command shows a list of duplicate MAC
addresses for VNI 1001:

``` 
cumulus@switch:~$ net show evpn mac vni 1001 duplicate
Number of MACs (local and remote) known for this VNI: 16
MAC               Type   Intf/Remote VTEP      VLAN 
aa:bb:cc:dd:ee:ff local  hostbond3             1001  
```

To show a list of IP addresses detected as duplicate for a specific VNI
or for all VNIs, run the `net show evpn arp-cache vni <vni-id|all>
duplicate` command. The following example command shows a list of
duplicate IP addresses for VNI 1001:

    cumulus@switch:~$ net show evpn arp-cache vni 1001 duplicate
    Number of ARPs (local and remote) known for this VNI: 20
    IP                Type   State    MAC                Remote VTEP          
    10.0.0.8          local  active   aa:11:aa:aa:aa:aa
    10.0.0.9          local  active   aa:11:aa:aa:aa:aa
    10.10.0.12        remote active   aa:22:aa:aa:aa:aa  172.16.0.16

To show configured duplicate address detection parameters, run the `net
show evpn` command:

    cumulus@switch:~$ net show evpn
    L2 VNIs: 4
    L3 VNIs: 2
    Advertise gateway mac-ip: No
    Duplicate address detection: Enable
      Detection max-moves 7, time 300
      Detection freeze permanent

## <span>EVPN Operational Commands</span>

### <span>General Linux Commands Related to EVPN</span>

You can use various `iproute2` commands to examine links, VLAN mappings
and the bridge MAC forwarding database known to the Linux kernel. You
can also use these commands to examine the neighbor cache and the
routing table (for the underlay or for a specific tenant VRF). Some of
the key commands are:

  - `ip [-d] link show`

  - `bridge link show`

  - `bridge vlan show`

  - `bridge [-s] fdb show`

  - `ip neighbor show`

  - `ip route show [table <vrf-name>]`

A sample output of `ip -d link show type vxlan` is shown below for one
VXLAN interface. Some relevant parameters are the VNI value, the state,
the local IP address for the VXLAN tunnel, the UDP port number (4789)
and the bridge that the interface is part of (*bridge* in the example
below). The output also shows that MAC learning is disabled (*off*) on
the VXLAN interface.

    cumulus@leaf01:~$ ip -d link show type vxlan
    9: vni100: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default 
        link/ether 72:bc:b4:a3:eb:1e brd ff:ff:ff:ff:ff:ff promiscuity 1 
        vxlan id 10100 local 10.0.0.1 srcport 0 0 dstport 4789 nolearning ageing 300 
        bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning off flood on port_id 0x8001 port_no 0x1 designated_port 32769 designated_cost 0 designated_bridge 8000.0:1:0:0:11:0 designated_root 8000.0:1:0:0:11:0 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on neigh_suppress on group_fwd_mask 0x0 group_fwd_mask_str 0x0 group_fwd_maskhi 0x0 group_fwd_maskhi_str 0x0 addrgenmode eui64 
    ...
    cumulus@leaf01:~$

A sample output of `bridge fdb show` is depicted below. Some interesting
information from this output includes:

  - swp3 and swp4 are access ports with VLAN ID 100. This is mapped to
    VXLAN interface vni100.

  - 00:02:00:00:00:01 is a local host MAC learned on swp3.

  - The remote VTEPs which participate in VLAN ID 100 are 10.0.0.3,
    10.0.0.4 and 10.0.0.2. This is evident from the FDB entries with a
    MAC address of 00:00:00:00:00:00. These entries are used for BUM
    traffic replication.

  - 00:02:00:00:00:06 is a remote host MAC reachable over the VXLAN
    tunnel to 10.0.0.2.

<!-- end list -->

    cumulus@leaf01:~$ bridge fdb show
    00:02:00:00:00:13 dev swp3 master bridge permanent
    00:02:00:00:00:01 dev swp3 vlan 100 master bridge 
    00:02:00:00:00:02 dev swp4 vlan 100 master bridge 
    72:bc:b4:a3:eb:1e dev vni100 master bridge permanent
    00:02:00:00:00:06 dev vni100 vlan 100 offload master bridge 
    00:00:00:00:00:00 dev vni100 dst 10.0.0.3 self permanent
    00:00:00:00:00:00 dev vni100 dst 10.0.0.4 self permanent
    00:00:00:00:00:00 dev vni100 dst 10.0.0.2 self permanent
    00:02:00:00:00:06 dev vni100 dst 10.0.0.2 self offload 
    ...

A sample output of `ip neigh show` is shown below. Some interesting
information from this output includes:

  - 172.16.120.11 is a locally-attached host on VLAN 100. It is shown
    twice because of the configuration of the anycast IP/MAC on the
    switch.

  - 172.16.120.42 is a remote host on VLAN 100 and 172.16.130.23 is a
    remote host on VLAN 200. The MAC address of these hosts can be
    examined using the `bridge fdb show` command described earlier to
    determine the VTEPs behind which these hosts are located.

<!-- end list -->

    cumulus@leaf01:~$ ip neigh show
    172.16.120.11 dev vlan100-v0 lladdr 00:02:00:00:00:01 STALE
    172.16.120.42 dev vlan100 lladdr 00:02:00:00:00:0e offload REACHABLE
    172.16.130.23 dev vlan200 lladdr 00:02:00:00:00:07 offload REACHABLE
    172.16.120.11 dev vlan100 lladdr 00:02:00:00:00:01 REACHABLE
    ...

### <span>General BGP Operational Commands Relevant to EVPN</span>

The following commands are not unique to EVPN but help troubleshoot
connectivity and route propagation. If BGP is used for the underlay
routing, you can view a summary of the layer 3 fabric connectivity by
running the `net show bgp summary` command:

    cumulus@leaf01:~$ net show bgp summary
    show bgp ipv4 unicast summary
    =============================
    BGP router identifier 10.0.0.1, local AS number 65001 vrf-id 0
    BGP table version 9
    RIB entries 11, using 1496 bytes of memory
    Peers 2, using 42 KiB of memory
    Peer groups 1, using 72 bytes of memory
     
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
    s1(swp49s0)     4      65100      43      49        0    0    0 02:04:00            4
    s2(swp49s1)     4      65100      43      49        0    0    0 02:03:59            4
    Total number of neighbors 2
     
    show bgp ipv6 unicast summary
    =============================
    No IPv6 neighbor is configured
     
    show bgp evpn summary
    =====================
    BGP router identifier 10.0.0.1, local AS number 65001 vrf-id 0
    BGP table version 0
    RIB entries 15, using 2040 bytes of memory
    Peers 2, using 42 KiB of memory
    Peer groups 1, using 72 bytes of memory
     
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
    s1(swp49s0)     4      65100      43      49        0    0    0 02:04:00           30
    s2(swp49s1)     4      65100      43      49        0    0    0 02:03:59           30
    Total number of neighbors 2

You can examine the underlay routing, which determines how remote VTEPs
are reached. Run the `net show route` command. Here is some sample
output from a leaf switch:

    cumulus@leaf01:~$ net show route
     
    show ip route
    =============
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
           T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
           F - PBR,
           > - selected route, * - FIB route
     
    C>* 10.0.0.11/32 is directly connected, lo, 19:48:21
    B>* 10.0.0.12/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:03
      *                     via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    B>* 10.0.0.13/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:03
      *                     via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    B>* 10.0.0.14/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:03
      *                     via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    B>* 10.0.0.21/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:04
    B>* 10.0.0.22/32 [20/0] via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    B>* 10.0.0.41/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:03
      *                     via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    B>* 10.0.0.42/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:03
      *                     via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    C>* 10.0.0.112/32 is directly connected, lo, 19:48:21
    B>* 10.0.0.134/32 [20/0] via fe80::4638:39ff:fe00:54, swp51, 19:48:03
      *                      via fe80::4638:39ff:fe00:25, swp52, 19:48:03
    C>* 169.254.1.0/30 is directly connected, peerlink.4094, 19:48:21
     
    show ipv6 route
    ===============
    Codes: K - kernel route, C - connected, S - static, R - RIPng,
           O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table,
           v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR,
           > - selected route, * - FIB route
    C * fe80::/64 is directly connected, bridge, 19:48:21
    C * fe80::/64 is directly connected, peerlink.4094, 19:48:21
    C * fe80::/64 is directly connected, swp52, 19:48:21
    C>* fe80::/64 is directly connected, swp51, 19:48:21
     
     
    cumulus@leaf01:~$

You can view the MAC forwarding database on the switch by running the
`net show bridge macs` command:

    cumulus@leaf01:~$ net show bridge macs
    VLAN      Master    Interface    MAC                TunnelDest    State      Flags          LastSeen
    --------  --------  -----------  -----------------  ------------  ---------  -------------  ---------------
    100       br0       br0          00:00:5e:00:01:01                permanent                 1 day, 03:38:43
    100       br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:43
    100       br0       swp3         00:02:00:00:00:01                                          00:00:26
    100       br0       swp4         00:02:00:00:00:02                                          00:00:16
    100       br0       vni100       00:02:00:00:00:0a                           offload        1 day, 03:38:20
    100       br0       vni100       00:02:00:00:00:0d                           offload        1 day, 03:38:20
    100       br0       vni100       00:02:00:00:00:0e                           offload        1 day, 03:38:20
    100       br0       vni100       00:02:00:00:00:05                           offload        1 day, 03:38:19
    100       br0       vni100       00:02:00:00:00:06                           offload        1 day, 03:38:19
    100       br0       vni100       00:02:00:00:00:09                           offload        1 day, 03:38:20
    200       br0       br0          00:00:5e:00:01:01                permanent                 1 day, 03:38:42
    200       br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:43
    200       br0       swp5         00:02:00:00:00:03                                          00:00:26
    200       br0       swp6         00:02:00:00:00:04                                          00:00:26
    200       br0       vni200       00:02:00:00:00:0b                           offload        1 day, 03:38:20
    200       br0       vni200       00:02:00:00:00:0c                           offload        1 day, 03:38:20
    200       br0       vni200       00:02:00:00:00:0f                           offload        1 day, 03:38:20
    200       br0       vni200       00:02:00:00:00:07                           offload        1 day, 03:38:19
    200       br0       vni200       00:02:00:00:00:08                           offload        1 day, 03:38:19
    200       br0       vni200       00:02:00:00:00:10                           offload        1 day, 03:38:20
    4001      br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:42
    4001      br0       vni4001      00:01:00:00:12:00                           offload        1 day, 03:38:19
    4001      br0       vni4001      00:01:00:00:13:00                           offload        1 day, 03:38:20
    4001      br0       vni4001      00:01:00:00:14:00                           offload        1 day, 03:38:20
    untagged            br0          00:00:5e:00:01:01                permanent  self           never
    untagged            vlan100      00:00:5e:00:01:01                permanent  self           never
    untagged            vlan200      00:00:5e:00:01:01                permanent  self           never
    ...

### <span>Display EVPN address-family Peers</span>

You can see the BGP peers participating in the layer 2 VPN/EVPN
address-family and their states using the ` net show bgp l2vpn evpn
summary  `command. The following sample output from a leaf switch shows
eBGP peering with two spine switches for exchanging EVPN routes; both
peering sessions are in the *established* state.

    cumulus@leaf01:~$ net show bgp l2vpn evpn summary
    BGP router identifier 10.0.0.1, local AS number 65001 vrf-id 0
    BGP table version 0
    RIB entries 15, using 2280 bytes of memory
    Peers 2, using 39 KiB of memory
    Peer groups 1, using 64 bytes of memory
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
    s1(swp1)        4      65100     103     107        0    0    0 1d02h08m           30
    s2(swp2)        4      65100     103     107        0    0    0 1d02h08m           30
    Total number of neighbors 2
    cumulus@leaf01:~$

### <span>Display VNIs in EVPN</span>

Run the `show bgp l2vpn evpn vni` command to display the configured VNIs
on a network device participating in BGP EVPN. This command is only
relevant on a VTEP. If symmetric routing is configured, this command
displays the special layer 3 VNIs that are configured per tenant VRF.

The following example from a leaf switch shows two layer 2 VNIs — 10100
and 10200 — as well as a layer 3 VNI — 104001. For layer 2 VNIs, the
number of associated MAC and neighbor entries are shown. The VXLAN
interface and VRF corresponding to each VNI are also shown.

    cumulus@leaf01:~$ net show evpn vni
    VNI        Type VxLAN IF              # MACs   # ARPs   # Remote VTEPs  Tenant VRF                           
    10200      L2   vni200              8        12       3               vrf1                                 
    10100      L2   vni100              8        12       3               vrf1                                 
    104001     L3   vni4001             3        3        n/a             vrf1                                 
    cumulus@leaf01:~$

You can examine the EVPN information for a specific VNI in detail. The
following output shows details for the layer 2 VNI 10100 as well as for
the layer 3 VNI 104001. For the layer 2 VNI, the remote VTEPs which have
that VNI are shown. For the layer 3 VNI, the router MAC and associated
layer 2 VNIs are shown. The state of the layer 3 VNI depends on the
state of its associated VRF as well as the states of its underlying
VXLAN interface and SVI.

    cumulus@leaf01:~$ net show evpn vni 10100
    VNI: 10100
     Type: L2
     Tenant VRF: vrf1
     VxLAN interface: vni100
     VxLAN ifIndex: 9
     Local VTEP IP: 10.0.0.1
     Remote VTEPs for this VNI:
      10.0.0.2
      10.0.0.4
      10.0.0.3
     Number of MACs (local and remote) known for this VNI: 8
     Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 12
     Advertise-gw-macip: No
    cumulus@leaf01:~$ 
    cumulus@leaf01:~$ net show evpn vni 104001
    VNI: 104001
      Type: L3
      Tenant VRF: vrf1
      Local Vtep Ip: 10.0.0.1
      Vxlan-Intf: vni4001
      SVI-If: vlan4001
      State: Up
      Router MAC: 00:01:00:00:11:00
      L2 VNIs: 10100 10200 
    cumulus@leaf01:~$

### <span>Examine Local and Remote MAC Addresses for a VNI in EVPN</span>

Run `net show evpn mac vni <vni>` to examine all local and remote MAC
addresses for a VNI. This command is only relevant for a layer 2 VNI:

    cumulus@leaf01:~$ net show evpn mac vni 10100
    Number of MACs (local and remote) known for this VNI: 8
    MAC               Type   Intf/Remote VTEP      VLAN 
    00:02:00:00:00:0e remote 10.0.0.4            
    00:02:00:00:00:06 remote 10.0.0.2            
    00:02:00:00:00:05 remote 10.0.0.2            
    00:02:00:00:00:02 local  swp4                  100  
    00:00:5e:00:01:01 local  vlan100-v0            100  
    00:02:00:00:00:09 remote 10.0.0.3            
    00:01:00:00:11:00 local  vlan100               100  
    00:02:00:00:00:01 local  swp3                  100  
    00:02:00:00:00:0a remote 10.0.0.3            
    00:02:00:00:00:0d remote 10.0.0.4            
    cumulus@leaf01:~$

Run the `net show evpn mac vni all` command to examine MAC addresses for
all VNIs.

You can examine the details for a specific MAC addresse or query all
remote MAC addresses behind a specific VTEP:

    cumulus@leaf01:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:02
    MAC: 00:02:00:00:00:02
     Intf: swp4(6) VLAN: 100
     Local Seq: 0 Remote Seq: 0
     Neighbors:
        172.16.120.12 Active
    cumulus@leaf01:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:05
    MAC: 00:02:00:00:00:05
     Remote VTEP: 10.0.0.2
     Neighbors:
        172.16.120.21 
    cumulus@leaf01:~$ net show evpn mac vni 10100 vtep 10.0.0.3
    VNI 10100
    MAC               Type   Intf/Remote VTEP      VLAN 
    00:02:00:00:00:09 remote 10.0.0.3            
    00:02:00:00:00:0a remote 10.0.0.3            
    cumulus@leaf01:~$

### <span>Examine Local and Remote Neighbors for a VNI in EVPN</span>

Run the `net show evpn arp-cache vni <vni>` command to examine all local
and remote neighbors (ARP entries) for a VNI. This command is only
relevant for a layer 2 VNI and the output shows both IPv4 and IPv6
neighbor entries:

    cumulus@leaf01:~$ net show evpn arp-cache vni 10100
    Number of ARPs (local and remote) known for this VNI: 12
    IP                      Type   MAC               Remote VTEP          
    172.16.120.11           local  00:02:00:00:00:01
    172.16.120.12           local  00:02:00:00:00:02
    172.16.120.22           remote 00:02:00:00:00:06 10.0.0.2            
    fe80::201:ff:fe00:1100  local  00:01:00:00:11:00
    172.16.120.1            local  00:01:00:00:11:00
    172.16.120.31           remote 00:02:00:00:00:09 10.0.0.3            
    fe80::200:5eff:fe00:101 local  00:00:5e:00:01:01
    ...

Run the `net show evpn arp-cache vni all` command to examine neighbor
entries for all VNIs.

### <span>Examine Remote Router MACs in EVPN</span>

When symmetric routing is deployed, run the ` net show evpn rmac vni
<vni>  `command to examine the router MACs corresponding to all remote
VTEPs. This command is only relevant for a layer 3 VNI:

    cumulus@leaf01:~$ net show evpn rmac vni 104001
    Number of Remote RMACs known for this VNI: 3
    MAC               Remote VTEP          
    00:01:00:00:14:00 10.0.0.4            
    00:01:00:00:12:00 10.0.0.2            
    00:01:00:00:13:00 10.0.0.3            
    cumulus@leaf01:~$

Run the ` net show evpn rmac vni all  `command to examine router MACs
for all layer 3 VNIs.

### <span>Examine Gateway Next Hops in EVPN</span>

When symmetric routing is deployed, you can run the `net show evpn
next-hops vni <vni>` command to examine the gateway next hops. This
command is only relevant for a layer 3 VNI. In general, the gateway next
hop IP addresses correspond to the remote VTEP IP addresses. Remote host
and prefix routes are installed using these next hops:

    cumulus@leaf01:~$ net show evpn next-hops vni 104001
    Number of NH Neighbors known for this VNI: 3
    IP              RMAC             
    10.0.0.3       00:01:00:00:13:00
    10.0.0.4       00:01:00:00:14:00
    10.0.0.2       00:01:00:00:12:00
    cumulus@leaf01:~$

Run the `net show evpn next-hops vni` all command to examine gateway
next hops for all layer 3 VNIs.

You can query a specific next hop; the output displays the remote host
and prefix routes through this next hop:

    cumulus@leaf01:~$ net show evpn next-hops vni 104001 ip 10.0.0.4
    Ip: 10.0.0.4
      RMAC: 00:01:00:00:14:00
      Refcount: 4
      Prefixes:
        172.16.120.41/32
        172.16.120.42/32
        172.16.130.43/32
        172.16.130.44/32
    cumulus@leaf01:~$

### <span>Display the VRF Routing Table in FRR</span>

Run the `net show route vrf <vrf-name>` comand to examine the VRF
routing table. This command is not specific to EVPN. In the context of
EVPN, this command is relevant when symmetric routing is deployed and
can be used to verify that remote host and prefix routes are installed
in the VRF routing table and point to the appropriate gateway next hop.

    cumulus@leaf01:~$ net show route vrf vrf1
    show ip route vrf vrf1 
    =======================
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
           T - Table, v - VNC, V - VNC-Direct, A - Babel,
           > - selected route, * - FIB route
     
    VRF vrf1:
    K * 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 1d02h42m
    C * 172.16.120.0/24 is directly connected, vlan100-v0, 1d02h42m
    C>* 172.16.120.0/24 is directly connected, vlan100, 1d02h42m
    B>* 172.16.120.21/32 [20/0] via 10.0.0.2, vlan4001 onlink, 1d02h41m
    B>* 172.16.120.22/32 [20/0] via 10.0.0.2, vlan4001 onlink, 1d02h41m
    B>* 172.16.120.31/32 [20/0] via 10.0.0.3, vlan4001 onlink, 1d02h41m
    B>* 172.16.120.32/32 [20/0] via 10.0.0.3, vlan4001 onlink, 1d02h41m
    B>* 172.16.120.41/32 [20/0] via 10.0.0.4, vlan4001 onlink, 1d02h41m
    ...

In the output above, the next hops for these routes are specified by
EVPN to be *onlink*, or reachable over the specified SVI. This is
necessary because this interface is not required to have an IP address.
Even if the interface is configured with an IP address, the next hop is
not on the same subnet as it is usually the IP address of the remote
VTEP (part of the underlay IP network).

### <span>Display the Global BGP EVPN Routing Table</span>

Run the `net show bgp l2vpn evpn route` command to display all EVPN
routes, both local and remote. The routes displayed here are based on RD
as they are across VNIs and VRFs:

    cumulus@leaf01:~$ net show bgp l2vpn evpn route 
    BGP table version is 0, local router ID is 10.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
    Route Distinguisher: 10.0.0.1:1
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[32]:[172.16.120.11]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[128]:[2001:172:16:120::11]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[32]:[172.16.120.12]
                        10.0.0.1                          32768 i
    *> [3]:[0]:[32]:[10.0.0.1]
                        10.0.0.1                          32768 i
    Route Distinguisher: 10.0.0.1:2
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[32]:[172.16.130.11]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[32]:[172.16.130.12]
                        10.0.0.1                          32768 i
    *> [3]:[0]:[32]:[10.0.0.1]
                        10.0.0.1                          32768 i
    ...

You can filter the routing table based on EVPN route type. The available
options are shown below:

    cumulus@leaf01:~$ net show bgp l2vpn evpn route type 
        macip      :  MAC-IP (Type-2) route
        multicast  :  Multicast
        prefix     :  An IPv4 or IPv6 prefix
    cumulus@leaf01:~$

### <span>Display a Specific EVPN Route</span>

To drill down on a specific route for more information, run the `net
show bgp l2vpn evpn route rd <rd-value>` command. This command displays
all EVPN routes with that RD and with the path attribute details for
each path. Additional filtering is possible based on route type or by
specifying the MAC and/or IP address. The following example shows a
specific MAC/IP route. The output shows that this remote host is behind
VTEP 10.0.0.4 and is reachable through two paths; one through either
spine switch. This example is from a symmetric routing deployment, so
the route shows both the layer 2 VNI (10200) and the layer 3 VNI
(104001) as well as the EVPN route target attributes corresponding to
each and the associated router MAC address.

    cumulus@leaf01:~$ net show bgp l2vpn evpn route rd 10.0.0.4:3 mac 00:02:00:00:00:10 ip 172.16.130.44
    BGP routing table entry for 10.0.0.4:3:[2]:[0]:[0]:[48]:[00:02:00:00:00:10]:[32]:[172.16.130.44]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp1) s2(swp2)
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:10]:[32]:[172.16.130.44] VNI 10200/104001
      65100 65004
        10.0.0.4 from s2(swp2) (172.16.110.2)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65004:10200 RT:65004:104001 ET:8 Rmac:00:01:00:00:14:00
          AddPath ID: RX 0, TX 97
          Last update: Sun Dec 17 20:57:24 2017
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:10]:[32]:[172.16.130.44] VNI 10200/104001
      65100 65004
        10.0.0.4 from s1(swp1) (172.16.110.1)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65004:10200 RT:65004:104001 ET:8 Rmac:00:01:00:00:14:00
          AddPath ID: RX 0, TX 71
          Last update: Sun Dec 17 20:57:23 2017
     
    Displayed 2 paths for requested prefix
    cumulus@leaf01:~$

{{%notice note%}}

  - Only global VNIs are supported. Even though VNI values are exchanged
    in the type-2 and type-5 routes, the received values are not used
    when installing the routes into the forwarding plane; the local
    configuration is used. You must ensure that the VLAN to VNI mappings
    and the layer 3 VNI assignment for a tenant VRF are uniform
    throughout the network.

  - If the remote host is dual attached, the next hop for the EVPN route
    is the anycast IP address of the remote
    [MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG)
    pair, when MLAG is active.

{{%/notice%}}

The following example shows a prefix (type-5) route. Such a route has
only the layer 3 VNI and the route target corresponding to this VNI.
This route is learned through two paths, one through each spine switch.

    cumulus@leaf01:~$ net show bgp l2vpn evpn route rd 172.16.100.2:3 type prefix
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
    EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
    BGP routing table entry for 172.16.100.2:3:[5]:[0]:[30]:[172.16.100.0]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp1) s2(swp2)
      Route [5]:[0]:[30]:[172.16.100.0] VNI 104001
      65100 65050
        10.0.0.5 from s2(swp2) (172.16.110.2)
          Origin incomplete, localpref 100, valid, external
          Extended Community: RT:65050:104001 ET:8 Rmac:00:01:00:00:01:00
          AddPath ID: RX 0, TX 112
          Last update: Tue Dec 19 00:12:18 2017
      Route [5]:[0]:[30]:[172.16.100.0] VNI 104001
      65100 65050
        10.0.0.5 from s1(swp1) (172.16.110.1)
          Origin incomplete, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65050:104001 ET:8 Rmac:00:01:00:00:01:00
          AddPath ID: RX 0, TX 71
          Last update: Tue Dec 19 00:12:17 2017
     
    Displayed 1 prefixes (2 paths) with this RD (of requested type)
    cumulus@leaf01:~$

### <span>Display the per-VNI EVPN Routing Table</span>

Received EVPN routes are maintained in the global EVPN routing table
(described above), even if there are no appropriate local VNIs to
**import** them into. For example, a spine switch maintains the global
EVPN routing table even though there are no VNIs present on it. When
local VNIs are present, received EVPN routes are imported into the
per-VNI routing tables based on the route target attributes. You can
examine the per-VNI routing table with the `net show bgp l2vpn evpn
route vni <vni>` command:

    cumulus@leaf01:~$ net show bgp l2vpn evpn route vni 10110
    BGP table version is 8, local router ID is 10.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:07]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:07]:[32]:[172.16.120.11]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:07]:[128]:[fe80::202:ff:fe00:7]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:08]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:08]:[32]:[172.16.120.12]
                        10.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:08]:[128]:[fe80::202:ff:fe00:8]
                        10.0.0.1                          32768 i
    *> [3]:[0]:[32]:[10.0.0.1]
                        10.0.0.1                          32768 i
    Displayed 7 prefixes (7 paths)
    cumulus@leaf01:~$

To display the VNI routing table for all VNIs, run the `net show bgp
l2vpn evpn route vni all` command.

### <span>Display the per-VRF BGP Routing Table</span>

When symmetric routing is deployed, received type-2 and type-5 routes
are imported into the VRF routing table (against the corresponding
address-family: IPv4 unicast or IPv6 unicast) based on a match on the
route target attributes. You can examine BGP's VRF routing table using
the `net show bgp vrf <vrf-name> ipv4 unicast` command or the `net show
bgp vrf <vrf-name> ipv6 unicast` command.

    cumulus@leaf01:~$ net show bgp vrf vrf1 ipv4 unicast 
    BGP table version is 8, local router ID is 172.16.120.250
    Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                  i internal, r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network          Next Hop            Metric LocPrf Weight Path
    *  172.16.120.21/32     10.0.0.2                              0 65100 65002 i
    *>                  10.0.0.2                              0 65100 65002 i
    *  172.16.120.22/32     10.0.0.2                              0 65100 65002 i
    *>                  10.0.0.2                              0 65100 65002 i
    *  172.16.120.31/32     10.0.0.3                              0 65100 65003 i
    *>                  10.0.0.3                              0 65100 65003 i
    *  172.16.120.32/32     10.0.0.3                              0 65100 65003 i
    *>                  10.0.0.3                              0 65100 65003 i
    *  172.16.120.41/32     10.0.0.4                              0 65100 65004 i
    *>                  10.0.0.4                              0 65100 65004 i
    *  172.16.120.42/32     10.0.0.4                              0 65100 65004 i
    *>                  10.0.0.4                              0 65100 65004 i
    *  172.16.100.0/24     10.0.0.5                              0 65100 65050 ?
    *>                  10.0.0.5                              0 65100 65050 ?
    *  172.16.100.0/24     10.0.0.6                              0 65100 65050 ?
    *>                  10.0.0.6                              0 65100 65050 ?
    Displayed  8 routes and 16 total paths
    cumulus@leaf01:~$

### <span>Examine MAC Moves</span>

The first time a MAC moves from behind one VTEP to behind another, BGP
associates a MAC Mobility (MM) extended community attribute of sequence
number 1, with the type-2 route for that MAC. From there, each time this
MAC moves to a new VTEP, the MM sequence number increments by 1. You can
examine the MM sequence number associated with a MAC's type-2 route with
the `net show bgp l2vpn evpn route vni <vni> mac <mac>` command. The
sample output below shows the type-2 route for a MAC that has moved
three times:

    cumulus@switch:~$ net show bgp l2vpn evpn route vni 10109 mac 00:02:22:22:22:02
    BGP routing table entry for [2]:[0]:[0]:[48]:[00:02:22:22:22:02]
    Paths: (1 available, best #1)
    Not advertised to any peer
    Route [2]:[0]:[0]:[48]:[00:02:22:22:22:02] VNI 10109
    Local
    6.0.0.184 from 0.0.0.0 (6.0.0.184)
    Origin IGP, localpref 100, weight 32768, valid, sourced, local, bestpath-from-AS Local, best
    Extended Community: RT:650184:10109 ET:8 MM:3
    AddPath ID: RX 0, TX 10350121
    Last update: Tue Feb 14 18:40:37 2017
     
    Displayed 1 paths for requested prefix

### <span>Examine Sticky MAC Addresses</span>

You can identify static or *sticky* MACs in EVPN by the presence of
`MM:0, sticky MAC` in the Extended Community line of the output from
`net show bgp l2vpn evpn route vni <vni> mac <mac>:`

    cumulus@switch:~$ net show bgp l2vpn evpn route vni 10101 mac 00:02:00:00:00:01
    BGP routing table entry for [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
    Paths: (1 available, best #1)
      Not advertised to any peer
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:01] VNI 10101
      Local
        172.16.130.18 from 0.0.0.0 (172.16.130.18)
          Origin IGP, localpref 100, weight 32768, valid, sourced, local, bestpath-from-AS Local, best
          Extended Community: ET:8 RT:60176:10101 MM:0, sticky MAC
          AddPath ID: RX 0, TX 46
          Last update: Tue Apr 11 21:44:02 2017
     
    Displayed 1 paths for requested prefix

## <span>Troubleshooting</span>

To troubleshoot EVPN, enable FRR debug logs. The relevant debug options
are as follows:

  - `debug zebra vxlan` traces VNI addition and deletion (local and
    remote) as well as MAC and neighbor addition and deletion (local and
    remote).

  - `debug zebra kernel` traces actual netlink messages exchanged with
    the kernel, which includes everything, not just EVPN.

  - `debug bgp updates` traces BGP update exchanges, including all
    updates. Output is extended to show EVPN specific information.

  - `debug bgp zebra` traces interactions between BGP and zebra for EVPN
    (and other) routes.

## <span id="src-8362732_EthernetVirtualPrivateNetwork-EVPN-caveats" class="confluence-anchor-link"></span><span>Caveats</span>

The following caveats apply to EVPN in this version of Cumulus Linux:

  - When EVPN is enabled on a switch (VTEP), all locally defined VNIs on
    that switch and other information (such as MAC addresses) pertaining
    to them are advertised to EVPN peers. There is no provision to only
    announce certain VNIs.

  - In a [VXLAN
    active-active](/cumulus-linux/Network_Virtualization/VXLAN_Active-Active_Mode)
    configuration, ARPs are sometimes *not* suppressed even if ARP
    suppression is enabled. This is because the neighbor entries are not
    synchronized between the two switches operating in active-active
    mode by a control plane. This has no impact on forwarding.

  - You must configure the overlay (tenants) in a specific VRF(s) and
    separate from the underlay, which resides in the default VRF. A
    layer 3 VNI mapping for the default VRF is not supported.

  - On the Broadcom Trident II+, Trident 3, and Maverick-based switch,
    when a lookup is done after VXLAN decapsulation on the
    external-facing switch (exit/border leaf), the switch does not
    rewrite the MAC addresses or TTL; for through traffic, packets are
    dropped by the next hop instead of correctly routing from a VXLAN
    overlay network into a non-VXLAN external network (such as the
    Internet). This applies to all forms of VXLAN routing (centralized,
    asymmetric and symmetric) and affects all traffic from VXLAN overlay
    hosts that need to be routed after VXLAN decapsulation on an
    exit/border leaf, including traffic destined to external networks
    (through traffic) and traffic destined to the exit leaf SVI address.
    
    To work around this issue, modify the external-facing interface for
    each VLAN sub-interface on the exit leaf by creating a temporary VNI
    and associating it with the existing VLAN ID.
    
    For example, if the expected interface configuration is:
    
        auto swp3.2001
        iface swp3.2001
            vrf vrf1
            address 10.0.0.2/24
        # where swp3 is the external facing port and swp3.2001 is the VLAN sub-interface
         
        auto bridge
        iface bridge
            bridge-vlan-aware yes
            bridge ports vx-4001
            bridge-vids 4001
         
        auto vx-4001
        iface vx-4001
            vxlan-id 4001
            <... usual vxlan config ...>
            bridge-access 4001
        # where vnid 4001 represents the L3 VNI
         
        auto vlan4001
        iface vlan4001
            vlan-id 4001
            vlan-raw-device bridge
            vrf vrf1
    
    Modify the configuration as follows:
    
        auto swp3
        iface swp3
            bridge-access 2001
        # associate the port (swp3) with bridge 2001
         
        auto bridge
        iface bridge
            bridge-vlan-aware yes
            bridge ports swp3 vx-4001 vx-16000000
            bridge-vids 2001
        # where vx-4001 is the existing VNI and vx-16000000 is a new temporary VNI
        # this is now bridging the port (swp3), the VNI (vx-4001),
        # and the new temporary VNI (vx-16000000)
        # the bridge VLAN ID is now 2001
         
        auto vlan2001
        iface vlan2001
            vlan-id 2001
            vrf vrf1
            address 10.0.0.2/24
            vlan-raw-device bridge
        # create a VLAN 2001 with the associated VRF and IP address
         
        auto vx-16000000
        iface vx-16000000
            vxlan-id 16000000
            bridge-access 2001
            <... usual vxlan config ...>
        # associate the temporary VNI (vx-16000000) with bridge 2001
         
        auto vx-4001
        iface vx-4001
            vxlan-id 4001
            <... usual vxlan config ...>
            bridge-access 4001
        # where vnid 4001 represents the L3 VNI
         
        auto vlan4001
        iface vlan4001
            vlan-id 4001
            vlan-raw-device bridge
            vrf vrf1
    
    If an MLAG pair is used instead of a single exit/border leaf, add
    the same temporary VNIs on both switches of the MLAG pair.

## <span>Example Configurations</span>

  - Basic Clos (4x2) for bridging

  - Clos with MLAG and centralized routing

  - Clos with MLAG and asymmetric routing

  - Basic Clos with symmetric routing and exit leafs

### <span>Basic Clos (4x2) for Bridging</span>

The following example configuration shows a basic Clos topology for
bridging.

{{% imgOld 1 %}}

#### <span>leaf01 and leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf01 /etc/network/interfaces
<pre><code>cumulus@leaf01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  920 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.8
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152 
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152 
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1
 
auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>cumulus@leaf02:~$ cat /etc/network/interfaces 
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.7
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1
 
auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off</code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/frr/frr.conf
<pre><code>cumulus@leaf01:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>leaf02 /etc/frr/frr.conf
<pre><code>cumulus@leaf02:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>leaf03 and leaf04 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf03 /etc/network/interfaces
<pre><code>cumulus@leaf03:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.10
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1
 
auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off</code></pre></td>
<td>leaf04 /etc/network/interfaces
<pre><code>cumulus@leaf04:~$ cat /etc/network/interfaces 
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    # post-up sysctl -w net.ipv4.conf.peerlink-3/4094.accept_local=1
    clagd-backup-ip 10.0.0.9
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto VxLanA-1
iface VxLanA-1
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1001
    bridge-pvid 1
 
auto vlan1
iface vlan1
    vlan-id 1
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device VxLanA-1
    ip-forward off
 
auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device VxLanA-1
    ip-forward off</code></pre></td>
</tr>
<tr class="even">
<td>leaf03 /etc/frr/frr.conf
<pre><code>cumulus@leaf03:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>leaf04 /etc/frr/frr.conf
<pre><code>cumulus@leaf04:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>spine01 and spine02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>spine01 /etc/network/interfaces
<pre><code>cumulus@spine01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
 
auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202</code></pre></td>
<td>spine02 /etc/network/interfaces
<pre><code>cumulus@spine02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
 
auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/frr/frr.conf
<pre><code>cumulus@spine01:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>spine02 /etc/frr/frr.conf
<pre><code>cumulus@spine02:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

### <span>Clos Configuration with MLAG and Centralized Routing</span>

The following example configuration shows a basic Clos topology with
centralized routing. MLAG is configured between leaf switches.

{{% imgOld 2 %}}

#### <span>leaf01 and leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf01 /etc/network/interfaces
<pre><code>cumulus@leaf01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.8
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1
 
auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2
 
auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>cumulus@leaf02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.7
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1
 
auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2
 
auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2 </code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/frr/frr.conf
<pre><code>cumulus@leaf01:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-default-gw
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
<td>leaf02 /etc/frr/frr.conf
<pre><code>cumulus@leaf02:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-default-gw
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
</tr>
</tbody>
</table>

#### <span>leaf03 and leaf04 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf03 /etc/network/interfaces
<pre><code>cumulus@leaf03:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.10
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device bridge
    ip-forward off
 
auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device bridge
    ip-forward off
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    vlan-id 1002
    vlan-raw-device bridge
    ip-forward off
 
auto vlan1003
iface vlan1003
    vlan-id 1003
    vlan-raw-device bridge
    ip-forward off </code></pre></td>
<td>leaf04 /etc/network/interfaces
<pre><code>cumulus@leaf04:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.9
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.9
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    vlan-id 1000
    vlan-raw-device bridge
    ip-forward off
 
auto vlan1001
iface vlan1001
    vlan-id 1001
    vlan-raw-device bridge
    ip-forward off
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    vlan-id 1002
    vlan-raw-device bridge
    ip-forward off
 
auto vlan1003
iface vlan1003
    vlan-id 1003
    vlan-raw-device bridge
    ip-forward off </code></pre></td>
</tr>
<tr class="even">
<td>leaf03 /etc/frr/frr.conf
<pre><code>cumulus@leaf03:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
<td>leaf04 /etc/frr/frr.conf
<pre><code>cumulus@leaf04:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
</tr>
</tbody>
</table>

#### <span>spine01 and spine02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>spine01 /etc/network/interfaces
<pre><code>cumulus@spine01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
 
auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202</code></pre></td>
<td>spine02 /etc/network/interfaces
<pre><code>cumulus@spine02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
 
auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/frr/frr.conf
<pre><code>cumulus@spine01:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
<td>spine02 /etc/frr/frr.conf
<pre><code>cumulus@spine02:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
</tr>
</tbody>
</table>

### <span>Clos Configuration with MLAG and EVPN Asymetric Routing</span>

The following example configuration is a basic Clos topology with EVPN
asymmetric routing. MLAG is configured between leaf switches.

{{% imgOld 3 %}}

#### <span>leaf01 and leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf01 /etc/network/interfaces
<pre><code>cumulus@leaf01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.7/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.8
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.7
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1
 
auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2
 
auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>cumulus@leaf02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.8/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 172.16.100.7
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:01
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.7
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.8
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1
 
auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2
 
auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2</code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/frr/frr.conf
<pre><code> cumulus@leaf01:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65542
 bgp router-id 10.0.0.7
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>leaf02 /etc/frr/frr.conf
<pre><code>cumulus@leaf02:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65543
 bgp router-id 10.0.0.8
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>leaf03 and leaf04 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf03 /etc/network/interfaces
<pre><code>cumulus@leaf03:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.9/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 36.0.0.9
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.9/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 4096
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.10
    clagd-backup-ip 10.0.0.10
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.9
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    address 45.0.0.2/24
    address 2001:fee1::2/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1
 
auto vlan1001
iface vlan1001
    address 45.0.1.2/24
    address 2001:fee1:0:1::2/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    address 45.0.2.2/24
    address 2001:fee1:0:2::2/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2
 
auto vlan1003
iface vlan1003
    address 45.0.3.2/24
    address 2001:fee1:0:3::2/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2</code></pre></td>
<td>leaf04 /etc/network/interfaces
<pre><code>cumulus@leaf04:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.10/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
    clagd-vxlan-anycast-ip 36.0.0.9
 
auto uplink-1
iface uplink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto uplink-2
iface uplink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto peerlink-3
iface peerlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto peerlink-3.4094
iface peerlink-3.4094
    address 169.254.0.10/30
    mtu 9202
    alias clag and vxlan communication primary path
    clagd-priority 8192
    clagd-sys-mac 44:38:39:ff:ff:02
    clagd-peer-ip 169.254.0.9
    clagd-backup-ip 10.0.0.9
 
auto hostbond4
iface hostbond4
    bond-slaves swp7
    mtu  9152
    clag-id 1
    bridge-pvid 1000
 
auto hostbond5
iface hostbond5
    bond-slaves swp8
    mtu  9152
    clag-id 2
    bridge-pvid 1001
 
auto vx-101000
iface vx-101000
    vxlan-id 101000
    bridge-access 1000
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101001
iface vx-101001
    vxlan-id 101001
    bridge-access 1001
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101002
iface vx-101002
    vxlan-id 101002
    bridge-access 1002
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto vx-101003
iface vx-101003
    vxlan-id 101003
    bridge-access 1003
    vxlan-local-tunnelip 10.0.0.10
    bridge-learning off
    bridge-arp-nd-suppress on
    mstpctl-portbpdufilter yes
    mstpctl-bpduguard  yes
    mtu 9152
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports vx-101000 vx-101001 vx-101002 vx-101003 peerlink-3 hostbond4 hostbond5
    bridge-stp on
    bridge-vids 1000-1003
    bridge-pvid 1
 
auto vrf1
iface vrf1
    vrf-table auto
 
auto vlan1000
iface vlan1000
    address 45.0.0.3/24
    address 2001:fee1::3/64
    vlan-id 1000
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.0.1/24 2001:fee1::1/64
    vrf vrf1
 
auto vlan1001
iface vlan1001
    address 45.0.1.3/24
    address 2001:fee1:0:1::3/64
    vlan-id 1001
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.1.1/24 2001:fee1:0:1::1/64
    vrf vrf1
 
auto vrf2
iface vrf2
    vrf-table auto
 
auto vlan1002
iface vlan1002
    address 45.0.2.3/24
    address 2001:fee1:0:2::3/64
    vlan-id 1002
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.2.1/24 2001:fee1:0:2::1/64
    vrf vrf2
 
auto vlan1003
iface vlan1003
    address 45.0.3.3/24
    address 2001:fee1:0:3::3/64
    vlan-id 1003
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 45.0.3.1/24 2001:fee1:0:3::1/64
    vrf vrf2 </code></pre></td>
</tr>
<tr class="even">
<td>leaf03 /etc/frr/frr.conf
<pre><code>cumulus@leaf03:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65544
 bgp router-id 10.0.0.9
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
<td>leaf04 /etc/frr/frr.conf
<pre><code>cumulus@leaf04:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface peerlink-3.4094
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface uplink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65545
 bgp router-id 10.0.0.10
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor peerlink-3.4094 interface v6only remote-as external
 neighbor uplink-1 interface v6only remote-as external
 neighbor uplink-2 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor peerlink-3.4094 activate
  neighbor uplink-1 activate
  neighbor uplink-2 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor uplink-1 activate
  neighbor uplink-2 activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
</tr>
</tbody>
</table>

#### <span>spine01 and spine02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>spine01 /etc/network/interfaces
<pre><code>cumulus@spine01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.5/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
 
auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202</code></pre></td>
<td>spine02 /etc/network/interfaces
<pre><code>cumulus@spine02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5)
 
# The primary network interface
auto eth0
iface eth0 inet dhcp
 
# Include any platform-specific interface configuration
#source /etc/network/interfaces.d/*.if
 
auto lo
iface lo
    address 10.0.0.6/32
    alias BGP un-numbered Use for Vxlan Src Tunnel
 
auto downlink-1
iface downlink-1
    bond-slaves swp1 swp2
    mtu  9202
 
auto downlink-2
iface downlink-2
    bond-slaves swp3 swp4
    mtu  9202
 
auto downlink-3
iface downlink-3
    bond-slaves swp5 swp6
    mtu  9202
 
auto downlink-4
iface downlink-4
    bond-slaves swp7 swp8
    mtu  9202</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/frr/frr.conf
<pre><code>cumulus@spine01:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.5
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
! </code></pre></td>
<td>spine02 /etc/frr/frr.conf
<pre><code>cumulus@spine02:~$ cat /etc/frr/frr.conf
 
log file /var/log/frr/bgpd.log
!
log timestamp precision 6
!
interface downlink-1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface downlink-4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 64435
 bgp router-id 10.0.0.6
 coalesce-time 1000
 bgp bestpath as-path multipath-relax
 neighbor downlink-1 interface v6only remote-as external
 neighbor downlink-2 interface v6only remote-as external
 neighbor downlink-3 interface v6only remote-as external
 neighbor downlink-4 interface v6only remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
  neighbor downlink-1 allowas-in origin
  neighbor downlink-2 allowas-in origin
  neighbor downlink-3 allowas-in origin
  neighbor downlink-4 allowas-in origin
 exit-address-family
 !
 address-family ipv6 unicast
  redistribute connected
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor downlink-1 activate
  neighbor downlink-2 activate
  neighbor downlink-3 activate
  neighbor downlink-4 activate
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

### <span>Basic Clos Configuration with EVPN Symmetric Routing</span>

The following example configuration is a basic Clos topology with EVPN
symmetric routing with external prefix (type-5) routing via dual,
non-MLAG exit leafs connected to an edge router. Here is the topology
diagram:

{{% imgOld 4 %}}

#### <span>leaf01 and leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf01 /etc/network/interfaces
<pre><code>cumulus@leaf01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 10.0.0.1/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
    bridge-access 110
 
auto swp4
iface swp4
    bridge-access 110
 
auto swp5
iface swp5
    bridge-access 210
 
auto swp6
iface swp6
    bridge-access 210
 
auto vni110
iface vni110
    vxlan-id 10110
    vxlan-local-tunnelip 10.0.0.1
    bridge-learning off
    bridge-access 110
    bridge-arp-nd-suppress on
 
auto vni210
iface vni210
    vxlan-id 10210
    vxlan-local-tunnelip 10.0.0.1
    bridge-learning off
    bridge-access 210
    bridge-arp-nd-suppress on
 
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.1
    bridge-learning off
    bridge-access 4001
 
auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.1
    bridge-learning off
    bridge-access 4002
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni110 vni210 vni4001 vni4002
    bridge-stp on
    bridge-vids 110 210
 
# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto
 
auto vrf2
iface vrf2
    vrf-table auto
 
# Tenant SVIs - anycast GW
auto vlan110
iface vlan110
    address 172.16.120.1/24
    vlan-id 110
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1
 
auto vlan210
iface vlan210
    address 172.16.130.1/24
    vlan-id 210
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2
 
# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>cumulus@leaf02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 10.0.0.2/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
    bridge-access 120
 
auto swp4
iface swp4
    bridge-access 120
 
auto swp5
iface swp5
    bridge-access 220
 
auto swp6
iface swp6
    bridge-access 220
 
auto vni120
iface vni120
    vxlan-id 10120
    vxlan-local-tunnelip 10.0.0.2
    bridge-learning off
    bridge-access 120
    bridge-arp-nd-suppress on
 
auto vni220
iface vni220
    vxlan-id 10220
    vxlan-local-tunnelip 10.0.0.2
    bridge-learning off
    bridge-access 220
    bridge-arp-nd-suppress on
 
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.2
    bridge-learning off
    bridge-access 4001
 
auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.2
    bridge-learning off
    bridge-access 4002
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni120 vni220 vni4001 vni4002
    bridge-stp on
    bridge-vids 120 220
 
# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto
 
auto vrf2
iface vrf2
    vrf-table auto
 
# Tenant SVIs - anycast GW
auto vlan120
iface vlan120
    address 172.16.120.2/24
    vlan-id 120
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1
 
auto vlan220
iface vlan220
    address 172.16.130.2/24
    vlan-id 220
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2
 
# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2</code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/frr/frr.conf
<pre><code>cumulus@leaf01:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65001
 bgp router-id 10.0.0.1
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.1/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>leaf02 /etc/frr/frr.conf
<pre><code>cumulus@leaf02:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65002
 bgp router-id 10.0.0.2
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.2/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>leaf03 and leaf04 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf03 /etc/network/interfaces
<pre><code>cumulus@leaf03:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 10.0.0.3/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
    bridge-access 130
 
auto swp4
iface swp4
    bridge-access 130
 
auto swp5
iface swp5
    bridge-access 230
 
auto swp6
iface swp6
    bridge-access 230
 
auto vni130
iface vni130
    vxlan-id 10130
    vxlan-local-tunnelip 10.0.0.3
    bridge-learning off
    bridge-access 130
    bridge-arp-nd-suppress on
 
auto vni230
iface vni230
    vxlan-id 10230
    vxlan-local-tunnelip 10.0.0.3
    bridge-learning off
    bridge-access 230
    bridge-arp-nd-suppress on
 
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.3
    bridge-learning off
    bridge-access 4001
 
auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.3
    bridge-learning off
    bridge-access 4002
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni130 vni230 vni4001 vni4002
    bridge-stp on
    bridge-vids 130 230
 
# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto
 
auto vrf2
iface vrf2
    vrf-table auto
 
# Tenant SVIs - anycast GW
auto vlan130
iface vlan130
    address 172.16.120.3/24
    vlan-id 130
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1
 
auto vlan230
iface vlan230
    address 172.16.130.3/24
    vlan-id 230
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2
 
# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2</code></pre></td>
<td>leaf04 /etc/network/interfaces
<pre><code>cumulus@leaf04:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 10.0.0.4/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
# L2 interfaces - ports, vxlan and bridge
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
    bridge-access 140
 
auto swp4
iface swp4
    bridge-access 140
 
auto swp5
iface swp5
    bridge-access 240
 
auto swp6
iface swp6
    bridge-access 240
 
auto vni140
iface vni140
    vxlan-id 10140
    vxlan-local-tunnelip 10.0.0.4
    bridge-learning off
    bridge-access 140
    bridge-arp-nd-suppress on
 
auto vni240
iface vni240
    vxlan-id 10240
    vxlan-local-tunnelip 10.0.0.4
    bridge-learning off
    bridge-access 240
    bridge-arp-nd-suppress on
 
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.4
    bridge-learning off
    bridge-access 4001
 
auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.4
    bridge-learning off
    bridge-access 4002
 
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3 swp4 swp5 swp6 vni140 vni240 vni4001 vni4002
    bridge-stp on
    bridge-vids 140 240
 
# Tenants (VRFs)
auto vrf1
iface vrf1
    vrf-table auto
 
auto vrf2
iface vrf2
    vrf-table auto
 
# Tenant SVIs - anycast GW
auto vlan140
iface vlan140
    address 172.16.120.4/24
    vlan-id 140
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1
 
auto vlan240
iface vlan240
    address 172.16.130.4/24
    vlan-id 240
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2
 
# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2</code></pre></td>
</tr>
<tr class="even">
<td>leaf03 /etc/frr/frr.conf
<pre><code>cumulus@leaf03:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65003
 bgp router-id 10.0.0.3
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.3/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>leaf04 /etc/frr/frr.conf
<pre><code>cumulus@leaf04:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65004
 bgp router-id 10.0.0.4
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.4/32
 exit-address-family
!
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
router bgp 65004 vrf vrf1
 bgp router-id 172.16.120.4
 neighbor 172.16.120.100 remote-as external
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
router bgp 65004 vrf vrf2
 bgp router-id 172.16.130.4
 neighbor 172.16.130.100 remote-as external
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>spine01 and spine02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>spine01 /etc/network/interfaces
<pre><code>cumulus@spine01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 172.16.110.1/24
 
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4
 
auto swp5
iface swp5
 
auto swp6
iface swp6</code></pre></td>
<td>spine02 /etc/network/interfaces
<pre><code>cumulus@spine02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 172.16.110.2/24
 
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4
 
auto swp5
iface swp5
 
auto swp6
iface swp6</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/frr/frr.conf
<pre><code>cumulus@spine01:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
router bgp 65100
 bgp router-id 172.16.110.1
 neighbor LEAF peer-group
 neighbor LEAF remote-as external
 neighbor LEAF timers 10 30
 neighbor swp1 interface peer-group LEAF
 neighbor swp2 interface peer-group LEAF
 neighbor swp3 interface peer-group LEAF
 neighbor swp4 interface peer-group LEAF
 neighbor BORDER-LEAF peer-group
 neighbor BORDER-LEAF remote-as external
 neighbor BORDER-LEAF timers 10 30
 neighbor swp5 interface peer-group BORDER-LEAF
 neighbor swp6 interface peer-group BORDER-LEAF
 !
 address-family ipv4 unicast
  network 172.16.110.1/24
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>spine02 /etc/frr/frr.conf
<pre><code>cumulus@spine02:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
router bgp 65100
 bgp router-id 172.16.110.2
 neighbor LEAF peer-group
 neighbor LEAF remote-as external
 neighbor LEAF timers 10 30
 neighbor swp1 interface peer-group LEAF
 neighbor swp2 interface peer-group LEAF
 neighbor swp3 interface peer-group LEAF
 neighbor swp4 interface peer-group LEAF
 neighbor BORDER-LEAF peer-group
 neighbor BORDER-LEAF remote-as external
 neighbor BORDER-LEAF timers 10 30
 neighbor swp5 interface peer-group BORDER-LEAF
 neighbor swp6 interface peer-group BORDER-LEAF
 !
 address-family ipv4 unicast
  network 172.16.110.2/24
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor LEAF activate
  neighbor BORDER-LEAF activate
  neighbor LEAF route-reflector-client
  neighbor BORDER-LEAF route-reflector-client
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>border-leaf01 and border-leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>border-leaf01 /etc/network/interfaces
<pre><code>cumulus@border-leaf01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0 inet dhcp
 
auto lo:1
iface lo:1
    address 10.0.0.5/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
# Physical interfaces
auto swp1s0
iface swp1s0
 
auto swp1s1
iface swp1s1
 
auto swp1s2
iface swp1s2
    bridge-vids 2001 2002
 
auto swp1s3
iface swp1s3
    bridge-access 150
 
auto swp2s0
iface swp2s0
    bridge-access 250
 
auto vni150
iface vni150
    vxlan-id 10150
    vxlan-local-tunnelip 10.0.0.5
    bridge-learning off
    bridge-access 150
    bridge-arp-nd-suppress on
    
auto vni250
iface vni250
    vxlan-id 10250
    vxlan-local-tunnelip 10.0.0.5
    bridge-learning off
    bridge-access 250
    bridge-arp-nd-suppress on
 
# Tenant VRFs
auto vrf1
iface vrf1
    vrf-table auto
 
auto vrf2
iface vrf2
    vrf-table auto
 
# VxLAN interfaces (VLAN to VNI mappings)
# Need only the L3 VxLAN interfaces
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.5
    bridge-learning off
    bridge-access 4001
 
auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.5
    bridge-learning off
    bridge-access 4002
 
# Bridge
auto bridge
iface bridge
      bridge-vlan-aware yes
      bridge-ports swp4 swp5 vni160 vni260 vni4001 vni4002
      bridge-stp on
      bridge-vids 160 260 2001 2002
 
# Tenant SVIs - anycast GW
auto vlan160
iface vlan160
    address 172.16.120.1/24
    vlan-id 160
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1
 
auto vlan260
iface vlan260
    address 172.16.130.2/24
    vlan-id 260
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2
 
# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
# External-facing L3 VLAN interface per tenant (towards WAN edge)
#auto swp1s2.4001
#iface swp1s2.4001
#    address 172.16.100.2/30
#    vrf vrf1
#
#auto swp1s2.4002
#iface swp1s2.4002
#    address 172.16.100.6/30
#    vrf vrf2
#
# configuration below is a workaround for RN-766
#
auto vlan2001
iface vlan2001
    vlan-id 2001
    vlan-raw-device bridge
    vrf vrf1
    address 172.16.100.2/30
 
auto vlan2002
iface vlan2002
    vlan-id 2002
    vlan-raw-device bridge
    vrf vrf2
    address 172.16.100.6/30
 
auto vni16001
iface vni16001
    vxlan-id 16001
    vxlan-local-tunnelip 10.0.0.5
    bridge-learning off
    bridge-access 2001
 
auto vni16002
iface vni16002
    vxlan-id 16002
    vxlan-local-tunnelip 10.0.0.5
    bridge-learning off
    bridge-access 2002</code></pre></td>
<td>border-leaf02 /etc/network/interfaces
<pre><code>cumulus@border-leaf02:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 10.0.0.6/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
# Physical interfaces
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4
    bridge-access 160
 
auto swp5
iface swp5
    bridge-access 260
 
auto vni160
iface vni160
    vxlan-id 10160
    vxlan-local-tunnelip 10.0.0.6
    bridge-learning off
    bridge-access 160
    bridge-arp-nd-suppress on
 
auto vni260
iface vni260
    vxlan-id 10260
    vxlan-local-tunnelip 10.0.0.6
    bridge-learning off
    bridge-access 260
    bridge-arp-nd-suppress on
 
# Tenant VRFs
auto vrf1
iface vrf1
    vrf-table auto
 
auto vrf2
iface vrf2
    vrf-table auto
 
# VxLAN interfaces (VLAN to VNI mappings)
# Need only the L3 VxLAN interfaces
auto vni4001
iface vni4001
    vxlan-id 104001
    vxlan-local-tunnelip 10.0.0.6
    bridge-learning off
    bridge-access 4001
 
auto vni4002
iface vni4002
    vxlan-id 104002
    vxlan-local-tunnelip 10.0.0.6
    bridge-learning off
    bridge-access 4002
 
# Bridge
auto bridge
iface bridge
      bridge-vlan-aware yes
      bridge-ports swp4 swp5 vni160 vni260 vni4001 vni4002
      bridge-stp on
      bridge-vids 160 260 2001 2002
 
# Tenant SVIs - anycast GW
auto vlan160
iface vlan160
    address 172.16.120.1/24
    vlan-id 160
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.120.250/24
    vrf vrf1
 
auto vlan260
iface vlan260
    address 172.16.130.2/24
    vlan-id 260
    vlan-raw-device bridge
    address-virtual 00:00:5e:00:01:01 172.16.130.250/24
    vrf vrf2
 
# L3 VLAN interface per tenant (for L3 VNI)
auto vlan4001
iface vlan4001
    vlan-id 4001
    vlan-raw-device bridge
    vrf vrf1
 
auto vlan4002
iface vlan4002
    vlan-id 4002
    vlan-raw-device bridge
    vrf vrf2
 
# External-facing L3 VLAN interface per tenant (towards WAN edge)
# auto swp3.4001
# iface swp3.4001
#     address 172.16.101.2/30
#     vrf vrf1
#  
# auto swp3.4002
# iface swp3.4002
#     address 172.16.101.6/30
#     vrf vrf2
#
# configuration below is a workaround for RN-766
#
auto vlan2001
iface vlan2001
    vlan-id 2001
    vlan-raw-device bridge
    vrf vrf1
    address 172.16.101.2/30
 
auto vlan2002
iface vlan2002
    vlan-id 2002
    vlan-raw-device bridge
    vrf vrf2
    address 172.16.101.6/30                         
 
auto vni16001
iface vni16001
    vxlan-id 16001
    vxlan-local-tunnelip 10.0.0.6
    bridge-learning off
    bridge-access 2001
 
auto vni16002
iface vni16002
    vxlan-id 16002
    vxlan-local-tunnelip 10.0.0.6
    bridge-learning off
    bridge-access 2002</code></pre></td>
</tr>
<tr class="even">
<td>border-leaf01 /etc/frr/frr.conf
<pre><code>cumulus@border-leaf01:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1s0
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp1s1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65005
 bgp router-id 10.0.0.5
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 1200 4800
 neighbor swp1s0 interface peer-group SPINE
 neighbor swp1s1 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.5/32
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
router bgp 65005 vrf vrf1
 bgp router-id 172.16.100.2
 neighbor 172.16.100.1 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65005 vrf vrf2
 bgp router-id 172.16.100.6
 neighbor 172.16.100.5 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
<td>border-leaf02 /etc/frr/frr.conf
<pre><code>cumulus@border-leaf02:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
vrf vrf1
 vni 104001
vrf vrf2
 vni 104002
!
interface swp1
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
interface swp2
 no ipv6 nd suppress-ra
 ipv6 nd ra-interval 10
!
router bgp 65005
 bgp router-id 10.0.0.6
 neighbor SPINE peer-group
 neighbor SPINE remote-as external
 neighbor SPINE timers 10 30
 neighbor swp1 interface peer-group SPINE
 neighbor swp2 interface peer-group SPINE
 !
 address-family ipv4 unicast
  network 10.0.0.6/32
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor SPINE activate
  advertise-all-vni
 exit-address-family
!
router bgp 65005 vrf vrf1
 bgp router-id 172.16.100.2
 neighbor 172.16.100.1 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
router bgp 65005 vrf vrf2
 bgp router-id 172.16.100.6
 neighbor 172.16.100.5 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected
 exit-address-family
 !
 address-family l2vpn evpn
  advertise ipv4 unicast
 exit-address-family
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>

#### <span>router01 Configurations</span>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td>router01 /etc/network/interfaces
<pre><code>cumulus@router01:~$ cat /etc/network/interfaces
 
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).
 
# The loopback network interface
auto lo
iface lo inet loopback
 
auto eth0
iface eth0
    address 192.168.0.15/24
    gateway 192.168.0.2
 
auto lo:1
iface lo:1
    address 120.0.0.1/32
    #pre-up sysctl -w net.ipv4.neigh.default.gc_thresh1=0
    #pre-up sysctl -w net.ipv4.route.gc_timeout=60
    #pre-up sysctl -w net.ipv4.neigh.default.base_reachable_time_ms=240000
 
auto swp1
iface swp1
 
auto swp1.2001
iface swp1.2001
    address 172.16.100.1/24
 
auto swp1.2002
iface swp1.2002
    address 172.16.100.5/24
 
auto swp2
iface swp2
 
auto swp2.4001
iface swp2.4001
    address 172.16.100.1/24
 
auto swp2.4002
iface swp2.4002
    address 172.16.100.5/24
 
auto swp3
iface swp3
    address 81.1.1.1/24
 
auto swp4
iface swp4
    address 81.1.2.1/24
 
auto swp5
iface swp5
    address 81.1.3.1/24
 
auto swp6
iface swp6
    address 81.1.4.1/24</code></pre></td>
</tr>
<tr class="even">
<td>router01 /etc/frr/frr.conf
<pre><code>cumulus@router01:~$ cat /etc/frr/frr.conf 
 
log file /var/log/frr/frr.log
log timestamp precision 6
!
password CumulusLinux!
enable password CumulusLinux!
!
router bgp 65200
 bgp router-id 120.0.0.1
 neighbor 172.16.100.2 remote-as external
 neighbor 172.16.100.6 remote-as external
 neighbor 172.16.100.2 remote-as external
 neighbor 172.16.100.6 remote-as external
 !
 address-family ipv4 unicast
  redistribute connected route-map HOST_ALLOW
 exit-address-family
!
ip prefix-list HOSTS seq 1 permit 81.1.1.0/24
ip prefix-list HOSTS seq 2 permit 81.1.2.0/24
ip prefix-list HOSTS seq 3 permit 81.1.3.0/24
ip prefix-list HOSTS seq 4 permit 81.1.4.0/24
ip prefix-list HOSTS seq 5 deny any
!
route-map HOST_ALLOW permit 1
 match ip address prefix-list HOSTS
!
!
line vty
 exec-timeout 0 0
!</code></pre></td>
</tr>
</tbody>
</table>
