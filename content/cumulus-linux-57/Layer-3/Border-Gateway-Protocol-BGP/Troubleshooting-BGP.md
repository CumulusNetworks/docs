---
title: Troubleshooting BGP
author: NVIDIA
weight: 870
toc: 3
---
Use the following commands to troubleshoot BGP.

## Basic Troubleshooting Commands

Run the following commands to help you troubleshoot BGP.

## Show BGP configuration Summary

To show a summary of the BGP configuration on the switch, run the vtysh `show ip bgp summary` command. For example:

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip bgp summary
ipv4 Unicast Summary
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 88
RIB entries 25, using 4800 bytes of memory
Peers 5, using 106 KiB of memory
Peer groups 1, using 64 bytes of memory

Neighbor              V         AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
spine01(swp51)        4      65199     31122     31194        0    0    0 1d01h44m            7
spine02(swp52)        4      65199     31060     31151        0    0    0 01:47:13            7
spine03(swp53)        4      65199     31150     31207        0    0    0 01:48:31            7
spine04(swp54)        4      65199     31042     31098        0    0    0 01:46:57            7
leaf02(peerlink.4094) 4      65101     30919     30913        0    0    0 01:47:43           12

Total number of neighbors 5
```

To view the routing table as defined by BGP, run the vtysh `show ip bgp ipv4 unicast` command or the `net show bgp ipv4 unicast` command. For example:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast
GP table version is 88, local router ID is 10.10.10.1, vrf id 0
Default local pref 100, local AS 65101
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop            Metric LocPrf Weight Path
* i10.0.1.1/32      peerlink.4094            0    100      0 ?
*>                  0.0.0.0                  0         32768 ?
*= 10.0.1.2/32      swp54                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
* i                 peerlink.4094                 100      0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
*= 10.0.1.254/32    swp54                                  0 65199 65132 ?
*=                  swp52                                  0 65199 65132 ?
* i                 peerlink.4094                 100      0 65199 65132 ?
*=                  swp53                                  0 65199 65132 ?
*>                  swp51                                  0 65199 65132 ?
*> 10.10.10.1/32    0.0.0.0                  0         32768 ?
*>i10.10.10.2/32    peerlink.4094            0    100      0 ?
*= 10.10.10.3/32    swp54                                  0 65199 65102 ?
*=                  swp52                                  0 65199 65102 ?
* i                 peerlink.4094                 100      0 65199 65102 ?
*=                  swp53                                  0 65199 65102 ?
*>                  swp51                                  0 65199 65102 ?
...
```

To show a more detailed breakdown of a specific neighbor, run the vtysh `show ip bgp neighbor <neighbor>` command or the NVUE `nv show vrf <vrf> router bgp neighbor <neighbor>` command:

```
cumulus@switch:~$ nv show vrf default router bgp neighbor swp51
                               operational                applied   
-----------------------------  -------------------------  ----------
description                                               none      
enforce-first-as                                          off       
multihop-ttl                                              auto      
nexthop-connected-check                                   on        
passive-mode                                              off       
password                                                  none      
address-family                                                      
  ipv4-unicast                                                      
    enable                                                on        
    add-path-tx                                           off       
    nexthop-setting                                       auto      
    route-reflector-client                                off       
    route-server-client                                   off       
    soft-reconfiguration                                  off       
    aspath                                                          
      private-as                                          none      
      replace-peer-as                                     off       
      allow-my-asn                                                  
        enable                                            off       
    attribute-mod                                                   
      aspath                   off                        on        
      med                      off                        on        
      nexthop                  off                        on        
...
```

To see details of a specific route, such as its source and destination, run the vtysh `show ip bgp <route>` command or the `net show bgp <route>` command.

