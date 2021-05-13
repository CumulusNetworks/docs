---
title: Troubleshooting
author: NVIDIA
weight: 590
toc: 4
---
This section provides various commands to help you examine your EVPN configuration and provides troubleshooting tips.

## General Linux Commands

You can use various `iproute2` commands to examine links, VLAN mappings and the bridge MAC forwarding database known to the Linux kernel. You can also use these commands to examine the neighbor cache and the routing table (for the underlay or for a specific tenant VRF). Some of the key commands are:

- `ip [-d] link show`
- `bridge link show`
- `bridge vlan show`
- `bridge [-s] fdb show`
- `ip neighbor show`
- `ip route show [table <vrf-name>]`

A sample output of `ip -d link show type vxlan` is shown below for one VXLAN interface. Relevant parameters are the VNI value, the state, the local IP address for the VXLAN tunnel, the UDP port number (4789) and the bridge of which the interface is part (*bridge* in the example below). The output also shows that MAC learning is disabled (*off*) on the VXLAN interface.

```
cumulus@leaf01:~$ ip -d link show type vxlan
9: vni100: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default 
    link/ether 72:bc:b4:a3:eb:1e brd ff:ff:ff:ff:ff:ff promiscuity 1
    vxlan id 10100 local 10.0.0.1 srcport 0 0 dstport 4789 nolearning ageing 300
    bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning off flood on port_id 0x8001 port_no 0x1 designated_port 32769 designated_cost 0 designated_bridge 8000.0:1:0:0:11:0 designated_root 8000.0:1:0:0:11:0 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on neigh_suppress on group_fwd_mask 0x0 group_fwd_mask_str 0x0 group_fwd_maskhi 0x0 group_fwd_maskhi_str 0x0 addrgenmode eui64
...
```

The following example output for the `bridge fdb show` command shows:

- swp3 and swp4 are access ports with VLAN ID 100. This is mapped to VXLAN interface vni100.
- 00:02:00:00:00:01 is a local host MAC learned on swp3.
- The remote VTEPs that participate in VLAN ID 100 are 10.0.0.3, 10.0.0.4, and 10.0.0.2 (the FDB entries have a MAC address of 00:00:00:00:00:00). These entries are used for BUM traffic replication.
- 00:02:00:00:00:06 is a remote host MAC reachable over the VXLAN tunnel to 10.0.0.2.

```
cumulus@leaf01:~$ bridge fdb show
00:02:00:00:00:13 dev swp3 master bridge permanent
00:02:00:00:00:01 dev swp3 vlan 100 master bridge
00:02:00:00:00:02 dev swp4 vlan 100 master bridge
72:bc:b4:a3:eb:1e dev vni100 master bridge permanent
00:02:00:00:00:06 dev vni100 vlan 100 extern_learn master bridge
00:00:00:00:00:00 dev vni100 dst 10.0.0.3 self permanent
00:00:00:00:00:00 dev vni100 dst 10.0.0.4 self permanent
00:00:00:00:00:00 dev vni100 dst 10.0.0.2 self permanent
00:02:00:00:00:06 dev vni100 dst 10.0.0.2 self extern_learn
...
```

The following example output for the `ip neigh show` command shows:

- 172.16.120.11 is a locally-attached host on VLAN 100. It is shown twice because of the configuration of the anycast IP/MAC on the switch.
- 172.16.120.42 is a remote host on VLAN 100 and 172.16.130.23 is a remote host on VLAN 200. You can examine the MAC address for these hosts with the `bridge fdb show` command to determine the VTEPs behind which these hosts are located.

```
cumulus@leaf01:~$ ip neigh show
172.16.120.11 dev vlan100-v0 lladdr 00:02:00:00:00:01 STALE
172.16.120.42 dev vlan100 lladdr 00:02:00:00:00:0e extern_learn REACHABLE
172.16.130.23 dev vlan200 lladdr 00:02:00:00:00:07 extern_learn REACHABLE
172.16.120.11 dev vlan100 lladdr 00:02:00:00:00:01 REACHABLE
...
```

## General BGP Commands

