---
title: Route Filtering and Redistribution
author: NVIDIA
weight: 750
toc: 3
---
Route filtering lets you exclude routes that are advertised or received from neighbors. You can use route filtering to manipulate traffic flows, reduce memory utilization, and improve security.

This section discusses the following route filtering methods:
- Prefix lists
- Route maps
- Route redistribution

## Prefix Lists

Prefix lists are access lists for route advertisements that match routes instead of traffic. Prefix lists are typically used with route maps and other filtering methods. A prefix list can match the prefix (the network itself) and the prefix-length (the length of the subnet mask).

The following example commands configure a prefix list that permits all prefixes in the range 10.0.0.0/16 with a subnet mask less than or equal to /30. For networks 10.0.0.0/24, 10.10.10.0/24, and 10.0.0.10/32, only 10.0.0.0/24 is matched (10.10.10.0/24 has a different prefix and 10.0.0.10/32 has a greater subnet mask).

{{< tabs "TabID22 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set router policy prefix-list prefixlist1 rule 1 match 10.0.0.0/16 max-prefix-len 30
cumulus@switch:~$ cl set router policy prefix-list prefixlist1 rule 1 action permit
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing prefix-list ipv4 prefixlist1 permit 10.0.0.0/16 le 30
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip prefix-list prefixlist1 permit 10.0.0.0/16 le 30
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}
{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 ospf router-id 10.10.10.1
 timers throttle spf 80 100 6000
 passive-interface vlan10
 passive-interface vlan20
ip prefix-list prefixlist1 permit 10.0.0.0/16 le 30
```

To use this prefix list in a route map, see {{<link url="#configuration-examples" text="Configuration-Examples">}} below.

## Route Maps

Route maps are routing policies that are considered before the router examines the forwarding table. Each statement in a route map is assigned a sequence number, and contains a series of match and set statements. The route map is parsed from the lowest sequence number to the highest, and stops when a match is found.

### Configure a Route Map

The following example commands configure a route map that sets the metric to 50 for interface swp51:

{{< tabs "TabID73 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set router policy route-map routemap1 rule 10 match interface swp51
cumulus@switch:~$ cl set router policy route-map routemap1 rule 10 set metric 50
cumulus@switch:~$ cl set router policy route-map routemap1 rule 10 action permit
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing route-map routemap1 permit 10 match interface swp51
cumulus@switch:~$ net add routing route-map routemap1 permit 10 set metric 50
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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

{{< /tab >}}
{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 ospf router-id 10.10.10.1
 timers throttle spf 80 100 6000
 passive-interface vlan10
 passive-interface vlan20
route-map routemap1 permit 10
 match interface swp51
 set metric 50
```

### Apply a Route Map

To apply the route map, you specify the routing protocol and the route map name.

The following example filters routes from Zebra into the Linux kernel. The commands apply the route map called routemap1 to BGP:

{{< tabs "TabID152 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set vrf default router bgp address-family ipv4-unicast rib-filter routemap1
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing protocol bgp route-map routemap1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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

{{< /tab >}}
{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 ospf router-id 10.10.10.1
 timers throttle spf 80 100 6000
 passive-interface vlan10
 passive-interface vlan20
ip protocol bgp route-map routemap1
```

For BGP, you can also apply a route map on route updates from BGP to Zebra. All the applicable match operations are allowed, such as match on prefix, next hop, communities, and so on. Set operations for this attach-point are limited to metric and next hop only. Any operation of this feature does not affect BGPs internal RIB. Both IPv4 and IPv6 address families are supported. Route maps work on multi-paths; however, the metric setting is based on the best path only.

To apply a route map to filter route updates from BGP into Zebra, run the following command:

```
cumulus@switch:$ net add bgp table-map routemap2
```

{{%notice note%}}
In NCLU, you can only set the community number in a route map. You cannot set other community options such as `no-export`, `no-advertise`, or `additive`.
{{%/notice%}}

## Route Redistribution

Route redistribution allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

To redistribute protocol routes, run the `net add <protocol> redistribute` command. The following example commands redistribute routing information from ospf routes into BGP:

{{< tabs "TabID219 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution ospf
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp redistribute ospf
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set vrf default router bgp address-family ipv4-unicast route-redistribution connected
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add bgp redistribute connected
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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

The following example filters routes from being advertised to the peer:

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
