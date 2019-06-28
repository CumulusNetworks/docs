---
title: VXLAN Routing
author: Cumulus Networks
weight: 151
aliases:
 - /display/CL34/VXLAN+Routing
 - /pages/viewpage.action?pageId=7112516
pageID: 7112516
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
VXLAN routing, sometimes referred to as inter-VXLAN routing, provides IP
routing between VXLAN VNIs in overlay networks. The routing of traffic
is based on the inner header or the overlay tenant IP address.

VXLAN routing is supported on the following platforms:

  - Broadcom Tomahawk using an internal loopback on one or more switch
    ports

  - Broadcom Trident II+ using a RIOT profile

  - Mellanox Spectrum

{{%notice tip%}}

If you want to use VXLAN routing on a Trident II switch, you must use a
[hyperloop](/version/cumulus-linux-343/Network_Virtualization/VXLAN_Hyperloop).

{{%/notice%}}

Features of VXLAN routing include:

  - [EVPN](/version/cumulus-linux-343/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN)
    is the control plane

  - [VRF](/version/cumulus-linux-343/Layer_Three/Virtual_Routing_and_Forwarding_-_VRF)
    support for overlay networks

  - Distributed asymmetric routing

  - Anycast routing and gateways

  - Host routing between and within data centers

Using EVPN as the control plane offers an integrated routing and
bridging solution as well as multi-tenancy support, where different
customers can share an IP address in the same network fabric.