```
cumulus@switch:~$ sudo vtysh
...
switch# show ip bgp 10.10.10.3/32
GP routing table entry for 10.10.10.3/32
Paths: (5 available, best #5, table default)
  Advertised to non peer-group peers:
  spine01(swp51) spine02(swp52) spine03(swp53) spine04(swp54) leaf02(peerlink.4094)
  65199 65102
    fe80::8e24:2bff:fe79:7d46 from spine04(swp54) (10.10.10.104)
    (fe80::8e24:2bff:fe79:7d46) (used)
      Origin incomplete, valid, external, multipath
      Last update: Wed Oct  7 13:13:13 2020
  65199 65102
    fe80::841:43ff:fe27:caf from spine02(swp52) (10.10.10.102)
    (fe80::841:43ff:fe27:caf) (used)
      Origin incomplete, valid, external, multipath
      Last update: Wed Oct  7 13:13:14 2020
  65199 65102
    fe80::90b1:7aff:fe00:3121 from leaf02(peerlink.4094) (10.10.10.2)
      Origin incomplete, localpref 100, valid, internal
      Last update: Wed Oct  7 13:13:08 2020
  65199 65102
    fe80::48e7:fbff:fee9:5bcf from spine03(swp53) (10.10.10.103)
    (fe80::48e7:fbff:fee9:5bcf) (used)
      Origin incomplete, valid, external, multipath
      Last update: Wed Oct  7 13:13:13 2020
  65199 65102
    fe80::7c41:fff:fe93:b711 from spine01(swp51) (10.10.10.101)
    (fe80::7c41:fff:fe93:b711) (used)
      Origin incomplete, valid, external, multipath, bestpath-from-AS 65199, best (Older Path)
      Last update: Wed Oct  7 13:13:13 2020
```

## Check BGP Timer Settings

To check BGP timers, such as the BGP keepalive interval, hold time, and advertisement interval, run the NVUE `nv show vrf default router bgp neighbor <neighbor> timers` command or the vtysh `show ip bgp neighbor <peer>` command. For example:

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 timers
                     operational  applied
-------------------  -----------  -------
connection-retry     10           auto   
hold                 9000         auto   
keepalive            3000         auto   
route-advertisement               auto
```

## BGP Update Groups

You can show information about update group events or information about a specific IPv4 or IPv6 update group.

To show information about update group events, run the vtysh `show bgp update-group` command or run these NVUE commands:
- `nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group` for IPv4
- `nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast update-group
   Time created  LocalAs change  Prepend Flag  Replace AS flag  Minimum advertisement interval  Routemap  Update group  Summary     
-  ------------  --------------  ------------  ---------------  ------------------------------  --------  ------------  ------------
5  1674253324                                                   0                                         5             sub-group: 5               
```

To show information about a specific update group, such as the number of peer refresh events, prune events, and packet queue length, run the vtysh `show bgp update-group <group-id>` command or run these NVUE commands:
- `nv show vrf <vrf-id> router bgp address-family ipv4-unicast update-group <group-id> -o json` for IPv4
- `nv show vrf <vrf-id> router bgp address-family ipv6-unicast update-group <group-id> -o json` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 1 -o json
{
  "create-time": 1682551552,
  "min-route-advertisement-interval": 0,
  "sub-group": {
    "1": {
      "adjacency-count": 6,
      "coalesce-time": 1100,
      "counters": {
        "join-events": 2,
        "merge-check-events": 0,
        "merge-events": 1,
        "peer-refresh-events": 0,
        "prune-events": 0,
        "split-events": 0,
        "switch-events": 0
      },
      "create-time": 1682551552,
      "needs-refresh": "off",
      "neighbor": {
        "swp51": {},
        "swp52": {}
      },
      "packet-counters": {
        "queue-hwm-len": 4,
        "queue-len": 0,
        "queue-total": 9,
        "total-enqueued": 9
      },
      "sub-group-id": 1,
      "version": 9
    }
  },
  "update-group-id": "1"
}
```

## Show BGP Route Information

You can run NVUE commands to show route statistics for a BGP neighbor, such as the number of routes, and information about advertised and received routes.

To show the route count, run the following NVUE commands:
- `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast route-counters` for IPv4.
- `nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast route-counters` for IPv6.

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast route-counters
               operational  applied
