---
title: Troubleshooting EVPN
author: NVIDIA
weight: 590
toc: 4
---
This section provides various commands to help you examine your EVPN configuration and provides troubleshooting tips.

## General Commands

You can use various NVUE or Linux commands to examine interfaces, VLAN mappings and the bridge MAC forwarding database known to the Linux kernel. You can also use these commands to examine the neighbor cache and the routing table (for the underlay or for a specific tenant VRF). Some of the key commands are:

- `ip [-d] link show type vxlan` (Linux)
- `nv show bridge domain <domain> mac-table` (NVUE) or `bridge [-s] fdb show` (Linux)
- `nv show bridge domain <domain> vlan` (NVUE) or `bridge vlan show` (Linux)
- `nv show bridge vlan-vni-map` (NVUE)
- `nv show bridge domain <bridge> vlan-vni-map` (NVUE)
- `nv show interface neighbor` (NVUE) or `ip neighbor show` (Linux)
- `ip route show [table <vrf-id>]` (Linux)

The sample output below shows `ip -d link show type vxlan` command output for one VXLAN interface. Relevant parameters are the VNI value, the state, the local IP address for the VXLAN tunnel, the UDP port number (4789) and the bridge of which the interface is part (*bridge* in the example below). The output also shows that MAC learning is *off* on the VXLAN interface.

```
cumulus@leaf01:~$ ip -d link show type vxlan
14: vni10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9216 qdisc noqueue master bridge state UP mode DEFAULT group default qlen 1000
    link/ether 42:83:73:20:46:ba brd ff:ff:ff:ff:ff:ff promiscuity 1 minmtu 68 maxmtu 65535
    vxlan id 10 local 10.0.1.1 srcport 0 0 dstport 4789 nolearning ttl 64 ageing 300 udpcsum noudp6zerocsumtx noudp6zerocsumrx
    bridge_slave state forwarding priority 8 cost 100 hairpin off guard off root_block off fastleave off learning off flood on port_id 0x8005 port_no 0x5 designated_port 32773 designated_cost 0 designated_bridge 8000.76:ed:2a:8a:67:24 designated_root 8000.76:ed:2a:8a:67:24 hold_timer    0.00 message_age_timer    0.00 forward_delay_timer    0.00 topology_change_ack 0 config_pending 0 proxy_arp off proxy_arp_wifi off mcast_router 1 mcast_fast_leave off mcast_flood on neigh_suppress on group_fwd_mask 0x0 group_fwd_mask_str 0x0 group_fwd_maskhi 0x0 group_fwd_maskhi_str 0x0 vlan_tunnel off isolated off addrgenmode eui64 numtxqueues 1 numrxqueues 1 gso_max_size 65536 gso_max_segs 65535
...
```

The following shows example output for the `nv show bridge domain <domain> mac-table` command:
<!-- vale off -->
```
cumulus@leaf01:mgmt:~$ nv show bridge domain br_default mac-table
entry-id  MAC address        vlan  interface   remote-dst   src-vni  entry-type    last-update  age    
--------  -----------------  ----  ----------  -----------  -------  ------------  -----------  -------
1         48:b0:2d:fd:d3:bf  10    vxlan48                           extern_learn  8:06:02      8:06:02
2         48:b0:2d:4e:1c:fe  20    vxlan48                           extern_learn  8:06:02      8:06:02
3         48:b0:2d:a7:4d:ce  30    vxlan48                           extern_learn  8:06:02      8:06:02
4         48:b0:2d:53:d2:34  20    vxlan48                           extern_learn  8:06:30      8:06:30
5         44:38:39:be:ef:bb  4063  vxlan48                           extern_learn  8:06:30      8:06:30
6         48:b0:2d:2d:5f:b3  30    vxlan48                           extern_learn  8:06:32      8:06:32
7         44:38:39:be:ef:bb  4006  vxlan48                           extern_learn  8:06:32      8:06:32
8         48:b0:2d:93:a1:3e  10    vxlan48                           extern_learn  8:06:35      8:06:35
9         44:38:39:22:01:74  4006  vxlan48                           extern_learn  8:06:38      8:06:38
10        44:38:39:22:01:74  4063  vxlan48                           extern_learn  8:06:38      8:06:38
11        44:38:39:22:01:7c  4006  vxlan48                           extern_learn  8:06:39      8:06:39
12        44:38:39:22:01:7c  4063  vxlan48                           extern_learn  8:06:39      8:06:39
13        44:38:39:22:01:8a  30    vxlan48                           extern_learn  8:06:42      8:06:42
14        44:38:39:22:01:8a  20    vxlan48                           extern_learn  8:06:42      8:06:42
15        44:38:39:22:01:8a  10    vxlan48                           extern_learn  8:06:42      8:04:05
16        44:38:39:22:01:84  10    vxlan48                           extern_learn  8:06:43      8:06:43
17        44:38:39:22:01:84  30    vxlan48                           extern_learn  8:06:43      8:06:15
18        44:38:39:22:01:84  20    vxlan48                           extern_learn  8:06:43      8:06:43
19        44:38:39:22:01:8a  4006  vxlan48                           extern_learn  8:06:43      8:06:43
20        44:38:39:22:01:8a  4063  vxlan48                           extern_learn  8:06:43      8:06:43
21        44:38:39:22:01:84  4063  vxlan48                           extern_learn  8:06:43      8:06:43
22        44:38:39:22:01:84  4006  vxlan48                           extern_learn  8:06:43      8:06:43
23        44:38:39:22:01:78  4063  vxlan48                           extern_learn  8:06:43      8:06:43
24        44:38:39:22:01:78  4006  vxlan48                           extern_learn  8:06:43      8:06:43
25        02:91:8d:cf:03:b2        vxlan48                           permanent     8:06:56      8:06:56
26        00:00:00:00:00:00        vxlan48     10.0.1.34    30       permanent     8:06:43      0:28:22
27        44:38:39:22:01:78        vxlan48     10.10.10.2   4001     extern_learn  8:06:43      8:06:43
28        44:38:39:22:01:8a        vxlan48     10.0.1.34    30       static        8:06:43      8:06:43
29        48:b0:2d:fd:d3:bf        vxlan48     10.0.1.34    10       extern_learn  8:06:02      8:06:02
30        44:38:39:22:01:84        vxlan48     10.0.1.34    10       extern_learn  8:06:43      8:06:43
31        48:b0:2d:2d:5f:b3        vxlan48     10.0.1.34    30       extern_learn  8:06:32      8:06:32
...
```

The following example shows the `nv show interface neighbor` command output:

