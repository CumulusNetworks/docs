---
title: View Routing Tables
author: NVIDIA
weight: 795
toc: 3
---

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

To show the total number of routes in the routing table, run the `nv show vrf <vrf-id> router rib <address-family> route-count` command:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route-count
                 operational 
------------     ----------- 
total-routes    34 
[protocol]      bgp 
[protocol]      connected 
```

For IPv6 run the `nv show vrf <vrf-id> router rib ipv6 route-count` command.

To show the total number of routes per protocol in the routing table, run the `nv show vrf <vrf-id> router rib <address-family> route-count protocol` command:

```
cumulus@switch:~$ nv show vrf default router rib ipv4 route-count protocol
Protocol   Total 
---------  ----- 
bgp        6 
connected  3 
ospf       8 
static     3 
```

For IPv6 run the `nv show vrf <vrf-id> router rib ipv6 route-count protocol` command.

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
```

To show only IPv4 FIB table entries for a VRF, run the `nv show vrf <vrf-id> router fib ipv4` command.

```
cumulus@leaf01:~$ nv show vrf BLUE router fib ipv4
```

To show only IPv6 FIB table entries for a VRF, run the `nv show vrf <vrf-id> router fib ipv6` command.

```
cumulus@leaf01:~$ nv show vrf BLUE router fib ipv6
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
cumulus@leaf01:~$ nv show vrf RED router fib ipv6 route 228:35::0/64
```

{{%notice note%}}
- Command output does not show the members of a next hop group or the resolved details of a next hop. To show this information, run the `nv show router nexthop rib <nhid>` command.
- SRv6 routes only show the next hop ID.
- Downstream VNI routes only show the gateway and source.
- If the same prefix is present multiple times in the kernel FIB, the command output only shows the first match.
{{%/notice%}}

## Next Hop Tracking

Routing daemons track the validity of next hops through notifications from the `zebra` daemon. For example, FRR uninstalls BGP routes that resolve to a next hop over a connected route in `zebra` when `bgpd` receives a next hop tracking (NHT) notification after `zebra` removes the connected route if the associated interface goes down.

The `zebra` daemon does not consider next hops that resolve to a default route as valid by default. You can configure NHT to consider a longest prefix match lookup for next hop addresses resolving to the default route as a valid next hop. The following example configures the default route to be valid for NHT in the default VRF:

{{< tabs "410">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set vrf default router nexthop-tracking ipv4 resolved-via-default on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf01# configure terminal
leaf01(config)# ip nht resolve-via-default
leaf01(config)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

You can apply a route map to NHT for specific routing daemons to permit or deny routes from consideration as valid next hops. The following example applies `ROUTEMAP1` to BGP, preventing NHT from considering next hops resolving to 10.0.0.0/8 in the default VRF as valid:

{{< tabs "436">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv set router policy prefix-list PREFIX1 type ipv4
cumulus@leaf01:~$ nv set router policy prefix-list PREFIX1 rule 1 match 10.0.0.0/8
cumulus@leaf01:~$ nv set router policy prefix-list PREFIX1 rule 1 action permit
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 1 match ip-prefix-list PREFIX1
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 1 action deny 
cumulus@leaf01:~$ nv set router policy route-map ROUTEMAP1 rule 2 action permit
cumulus@leaf01:~$ nv set vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 protocol bgp
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
leaf02# configure terminal
leaf02(config)# ip prefix-list PREFIX1 seq 1 permit 10.0.0.0/8
leaf02(config)# route-map ROUTEMAP1 deny 1
leaf02(config-route-map)#  match ip address prefix-list PREFIX1
leaf02(config-route-map)# route-map ROUTEMAP1 permit 2
leaf02(config-route-map)# ip nht bgp route-map ROUTEMAP1
leaf02(config)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

You can show tracked next hops with the following NVUE commands:
- `nv show vrf <vrf-id> router nexthop-tracking ipv4`
- `nv show vrf <vrf-id> router nexthop-tracking ipv4 <ip-address>`
- `nv show vrf <vrf-id> router nexthop-tracking ipv6`
- `nv show vrf <vrf-id> router nexthop-tracking ipv6 <ip-address>`

```
cumulus@leaf01:~$  nv show vrf default router nexthop-tracking ipv4
                      operational  applied  pending
--------------------  -----------  -------  -------
resolved-via-default                        on

route-map
============
No Data

ip-address
=============
                                                                                
    DirectlyConnected - Indicates if nexthop is directly connected or not,          
    ResolvedProtocol - Resolved via protocol, Interface - Resolved via interface,   
    ProtocolFiltered - Indicates whether protocol filtered or not, Flags - o -      
    onlink, c - directly-connected, A - active                                      
                                                                                
    IPAddress    DirectlyConnected  ResolvedProtocol  Interface      VRF      Weight  ProtocolFiltered  Flags
    -----------  -----------------  ----------------  -------------  -------  ------  ----------------  -----
    10.0.1.34    off                bgp               swp52          default  1       off               A    
                                                      swp53          default  1                         A    
                                                      swp54          default  1                         A    
                                                      swp51          default  1                         A    
    10.10.10.2   off                bgp               peerlink.4094  default  1       off               A    
    10.10.10.3   off                bgp               swp52          default  1       off               A    
                                                      swp53          default  1                         A    
                                                      swp54          default  1                         A    
                                                      swp51          default  1                         A    
    10.10.10.4   off                bgp               swp52          default  1       off               A    
                                                      swp53          default  1                         A    
                                                      swp54          default  1                         A    
                                                      swp51          default  1                         A    
    10.10.10.63  off                bgp               swp52          default  1       off               A    
                                                      swp53          default  1                         A    
                                                      swp54          default  1                         A    
                                                      swp51          default  1                         A    
    10.10.10.64  off                bgp               swp52          default  1       off               A    
                                                      swp53          default  1                         A    
                                                      swp54          default  1                         A    
                                                      swp51          default  1                         A
```

You can also run the vtysh `show ip nht vrf <vrf-id> <ip-address>` command.