If you use BGP for the underlay routing, run the NCLU `net show bgp summary` command or the vtysh `show bgp summary` command to view a summary of the layer 3 fabric connectivity:

```
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
```

Run the NCLU `net show route` command or the vtysh `show route` command to examine the underlay routing and determine how remote VTEPs are reached. The following example shows output from a leaf switch:

```
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
```

Run the NCLU `net show bridge macs` command to view the MAC forwarding database on the switch:

```
cumulus@leaf01:~$ net show bridge macs
VLAN      Master    Interface    MAC                TunnelDest    State      Flags          LastSeen
--------  --------  -----------  -----------------  ------------  ---------  -------------  ---------------
100       br0       br0          00:00:5e:00:01:01                permanent                 1 day, 03:38:43
100       br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:43
100       br0       swp3         00:02:00:00:00:01                                          00:00:26
100       br0       swp4         00:02:00:00:00:02                                          00:00:16
100       br0       vni100       00:02:00:00:00:0a                           extern_learn   1 day, 03:38:20
100       br0       vni100       00:02:00:00:00:0d                           extern_learn   1 day, 03:38:20
100       br0       vni100       00:02:00:00:00:0e                           extern_learn   1 day, 03:38:20
100       br0       vni100       00:02:00:00:00:05                           extern_learn   1 day, 03:38:19
100       br0       vni100       00:02:00:00:00:06                           extern_learn   1 day, 03:38:19
100       br0       vni100       00:02:00:00:00:09                           extern_learn   1 day, 03:38:20
200       br0       br0          00:00:5e:00:01:01                permanent                 1 day, 03:38:42
200       br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:43
200       br0       swp5         00:02:00:00:00:03                                          00:00:26
 200       br0       swp6         00:02:00:00:00:04                                         00:00:26
200       br0       vni200       00:02:00:00:00:0b                           extern_learn   1 day, 03:38:20
200       br0       vni200       00:02:00:00:00:0c                           extern_learn   1 day, 03:38:20
200       br0       vni200       00:02:00:00:00:0f                           extern_learn   1 day, 03:38:20
200       br0       vni200       00:02:00:00:00:07                           extern_learn   1 day, 03:38:19
200       br0       vni200       00:02:00:00:00:08                           extern_learn   1 day, 03:38:19
200       br0       vni200       00:02:00:00:00:10                           extern_learn   1 day, 03:38:20
4001      br0       br0          00:01:00:00:11:00                permanent                 1 day, 03:38:42
4001      br0       vni4001      00:01:00:00:12:00                           extern_learn   1 day, 03:38:19
4001      br0       vni4001      00:01:00:00:13:00                           extern_learn   1 day, 03:38:20
4001      br0       vni4001      00:01:00:00:14:00                           extern_learn   1 day, 03:38:20
untagged            br0          00:00:5e:00:01:01                permanent  self           never
untagged            vlan100      00:00:5e:00:01:01                permanent  self           never
untagged            vlan200      00:00:5e:00:01:01                permanent  self           never
...
```

## Show EVPN address-family Peers

Run the NCLU `net show bgp l2vpn evpn summary` command or the vtysh `show bgp l2vpn evpn summary` command to see the BGP peers participating in the layer 2 VPN/EVPN address-family and their states. The following example output from a leaf switch shows eBGP peering with two spine switches to exchange EVPN routes; both peering sessions are in the *established* state.

```
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
```

## Show EVPN VNIs

Run the NCLU `net show bgp l2vpn evpn vni` command or the vtysh `show bgp l2vpn evpn vni` command to display the configured VNIs on a network device participating in BGP EVPN. This command is only relevant on a VTEP. If you have configured symmetric routing, this command displays the special layer 3 VNIs that are configured per tenant VRF.

The following example from a leaf switch shows two layer 2 VNIs (10100 and 10200) as well as a layer 3 VNI (104001). The command output also shows the number of associated MAC and neighbor entries for layer 2 VNIs, and the VXLAN interface and VRF corresponding to each VNI.