```
cumulus@leaf01:mgmt:~$ nv show interface neighbor
Interface      IP/IPV6                    LLADR(MAC)         Neighbor State  Flag     
-------------  -------------------------  -----------------  --------------  ---------
eth0           192.168.200.251            48:b0:2d:00:00:01  stale                    
               192.168.200.1              48:b0:2d:7a:a5:cb  reachable                
               fe80::4ab0:2dff:fe00:1     48:b0:2d:00:00:01  reachable       router   
peerlink.4094  169.254.0.1                48:b0:2d:52:13:fd  permanent                
               fe80::4ab0:2dff:fe52:13fd  48:b0:2d:52:13:fd  reachable       router   
swp51          169.254.0.1                48:b0:2d:3a:75:22  permanent                
               fe80::4ab0:2dff:fe3a:7522  48:b0:2d:3a:75:22  reachable       router   
swp52          169.254.0.1                48:b0:2d:b6:62:a4  permanent                
               fe80::4ab0:2dff:feb6:62a4  48:b0:2d:b6:62:a4  reachable       router   
swp53          169.254.0.1                48:b0:2d:83:10:5c  permanent                
               fe80::4ab0:2dff:fe83:105c  48:b0:2d:83:10:5c  reachable       router   
swp54          169.254.0.1                48:b0:2d:d4:6a:cf  permanent                
               fe80::4ab0:2dff:fed4:6acf  48:b0:2d:d4:6a:cf  reachable       router   
vlan10         10.1.10.101                48:b0:2d:5b:5f:9d  reachable                
               10.1.10.3                  44:38:39:22:01:78  permanent                
               10.1.10.104                48:b0:2d:a1:ea:d0  noarp           ext_learn
               fe80::4ab0:2dff:fea1:ead0  48:b0:2d:a1:ea:d0  noarp           ext_learn
               fe80::4ab0:2dff:fe5b:5f9d  48:b0:2d:5b:5f:9d  reachable                
               fe80::4638:39ff:fe22:178   44:38:39:22:01:78  permanent                
vlan10-v0      10.1.10.101                48:b0:2d:5b:5f:9d  stale                    
               fe80::4ab0:2dff:fea1:ead0  48:b0:2d:a1:ea:d0  stale                    
               fe80::4ab0:2dff:fe5b:5f9d  48:b0:2d:5b:5f:9d  stale                    
vlan20         10.1.20.102                48:b0:2d:5b:d5:c8  reachable                
               10.1.20.3                  44:38:39:22:01:78  permanent                
               10.1.20.105                48:b0:2d:8c:b3:8a  noarp           ext_learn
               fe80::4ab0:2dff:fe8c:b38a  48:b0:2d:8c:b3:8a  noarp           ext_learn
               fe80::4ab0:2dff:fe5b:d5c8  48:b0:2d:5b:d5:c8  reachable                
               fe80::4638:39ff:fe22:178   44:38:39:22:01:78  permanent                
vlan20-v0      10.1.20.102                48:b0:2d:5b:d5:c8  stale                    
               fe80::4ab0:2dff:fe5b:d5c8  48:b0:2d:5b:d5:c8  stale                    
               fe80::4ab0:2dff:fe8c:b38a  48:b0:2d:8c:b3:8a  stale                    
vlan30         10.1.30.106                48:b0:2d:00:df:e9  noarp           ext_learn
               10.1.30.3                  44:38:39:22:01:78  permanent                
               10.1.30.103                48:b0:2d:a7:ef:72  reachable                
               fe80::4638:39ff:fe22:178   44:38:39:22:01:78  permanent                
               fe80::4ab0:2dff:fe00:dfe9  48:b0:2d:00:df:e9  noarp           ext_learn
               fe80::4ab0:2dff:fea7:ef72  48:b0:2d:a7:ef:72  reachable                
vlan30-v0      10.1.30.103                48:b0:2d:a7:ef:72  stale                    
               fe80::4ab0:2dff:fea7:ef72  48:b0:2d:a7:ef:72  stale                    
               fe80::4ab0:2dff:fe00:dfe9  48:b0:2d:00:df:e9  stale                    
vlan4006_l3    10.0.1.34                  44:38:39:be:ef:bb  noarp           ext_learn
               10.10.10.4                 44:38:39:22:01:8a  noarp           ext_learn
               10.10.10.2                 44:38:39:22:01:78  noarp           ext_learn
               10.10.10.63                44:38:39:22:01:74  noarp           ext_learn
               10.10.10.64                44:38:39:22:01:7c  noarp           ext_learn
               10.10.10.3                 44:38:39:22:01:84  noarp           ext_learn
               fe80::4638:39ff:fe22:178   44:38:39:22:01:78  permanent                
vlan4063_l3    10.0.1.34                  44:38:39:be:ef:bb  noarp           ext_learn
               10.10.10.63                44:38:39:22:01:74  noarp           ext_learn
               10.10.10.3                 44:38:39:22:01:84  noarp           ext_learn
               10.10.10.4                 44:38:39:22:01:8a  noarp           ext_learn
               10.10.10.2                 44:38:39:22:01:78  noarp           ext_learn
               10.10.10.64                44:38:39:22:01:7c  noarp           ext_learn
               fe80::4638:39ff:fe22:178   44:38:39:22:01:78  permanent                
vxlan48        10.10.10.3                 44:38:39:22:01:84  noarp           ext_learn
               10.10.10.4                 44:38:39:22:01:8a  noarp           ext_learn
               10.0.1.34                  44:38:39:be:ef:bb  noarp           ext_learn
               10.10.10.2                 44:38:39:22:01:78  noarp           ext_learn
               10.10.10.64                44:38:39:22:01:7c  noarp           ext_learn
               10.10.10.63                44:38:39:22:01:74  noarp           ext_learn
```

The following command shows the VLAN to VNI mapping for all bridges:

```
cumulus@switch:mgmt:~$ nv show bridge vlan-vni-map
br_default vlan-vni-offset: 0         
      VLAN        VNI         
      ----        -------     
      10          10          
      20          20          
      30          30
```

The following command shows the VLAN to VNI mapping for a specific bridge:

```
cumulus@switch:mgmt:~$ nv show bridge domain br_default vlan-vni-map
vlan-vni-offset: 0         
      VLAN        VNI         
      ----        -------     
      10          10          
      20          20          
      30          30   
```

## General BGP Commands

If you use BGP for the underlay routing, run the vtysh `show bgp summary` command to view a summary of the layer 3 fabric connectivity:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show bgp summary
IPv4 Unicast Summary
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 13
RIB entries 25, using 4800 bytes of memory
Peers 5, using 106 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
spine01(swp51)        4      65199       814       805        0    0    0 00:37:34            7
spine02(swp52)        4      65199       814       805        0    0    0 00:37:34            7
spine03(swp53)        4      65199       814       805        0    0    0 00:37:34            7
spine04(swp54)        4      65199       814       805        0    0    0 00:37:34            7
leaf02(peerlink.4094) 4      65101       766       768        0    0    0 00:37:35           12

Total number of neighbors 5

show bgp ipv6 unicast summary
=============================
% No BGP neighbors found

show bgp l2vpn evpn summary
===========================
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 0
RIB entries 23, using 4416 bytes of memory
Peers 4, using 85 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
spine01(swp51)  4      65199       814       805        0    0    0 00:37:35           34
spine02(swp52)  4      65199       814       805        0    0    0 00:37:35           34
spine03(swp53)  4      65199       814       805        0    0    0 00:37:35           34
spine04(swp54)  4      65199       814       805        0    0    0 00:37:35           34

Total number of neighbors 4
```

Run the vtysh `show ip route` command to examine the underlay routing and determine how the switch reaches remote VTEPs. The following example shows output from a leaf switch:
{{<notice note>}}
This is the routing table of the global (underlay) routing table. Use the `vrf` keyword to see routes for specific VRFs where the hosts reside.
{{</notice>}}

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route

C>* 10.0.1.1/32 is directly connected, lo, 00:40:02
B>* 10.0.1.2/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:40:04
  *                    via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:40:04
  *                    via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:40:04
  *                    via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:40:04
B>* 10.0.1.254/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:35:18
  *                      via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:35:18
  *                      via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:35:18
  *                      via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:35:18
C>* 10.10.10.1/32 is directly connected, lo, 00:42:58
B>* 10.10.10.2/32 [200/0] via fe80::c28a:e6ff:fe03:96d0, peerlink.4094, weight 1, 00:42:56
B>* 10.10.10.3/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:42:55
  *                      via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:42:55
  *                      via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:42:55
  *                      via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:42:55
B>* 10.10.10.4/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:42:55
  *                      via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:42:55
  *                      via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:42:55
  *                      via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:42:55
B>* 10.10.10.63/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:42:55
  *                       via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:42:55
  *                       via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:42:55
  *                       via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:42:55
B>* 10.10.10.64/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:38:07
  *                       via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:38:07
  *                       via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:38:07
  *                       via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:38:07
B>* 10.10.10.101/32 [20/0] via fe80::f208:5fff:fe12:cc8c, swp51, weight 1, 00:42:56
B>* 10.10.10.102/32 [20/0] via fe80::c299:6bff:fec0:e1ca, swp52, weight 1, 00:42:56
B>* 10.10.10.103/32 [20/0] via fe80::2ef3:45ff:fef4:6f5f, swp53, weight 1, 00:42:56
B>* 10.10.10.104/32 [20/0] via fe80::ae56:f0ff:fef3:590c, swp54, weight 1, 00:42:56
```

