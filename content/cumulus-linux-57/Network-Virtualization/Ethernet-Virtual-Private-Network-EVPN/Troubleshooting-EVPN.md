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
- `ip neighbor show` (Linux)
- `ip route show [table <vrf-name>]` (Linux)

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
<!--
- bond1 is in VLAN ID 10.
- 48:b0:2d:d8:33 is the host MAC address learned on bond1.
- A remote VTEP that participates in VLAN ID 10 is 10.0.1.34 (the FDB entries have a MAC address of 48:b0:2d:b4:4e). BUM traffic replication uses these entries.
- 44:38:39:22:01 is a remote host MAC reachable over the VXLAN tunnel via VTEP 10.0.1.2.
-->
```
cumulus@leaf01:mgmt:~$ nv show bridge domain br_default mac-table
entry-id  age    bridge-domain  entry-type    interface   last-update  MAC address        remote-dst       src-vni  vlan
--------  -----  -------------  ------------  ----------  -----------  -----------------  ---------------  -------  ----
1         12562  br_default     static        bond1       12562        48:b0:2d:98:61:d4                            10  
2         22     br_default     static        bond1       10550        48:b0:2d:72:9d:99                            10  
3         12777  br_default     permanent     bond1       12777        48:b0:2d:4c:da:d9                                
4         12562  br_default     extern_learn  vxlan48     12562        48:b0:2d:aa:b7:0c                            10  
5         12573  br_default     extern_learn  vxlan48     10549        48:b0:2d:ff:b8:07                            10  
6         12773  br_default     extern_learn  vxlan48     12773        44:38:39:22:01:8a                            10  
7         12773  br_default     extern_learn  vxlan48     12773        44:38:39:22:01:8a                            30  
8         12773  br_default     extern_learn  vxlan48     12773        44:38:39:22:01:8a                            20  
9         12773  br_default     extern_learn  vxlan48     116          44:38:39:22:01:78                            10  
10        12773  br_default     extern_learn  vxlan48     98           44:38:39:22:01:78                            30  
11        12773  br_default     extern_learn  vxlan48     86           44:38:39:22:01:78                            20  
12        12774  br_default     extern_learn  vxlan48     12556        44:38:39:22:01:84                            20  
13        12774  br_default     extern_learn  vxlan48     12566        44:38:39:22:01:84                            30  
14        12774  br_default     extern_learn  vxlan48     12774        44:38:39:22:01:84                            10  
15        12777  br_default     permanent     vxlan48     12777        76:2e:db:01:52:0e                                
16        12773                 extern_learn  vxlan48     116          44:38:39:22:01:78  10.10.10.2       10           
17        12562                 extern_learn  vxlan48     12562        48:b0:2d:aa:b7:0c  nhid: 536870916  10           
18        12773                 extern_learn  vxlan48     12773        44:38:39:22:01:8a  10.10.10.4       30           
19        12773                 extern_learn  vxlan48     86           44:38:39:22:01:78  10.10.10.2       20           
20        12774                 extern_learn  vxlan48     12774        44:38:39:22:01:84  10.10.10.3       10           
21        12773                 extern_learn  vxlan48     98           44:38:39:22:01:78  10.10.10.2       30           
22        12573                 extern_learn  vxlan48     10549        48:b0:2d:ff:b8:07  nhid: 536870916  10           
23        12774                 extern_learn  vxlan48     12566        44:38:39:22:01:84  10.10.10.3       30           
24        12774                 extern_learn  vxlan48     12556        44:38:39:22:01:84  10.10.10.3       20           
25        12773                 extern_learn  vxlan48     12773        44:38:39:22:01:8a  10.10.10.4       10           
26        12773                 permanent     vxlan48     25           00:00:00:00:00:00  10.10.10.3       20           
27        12773                 permanent     vxlan48     25           00:00:00:00:00:00  10.10.10.2       20           
28        12773                 permanent     vxlan48     25           00:00:00:00:00:00  10.10.10.4       20           
29        12773                 permanent     vxlan48     41           00:00:00:00:00:00  10.10.10.3       30           
30        12773                 permanent     vxlan48     41           00:00:00:00:00:00  10.10.10.2       30           
31        12773                 permanent     vxlan48     41           00:00:00:00:00:00  10.10.10.4       30           
32        12773                 permanent     vxlan48     47           00:00:00:00:00:00  10.10.10.3       10           
33        12773                 permanent     vxlan48     47           00:00:00:00:00:00  10.10.10.2       10           
34        12773                 permanent     vxlan48     47           00:00:00:00:00:00  10.10.10.4       10           
35        12773                 extern_learn  vxlan48     12773        44:38:39:22:01:8a  10.10.10.4       20           
36        12562  br_default     static        bond2       12562        48:b0:2d:ac:01:da                            20  
37        21     br_default     static        bond2       12556        48:b0:2d:8f:4b:ff                            20  
38        12777  br_default     permanent     bond2       12777        48:b0:2d:f9:41:f5                                
39        12562  br_default     static        bond3       12562        48:b0:2d:2d:8b:15                            30  
40        21     br_default     static        bond3       12566        48:b0:2d:56:1a:96                            30
...
```