``` 
cumulus@leaf01:~$ net show evpn vni
VNI        Type  VxLAN IF            # MACs   # ARPs   # Remote VTEPs  Tenant VRF
10200      L2    vni200              8        12       3               vrf1

10100      L2    vni100              8        12       3               vrf1

104001     L3    vni4001             3        3        n/a             vrf1

```

Run the NCLU `net show evpn vni <vni>` command or the vtysh `show evpn vni <vni>` command to examine EVPN information for a specific VNI in detail. The following example output shows details for the layer 2 VNI 10100 as well as for the layer 3 VNI 104001. For the layer 2 VNI, the remote VTEPs that contain that VNI are shown. For the layer 3 VNI, the router MAC and associated layer 2 VNIs are shown. The state of the layer 3 VNI depends on the state of its associated VRF as well as the states of its underlying VXLAN interface and SVI.

```
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
```

## Examine Local and Remote MAC Addresses for a VNI

Run the NCLU `net show evpn mac vni <vni>` command or the vtysh `show evpn mac vni <vni>` command to examine all local and remote MAC addresses for a VNI. This command is only relevant for a layer 2 VNI:

```
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
```

Run the NCLU `net show evpn mac vni all` command or the vtysh `show evpn mac vni all` command to examine MAC addresses for all VNIs.

You can examine the details for a specific MAC addresse or query all remote MAC addresses behind a specific VTEP:

```
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
```

## Examine Local and Remote Neighbors for a VNI

Run the NCLU `net show evpn arp-cache vni <vni>` command or the vtysh `show evpn arp-cache vni <vni>` command to examine all local and remote neighbors (ARP entries) for a VNI. This command is only relevant for a layer 2 VNI and the output shows both IPv4 and IPv6 neighbor entries:

```
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
```

Run the NCLU `net show evpn arp-cache vni all` command or the vtysh `show evpn arp-cache vni all` command to examine neighbor entries for all VNIs.

## Examine Remote Router MACs

For symmetric routing, run the NCLU `net show evpn rmac vni <vni>` command or the vtysh `show evpn rmac vni <vni>` command to examine the router MACs corresponding to all remote VTEPs. This command is only relevant for a layer 3 VNI:

```
cumulus@leaf01:~$ net show evpn rmac vni 104001
Number of Remote RMACs known for this VNI: 3
MAC               Remote VTEP          
00:01:00:00:14:00 10.0.0.4            
00:01:00:00:12:00 10.0.0.2            
00:01:00:00:13:00 10.0.0.3            
cumulus@leaf01:~$
```

Run the NCLU `net show evpn rmac vni all` command or the vtysh `show evpn rmac vni all` command to examine router MACs for all layer 3 VNIs.

## Examine Gateway Next Hops

For symmetric routing, you can run the NCLU `net show evpn next-hops vni <vni>` command or the vtysh `show evpn next-hops vni <vni>` command to examine the gateway next hops. This command is only relevant for a layer 3 VNI. In general, the gateway next hop IP addresses correspond to the remote VTEP IP addresses. Remote host and prefix routes are installed
 sing these next hops:

```
cumulus@leaf01:~$ net show evpn next-hops vni 104001
Number of NH Neighbors known for this VNI: 3
IP              RMAC             
10.0.0.3       00:01:00:00:13:00
10.0.0.4       00:01:00:00:14:00
10.0.0.2       00:01:00:00:12:00
cumulus@leaf01:~$
```

Run the NCLU `net show evpn next-hops vni` `all` command or the vtysh `show evpn next-hops vni` `all` command to examine gateway next hops for all layer 3 VNIs.

You can query a specific next hop; the output displays the remote host and prefix routes through this next hop:

```
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
```

## Show the VRF Routing Table in FRR

Run the `net show route vrf <vrf-name>` command to examine the VRF routing table. In the context of EVPN, this command is relevant for symmetric routing to verify that remote host and prefix routes are installed in the VRF routing table and point to the appropriate gateway next hop.

```
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
```

In the output above, the next hops for these routes are specified by EVPN to be *onlink*, or reachable over the specified SVI. This is necessary because this interface is not required to have an IP address. Even if the interface is configured with an IP address, the next hop is not on the same subnet as it is usually the IP address of the remote VTEP (part of the underlay IP network).