## Show EVPN Address Family Peers

Run the vtysh `show bgp l2vpn evpn summary` command to see the BGP peers participating in the EVPN address family and their states. The following example output from a leaf switch shows eBGP peering with four spine switches to exchange EVPN routes; all peering sessions are in the *established* state.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show bgp l2vpn evpn summary
BGP router identifier 10.10.10.1, local AS number 65101 VRF default vrf-id 0
BGP table version 0
RIB entries 47, using 6016 bytes of memory
Peers 5, using 100 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd   PfxSnt Desc
leaf02(peerlink.4094) 4      65102     30648     30648       32    0    0 1d01h27m           57       81 FRRouting/10.0.3
spine01(swp51)        4      65199     30667     30645       32    0    0 1d01h27m           57       81 FRRouting/10.0.3
spine02(swp52)        4      65199     30662     30643       32    0    0 1d01h27m           57       81 FRRouting/10.0.3
spine03(swp53)        4      65199     30669     30644       32    0    0 1d01h27m           57       81 FRRouting/10.0.3
spine04(swp54)        4      65199     30666     30644       32    0    0 1d01h27m           57       81 FRRouting/10.0.3

Total number of neighbors 5
```

## Show Configured EVPN VNIs

To display the configured VNIs on a network device participating in BGP EVPN, run the vtysh `show bgp l2vpn evpn vni` command. This command is only relevant on a VTEP. For symmetric routing, this command displays the special layer 3 VNIs for each tenant VRF.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show bgp l2vpn evpn vni
Advertise Gateway Macip: Disabled
Advertise SVI Macip: Disabled
Advertise All VNI flag: Enabled
BUM flooding: Head-end replication
VXLAN flooding: Enabled
Number of L2 VNIs: 3
Number of L3 VNIs: 2
Flags: * - Kernel
  VNI        Type RD                    Import RT                 Export RT                 MAC-VRF Site-of-Origin    Tenant VRF                           
* 20         L2   10.10.10.1:4          65101:20                  65101:20                                            RED                                  
* 30         L2   10.10.10.1:5          65101:30                  65101:30                                            BLUE                                 
* 10         L2   10.10.10.1:6          65101:10                  65101:10                                            RED                                  
* 4002       L3   10.10.10.1:2          65101:4002                65101:4002                                          BLUE                                 
* 4001       L3   10.10.10.1:3          65101:4001                65101:4001                                          RED
```

To show the configured layer 3 VNIs on a network device participating in EVPN, run the vtysh `show evpn vni detail` command. This command provides detailed information about all layer 3 VNIs configured across all VRFs on the device.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show evpn vni detail
VNI: 10
 Type: L2
 Vlan: 10
 Bridge: br_default
 Tenant VRF: RED
 VxLAN interface: vxlan48
 VxLAN ifIndex: 61
 SVI interface: vlan10
 SVI ifIndex: 69
 Local VTEP IP: 10.0.1.12
 Mcast group: 0.0.0.0
 Remote VTEPs for this VNI:
  10.0.1.34 flood: HER
 Number of MACs (local and remote) known for this VNI: 9
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 4
 Advertise-gw-macip: No
 Advertise-svi-macip: No

VNI: 30
 Type: L2
 Vlan: 30
 Bridge: br_default
 Tenant VRF: BLUE
 VxLAN interface: vxlan48
 VxLAN ifIndex: 61
 SVI interface: vlan30
 SVI ifIndex: 64
 Local VTEP IP: 10.0.1.12
 Mcast group: 0.0.0.0
 Remote VTEPs for this VNI:
  10.0.1.34 flood: HER
 Number of MACs (local and remote) known for this VNI: 9
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 4
 Advertise-gw-macip: No
 Advertise-svi-macip: No

VNI: 20
 Type: L2
 Vlan: 20
 Bridge: br_default
 Tenant VRF: RED
 VxLAN interface: vxlan48
 VxLAN ifIndex: 61
 SVI interface: vlan20
 SVI ifIndex: 72
 Local VTEP IP: 10.0.1.12
 Mcast group: 0.0.0.0
 Remote VTEPs for this VNI:
  10.0.1.34 flood: HER
 Number of MACs (local and remote) known for this VNI: 9
 Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 4
 Advertise-gw-macip: No
 Advertise-svi-macip: No

VNI: 4001
  Type: L3
  Tenant VRF: RED
  Vlan: 4063
  Bridge: br_default
  Local Vtep Ip: 10.0.1.12
  Vxlan-Intf: vxlan48
  SVI-If: vlan4063_l3
  State: Up
  VNI Filter: none
  System MAC: 44:38:39:22:01:7a
  Router MAC: 44:38:39:be:ef:aa
  Number of MACs (local and remote) known for this VNI: 6
  Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 6
  L2 VNIs: 10 20 

VNI: 4002
  Type: L3
  Tenant VRF: BLUE
  Vlan: 4006
  Bridge: br_default
  Local Vtep Ip: 10.0.1.12
  Vxlan-Intf: vxlan48
  SVI-If: vlan4006_l3
  State: Up
  VNI Filter: none
  System MAC: 44:38:39:22:01:7a
  Router MAC: 44:38:39:be:ef:aa
  Number of MACs (local and remote) known for this VNI: 6
  Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 6
  L2 VNIs: 30
```

Run the NVUE `nv show evpn vni` command or the vtysh `show evpn vni` command to see a summary of all VNIs and the number of MAC or ARP entries associated with each VNI.

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 
NumMacs - Number of MACs (local and remote) known for this VNI, NumArps - Number
of ARPs (IPv4 and IPv6, local and remote) known for this VNI                    
, NumRemVteps - Number of Remote Vteps, Bridge - Bridge to which the vni        
belongs, Vlan - VLAN assoicated to MAC                                          
VNI  NumMacs  NumArps  NumRemVteps  TenantVrf  Bridge      Vlan
---  -------  -------  -----------  ---------  ----------  ----
10   7        4        1            RED        br_default  10  
20   7        4        1            RED        br_default  20  
30   7        4        1            BLUE       br_default  30  
```

Run the NVUE `nv show evpn vni <vni>` command or the vtysh `show evpn vni <vni>` command to examine EVPN information for a specific VNI in detail. The following example output shows details for the layer 2 VNI 10. The output shows the remote VTEPs that contain that VNI.

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10
                   operational  applied
-----------------  -----------  -------
route-advertise                        
  svi-ip           off                 
  default-gateway  off                 
[remote-vtep]      10.0.1.34           
vlan               10                  
bridge-domain      br_default          
tenant-vrf         RED                 
vxlan-interface    vxlan48             
mac-count          9                   
host-count         4                   
remote-vtep-count  1                   
local-vtep         10.0.1.12
```

## Show EVPN VNIs Across All VRFs

To show a summary of all VNIs with the number of MAC or ARP entries and VLAN IDs associated with layer 3 VNIs across all VRFs, run the NVUE `nv show vrf evpn` or `nv show vrf evpn  --view=evpn` command.

```
cumulus@leaf01:mgmt:~$ nv show vrf evpn