The following example output for the `net show neighbor` command shows:

- 10.1.10.101 is a locally attached host server01 on VLAN 10. Interface `vlan10-v0` is the virtual VRR address for VLAN10.
- 10.1.10.104 is remote-host, server04 on VLAN10. The STATE `zebra` shows that it is an EVPN learned entry. Use `net show bridge macs` to see information about which VTEP the host is behind.
- 10.1.20.105 is remote-host, server05 on VLAN 20.

```
cumulus@leaf01:mgmt:~$ net show neighbor
Neighbor                   MAC                Interface      AF    STATE
-------------------------  -----------------  -------------  ----  ---------
10.1.10.104                68:0f:31:ae:3d:7a  vlan10         IPv4  zebra
10.1.10.101                26:76:e6:93:32:78  vlan10-v0      IPv4  REACHABLE
169.254.0.1                c0:8a:e6:03:96:d0  peerlink.4094  IPv4  zebra
10.0.1.2                   44:38:39:be:ef:bb  vlan4001       IPv4  zebra
169.254.0.1                c0:99:6b:c0:e1:ca  swp52          IPv4  zebra
10.1.20.3                  c0:8a:e6:03:96:d0  vlan20         IPv4  PERMANENT
169.254.0.1                ac:56:f0:f3:59:0c  swp54          IPv4  zebra
10.1.20.105                12:15:9a:9c:f2:e1  vlan20         IPv4  zebra
169.254.0.1                2c:f3:45:f4:6f:5f  swp53          IPv4  zebra
192.168.200.1              12:72:bc:4c:e1:83  eth0           IPv4  REACHABLE
169.254.0.1                f0:08:5f:12:cc:8c  swp51          IPv4  zebra
192.168.200.250            44:38:39:00:01:80  eth0           IPv4  REACHABLE
10.1.30.3                  c0:8a:e6:03:96:d0  vlan30         IPv4  PERMANENT
192.168.200.2              02:7a:19:45:66:48  eth0           IPv4  STALE
10.1.10.101                26:76:e6:93:32:78  vlan10         IPv4  REACHABLE
10.1.10.3                  c0:8a:e6:03:96:d0  vlan10         IPv4  PERMANENT
...
```

The following command shows the VLAN to VNI mapping for all bridges:

```
cumulus@switch:mgmt:~$ nv show bridge vlan-vni-map
br_default  VLAN-VNI-Offset: None 

VLAN  VNI
----  -----   
10    10  
20    20  
30    30  

br1   VLAN-VNI-Offset: None 

VLAN  VNI     
----  -----   
40   40   
50   50
```

The following command shows the VLAN to VNI mapping for a specific bridge:

```
cumulus@switch:mgmt:~$ nv show bridge domain br_default vlan-vni-map
br_default  VLAN-VNI-Offset: None 

VLAN  VNI
----  -----   
10    10
20    20   
30    30   
```

## General BGP Commands

If you use BGP for the underlay routing, run the vtysh `show bgp summary` command or the `net show bgp summary` command to view a summary of the layer 3 fabric connectivity:

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

Run the vtysh `show ip route` command or the `net show route` command to examine the underlay routing and determine how the switch reaches remote VTEPs. The following example shows output from a leaf switch:
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

Run the vtysh `show bgp l2vpn evpn summary` command or the `net show bgp l2vpn evpn summary` command to see the BGP peers participating in the EVPN address family and their states. The following example output from a leaf switch shows eBGP peering with four spine switches to exchange EVPN routes; all peering sessions are in the *established* state.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show bgp l2vpn evpn summary
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 0
RIB entries 23, using 4416 bytes of memory
Peers 4, using 85 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor        V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
spine01(swp51)  4      65199       958       949        0    0    0 00:44:46           34
spine02(swp52)  4      65199       958       949        0    0    0 00:44:46           34
spine03(swp53)  4      65199       958       949        0    0    0 00:44:46           34
spine04(swp54)  4      65199       958       949        0    0    0 00:44:46           34

Total number of neighbors 4
```

## Show EVPN VNIs

To display the configured VNIs on a network device participating in BGP EVPN, run the vtysh `show bgp l2vpn evpn vni` command. This command is only relevant on a VTEP. For symmetric routing, this command displays the special layer 3 VNIs for each tenant VRF.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
leaf01# show bgp l2vpn evpn vni
Advertise Gateway Macip: Disabled
Advertise SVI Macip: Disabled
Advertise All VNI flag: Enabled
BUM flooding: Head-end replication
Number of L2 VNIs: 3
Number of L3 VNIs: 2
Flags: * - Kernel
  VNI        Type RD                    Import RT                 Export RT                 Tenant VRF
* 20         L2   10.10.10.1:4          65101:20                  65101:20                 RED
* 30         L2   10.10.10.1:6          65101:30                  65101:30                 BLUE
* 10         L2   10.10.10.1:3          65101:10                  65101:10                 RED
* 4002       L3   10.1.30.2:2           65101:4002                65101:4002               BLUE
* 4001       L3   10.1.20.2:5           65101:4001                65101:4001               RED
```

Run the vtysh `show evpn vni` command to see a summary of all VNIs and the number of MAC or ARP entries associated with each VNI.

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show evpn vni
VNI        Type VxLAN IF              # MACs   # ARPs   # Remote VTEPs  Tenant VRF
20         L2   vni20                 8        5        1               RED
30         L2   vni30                 8        4        1               BLUE
10         L2   vni10                 8        6        1               RED
4001       L3   vniRED                1        1        n/a             RED
4002       L3   vniBLUE               0        0        n/a             BLUE
```

You can also show the above information with the NVUE `nv show evpn vni` and `nv show vrf <vrf> evpn vni` commands.

Run the NVUE `nv show evpn vni <vni>` command or the vtysh `show evpn vni <vni>` command to examine EVPN information for a specific VNI in detail. The following example output shows details for the layer 2 VNI 10. The output shows the remote VTEPs that contain that VNI.

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10
                   operational  applied
-----------------  -----------  -------
route-advertise                        
  default-gateway  off                 
  svi-ip           off                 
[remote-vtep]      10.10.10.2          
[remote-vtep]      10.10.10.3          
[remote-vtep]      10.10.10.4          
bridge-domain      br_default          
host-count         4                   
local-vtep         10.10.10.1          
mac-count          8                   
remote-vtep-count  3                   
tenant-vrf         RED                 
vlan               10                  
vxlan-interface    vxlan48
```

