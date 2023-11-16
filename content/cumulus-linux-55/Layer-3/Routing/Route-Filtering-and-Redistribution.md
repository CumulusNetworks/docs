---
title: Route Filtering and Redistribution
author: NVIDIA
weight: 750
toc: 3
---
Route filtering lets you exclude routes that neighbors advertise or receive. You can use route filtering to manipulate traffic flows, reduce memory utilization, and improve security.

This section discusses the following route filtering methods:
- Prefix lists
- Route maps
- Route redistribution

## Prefix Lists

Prefix lists are access lists for route advertisements that match routes instead of traffic. Prefix lists are typically used with route maps and other filtering methods. A prefix list can match the prefix (the network itself) and the prefix length (the length of the subnet mask).

The following example commands configure a prefix list that permits all prefixes in the range 10.0.0.0/16 with a subnet mask less than or equal to /30. For networks 10.0.0.0/24, 10.10.10.0/24, and 10.0.0.10/32, only 10.0.0.0/24 matches (10.10.10.0/24 has a different prefix and 10.0.0.10/32 has a greater subnet mask).

{{< tabs "TabID22 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router policy prefix-list prefixlist1 rule 1 match 10.0.0.0/16 max-prefix-len 30
cumulus@switch:~$ nv set router policy prefix-list prefixlist1 rule 1 action permit
cumulus@switch:~$ nv config apply
```

For IPv6, you need to run an additional command to set the prefix list type to IPv6. For example:

```
cumulus@switch:~$ nv set router policy prefix-list prefixlistipv6 type ipv6
cumulus@switch:~$ nv set router policy prefix-list prefixlistipv6 rule 1 match 2001:100::1/64
cumulus@switch:~$ nv set router policy prefix-list prefixlistipv6 rule 1 action permit 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# ip prefix-list prefixlist1 seq 1 permit 10.0.0.0/16 le 30
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
router ospf
 ospf router-id 10.10.10.1
 timers throttle spf 80 100 6000
 passive-interface vlan10
 passive-interface vlan20
ip prefix-list prefixlist1 seq 1 permit 10.0.0.0/16 le 30
```

{{< /tab >}}
{{< /tabs >}}

To use this prefix list in a route map called MAP1:

{{< tabs "TabID82 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 action permit
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match type ipv4
cumulus@switch:~$ nv set router policy route-map MAP1 rule 10 match ip-prefix-list prefixlist1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# route-map MAP1 permit 10
switch(config-route-map)# match ip address prefix-list prefixlist1
switch(config-route-map)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
ip prefix-list prefixlist1 seq 1 permit 10.0.0.0/16 le 30
route-map MAP1 permit 10
match ip address prefix-list prefixlist1
```

{{< /tab >}}
{{< /tabs >}}

## Route Maps

Route maps are routing policies that Cumulus Linux considers before the router examines the forwarding table. Each statement in a route map has a sequence number, and includes a series of match and set statements. The route map parses from the lowest sequence number to the highest, and stops when there is a match.

Cumulus Linux supports several match and set statements. For example, you can match on an interface, prefix length, next hop or BGP AS path list. You can set the BGP metric, local-preference on routes, source IP, or the tag on the matched route. For a list of supported match and set statements, see {{<link url="#match-and-set-statements" text="Match and Set Statements" >}} below.

### Configure a Route Map

To configure a route map:

1. Specify one or more conditions that must match and, optionally, one or more set actions to set or modify attributes of the route. If a route map does not specify any matching conditions, it always matches.
2. Specify the matching policy: permit (if the entry matches, carry out the set actions) or deny (if the entry matches, deny the route).

To apply the route map, see {{<link url="#apply-a-route-map" text="Apply a Route Map" >}} below.

The following example commands configure a route map that sets the BGP metric to 50 for interface swp51:

{{< tabs "TabID73 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 match interface swp51
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 set metric 50
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 action permit
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# route-map routemap1 permit 10
switch(config-route-map)# match interface swp51
switch(config-route-map)# set metric 50
switch(config-route-map)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
route-map routemap1 permit 10
 match interface swp51
 set metric 50
```

{{< /tab >}}
{{< /tabs >}}

The following example commands configure a route map to match the prefixes defined in `prefixlist1` and set the nexth hop to 10.10.10.5:

{{< tabs "TabID212 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 match ip-prefix-list prefixlist1
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 set ip-nexthop 10.10.10.5
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 action permit
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# route-map routemap1 permit 10
switch(config-route-map)# match ip route-source prefix-list prefixlist1
switch(config-route-map)# set ip next-hop 10.10.10.5
switch(config-route-map)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
route-map routemap1 permit 10
 match ip route-source prefix-list prefixlist1
 set ip next-hop 10.10.10.5
```

{{< /tab >}}
{{< /tabs >}}

The following example commands configure a route map to set the local-preference on routes to 400:

{{< tabs "TabID252 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router policy route-map routemap2 rule 10 set local-preference 400
cumulus@switch:~$ nv set router policy route-map routemap2 rule 10 action permit
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# route-map routemap2 permit 10
switch(config-route-map)# set local-preference 400
switch(config-route-map)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
route-map routemap2 permit 10
 set local-preference 400
```

{{< /tab >}}
{{< /tabs >}}

### Match and Set Statements

Cumulus Linux supports the following match and set statements.

{{%notice note%}}
You can use the following list of supported match and set statements with NVUE commands. For a list of the match and set statements that vtysh supports, see the {{<exlink url="https://docs.frrouting.org/en/latest/routemap.html?highlight=match" text="FRRouting User Guide">}}.
{{%/notice%}}

{{< tabs "TabID122 ">}}
{{< tab "Match Statements ">}}

| <div style="width:250px">Match        | Description|
| ------------ | ---------- |
| `as-path-list` | Matches the specified AS path list.|
| `interface` | Matches the specified interface. |
| `ip-prefix-len`| Matches the specified prefix length.  |
| `origin`| Matches the specified BGP origin. You can specify `egp`, `igp`, or `incomplete`. |
| `type`| Matches the specified route type, such as IPv4 or IPv6.|
| `community-list`| Matchest the specified community list. |
| `ip-nexthop` | Matches the specified next hop. |
| `ip-prefix-list`| Matches the specified prefix list.  |
| `peer` | Matches the specified BGP neighbor. |
| `evpn-default-route` | Matches the EVPN default route. You can specify `on` or `off`.|
| `ip-nexthop-len` | Matches the specified next hop prefix length. |
| `large-community-list` | Matches the specified large community list.|
| `source-protocol` |Matches the specified source protocol, such as BGP, OSPF or static. |
| `evpn-route-type` | Matches the specified EVPN route type. You can specify `macip`, `imet`, or `prefix`. |
| `ip-nexthop-list` | Matches the specified next hop list.|
| `local-preference` | Matches the specified local preference. You can specify a value between 0 and 4294967295. |
| `source-vrf` | Matches the specified source VRF. |
| `evpn-vni`| Matches the specified EVPN VNI. |
| `ip-nexthop-type`| Matches the specified next hop type, such as `blackhole`.|
| `metric`  | Matches the specified BGP metric. |
| `tag` | Matches the specified tag value associated with the route. You can specify a value between 1 and 4294967295.

{{%notice note%}}
The `source-protocol` match statement is only supported in {{<link url="FRRouting/#architecture" text="zebra">}}. Cumulus Linux does not support the `match source-protocol` statement in route maps configured for routing protocols such as BGP and OSPF.
{{%/notice%}}

{{< /tab >}}
{{< tab "Set Statements ">}}

| <div style="width:250px">Set          | Description|
| ------------ | ---------- |
| `aggregator-as` | Sets the aggregator AS. |
| `ext-community-rt` | Sets the BGP extended community RT.|
| `originator-id` | Sets the originator ID so that BGP choses the preferred path. |
| `as-path-exclude` | Sets BGP AS path exclude attribute to avoid considering the AS path during best path route selection. |
| `ext-community-soo` | Sets the BGP extended community Sight of Origin (SOO).|
| `large-community` |Sets the BGP large community. |
| `source-ip` | Sets the source IP address.|
| `as-path-prepend` | Sets the BGP AS path prepend attribute.|
| `forwarding-address` | Sets the route forwarding address.|
| `large-community-delete-list` | Sets the BGP large community delete list.|
| `tag` | Sets a tag on the matched route. You can specify a value between 1 and 4294967295. |
| `atomic-aggregate` | Sets the Atomic Aggregate attribute to inform BGP peers that the local router is using a less specific (aggregated) route to a destination. |
| `ip-nexthop` | Sets the BGP next hop. |
| `local-preference` | Sets the BGP local preference to `local_pref`. |
| `weight`  | Sets the route’s weight.|
| `community` | Sets the BGP community attribute.|
| `ipv6-nexthop-global`  | Sets the IPv6 next hop global attribute.|
| `metric` |  Sets the BGP attribute MED to a specific value. You can specify `metric-minus` to subtract the specified value from the MED,  `metric-plus` to add the specified value to the MED, `rtt` to set the MED to the round trip time, `rtt-minus` to subtract the round trip time from the MED, or `rtt-plus` to add the round trip time to the MED.|
| `community-delete-list`  | Sets the BGP community delete list. |
| `ipv6-nexthop-local`  |Sets the IPv6 next hop local attribute. |
| `metric-type` | Sets the metric type. You can specify `type-1` or `type-2`. |
| `ext-community-bw` | Sets the BGP extended community link bandwidth. |
| `ipv6-nexthop-prefer-global` | Sets IPv6 inbound routes to use the global address when both a global and link-local next hop is available.|
| `origin` | Sets the BGP route origin, such as eBGP or iBGP.|

{{< /tab >}}
{{< /tabs >}}

### Apply a Route Map

To apply the route map, you specify the routing protocol and the route map name.

The following example commands apply the route map called routemap2 to BGP neighbor swp51:

{{< tabs "TabID293 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound route-map routemap2
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp 65101
switch(config-router)# address-family ipv4 unicast 
switch(config-router-af)# neighbor swp51 route-map routemap2 in
switch(config-router-af)# end
switch# wr mem
Note: this version of vtysh never writes vtysh.conf
Building Configuration...
Integrated configuration saved to /etc/frr/frr.conf
[OK]
switch# exit
cumulus@switch:mgmt:~$ 
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
neighbor swp51 route-map routemap2 in
```

{{< /tab >}}
{{< /tabs >}}

The following example filters routes from Zebra (RIB) into the Linux kernel (FIB). The commands apply the route map called routemap1 to BGP routes in the RIB:

{{< tabs "TabID152 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router rib ipv4 protocol bgp fib-filter routemap1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# ip protocol bgp route-map routemap1
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
ip protocol bgp route-map routemap1
```

{{< /tab >}}
{{< /tabs >}}

For <span style="background-color:#F5F5DC">[BGP](## "Border Gateway Protocol")</span>, you can also apply a route map on route updates from BGP to the RIB. You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. You can use both IPv4 and IPv6 address families. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

To apply a route map to filter route updates from BGP into the RIB:

{{< tabs "TabID194 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:$ nv set vrf default router bgp address-family ipv4-unicast rib-filter routemap1
cumulus@switch:$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp 65000
switch(config-router)# address-family ipv4 unicast
switch(config-router-af)# table-map routemap1
switch(config-router-af)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@switch:~$ sudo cat /etc/frr/frr.conf
...
address-family ipv4 unicast
table-map routemap1
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
To apply an outbound route map to a route reflector client, you must run the NVUE `nv set vrf <vrf> router bgp route-reflection outbound-policy on` command or the vtysh `neighbor <neighbor> route-map SET_IBGP_ORIG out` command under the address family, before you apply the route map.
{{%/notice%}}

### Route Map Description

To provide a description for a route map, run the NVUE `nv set router policy route-map <route-map> rule <rule> description` command.

```
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 match interface swp51
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 set metric 50
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 action permit
cumulus@switch:~$ nv set router policy route-map routemap1 rule 10 description set-metric-swp51
cumulus@switch:~$ nv config apply
```

### Clear Matches Against a Route Map

To clear the number of matches shown against a route map, run the `nv action clear router policy route-map <route-map>` command.

The following example clears the number of matches shown against the route map called ROUTEMAP1.

```
cumulus@switch:~$ nv action clear router policy route-map ROUTEMAP1
Running handle_clear_route_map ROUTEMAP1
Action succeeded
```

## Route Redistribution

Route redistribution allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

The following example commands redistribute routing information from <span style="background-color:#F5F5DC">[OSPF](## "Open Shortest Path First")</span> routes into <span style="background-color:#F5F5DC">[BGP](## "Border Gateway Protocol")</span>:

{{< tabs "TabID273 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp
switch(config-router)# redistribute ospf
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

To redistribute all directly connected networks, use the `redistribute connected` command. For example:

{{< tabs "TabID251 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router bgp
switch(config-router)# redistribute connected
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
For OSPF, redistribution loads the database unnecessarily with type-5 LSAs. Only use this method to generate real external prefixes (type-5 LSAs).
{{%/notice%}}

## Configuration Examples

This section shows the `/etc/frr/frr.conf` file configuration for example route filters and redistribution.

The following example filters all routes that are not originated in the local AS:

```
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay interface remote-as external
 !
 address-family ipv4 unicast
  neighbor underlay route-map my-as out
 exit-address-family
!
bgp as-path access-list my-as permit ^$
!
route-map my-as permit 10
 match as-path my-as
!
route-map my-as deny 20
!
```

The following example sets communities based on prefix-lists:

```
...
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay interface remote-as external
 !
 address-family ipv6 unicast
  neighbor underlay activate
  neighbor underlay route-map MARK-PREFIXES out
 exit-address-family
!
ipv6 prefix-list LOW-PRIO seq 5 permit 2001:db8:dead::/56 le 64
ipv6 prefix-list MID-PRIO seq 5 permit 2001:db8:beef::/56 le 64
ipv6 prefix-list HI-PRIO seq 5 permit 2001:db8:cafe::/56 le 64
!
route-map MARK-PREFIXES permit 10
 match ipv6 address prefix-list LOW-PRIO
 set community 123:200
!
route-map MARK-PREFIXES permit 20
 match ipv6 address prefix-list MID-PRIO
 set community 123:500
!
route-map MARK-PREFIXES permit 30
 match ipv6 address prefix-list HI-PRIO
 set community 123:1000
!
```

The following example filters routes from advertising to the peer:

```
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay interface remote-as external
 !
 address-family ipv4 unicast
  neighbor underlay route-map POLICY-OUT out
 exit-address-family
!
ip prefix-list BLOCK-RFC1918 seq 5 permit 10.0.0.0/8 le 24
ip prefix-list BLOCK-RFC1918 seq 10 permit 172.16.0.0/12 le 24
ip prefix-list BLOCK-RFC1918 seq 15 permit 192.168.0.0/16 le 24
ip prefix-list ADD-COMM-OUT seq 5 permit 100.64.0.0/10 le 24
ip prefix-list ADD-COMM-OUT seq 10 permit 192.0.2.0/24
!
route-map POLICY-OUT deny 10
 match ip address prefix-list BLOCK-RFC1918
!
route-map POLICY-OUT permit 20
 match ip address prefix-list ADD-COMM-OUT
 set community 123:1000
!
route-map POLICY-OUT permit 30
```

The following example sets mutual redistribution between OSPF and BGP (filters by route tags):

```
...
router ospf
  redistribute bgp route-map BGP-INTO-OSPF
!
router bgp 65101
 bgp router-id 10.10.10.1
 neighbor underlay interface remote-as external
 !
 address-family ipv4 unicast
  redistribute ospf route-map OSPF-INTO-BGP
 exit-address-family
!
route-map OSPF-INTO-BGP deny 10
 match tag 4271
!
route-map OSPF-INTO-BGP permit 20
 set tag 2328
!
route-map BGP-INTO-OSPF deny 10
 match tag 2328
!
route-map BGP-INTO-OSPF permit 20
 set tag 4271
```

The following example filters and modifies redistributed routes:

```
...
router ospf
  redistribute bgp route-map EXTERNAL-2-1K
!
route-map EXTERNAL-2-1K permit 10
 set metric 1000
 set metric-type type-1
```

## Considerations

When you configure a route map to match a prefix list, community list, or aspath list, the permit or deny actions in the list determine the criteria to evaluate in each route map sequence; for example:
- If you match a list in a route map permit sequence, Cumulus Linux matches the permitted routes in the list for that route map sequence and the policy permits them. Denied routes in the list do not match and Cumulus Linux evaluates them in later route map sequences.
- If you match a list in a route map deny sequence, Cumulus Linux matches the permitted routes in the list for that route map sequence and the policy denies them. Denied routes in the list do not match and Cumulus Linux evaluates them in later route map sequences.

NVIDIA recommends you always configure a community list as `permit`, and permit or deny routes using route map sequences.