State - State of the L3VNI, Svi - Svi interface for L3VNI, RouterMac - Router
MAC Address, SystemMac - System MAC Address, NexthopCount - Number of ARPs (IPv4
and IPv6, local and remote) known for this VNI, RouterMacCount - Number of MACs
(local and remote) known for this VNI, VXLANIntf - Vxlan interface of the L3VNI,
PrefixRoutesOnly - Associated L3 VNI and corresponding route targets only with
EVPN type-5 routes, not with EVPN type-2 routes.

Name  Vni   State  Svi          RouterMac          SystemMac          Vlan  NexthopCount  RouterMacCount  VXLANIntf  PrefixRoutesOnly
----  ----  -----  -----------  -----------------  -----------------  ----  ------------  --------------  ---------  ----------------
BLUE  4002  up     vlan4006_l3  44:38:39:be:ef:aa  44:38:39:22:01:7a  4006  6             6               vxlan48    off             
RED   4001  up     vlan4063_l3  44:38:39:be:ef:aa  44:38:39:22:01:7a  4063  6             6               vxlan48    off
```

## Show EVPN Information for a Specific VRF

To examine EVPN information for a specific VRF VNI in detail, run the NVUE `nv show vrf <vrf-id> evpn` command. The following example shows comprehensive information such as VNI, MAC or ARP entries, VLAN-ID and more:

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn
                    operational        applied
------------------  -----------------  -------
enable                                 on     
vlan                4063               auto   
[vni]               4001               4001   
nexthop-count       6                         
router-mac-count    6                         
state               Up                        
svi                 vlan4063_l3               
router-mac          44:38:39:be:ef:aa         
vxlan-interface     vxlan48                   
system-mac          44:38:39:22:01:7a         
prefix-routes-only  off                off
```

To show details for a layer 3 VRF for a specific VNI, run the vtysh `show vrf <vrf-id> vni` and the `show evpn vni <vni>` command.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show vrf RED vni
VRF            VNI        VxLAN IF          L3-SVI             State    Rmac              
RED            4001       vxlan48           vlan4063_l3        Up       44:38:39:be:ef:aa
```

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show evpn vni 4001
VNI: 4001
  Type: L3
  Tenant VRF: RED
  Vlan: 4063
  Bridge: br_default
  Local Vtep Ip: 10.0.1.12
  Vxlan-Intf: vxlan48
  SVI-If: vlan4063_l3
  State: Up
  VNI Filter: none
  System MAC: 44:38:39:22:01:7a
  Router MAC: 44:38:39:be:ef:aa
  Number of MACs (local and remote) known for this VNI: 6
  Number of ARPs (IPv4 and IPv6, local and remote) known for this VNI: 6
  L2 VNIs: 10 20
```

## Show BGP Information for a VNI

To show VNI BGP information, run the NVUE `nv show evpn vni <id> bgp-info` and `nv show vrf <vrf_id> evpn bgp-info` commands, or the vtysh `show bgp l2vpn evpn vni <vni>` command.

```
cumulus@border01:mgmt:~$ nv show vrf RED evpn bgp-info
                       operational      
---------------------  -----------------
rd                     10.10.10.1:3     
local-vtep             10.0.1.12        
router-mac             44:38:39:be:ef:aa
system-mac             44:38:39:22:01:7a
system-ip              10.10.10.1       
[import-route-target]  65101:4001       
[export-route-target]  65101:4001
```

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 bgp-info 
                           operational   pending
-------------------------  ------------  -------
rd                         10.10.10.1:9         
local-vtep                 10.10.10.1           
advertise-svi-ip           off                  
advertise-default-gateway  off                  
in-kernel                  on                   
type                       L2                   
mac-vrf-soo                                     
[import-route-target]      65101:10             
[export-route-target]      65101:10
```

## Examine Local and Remote MAC Addresses for a VNI

Run the NVUE `nv show evpn vni <vni> mac` command or the vtysh `show evpn mac vni <vni>` command to examine all local and remote MAC addresses for a VNI. This command is only relevant for a layer 2 VNI:

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 mac                                                                               
LocMobSeq - local mobility sequence, RemMobSeq - remote mobility sequence,      
RemoteVtep - Remote Vtep address, Esi - Remote Esi                              
MAC address        Type    LocMobSeq  RemMobSeq  Interface  RemoteVtep  Esi
-----------------  ------  ---------  ---------  ---------  ----------  ---
44:38:39:22:01:8a  remote  0          0                     10.0.1.34      
44:38:39:22:01:78  local   0          0          peerlink                  
44:38:39:22:01:84  remote  0          0                     10.0.1.34      
48:b0:2d:5c:8a:ee  local   0          0          bond1                     
48:b0:2d:29:c0:bb  remote  0          0                     10.0.1.34      
48:b0:2d:c9:f8:14  remote  0          0                     10.0.1.34      
48:b0:2d:fa:72:e7  local   0          0          bond      
```

Run the vtysh `show evpn mac vni all` command to examine MAC addresses for all VNIs.

You can examine the details for a specific MAC addresses or query all remote MAC addresses behind a specific VTEP:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show evpn mac vni 10 mac 94:8e:1c:0d:77:93
MAC: 94:8e:1c:0d:77:93
 Remote VTEP: 10.0.1.2
 Sync-info: neigh#: 0
 Local Seq: 0 Remote Seq: 0
 Neighbors:
    No Neighbors

leaf01# show evpn mac vni 20 vtep 10.0.1.2
VNI 20

MAC               Type   FlagsIntf/Remote ES/VTEP            VLAN  Seq #'s
12:15:9a:9c:f2:e1 remote       10.0.1.2                             1/0
50:88:b2:3c:08:f9 remote       10.0.1.2                             0/0
f8:4f:db:ef:be:8b remote       10.0.1.2                             0/0
c8:7d:bc:96:71:f3 remote       10.0.1.2                             0/0
```

## Examine Local and Remote Neighbors for a VNI

Run the vtysh `show evpn arp-cache vni <vni>` command to examine all local and remote neighbors (ARP entries) for a VNI. This command is only relevant for a layer 2 VNI and the output shows both IPv4 and IPv6 neighbor entries:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show evpn arp-cache vni 10
Number of ARPs (local and remote) known for this VNI: 6
Flags: I=local-inactive, P=peer-active, X=peer-proxy
Neighbor                  Type   Flags State    MAC               Remote ES/VTEP                 Seq #'s
10.1.10.2                 local        active   76:ed:2a:8a:67:24                                0/0
fe80::968e:1cff:fe0d:7793 remote       active   68:0f:31:ae:3d:7a 10.0.1.2                       0/0
10.1.10.101               local        active   26:76:e6:93:32:78                                0/0
fe80::9465:45ff:fe6d:4890 local        active   26:76:e6:93:32:78                                0/0
10.1.10.104               remote       active   68:0f:31:ae:3d:7a 10.0.1.2                       0/0
fe80::74ed:2aff:fe8a:6724 local        active   76:ed:2a:8a:67:24                                0/0
...
```

Run the vtysh `show evpn arp-cache vni all` command to examine neighbor entries for all VNIs.

## Examine Remote Router MAC Addresses

To examine the router MAC addresses corresponding to all remote VTEPs for symmetric routing, run the NVUE `nv show vrf <vrf-id> evpn remote-router-mac` command or the vtysh `show evpn rmac vni all` command. This command is only relevant for a layer 3 VNI:

```
cumulus@border01:mgmt:~$ nv show vrf RED evpn remote-router-mac
MAC address        remote-vtep
-----------------  -----------
44:38:39:22:01:7a  10.10.10.1 
44:38:39:22:01:7c  10.10.10.64
44:38:39:22:01:8a  10.10.10.4 
44:38:39:22:01:78  10.10.10.2 
44:38:39:22:01:84  10.10.10.3 
44:38:39:be:ef:aa  10.0.1.12
```