To show VNI BGP information run the NVUE `nv show evpn vni <id> bgp-info` and `nv show vrf <vrf_id> evpn bgp-info` commands, or the vtysh `show bgp l2vpn evpn vni <vni>` command.

```
cumulus@border01:mgmt:~$ nv show vrf RED evpn bgp-info
                       operational        applied
---------------------  -----------------  -------
local-vtep             10.0.1.255                
rd                     10.10.10.63:3             
router-mac             44:38:39:be:ef:ff         
system-ip              10.10.10.63               
system-mac             44:38:39:22:01:74         
[export-route-target]  65253:4001                
[import-route-target]  65253:4001
```

## Examine Local and Remote MAC Addresses for a VNI

Run the NVUE `nv show evpn vni <vni> mac` command or the vtysh `show evpn mac vni <vni>` command to examine all local and remote MAC addresses for a VNI. This command is only relevant for a layer 2 VNI:

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 mac                                                                               
LocMobSeq - local mobility sequence, RemMobSeq - remote mobility sequence,       
RemoteVtep - Remote Vtep address, Esi - Remote Esi                               
                                                                                 
MAC address        Type    State  LocMobSeq  RemMobSeq  Interface  RemoteVtep  Esi
-----------------  ------  -----  ---------  ---------  ---------  ----------  ---
44:38:39:22:01:7a  local          0          0          vlan10                    
44:38:39:22:01:8a  remote         0          0                     10.0.1.34      
44:38:39:22:01:84  remote         0          0                     10.0.1.34      
48:b0:2d:0c:a9:f4  remote         0          0                     10.0.1.12      
48:b0:2d:3a:a3:38  local          1408       1407       bond1                     
48:b0:2d:d2:ac:68  remote         0          0                     10.0.1.34      
48:b0:2d:eb:26:6e  remote         1          0                     10.0.1.34      
```

Run the vtysh `show evpn mac vni all` command or the `net show evpn mac vni all` command to examine MAC addresses for all VNIs.

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

Run the vtysh `show evpn arp-cache vni <vni>` command or the `net show evpn arp-cache vni <vni>` command to examine all local and remote neighbors (ARP entries) for a VNI. This command is only relevant for a layer 2 VNI and the output shows both IPv4 and IPv6 neighbor entries:

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

Run the vtysh `show evpn arp-cache vni all` command or the `net show evpn arp-cache vni all` command to examine neighbor entries for all VNIs.

## Examine Remote Router MAC Addresses

To examine the router MAC addresses corresponding to all remote VTEPs for symmetric routing, run the NVUE `nv show vrf <vrf> evpn remote-router-mac` command or the vtysh `show evpn rmac vni all` command. This command is only relevant for a layer 3 VNI:

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

To examine the gateway next hops for symmetric routing, run the NVUE `nv show vrf <vrf> evpn nexthop-vtep` command or the vtysh `show evpn next-hops vni all` command. This command is only relevant for a layer 3 VNI. The gateway next hop IP addresses correspond to the remote VTEP IP addresses. Cumulus Linux installs the remote host and prefix routes using these next hops.

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

To show the router MAC address for a specific next hop, run the NVUE `nv show vrf <vrf> evpn nexthop-vtep <ip-address>` command:

```
cumulus@leaf01:mgmt:~$ nv show vrf RED evpn nexthop-vtep 10.10.10.2
            operational        applied
----------  -----------------  -------
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

To show access VLANs on the switch and their corresponding VNI, run the NVUE `nv show evpn access-vlan-info vlan` command or the vtysh `show evpn access-vlan` command.

```
cumulus@border01:mgmt:~$ nv show evpn access-vlan-info vlan
Vlan-id  member-interface-count  vni  vni-count  vxlan-interface  Summary                
-------  ----------------------  ---  ---------  ---------------  -----------------------
10       1                       10   1          vxlan48          member-interface: bond1
20       1                       20   1          vxlan48          member-interface: bond2
30       1                       30   1          vxlan48          member-interface: bond3
220                                   1          vxlan99                                 
297                                   1          vxlan99      
```