--------------  -----------  -------
adj-rib-in      0                   
all-rib         8                   
best-routes     2                   
damped          0                   
history         0                   
removed         0                   
route-count     8                   
routes-counted  8                   
stale           0                   
usable          8                   
valid           8
```

To show all the advertised routes, run these commands:
- `nv show vrf default router bgp neighbor swp1 address-family ipv4-unicast advertised-routes -o json` for IPv4 
- `nv show vrf default router bgp neighbor swp1 address-family ipv6-unicast advertised-routes -o json` for IPv6

To show information about a specific advertised route, run these commands:
- `nv show vrf default router bgp neighbor swp1 address-family ipv4-unicast advertised-routes <route> -o json` for IPv4
- `nv show vrf default router bgp neighbor swp1 address-family ipv6-unicast advertised-routes <route> -o json` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes -o json
{
  "10.10.10.1/32": {
    "path": {
      "1": {
        "aspath": {},
        "bestpath": {
          "overall": "on",
          "selection-reason": "First path received"
        },
        "flags": {},
        "last-update": 1682551550,
        "metric": 0,
        "nexthop": {
          "1": {
            "accessible": "on",
            "afi": "ipv4",
            "ip": "0.0.0.0",
            "metric": 0,
            "used": "on"
          }
        },
        "nexthop-count": 1,
        "origin": "incomplete",
        "peer": {
          "id": "0.0.0.0",
          "router-id": "10.10.10.1"
        },
        "sourced": "on",
        "valid": "on",
        "weight": 32768
      }
    }
  },
  "10.10.10.101/32": {
    "path": {
      "1": {
        "aspath": {
          "65199": {}
...
```

To show all the received routes, run these commands:
- `nv show vrf default router bgp neighbor swp1 address-family ipv4-unicast received-routes -o json` for IPv4
- `nv show vrf default router bgp neighbor swp1 address-family ipv6-unicast received-routes -o json` for IPv6

To show information about a specific received route, run these commands:
- `nv show vrf default router bgp neighbor swp1 address-family ipv4-unicast received-routes <route> -o json` for IPv4
- `nv show vrf default router bgp neighbor swp1 address-family ipv6-unicast received-routes <route> -o json` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 -o json
```

## Show Next Hop Information

To show a summary of all the BGP IPv4 or IPv6 next hops, run the `nv show vrf <vrf> router bgp nexthop ipv4` or `nv show vrf <vrf> router bgp nexthop ipv6` command. The output shows the IGP metric, the number of paths pointing to a next hop, and the address or interface used to reach a next hop.

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4
Nexthops
===========
                                                                                 
    PathCnt - Number of paths pointing to this Nexthop, ResolvedVia - Resolved via   
    address or interface, Interface - Resolved via interface                         
                                                                                 
    Address      IGPMetric  Valid  PathCnt  ResolvedVia                Interface    
    -----------  ---------  -----  -------  -------------------------  -------------
    10.0.1.34    0          on     160      fe80::4ab0:2dff:fe60:910e  swp54        
                                            fe80::4ab0:2dff:fea7:7852  swp53        
                                            fe80::4ab0:2dff:fec8:8fb9  swp52        
                                            fe80::4ab0:2dff:feff:e147  swp51        
    10.10.10.2   0          on     15       fe80::4ab0:2dff:fe2d:495c  peerlink.4094
    10.10.10.3   0          on     15       fe80::4ab0:2dff:fe60:910e  swp54        
                                            fe80::4ab0:2dff:fea7:7852  swp53        
                                            fe80::4ab0:2dff:fec8:8fb9  swp52        
                                            fe80::4ab0:2dff:feff:e147  swp51        
    10.10.10.4   0          on     15       fe80::4ab0:2dff:fe60:910e  swp54        
                                            fe80::4ab0:2dff:fea7:7852  swp53        
                                            fe80::4ab0:2dff:fec8:8fb9  swp52        
                                            fe80::4ab0:2dff:feff:e147  swp51        
    10.10.10.63  0          on     15       fe80::4ab0:2dff:fe60:910e  swp54        
                                            fe80::4ab0:2dff:fea7:7852  swp53        
                                            fe80::4ab0:2dff:fec8:8fb9  swp52        
                                            fe80::4ab0:2dff:feff:e147  swp51        
    10.10.10.64  0          on     15       fe80::4ab0:2dff:fe60:910e  swp54        
                                            fe80::4ab0:2dff:fea7:7852  swp53        
                                            fe80::4ab0:2dff:fec8:8fb9  swp52        
                                            fe80::4ab0:2dff:feff:e147  swp51    
```