## Examine Gateway Next Hops

To examine the gateway next hops for symmetric routing, run the NVUE `nv show vrf <vrf-id> evpn nexthop-vtep` command or the vtysh `show evpn next-hops vni all` command. This command is only relevant for a layer 3 VNI. The gateway next hop IP addresses correspond to the remote VTEP IP addresses. Cumulus Linux installs the remote host and prefix routes using these next hops.

```
cumulus@border01:mgmt:~$ nv show vrf RED evpn nexthop-vtep
Nexthop      router-mac       
-----------  -----------------
10.0.1.12    44:38:39:be:ef:aa
10.10.10.1   44:38:39:22:01:7a
10.10.10.2   44:38:39:22:01:78
10.10.10.3   44:38:39:22:01:84
10.10.10.4   44:38:39:22:01:8a
10.10.10.64  44:38:39:22:01:7c
```

To show the router MAC address for a specific next hop, run the NVUE `nv show vrf <vrf-id> evpn nexthop-vtep <ip-address>` command:

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn nexthop-vtep 10.10.10.2
            operational       
----------  -----------------
router-mac  44:38:39:22:01:78
```

To show the remote host and prefix routes through a specific next hop, run the vtysh `show evpn next-hops vni <vni> ip <ip-address>` command:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show evpn next-hops vni 4001 ip 10.0.1.2
Ip: 10.0.1.2
  RMAC: 44:38:39:be:ef:bb
  Refcount: 2
  Prefixes:
    10.1.10.104/32
    10.1.20.105/32
```

To show the VTEP IP addresses for the next hop groups, run the `nv show evpn l2-nhg vtep-ip` command.

## Show Access VLANs

To show access VLANs on the switch and their corresponding VNI, run the NVUE `nv show evpn access-vlan-info` command or the vtysh `show evpn access-vlan` command.

```
cumulus@border01:mgmt:~$ nv show evpn access-vlan-info
vlan
=======
    Id    MemberCnt  Vni  VniCnt  VxlanIntf  MemberIntf
    ----  ---------  ---  ------  ---------  ----------
    1     1                                  peerlink  
    10    2          10   1       vxlan48    bond1     
                                             peerlink  
    20    2          20   1       vxlan48    bond2     
                                             peerlink  
    30    2          30   1       vxlan48    bond3     
                                             peerlink  
    4006                  1       vxlan48              
    4063                  1       vxlan48    
```

You can drill down and show information about a specific vlan with the `nv show evpn access-vlan-info vlan <vlan>` command.

## Show the VRF Routing Table in FRR

Run the NVUE `nv show vrf <vrf-id> router rib <address-family> route` command or the vtysh `show ip route vrf <vrf-id>` command to examine the VRF routing table. Use this command for symmetric routing to verify that remote host and prefix routes are in the VRF routing table and point to the appropriate gateway next hop.

```
cumulus@leaf01:mgmt:~$ nv show vrf RED router rib ipv4 route
                                                                                
Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-        
selected, x - failed                                                            
                                                                                
Route           Protocol   Distance  Uptime                NHGId  Metric  Flags
--------------  ---------  --------  --------------------  -----  ------  -----
0.0.0.0/0       kernel     255       2024-10-25T14:02:23Z  21     8192    *Si  
10.1.10.0/24    connected  0         2024-10-25T14:02:33Z  100    1024    io   
                connected  0         2024-10-25T14:02:33Z  88     0       *Sio 
10.1.20.0/24    connected  0         2024-10-25T14:02:33Z  103    1024    io   
                connected  0         2024-10-25T14:02:33Z  92     0       *Sio 
10.1.20.105/32  bgp        20        2024-10-25T14:02:46Z  166    0       *Si  
10.1.30.0/24    bgp        20        2024-10-25T14:02:39Z  154    0       *Si
```

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip route vrf RED
show ip route vrf RED
======================
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route

VRF RED:
K>* 0.0.0.0/0 [255/8192] unreachable (ICMP unreachable), 00:53:46
C * 10.1.10.0/24 [0/1024] is directly connected, vlan10-v0, 00:53:46
C>* 10.1.10.0/24 is directly connected, vlan10, 00:53:46
B>* 10.1.10.104/32 [20/0] via 10.0.1.2, vlan4001 onlink, weight 1, 00:43:55
C * 10.1.20.0/24 [0/1024] is directly connected, vlan20-v0, 00:53:46
C>* 10.1.20.0/24 is directly connected, vlan20, 00:53:46
B>* 10.1.20.105/32 [20/0] via 10.0.1.2, vlan4001 onlink, weight 1, 00:20:07
...
```
<!-- vale on -->
In the output above, EVPN specifies the next hops for these routes to be *onlink*, or reachable over the specified SVI. This is necessary because this interface does not need to have an IP address. Even if the interface has an IP address, the next hop is not on the same subnet as it is typically the IP address of the remote VTEP (part of the underlay IP network).

## Show the Global BGP EVPN Routing Table

Run the vtysh `show bgp l2vpn evpn route` command to display all EVPN routes, both local and remote. Cumulus Linux bases the routes on the RD as they are across VNIs and VRFs:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show bgp l2vpn evpn route
BGP table version is 6, local router ID is 10.10.10.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
                    Extended Community
Route Distinguisher: 10.10.10.1:3
*> [2]:[0]:[48]:[00:60:08:69:97:ef]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[26:76:e6:93:32:78]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[26:76:e6:93:32:78]:[32]:[10.1.10.101]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[26:76:e6:93:32:78]:[128]:[fe80::9465:45ff:fe6d:4890]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10
*> [2]:[0]:[48]:[c0:8a:e6:03:96:d0]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10 RT:65101:4001 MM:0, sticky MAC Rmac:44:38:39:be:ef:aa
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:10
Route Distinguisher: 10.10.10.1:4
*> [2]:[0]:[48]:[c0:8a:e6:03:96:d0]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:20 RT:65101:4001 MM:0, sticky MAC Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[cc:6e:fa:8d:ff:92]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:20 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[f0:9d:d0:59:60:5d]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:20 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[f0:9d:d0:59:60:5d]:[128]:[fe80::ce6e:faff:fe8d:ff92]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:20
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:20
Route Distinguisher: 10.10.10.1:6
*> [2]:[0]:[48]:[c0:8a:e6:03:96:d0]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:30 RT:65101:4002 MM:0, sticky MAC Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[de:02:3b:17:c9:6d]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:30 RT:65101:4002 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[de:02:3b:17:c9:6d]:[128]:[fe80::dc02:3bff:fe17:c96d]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:30
*> [2]:[0]:[48]:[ea:77:bb:f1:a7:ca]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:30 RT:65101:4002 Rmac:44:38:39:be:ef:aa
*> [3]:[0]:[32]:[10.0.1.1]
                    10.0.1.1                           32768 i
                    ET:8 RT:65101:30
Route Distinguisher: 10.10.10.3:3
*> [2]:[0]:[48]:[12:15:9a:9c:f2:e1]
                    10.0.1.2                               0 65199 65102 i
                    RT:65102:20 RT:65102:4001 ET:8 Rmac:44:38:39:be:ef:bb
*  [2]:[0]:[48]:[12:15:9a:9c:f2:e1]
                    10.0.1.2                               0 65199 65102 i
                    RT:65102:20 RT:65102:4001 ET:8 Rmac:44:38:39:be:ef:bb
...
```

You can filter the routing table based on EVPN route type. The available options are:
ead: EAD (Type-1) route
es: Ethernet Segment (type-4) route
macip: MAC-IP (Type-2) route
multicast: Multicast
prefix: An IPv4 or IPv6 prefix