Cumulus Networks also includes [early
access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
support for VXLAN routing using an external loopback, which only works
with
[LNV](/version/cumulus-linux-343/Network_Virtualization/Lightweight_Network_Virtualization_-_LNV_Overview/).

VXLAN routing currently does not support:

  - Overlay ECMP

  - Prefix routes

  - Symmetric routing

  - External routing

  - Centralized routing on Mellanox switches only

## <span>VXLAN Routing Data Plane and the Broadcom Tomahawk and Trident II+ Platforms</span>

On switches with Broadcom ASICs, VXLAN routing is supported only on the
Tomahawk and Trident II+ platforms. Below are some differences in how
VXLAN routing works on these switches.

### <span>Trident II+</span>

For Trident II+ switches, you can specify a VXLAN routing (RIOT —
routing in and out of tunnels) profile in the
`vxlan_routing_overlay.profile` field in the
`/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf`
file if you don't want to use the default. This profile determines the
maximum number of overlay next hops (adjacency entries). The profile is
one of the following:

  - *default*: 15% of the underlay next hops are set apart for overlay,
    up to a maximum of 8k next hops

  - *mode-1*: 25% of the underlay next hops are set apart for overlay

  - *mode-2*: 50% of the underlay next hops are set apart for overlay

  - *mode-3*: 80% of the underlay next hops are set apart for overlay

  - *disable*: disables VXLAN routing

The Trident II+ ASIC supports a maximum of 48k underlay next hops.

The maximum number of VXLAN SVI interfaces that can be allocated is 2k
(2048) regardless of which profile you specify.

If you want to disable VXLAN routing on a Trident II+ switch, set the
`vxlan_routing_overlay.profile` field to *disable*.

### <span>Tomahawk</span>

The Tomahawk ASIC does not support RIOT natively, so you must configure
the switch ports for VXLAN routing to use the internal loopback. The
internal loopback facilitates the recirculation of packets through the
ingress pipeline to achieve VXLAN routing. One or more loopback switch
ports can be bundled into a loopback trunk based on the amount of
bandwidth needed.

{{%notice note%}}

VXLAN routing using the internal loopback is supported only with
[VLAN-aware
bridges](/version/cumulus-linux-343/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments);
you cannot use a bridge in [traditional
mode](/version/cumulus-linux-343/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges).

{{%/notice%}}

To configure one or more switch ports for loopback mode, edit the
`/etc/cumulus/ports.conf` file, changing the port speed to *loopback*.
In the example below, swp8 and swp9 are configured for loopback mode:

    cumulus@switch:~$ sudo nano /etc/cumulus/ports.conf
     
    ...
     
    7=4x10G
    8=loopback
    9=loopback
    10=100G
     
     
    ...

After you save your changes to the `ports.conf` file, you must [restart
`switchd`](Configuring_switchd.html#src-7112319_Configuringswitchd-restartswitchd)
for the changes to take effect.

## <span>Configuring VXLAN Routing</span>

The following configuration using a single VTEP and does not include a
[VRF](/version/cumulus-linux-343/Layer_Three/Virtual_Routing_and_Forwarding_-_VRF).
It uses elements from the following topology:

{{% imgOld 0 %}}

{{%notice tip%}}

When configuring VXLAN routing, Cumulus Networks recommends that you
enable [ARP
suppression](Ethernet_Virtual_Private_Network_-_EVPN.html#src-7112514_EthernetVirtualPrivateNetwork-EVPN-arp)
on all VXLAN interfaces. Otherwise, when a locally-attached host ARPs
for the gateway, it will receive multiple responses, one from each
anycast gateway.

{{%/notice%}}

### <span>Configuring the Underlays</span>

1.  Configure the loopback address on the following network devices.
    
    leaf01:
    
        cumulus@leaf01:~$ net add loopback lo ip address 10.0.0.11/32
    
    leaf03:
    
        cumulus@leaf03:~$ net add loopback lo ip address 10.0.0.13/32
    
    spine01:
    
        cumulus@spine01:~$ net add loopback lo ip address 10.0.0.21/32

2.  Advertise the loopback addresses into the underlay.
    
    leaf01:
    
        cumulus@leaf01:~$ net add bgp autonomous-system 65011
        cumulus@leaf01:~$ net add bgp neighbor swp51 remote-as external
        cumulus@leaf01:~$ net add bgp network 10.0.0.11/32
    
    leaf03:
    
        cumulus@leaf03:~$ net add bgp autonomous-system 65013
        cumulus@leaf03:~$ net add bgp neighbor swp51 remote-as external
        cumulus@leaf03:~$ net add bgp network 10.0.0.13/32
    
    spine01:
    
        cumulus@spine01:~$ net add bgp autonomous-system 65020
        cumulus@spine01:~$ net add bgp neighbor swp1 remote-as external
        cumulus@spine01:~$ net add bgp neighbor swp3 remote-as external

3.  Review and commit your changes:
    
        cumulus@leaf01:~$ net pending
        cumulus@leaf01:~$ net commit
    
        cumulus@leaf03:~$ net pending
        cumulus@leaf03:~$ net commit
    
        cumulus@spine01:~$ net pending
        cumulus@spine01:~$ net commit

4.  Verify the loopback addresses are advertised and learned by all
    VTEPs (look for the line that starts with B\>\*).
    
    leaf01:
    
        cumulus@leaf01:~$ net show route
         
        show ip route
        =============
        Codes: K - kernel route, C - connected, S - static, R - RIP,
               O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
               T - Table, v - VNC, V - VNC-Direct, A - Babel,
               > - selected route, * - FIB route
        C>* 10.0.0.11/32 is directly connected, lo
        B>* 10.0.0.13/32 [20/0] via fe80::eef4:bbff:fefc:bf36, swp51, 00:10:57
        C * 10.100.0.0/24 is directly connected, vlan100-v0
        C>* 10.100.0.0/24 is directly connected, vlan100
        C * 10.200.0.0/24 is directly connected, vlan200-v0
        C>* 10.200.0.0/24 is directly connected, vlan200
    
    leaf03:
    
        cumulus@leaf03:~$ net show route
         
        show ip route
        =============
        Codes: K - kernel route, C - connected, S - static, R - RIP,
               O - OSPF, I - IS-IS, B - BGP, P - PIM, E - EIGRP, N - NHRP,
               T - Table, v - VNC, V - VNC-Direct, A - Babel,
               > - selected route, * - FIB route
        B>* 10.0.0.11/32 [20/0] via fe80::eef4:bbff:fefc:bf3e, swp51, 00:00:12
        C>* 10.0.0.13/32 is directly connected, lo
        C * 10.100.0.0/24 is directly connected, vlan100-v0
        C>* 10.100.0.0/24 is directly connected, vlan100
        C * 10.200.0.0/24 is directly connected, vlan200-v0
        C>* 10.200.0.0/24 is directly connected, vlan200

### <span>Configuring the Server-facing Downlinks</span>

Create routed VLANs for the servers. All Virtual IP addreses (ie. VRR)
are the same since this example configuration uses anycast gateways. See
the diagram above for connectivity.

leaf01:

    cumulus@leaf01:~$ net add vlan 100 ip address-virtual 00:00:00:00:00:1a 10.100.0.1/24
    cumulus@leaf01:~$ net add vlan 100 ip address 10.100.0.2/24
    cumulus@leaf01:~$ net add vlan 200 ip address-virtual 00:00:00:00:00:1b 10.200.0.1/24
    cumulus@leaf01:~$ net add vlan 200 ip address 10.200.0.2/24
    cumulus@leaf01:~$ net add bridge bridge ports swp1
    cumulus@leaf01:~$ net add interface swp1 bridge access 100
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

leaf03:

    cumulus@leaf03:~$ net add vlan 100 ip address-virtual 00:00:00:00:00:1a 10.100.0.1/24
    cumulus@leaf03:~$ net add vlan 100 ip address 10.100.0.4/24
    cumulus@leaf03:~$ net add vlan 200 ip address-virtual 00:00:00:00:00:1b 10.200.0.1/24
    cumulus@leaf03:~$ net add vlan 200 ip address 10.200.0.4/24
    cumulus@leaf03:~$ net add bridge bridge ports swp1
    cumulus@leaf03:~$ net add interface swp1 bridge access 200
    cumulus@leaf03:~$ net pending
    cumulus@leaf03:~$ net commit

{{%notice note%}}

The real IP addresses assigned to each SVI must be unique per VTEP. The
virtual address can be reused as the anycast gateway.

{{%/notice%}}

### <span>Configuring BGP EVPN</span>

1.  Configure the VTEPs to advertise layer 2 MAC address information via
    EVPN.
    
    leaf01:
    
        cumulus@leaf01:~$ net add bgp l2vpn evpn neighbor swp51 activate
        cumulus@leaf01:~$ net add bgp l2vpn evpn advertise-all-vni
        cumulus@leaf01:~$ net pending
        cumulus@leaf01:~$ net commit
    
    leaf03:
    
        cumulus@leaf03:~$ net add bgp l2vpn evpn neighbor swp51 activate
        cumulus@leaf03:~$ net add bgp l2vpn evpn advertise-all-vni
        cumulus@leaf03:~$ net pending
        cumulus@leaf03:~$ net commit
    
    spine01:
    
        cumulus@leaf03:~$ net add bgp l2vpn evpn neighbor swp1 activate
        cumulus@leaf03:~$ net add bgp l2vpn evpn neighbor swp3 activate
        cumulus@leaf03:~$ net pending
        cumulus@leaf03:~$ net commit

2.  Verify EVPN is peering.
    
    leaf01:
    
        cumulus@leaf01:~$ net show bgp l2vpn evpn route
         
        BGP table version is 0, local router ID is 10.200.0.2
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
        Origin codes: i - IGP, e - EGP, ? - incomplete
        EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
        EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
         
           Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 10.0.0.13:1
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                              0 65020 65013 i
        Route Distinguisher: 10.0.0.13:2
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]
                            10.0.0.13                              0 65020 65013 i
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                              0 65020 65013 i
        Route Distinguisher: 10.200.0.2:1
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:98:94]
                            10.0.0.11                          32768 i
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                          32768 i
        Route Distinguisher: 10.200.0.2:2
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                          32768 i
         
        Displayed 6 prefixes (6 paths)
    
    leaf03:
    
        cumulus@leaf03:~$ net show bgp l2vpn evpn route
         
        BGP table version is 0, local router ID is 10.0.0.13
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
        Origin codes: i - IGP, e - EGP, ? - incomplete
        EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
        EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
         
           Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 10.0.0.13:1
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                          32768 i
        Route Distinguisher: 10.0.0.13:2
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]
                            10.0.0.13                          32768 i
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                          32768 i
        Route Distinguisher: 10.200.0.2:1
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:98:94]
                            10.0.0.11                              0 65020 65011 i
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                              0 65020 65011 i
        Route Distinguisher: 10.200.0.2:2
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                              0 65020 65011 i
         
        Displayed 6 prefixes (6 paths)