To show information about a specific next hop, run the vtysh `show bgp vrf default nexthop <ip-address> ` command or run these NVUE commands:
- `nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address <ip-address> -o json` for IPv4
- `nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address <ip-address> -o json` for IPv6

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 -o json
{
  "complete": "on",
  "igp-metric": 0,
  "last-update-time": 1681940481,
  "path": {
    "1": {
      "address-family": "l2vpn-evpn",
      "flags": {
        "damped": "off",
        "deterministic-med-selected": "on",
        "history": "off",
        "multipath": "off",
        "nexthop-self": "off",
        "removed": "off",
        "selected": "off",
        "stale": "off",
        "valid": "on"
      },
      "prefix": "[5]:[0]:[10.1.20.0/24]/352",
      "rd": "10.10.10.2:3",
      "vrf": "default"
    },
    "10": {
      "address-family": "l2vpn-evpn",
      "flags": {
        "damped": "off",
        "deterministic-med-selected": "off",
        "history": "off",
        "multipath": "off",
        "nexthop-self": "off",
        "removed": "off",
        "selected": "off",
        "stale": "off",
        "valid": "on"
      },
      "prefix": "[5]:[0]:[10.1.30.0/24]/352",
      "rd": "10.10.10.2:2",
      "vrf": "default"
    },
    "11": {
      "address-family": "l2vpn-evpn",
      "flags": {
        "damped": "off",
        "deterministic-med-selected": "off",
        "history": "off",
        "multipath": "off",
        "nexthop-self": "off",
        "removed": "off",
        "selected": "off",
        "stale": "off",
        "valid": "on"
      },
      "prefix": "[5]:[0]:[10.1.20.0/24]/352",
      "rd": "10.10.10.2:3",
      "vrf": "default"
    },
...
```

To show specific next hop path information, run these NVUE commands:
- `nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address <ip-address-id> path -o json` for IPv4
- `nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address <ip-address-id> path -o json` for IPv6

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 path -o json
{
  "1": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "on",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "off",
      "stale": "off",
      "valid": "on"
    },
    "prefix": "[5]:[0]:[10.1.20.0/24]/352",
    "rd": "10.10.10.2:3",
    "vrf": "default"
  },
  "10": {
    "address-family": "l2vpn-evpn",
    "flags": {
      "damped": "off",
      "deterministic-med-selected": "off",
      "history": "off",
      "multipath": "off",
      "nexthop-self": "off",
      "removed": "off",
      "selected": "off",
      "stale": "off",
      "valid": "on"
    },
    "prefix": "[5]:[0]:[10.1.30.0/24]/352",
    "rd": "10.10.10.2:2",
    "vrf": "default"
  },
...
```

To show through which address and interface BGP resolves a specific next hop, run these NVUE commands:
- `nv show vrf <vrf-id> router bgp nexthop ipv4 ip-address <ip-address-id> resolved-via` for IPv4
- `nv show vrf <vrf-id> router bgp nexthop ipv6 ip-address <ip-address-id> resolved-via` for IPv6

```
cumulus@leaf01:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.2 resolved-via
Nexthop                    interface
-------------------------  ---------
fe80::4ab0:2dff:fe20:ac25  swp51    
fe80::4ab0:2dff:fe93:d92d  swp52
```

## Troubleshoot BGP Unnumbered

To verify that FRR learns the neighboring link-local IPv6 address through the IPv6 neighbor discovery router advertisements on a given interface, run the vtysh `show interface <interface>` command or the `net show interface <interface>` command.

If you do not enable `ipv6 nd suppress-ra` on both ends of the interface, `Neighbor address(s):` shows the link-local address of the other end (the address that BGP uses when that interface uses BGP).

{{%notice note%}}
Cumulus Linux automatically enables IPv6 route advertisements (RAs) on an interface with IPv6 addresses. You do not need to run the `no ipv6 nd suppress-ra` command for BGP unnumbered.
{{%/notice%}}

```
cumulus@switch:~$ sudo vtysh
...
switch# show interface swp51
  Interface swp51 is up, line protocol is up
  Link ups:       0    last: (never)
  Link downs:     0    last: (never)
  PTM status: disabled
  vrf: default
  OS Description: leaf to spine
  index 8 metric 0 mtu 9216 speed 1000
  flags: <UP,BROADCAST,RUNNING,MULTICAST>
  Type: Ethernet
  HWaddr: 10:d8:68:d4:a6:81
  inet6 fe80::12d8:68ff:fed4:a681/64
  Interface Type Other
  protodown: off
  ND advertised reachable time is 0 milliseconds
  ND advertised retransmit interval is 0 milliseconds
  ND advertised hop-count limit is 64 hops
  ND router advertisements sent: 217 rcvd: 216
  ND router advertisements are sent every 10 seconds
  ND router advertisements lifetime tracks ra-interval
  ND router advertisement default router preference is medium
  Hosts use stateless autoconfig for addresses.
  Neighbor address(s):
  inet6 fe80::f208:5fff:fe12:cc8c/128
```

## Troubleshoot IPv4 Prefixes Learned with IPv6 Next Hops

To show IPv4 prefixes learned with IPv6 next hops, run the following commands.

The following examples show an IPv4 prefix learned from a BGP peer over an IPv6 session using IPv6 global addresses, but where the next hop installed by BGP is a link-local IPv6 address. This occurs when the session is directly between peers, and the BGP update for the prefix includes both link-local and global IPv6 addresses as next hops. If both global and link-local next hops exist, BGP prefers the link-local address for route installation.

```
cumulus@spine01:mgmt:~$ sudo vtysh
...
spine01# show ip bgp ipv4 unicast summary
BGP router identifier 10.10.10.101, local AS number 65199 vrf-id 0
BGP table version 3
RIB entries 3, using 576 bytes of memory
Peers 1, using 21 KiB of memory

Neighbor                   V      AS   MsgRcvd   MsgSent   TblVer  InQ OutQ  Up/Down State/PfxRcd
leaf01(2001:db8:2::a00:1) 4     65101       22        22        0    0    0  00:01:00           0

Total number of neighbors 1
```

```
cumulus@spine01:mgmt:~$ sudo vtysh
...
spine01# show ip bgp ipv4 unicast
BGP table version is 3, local router ID is 10.10.10.101, vrf id 0
Default local pref 100, local AS 65199
Status codes:  s suppressed, d damped, h history, * valid, > best, = multipath,
               i internal, r RIB-failure, S Stale, R Removed
Nexthop codes: @NNN nexthop's vrf id, < announce-nh-self
Origin codes:  i - IGP, e - EGP, ? - incomplete

   Network          Next Hop                Metric LocPrf Weight Path
   10.10.10.101/32   fe80::a00:27ff:fea6:b9fe      0     0   32768 i

Displayed  1 routes and 1 total paths
```

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show ip bgp ipv4 unicast 10.10.10.101/32
BGP routing table entry for 10.10.10.101/32
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  Leaf01(2001:db8:0002::0a00:1)
  3
    2001:db8:0002::0a00:1 from Leaf01(2001:db8:0002::0a00:1) (10.10.10.101)
    (fe80::a00:27ff:fea6:b9fe) (used)
      Origin IGP, metric 0, valid, external, bestpath-from-AS 3, best (First path received)
      AddPath ID: RX 0, TX 3
      Last update: Mon Oct 22 08:09:22 2018
```

The example output below shows the results of installing the route in the FRR RIB as well as the kernel FIB. The next hop installed in the FRR RIB is the link-local IPv6 address, which Cumulus Linux converts into an IPv4 link-local address, as required for installation into the kernel FIB.

```
cumulus@spine01:~$ sudo vtysh
...
spine01# show ip route 10.10.10.101/32
RIB entry for 10.10.10.101/32
===========================
Routing entry for 10.10.10.101/32
  Known via "bgp", distance 20, metric 0, best
  Last update 2d17h05m ago
  * fe80::a00:27ff:fea6:b9fe, via swp1

FIB entry for 10.10.10.101/32
===========================
10.10.10.101/32 via 10.0.1.0 dev swp1 proto bgp metric 20 onlink
```

If BGP learns an IPv4 prefix with only an IPv6 global next hop address (when it learns the route through a route reflector), the command output shows the IPv6 global address as the next hop value. The command also shows that it learns recursively through the link-local address of the route reflector. When you use a global IPv6 address as a next hop for route installation in the FRR RIB, the switch still converts it into an IPv4 link-local address for installation into the kernel.

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast summary
BGP router identifier 10.10.10.1, local AS number 65101 vrf-id 0
BGP table version 1
RIB entries 1, using 152 bytes of memory
Peers 1, using 19 KiB of memory

Neighbor             V AS MsgRcvd  MsgSent  TblVer  InQ  OutQ  Up/Down  State/PfxRcd
Spine01(2001:db8:0002::0a00:2) 4 1   74       68         0     0     0     00:00:45      1

Total number of neighbors 1
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast summary
  BGP table version is 1, local router ID is 10.10.10.1
  Status codes: s suppressed, d damped, h history, * valid, > best, = multipath,
                i internal, r RIB-failure, S Stale, R Removed
  Origin codes: i - IGP, e - EGP, ? - incomplete

Network          Next Hop    Metric LocPrf Weight Path
*>i10.1.10.0/24 2001:2:2::4       0    100      0    i

Displayed 1 routes and 1 total paths
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip bgp ipv4 unicast 10.10.10.101/32
BGP routing table entry for 10.10.10.101/32
Paths: (1 available, best #1, table default)
  Not advertised to any peer
  Local
  2001:2:2::4 from Spine01(2001:1:1::1) (10.10.10.104)
    Origin IGP, metric 0, localpref 100, valid, internal, bestpath-from-AS Local, best (First path received)
    Originator: 10.0.0.14, Cluster list: 10.10.10.111
    AddPath ID: RX 0, TX 5
    Last update: Mon Oct 22 14:25:30 2018
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip route 10.10.10.1/32
RIB entry for 10.10.10.1/32
===========================
Routing entry for 10.10.10.1/32
  Known via "bgp", distance 200, metric 0, best
  Last update 00:01:13 ago
  2001:2:2::4 (recursive)
  * fe80::a00:27ff:fe5a:84ae, via swp1

FIB entry for 10.10.10.1/32
===========================
10.10.10.1/32 via 10.0.1.1 dev swp1 proto bgp metric 20 onlink
```

To only use IPv6 global addresses for route installation into the FRR RIB, you must add an additional route map to the neighbor or peer group statement in the appropriate address family. When the route map command `set ipv6 next-hop prefer-global` applies to a neighbor, if both a link-local and global IPv6 address are in the BGP update for a prefix, BGP uses the IPv6 global address for route installation.

With this additional configuration, the output in the FRR RIB changes in the direct neighbor case as shown below:

```
router bgp 65101
  bgp router-id 10.10.10.1
  neighbor 2001:db8:2::a00:1 remote-as internal
  neighbor 2001:db8:2::a00:1 capability extended-nexthop
  !
  address-family ipv4 unicast
  neighbor 2001:db8:2::a00:1 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 20
  set ipv6 next-hop prefer-global
!
```

The resulting FRR RIB output is as follows:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
    O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
    T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
    F - PBR,
    > - selected route, * - FIB route

B 0.0.0.0/0 [200/0] via 2001:2:2::4, swp2, 00:01:00
K 0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 1d02h29m
C>* 10.0.0.9/32 is directly connected, lo, 5d18h32m
C>* 10.0.2.0/24 is directly connected, eth0, 03:51:31
B>* 172.16.4.0/24 [200/0] via 2001:2:2::4, swp2, 00:01:00ß
C>* 172.16.10.0/24 is directly connected, swp3, 5d18h32m
```

When the switch learns the route through a route reflector, it appears like this:

```
router bgp 65101
  bgp router-id 10.10.10.1
  neighbor 2001:db8:2::a00:2 remote-as internal
  neighbor 2001:db8:2::a00:2 capability extended-nexthop
  !
  address-family ipv6 unicast
  neighbor 2001:db8:2::a00:2 activate
  neighbor 2001:db8:2::a00:2 route-map GLOBAL in
  exit-address-family
!
route-map GLOBAL permit 10
  set ipv6 next-hop prefer-global
```

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# show ip route
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route

B   0.0.0.0/0 [200/0] via 2001:2:2::4, 00:00:01
K   0.0.0.0/0 [0/0] via 10.0.2.2, eth0, 3d00h26m
C>* 10.0.0.8/32 is directly connected, lo, 3d00h26m
C>* 10.0.2.0/24 is directly connected, eth0, 03:39:18
C>* 172.16.3.0/24 is directly connected, swp2, 3d00h26m
B>  172.16.4.0/24 [200/0] via 2001:2:2::4 (recursive), 00:00:01
  *                         via 2001:1:1::1, swp1, 00:00:01
C>* 172.16.10.0/24 is directly connected, swp3, 3d00h26m
```

## Neighbor State Change Log

Cumulus Linux records the changes that a neighbor goes through in `syslog` and in the `/var/log/frr/frr.log` file. For example:

```
020-10-05T15:51:32.621773-07:00 leaf01 bgpd[10104]: %NOTIFICATION: sent to neighbor peerlink.4094 6/7 (Cease/Connection collision resolution) 0 bytes
2020-10-05T15:51:32.623023-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor peerlink.4094(leaf02) in vrf default Up
2020-10-05T15:51:32.623156-07:00 leaf01 bgpd[10104]: %NOTIFICATION: sent to neighbor peerlink.4094 6/7 (Cease/Connection collision resolution) 0 bytes
2020-10-05T15:51:32.623496-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor peerlink.4094(leaf02) in vrf default Down No AFI/SAFI activated for peer
2020-10-05T15:51:33.040332-07:00 leaf01 bgpd[10104]: [EC 33554454] swp53 [Error] bgp_read_packet error: Connection reset by peer
2020-10-05T15:51:33.279468-07:00 leaf01 bgpd[10104]: [EC 33554454] swp52 [Error] bgp_read_packet error: Connection reset by peer
2020-10-05T15:51:33.339487-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp54(spine04) in vrf default Up
2020-10-05T15:51:33.340893-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp53(spine03) in vrf default Up
2020-10-05T15:51:33.341648-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp52(spine02) in vrf default Up
2020-10-05T15:51:33.342369-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor swp51(spine01) in vrf default Up
2020-10-05T15:51:33.627958-07:00 leaf01 bgpd[10104]: %ADJCHANGE: neighbor peerlink.4094(leaf02) in vrf default Up
```

## Clear BGP Routes

NVUE provides commands to clear and refresh routes in the BGP table. You can clear all routes in the BGP table or all routes for an address family (IPv4, IPv6, or EVPN) in a VRF.

The BGP clear commands do not clear counters in the kernel or hardware.

{{%notice note%}}
- BGP clear route commands that specify a direction (`in` or `out`) do not reset BGP neighbor adjacencies.
- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, performing a clear in or soft clear in clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured without the `soft-reconfiguration inbound` option enabled, performing a clear in or soft in sends the peer a route refresh message.
- Outbound BGP clear commands (either out or soft out) readvertise all routes to BGP peers.
- BGP soft clear commands that do not specify a direction (`in` or `out`) do not reset BGP neighbor adjacencies, and affect both inbound and outbound routes, as described above, depending on if you enable `soft-reconfiguration inbound`.
{{%/notice%}}

{{< tabs "742 ">}}
{{< tab "NVUE Commands ">}}

To clear and refresh all IPv4 inbound routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family ipv4-unicast soft in
```

To clear and resend all IPv6 outbound routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft out
```

To clear and refresh all EVPN inbound routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft in
```

To clear and resend all outbound IPv4 routes:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp address-family ipv4-unicast soft out
```

To clear and resend all IPv6 outbound routes to BGP neighbor 10.10.10.101:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp neighbor 10.10.10.101 address-family ipv6-unicast out
```

To clear and resend outbound routes for all address families (IPv4, IPv6, and l2vpn-evpn) for the BGP peer group SPINES:

```
cumulus@leaf01:~$ nv action clear vrf default router bgp peer-group SPINES out
```

To clear and refresh all IPv4 inbound routes for all VRFs and address families:

```
cumulus@switch:~$ nv action clear router bgp soft in
Action succeeded
```

To clear and refresh inbound routes for all neighbors, address families, and VRFs and to refresh the outbound route filtering prefix-list:

```
cumulus@switch:~$ nv action clear router bgp in prefix-filter
Action succeeded
```

To clear BGP sessions with all neighbors, forcing the neighbors to restart:

```
cumulus@switch:~$ nv action clear router bgp
Action succeeded
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To clear and refresh all IPv4 inbound routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv4 unicast * soft in
switch# exit
```

To clear and resend all IPv6 outbound routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv6 unicast * soft out
switch# exit
```

To clear and refresh all EVPN inbound routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default l2vpn evpn * soft in
switch# exit
```

To clear and resend all outbound IPv4 routes:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv4 unicast * soft out
switch# exit
```

To clear and resend all IPv6 outbound routes to BGP neighbor 10.10.10.101:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default ipv6 unicast 10.10.10.101 out
switch# exit
```

To clear and resend outbound routes for all address families (IPv4, IPv6, and l2vpn-evpn) for the BGP peer group SPINES:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp vrf default peer-group SPINES out
switch# exit
```

To clear and refresh inbound routes for all neighbors, address families, and VRFs and to refresh the outbound route filtering prefix-list:

```
cumulus@spine01:~$ sudo vtysh
...
switch# clear bgp in prefix-filter
switch# exit
```

To clear BGP sessions with all neighbors, forcing the neighbors to restart:

```
cumulus@switch:~$ sudo vtysh
...
switch# clear bgp *
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}