## Show EVPN RD Routes

To show EVPN RD routes, run the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route` command. This command shows the EVPN RD routes in brief format to improve performance for high scale environments. To show the EVPN RD routes in more detail, run the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route --view=detail` command. To show the information in json format, run the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route -o json` command.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn route
PathCnt - number of L2VPN EVPN per (RD, route-type) paths
Route                                                                   rd             route-type  PathCnt
----------------------------------------------------------------------  -------------  ----------  -------
[10.10.10.1:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.1:2   5           1      
[10.10.10.1:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.1:3   5           1      
[10.10.10.1:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.1:3   5           1      
[10.10.10.1:4]:[2]:[0]:[44:38:39:22:01:78]                              10.10.10.1:4   2           1      
[10.10.10.1:4]:[2]:[0]:[48:b0:2d:7f:74:13]                              10.10.10.1:4   2           1      
[10.10.10.1:4]:[2]:[0]:[48:b0:2d:7f:74:13]:[10.1.20.102]                10.10.10.1:4   2           1      
[10.10.10.1:4]:[2]:[0]:[48:b0:2d:7f:74:13]:[fe80::4ab0:2dff:fe7f:7413]  10.10.10.1:4   2           1      
[10.10.10.1:4]:[2]:[0]:[48:b0:2d:a4:40:62]                              10.10.10.1:4   2           1      
[10.10.10.1:4]:[3]:[0]:[10.0.1.12]                                      10.10.10.1:4   3           1      
[10.10.10.1:5]:[2]:[0]:[44:38:39:22:01:78]                              10.10.10.1:5   2           1      
[10.10.10.1:5]:[2]:[0]:[48:b0:2d:99:9e:04]                              10.10.10.1:5   2           1      
[10.10.10.1:5]:[2]:[0]:[48:b0:2d:c2:f9:21]                              10.10.10.1:5   2           1      
[10.10.10.1:5]:[2]:[0]:[48:b0:2d:c2:f9:21]:[10.1.30.103]                10.10.10.1:5   2           1      
[10.10.10.1:5]:[2]:[0]:[48:b0:2d:c2:f9:21]:[fe80::4ab0:2dff:fec2:f921]  10.10.10.1:5   2           1      
[10.10.10.1:5]:[3]:[0]:[10.0.1.12]                                      10.10.10.1:5   3           1      
[10.10.10.1:6]:[2]:[0]:[44:38:39:22:01:78]                              10.10.10.1:6   2           1      
[10.10.10.1:6]:[2]:[0]:[48:b0:2d:5c:8a:ee]                              10.10.10.1:6   2           1      
[10.10.10.1:6]:[2]:[0]:[48:b0:2d:fa:72:e7]                              10.10.10.1:6   2           1      
[10.10.10.1:6]:[2]:[0]:[48:b0:2d:fa:72:e7]:[10.1.10.101]                10.10.10.1:6   2           1      
[10.10.10.1:6]:[2]:[0]:[48:b0:2d:fa:72:e7]:[fe80::4ab0:2dff:fefa:72e7]  10.10.10.1:6   2           1      
[10.10.10.1:6]:[3]:[0]:[10.0.1.12]                                      10.10.10.1:6   3           1      
[10.10.10.2:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.2:2   5           5      
[10.10.10.2:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.2:3   5           5      
[10.10.10.2:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.2:3   5           5      
[10.10.10.3:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.3:2   5           5      
[10.10.10.3:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.3:3   5           5      
[10.10.10.3:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.3:3   5           5      
[10.10.10.3:4]:[2]:[0]:[44:38:39:22:01:8a]                              10.10.10.3:4   2           5      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:48:21:9d]                              10.10.10.3:4   2           5      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:82:43:48]                              10.10.10.3:4   2           5      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:82:43:48]:[10.1.20.105]                10.10.10.3:4   2           5      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:82:43:48]:[fe80::4ab0:2dff:fe82:4348]  10.10.10.3:4   2           5      
[10.10.10.3:4]:[3]:[0]:[10.0.1.34]                                      10.10.10.3:4   3           5      
[10.10.10.3:5]:[2]:[0]:[44:38:39:22:01:8a]                              10.10.10.3:5   2           5      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:d5:45:6f]                              10.10.10.3:5   2           5      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:d5:45:6f]:[10.1.30.106]                10.10.10.3:5   2           5      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:d5:45:6f]:[fe80::4ab0:2dff:fed5:456f]  10.10.10.3:5   2           5      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:df:a8:20]                              10.10.10.3:5   2           5      
[10.10.10.3:5]:[3]:[0]:[10.0.1.34]                                      10.10.10.3:5   3           5      
[10.10.10.3:6]:[2]:[0]:[44:38:39:22:01:8a]                              10.10.10.3:6   2           5      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:29:c0:bb]                              10.10.10.3:6   2           5      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:29:c0:bb]:[10.1.10.104]                10.10.10.3:6   2           5      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:29:c0:bb]:[fe80::4ab0:2dff:fe29:c0bb]  10.10.10.3:6   2           5      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:c9:f8:14]                              10.10.10.3:6   2           5      
[10.10.10.3:6]:[3]:[0]:[10.0.1.34]                                      10.10.10.3:6   3           5      
[10.10.10.4:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.4:2   5           5      
[10.10.10.4:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.4:3   5           5      
[10.10.10.4:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.4:3   5           5      
[10.10.10.4:4]:[2]:[0]:[44:38:39:22:01:84]                              10.10.10.4:4   2           5      
[10.10.10.4:4]:[2]:[0]:[48:b0:2d:48:21:9d]                              10.10.10.4:4   2           5      
[10.10.10.4:4]:[2]:[0]:[48:b0:2d:82:43:48]                              10.10.10.4:4   2           5      
[10.10.10.4:4]:[2]:[0]:[48:b0:2d:82:43:48]:[10.1.20.105]                10.10.10.4:4   2           5      
[10.10.10.4:4]:[2]:[0]:[48:b0:2d:82:43:48]:[fe80::4ab0:2dff:fe82:4348]  10.10.10.4:4   2           5      
[10.10.10.4:4]:[3]:[0]:[10.0.1.34]                                      10.10.10.4:4   3           5      
[10.10.10.4:5]:[2]:[0]:[44:38:39:22:01:84]                              10.10.10.4:5   2           5      
[10.10.10.4:5]:[2]:[0]:[48:b0:2d:d5:45:6f]                              10.10.10.4:5   2           5      
[10.10.10.4:5]:[2]:[0]:[48:b0:2d:d5:45:6f]:[10.1.30.106]                10.10.10.4:5   2           5      
[10.10.10.4:5]:[2]:[0]:[48:b0:2d:d5:45:6f]:[fe80::4ab0:2dff:fed5:456f]  10.10.10.4:5   2           5      
[10.10.10.4:5]:[2]:[0]:[48:b0:2d:df:a8:20]                              10.10.10.4:5   2           5      
[10.10.10.4:5]:[3]:[0]:[10.0.1.34]                                      10.10.10.4:5   3           5      
[10.10.10.4:6]:[2]:[0]:[44:38:39:22:01:84]                              10.10.10.4:6   2           5      
[10.10.10.4:6]:[2]:[0]:[48:b0:2d:29:c0:bb]                              10.10.10.4:6   2           5      
[10.10.10.4:6]:[2]:[0]:[48:b0:2d:29:c0:bb]:[10.1.10.104]                10.10.10.4:6   2           5      
[10.10.10.4:6]:[2]:[0]:[48:b0:2d:29:c0:bb]:[fe80::4ab0:2dff:fe29:c0bb]  10.10.10.4:6   2           5      
[10.10.10.4:6]:[2]:[0]:[48:b0:2d:c9:f8:14]                              10.10.10.4:6   2           5      
[10.10.10.4:6]:[3]:[0]:[10.0.1.34]                                      10.10.10.4:6   3           5      
[10.10.10.63:2]:[5]:[0]:[10.1.10.0/24]                                  10.10.10.63:2  5           5      
[10.10.10.63:2]:[5]:[0]:[10.1.20.0/24]                                  10.10.10.63:2  5           5      
[10.10.10.63:3]:[5]:[0]:[10.1.30.0/24]                                  10.10.10.63:3  5           5      
[10.10.10.64:2]:[5]:[0]:[10.1.10.0/24]                                  10.10.10.64:2  5           5      
[10.10.10.64:2]:[5]:[0]:[10.1.20.0/24]                                  10.10.10.64:2  5           5      
[10.10.10.64:3]:[5]:[0]:[10.1.30.0/24]                                  10.10.10.64:3  5           5 
```