### <span>Configuring the VXLANs</span>

1.  Configure the VNIs on each VTEP.
    
    leaf01:
    
        cumulus@leaf01:~$ net add vxlan VNI100 vxlan id 10100
        cumulus@leaf01:~$ net add vxlan VNI100 bridge access 100
        cumulus@leaf01:~$ net add vxlan VNI100 vxlan local-tunnelip 10.0.0.11
        cumulus@leaf01:~$ net add vxlan VNI200 vxlan id 10200
        cumulus@leaf01:~$ net add vxlan VNI200 bridge access 200
        cumulus@leaf01:~$ net add vxlan VNI200 vxlan local-tunnelip 10.0.0.11
        cumulus@leaf01:~$ net add bridge bridge ports VNI100,VNI200
    
    leaf03:
    
        cumulus@leaf03:~$ net add vxlan VNI100 vxlan id 10100
        cumulus@leaf03:~$ net add vxlan VNI100 bridge access 100
        cumulus@leaf03:~$ net add vxlan VNI100 vxlan local-tunnelip 10.0.0.13
        cumulus@leaf03:~$ net add vxlan VNI200 vxlan id 10200
        cumulus@leaf03:~$ net add vxlan VNI200 bridge access 200
        cumulus@leaf03:~$ net add vxlan VNI200 vxlan local-tunnelip 10.0.0.13
        cumulus@leaf03:~$ net add bridge bridge ports VNI100,VNI200