You can drill down and show information about a specific vlan with the `nv show evpn access-vlan-info vlan <vlan>` command.

## Show the VRF Routing Table in FRR

Run the vtysh `show ip route vrf <vrf-name>` command or the `net show route vrf <vrf-name>` command to examine the VRF routing table. Use this command for symmetric routing to verify that remote host and prefix routes are in the VRF routing table and point to the appropriate gateway next hop.

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

In the output above, EVPN specifies the next hops for these routes to be *onlink*, or reachable over the specified SVI. This is necessary because this interface does not need to have an IP address. Even if the interface has an IP address, the next hop is not on the same subnet as it is typically the IP address of the remote VTEP (part of the underlay IP network).

## Show the Global BGP EVPN Routing Table

Run the vtysh `show bgp l2vpn evpn route` command or the `net show bgp l2vpn evpn route` command to display all EVPN routes, both local and remote. Cumulus Linux bases the routes on the RD as they are across VNIs and VRFs:

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

## Show a Specific EVPN Route

To drill down on a specific route for more information, run the vtysh `show bgp l2vpn evpn route rd <rd-value>` command or the `net show bgp l2vpn evpn route rd <rd-value>` command. This command displays all EVPN routes with that RD and with the path attribute details for each path. Additional filtering is possible based on route type or by specifying the MAC and/or IP address. The following example shows the specific MAC/IP route of server05. The output shows that this remote host is behind VTEP 10.10.10.3 and is reachable through four paths; one through each spine switch. This example is from a symmetric routing configuration, so the route shows both the layer 2 VNI (20) and the layer 3 VNI (4001), as well as the EVPN route target attributes corresponding to each and the associated router MAC address.

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

## Show the VNI EVPN Routing Table

The switch maintains the received EVPN routes in the global EVPN routing table (described above), even if there are no appropriate local VNIs to **import** them into. For example, a spine maintains the global EVPN routing table even though there are no VNIs present in the table. When local VNIs are present, the switch imports received EVPN routes into the per-VNI routing tables according to the route target attributes. You can examine the per-VNI routing table with the vtysh `show bgp vni <vni>` command:

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

To view the EVPN RIB with NVUE, run the `nv show vrf <vrf> router bgp address-family l2vpn-evpn loc-rib rd <rd> route-type <type> route` command.

## Show the VRF BGP Routing Table

For symmetric routing, the switch imports received type-2 and type-5 routes into the VRF routing table (according to address family: IPv4 unicast or IPv6 unicast) based on a match on the route target attributes. To examine the BGP VRF routing table, run the vtysh `show bgp vrf <vrf-name> ipv4 unicast` and `show bgp vrf <vrf-name> ipv6 unicast` command. You can also run the `net show bgp vrf <vrf-name> ipv4 unicast` command or the `net show bgp vrf <vrf-name> ipv6 unicast` command.

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

To show that the neighbor table includes the EVPN arp-cache and that the IPv6-MAC entry belongs to a router, run the vtysh `show evpn arp-cache vni <vni> ip <address>` command or the `net show evpn arp-cache vni <vni> ip <address>` command. For example:

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

The first time a MAC moves from behind one VTEP to behind another, BGP associates a MAC Mobility (MM) extended community attribute of sequence number 1, with the type-2 route for that MAC. From there, each time this MAC moves to a new VTEP, the MM sequence number increments by 1. You can examine the MM sequence number associated with a MAC's type-2 route with the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac>` command or the `net show bgp l2vpn evpn route vni <vni> mac <mac>` command. The example output below shows the type-2 route for a MAC that has moved three times:

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

You can identify static or *sticky* MACs in EVPN by the presence of `MM:0, sticky MAC` in the Extended Community line of the output from the vtysh `show bgp l2vpn evpn route vni <vni> mac <mac>` command or the `net show bgp l2vpn evpn route vni <vni> mac <mac>` command.

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