## Show a Specific EVPN Route

To drill down on a specific route for more information, run the vtysh `show bgp l2vpn evpn route rd <rd-value>` command. This command displays all EVPN routes with that RD and with the path attribute details for each path. Additional filtering is possible based on route type or by specifying the MAC and/or IP address. The following example shows the specific MAC/IP route of server05. The output shows that this remote host is behind VTEP 10.10.10.3 and is reachable through four paths; one through each spine switch. This example is from a symmetric routing configuration, so the route shows both the layer 2 VNI (20) and the layer 3 VNI (4001), as well as the EVPN route target attributes corresponding to each and the associated router MAC address.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show bgp l2vpn evpn route rd 10.10.10.3:3 mac 12:15:9a:9c:f2:e1 ip 10.1.20.105
BGP routing table entry for 10.10.10.3:3:[2]:[0]:[48]:[12:15:9a:9c:f2:e1]:[32]:[10.1.20.105]
Paths: (4 available, best #1)
  Advertised to non peer-group peers:
  spine01(swp51) spine02(swp52) spine03(swp53) spine04(swp54)
  Route [2]:[0]:[48]:[12:15:9a:9c:f2:e1]:[32]:[10.1.20.105] VNI 20/4001
  65199 65102
    10.0.1.2 from spine01(swp51) (10.10.10.101)
      Origin IGP, valid, external, bestpath-from-AS 65199, best (Router ID)
      Extended Community: RT:65102:20 RT:65102:4001 ET:8 Rmac:44:38:39:be:ef:bb
      Last update: Fri Jan 15 08:16:24 2021
  Route [2]:[0]:[48]:[12:15:9a:9c:f2:e1]:[32]:[10.1.20.105] VNI 20/4001
  65199 65102
    10.0.1.2 from spine04(swp54) (10.10.10.104)
      Origin IGP, valid, external
      Extended Community: RT:65102:20 RT:65102:4001 ET:8 Rmac:44:38:39:be:ef:bb
      Last update: Fri Jan 15 08:16:24 2021
  Route [2]:[0]:[48]:[12:15:9a:9c:f2:e1]:[32]:[10.1.20.105] VNI 20/4001
  65199 65102
    10.0.1.2 from spine02(swp52) (10.10.10.102)
      Origin IGP, valid, external
      Extended Community: RT:65102:20 RT:65102:4001 ET:8 Rmac:44:38:39:be:ef:bb
      Last update: Fri Jan 15 08:16:24 2021
  Route [2]:[0]:[48]:[12:15:9a:9c:f2:e1]:[32]:[10.1.20.105] VNI 20/4001
  65199 65102
    10.0.1.2 from spine03(swp53) (10.10.10.103)
      Origin IGP, valid, external
      Extended Community: RT:65102:20 RT:65102:4001 ET:8 Rmac:44:38:39:be:ef:bb
      Last update: Fri Jan 15 08:16:24 2021

Displayed 4 paths for requested prefix
```

{{%notice note%}}
- Only use global VNIs. Even though the switch exchanges VNI values in the type-2 and type-5 routes, Cumulus Linux does not use the received values when installing the routes into the forwarding plane but uses the local configuration instead. Ensure that the VLAN to VNI mappings and the layer 3 VNI assignment for a tenant VRF are the same throughout the network.
- If the remote host is dual attached, the next hop for the EVPN route is the anycast IP address of the remote {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}} pair when MLAG is active.
{{%/notice%}}

## Filter EVPN Routes by Neighbor, RD and Route Type

You can filter EVPN routes by a specific neighbor (numbered or unnumbered) with the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route --filter=”neighbor=<neighbor>"` command.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn route --filter="neighbor=swp51"
PathCnt - number of L2VPN EVPN per (RD, route-type) paths

Route                                                                   rd             route-type  PathCnt
----------------------------------------------------------------------  -------------  ----------  -------
[10.10.10.2:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.2:2   5           1      
[10.10.10.2:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.2:3   5           1      
[10.10.10.2:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.2:3   5           1      
[10.10.10.3:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.3:2   5           1      
[10.10.10.3:3]:[5]:[0]:[10.1.10.0/24]                                   10.10.10.3:3   5           1      
[10.10.10.3:3]:[5]:[0]:[10.1.20.0/24]                                   10.10.10.3:3   5           1      
[10.10.10.3:4]:[2]:[0]:[4a:b0:2d:0d:12:d8]                              10.10.10.3:4   2           1      
[10.10.10.3:4]:[2]:[0]:[4a:b0:2d:29:55:06]                              10.10.10.3:4   2           1      
[10.10.10.3:4]:[2]:[0]:[44:38:39:22:01:8a]                              10.10.10.3:4   2           1      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:0d:12:d8]                              10.10.10.3:4   2           1      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:0d:12:d8]:[10.1.20.105]                10.10.10.3:4   2           1      
[10.10.10.3:4]:[2]:[0]:[48:b0:2d:0d:12:d8]:[fe80::4ab0:2dff:fe0d:12d8]  10.10.10.3:4   2           1      
[10.10.10.3:4]:[3]:[0]:[10.0.1.34]                                      10.10.10.3:4   3           1      
[10.10.10.3:5]:[2]:[0]:[4a:b0:2d:c1:30:61]                              10.10.10.3:5   2           1      
[10.10.10.3:5]:[2]:[0]:[4a:b0:2d:c7:fa:bd]                              10.10.10.3:5   2           1      
[10.10.10.3:5]:[2]:[0]:[44:38:39:22:01:8a]                              10.10.10.3:5   2           1      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:c1:30:61]                              10.10.10.3:5   2           1      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:c1:30:61]:[10.1.30.106]                10.10.10.3:5   2           1      
[10.10.10.3:5]:[2]:[0]:[48:b0:2d:c1:30:61]:[fe80::4ab0:2dff:fec1:3061]  10.10.10.3:5   2           1      
[10.10.10.3:5]:[3]:[0]:[10.0.1.34]                                      10.10.10.3:5   3           1      
[10.10.10.3:6]:[2]:[0]:[4a:b0:2d:a1:a0:74]                              10.10.10.3:6   2           1      
[10.10.10.3:6]:[2]:[0]:[4a:b0:2d:d1:b9:ac]                              10.10.10.3:6   2           1      
[10.10.10.3:6]:[2]:[0]:[44:38:39:22:01:8a]                              10.10.10.3:6   2           1      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:d1:b9:ac]                              10.10.10.3:6   2           1      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:d1:b9:ac]:[10.1.10.104]                10.10.10.3:6   2           1      
[10.10.10.3:6]:[2]:[0]:[48:b0:2d:d1:b9:ac]:[fe80::4ab0:2dff:fed1:b9ac]  10.10.10.3:6   2           1      
[10.10.10.3:6]:[3]:[0]:[10.0.1.34]                                      10.10.10.3:6   3           1      
[10.10.10.4:2]:[5]:[0]:[10.1.30.0/24]                                   10.10.10.4:2   5           1          
...
```

You can also filter EVPN routes by a specific <span class="a-tooltip">[RD](## "Route Distinguisher")</span> with the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route --filter="rd=<rd>"` command and the route type with the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route --filter="rd=<rd>&route-type=<route-type>"` command.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn route --filter="rd=10.10.10.2:2" 
PathCnt - number of L2VPN EVPN per (RD, route-type) paths

Route                                  rd            route-type  PathCnt
-------------------------------------  ------------  ----------  -------
[10.10.10.2:2]:[5]:[0]:[10.1.30.0/24]  10.10.10.2:2  5           3 
...
```