## Show the Global BGP EVPN Routing Table

Run the NCLU `net show bgp l2vpn evpn route` command or the vtysh `show bgp l2vpn evpn route` command to display all EVPN routes, both local and remote. The routes displayed here are based on RD as they are across VNIs and VRFs:

```
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
```

You can filter the routing table based on EVPN route type. The available options are shown below:

```
cumulus@leaf01:~$ net show bgp l2vpn evpn route type 
    macip      :  MAC-IP (Type-2) route
    multicast  :  Multicast
    prefix     :  An IPv4 or IPv6 prefix
cumulus@leaf01:~$
```

## Show a Specific EVPN Route

To drill down on a specific route for more information, run the NCLU `net show bgp l2vpn evpn route rd <rd-value>` command or the vtysh `show bgp l2vpn evpn route rd <rd-value>` command. This command displays all EVPN routes with that RD and with the path attribute details for each path. Additional filtering is possible based on route type or by specifying the MAC and/or IP address. The following example shows a specific MAC/IP route. The output shows that this remote host is behind VTEP 10.0.0.4 and is reachable through two paths; one through either spine switch. This example is from a symmetric routing configuration, so the route shows both the layer 2 VNI (10200) and the layer 3 VNI (104001), as well as the EVPN route target attributes corresponding to each and the associated router MAC address.

```
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
```

{{%notice note%}}

- Only global VNIs are supported. Even though VNI values are exchanged in the type-2 and type-5 routes, the received values are not used when installing the routes into the forwarding plane; the local configuration is used. You must ensure that the VLAN to VNI mappings and the layer 3 VNI assignment for a tenant VRF are uniform throughout the network.
- If the remote host is dual attached, the next hop for the EVPN route is the anycast IP address of the remote {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} pair, when MLAG is active.

{{%/notice%}}

The following example shows a prefix (type-5) route. Such a route has only the layer 3 VNI and the route target corresponding to this VNI. This route is learned through two paths, one through each spine switch.

```
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
```

## Show the per-VNI EVPN Routing Table

Received EVPN routes are maintained in the global EVPN routing table (described above), even if there are no appropriate local VNIs to **import** them into. For example, a spine switch maintains the global EVPN routing table even though there are no VNIs present on it. When local VNIs are present, received EVPN routes are imported into the per-VNI routing tables based on the route target attributes. You can examine the per-VNI routing table with the `net show bgp l2vpn evpn route vni <vni>` command:

```
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
```

To display the VNI routing table for all VNIs, run the `net show bgp l2vpn evpn route vni all` command.

## Show the per-VRF BGP Routing Table

For symmetric routing, received type-2 and type-5 routes are imported into the VRF routing table (against the corresponding address-family: IPv4 unicast or IPv6 unicast) based on a match on the route target attributes. Run the NCLU `net show bgp vrf <vrf-name> ipv4 unicast` command or the `net show bgp vrf <vrf-name> ipv6 unicast` command to examine the BGP VRF routing table. The equivalent vtysh commands are `show bgp vrf <vrf-name> ipv4 unicast` and `show bgp vrf <vrf-name> ipv6 unicast`.

```
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
```

## Support for EVPN Neighbor Discovery (ND) Extended Community

In an EVPN VXLAN deployment with ARP and ND suppression where the VTEPs are only configured for layer 2, EVPN needs to carry additional information for the attached devices so proxy ND can provide the correct information to attached hosts. Without this information, hosts might not be able to configure their default routers or might lose their existing default router information. Cumulus Linux supports the EVPN Neighbor Discovery (ND) Extended Community with a type field value of 0x06, a sub-type field value of 0x08 (ND Extended Community), and a router flag; this enables the switch to determine if a particular IPv6-MAC pair belongs to a host or a router.

The **router flag** (R-bit) is used in:

- A centralized VXLAN routing configuration with a gateway router.
- A layer 2 switch deployment with ARP/ND suppression.