2.  Disable bridge learning and enable ARP suppression for VXLAN
    routing, then review and commit your changes.
    
    leaf01:
    
        cumulus@leaf01:~$ net add vxlan VNI100 bridge learning off
        cumulus@leaf01:~$ net add vxlan VNI100 bridge arp-nd-suppress on
        cumulus@leaf01:~$ net add vxlan VNI200 bridge learning off
        cumulus@leaf01:~$ net add vxlan VNI200 bridge arp-nd-suppress on
        cumulus@leaf01:~$ net pending
        cumulus@leaf01:~$ net commit
    
    leaf03:
    
        cumulus@leaf03:~$ net add vxlan VNI100 bridge learning off
        cumulus@leaf03:~$ net add vxlan VNI100 bridge arp-nd-suppress on
        cumulus@leaf03:~$ net add vxlan VNI200 bridge learning off
        cumulus@leaf03:~$ net add vxlan VNI200 bridge arp-nd-suppress on
        cumulus@leaf03:~$ net pending
        cumulus@leaf03:~$ net commit

3.  Verify the VXLAN entries are being learned in EVPN.
    
    leaf01:
    
        cumulus@leaf01:~$ net show bgp l2vpn evpn route
         
        BGP table version is 0, local router ID is 10.200.0.2
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
        Origin codes: i - IGP, e - EGP, ? - incomplete
        EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
        EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
         
           Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 10.0.0.13:1
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                              0 65020 65013 i
        Route Distinguisher: 10.0.0.13:2
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]
                            10.0.0.13                              0 65020 65013 i
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]:[32]:[10.200.0.20]
                            10.0.0.13                              0 65020 65013 i
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]:[128]:[fe80::92e2:baff:fe7e:96d8]
                            10.0.0.13                              0 65020 65013 i
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                              0 65020 65013 i
        Route Distinguisher: 10.200.0.2:1
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:98:94]
                            10.0.0.11                          32768 i
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:98:94]:[32]:[10.100.0.10]
                            10.0.0.11                          32768 i
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                          32768 i
        Route Distinguisher: 10.200.0.2:2
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                          32768 i
         
        Displayed 9 prefixes (9 paths)
    
    leaf03:
    
        cumulus@leaf03:~$ net show bgp l2vpn evpn route
         
        BGP table version is 0, local router ID is 10.0.0.13
        Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
        Origin codes: i - IGP, e - EGP, ? - incomplete
        EVPN type-2 prefix: [2]:[ESI]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
        EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
         
           Network          Next Hop            Metric LocPrf Weight Path
        Route Distinguisher: 10.0.0.13:1
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                          32768 i
        Route Distinguisher: 10.0.0.13:2
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]
                            10.0.0.13                          32768 i
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]:[32]:[10.200.0.20]
                            10.0.0.13                          32768 i
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:96:d8]:[128]:[fe80::92e2:baff:fe7e:96d8]
                            10.0.0.13                          32768 i
        *> [3]:[0]:[32]:[10.0.0.13]
                            10.0.0.13                          32768 i
        Route Distinguisher: 10.200.0.2:1
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:98:94]
                            10.0.0.11                              0 65020 65011 i
        *> [2]:[0]:[0]:[48]:[90:e2:ba:7e:98:94]:[32]:[10.100.0.10]
                            10.0.0.11                              0 65020 65011 i
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                              0 65020 65011 i
        Route Distinguisher: 10.200.0.2:2
        *> [3]:[0]:[32]:[10.0.0.11]
                            10.0.0.11                              0 65020 65011 i
         
        Displayed 9 prefixes (9 paths)