## Show the VNI EVPN Routing Table

The switch maintains the received EVPN routes in the global EVPN routing table, even if there are no appropriate local VNIs to **import** them into. For example, a spine maintains the global EVPN routing table even though there are no VNIs present in the table. When local VNIs are present, the switch imports received EVPN routes into the per-VNI routing tables according to the route target attributes. You can examine the per-VNI routing table with the vtysh `show bgp vni <vni>` command:

```
leaf01# show bgp vni 10
BGP table version is 351, local router ID is 10.10.10.1
Status codes: s suppressed, d damped, h history, * valid, > best, i - internal
Origin codes: i - IGP, e - EGP, ? - incomplete
EVPN type-1 prefix: [1]:[ESI]:[EthTag]:[IPlen]:[VTEP-IP]:[Frag-id]
EVPN type-2 prefix: [2]:[EthTag]:[MAClen]:[MAC]:[IPlen]:[IP]
EVPN type-3 prefix: [3]:[EthTag]:[IPlen]:[OrigIP]
EVPN type-4 prefix: [4]:[ESI]:[IPlen]:[OrigIP]
EVPN type-5 prefix: [5]:[EthTag]:[IPlen]:[IP]

   Network          Next Hop            Metric LocPrf Weight Path
*> [2]:[0]:[48]:[44:38:39:00:00:32]:[32]:[10.1.10.101]
                    10.0.1.12 (leaf01)
                                                       32768 i
                    ET:8 RT:65101:10 RT:65101:4001 Rmac:44:38:39:be:ef:aa
*> [2]:[0]:[48]:[44:38:39:00:00:32]:[128]:[fe80::4638:39ff:fe00:32]
                    10.0.1.12 (leaf01)
                                                       32768 i
                    ET:8 RT:65101:10
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (leaf02)
                                                           0 65102 65199 65104 i
                    RT:65104:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (leaf02)
                                                           0 65102 65199 65103 i
                    RT:65103:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine02)
                                                           0 65199 65104 i
                    RT:65104:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine02)
                                                           0 65199 65103 i
                    RT:65103:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine04)
                                                           0 65199 65104 i
                    RT:65104:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine04)
                                                           0 65199 65103 i
                    RT:65103:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine03)
                                                           0 65199 65104 i
                    RT:65104:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine03)
                                                           0 65199 65103 i
                    RT:65103:10 ET:8
*  [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine01)
                                                           0 65199 65104 i
                    RT:65104:10 ET:8
*> [2]:[0]:[48]:[44:38:39:00:00:3e]:[128]:[fe80::4638:39ff:fe00:3e]
                    10.0.1.34 (spine01)
                                                           0 65199 65103 i
                    RT:65103:10 ET:8
...
```

To display the VNI routing table for all VNIs, run the vtysh `show bgp l2vpn evpn route vni all` command.

To view the EVPN RIB with NVUE, run the `nv show vrf <vrf-id> router bgp address-family l2vpn-evpn route` command.

## Show the VRF BGP Routing Table

For symmetric routing, the switch imports received type-2 and type-5 routes into the VRF routing table (according to address family: IPv4 unicast or IPv6 unicast) based on a match on the route target attributes. To examine the BGP VRF routing table, run the vtysh `show bgp vrf <vrf-id> ipv4 unicast` and `show bgp vrf <vrf-id> ipv6 unicast` command.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show bgp vrf RED ipv4 unicast
BGP table version is 2, local router ID is 10.1.20.2, vrf id 24
Default local pref 100, local AS 65101
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
*  10.1.10.104/32   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*>                  10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*  10.1.20.105/32   10.0.1.2<                              0 65199 65102 i
*>                  10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i
*                   10.0.1.2<                              0 65199 65102 i

Displayed  2 routes and 16 total paths
```

## Support for EVPN Neighbor Discovery (ND) Extended Community

In EVPN VXLAN with ARP and ND suppression where you only configure the VTEPs for layer 2, EVPN needs to carry additional information for the attached devices so proxy ND can provide the correct information to attached hosts. Without this information, hosts cannot configure their default routers or lose their existing default router information. Cumulus Linux supports the EVPN Neighbor Discovery (ND) Extended Community with a type field value of 0x06, a subtype field value of 0x08 (ND Extended Community), and a router flag; this enables the switch to determine if a particular IPv6-MAC pair belongs to a host or a router.

The following configurations use the **router flag** (R-bit):

- Centralized VXLAN routing with a gateway router.
- A layer 2 switch with ARP and ND suppression.

When the MAC/IP (type-2) route contains the IPv6-MAC pair with the R-bit flag, the route belongs to a router. If the R-bit is zero, the route belongs to a host. If the router is in a local LAN segment, the switch implementing the proxy ND function learns of this information by snooping on neighbor advertisement messages for the associated IPv6 address. Other EVPN peers exchange this information by using the ND extended community in BGP updates.

To show that the neighbor table includes the EVPN arp-cache and that the IPv6-MAC entry belongs to a router, run the vtysh `show evpn arp-cache vni <vni> ip <address>` command. For example:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show evpn arp-cache vni 20 ip 10.1.20.105
IP: 10.1.20.105
 Type: remote
 State: active
 MAC: 12:15:9a:9c:f2:e1
 Sync-info: -
 Remote VTEP: 10.0.1.2
 Local Seq: 0 Remote Seq: 0
```

## Examine MAC Moves

The first time a MAC moves from behind one VTEP to behind another, BGP associates a MAC Mobility (MM) extended community attribute of sequence number 1, with the type-2 route for that MAC. From there, each time this MAC moves to a new VTEP, the MM sequence number increments by 1. You can examine the MM sequence number associated with a MAC's type-2 route with the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac>` command. The example output below shows the type-2 route for a MAC that has moved three times:

```
cumulus@switch:~$ sudo vtysh
...
switch# show bgp l2vpn evpn route vni 10109 mac 00:02:22:22:22:02
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

You can identify static or *sticky* MACs in EVPN by the presence of `MM:0, sticky MAC` in the Extended Community line of the output from the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac>` command.

```
cumulus@switch:~$ sudo vtysh
...
switch# show bgp l2vpn evpn route vni 10101 mac 00:02:00:00:00:01
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
|`debug bgp updates` | Traces BGP update exchanges, including all updates. The output also shows EVPN specific information. |
| `debug bgp zebra` | Traces interactions between BGP and zebra for EVPN (and other) routes. |

## ICMP echo Replies and the ping Command

When you run the `ping -I ` command and specify an interface, you do not receive an ICMP echo reply. However, when you run the `ping` command without the `-I` option, everything works as expected.

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

When you send an ICMP echo request to an IP address that is not in the same subnet using the `ping -I` command, Cumulus Linux creates a failed ARP entry for the destination IP address.

For more information, refer to [this article]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/ICMP-Ping-Doesn-t-Work-when-Specifying-I-Option" >}}).
