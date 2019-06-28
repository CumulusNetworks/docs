---
title: Ethernet Virtual Private Network - EVPN
author: Cumulus Networks
weight: 145
aliases:
 - /display/CL330/Ethernet+Virtual+Private+Network+-+EVPN
 - /pages/viewpage.action?pageId=5866293
pageID: 5866293
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
---
Ethernet Virtual Private Network (EVPN) provides a control plane for
[VXLANs](/version/cumulus-linux-330/Network_Virtualization/) in Cumulus
Linux, with the following functionality:

  - VNI membership exchange between VTEPs using EVPN type-3 (Inclusive
    multicast Ethernet tag) routes.

  - Exchange of host MAC and IP addresses using EVPN type-2 (MAC/IP
    advertisement) routes.

  - Support for host/VM mobility (MAC and IP moves) through exchange of
    the MAC Mobility Extended community.

  - Support for dual-attached hosts via [VXLAN active-active
    mode](/version/cumulus-linux-330/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode);
    note that MAC synchronization between the peer switches is done
    using
    [MLAG](/version/cumulus-linux-330/Layer_One_and_Two/Multi-Chassis_Link_Aggregation_-_MLAG).

  - Support for ARP/ND suppression, which provides VTEPs with the
    ability to suppress ARP flooding over VXLAN tunnels.

  - Support for static ("sticky") MAC addresses and their exchange via
    EVPN.

You can provision and manage EVPN using
[NCLU](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility).

## <span>Using EVPN with Cumulus Linux</span>

As of Cumulus Linux version 3.3, EVPN is available with the standard set
of packages that make up the release and no longer needs any early
access packages to be installed. If you are doing a fresh installation
of Cumulus Linux 3.3, or are upgrading a switch that does not have the
`cumulus-evpn` package already installed, no additional steps are
needed. Otherwise, if you used EVPN with an older version of Cumulus
Linux on this switch, you need to remove the `cumulus-evpn` package
before upgrading to version 3.3.

To determine if you have the EVPN package installed in a pre-3.3 version
of Cumulus Linux, run the following command:

    cumulus@switch:~$ sudo dpkg -l quagga

If the Quagga version is *1.0.0+cl3u11* or higher, the EVPN package is
current, and you don't need to do anything.

If the version is *1.0.0+cl3eau8* or any earlier *3eau* version, then
you need to remove it.

Removing an older EVPN version

{{%notice note%}}

Please contact [Cumulus Networks
support](mailto:support@cumulusnetworks.com) if you need assistance with
reverting the EA packages or reconfiguring EVPN.

{{%/notice%}}

To remove the older version, do the following:

    cumulus@switch:~$ sudo apt-get update
    cumulus@switch:~$ sudo apt-get remove cumulus-evpn
    cumulus@switch:~$ sudo apt-get upgrade

To verify that you have the current EVPN package installed now, run the
following command:

    cumulus@switch:~$ sudo dpkg -l quagga

If the Quagga version is *1.0.0+cl3u11* or higher, the EVPN package is
current.

## <span>Configuring EVPN</span>

### <span>Enabling EVPN between BGP Neighbors</span>

You enable EVPN between
[BGP](/version/cumulus-linux-330/Layer_Three/Border_Gateway_Protocol_-_BGP)
neighbors by adding the address family *evpn* to the existing neighbor
address-family activation command.

For a non-VTEP device, such as a spine switch, that is merely
participating in EVPN route exchange (as in, the network deployment uses
hop-by-hop eBGP or the switch is acting as an iBGP route reflector),
activating the interface for the EVPN address family is the only
configuration needed.

EVPN supports the configuration of only these two BGP neighbor
address-family-specific configurations: `allowas-in` and
`route-reflector-client`.

To configure an EVPN route exchange with a BGP peer, the peer or
peer-group must be activated within the EVPN address-family:

    cumulus@switch:~$ net add bgp autonomous-system 65000
    cumulus@switch:~$ net add bgp evpn neighbor swp1 activate
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in
`/etc/quagga/Quagga.conf`:

    router bgp 65000
     address-family evpn
      neighbor swp1 activate