4.  Verify the VXLAN entries are programmed into the bridge table.
    
    leaf01:
    
        cumulus@leaf01:~$ bridge fdb show
        90:e2:ba:7e:98:94 dev swp1 vlan 100 master bridge
        34:17:eb:f6:36:c5 dev swp1 master bridge permanent
        4e:40:85:36:30:de dev VNI100 master bridge permanent
        4e:40:85:36:30:de dev VNI100 vlan 100 master bridge permanent
        00:00:00:00:00:00 dev VNI100 dst 10.0.0.13 self permanent
        b6:3d:a5:f2:2b:16 dev VNI200 master bridge permanent
        90:e2:ba:7e:96:d8 dev VNI200 vlan 200 offload master bridge
        00:00:00:00:00:00 dev VNI200 dst 10.0.0.13 self permanent
        90:e2:ba:7e:96:d8 dev VNI200 dst 10.0.0.13 self offload
        00:00:00:00:00:1b dev bridge self permanent
        00:00:00:00:00:1a dev bridge self permanent
        4e:40:85:36:30:de dev bridge self permanent
        00:00:00:00:00:1b dev bridge vlan 200 master bridge permanent
        34:17:eb:f6:36:c5 dev bridge vlan 200 master bridge permanent
        34:17:eb:f6:36:c5 dev bridge vlan 100 master bridge permanent
        00:00:00:00:00:1a dev bridge vlan 100 master bridge permanent
        00:00:00:00:00:1b dev vlan200 self permanent
        00:00:00:00:00:1a dev vlan100 self permanent
    
    leaf03:
    
        cumulus@leaf03:~$  bridge fdb show
        90:e2:ba:7e:96:d8 dev swp1 vlan 200 master bridge
        2c:60:0c:72:eb:70 dev swp1 master bridge permanent
        9e:f1:f5:bd:16:cc dev VNI100 master bridge permanent
        90:e2:ba:7e:98:94 dev VNI100 vlan 100 offload master bridge
        9e:f1:f5:bd:16:cc dev VNI100 vlan 100 master bridge permanent
        00:00:00:00:00:00 dev VNI100 dst 10.0.0.11 self permanent
        90:e2:ba:7e:98:94 dev VNI100 dst 10.0.0.11 self offload
        e6:1a:7b:f4:4f:7b dev VNI200 master bridge permanent
        00:00:00:00:00:00 dev VNI200 dst 10.0.0.11 self permanent
        00:00:00:00:00:1b dev bridge self permanent
        00:00:00:00:00:1a dev bridge self permanent
        9e:f1:f5:bd:16:cc dev bridge self permanent
        2c:60:0c:72:eb:70 dev bridge vlan 200 master bridge permanent
        00:00:00:00:00:1b dev bridge vlan 200 master bridge permanent
        2c:60:0c:72:eb:70 dev bridge vlan 100 master bridge permanent
        00:00:00:00:00:1a dev bridge vlan 100 master bridge permanent
        00:00:00:00:00:1b dev vlan200 self permanent
        00:00:00:00:00:1a dev vlan100 self permanent

