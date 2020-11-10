---
title: Route Filtering and Redistribution
author: Cumulus Networks
weight: 750
toc: 3
---
Route filtering lets you exclude routes that are advertised or received from neighbors. You can use route filtering to manipulate traffic flows, reduce memory utilization, and improve security.

This section discusses the following route filtering methods:
- Route maps
- Prefix lists
- Route redistribution

## Prefix Lists

Prefix lists are access lists for route advertisements that match routes instead of traffic. Prefix lists are typically used with route maps and other filtering methods. A prefix list can match the prefix (the network itself) and the prefix-length (the length of the subnet mask).

The following example commands configure a prefix list that permits all prefixes in the range 10.0.0.0/16 with a subnet mask less than or equal to /30. For networks 10.0.0.0/24, 10.10.10.0/24, and 10.0.0.10/32, only 10.0.0.0/24 is matched (10.10.10.0/24 has a different prefix and 10.0.0.10/32 has a greater subnet mask).

{{< tabs "TabID22 ">}}

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

A route map filters routes from Zebra into the Linux kernel. To apply the route map, you specify the routing protocol (bgp, ospf, or static) and the route map name.

The following example commands apply the route map called routemap1 to BGP:

{{< tabs "TabID152 ">}}

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

The following example:
- Creates a prefix list that permits all prefixes in the range 10.0.0.0/16 with a subnet mask less than or equal to /30
- Creates a route map that matches the prefix list and sets the metric to 50
- Applies the route map

{{< tabs "TabID119 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add routing prefix-list ipv4 prefixlist1 permit 10.0.0.0/16 le 30
cumulus@switch:~$ net add routing route-map routemap1 permit 10 match ip address prefix-list prefixlist1
cumulus@switch:~$ net add routing route-map routemap1 permit 10 set metric 50
cumulus@switch:~$ net add routing protocol ospf route-map routemap1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip prefix-list prefixlist1 permit 10.0.0.0/16 le 30
switch(config)# route-map routemap1 permit 10
switch(config-route-map)# match ip address prefix-list prefixlist1
switch(config-route-map)# set metric 50
switch(config-route-map)# exit
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

ip prefix-list prefixlist1 permit 10.0.0.0/16 le 30
route-map routemap1 permit 10
 match ip address prefix-list prefixlist1
 set metric 50
ip protocol ospf route-map routemap1

```

The following example commands apply the route map called `map1` to redistributed routes:

{{< tabs "TabID1012 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add ospf redistribute connected route-map map1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The following example commands apply the route map called `map1` to redistributed routes:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# redistribute connected route-map map1
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
 redistribute connected route-map map1
...
```