When the MAC/IP (type-2) route contains the IPv6-MAC pair and the R-bit is set, the route belongs to a router. If the R-bit is set to zero, the route belongs to a host. If the router is in a local LAN segment, the switch implementing the proxy ND function learns of this information by snooping on neighbor advertisement messages for the associated IPv6 address. This information is then exchanged with other EVPN peers by using the ND extended community in BGP updates.

To show the EVPN arp-cache that gets populated by the neighbor table and see if the IPv6-MAC entry belongs to a router, run either the NCLU `net show evpn arp-cache vni <vni> ip <address>` command or the vtysh `show evpn arp-cache vni <vni> ip <address>` command. For example:

```
cumulus@switch:mgmt-vrf:~$ net show evpn arp-cache vni 101 ip fe80::202:ff:fe00:11
IP: fe80::202:ff:fe00:11
  Type: remote
  State: active
  MAC: 00:02:00:00:00:11
  Remote VTEP: 10.0.0.134
  Flags: Router
  Local Seq: 0 Remote Seq: 0
```

To show the BGP routing table entry for the IPv6-MAC EVPN route with the ND extended community, run the NCLU `net show bgp l2vpn evpn route vni <vni> mac <mac-address> ip <ip-address>` command or the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac-address> ip <ip-address>` command. For example:

```
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
```

## Examine MAC Moves

The first time a MAC moves from behind one VTEP to behind another, BGP associates a MAC Mobilit (MM) extended community attribute of sequence number 1, with the type-2 route for that MAC. From there, each time this MAC moves to a new VTEP, the MM sequence number increments by 1. You can examine the MM sequence number associated with a MAC's type-2 route with the NCLU `net show bgp l2vpn evpn route vni <vni> mac <mac>` command or the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac>` command. The example output below shows the type-2 route for a MAC that has moved three times:

```
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
```

## Examine Static MAC Addresses

You can identify static or *sticky* MACs in EVPN by the presence of `MM:0, sticky MAC` in the Extended Community line of the output from the NCLU `net show bgp l2vpn evpn route vni <vni> mac <mac>` command or the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac>` command.

```
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
```

## Enable FRR Debug Logs

To troubleshoot EVPN, enable FRR debug logs. The relevant debug options are:

| <div style="width:250px">Option | Description |
|------- | ----------- |
|`debug zebra vxlan` | Traces VNI addition and deletion (local and remote) as well as MAC and neighbor addition and deletion (local and remote). |
| `debug zebra kernel` | Traces actual netlink messages exchanged with the kernel, which includes everything, not just EVPN.|
|`debug bgp updates` | Traces BGP update exchanges, including all  updates. Output is extended to show EVPN specific information. |
| `debug bgp zebra` | Traces interactions between BGP and zebra for EVPN (and other) routes. |

## ICMP echo Replies and the ping Command

When you run the `ping -I ` command and specify an interface, you don't get an ICMP echo reply. However, when you run the `ping` command without the `-I` option, everything works as expected.

`ping -I` command example:

```
cumulus@switch:default:~:# ping -I swp2 10.0.10.1
PING 10.0.10.1 (10.0.10.1) from 10.0.0.2 swp1.5: 56(84) bytes of data.
```

`ping` command example:

```
cumulus@switch:default:~:# ping 10.0.10.1
PING 10.0.10.1 (10.0.10.1) 56(84) bytes of data.
64 bytes from 10.0.10.1: icmp_req=1 ttl=63 time=4.00 ms
64 bytes from 10.0.10.1: icmp_req=2 ttl=63 time=0.000 ms
64 bytes from 10.0.10.1: icmp_req=3 ttl=63 time=0.000 ms
64 bytes from 10.0.10.1: icmp_req=4 ttl=63 time=0.000 ms
^C
--- 10.0.10.1 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3004ms
rtt min/avg/max/mdev = 0.000/1.000/4.001/1.732 ms
```

This is expected behavior with Cumulus Linux; when you send an ICMP echo request to an IP address that is not in the same subnet using the `ping -I` command, Cumulus Linux creates a failed ARP entry for the destination IP address.

For more information, refer to [this article]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/ICMP-Ping-Doesn-t-Work-when-Specifying-I-Option">}}).