The above configuration does not result in BGP knowing about the local
VNIs defined on the system and advertising them to peers. This requires
additional configuration, [as described
below](#src-5866293_EthernetVirtualPrivateNetwork-EVPN-allvnis).

### <span id="src-5866293_EthernetVirtualPrivateNetwork-EVPN-allvnis" class="confluence-anchor-link"></span><span>Advertising All VNIs</span>

A single configuration variable enables the BGP control plane for all
VNIs configured on the switch. Set the variable `advertise-all-vni` to
provision all locally configured VNIs to be advertised by the BGP
control plane. Quagga is not aware of any local VNIs and MACs associated
with that VNI until `advertise-all-vni` is configured.

When a local VNI is learned by Quagga and there is no explicit
configuration for that VNI in Quagga, the route distinguisher (RD) and
import and export route targets (RTs) for this VNI are automatically
derived — the RD uses “RouterId:VNI-Index” and both RTs use “AS:VNI”.
The RD and RTs are used in the EVPN route exchange, with the former to
disambiguate EVPN routes in different VNIs (as they may have the same
MAC and/or IP address) while the latter describes the VPN membership for
the route. The "VNI-Index" used for the RD is a unique, internally
generated number for a VNI. It solely has local significance; on remote
switches, its only role is for route disambiguation. This number is used
instead of the VNI value itself because this number has to be less than
or equal to 65535. In the RT, the AS part is always encoded as a 2-byte
value in order to allow room for a large VNI. If the router has a 4-byte
AS, only the lower 2 bytes are used. This ensures a unique RT for
different VNIs while having the same RT for the same VNI across routers
in the same AS.

For eBGP EVPN peering, since the peers are in a different AS, using an
automatic RT of "AS:VNI" does not work for route import. Thus, the
import RT is actually treated as "\*:VNI" for determining which received
routes are applicable to a particular VNI. This only applies when the
import RT is auto-derived and not configured.

{{%notice note%}}

This configuration is only needed on leaf switches that are VTEPs.

{{%/notice%}}

To build upon the previous example, run the following commands to
advertise all VNIs:

    cumulus@switch:~$ net add bgp autonomous-system 65000
    cumulus@switch:~$ net add bgp evpn neighbor swp1 activate 
    cumulus@switch:~$ net add bgp evpn advertise-all-vni
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in
`/etc/quagga/Quagga.conf`:

    router bgp 65000
     address-family evpn
      neighbor swp1 activate
      advertise-all-vni

{{%notice note%}}

EVPN routes received from a BGP peer are accepted, even without this
explicit EVPN configuration. These routes are maintained in the global
EVPN routing table. However, they only become effective (that is,
imported into the per-VNI routing table and appropriate entries
installed in the kernel) when the VNI corresponding to the received
route is locally known.

{{%/notice%}}

### <span>Enabling EVPN with User-defined RDs and RTs</span>

EVPN also supports manual configuration of RDs and RTs, if you don't
want them derived automatically. To manually define RDs and RTs, use the
`vni` option within NCLU to configure the switch:

    cumulus@switch:~$ net add bgp evpn vni 10200 rd 172.16.10.1:20
    cumulus@switch:~$ net add bgp evpn vni 10200 route-target import 65100:20
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in
`/etc/quagga/Quagga.conf`:

    router bgp 65100
     address-family evpn
      neighbor SPINE activate
      advertise-all-vni
      vni 10200
       rd 172.16.10.1:20
       route-target import 65100:20

{{%notice note%}}

These commands are per VNI and must be specified under `address-family
evpn` in BGP.

{{%/notice%}}

{{%notice note%}}

If you delete the RD or RT later, it reverts back to its corresponding
default value.

{{%/notice%}}

You can configure multiple RT values for import or export for a VNI. In
addition, you can configure both the import and export route targets
with a single command by using `route-target both`:

    cumulus@switch:~# net add bgp evpn vni 10400 route-target import 100:400
    cumulus@switch:~# net add bgp evpn vni 10400 route-target import 100:500
    cumulus@switch:~# net add bgp evpn vni 10500 route-target both 65000:500
    cumulus@switch:~# net pending
    cumulus@switch:~# net commit

These commands create the following configuration snippet in the
`/etc/quagga/Quagga.conf` file:

    address-family evpn
      neighbor SPINE activate
      advertise-all-vni 
      vni 10400
        route-target import 100:400
        route-target import 100:500
      vni 10500
        route-target import 65000:500
        route-target export 65000:500

### <span>Enabling EVPN in an iBGP Environment with an OSPF Underlay</span>

EVPN can be deployed with an
[OSPF](/version/cumulus-linux-330/Layer_Three/Open_Shortest_Path_First_-_OSPF_-_Protocol)
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
`/etc/quagga/Quagga.conf`:

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
     address-family evpn
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
VxLAN interfaces to avoid race conditions between control plane learning
and data plane learning. In the `/etc/network/interfaces` file,
configure the `bridge-learning` value to *off*:

    cumulus@switch:~$ net add vxlan vxlan200 vxlan id 10200
    cumulus@switch:~$ net add vxlan vxlan200 vxlan local-tunnelip 10.0.0.1
    cumulus@switch:~$ net add vxlan vxlan200 bridge access 200
    cumulus@switch:~$ net add vxlan vxlan200 bridge learning off
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following code snippet in the
`/etc/network/interfaces` file:

    auto vxlan200
    iface vxlan200
        bridge-access 200
        bridge-learning off
        vxlan-id 10200
        vxlan-local-tunnelip 10.0.0.1

{{%notice tip%}}

For a bridge in [traditional
mode](/version/cumulus-linux-330/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges),
you must edit the bridge configuration in the `/etc/network/interfaces`
file in a text editor:

    auto bridge1
    iface bridge1
        bridge-ports swp3.100 swp4.100 vxlan100
        bridge-learning vxlan100=off

{{%/notice%}}

## <span>ARP and ND Suppression</span>

ARP suppression in an EVPN context refers to the ability of a VTEP to
suppress ARP flooding over VXLAN tunnels as much as possible. Instead, a
local proxy handles ARP requests received from locally attached hosts
for remote hosts. ARP suppression is the implementation for IPv4; ND
suppression is the implementation for IPv6.

ARP suppression is not enabled by default. You configure ARP/ND
suppression on a VXLAN interface. You also need to create an SVI for the
neighbor entry.

To configure ARP suppression, use
[NCLU](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility).
Here's an example configuration using 2 VXLANs, 10100 and 10200, and 2
VLANs, 100 and 200:

    cumulus@switch:~$ net add bridge bridge ports vtep100,vtep200
    cumulus@switch:~$ net add bridge bridge vids 100,200
    cumulus@switch:~$ net add vxlan vtep100 vxlan id 10100
    cumulus@switch:~$ net add vxlan vtep200 vxlan id 10200
    cumulus@switch:~$ net add vxlan vtep100 bridge learning off
    cumulus@switch:~$ net add vxlan vtep200 bridge learning off
    cumulus@switch:~$ net add vxlan vtep100 bridge access 100
    cumulus@switch:~$ net add vxlan vtep100 bridge arp-nd-suppress on
    cumulus@switch:~$ net add vxlan vtep200 bridge arp-nd-suppress on
    cumulus@switch:~$ net add vxlan vtep200 bridge access 200
    cumulus@switch:~$ net add vxlan vtep100 vxlan local-tunnelip 110.0.0.1
    cumulus@switch:~$ net add vxlan vtep200 vxlan local-tunnelip 110.0.0.1
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
        bridge-ports vtep100 vtep200
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
     
    auto vtep100
    iface vtep100
        bridge-access 100
        bridge-arp-nd-suppress on
        bridge-learning off
        vxlan-id 10100
        vxlan-local-tunnelip 110.0.0.1
     
    auto vtep200
    iface vtep200
         bridge-learning off
         bridge-access 200
         bridge-arp-nd-suppress on
         vxlan-id 10200
         vxlan-local-tunnelip 110.0.0.1

{{%notice warning%}}

ARP suppression does not interoperate with [VXLAN active-active
mode](/version/cumulus-linux-330/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode)
in an optimal manner, because the neighbor entries are not synced by a
control plane. Thus, ARPs may not be suppressed sometimes. This has no
impact on forwarding.

{{%/notice%}}

{{%notice tip%}}

For a bridge in [traditional
mode](/version/cumulus-linux-330/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges),
you must edit the bridge configuration in the `/etc/network/interfaces`
file in a text editor:

    auto bridge1
    iface bridge1
        bridge-ports swp3.100 swp4.100 vxlan100
        bridge-learning vxlan100=off
        bridge-arp-nd-suppress vxlan100=on
        ip6-forward off
        ip-forward off 

{{%/notice%}}

You can examine the overall ARP cache:

``` 
cumulus@switch:~$ net show evpn arp-cache vni 10100
Number of ARPs (local and remote) known for this VNI: 9
IP              Type   MAC               Remote VTEP          
50.1.1.11       local  00:02:00:00:00:01 
50.1.1.12       local  00:02:00:00:00:02 
50.1.1.22       remote 00:02:00:00:00:04 110.0.0.2            
2001:50:1:1::11 local  00:02:00:00:00:01 
50.1.1.31       remote 00:02:00:00:00:05 110.0.0.3            
50.1.1.42       remote 00:02:00:00:00:08 110.0.0.4            
50.1.1.21       remote 00:02:00:00:00:03 110.0.0.2            
50.1.1.32       remote 00:02:00:00:00:06 110.0.0.3            
50.1.1.41       remote 00:02:00:00:00:07 110.0.0.4  
```

You can also examine the ARP cache for a specific neighbor:

    cumulus@switch:~$ net show evpn arp-cache vni 10100 ip 50.1.1.32
    IP: 50.1.1.32
     MAC: 00:02:00:00:00:06 Remote VTEP: 110.0.0.3

To filter the ARP cache for a part of an IP address, use `ip neighbor
show`, then pipe it through `grep`:

    cumulus@switch:~$ sudo ip neighbor show | grep 11
    11.11.11.112 dev bridge.100 lladdr 00:02:00:00:00:02 REACHABLE
    11.11.11.133 dev bridge.100 lladdr 00:02:00:00:00:0b offload STALE
    11.11.11.142 dev bridge.100 lladdr 00:02:00:00:00:0e offload STALE
    11.11.11.111 dev bridge.100 lladdr 00:02:00:00:00:01 REACHABLE
    11.11.44.114 dev bridge.400 lladdr 00:02:00:00:00:04 REACHABLE
    11.11.11.141 dev bridge.100 lladdr 00:02:00:00:00:0d offload STALE
    11.11.11.132 dev bridge.100 lladdr 00:02:00:00:00:0a offload STALE
    11.11.44.144 dev bridge.400 lladdr 00:02:00:00:00:10 offload STALE
    11.11.11.131 dev bridge.100 lladdr 00:02:00:00:00:09 offload STALE
    11.11.44.134 dev bridge.400 lladdr 00:02:00:00:00:0c offload STALE
    11.11.11.123 dev bridge.100 lladdr 00:02:00:00:00:07 offload STALE
    11.11.44.124 dev bridge.400 lladdr 00:02:00:00:00:08 offload STALE
    11.11.11.113 dev bridge.100 lladdr 00:02:00:00:00:03 REACHABLE
    11.11.11.122 dev bridge.100 lladdr 00:02:00:00:00:06 offload STALE
    11.11.11.143 dev bridge.100 lladdr 00:02:00:00:00:0f offload STALE
    11.11.11.121 dev bridge.100 lladdr 00:02:00:00:00:05 offload STALE
    2011:11:11::142 dev bridge.100 lladdr 00:02:00:00:00:0e offload PROBE
    2011:11:11::133 dev bridge.100 lladdr 00:02:00:00:00:0b offload PROBE
    2011:11:44::124 dev bridge.400 lladdr 00:02:00:00:00:08 offload REACHABLE
    2011:11:11::121 dev bridge.100 lladdr 00:02:00:00:00:05 offload PROBE
    2011:11:44::144 dev bridge.400 lladdr 00:02:00:00:00:10 offload PROBE
    2011:11:11::112 dev bridge.100 lladdr 00:02:00:00:00:02 router REACHABLE
    2011:11:11::141 dev bridge.100 lladdr 00:02:00:00:00:0d offload DELAY
    2011:11:11::132 dev bridge.100 lladdr 00:02:00:00:00:0a offload REACHABLE
    2011:11:11::123 dev bridge.100 lladdr 00:02:00:00:00:07 offload PROBE
    2011:11:44::114 dev bridge.400 lladdr 00:02:00:00:00:04 router REACHABLE
    2011:11:11::111 dev bridge.100 lladdr 00:02:00:00:00:01 router REACHABLE
    2011:11:11::143 dev bridge.100 lladdr 00:02:00:00:00:0f offload DELAY
    2011:11:44::134 dev bridge.400 lladdr 00:02:00:00:00:0c offload PROBE
    2011:11:11::131 dev bridge.100 lladdr 00:02:00:00:00:09 offload DELAY
    2011:11:11::122 dev bridge.100 lladdr 00:02:00:00:00:06 offload REACHABLE
    2011:11:11::113 dev bridge.100 lladdr 00:02:00:00:00:03 router REACHABLE

For bridge information, use `net show bridge macs`:

    cumulus@switch:~$ net show bridge macs 
    VLAN      Master    Interface    MAC                TunnelDest    State      Flags          LastSeen
    --------  --------  -----------  -----------------  ------------  ---------  -------------  ----------
    100       bridge    bridge       44:38:39:00:69:8a                permanent                 00:16:44
    100       bridge    swp2s2       00:02:00:00:00:01                                          00:00:04
    100       bridge    swp2s3       00:02:00:00:00:02                                          00:00:04
    100       bridge    swp18s0      00:02:00:00:00:03                                          00:00:04
    100       bridge    vxlan10100   00:02:00:00:00:0a                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:0b                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:0d                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:0e                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:0f                           offload        00:16:39
    100       bridge    vxlan10100   00:02:00:00:00:05                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:06                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:07                           offload        00:16:40
    100       bridge    vxlan10100   00:02:00:00:00:09                           offload        00:16:40
    200       bridge    bridge       44:38:39:00:69:8a                permanent                 00:16:44
    300       bridge    bridge       44:38:39:00:69:8a                permanent                 00:16:44
    400       bridge    bridge       44:38:39:00:69:8a                permanent                 00:16:43
    400       bridge    swp18s1      00:02:00:00:00:04                                          00:00:04
    400       bridge    vxlan10400   00:02:00:00:00:0c                           offload        00:16:40
    400       bridge    vxlan10400   00:02:00:00:00:08                           offload        00:16:40
    400       bridge    vxlan10400   00:02:00:00:00:10                           offload        00:16:39
    untagged            vxlan10100   00:00:00:00:00:00  10.10.3.12    permanent  self           00:16:41
    untagged            vxlan10100   00:00:00:00:00:00  10.10.3.13    permanent  self           00:16:41
    untagged            vxlan10100   00:00:00:00:00:00  10.10.3.14    permanent  self           00:16:41
    untagged            vxlan10100   00:02:00:00:00:0a  10.10.3.13               self, offload  00:16:40
    untagged            vxlan10100   00:02:00:00:00:0b  10.10.3.13               self, offload  00:16:41
    untagged            vxlan10100   00:02:00:00:00:0d  10.10.3.14               self, offload  00:16:41
    untagged            vxlan10100   00:02:00:00:00:0e  10.10.3.14               self, offload  00:16:41
    untagged            vxlan10100   00:02:00:00:00:0f  10.10.3.14               self, offload  00:16:39
    untagged            vxlan10100   00:02:00:00:00:05  10.10.3.12               self, offload  00:16:41
    untagged            vxlan10100   00:02:00:00:00:06  10.10.3.12               self, offload  00:16:41
    untagged            vxlan10100   00:02:00:00:00:07  10.10.3.12               self, offload  00:16:41
    untagged            vxlan10100   00:02:00:00:00:09  10.10.3.13               self, offload  00:16:41
    untagged            vxlan10200   00:00:00:00:00:00  10.10.3.12    permanent  self           00:16:41
    untagged            vxlan10200   00:00:00:00:00:00  10.10.3.13    permanent  self           00:16:41
    untagged            vxlan10200   00:00:00:00:00:00  10.10.3.14    permanent  self           00:16:41
    untagged            vxlan10300   00:00:00:00:00:00  10.10.3.12    permanent  self           00:16:41
    untagged            vxlan10300   00:00:00:00:00:00  10.10.3.13    permanent  self           00:16:41
    untagged            vxlan10300   00:00:00:00:00:00  10.10.3.14    permanent  self           00:16:41
    untagged            vxlan10400   00:00:00:00:00:00  10.10.3.12    permanent  self           00:16:41
    untagged            vxlan10400   00:00:00:00:00:00  10.10.3.13    permanent  self           00:16:41
    untagged            vxlan10400   00:00:00:00:00:00  10.10.3.14    permanent  self           00:16:41
    untagged            vxlan10400   00:02:00:00:00:0c  10.10.3.13               self, offload  00:16:41
    untagged            vxlan10400   00:02:00:00:00:08  10.10.3.12               self, offload  00:16:41
    untagged            vxlan10400   00:02:00:00:00:10  10.10.3.14               self, offload  00:16:39
    untagged  bridge    swp2s2       44:38:39:00:69:8a                permanent                 00:16:44
    untagged  bridge    swp2s3       44:38:39:00:69:8b                permanent                 00:16:44
    untagged  bridge    swp18s0      44:38:39:00:69:c8                permanent                 00:16:44
    untagged  bridge    swp18s1      44:38:39:00:69:c9                permanent                 00:16:44
    untagged  bridge    vxlan10100   ca:b4:aa:b2:62:64                permanent                 00:16:44
    untagged  bridge    vxlan10200   de:b7:11:58:c5:6c                permanent                 00:16:44
    untagged  bridge    vxlan10300   c6:8f:a6:7c:9b:bd                permanent                 00:16:44
    untagged  bridge    vxlan10400   fa:e1:44:86:93:99                permanent                 00:16:44

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
        bridge-ports swp1 vxlan10101
        bridge-vids 101
        bridge-vlan-aware yes
        post-up bridge fdb add 00:11:22:33:44:55 dev swp1 vlan 101 master static

{{%notice tip%}}

For a bridge in [traditional
mode](/version/cumulus-linux-330/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges),
you must edit the bridge configuration in the `/etc/network/interfaces`
file in a text editor:

    auto br101
    iface br101
        bridge-ports swp1.101 vxlan10101
        bridge-learning vxlan10101=off
        post-up bridge fdb add 00:11:22:33:44:55 dev swp1.101 master static

{{%/notice%}}

## <span>Handling BUM Traffic</span>

With EVPN, the only method of handling BUM traffic is [Head End
Replication
(HER)](Lightweight_Network_Virtualization_-_LNV_Overview.html#src-5866264_LightweightNetworkVirtualization-LNVOverview-head-end).
HER is enabled by default, as it is when [Lightweight Network
Virtualization
(LNV)](/display/CL330/Lightweight+Network+Virtualization+-+LNV+Overview)
is used.

## <span>EVPN and VXLAN Active-Active Mode</span>

There is no specific configuration to enable EVPN to work with [VXLAN
active-active
mode](/version/cumulus-linux-330/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode).
Both switches in the MLAG pair establish EVPN peering with other EVPN
speakers (for example, with spine switches, if using hop-by-hop eBGP)
and inform about their locally known VNIs and MACs. When MLAG is active,
both switches announce this information with the shared anycast IP
address.

MLAG syncs information between the two switches in the MLAG pair, EVPN
does not synchronize. Therefore, Cumulus Networks recommends you do not
configure EVPN peering between the MLAG switches over the peerlink.

## <span>Example Configuration</span>

The following configurations are used throughout this chapter. You can
find the flat-file configurations for the network devices in the Cumulus
Networks [GitHub
repository](https://github.com/CumulusNetworks/cldemo-evpn/tree/master/config).
Only a subset is shown here for brevity (not shown are configurations
for leaf03, leaf04, server03, server04). Here is the topology diagram:

{{% imgOld 0 %}}

### <span>leaf01 and leaf02 Configurations</span>

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
 
auto br0
iface br0
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
 
auto br0
iface br0
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
<td>leaf01 /etc/quagga/Quagga.conf
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
 address-family evpn
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
<td>leaf02 /etc/quagga/Quagga.conf
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
 address-family evpn
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

### <span>spine01 and spine02 Configurations</span>

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
<td>spine01 /etc/quagga/Quagga.conf
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
 address-family evpn
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
<td>spine02 /etc/quagga/Quagga.conf
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
 address-family evpn
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

### <span>server01 and server02 Configurations</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>/etc/network/interfaces</p>
<pre><code>#configuration is for Cumulus VX
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
<td><p>/etc/network/interfaces</p>
<pre><code>#configuration is for Cumulus VX
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

## <span>Testing Connectivity between Servers</span>

SSH to server01 and ping the VLAN1 IP address on server02:

    user@server01:~$ ping 172.16.1.102
    PING 172.16.1.102 (172.16.1.102) 56(84) bytes of data.
    64 bytes from 172.16.1.102: icmp_seq=1 ttl=64 time=2.52 ms
    64 bytes from 172.16.1.102: icmp_seq=2 ttl=64 time=2.74 ms
    ^C
    --- 172.16.1.102 ping statistics ---
    2 packets transmitted, 2 received, 0% packet loss, time 1001ms
    rtt min/avg/max/mdev = 2.528/2.638/2.749/0.121 ms

The following table lists all the servers IP addresses to test
connectivity across the L3 fabric:

|         | server01       | server02       | server03       | server04       |
| ------- | -------------- | -------------- | -------------- | -------------- |
| VLAN1   | 172.16.1.101   | 172.16.1.102   | 172.16.1.103   | 172.16.1.104   |
| VLAN100 | 172.16.100.101 | 172.16.100.102 | 172.16.100.103 | 172.16.100.104 |
| VLAN200 | 172.16.200.101 | 172.16.200.102 | 172.16.200.103 | 172.16.200.104 |

## <span>Cumulus Linux Output Commands</span>

You can use various `iproute2` commands to examine links, VLAN mappings
and displaying bridge FDB data:

  - ip \[-d\] link show

  - bridge link show

  - bridge vlan show

  - bridge \[-s\] fdb show

For example, the output from the following `bridge fdb show` command
reveals information relevant only for a VTEP.

  - 3 remote VTEPs (10.0.0.5, 10.0.0.6 and 80.80.80.2) for each of the 2
    VNIs.

  - MAC address 00:02:00:00:00:03 is a local MAC learned over a bond
    interface while MAC address 00:02:00:00:00:08 is a remote MAC from
    VTEP 80.80.80.2 for VNI 10100 (vtep100).

  - The entries with MAC “00:00:00:00:00:00” are for BUM traffic
    replication.

<!-- end list -->

    cumulus@switch:~$ bridge fdb show
    00:02:00:00:00:0f dev swp3 master bridge permanent
    00:02:00:00:00:01 dev swp3 vlan 1 master bridge 
    00:02:00:00:00:04 dev peerlink vlan 1 master bridge 
    00:02:00:00:00:12 dev peerlink master bridge permanent
    92:b0:8f:b6:82:7b dev vtep100 master bridge permanent
    00:02:00:00:00:08 dev vtep100 vlan 100 master bridge 
    00:00:00:00:00:00 dev vtep100 dst 10.0.0.5 self permanent
    00:00:00:00:00:00 dev vtep100 dst 10.0.0.6 self permanent
    00:00:00:00:00:00 dev vtep100 dst 80.80.80.2 self permanent
    00:02:00:00:00:08 dev vtep100 dst 80.80.80.2 self 
    5e:75:42:b8:47:e6 dev vtep200 master bridge permanent
    00:00:00:00:00:00 dev vtep200 dst 10.0.0.5 self permanent
    00:00:00:00:00:00 dev vtep200 dst 10.0.0.6 self permanent
    00:00:00:00:00:00 dev vtep200 dst 80.80.80.2 self permanent
    00:02:00:00:00:10 dev bond0 master bridge permanent
    02:02:00:00:00:03 dev bond0 vlan 1 master bridge 
    02:02:00:00:00:02 dev bond0 vlan 1 master bridge 
    00:02:00:00:00:03 dev bond0 vlan 100 master bridge 

## <span>BGP Output Commands</span>

The following commands are not unique to EVPN but help troubleshoot
connectivity and route propagation. You can display the L3 fabric by
running `net show bgp summary` command on one of the spines:

    cumulus@spine01:~$ net show bgp summary
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

You can see the loopback addresses for all the network devices
participating in BGP by running the `net show bgp` command:

    cumulus@spine01:~$ net show bgp
     
    show bgp ipv4 unicast
    =====================
    BGP table version is 9, local router ID is 110.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                  i internal, r RIB-failure, S Stale, R Removed
    Origin codes: i - IGP, e - EGP, ? - incomplete
       Network          Next Hop            Metric LocPrf Weight Path
    *> 20.0.0.1/32      swp49s0
                                                          0             0 65100 i
    *> 20.0.0.2/32      swp49s1
                                                          0             0 65100 i
    *> 110.0.0.1/32     0.0.0.0                  0         32768 i
    *= 110.0.0.2/32     swp49s1
                                                                        0 65100 65002 i
    *>                  swp49s0
                                                                        0 65100 65002 i
    *= 110.0.0.3/32     swp49s1
                                                                        0 65100 65003 i
    *>                  swp49s0
                                                                        0 65100 65003 i
    *= 110.0.0.4/32     swp49s1
                                                                        0 65100 65004 i
    *>                  swp49s0
                                                                        0 65100 65004 i
    Displayed  6 out of 9 total prefixes
     
    show bgp ipv6 unicast
    =====================
    No BGP prefixes displayed, 0 exist

## <span>EVPN Output Commands</span>

The following commands are unique to EVPN address-families and VXLAN.
Note that just because two network nodes are BGP peers does not mean
they are EVPN address-family peers or are exchanging VXLAN information.

### <span>Displaying EVPN address-family Peers</span>

The network device participating in BGP EVPN address-family can be shown
using the ` show net show bgp evpn summary  `command:

    cumulus@leaf01:~$ net show bgp evpn summary 
    BGP router identifier 110.0.0.1, local AS number 65001 vrf-id 0
    BGP table version 0
    RIB entries 15, using 2040 bytes of memory
    Peers 2, using 42 KiB of memory
    Peer groups 1, using 72 bytes of memory
    Neighbor        V         AS MsgRcvd MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
    s1(swp49s0)     4      65100      25      31        0    0    0 00:43:26           18
    s2(swp49s1)     4      65100      25      31        0    0    0 00:43:25           18
    Total number of neighbors 2

### <span>Displaying VNIs or EVPN VXLANs</span>

You can display the configured VNIs on a network device participating in
BGP EVPN by running the `show bgp evpn vni` command. This command works
only when run on a VTEP.

The following example examines leaf01, where 2 VNIs are configured —
10100 and 10200. It identifies the VTEPs that are part of each VNI,
their IP addresses and the number of MAC addresses and neighbors
associated with them:

``` 
cumulus@leaf01:~$ net show evpn vni
Number of VNIs: 2
VNI        VxLAN IF              VTEP IP         # MACs   # ARPs   # Remote VTEPs 
10200      vtep200               110.0.0.1       8        8        3              
10100      vtep100               110.0.0.1       8        9        3          
```

You can examine the EVPN configuration for a single VXLAN:

    cumulus@leaf01:~$ net show evpn vni 10100
    VNI: 10100
     VxLAN interface: vtep100 ifIndex: 88 VTEP IP: 110.0.0.1
     Remote VTEPs for this VNI:
      110.0.0.2
      110.0.0.4
      110.0.0.3
     Number of MACs (local and remote) known for this VNI: 8
     Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 9

The corresponding BGP configuration for VNI 10200 is as follows (only
the EVPN section is shown):

    cumulus@switch:~$ net show configuration files 
     
    ...
     
     address-family ipv4 unicast
      network 110.0.0.1/32
     exit-address-family
     address-family evpn
      neighbor SPINE activate
      advertise-all-vni
     exit-address-family
     
    ...

### <span>Examining Local and Remote MAC Addresses for a VNI in Quagga</span>

You can examine all local and remote MAC addresses for a VNI by running
`net show evpn mac vni <vni>`.

    cumulus@leaf01:~$ net show evpn mac vni 10100
    Number of MACs (local and remote) known for this VNI: 8
    MAC               Type   Intf/Remote VTEP      VLAN 
    00:02:00:00:00:01 local  swp49s2               100  
    00:02:00:00:00:02 local  swp49s3               100  
    00:02:00:00:00:03 remote 110.0.0.2            
    00:02:00:00:00:04 remote 110.0.0.2            
    00:02:00:00:00:05 remote 110.0.0.3            
    00:02:00:00:00:06 remote 110.0.0.3            
    00:02:00:00:00:07 remote 110.0.0.4            
    00:02:00:00:00:08 remote 110.0.0.4 

You can examine MAC addresses across VNIs using `net show evpn mac vni
all`:

``` 
cumulus@leaf01:~$ net show evpn mac vni all
 
VNI 10200 #MACs (local and remote) 8
 
 
MAC               Type   Intf/Remote VTEP      VLAN 
00:02:00:00:00:01 local  swp49s2               200  
00:02:00:00:00:02 local  swp49s3               200  
00:02:00:00:00:03 remote 110.0.0.2            
00:02:00:00:00:04 remote 110.0.0.2            
00:02:00:00:00:05 remote 110.0.0.3            
00:02:00:00:00:06 remote 110.0.0.3            
00:02:00:00:00:07 remote 110.0.0.4            
00:02:00:00:00:08 remote 110.0.0.4            
 
 
VNI 10100 #MACs (local and remote) 8
 
 
MAC               Type   Intf/Remote VTEP      VLAN 
00:02:00:00:00:01 local  swp49s2               100  
00:02:00:00:00:02 local  swp49s3               100  
00:02:00:00:00:03 remote 110.0.0.2            
00:02:00:00:00:04 remote 110.0.0.2            
00:02:00:00:00:05 remote 110.0.0.3            
00:02:00:00:00:06 remote 110.0.0.3            
00:02:00:00:00:07 remote 110.0.0.4            
00:02:00:00:00:08 remote 110.0.0.4   
```

You can examine MAC addresses for a remote VTEP and/or query a specific
MAC address. This command only works when run on a VTEP:

    cumulus@leaf01:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:03
    MAC: 00:02:00:00:00:03
     Remote VTEP: 110.0.0.2 ARP ref: 1
    cumulus@leaf01:~$ 
    cumulus@leaf01:~$ 
    cumulus@leaf01:~$ net show evpn mac vni 10100 mac 00:02:00:00:00:01
    MAC: 00:02:00:00:00:01
     Intf: swp49s2(53) VLAN: 100 ARP ref: 0

### <span>Displaying the Global BGP EVPN Routing Table</span>

Run the `net show bgp evpn route` command to display all EVPN routes at
the same time:

    cumulus@leaf01:~$ net show bgp evpn route 
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
    Route Distinguisher: 110.0.0.2:1
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:04]:[32]:[50.1.1.22]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:04]:[32]:[50.1.1.22]
                        110.0.0.2                              0 65100 65002 i
    *  [3]:[0]:[32]:[110.0.0.2]
                        110.0.0.2                              0 65100 65002 i
    *> [3]:[0]:[32]:[110.0.0.2]
                        110.0.0.2                              0 65100 65002 i
     
    ... ## output truncated
     
    Displayed 29 prefixes (47 paths)

The output ` *> [3]:[0]:[32]:[110.0.0.2]  `(the last line above) is
explained as follows:

| Output    | Explanation                         |
| --------- | ----------------------------------- |
| \[3\]     | Type 3 EVPN route                   |
| \[0\]     | Ethernet tag                        |
| \[32\]    | IP address length of 32 bits        |
| 110.0.0.2 | IPv4 address originating this route |

### <span>Displaying EVPN Type-2 (MAC/IP) Routes</span>

To display only EVPN type-2 (MAC/IP) routes, run `show bgp evpn route
type macip`. The output displays the EVPN route-type fields followed by
type-specific fields:

  - Type 2 route: \[type\]:\[ESI\]:\[ET\]:\[MAC length\]:\[MAC\]

  - Type 2 route with ARP suppression: \[type\]:\[ESI\]:\[ET\]:\[MAC
    length\]:\[MAC\]:\[IP length\]:\[IP\]
    
      - The Ethernet Segment Id (ESI) and Ethernet Tag (ET) are always
        0.

  - Type 3 route: \[type\]:\[ET\]:\[Originating Router IP\]
    
      - The Ethernet Tag (ET) is always 0.
    
      - The "Originating Router IP" is the VTEP local IP for the
        corresponding VNI.

<!-- end list -->

    cumulus@leaf01:~$ net show bgp evpn route type macip 
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
    Route Distinguisher: 110.0.0.1:2
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[32]:[60.1.1.11]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[32]:[60.1.1.12]
                        110.0.0.1                          32768 i
    Route Distinguisher: 110.0.0.2:1
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:04]:[32]:[50.1.1.22]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:04]:[32]:[50.1.1.22]
                        110.0.0.2                              0 65100 65002 i
     
    ... ## output truncated
     
    Displayed 21 prefixes (33 paths) (of requested type)

