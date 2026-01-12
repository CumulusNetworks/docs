---
title: Routing Tables
author: NVIDIA
weight: 795
toc: 3
---
Cumulus Linux provides commands to show route information in the routing table and FIB table entries.

## Show Routes in the Routing Table

To show all the routes in the routing table, run the `nv show vrf <vrf-id> router rib <address-family> route` command:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route

Flags - * - selected, q - queued, o - offloaded, i - installed, S - fib-        
selected, x - failed                                                            
                                                                                
Route            Protocol   Distance  Uptime                NHGId  Metric  Flags
---------------  ---------  --------  --------------------  -----  ------  -----
10.0.1.12/32     connected  0         0:42:54               15     0       *Sio 
10.0.1.34/32     bgp        20        0:42:54               125    0       *Si  
10.0.1.255/32    bgp        20        23:21:18              125    0       *Si  
10.10.10.1/32    connected  0         23:21:18              15     0       *Sio 
10.10.10.2/32    bgp        20        0:42:54               62     0       *Si  
10.10.10.3/32    bgp        20        0:42:54               125    0       *Si  
10.10.10.4/32    bgp        20        0:42:54               125    0       *Si  
10.10.10.63/32   bgp        20        0:42:54               125    0       *Si  
10.10.10.64/32   bgp        20        23:26:25              125    0       *Si  
10.10.10.101/32  bgp        20        23:26:25              115    0       *Si  
10.10.10.102/32  bgp        20        23:26:25              107    0       *Si
```

To show information about a specific route, run the `nv show vrf <vrf-id> router rib <address-family> route <prefix>` command:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route 10.0.1.34/32
route-entry
==============
                                                                                
    Protocol - Protocol name, TblId - Table Id, NHGId - Nexthop group Id, Flags - u 
    - unreachable, r - recursive, o - onlink, i - installed, d - duplicate, c -     
    connected, A - active                                                           
                                                                                
    EntryIdx  Protocol  TblId  NHGId  Distance  Metric  ResolvedVia                ResolvedViaIntf  Weight  Flags
    --------  --------  -----  -----  --------  ------  -------------------------  ---------------  ------  -----
    1         bgp       254    125    20        0       fe80::4ab0:2dff:fe32:2a3f  swp52            1       iA   
                                                        fe80::4ab0:2dff:fe41:6b79  swp51            1       iA
```

To show the total number of routes in the routing table, run the `nv show vrf <vrf-id> router rib ipv4 route-count` command or `nv show vrf <vrf-id> router rib ipv6 route-count` command:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route-count
                 operational 
------------     ----------- 
total-routes    34 
[protocol]      bgp 
[protocol]      connected 
```

To show the total number of routes per protocol in the routing table, run the `nv show vrf <vrf-id> router rib ipv4 route-count protocol` command or the `nv show vrf <vrf-id> router rib ipv6 route-count protocol` command:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route-count protocol
Protocol   Total 
---------  ----- 
bgp        6 
connected  3 
ospf       8 
static     3 
```

## Look Up the Route for a Destination

To look up the route in the routing table for a specific destination, run the `nv action lookup vrf <vrf-id> router fib <address-family> <ip-address>` command.

The following example looks up the route in the routing table for the destination with the IPv4 address 10.10.10.3:

```
cumulus@switch:~$ nv action lookup vrf default router fib ipv4 10.10.10.3
Action executing ...

dst: 10.10.10.4
nhid: 106
protocol: bgp
metric: 20
flags: []

id: 106
group: 62,102
protocol: zebra
flags: []

id: 62
gateway: fe80::4ab0:2dff:feff:6ac0
dev: swp52
scope: link
protocol: zebra
flags: []

id: 102
gateway: fe80::4ab0:2dff:fe8b:d6bf
dev: swp51
scope: link
protocol: zebra
flags: []

Action succeeded 
```

The following example shows the route in the routing table for the destination with the IPv6 address 228:35::5

```
cumulus@switch:~$ nv action lookup vrf default router fib ipv6 fe80::4ab0:2dff:fe8b:d6bf
Action executing ...

dst: fe80::/64
dev: br_default
protocol: kernel
metric: 256
flags: []
pref: medium

Action succeeded
```

## Show FIB Table Entries

You can show the IPv4 and IPv6 FIB table entries for a VRF and the FIB table entries by prefix for a VRF.

To show both IPv4 and IPv6 FIB table entries for a VRF, run the `nv show vrf <vrf-id> router fib` command:

```
cumulus@leaf01:~$ nv show vrf BLUE router fib
AFI   Prefix
----  ---------
ipv4  0.0.0.0/0
      10.1.10.0/24
      10.1.20.0/24
      10.1.30.0/24
      10.1.30.106/32
      127.0.0.0/8
ipv6  ::/0
      ::1/128
      fe80::/128
      fe80::/64
      ff00::/8
```

To show only IPv4 FIB table entries for a VRF, run the `nv show vrf <vrf-id> router fib ipv4` command.

```
cumulus@leaf01:~$ nv show vrf BLUE router fib ipv4
Prefix          Next-hop     Protocol  Scope   Summary
--------------  -----------  --------  ------  ------------------
0.0.0.0/0       unreachable  boot      global  Metric: 4278198272
10.1.10.0/24    nhid 460     bgp       global  Metric: 20
10.1.20.0/24    nhid 460     bgp       global  Metric: 20
10.1.30.0/24    dev vlan30   kernel    link    PrefSrc: 10.1.30.3
10.1.30.106/32  nhid 459     bgp       global  Metric: 20
127.0.0.0/8     dev BLUE     kernel    link    PrefSrc: 127.0.0.1
```

To show only IPv6 FIB table entries for a VRF, run the `nv show vrf <vrf-id> router fib ipv6` command.

```
cumulus@leaf01:~$ nv show vrf BLUE router fib ipv6
Prefix      Next-hop       Protocol  Scope   Summary
----------  -------------  --------  ------  ------------------
::/0        unreachable    boot      global  Metric: 4278198272
::1/128     dev BLUE       kernel    global  Metric: 256
fe80::/128  dev vlan30-v0  kernel    global  Metric: 0
fe80::/64   dev vlan30     kernel    global  Metric: 256
ff00::/8    dev vlan30     kernel    global  Metric: 256
```

To show IPv4 FIB table entries for a specific prefix in a VRF, run the `nv show vrf <vrf-id> router fib ipv4 route <prefix>` command.

```
cumulus@leaf01:~$ nv show vrf default router fib ipv4 route 10.10.10.1/32 

Prefix             Next-hop               Proto  Scope  Summary 
------------------ ---------------------- ------ ------ ----------------------- 
10.10.10.1/32      nhid 68                bgp    global Metric: 20
```

To show IPv6 FIB table entries for a specific prefix in a VRF, run the `nv show vrf <vrf-id> router fib ipv6 route <prefix>` command.

```
cumulus@leaf01:~$ nv show vrf RED router fib ipv6 route fe80::/64
Prefix     Next-hop    Protocol  Scope   Summary
---------  ----------  --------  ------  -----------
fe80::/64  dev vlan10  kernel    global  Metric: 256
```

{{%notice note%}}
- Command output does not show the members of a next hop group or the resolved details of a next hop. To show this information, run the `nv show router nexthop rib <nhid>` command.
- SRv6 routes only show the next hop ID.
- Downstream VNI routes only show the gateway and source.
- If the same prefix is present multiple times in the kernel FIB, the command output only shows the first match.
{{%/notice%}}