### <span>Resulting Configurations</span>

Following are the resulting interfaces and routing configurations for
the three nodes you configured above: leaf01, leaf03 and spine01.

#### <span>leaf01</span>

leaf01 /etc/network/interfaces

    cumulus@leaf01:mgmt-vrf:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    source /etc/network/interfaces.d/*.intf
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
        address 10.0.0.11/32
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
        vrf mgmt
     
    iface eth1 inet dhcp
     
    auto swp1
    iface swp1
        bridge-access 100
        mtu 9216
     
    auto swp51
    iface swp51
        mtu 9216
     
    auto VNI100
    iface VNI100
        bridge-access 100
        bridge-arp-nd-suppress on
        bridge-learning off
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
        mtu 9152
        vxlan-id 10100
        vxlan-local-tunnelip 10.0.0.11
     
    auto VNI200
    iface VNI200
        bridge-access 200
        bridge-arp-nd-suppress on
        bridge-learning off
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
        mtu 9152
        vxlan-id 10200
        vxlan-local-tunnelip 10.0.0.11
     
    auto bridge
    iface bridge
        bridge-ports VNI100 VNI200 swp1
        bridge-vids 100 200
        bridge-vlan-aware yes
     
    auto mgmt
    iface mgmt
        address 127.0.0.1/8
        vrf-table auto
     
    auto vlan100
    iface vlan100
        address 10.100.0.2/24
        address-virtual 00:00:00:00:00:1a 10.100.0.1/24
        vlan-id 100
        vlan-raw-device bridge
     
    auto vlan200
    iface vlan200
        address 10.200.0.2/24
        address-virtual 00:00:00:00:00:1b 10.200.0.1/24
        vlan-id 200
        vlan-raw-device bridge

leaf01 /etc/frr/frr.conf

    cumulus@leaf01:mgmt-vrf:~$ sudo cat /etc/frr/frr.conf
    frr version 3.1+cl3u1
    frr defaults datacenter
    username cumulus nopassword
    !
    service integrated-vtysh-config
    !
    log syslog informational
    !
    interface swp51
     ipv6 nd ra-interval 10
     no ipv6 nd suppress-ra
    !
    router bgp 65011
     bgp router-id 10.0.0.11
     neighbor swp51 interface remote-as external
     !
     address-family ipv4 unicast
      network 10.0.0.11/32
     exit-address-family
     !
     address-family l2vpn evpn
      neighbor swp51 activate
      advertise-all-vni
     exit-address-family
    !
    line vty
    !

#### <span>leaf03</span>

leaf03 /etc/network/interfaces

    cumulus@leaf03:mgmt-vrf:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    source /etc/network/interfaces.d/*.intf
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
        address 10.0.0.13/32
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
        vrf mgmt
     
    auto swp1
    iface swp1
        bridge-access 200
        mtu 9216
     
    auto swp51
    iface swp51
        mtu 9216
     
    auto VNI100
    iface VNI100
        bridge-access 100
        bridge-arp-nd-suppress on
        bridge-learning off
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
        mtu 9152
        vxlan-id 10100
        vxlan-local-tunnelip 10.0.0.13
     
    auto VNI200
    iface VNI200
        bridge-access 200
        bridge-arp-nd-suppress on
        bridge-learning off
        mstpctl-bpduguard yes
        mstpctl-portbpdufilter yes
        mtu 9152
        vxlan-id 10200
        vxlan-local-tunnelip 10.0.0.13
     
    auto bridge
    iface bridge
        bridge-ports VNI100 VNI200 swp1
        bridge-vids 100 200
        bridge-vlan-aware yes
     
    auto mgmt
    iface mgmt
        address 127.0.0.1/8
        vrf-table auto
     
    auto vlan100
    iface vlan100
        address 10.100.0.4/24
        address-virtual 00:00:00:00:00:1a 10.100.0.1/24
        vlan-id 100
        vlan-raw-device bridge
     
    auto vlan200
    iface vlan200
        address 10.200.0.4/24
        address-virtual 00:00:00:00:00:1b 10.200.0.1/24
        vlan-id 200
        vlan-raw-device bridge

leaf03 /etc/frr/frr.conf

    cumulus@leaf03:mgmt-vrf:~$ sudo cat /etc/frr/frr.conf
    frr version 3.1+cl3u1
    frr defaults datacenter
    username cumulus nopassword
    !
    service integrated-vtysh-config
    !
    log syslog informational
    !
    interface swp51
     ipv6 nd ra-interval 10
     no ipv6 nd suppress-ra
    !
    router bgp 65013
     bgp router-id 10.0.0.13
     neighbor swp51 interface remote-as external
     !
     address-family ipv4 unicast
      network 10.0.0.13/32
     exit-address-family
     !
     address-family l2vpn evpn
      neighbor swp51 activate
      advertise-all-vni
     exit-address-family
    !
    line vty
    !

#### <span>spine01</span>

spine01 /etc/network/interfaces

    cumulus@spine01:mgmt-vrf:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    source /etc/network/interfaces.d/*.intf
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
        address 10.0.0.21/32
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
        vrf mgmt
     
    auto swp1
    iface swp1
        mtu 9216
     
    auto swp2
    iface swp2
     
    auto swp3
    iface swp3
        mtu 9216
     
    auto swp51
    iface swp51
     
    auto swp52
    iface swp52
     
    auto mgmt
    iface mgmt
        address 127.0.0.1/8
        vrf-table auto

spine01 /etc/frr/frr.conf

    cumulus@spine01:mgmt-vrf:~$ sudo cat /etc/frr/frr.conf
    frr version 3.1+cl3u1
    frr defaults datacenter
    username cumulus nopassword
    !
    service integrated-vtysh-config
    !
    log syslog informational
    !
    interface swp1
     ipv6 nd ra-interval 10
     no ipv6 nd suppress-ra
    !
    interface swp3
     ipv6 nd ra-interval 10
     no ipv6 nd suppress-ra
    !
    router bgp 65020
     neighbor swp1 interface remote-as external
     neighbor swp3 interface remote-as external
     !
     address-family l2vpn evpn
      neighbor swp1 activate
      neighbor swp3 activate
     exit-address-family
    !
    line vty
    !

## <span>VXLAN Routing with Active-Active VTEPs</span>

VXLAN routing with active-active VTEPs is configured the same way as
VXLAN with active-active mode VTEPs. Follow the instructions located in
the [VXLAN and EVPN Active-Active
chapter](/display/CL34/Ethernet+Virtual+Private+Network+-+EVPN#EthernetVirtualPrivateNetwork-EVPN-EVPNandVXLANActive-ActiveMode).

## <span>VXLAN with VRFs</span>

VXLAN can be configured with VRF support. In order to do so, just apply
the server downlink SVI configuration on the top of rack switches inside
a VRF. The BGP EVPN address family and `advertise-all-vni` command are
smart enough to apply the correct RD and RT information to each VRF.

Below is an example for leaf01 where VLAN 100 and VLAN 150 are part of
VRF *RED* and can VXLAN route between each other. VLAN 200 is part of
VRF *BLUE* and cannot communicate with any hosts in VRF *RED*:

    cumulus@leaf01:~$ net add vrf RED
    cumulus@leaf01:~$ net add vlan 100 vrf RED
    cumulus@leaf01:~$ net add vlan 100 ip address-virtual 00:00:00:00:00:1a 10.100.0.1/24
    cumulus@leaf01:~$ net add vlan 100 ip address 10.100.0.2/24
    cumulus@leaf01:~$ net add vlan 150 vrf RED
    cumulus@leaf01:~$ net add vlan 150 ip address-virtual 00:00:00:00:00:1c 10.150.0.1/24
    cumulus@leaf01:~$ net add vlan 150 ip address 10.150.0.2/24
    cumulus@leaf01:~$ net add vrf BLUE
    cumulus@leaf01:~$ net add vlan 200 vrf BLUE
    cumulus@leaf01:~$ net add vlan 200 ip address-virtual 00:00:00:00:00:1b 10.200.0.1/24
    cumulus@leaf01:~$ net add vlan 200 ip address 10.200.0.2/24
    cumulus@leaf01:~$ net pending
    cumulus@leaf01:~$ net commit

## <span>Viewing VXLAN Routing Information</span>

You can use the following commands to display VXLAN routing-related
information:

  - ip link show dev \<DEVICE\>

  - ip route

  - ip neighbor

  - bridge fdb show

To get basic information about a VXLAN, use `ip link show`:

    cumulus@switch:~$ ip link show VNI-11000
    68: VNI-11000: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9152 state UP mode DEFAULT group default  
     link/ether 0a:09:cd:9d:f0:c7 brd ff:ff:ff:ff:ff:ff

To view the routing table, use `ip route`:

    cumulus@switch:~$ ip route
    45.0.0.0/26 dev vlan1000 proto kernel  scope link  src 45.0.0.16 
    45.0.0.64/26 dev vlan1001  proto kernel  scope link  src 45.0.0.80

To view the neighbor table, run `ip neighbor`:

    cumulus@switch:~$ ip neighbor 
    45.0.0.70 dev vlan1001 lladdr 00:02:00:00:00:0c STALE
    45.0.0.72 dev vlan1001 lladdr 00:02:00:00:00:10 REACHABLE
    45.0.0.5 dev vlan1000 lladdr 00:02:00:00:00:0a REACHABLE

To view the forwarding database, use `bridge fdb show`:

    cumulus@switch:~$ bridge fdb show
    ca:0b:56:be:a7:74 dev VNI-11000 master bridge permanent
    ba:08:bc:60:b2:15 dev VNI-11001 master bridge permanent
    00:00:5e:00:01:01 dev bridge vlan 1001 master bridge permanent
    00:00:5e:00:01:01 dev bridge vlan 1000 master bridge permanent

## <span>Troubleshooting VXLAN Routing</span>

You can investigate control plane VXLAN routing issues with the
following commands:

  - net show bgp l2vpn evpn route

  - net show bgp l2vpn evpn route vni \<vni\>

  - net show bgp l2vpn evpn vni

  - net show l2vpn evpn mac vni \<vni\>

  - net show l2vpn evpn arp-cache vni \<vni\>