### <span>Displaying a Specific EVPN Route</span>

To drill down on a specific route for more information, run the `net
show bgp evpn route rd <VTEP:VXLAN>` command. The following example
shows leaf01 receiving type-2 and type-3 routes from two spine switches
(s1 and s2). The actual remote VTEP is 110.0.0.2, specified in the next
hop of the route. Both routes contain the BGP Encapsulation extended
community (ET) with value 8 (VXLAN); the type-2 route also carries the
VNI (10100).

    cumulus@leaf01:~$ net show bgp evpn route rd 110.0.0.2:1
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
     
     
    BGP routing table entry for 110.0.0.2:1:[2]:[0]:[0]:[48]:[00:02:00:00:00:03]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp49s0) s2(swp49s1)
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:03] VNI 10100
      65100 65002
        110.0.0.2 from s2(swp49s1) (20.0.0.2)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 179
          Last update: Wed Apr 26 20:03:55 2017
     
     
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:03] VNI 10100
      65100 65002
        110.0.0.2 from s1(swp49s0) (20.0.0.1)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 177
          Last update: Wed Apr 26 20:03:55 2017
     
     
    BGP routing table entry for 110.0.0.2:1:[2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp49s0) s2(swp49s1)
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21] VNI 10100
      65100 65002
        110.0.0.2 from s2(swp49s1) (20.0.0.2)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 112
          Last update: Wed Apr 26 19:04:20 2017
     
     
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21] VNI 10100
      65100 65002
        110.0.0.2 from s1(swp49s0) (20.0.0.1)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 91
          Last update: Wed Apr 26 19:04:19 2017
     
    ...
     
    BGP routing table entry for 110.0.0.2:1:[3]:[0]:[32]:[110.0.0.2]
    Paths: (2 available, best #2)
      Advertised to non peer-group peers:
      s1(swp49s0) s2(swp49s1)
      Route [3]:[0]:[32]:[110.0.0.2]
      65100 65002
        110.0.0.2 from s2(swp49s1) (20.0.0.2)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 118
          Last update: Wed Apr 26 19:04:20 2017
     
     
      Route [3]:[0]:[32]:[110.0.0.2]
      65100 65002
        110.0.0.2 from s1(swp49s0) (20.0.0.1)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 97
          Last update: Wed Apr 26 19:04:19 2017
     
    Displayed 5 prefixes (10 paths) with this RD

{{%notice note%}}

  - Though the local VNI is included in the type-2 route, the receiver
    does not use it. It uses the received RT to match the route to an
    appropriate local VNI and then assumes the remote VTEP uses the same
    VNI value — that is, global VNIs are in use.

  - If MAC mobility extended community is exchanged, it gets shown in
    the above output.

  - If the remote MAC is dual attached, the next hop for the EVPN route
    is the anycast IP address of the remote
    [MLAG](/version/cumulus-linux-330/Layer_One_and_Two/Multi-Chassis_Link_Aggregation_-_MLAG)
    pair (when MLAG is active). You can see this in the above example,
    where 110.0.0.2 is actually the anycast IP of the MLAG pair.

{{%/notice%}}

### <span>Displaying the per-VNI EVPN Routing Table</span>

Received EVPN routes are maintained in the global EVPN routing table
(described above), even if there are no appropriate local VNIs to
**import** them into. For example, a spine switch maintains the global
EVPN routing table even though there are no VNIs present on it. When
local VNIs are present, received EVPN routes are imported into the
per-VNI routing tables based on the route target attributes. The per-VNI
routing table can be examined using `net show bgp evpn route vni <vni>`:

    cumulus@leaf01:~$ net show bgp evpn route vni 10100
    BGP table version is 0, local router ID is 110.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[128]:[fe80::202:ff:fe00:1]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[128]:[fe80::202:ff:fe00:2]
                        110.0.0.1                          32768 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
                        110.0.0.2                              0 65100 65002 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[128]:[fe80::202:ff:fe00:3]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[128]:[fe80::202:ff:fe00:3]
                        110.0.0.2                              0 65100 65002 i
     
     
    ... ## output truncated
     
    Displayed 24 prefixes (45 paths)

### <span>Displaying a Specific MAC or Remote VTEP</span>

You can examine a specific MAC or IP (remote VTEP):

    cumulus@leaf01:~$ net show bgp evpn route vni 10100 mac 00:02:00:00:00:03
    BGP routing table entry for [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
    Paths: (2 available, best #2)
      Not advertised to any peer
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:03] VNI 10100
      Imported from 110.0.0.2:1:[2]:[0]:[0]:[48]:[00:02:00:00:00:03]
      65100 65002
        110.0.0.2 from s2(swp49s1) (20.0.0.2)
          Origin IGP, localpref 100, valid, external
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 180
          Last update: Wed Apr 26 20:03:55 2017
     
     
      Route [2]:[0]:[0]:[48]:[00:02:00:00:00:03] VNI 10100
      Imported from 110.0.0.2:1:[2]:[0]:[0]:[48]:[00:02:00:00:00:03]
      65100 65002
        110.0.0.2 from s1(swp49s0) (20.0.0.1)
          Origin IGP, localpref 100, valid, external, bestpath-from-AS 65100, best
          Extended Community: RT:65002:10100 ET:8
          AddPath ID: RX 0, TX 178
          Last update: Wed Apr 26 20:03:55 2017
     
    Displayed 2 paths for requested prefix

To display the VNI routing table for all VNIs, run `net show bgp evpn
route vni all`:

    cumulus@leaf01:~$ net show bgp evpn route vni all
     
    VNI: 10200
     
    BGP table version is 0, local router ID is 110.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:01]:[32]:[60.1.1.11]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]
                        110.0.0.1                          32768 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:02]:[32]:[60.1.1.12]
                        110.0.0.1                          32768 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
                        110.0.0.2                              0 65100 65002 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[60.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[60.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    ...
     
    *> [3]:[0]:[32]:[110.0.0.1]
                        110.0.0.1                          32768 i
    *  [3]:[0]:[32]:[110.0.0.2]
                        110.0.0.2                              0 65100 65002 i
    *> [3]:[0]:[32]:[110.0.0.2]
                        110.0.0.2                              0 65100 65002 i
    *  [3]:[0]:[32]:[110.0.0.3]
                        110.0.0.3                              0 65100 65003 i
    *> [3]:[0]:[32]:[110.0.0.3]
                        110.0.0.3                              0 65100 65003 i
    *  [3]:[0]:[32]:[110.0.0.4]
                        110.0.0.4                              0 65100 65004 i
    *> [3]:[0]:[32]:[110.0.0.4]
                        110.0.0.4                              0 65100 65004 i
     
     
    Displayed 20 prefixes (35 paths)
     
     
     
    VNI: 10100
     
    BGP table version is 0, local router ID is 110.0.0.1
    Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
    Origin codes: i - IGP, e - EGP, ? - incomplete
    EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]
    EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
       Network          Next Hop            Metric LocPrf Weight Path
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
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]
                        110.0.0.2                              0 65100 65002 i
    *  [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
    *> [2]:[0]:[0]:[48]:[00:02:00:00:00:03]:[32]:[50.1.1.21]
                        110.0.0.2                              0 65100 65002 i
     
    ...
     
    *> [3]:[0]:[32]:[110.0.0.1]
                        110.0.0.1                          32768 i
    *  [3]:[0]:[32]:[110.0.0.2]
                        110.0.0.2                              0 65100 65002 i
    *> [3]:[0]:[32]:[110.0.0.2]
                        110.0.0.2                              0 65100 65002 i
    *  [3]:[0]:[32]:[110.0.0.3]
                        110.0.0.3                              0 65100 65003 i
    *> [3]:[0]:[32]:[110.0.0.3]
                        110.0.0.3                              0 65100 65003 i
    *  [3]:[0]:[32]:[110.0.0.4]
                        110.0.0.4                              0 65100 65004 i
    *> [3]:[0]:[32]:[110.0.0.4]
                        110.0.0.4                              0 65100 65004 i
     
     
    Displayed 21 prefixes (36 paths)

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

You can identify static or "sticky" MACs in Quagga by the presence of
"MM:0, sticky MAC" in the Extended Community line of the output from
`net show bgp evpn route vni <vni> mac <mac>`:

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

The primary way to troubleshoot EVPN is by enabling Quagga debug logs.
The relevant debug options are:

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

The following caveat applies to EVPN in Cumulus Linux 3.3:

  - EVPN in Cumulus Linux does not support the ability to only announce
    certain VNIs. It supports either all locally defined VNIs (using the
    configuration specified above) or none of them. Provisioning options
    to advertise only specific VNIs will be introduced in a future
    release.

  - ARP suppression does not interoperate with [VXLAN active-active
    mode](/version/cumulus-linux-330/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/LNV_VXLAN_Active-Active_Mode)
    in an optimal manner, because the neighbor entries are not synced by
    a control plane. Thus, ARPs may not be suppressed sometimes. This
    has no impact on forwarding.
