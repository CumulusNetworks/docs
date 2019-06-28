---
title: Ethernet Virtual Private Network - EVPN
author: Cumulus Networks
weight: 143
aliases:
 - /display/CL35/Ethernet+Virtual+Private+Network+-+EVPN
 - /pages/viewpage.action?pageId=8357510
pageID: 8357510
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
VXLAN is the de facto technology for implementing network virtualization
in the data center, enabling layer 2 segments to be extended over an IP
core (the underlay). The initial definition of VXLAN
([RFC 7348](https://tools.ietf.org/html/rfc7348)) did not include any
control plane and relied on a flood-and-learn approach for MAC address
learning. An alternate deployment model was to use a controller or a
technology such as [Lightweight Network Virtualization
(LNV)](/display/CL35/Lightweight+Network+Virtualization+-+LNV+Overview)
in Cumulus Linux.

{{%notice note%}}

When you are using EVPN, you cannot use LNV at the same time.

{{%/notice%}}

Ethernet Virtual Private Network (EVPN) is a standards-based control
plane for [VXLAN](/version/cumulus-linux-35/Network_Virtualization/)
defined in [RFC 7432](https://tools.ietf.org/html/rfc7432) and
[draft-ietf-bess-evpn-overlay](https://datatracker.ietf.org/doc/draft-ietf-bess-evpn-overlay/)
that allows for building and deploying VXLANs at scale. It relies on
multi-protocol BGP (MP-BGP) for exchanging information and is based on
BGP-MPLS IP VPNs ([RFC 4364](https://tools.ietf.org/html/rfc4364)).
Hence, it has provisions to enable not only bridging between end systems
in the same layer 2 segment but also routing between different segments
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
    mode](/version/cumulus-linux-35/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode).
    MAC synchronization between the peer switches is done using
    [MLAG](/version/cumulus-linux-35/Layer_1_and_2/Multi-Chassis_Link_Aggregation_-_MLAG).

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
[NCLU](/version/cumulus-linux-35/System_Configuration/Network_Command_Line_Utility_-_NCLU/).

{{%notice note%}}

For Cumulus Linux 3.4 and later releases, the routing control plane
(including EVPN) is installed as part of the
[FRRouting](https://frrouting.org) (FRR) package. For more information
about FRR, refer to the [FRR
Overview](/display/CL35/FRRouting+Overview).

{{%/notice%}}

## <span>Basic EVPN Configuration</span>

The following three steps represent the fundamental configuration to use
EVPN as the control plane for VXLAN. These steps are in addition to
configuring VXLAN interfaces, attaching them to a bridge and mapping
VLANs to VNIs.

1.  Enable EVPN route exchange (that is, address-family L2VPN/EVPN)
    between BGP peers

2.  Enable EVPN on the system to advertise VNIs and host reachability
    information (MAC addresses learned on associated VLANs) to BGP peers

3.  Disable MAC learning on VXLAN interfaces as EVPN is responsible for
    installing remote MACs

There are additional steps (configuration) to enable ARP/ND suppression,
provision inter-subnet routing, and so forth. These steps depend on the
deployment scenario. Various other BGP parameters can also be
configured, if desired.

### <span>Enabling EVPN between BGP Neighbors</span>

You enable EVPN between
[BGP](/version/cumulus-linux-35/Layer_3/Border_Gateway_Protocol_-_BGP)
neighbors by adding the address family *evpn* to the existing neighbor
address-family activation command.

For a non-VTEP device that is merely participating in EVPN route
exchange, such as a spine switch (the network deployment uses hop-by-hop
eBGP or the switch is acting as an iBGP route reflector), activating the
interface for the EVPN address family is the fundamental configuration
needed in
[FRRouting](/version/cumulus-linux-35/Layer_3/FRRouting_Overview/).
Additional configuration options for specific scenarios are described
later on in this chapter.

The other BGP neighbor address-family-specific configurations supported
for EVPN are `allowas-in` and `route-reflector-client`.

To configure an EVPN route exchange with a BGP peer, you must activate
the peer or peer-group within the EVPN address-family:

    cumulus@switch:~$ net add bgp autonomous-system 65000
    cumulus@switch:~$ net add bgp neighbor swp1 remote-as external
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp1 activate
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Adjust the `remote-as` above to be appropriate for your environment.

{{%/notice%}}

{{%notice note%}}

The command syntax `bgp evpn` is also permitted for backwards
compatibility with prior versions of Cumulus Linux, but the syntax `bgp
l2vpn evpn` is recommended in order to standardize the BGP
address-family configuration to the AFI/SAFI format.

{{%/notice%}}

These commands create the following configuration snippet in
`/etc/frr/frr.conf`:

    router bgp 65000
     neighbor swp1 interface remote-as external
     address-family l2vpn evpn
      neighbor swp1 activate

The above configuration does not result in BGP knowing about the local
VNIs defined on the system and advertising them to peers. This requires
additional configuration, [as described
below](#src-8357510_EthernetVirtualPrivateNetwork-EVPN-allvnis).

### <span id="src-8357510_EthernetVirtualPrivateNetwork-EVPN-allvnis" class="confluence-anchor-link"></span><span>Advertising All VNIs</span>

A single configuration variable enables the BGP control plane for all
VNIs configured on the switch. Set the variable `advertise-all-vni` to
provision all locally configured VNIs to be advertised by the BGP
control plane. FRR is not aware of any local VNIs and MACs and hosts
(neighbors) associated with those VNIs until `advertise-all-vni` is
configured.

To build upon the previous example, run the following commands to
advertise all VNIs:

    cumulus@switch:~$ net add bgp autonomous-system 65000
    cumulus@switch:~$ net add bgp neighbor swp1 remote-as external
    cumulus@switch:~$ net add bgp l2vpn evpn neighbor swp1 activate 
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Adjust the `remote-as` above to be appropriate for your environment.

{{%/notice%}}

These commands create the following configuration snippet in
`/etc/frr/frr.conf`:

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

### <span>Auto-derivation of RDs and RTs</span>

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

### <span>User-defined RDs and RTs</span>

EVPN also supports manual configuration of RDs and RTs, if you don't
want them derived automatically. To manually define RDs and RTs, use the
`vni` option within NCLU to configure the switch:

    cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 rd 172.16.10.1:20
    cumulus@switch:~$ net add bgp l2vpn evpn vni 10200 route-target import 65100:20
    cumulus@switch:~$ net add bgp l2vpn evpn advertise-all-vni
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in
`/etc/frr/frr.conf`:

``` 
 address-family l2vpn evpn
  advertise-all-vni
  vni 10200
   rd 172.16.10.1:20
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

### <span>Enabling EVPN in an iBGP Environment with an OSPF Underlay</span>

EVPN can be deployed with an
[OSPF](/version/cumulus-linux-35/Layer_3/Open_Shortest_Path_First_-_OSPF_-_Protocol)
or static route underlay if needed. This is a more complex configuration
than using eBGP. In this case, iBGP advertises EVPN routes directly
between VTEPs, and the spines are unaware of EVPN or BGP.

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

These commands create the following configuration snippet in
`/etc/frr/frr.conf`:

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

### <span>Disabling Data Plane MAC Learning over VXLAN Tunnels</span>

When EVPN is provisioned, data plane MAC learning should be disabled for
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
mode](/version/cumulus-linux-35/Layer_1_and_2/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges),
you must edit the bridge configuration in the `/etc/network/interfaces`
file in a text editor:

    auto bridge1
    iface bridge1
        bridge-ports swp3.100 swp4.100 vni100
        bridge-learning vni100=off

{{%/notice%}}

### <span>Handling BUM Traffic</span>

With EVPN, the only method of handling BUM traffic is [Head End
Replication
(HER)](Lightweight_Network_Virtualization_-_LNV_Overview.html#src-8357484_LightweightNetworkVirtualization-LNVOverview-head-end).
HER is enabled by default, as it is when [Lightweight Network
Virtualization
(LNV)](/display/CL35/Lightweight+Network+Virtualization+-+LNV+Overview)
is used.

## <span id="src-8357510_EthernetVirtualPrivateNetwork-EVPN-arp" class="confluence-anchor-link"></span><span>ARP and ND Suppression</span>

ARP suppression in an EVPN context refers to the ability of a VTEP to
suppress ARP flooding over VXLAN tunnels as much as possible. Instead, a
local proxy handles ARP requests received from locally attached hosts
for remote hosts. ARP suppression is the implementation for IPv4; ND
suppression is the implementation for IPv6.

{{%notice note%}}

On switches with the Mellanox Spectrum chipset, ND suppression only
functions with the [Spectrum A1
chip](https://support.cumulusnetworks.com/hc/en-us/articles/115015646107).

{{%/notice%}}

ARP and ND suppression are not enabled by default. You configure ARP/ND
suppression on a VXLAN interface. You also need to create an SVI for the
neighbor entry.

To configure ARP or ND suppression, use
[NCLU](/version/cumulus-linux-35/System_Configuration/Network_Command_Line_Utility_-_NCLU/).
Here's an example configuration using 2 VXLANs, 10100 and 10200, and 2
VLANs, 100 and 200:

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
    cumulus@switch:~$ net add vxlan vni100 vxlan local-tunnelip 110.0.0.1
    cumulus@switch:~$ net add vxlan vni200 vxlan local-tunnelip 110.0.0.1
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
        vxlan-local-tunnelip 110.0.0.1
     
    auto vni200
    iface vni200
         bridge-learning off
         bridge-access 200
         bridge-arp-nd-suppress on
         vxlan-id 10200
         vxlan-local-tunnelip 110.0.0.1

{{%notice tip%}}

For a bridge in [traditional
mode](/version/cumulus-linux-35/Layer_1_and_2/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges),
you must edit the bridge configuration in the `/etc/network/interfaces`
file in a text editor:

    auto bridge1
    iface bridge1
        bridge-ports swp3.100 swp4.100 vni100
        bridge-learning vni100=off
        bridge-arp-nd-suppress vni100=on
        ip6-forward off
        ip-forward off 

{{%/notice%}}

### <span>Using UFT Profiles Other than the Default</span>

When deploying EVPN and VXLAN using a hardware profile other than the
default UFT profile, you need to ensure that the Linux kernel ARP sysctl
settings `gc_thresh2` and `gc_thresh3` are both set to a value larger
than the number of the neighbor (ARP/ND) entries anticipated in the
deployment.

To configure these settings, edit `/etc/sysctl.d/neigh.conf` in a text
editor. If your network has more hosts than the values used in the
example below, change the sysctl entries accordingly.

    cumulus@switch:~$ sudo nano /etc/sysctl.d/neigh.conf
    ...
    net.ipv4.neigh.default.gc_thresh3=14336
    net.ipv6.neigh.default.gc_thresh3=16384
    net.ipv4.neigh.default.gc_thresh2=7168
    net.ipv6.neigh.default.gc_thresh2=8192
    ...

After you save your settings, reboot the switch to apply the new
configuration.

## <span>EVPN and VXLAN Active-Active Mode</span>

No additional EVPN-specific configuration is needed for [VXLAN
active-active
mode](/version/cumulus-linux-35/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode).
Both switches in the
[MLAG](/version/cumulus-linux-35/Layer_1_and_2/Multi-Chassis_Link_Aggregation_-_MLAG)
pair establish EVPN peering with other EVPN speakers (for example, with
spine switches, if using hop-by-hop eBGP) and inform about their locally
known VNIs and MACs. When MLAG is active, both switches announce this
information with the shared anycast IP address.

The active-active configuration should include the following:

  - The `clagd-vxlan-anycast-ip` parameter must be under the [loopback
    stanza](LNV_VXLAN_Active-Active_Mode.html#src-8357503_LNVVXLANActive-ActiveMode-anycast)
    on both peers

  - The anycast address should be advertised to the routed fabric from
    both peers

  - The
    [VNIs](LNV_VXLAN_Active-Active_Mode.html#src-8357503_LNVVXLANActive-ActiveMode-example)
    must be configured identically on both peers. However,
    `vxlan-local-``tunnelip` must be sourced from the switch's unique
    loopback stanza IP address.

  - The
    [peerlink](LNV_VXLAN_Active-Active_Mode.html#src-8357503_LNVVXLANActive-ActiveMode-example)
    must belong to the bridge

MLAG syncs information between the two switches in the MLAG pair; EVPN
does not synchronize.

## <span>Inter-subnet Routing</span>

There are multiple models in EVPN for routing between different subnets
(VLANs). These models arise due to the following two main
considerations:

  - Does every VTEP act as an L3 gateway and do routing, or only
    specific VTEPs do routing?

  - Is routing done only at the ingress of the VXLAN tunnel or is it
    done at both the ingress and the egress of the VXLAN tunnel?

These models are:

  - **Centralized routing:** Specific VTEPs act as designated L3
    gateways and do routing between subnets; other VTEPs just do
    bridging.

  - **Distributed asymmetric routing:** Every VTEP participates in
    routing, but all routing is done at the ingress VTEP; the egress
    VTEP only does bridging.

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
forwarding](/version/cumulus-linux-35/Layer_3/Virtual_Routing_and_Forwarding_-_VRF)).
A VRF instance is provisioned for each tenant, and the subnets of the
tenant are associated with that VRF (the corresponding SVI is attached
to the VRF). Inter-subnet routing for each tenant occurs within the
context of that tenant's VRF, and is separate from the routing for other
tenants.

{{%notice note%}}

When configuring [VXLAN
routing](/version/cumulus-linux-35/Network_Virtualization/VXLAN_Routing),
Cumulus Networks recommends enabling ARP suppression on all VXLAN
interfaces. Otherwise, when a locally attached host ARPs for the
gateway, it will receive multiple responses, one from each anycast
gateway.

{{%/notice%}}

### <span id="src-8357510_EthernetVirtualPrivateNetwork-EVPN-centralized" class="confluence-anchor-link"></span><span>Centralized Routing</span>

In centralized routing, a specific VTEP is configured to act as the
default gateway for all the hosts in a particular subnet throughout the
EVPN fabric. It is common to provision a pair of VTEPs in active-active
mode as the default gateway, using an anycast IP/MAC address for each
subnet. All subnets need to be configured on such gateway VTEP(s). When
a host in one subnet wants to communicate with a host in another subnet,
it addresses the packets to the gateway VTEP. The ingress VTEP (to which
the source host is attached) bridges the packets to the gateway VTEP
over the corresponding VXLAN tunnel. The gateway VTEP performs the
routing to the destinaion host and post-routing, the packet gets bridged
to the egress VTEP (to which the destination host is attached). The
egress VTEP then bridges the packet on to the destination host.

#### <span>Advertising the Default Gateway</span>

In order to enable centralized routing, the gateway VTEPs must be
configured to advertise their IP/MAC address. This is done using the
`advertise-default-gw command.`

    cumulus@leaf01:~$ net add bgp autonomous-system 65000
    cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-default-gw
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following configuration snippet in
`/etc/frr/frr.conf`:

    router bgp 65000
      address-family l2vpn evpn
       advertise-default-gw
      exit-address-family

{{%notice note%}}

  - Centralized routing can be deployed at the VNI level. Thus, you can
    configure the `advertise-default-gw` command per VNI so that
    centralized routing is used for some VNIs while distributed routing
    (described below) is used for other VNIs. This type of configuration
    is not recommended unless the deployment requires it.

  - When centralized routing is in use, even if the source host and
    destination host are attached to the same VTEP, the packets travel
    to the gateway VTEP to get routed and then come back.

{{%/notice%}}

### <span id="src-8357510_EthernetVirtualPrivateNetwork-EVPN-asymmetric" class="confluence-anchor-link"></span><span>Asymmetric Routing</span>

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

### <span id="src-8357510_EthernetVirtualPrivateNetwork-EVPN-symmetric" class="confluence-anchor-link"></span><span>Symmetric Routing</span>

In distributed symmetric routing, each VTEP acts as a layer 3 gateway,
performing routing for its attached hosts. This is the same as in
asymmetric routing. The difference is that in symmetric routing, both
the ingress VTEP and egress VTEP route the packets. Thus, it can be
compared to the traditional routing behavior of routing to a next hop
router. In the VXLAN encapsulated packet, the inner destination MAC
address is set to the router MAC address of the egress VTEP as an
indication that the egress VTEP is the next hop and also needs to
perform routing. All routing happens in the context of a tenant (VRF).
For a packet received by the ingress VTEP from a locally attached host,
the SVI interface corresponding to the VLAN determines the VRF. For a
packet received by the egress VTEP over VXLAN tunnel, the VNI in the
packet has to specify the VRF. For symmetric routing, this is a VNI
corresponding to the tenant and is different from either the source VNI
or the destination VNI. This VNI is referred to as the L3-VNI or
interconnecting VNI; it has to be provisioned by the operator and is
exchanged through the EVPN control plane. In order to make the
distinction clear, the regular VNI, which is used to map a VLAN, is
referred to as the L2-VNI.

{{%notice note%}}

**L3-VNI**

  - There is a one-to-one mapping between an L3-VNI and a tenant (VRF).

  - The VRF to L3-VNI mapping has to be consistent across all VTEPs. The
    L3-VNI has to be provisioned by the operator.

  - L3-VNI and L2-VNI cannot share the same number space.

{{%/notice%}}

In addition to the L3-VNI, the other parameter relevant to symmetric
routing is the router MAC address. This should be a MAC address of the
VTEP so that it knows to route the packet after VXLAN decapsulation.
This parameter is automatically derived from the MAC address of the SVI
corresponding to the L3-VNI. It is also exchanged through the EVPN
control plane.

For EVPN symmetric routing, the additional configuration required is as
follows:

1.  Configure a per-tenant VXLAN interface that specifies the L3-VNI for
    the tenant. This VXLAN interface is part of the bridge and router
    MAC addresses of remote VTEPs is installed over this interface.

2.  Configure an SVI (layer 3 interface) corresponding to the per-tenant
    VXLAN interface. This is attached to the tenant's VRF. Remote host
    routes for symmetric routing are installed over this SVI.

3.  Specify the mapping of VRF to L3-VNI. This configuration is for the
    BGP control plane.

#### <span>VXLAN Interface Corresponding to the L3-VNI</span>

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

#### <span>SVI for the L3-VNI</span>

    cumulus@leaf01:~$ net add vlan 4001 vrf blue
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following snippet in the
`/etc/network/interfaces` file:

    auto vlan4001
    iface vlan4001
        vlan-id 4001
        vlan-raw-device bridge
        vrf blue

{{%notice note%}}

When two VTEPs are operating in VXLAN active-active mode and performing
symmetric routing, their router MAC needs to be configured corresponding
to each L3-VNI in order to ensure both VTEPs use the same MAC address.
Do this by specifying the `hwaddress` (MAC address) for the SVI
corresponding to the L3-VNI, with the same address used on both switches
in the MLAG pair. It is recommended that you use the MLAG system MAC
address for this purpose. The corresponding snippet of configuration in
the `/etc/network/interfaces` file looks like this:

    auto vlan4001
    iface vlan4001
        hwaddress 44:39:39:FF:40:94
        vlan-id 4001
        vlan-raw-device bridge
        vrf blue

{{%/notice%}}

#### <span>VRF to L3-VNI Mapping</span>

    cumulus@leaf01:~$ net add vrf blue vni 104001
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

These commands create the following configuration snippet in
`/etc/frr/frr.conf`:

    vrf blue
     vni 104001
    !

#### <span>Advertising the Locally-attached Subnets</span>

Symmetric routing presents a problem in the presence of silent hosts. If
the ingress VTEP does not have the destination subnet and the host route
is not advertised for the destination host, the ingress VTEP cannot
route the packet to its destination. This problem can be overcome by
having VTEPs announce the subnet prefixes corresponding to their
connected subnets in addition to announcing host routes. These routes
must be announced as EVPN prefix (type-5) routes.

To advertise locally attached subnets, you must:

1.  Enable advertisement of EVPN prefix (type-5) routes. Refer to the
    [next
    section](#src-8357510_EthernetVirtualPrivateNetwork-EVPN-type5) for
    the steps to do this.

2.  Ensure that the routes corresponding to the connected subnets are
    known in the BGP VRF routing table by injecting them using the
    `network` command or redistributing them using the `redistribute
    connected` command.

{{%notice note%}}

This configuration is recommended only if the deployment is known to
have silent hosts. It is also recommended that this should be enabled on
only one VTEP per subnet, or two for redundancy.

{{%/notice%}}

{{%notice note%}}

An earlier version of this chapter referred to the `advertise-subnet`
command. This command has been deprecated and should not be used.

{{%/notice%}}

## <span id="src-8357510_EthernetVirtualPrivateNetwork-EVPN-type5" class="confluence-anchor-link"></span><span>Prefix-based Routing — EVPN Type-5 Routes</span>

EVPN in Cumulus Linux supports prefix-based routing using EVPN type-5
(prefix) routes. Type-5 routes (or prefix routes) are primarily used to
route to destinations outside of the data center fabric.

EVPN prefix routes carry the L3-VNI and router MAC address and follow
the symmetric routing model for routing to the destination prefix.

{{%notice tip%}}

When connecting to a WAN edge router to reach destinations outside the
data center, it is highly recommended that specific border/exit leaf
switches be deployed to originate the type-5 routes.

{{%/notice%}}

{{%notice note%}}

On switches with the Mellanox Spectrum chipset, centralized routing,
symmetric routing and prefix-based routing only functions with the
Spectrum A1 chip.

{{%/notice%}}

{{%notice note%}}

If you are using a Broadcom Trident II+ switch as a border/exit leaf,
[review release
note 766](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848#rn766)
for a necessary workaround; the workaround only applies to Trident II+
switches, not Tomahawk or Spectrum.

{{%/notice%}}

### <span>Configuring the Switch to Install EVPN Type-5 Routes</span>

In order for a switch to be able to install EVPN type-5 routes into the
routing table, it must be configured with the L3-VNI related
information. This configuration is the same as what you use for
symmetric routing. That is, you need to:

1.  Configure a per-tenant VXLAN interface that specifies the L3-VNI for
    the tenant. This VXLAN interface is part of the bridge; router MAC
    addresses of remote VTEPs are installed over this interface.

2.  Configure an SVI (layer 3 interface) corresponding to the per-tenant
    VXLAN interface. This is attached to the tenant's VRF. The remote
    prefix routes are installed over this SVI.

3.  Specify the mapping of the VRF to L3-VNI. This configuration is for
    the BGP control plane.

### <span>Announcing EVPN Type-5 Routes</span>

The following configuration is needed in the tenant VRF in order to
announce IP prefixes in BGP's RIB as EVPN type-5 routes.

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

## <span>Static (Sticky) MAC Addresses</span>

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
mode](/version/cumulus-linux-35/Layer_1_and_2/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges),
you must edit the bridge configuration in the `/etc/network/interfaces`
file in a text editor:

    auto br101
    iface br101
        bridge-ports swp1.101 vni10101
        bridge-learning vni10101=off
        post-up bridge fdb add 00:11:22:33:44:55 dev swp1.101 master static

{{%/notice%}}

## <span>EVPN Operational Commands</span>

### <span>General Linux Commands Related to EVPN</span>

You can use various `iproute2` commands to examine links, VLAN mappings
and the bridge MAC forwarding database known to the Linux kernel. You
can also use such commands to examine the neighbor cache and the routing
table (for the underlay or for a specific tenant VRF). Some of the key
commands are:

  - ip \[-d\] link show

  - bridge link show

  - bridge vlan show

  - bridge \[-s\] fdb show

  - ip neighbor show

  - ip route show \[table \<vrf-name\>\]

A sample output of `ip -d link show type vxlan` is shown below for one
VXLAN interface. Some relevant parameters are the VNI value, the state,
the local IP address for the VXLAN tunnel, the UDP port number (4789)
and the bridge that the interface is part of (*bridge* in the example
below). The output also shows that MAC learning is disabled (*off*) on
the VXLAN interface.

    cumulus@leaf01:~$ ip -d link show type vxlan
    9: vni100: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default 
        link/ether 72:bc:b4:a3:eb:1e brd ff:ff:ff:ff:ff:ff promiscuity 1 
        vxlan id 10100 local 110.0.0.1 srcport 0 0 dstport 4789 nolearning ageing 300 
        bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning off flood on port_id 0x8001 port_no 0x1 designated_port 32769 designated_cost 0 designated_bridge 8000.0:1:0:0:11:0 designated_root 8000.0:1:0:0:11:0 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on neigh_suppress on group_fwd_mask 0x0 group_fwd_mask_str 0x0 group_fwd_maskhi 0x0 group_fwd_maskhi_str 0x0 addrgenmode eui64 
    ...
    cumulus@leaf01:~$

A sample output of `bridge fdb show` is depicted below. Some information
of interest from this output are:

  - swp3 and swp4 are access ports with VLAN ID 100. This is mapped to
    VXLAN interface vni100.

  - 00:02:00:00:00:01 is a local host MAC learned on swp3.

  - The remote VTEPs which participate in VLAN ID 100 are 110.0.0.3,
    110.0.0.4 and 110.0.0.2. This is evident from the FDB entries with a
    MAC address of 00:00:00:00:00:00. These entries are used for BUM
    traffic replication.

  - 00:02:00:00:00:06 is a remote host MAC reachable over the VXLAN
    tunnel to 110.0.0.2.

<!-- end list -->

    cumulus@leaf01:~$ bridge fdb show
    00:02:00:00:00:13 dev swp3 master bridge permanent
    00:02:00:00:00:01 dev swp3 vlan 100 master bridge 
    00:02:00:00:00:02 dev swp4 vlan 100 master bridge 
    72:bc:b4:a3:eb:1e dev vni100 master bridge permanent
    00:02:00:00:00:06 dev vni100 vlan 100 offload master bridge 
    00:00:00:00:00:00 dev vni100 dst 110.0.0.3 self permanent
    00:00:00:00:00:00 dev vni100 dst 110.0.0.4 self permanent
    00:00:00:00:00:00 dev vni100 dst 110.0.0.2 self permanent
    00:02:00:00:00:06 dev vni100 dst 110.0.0.2 self offload 
    ...

A sample output of `ip neigh show` is depicted below. Some interesting
information from this output includes:

  - 50.1.1.11 is a locally-attached host on VLAN 100. It is shown twice
    because of the configuration of the anycast IP/MAC on the switch.

  - 50.1.1.42 is a remote host on VLAN 100 and 60.1.1.23 is a remote
    host on VLAN 200. The MAC address of these hosts can be examined
    using the `bridge fdb show` command described earlier to determine
    the VTEPs behind which these hosts are located.

<!-- end list -->

    cumulus@leaf01:~$ ip neigh show
    50.1.1.11 dev vlan100-v0 lladdr 00:02:00:00:00:01 STALE
    50.1.1.42 dev vlan100 lladdr 00:02:00:00:00:0e offload REACHABLE
    60.1.1.23 dev vlan200 lladdr 00:02:00:00:00:07 offload REACHABLE
    50.1.1.11 dev vlan100 lladdr 00:02:00:00:00:01 REACHABLE
    ...

### <span>General BGP Operational Commands Relevant to EVPN</span>

The following commands are not unique to EVPN but help troubleshoot
connectivity and route propagation. If BGP is used for the underlay
routing, you can view a summary of the layer 3 fabric connectivity by
running the `net show bgp summary` command:

    cumulus@leaf01:~$ net show bgp summary
    show bgp ipv4 unicast summary
    =============================
    BGP router identifier 110.0.0.1, local AS number 65001 vrf-id 0
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
    BGP router identifier 110.0.0.1, local AS number 65001 vrf-id 0
    BGP table version 0
    RIB entries 15, using 2040 bytes of memory
    Peers 2, using 42 KiB of memory
    Peer groups 1, using 72 bytes of memory
     
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
    s1(swp49s0)     4      65100      43      49        0    0    0 02:04:00           30
    s2(swp49s1)     4      65100      43      49        0    0    0 02:03:59           30
    Total number of neighbors 2

You can examine the underlay routing, which determines how remote VTEPs
are reached, by running the `net show route` command. Here is some
sample output from a leaf switch:

    cumulus@leaf01:~$ net show route
    show ip route
    =============
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
           T - Table, v - VNC, V - VNC-Direct, A - Babel,
           > - selected route, * - FIB route
    K>* 0.0.0.0/0 [0/0] via 192.168.0.2, eth0, 1d03h41m
    B>* 20.0.0.1/32 [20/0] via fe80::202:ff:fe00:29, swp1, 1d03h40m
    B>* 20.0.0.2/32 [20/0] via fe80::202:ff:fe00:2d, swp2, 1d03h40m
    C>* 110.0.0.1/32 is directly connected, lo, 1d03h41m
    B>* 110.0.0.2/32 [20/0] via fe80::202:ff:fe00:29, swp1, 1d03h40m
      *                     via fe80::202:ff:fe00:2d, swp2, 1d03h40m
    B>* 110.0.0.3/32 [20/0] via fe80::202:ff:fe00:29, swp1, 1d03h40m
      *                     via fe80::202:ff:fe00:2d, swp2, 1d03h40m
    B>* 110.0.0.4/32 [20/0] via fe80::202:ff:fe00:29, swp1, 1d03h40m
      *                     via fe80::202:ff:fe00:2d, swp2, 1d03h40m
    C>* 192.168.0.0/24 is directly connected, eth0, 1d03h41m
     
    show ipv6 route
    ===============
    Codes: K - kernel route, C - connected, S - static, R - RIPng,
           O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table,
           v - VNC, V - VNC-Direct, A - Babel,
           > - selected route, * - FIB route
    C * fe80::/64 is directly connected, swp2, 1d03h41m
    C * fe80::/64 is directly connected, swp1, 1d03h41m
    C>* fe80::/64 is directly connected, eth0, 1d03h41m
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
    100       br0       vni100     00:02:00:00:00:0a                           offload        1 day, 03:38:20
    100       br0       vni100     00:02:00:00:00:0d                           offload        1 day, 03:38:20
    100       br0       vni100     00:02:00:00:00:0e                           offload        1 day, 03:38:20
    100       br0       vni100     00:02:00:00:00:05                           offload        1 day, 03:38:19
    100       br0       vni100     00:02:00:00:00:06                           offload        1 day, 03:38:19
    100       br0       vni100     00:02:00:00:00:09                           offload        1 day, 03:38:20
    200       br0       br0          00:00:5e:00:01:01                permanent                 1 day, 03:38:42
    200       br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:43
    200       br0       swp5         00:02:00:00:00:03                                          00:00:26
    200       br0       swp6         00:02:00:00:00:04                                          00:00:26
    200       br0       vni200     00:02:00:00:00:0b                           offload        1 day, 03:38:20
    200       br0       vni200     00:02:00:00:00:0c                           offload        1 day, 03:38:20
    200       br0       vni200     00:02:00:00:00:0f                           offload        1 day, 03:38:20
    200       br0       vni200     00:02:00:00:00:07                           offload        1 day, 03:38:19
    200       br0       vni200     00:02:00:00:00:08                           offload        1 day, 03:38:19
    200       br0       vni200     00:02:00:00:00:10                           offload        1 day, 03:38:20
    4001      br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:42
    4001      br0       vni4001    00:01:00:00:12:00                           offload        1 day, 03:38:19
    4001      br0       vni4001    00:01:00:00:13:00                           offload        1 day, 03:38:20
    4001      br0       vni4001    00:01:00:00:14:00                           offload        1 day, 03:38:20
    untagged            br0          00:00:5e:00:01:01                permanent  self           never
    untagged            vlan100      00:00:5e:00:01:01                permanent  self           never
    untagged            vlan200      00:00:5e:00:01:01                permanent  self           never
    ...

### <span>Displaying EVPN address-family Peers</span>

The BGP peers participating in the L2VPN/EVPN address-family and their
states can be shown using the ` net show bgp l2vpn evpn summary
 `command. The following sample output from a leaf switch shows eBGP
peering with 2 spine switches for exchanging EVPN routes; both peering
sessions are in the *established* state.

    cumulus@leaf01:~$ net show bgp l2vpn evpn summary
    BGP router identifier 110.0.0.1, local AS number 65001 vrf-id 0
    BGP table version 0
    RIB entries 15, using 2280 bytes of memory
    Peers 2, using 39 KiB of memory
    Peer groups 1, using 64 bytes of memory
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
    s1(swp1)        4      65100     103     107        0    0    0 1d02h08m           30
    s2(swp2)        4      65100     103     107        0    0    0 1d02h08m           30
    Total number of neighbors 2
    cumulus@leaf01:~$

### <span>Displaying VNIs in EVPN</span>

You can display the configured VNIs on a network device participating in
BGP EVPN by running the `show bgp evpn vni` command. This command is
only relevant on a VTEP. If symmetric routing is configured, this
command displays the special L3-VNIs that are configured per tenant VRF.

The following example from a leaf switch shows 2 L2-VNIs — 10100 and
10200 — as well as a L3-VNI — 104001. For L2-VNIs, the number of
associated MAC and neighbor entries are shown. The VXLAN interface and
VRF corresponding to each VNI are also shown.

    cumulus@leaf01:~$ net show evpn vni
    VNI        Type VxLAN IF              # MACs   # ARPs   # Remote VTEPs  Tenant VRF                           
    10200      L2   vni200              8        12       3               vrf1                                 
    10100      L2   vni100              8        12       3               vrf1                                 
    104001     L3   vni4001             3        3        n/a             vrf1                                 
    cumulus@leaf01:~$

You can examine the EVPN information for a specific VNI in detail. The
following output shows the details for the L2-VNI 10100 as well as for
the L3-VNI 104001. For the L2-VNI, the remote VTEPs which have that VNI
are shown. For the L3-VNI, the router MAC and associated L2-VNIs are
shown. The state of the L3-VNI depends on the state of its associated
VRF as well as the states of its underlying VXLAN interface and SVI.

    cumulus@leaf01:~$ net show evpn vni 10100
    VNI: 10100
     Type: L2
     Tenant VRF: vrf1
     VxLAN interface: vni100
     VxLAN ifIndex: 9
     Local VTEP IP: 110.0.0.1
     Remote VTEPs for this VNI:
      110.0.0.2
      110.0.0.4
      110.0.0.3
     Number of MACs (local and remote) known for this VNI: 8
     Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 12
     Advertise-gw-macip: No
    cumulus@leaf01:~$ 
    cumulus@leaf01:~$ net show evpn vni 104001
    VNI: 104001
      Type: L3
      Tenant VRF: vrf1
      Local Vtep Ip: 110.0.0.1
      Vxlan-Intf: vni4001
      SVI-If: vlan4001
      State: Up
      Router MAC: 00:01:00:00:11:00
      L2 VNIs: 10100 10200 
    cumulus@leaf01:~$

### <span>Examining Local and Remote MAC Addresses for a VNI in EVPN</span>

You can examine all local and remote MAC addresses for a VNI by running
`net show evpn mac vni <vni>`. This command is only relevant for an
L2-VNI:

    cumulus@leaf01:~$ net show evpn mac vni 10100
    Number of MACs (local and remote) known for this VNI: 8
    MAC               Type   Intf/Remote VTEP      VLAN 
    00:02:00:00:00:0e remote 110.0.0.4            
    00:02:00:00:00:06 remote 110.0.0.2            
    00:02:00:00:00:05 remote 110.0.0.2            
    00:02:00:00:00:02 local  swp4                  100  
    00:00:5e:00:01:01 local  vlan100-v0            100  
    00:02:00:00:00:09 remote 110.0.0.3            
    00:01:00:00:11:00 local  vlan100               100  
    00:02:00:00:00:01 local  swp3                  100  
    00:02:00:00:00:0a remote 110.0.0.3            
    00:02:00:00:00:0d remote 110.0.0.4            
    cumulus@leaf01:~$

You can examine MAC addresses for all VNIs using `net show evpn mac vni
all.`

You can examine the details for a specific MAC addresses or query all
remote MAC addresses behind a specific VTEP:

    cumulus@leaf01:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:02
    MAC: 00:02:00:00:00:02
     Intf: swp4(6) VLAN: 100
     Neighbors:
        50.1.1.12 Active
    cumulus@leaf01:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:05
    MAC: 00:02:00:00:00:05
     Remote VTEP: 110.0.0.2
     Neighbors:
        50.1.1.21 
    cumulus@leaf01:~$ net show evpn mac vni 10100 vtep 110.0.0.3
    VNI 10100
    MAC               Type   Intf/Remote VTEP      VLAN 
    00:02:00:00:00:09 remote 110.0.0.3            
    00:02:00:00:00:0a remote 110.0.0.3            
    cumulus@leaf01:~$

### <span>Examining Local and Remote Neighbors for a VNI in EVPN</span>

You can examine all local and remote neighbors (ARP entries) for a VNI
by running `net show evpn arp-cache vni <vni>`. This command is only
relevant for an L2-VNI and the output shows both IPv4 and IPv6 neighbor
entries:

    cumulus@leaf01:~$ net show evpn arp-cache vni 10100
    Number of ARPs (local and remote) known for this VNI: 12
    IP                      Type   MAC               Remote VTEP          
    50.1.1.11               local  00:02:00:00:00:01
    50.1.1.12               local  00:02:00:00:00:02
    50.1.1.22               remote 00:02:00:00:00:06 110.0.0.2            
    fe80::201:ff:fe00:1100  local  00:01:00:00:11:00
    50.1.1.1                local  00:01:00:00:11:00
    50.1.1.31               remote 00:02:00:00:00:09 110.0.0.3            
    fe80::200:5eff:fe00:101 local  00:00:5e:00:01:01
    ...

You can examine neighbor entries for all VNIs using `net show evpn
arp-cache vni all.`

### <span>Examining Remote Router MACs in EVPN</span>

When symmetric routing is deployed, you can examine the router MACs
corresponding to all remote VTEPs by running `net show evpn rmac vni
<vni>`. This command is only relevant for an L3-VNI:

    cumulus@leaf01:~$ net show evpn rmac vni 104001
    Number of Remote RMACs known for this VNI: 3
    MAC               Remote VTEP          
    00:01:00:00:14:00 110.0.0.4            
    00:01:00:00:12:00 110.0.0.2            
    00:01:00:00:13:00 110.0.0.3            
    cumulus@leaf01:~$

You can examine router MACs for all L3-VNIs using `net show evpn rmac
vni all.`

### <span>Examining Gateway Next Hops in EVPN</span>

When symmetric routing is deployed, you can examine the gateway next
hops by running `net show evpn next-hops vni <vni>`. This command is
only relevant for an L3-VNI. In general, the gateway next hop IP
addresses should correspond to the remote VTEP IP addresses. Remote host
and prefix routes are installed via these next hops:

    cumulus@leaf01:~$ net show evpn next-hops vni 104001
    Number of NH Neighbors known for this VNI: 3
    IP              RMAC             
    110.0.0.3       00:01:00:00:13:00
    110.0.0.4       00:01:00:00:14:00
    110.0.0.2       00:01:00:00:12:00
    cumulus@leaf01:~$

You can examine gateway next hops for all L3-VNIs using `net show evpn
next-hops vni all`.

You can query a specific next hop; the output displays the remote host
and prefix routes via this next hop:

    cumulus@leaf01:~$ net show evpn next-hops vni 104001 ip 110.0.0.4
    Ip: 110.0.0.4
      RMAC: 00:01:00:00:14:00
      Refcount: 4
      Prefixes:
        50.1.1.41/32
        50.1.1.42/32
        60.1.1.43/32
        60.1.1.44/32
    cumulus@leaf01:~$

### <span>Displaying the VRF Routing Table in FRR</span>

You can examine the VRF routing table by running `net show route vrf
<vrf-name>`. This command is not specific to EVPN. In the context of
EVPN, this command is relevant when symmetric routing is deployed and
can be used to verify that remote host and prefix routes are installed
in the VRF routing table and point to the appropriate gateway next hop:

    cumulus@leaf01:~$ net show route vrf vrf1
    show ip route vrf vrf1 
    =======================
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
           T - Table, v - VNC, V - VNC-Direct, A - Babel,
           > - selected route, * - FIB route
     
    VRF vrf1:
    K * 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 1d02h42m
    C * 50.1.1.0/24 is directly connected, vlan100-v0, 1d02h42m
    C>* 50.1.1.0/24 is directly connected, vlan100, 1d02h42m
    B>* 50.1.1.21/32 [20/0] via 110.0.0.2, vlan4001 onlink, 1d02h41m
    B>* 50.1.1.22/32 [20/0] via 110.0.0.2, vlan4001 onlink, 1d02h41m
    B>* 50.1.1.31/32 [20/0] via 110.0.0.3, vlan4001 onlink, 1d02h41m
    B>* 50.1.1.32/32 [20/0] via 110.0.0.3, vlan4001 onlink, 1d02h41m
    B>* 50.1.1.41/32 [20/0] via 110.0.0.4, vlan4001 onlink, 1d02h41m
    ...

As you can see in the output above, the next hops for these routes are
specified by EVPN to be *onlink*, or reachable over the specified SVI.
This is necessary because this interface is not required to have an IP
address, and even if it is configured with an IP address, the next hop
would not be on the same subnet as it is usually the remote VTEP's IP
address, and hence, part of the underlay IP network.

### <span>Displaying the Global BGP EVPN Routing Table</span>

Run the `net show bgp l2vpn evpn route` command to display all EVPN
routes, both local and remote. The routes displayed here are based on RD
as they are across VNIs and VRFs:

    cumulus@leaf01:~$ net show bgp l2vpn evpn route 
    BGP table version is 0, local router ID is 110.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
    Route Distinguisher: 110.0.0.1:1
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[32]:[50.1.1.11]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[128]:[2001:50:1:1::11]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[32]:[50.1.1.12]
                        110.0.0.1                          32768 i
    *> [3]:[0]:[32]:[110.0.0.1]
                        110.0.0.1                          32768 i
    Route Distinguisher: 110.0.0.1:2
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[32]:[60.1.1.11]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[32]:[60.1.1.12]
                        110.0.0.1                          32768 i
    *> [3]:[0]:[32]:[110.0.0.1]
                        110.0.0.1                          32768 i
    ...

The routing table can be filtered based on EVPN route type. The
available options are as shown below:

    cumulus@leaf01:~$ net show bgp l2vpn evpn route type 
        macip      :  MAC-IP (Type-2) route
        multicast  :  Multicast
        prefix     :  An IPv4 or IPv6 prefix
    cumulus@leaf01:~$

### <span>Displaying a Specific EVPN Route</span>

To drill down on a specific route for more information, run the `net
show bgp l2vpn evpn route rd <rd-value>` command. This displays all EVPN
routes with that RD and with the path attribute details for each path.
Additional filtering is possible based on route type or by specifying
the MAC and/or IP address. The following example shows a specific MAC/IP
route. The output shows that this remote host is behind VTEP 110.0.0.4
and is reachable via two paths — one through either spine switch. This
example is from a symmetric routing deployment, so the route shows both
the L2-VNI (10200) and the L3-VNI (104001) as well as the EVPN route
target attributes corresponding to each and the associated router MAC
address.

    cumulus@leaf01:~$ net show bgp l2vpn evpn route rd 110.0.0.4:3 mac 00:02:00:00:00:10 ip 60.1.1.44
    BGP routing table entry for 110.0.0.4:3:[2]:[0]:[0]:[48]:[00:02:00:00:00:10]:[32]:[60.1.1.44]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp1) s2(swp2)
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:10]:[32]:[60.1.1.44] VNI 10200/104001
      65100 65004
        110.0.0.4 from s2(swp2) (20.0.0.2)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65004:10200 RT:65004:104001 ET:8 Rmac:00:01:00:00:14:00
          AddPath ID: RX 0, TX 97
          Last update: Sun Dec 17 20:57:24 2017
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:10]:[32]:[60.1.1.44] VNI 10200/104001
      65100 65004
        110.0.0.4 from s1(swp1) (20.0.0.1)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65004:10200 RT:65004:104001 ET:8 Rmac:00:01:00:00:14:00
          AddPath ID: RX 0, TX 71
          Last update: Sun Dec 17 20:57:23 2017
     
    Displayed 2 paths for requested prefix
    cumulus@leaf01:~$

{{%notice note%}}

  - Only global VNIs are supported. So even though VNI values are
    exchanged in the type-2 and type-5 routes, the received values are
    not used when installing the routes into the forwarding plane; the
    local configuration is used. You must ensure that the VLAN to VNI
    mappings and the L3-VNI assignment for a tenant VRF are uniform
    throughout the network.

  - If the remote host is dual attached, the next hop for the EVPN route
    is the anycast IP address of the remote
    [MLAG](/version/cumulus-linux-35/Layer_1_and_2/Multi-Chassis_Link_Aggregation_-_MLAG)
    pair, when MLAG is active.

{{%/notice%}}

The following example shows a prefix (type-5) route. Such a route has
only the L3-VNI and the route target corresponding to this VNI. This
route is learned via two paths, one through each spine switch.

    cumulus@leaf01:~$ net show bgp l2vpn evpn route rd 144.1.1.2:3 type prefix
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
    EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]
    BGP routing table entry for 144.1.1.2:3:[5]:[0]:[30]:[144.1.1.0]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp1) s2(swp2)
      Route [5]:[0]:[30]:[144.1.1.0] VNI 104001
      65100 65050
        110.0.0.5 from s2(swp2) (20.0.0.2)
          Origin incomplete, localpref 100, valid, external
          Extended Community: RT:65050:104001 ET:8 Rmac:00:01:00:00:01:00
          AddPath ID: RX 0, TX 112
          Last update: Tue Dec 19 00:12:18 2017
      Route [5]:[0]:[30]:[144.1.1.0] VNI 104001
      65100 65050
        110.0.0.5 from s1(swp1) (20.0.0.1)
          Origin incomplete, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65050:104001 ET:8 Rmac:00:01:00:00:01:00
          AddPath ID: RX 0, TX 71
          Last update: Tue Dec 19 00:12:17 2017
     
    Displayed 1 prefixes (2 paths) with this RD (of requested type)
    cumulus@leaf01:~$

### <span>Displaying the per-VNI EVPN Routing Table</span>

Received EVPN routes are maintained in the global EVPN routing table
(described above), even if there are no appropriate local VNIs to
**import** them into. For example, a spine switch maintains the global
EVPN routing table even though there are no VNIs present on it. When
local VNIs are present, received EVPN routes are imported into the
per-VNI routing tables based on the route target attributes. The per-VNI
routing table can be examined using the `net show bgp l2vpn evpn route
vni <vni>` command:

    cumulus@leaf01:~$ net show bgp l2vpn evpn route vni 10110
    BGP table version is 8, local router ID is 110.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:07]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:07]:[32]:[50.1.1.11]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:07]:[128]:[fe80::202:ff:fe00:7]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:08]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:08]:[32]:[50.1.1.12]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:08]:[128]:[fe80::202:ff:fe00:8]
                        110.0.0.1                          32768 i
    *> [3]:[0]:[32]:[110.0.0.1]
                        110.0.0.1                          32768 i
    Displayed 7 prefixes (7 paths)
    cumulus@leaf01:~$

To display the VNI routing table for all VNIs, run `net show bgp l2vpn
evpn route vni all.`

### <span>Displaying the per-VRF BGP Routing Table</span>

When symmetric routing is deployed, received type-2 and type-5 routes
are imported into the VRF routing table (against the corresponding
address-family: IPv4 unicast or IPv6 unicast) based on a match on the
route target attributes. You can examine BGP's VRF routing table using
`net show bgp vrf <vrf-name> ipv4 unicast` (or `net show bgp vrf
<vrf-name> ipv6 unicast`):

    cumulus@leaf01:~$ net show bgp vrf vrf1 ipv4 unicast 
    BGP table version is 8, local router ID is 50.1.1.250
    Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                  i internal, r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network          Next Hop            Metric LocPrf Weight Path
    *  50.1.2.21/32     110.0.0.2                              0 65100 65002 i
    *>                  110.0.0.2                              0 65100 65002 i
    *  50.1.2.22/32     110.0.0.2                              0 65100 65002 i
    *>                  110.0.0.2                              0 65100 65002 i
    *  50.1.3.31/32     110.0.0.3                              0 65100 65003 i
    *>                  110.0.0.3                              0 65100 65003 i
    *  50.1.3.32/32     110.0.0.3                              0 65100 65003 i
    *>                  110.0.0.3                              0 65100 65003 i
    *  50.1.4.41/32     110.0.0.4                              0 65100 65004 i
    *>                  110.0.0.4                              0 65100 65004 i
    *  50.1.4.42/32     110.0.0.4                              0 65100 65004 i
    *>                  110.0.0.4                              0 65100 65004 i
    *  144.1.1.0/30     110.0.0.5                              0 65100 65050 ?
    *>                  110.0.0.5                              0 65100 65050 ?
    *  144.2.1.0/30     110.0.0.6                              0 65100 65050 ?
    *>                  110.0.0.6                              0 65100 65050 ?
    Displayed  8 routes and 16 total paths
    cumulus@leaf01:~$

### <span>Examining MAC Moves</span>

The first time a MAC moves from behind one VTEP to behind another, BGP
associates a MAC Mobility (MM) extended community attribute of sequence
number 1, with the type-2 route for that MAC. From there, each time this
MAC moves to a new VTEP, the MM sequence number increments by 1. You can
examine the MM sequence number associated with a MAC's type-2 route
using `net show bgp evpn route vni <vni> mac <mac>`. The sample output
below shows the type-2 route for a MAC that has moved three times:

    cumulus@switch:~$ net show bgp evpn route vni 10109 mac 00:02:22:22:22:02
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

### <span>Examining Sticky MAC Addresses</span>

You can identify static or "sticky" MACs in EVPN by the presence of
"MM:0, sticky MAC" in the Extended Community line of the output from
`net show bgp evpn route vni <vni> mac <mac>:`

    cumulus@switch:~$ net show bgp evpn route vni 10101 mac 00:02:00:00:00:01
    BGP routing table entry for [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
    Paths: (1 available, best #1)
      Not advertised to any peer
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:01] VNI 10101
      Local
        6.0.0.18 from 0.0.0.0 (6.0.0.18)
          Origin IGP, localpref 100, weight 32768, valid, sourced, local, bestpath-from-AS Local, best
          Extended Community: ET:8 RT:60176:10101 MM:0, sticky MAC
          AddPath ID: RX 0, TX 46
          Last update: Tue Apr 11 21:44:02 2017
     
    Displayed 1 paths for requested prefix

## <span>Troubleshooting EVPN</span>

The primary way to troubleshoot EVPN is by enabling FRR debug logs. The
relevant debug options are:

  - `debug zebra vxlan` — which traces VNI addition and deletion (local
    and remote) as well as MAC and neighbor addition and deletion (local
    and remote).

  - `debug zebra kernel` — which traces actual netlink messages
    exchanged with the kernel, which includes everything, not just EVPN.

  - `debug bgp updates` — which traces BGP update exchanges, including
    all updates. Output is extended to show EVPN specific information.

  - `debug bgp zebra` — which traces interactions between BGP and zebra
    for EVPN (and other) routes.

## <span>Caveats</span>

The following caveats apply to EVPN in this version of Cumulus Linux:

  - When EVPN is enabled on a switch (VTEP), all locally defined VNIs on
    that switch and other information (such as MAC addresses) pertaining
    to them will be advertised to EVPN peers. There is no provision to
    only announce certain VNIs.

  - In a [VXLAN
    active-active](/version/cumulus-linux-35/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode)
    configuration, ARPs may sometimes not be suppressed even if ARP
    suppression is enabled. This is because the neighbor entries are not
    synced between the two switches operating in active-active mode by a
    control plane. This has no impact on forwarding.

  - Symmetric routing and prefix-based routing are only supported for
    IPv4 hosts and IPv4 prefixes; IPv6 routing is currently supported
    with asymmetric routing only.

  - Currently, only switches with the Mellanox Spectrum chipset or the
    Broadcom Tomahawk chipset can be deployed as a border/exit leaf. If
    you want to use a Broadcom Trident II+ switch as a border/exit leaf,
    please [read release
    note 766](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848#rn766)
    for a necessary workaround; the workaround only applies to Trident
    II+ switches, not Tomahawk or Spectrum.

  - The overlay (tenants) need to be configured in a specific VRF(s) and
    separated from the underlay, which resides in the default VRF. An
    L3-VNI mapping for the default VRF is not supported.

## <span>Example Configuration</span>

### <span>Example Configuration for EVPN for Bridging</span>

The following configurations are used throughout this chapter. You can
find the flat-file configurations for the network devices in the Cumulus
Networks [GitHub
repository](https://github.com/CumulusNetworks/cldemo-evpn/tree/master/config).
Only a subset is shown here for brevity (not shown are configurations
for leaf03, leaf04, server03, server04). Here is the topology diagram:

{{% imgOld 0 %}}

#### <span>leaf01 and leaf02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td>leaf01 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.11/32
 
auto eth0
iface eth0 inet dhcp
 
# uplinks
auto swp51
iface swp51
 
auto swp52
iface swp52
 
auto bridge
iface bridge
    bridge-ports swp1 vxlan10001 vxlan10100 vxlan10200
    bridge-vlan-aware yes
    bridge-vids 1 100 200
    bridge-pvid 1
 
auto vxlan10001
iface vxlan10001
    vxlan-id 10001
    vxlan-local-tunnelip 10.0.0.11
    bridge-access 1
    bridge-learning off
 
auto vxlan10100
iface vxlan10100
     vxlan-id 10100
     vxlan-local-tunnelip 10.0.0.11
     bridge-access 100
     bridge-learning off
 
auto vxlan10200
iface vxlan10200
     vxlan-id 10200
     vxlan-local-tunnelip 10.0.0.11
     bridge-access 200
     bridge-learning off</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.12/32
 
auto eth0
iface eth0 inet dhcp
 
# uplinks
auto swp51
iface swp51
 
auto swp52
iface swp52
 
auto bridge
iface bridge
    bridge-ports swp2 vxlan10001 vxlan10100 vxlan10200
    bridge-vlan-aware yes
    bridge-vids 1 100 200
    bridge-pvid 1
 
auto vxlan10001
iface vxlan10001
    vxlan-id 10001
    vxlan-local-tunnelip 10.0.0.12
    bridge-access 1
    bridge-learning off
 
auto vxlan10100
iface vxlan10100
    vxlan-id 10100
    vxlan-local-tunnelip 10.0.0.12
    bridge-access 100
    bridge-learning off
 
auto vxlan10200
iface vxlan10200
    vxlan-id 10200
    vxlan-local-tunnelip 10.0.0.12
    bridge-access 200
    bridge-learning off</code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/frr/frr.conf
<pre><code>!
interface swp51
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp52
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65011
 bgp router-id 10.0.0.11
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp51 interface peer-group fabric
 neighbor swp52 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.11/32
  neighbor fabric prefix-list dc-leaf-in in
  neighbor fabric prefix-list dc-leaf-out out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor fabric activate
  advertise-all-vni
 exit-address-family
 exit
!
ip prefix-list dc-leaf-in seq 10 permit 0.0.0.0/0
ip prefix-list dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-in seq 500 deny any
ip prefix-list dc-leaf-out seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-out seq 500 deny any
!
line vty
!
end</code></pre></td>
<td>leaf02 /etc/frr/frr.conf
<pre><code>!
interface swp51
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp52
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65012
 bgp router-id 10.0.0.12
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp51 interface peer-group fabric
 neighbor swp52 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.12/32
  neighbor fabric prefix-list dc-leaf-in in
  neighbor fabric prefix-list dc-leaf-out out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor fabric activate
  advertise-all-vni
 exit-address-family
 exit
!
ip prefix-list dc-leaf-in seq 10 permit 0.0.0.0/0
ip prefix-list dc-leaf-in seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-in seq 500 deny any
ip prefix-list dc-leaf-out seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-leaf-out seq 500 deny any
!
line vty
!
end</code></pre></td>
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
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.21/32
 
auto eth0
iface eth0 inet dhcp
 
# downlinks
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4</code></pre></td>
<td>spine02 /etc/network/interfaces
<pre><code>auto lo
iface lo inet loopback
    address 10.0.0.22/32
 
auto eth0
iface eth0 inet dhcp
 
# downlinks
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/frr/frr.conf
<pre><code>!
interface swp1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65020
 bgp router-id 10.0.0.21
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp1 interface peer-group fabric
 neighbor swp2 interface peer-group fabric
 neighbor swp3 interface peer-group fabric
 neighbor swp4 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.21/32
  neighbor fabric prefix-list dc-spine in
  neighbor fabric prefix-list dc-spine out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor fabric activate
 exit-address-family
 exit
!
ip prefix-list dc-spine seq 10 permit 0.0.0.0/0
ip prefix-list dc-spine seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-spine seq 500 deny any
!
line vty
!
end</code></pre></td>
<td>spine02 /etc/frr/frr.conf
<pre><code>!
interface swp1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65020
 bgp router-id 10.0.0.22
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp1 interface peer-group fabric
 neighbor swp2 interface peer-group fabric
 neighbor swp3 interface peer-group fabric
 neighbor swp4 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.22/32
  neighbor fabric prefix-list dc-spine in
  neighbor fabric prefix-list dc-spine out
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor fabric activate
 exit-address-family
 exit
!
ip prefix-list dc-spine seq 10 permit 0.0.0.0/0
ip prefix-list dc-spine seq 20 permit 10.0.0.0/24 le 32
ip prefix-list dc-spine seq 500 deny any
!
line vty
!
end</code></pre></td>
</tr>
</tbody>
</table>

#### <span>server01 and server02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>#configuration is for Cumulus VX
#in real life this is a server OS
 
auto eth0
iface eth0 inet dhcp
 
auto eth1
iface eth1
    address 172.16.1.101/24
 
auto eth1.100
iface eth1.100
    address 172.16.100.101/24
 
auto eth1.200
iface eth1.200
    address 172.16.200.101/24</code></pre></td>
<td><pre><code>#configuration is for Cumulus VX
#in real life this is a server OS
 
auto eth0
iface eth0 inet dhcp
 
auto eth2
iface eth2
    address 172.16.1.102/24
 
auto eth2.100
iface eth2.100
    address 172.16.100.102/24
 
auto eth2.200
iface eth2.200
    address 172.16.200.102/24</code></pre></td>
</tr>
</tbody>
</table>

### <span>Example Active-active Configuration</span>

The following configurations demonstrate a dual-attached
([MLAG](/version/cumulus-linux-35/Layer_1_and_2/Multi-Chassis_Link_Aggregation_-_MLAG))
EVPN scenario. You can find the flat-file configurations for the network
devices in the Cumulus Networks [GitHub
repository](https://github.com/CumulusNetworks/cldemo-evpn/). Only a
subset is shown here for brevity (not shown are configurations for
leaf03, leaf04, server02, server04). Here is the topology diagram:

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
 
auto lo
iface lo inet loopback
    alias loopback
    address 10.0.0.11/32
    clagd-vxlan-anycast-ip 10.10.10.20
 
auto eth0
iface eth0 inet dhcp
 
# uplinks
auto swp51
iface swp51
 
auto swp52
iface swp52
 
#host connections
auto swp1
iface swp1
 
auto server01
iface server01
  alias server01 MLAG bond
  bond-slaves swp1
  clag-id 1
 
auto peerlink
iface peerlink
  alias MLAG peerlink bond
  bond-slaves swp49 swp50
 
auto peerlink.4094
iface peerlink.4094
  address 169.254.1.1/30
  clagd-peer-ip 169.254.1.2
  clagd-backup-ip 192.168.200.12
  clagd-sys-mac 44:38:39:FF:40:94
 
auto bridge
iface bridge
    bridge-ports server01 peerlink vxlan10001 vxlan10100 vxlan10200
    bridge-vlan-aware yes
    bridge-vids 1 100 200
    bridge-pvid 1
 
auto vxlan10001
iface vxlan10001
    vxlan-id 10001
    vxlan-local-tunnelip 10.0.0.11
    bridge-access 1
    bridge-learning off
 
auto vxlan10100
iface vxlan10100
     vxlan-id 10100
     vxlan-local-tunnelip 10.0.0.11
     bridge-access 100
     bridge-learning off
 
auto vxlan10200
iface vxlan10200
     vxlan-id 10200
     vxlan-local-tunnelip 10.0.0.11
     bridge-access 200
     bridge-learning off</code></pre></td>
<td>leaf02 /etc/network/interfaces
<pre><code>cumulus@leaf02:~$ cat /etc/network/interfaces
 
auto lo
iface lo inet loopback
    alias loopback
    address 10.0.0.12/32
    clagd-vxlan-anycast-ip 10.10.10.20
 
auto eth0
iface eth0 inet dhcp
 
# uplinks
auto swp51
iface swp51
 
auto swp52
iface swp52
 
#host connections
auto swp1
iface swp1
 
auto server01
iface server01
  alias server01 MLAG bond
  bond-slaves swp1
  clag-id 1
 
auto peerlink
iface peerlink
  alias MLAG peerlink bond
  bond-slaves swp49 swp50
 
auto peerlink.4094
iface peerlink.4094
  address 169.254.1.2/30
  clagd-peer-ip 169.254.1.1
  clagd-backup-ip 192.168.200.11
  clagd-sys-mac 44:38:39:FF:40:94
 
auto bridge
iface bridge
    bridge-ports server01 peerlink vxlan10001 vxlan10100 vxlan10200
    bridge-vlan-aware yes
    bridge-vids 1 100 200
    bridge-pvid 1
 
auto vxlan10001
iface vxlan10001
    vxlan-id 10001
    vxlan-local-tunnelip 10.0.0.12
    bridge-access 1
    bridge-learning off
 
auto vxlan10100
iface vxlan10100
     vxlan-id 10100
     vxlan-local-tunnelip 10.0.0.12
     bridge-access 100
     bridge-learning off
 
auto vxlan10200
iface vxlan10200
     vxlan-id 10200
     vxlan-local-tunnelip 10.0.0.12
     bridge-access 200
     bridge-learning off</code></pre></td>
</tr>
<tr class="even">
<td>leaf01 /etc/frr/frr.conf
<pre><code>cumulus@leaf01:~$ cat /etc/frr/frr.conf 
!
username cumulus nopassword
!
log syslog
!
interface swp51
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp52
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65011
 bgp router-id 10.0.0.11
 bgp bestpath as-path multipath-relax
 neighbor FABRIC peer-group
 neighbor FABRIC remote-as external
 neighbor FABRIC description Internal FABRIC Network
 neighbor FABRIC capability extended-nexthop
 neighbor swp51 interface peer-group FABRIC
 neighbor swp52 interface peer-group FABRIC
 !
 address-family ipv4 unicast
  network 10.0.0.11/32
  network 10.10.10.20/32
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor FABRIC activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor FABRIC activate
  advertise-all-vni
 exit-address-family
 exit
!
line vty
!
end</code></pre></td>
<td>leaf02 /etc/frr/frr.conf
<pre><code>cumulus@leaf02:~$ cat /etc/frr/frr.conf 
!
username cumulus nopassword
!
log syslog
!
interface swp51
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp52
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65012
 bgp router-id 10.0.0.12
 bgp bestpath as-path multipath-relax
 neighbor FABRIC peer-group
 neighbor FABRIC remote-as external
 neighbor FABRIC description Internal FABRIC Network
 neighbor FABRIC capability extended-nexthop
 neighbor swp51 interface peer-group FABRIC
 neighbor swp52 interface peer-group FABRIC
 !
 address-family ipv4 unicast
  network 10.0.0.12/32
  network 10.10.10.20/32
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor FABRIC activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor FABRIC activate
  advertise-all-vni
 exit-address-family
 exit
!
line vty
!
end</code></pre></td>
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
<td><pre><code>cumulus@spine01:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.21/32
 
auto eth0
iface eth0 inet dhcp
 
# downlinks
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4</code></pre></td>
<td><pre><code>cumulus@spine01:~$ cat /etc/network/interfaces
auto lo
iface lo inet loopback
    address 10.0.0.22/32
 
auto eth0
iface eth0 inet dhcp
 
# downlinks
auto swp1
iface swp1
 
auto swp2
iface swp2
 
auto swp3
iface swp3
 
auto swp4
iface swp4</code></pre></td>
</tr>
<tr class="even">
<td>spine01 /etc/frr/frr.conf
<pre><code>cumulus@spine01:~$ cat /etc/frr/frr.conf 
!
username cumulus nopassword
!
log syslog
!
interface swp1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65020
 bgp router-id 10.0.0.21
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp1 interface peer-group fabric
 neighbor swp2 interface peer-group fabric
 neighbor swp3 interface peer-group fabric
 neighbor swp4 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.21/32
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor fabric activate
 exit-address-family
 exit
!
line vty
!
end</code></pre></td>
<td>spine02 /etc/frr/frr.conf
<pre><code>cumulus@spine02:~$ cat /etc/frr/frr.conf 
!
username cumulus nopassword
!
log syslog
!
interface swp1
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp2
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp3
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
interface swp4
 ipv6 nd ra-interval 10
 no ipv6 nd suppress-ra
!
router bgp 65020
 bgp router-id 10.0.0.22
 bgp bestpath as-path multipath-relax
 neighbor fabric peer-group
 neighbor fabric remote-as external
 neighbor fabric description Internal Fabric Network
 neighbor fabric capability extended-nexthop
 neighbor swp1 interface peer-group fabric
 neighbor swp2 interface peer-group fabric
 neighbor swp3 interface peer-group fabric
 neighbor swp4 interface peer-group fabric
 !
 address-family ipv4 unicast
  network 10.0.0.22/32
 exit-address-family
 !
!
 address-family ipv6 unicast
  neighbor fabric activate
 exit-address-family
 !
 address-family l2vpn evpn
  neighbor fabric activate
 exit-address-family
 exit
!
line vty
!
end</code></pre></td>
</tr>
</tbody>
</table>

#### <span>server01 and server03 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>cumulus@server01:~$ cat /etc/network/interfaces
 
auto eth0
iface eth0 inet dhcp
 
auto bond0
iface bond0
    bond-slaves eth1 eth2
    address 172.16.1.101/24
 
auto bond0.100
iface bond0.100
    address 172.16.100.101/24
 
auto bond0.200
iface bond0.200
    address 172.16.200.101/24</code></pre></td>
<td><pre><code>cumulus@server03:~$ cat /etc/network/interfaces
 
auto eth0
iface eth0 inet dhcp
 
auto bond0
iface bond0
    bond-slaves eth1 eth2
    address 172.16.1.103/24
 
auto bond0.100
iface bond0.100
    address 172.16.100.103/24
 
auto bond0.200
iface bond0.200
    address 172.16.200.103/24</code></pre></td>
</tr>
</tbody>
</table>
