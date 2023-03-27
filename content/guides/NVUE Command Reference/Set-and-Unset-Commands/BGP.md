---
title: BGP
author: Cumulus Networks
weight: 520
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set router bgp

Configures BGP globally on the switch.

- - -

## nv set router bgp autonomous-system

Configures the BGP <span style="background-color:#F5F5DC">[ASN](## "Autonomous System Number ")</span> on the switch to identify the BGP node. You can set a value between 1 and 4294967295. To use auto BGP to assign an ASN automatically on the leaf, set the value to `leaf`. To use auto BGP to assign an ASN automatically on the spine, set the value to `spine`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp autonomous-system 65101
```

- - -

## nv set router bgp convergence-wait

Configures BGP read-only mode. Sometimes, as Cumulus Linux establishes BGP peers and receives updates, it installs prefixes in the RIB and advertises them to BGP peers before receiving and processing information from all the peers. Also, depending on the timing of the updates, Cumulus Linux sometimes installs prefixes, then withdraws and replaces them with new routing information. Read-only mode minimizes this BGP route churn in both the local RIB and with BGP peers.

Enable read-only mode to reduce CPU and network usage when restarting the BGP process. Because intermediate best paths are possible for the same prefix as peers establish and start receiving updates at different times, read-only mode is useful in topologies where BGP learns a prefix from a large number of peers and the network has a high number of prefixes.

While in read-only mode, BGP does not run best-path or generate any updates to its peers.

- - -

## nv set router bgp convergence-wait establish-wait-time

Configures BGP read-only mode by setting the establish wait time. You can set a value between 0 and 3600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp convergence-wait establish-wait-time 200
```

- - -

## nv set router bgp convergence-wait time

Configures BGP read-only mode by setting the convergence wait time. You can set a value between 0 and 3600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp convergence-wait time 300
```

- - -

## nv set router bgp enable

Turns BGP `on` or `off` on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp enable on
```

- - -

## nv set router bgp graceful-restart

Configures BGP graceful restart globally on the switch to minimize the negative effects that occur when BGP restarts. All BGP peers inherit the graceful restart capability.

- - -

## nv set router bgp graceful-restart mode

Configures the BGP graceful restart mode globally on the switch. You can specify the following settings:
- `off`, where graceful restart is not negotiated with peers.
- `helper-only`, where the switch is in a helper role only, and routes originated and advertised from a BGP peer in the peer group are not deleted. - `full`, where the switch is in both a helper and restarter role.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart mode helper-only
```

- - -

## nv set router bgp graceful-restart path-selection-deferral-time

Configures the number of seconds a restarting peer defers path-selection when waiting for the EOR marker from peers. The default is 360 seconds. You can set a value between 0 and 3600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart path-selection-deferral-time 300
```

- - -

## nv set router bgp graceful-restart restart-time

Configures the number of seconds to wait for a graceful restart capable peer to re-establish BGP peering. The default is 120 seconds. You can set a value between 1 and 4095.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart restart-time 400
```

- - -

## nv set router bgp graceful-restart stale-routes-time

Configures the number of seconds to hold stale routes for a restarting peer. The default is 360 seconds. You can set a value between 1 and 4095.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-restart stale-routes-time 400
```

- - -

## nv set router bgp graceful-shutdown

Turns BGP graceful shutdown on or off on the switch to reduce packet loss during planned maintenance of a router or link. BGP graceful shutdown  forces traffic to route around the BGP node:.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp graceful-shutdown on
```

- - -

## nv set router bgp policy-update-timer

Configures the BGP policy update timer globally on the switch to wait the specified number of seconds before processing updates to policies to ensure that a series of changes are processed together. You can set a value between 0 and 600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp policy-update-timer 300
```

- - -

## nv set router bgp router-id

Configures the BGP router ID on the switch. NVUE automatically assigns the loopback address of the switch to be the router ID. FRR automatically assigns the router ID to be the loopback address or the highest IPv4 address for the interface. If you do not have a loopback address configured or want to use a specific router ID, set the router ID globally.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp router-id 10.10.10.1
```

- - -

## nv set router bgp wait-for-install

Turns BGP wait for install on or off. When BGP *wait for install* is on, BGP waits for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router bgp wait-for-install on
```

- - -

## nv set vrf \<vrf-id\> router bgp

Provides commands to configure BGP on the specified VRF.

- - -

## nv set vrf \<vrf-id\> router bgp address-family

Provides commands to configure the address family in the specified VRF.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast

Provides commands to configure the IPv4 unicast address family in the specified VRF.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Provides commands to configure IPv4 route redistribution, which allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static

Provides commands to configure route redistribution of IPv4 static routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static enable

Turns IPv4 static route redistribution on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute static enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static metric

Configures the metric you want to use for the redistributed IPv4 route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute static metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static route-map

Sets the route map to apply to the redistributed IPv4 route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute static route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected

Configures route redistribution of IPv4 connected routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected enable

Turns route redistribution of IPv4 connected routes on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected metric

Configures the metric you want to use for the redistributed connected route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected route-map

Applies the specified route map to the redistributed connected IPv4 route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute connected route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel

Provides commands to configure IPv4 kernel route redistribution.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel enable

Turns IPv4 kernel route redistribution on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute kernel enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel metric

Configures the metric you want to use for the redistributed IPv4 kernel route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute kernel metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel route-map

Applies the route map to the redistributed IPv4 kernel route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute kernel route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf

Provides commands to configure OSPF IPv4 route redistribution.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf enable

Turns OSPF route redistribution on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf metric

Configures the metric you want to use for the OSPF redistributed routes. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf route-map

Applies the route map to the redistributed OSPF route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast redistribute ospf route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\>

Provides commands to configure IPv4 route aggregation to minimize the size of the routing table and save bandwidth. You can aggregate a range of networks in your routing table into a single prefix.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\> summary-only

Configures BGP to suppress longer IPv4 prefixes inside the aggregate address before sending updates.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 summary-only on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\> as-set

Turns generation of an `AS_SET` for route aggregate on or off. When `on`, BGP creates an aggregate address with a mathematical set of autonomous systems. The `AS_SET` option summarizes the `AS_PATH` attributes of all the individual routes to help BGP detect and avoid loops.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 as-set on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\> route-map

Applies a route map to the IPv4 aggregate route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\>

Configures the IPv4 prefixes to originate from a BGP node.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\> route-map

Applies a route map to the IPv4 prefixes that originate from a BGP node.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32 route-map HI-PRIO
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import

Provides commands to configure IPv4 route leaking, where a destination VRF wants to know the routes of a source VRF. As routes come and go in the source VRF, they dynamically leak to the destination VRF through BGP.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf

Provides commands to configure the VRF from which IPv4 route leaking occurs.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\>

Configures the VRF from which to import IPv4 routes. You can specify multiple VRFs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<leak-vrf-id>`  | The VRF from which you want to leak routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf list BLUE
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf enable

Turns IPv4 route leaking on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf route-map \<instance-name\>

Applies a route map to control importing IPv4 routes. For example, to exclude certain prefixes from the import process, configure the prefixes in a route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf route-map BLUEtoRED
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths

Configures the maximum number of equal-cost BGP paths allowed for IPv4. The BGP multipath option is on by default and the maximum number of paths is 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs. 1 disables the BGP multipath option.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv4-unicast multipaths 1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths ebgp

Configures the number of equal-cost eBGP paths allowed for IPv4.

The default value is 64.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ebgp 120
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths ibgp

Configures the number of equal-cost iBGP paths allowed for IPv4.

The default value is 64.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ibgp 120
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths compare-cluster-length

Turns on cluster length comparison for IPv4. When `on` and iBGP paths have a cluster list, their lengths must be equal to be selected as multipaths.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast compare-cluster-length on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance

Provides commands to configure the BGP administrative distance so that the switch can choose which routing protocol to use when two different protocols provide IPv4 route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from BGP with an administrative distance of 100, the switch chooses BGP.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance external

Configures the distance to apply to IPv4 routes from eBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance external 150
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance internal

Configures the distance to apply to IPv4 routes from iBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance internal 110
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export

Provides commands to configure IPv4 route export settings.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn

Provides commands to configure IPv4 prefix-based routing using EVPN type-5 routes. Type-5 routes (or prefix routes) primarily route to destinations outside of the data center fabric. EVPN prefix routes carry the layer 3 VNI and router MAC address and follow the symmetric routing model to route to the destination prefix.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn enable

Turns IPv4 prefix-based routing using EVPN type-5 routes on or off. When `on`, the switch can announce IP prefixes in the BGP RIB as EVPN type-5 routes.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn route-map

Sets the route map to control the export of IPv4 routes into EVPN. By default, when announcing IP prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn route-map HIGH-PRIO
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination

Configures originating EVPN default type-5 routes. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn default-route-origination on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast rib-filter

Applies a route map on IPv4 route updates from BGP to the Route Information Base (RIB). You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast rib-filter routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast enable

Tuns the BGP IPv4 address family on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family l2vpn-evpn

Provides commands to configure the L2VPN-EVPN address family.

- - -

## nv set vrf \<vrf-id\> router bgp address-family l2vpn-evpn enable

Tuns the L2VPN-EVPN address family on or off for the VRF.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family l2vpn-evpn enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast

Provides commands to configure the BGP for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\>

Provides commands to configure an IPv6 aggregate route.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> summary-only

Ensures that BGP suppresses longer IPv6 prefixes inside the aggregate address before sending updates.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 summary-only on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> as-set

Turns generation of an `AS_SET` for the aggregate on or off. When `on`, BGP creates an aggregate address with a mathematical set of autonomous systems. The `AS_SET` option summarizes the `AS_PATH` attributes of all the individual IPv6 routes to help BGP detect and avoid loops.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 as-set on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> route-map

Applies a route map to the aggregate IPv6 route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\>

Provides commands to configure an IPv6 static network.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import

Provides commands to configure IPv6 route leaking, where a destination VRF wants to know the routes of a source VRF. As routes come and go in the source VRF, they dynamically leak to the destination VRF through BGP.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf

Provides commands to configure VRF to VRF route leaking for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list

Configures the VRF from which to import IPv6 routes. You can specify multiple VRFs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf list BLUE
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf enable

Turns IPv6 route leaking on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf route-map \<instance-name\>

Applies a route map to control importing IPv6 routes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf route-map BLUEtoRED
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths

Provides commands to configure the maximum number of equal-cost BGP paths allowed. The BGP multipath option is on by default and the maximum number of paths is 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths ebgp

Configures the number of equal-cost eBGP paths allowed. You can specify a value between 1 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast multipaths ebgp 120
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths ibgp

Configures the number of equal-cost iBGP paths allowed for IPv6. You can specify a value between 1 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast multipaths ibgp 120
```

- - -

## nv set vrf \<vrf-id> router bgp address-family ipv6-unicast multipaths compare-cluster-length

Turns on cluster length comparison for IPv6. When `on` and iBGP paths have a cluster list, their lengths must be equal to be selected as multipaths.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast compare-cluster-length on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance

Provides commands to configure the administrative distance for internal and external IPv6 routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance external

Configures the distance to apply to IPv6 routes from eBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast admin-distance external 150
```

- - -

## nv set vrf \<vrf-id>\ router bgp address-family ipv6-unicast admin-distance internal

Configures the distance to apply to IPv6 routes from iBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast admin-distance internal 110
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export

Provides commands to configure IPv6 route export settings.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn

Provides commands to export IPv6 routes from this VRF into EVPN as type-5 routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn enable

Turns IPv6 prefix-based routing for EVPN type-5 routes on or off. When `on`, the switch can announce IPv6 prefixes in the BGP RIB as EVPN type-5 routes.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn route-map

Applies the route map to control how IPv6 routes export into EVPN. By default, when announcing IPv6 prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn route-map HIGH-PRIO
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination

Configures originating EVPN default type-5 routes. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod).

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn default-route-origination on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute

Provides commands to configure IPv6 route redistribution, which allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static

Provides commands to configure redistribution of IPv6 static routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static enable

Turns route redistribution of IPv6 static routes on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static metric

Configures the metric you want to use for the redistributed IPv6 route. You can specify `auto`, or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static route-map

Applies the route map to the redistributed static IPv6 route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected

Provides commands to configure route redistribution of IPv6 connected routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected enable

Turns route redistribution of IPv6 connected routes on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected metric

Configures the metric you want to use for the redistributed connected IPv6 route. You can specify auto or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected route-map (none|<instance-name>)

Applies a route map to the redistributed connected IPv6 route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel

Provides commands to configure redistribution of IPv6 kernel routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel enable

Turns redistribution of IPv6 kernel routes on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel metric

Configures the metric you want to use for the redistributed kernel route. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch choses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel route-map

Applies a route map to the redistributed IPv6 route.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6

Provides commands to configure redistribution of OSPF IPv6 routes.

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 enable

Turns redistribution of OSPF IPv6 routes on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 metric (0-4294967295|auto)

Configures the metric you want to use for the redistributed OSPF routes. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch chooses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf metric 4294967295
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 route-map (none|<instance-name>)

Applies a route map to the redistributed IPv6 route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast rib-filter

Applies a route map on IPv6 route updates from BGP to the Route Information Base (RIB). You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast rib-filter routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast enable

Tuns the BGP for IPv6 on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp address-family ipv6-unicast enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection

Provides commands to configure BGP best path selection.

- - -

## nv set vrf \<vrf-id\> router bgp path-selection aspath

Provides commands to configure how BGP selects the best path to an autonomous system (AS).

- - -

## nv set vrf \<vrf-id\> router bgp path-selection aspath compare-lengths

Configures BGP to select the AS based on path length.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection aspath compare-lengths on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection aspath compare-confed

Configures BGP to select the AS based on confederations.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection aspath compare-confed on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection med

Provides commands to configure BGP multi-exit discriminator (MED) path selection.

- - -

## nv set vrf \<vrf-id\> router bgp path-selection med compare-always

Configures BGP to always compare the MED on routes even when received from different neighboring autonomous systems. When enabled, BGP compares MEDs for all paths.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection med compare-always on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection med compare-deterministic

Applies route selection in a way that produces deterministic answers locally.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection med compare-deterministic on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection med compare-confed

Configures MED for route-selection based on confederations.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection med compare-confed on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection med missing-as-max

Turns BGP MED missing-as-max on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection med missing-as-max on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection multipath

Provides commands to configure BGP multipath path selection.

- - -

## nv set vrf \<vrf-id\> router bgp path-selection multipath aspath-ignore

Configures BGP to ignore the AS path when determining multipath routing.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection multipath generate-asset

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection multipath generate-asset on
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection multipath bandwidth

Configures multipath route selection based on bandwidth. You can specify `bandwidth`, `all-paths`, `skip-missing`, `default-weight-for-missing`, or `ignore`.

The default setting is `ignore`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection multipath bandwidth all-paths
```

- - -

## nv set vrf \<vrf-id\> router bgp path-selection routerid-compare

Configures BGP to use the router ID to decide the best path when two identical routes are received from two different peers.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp path-selection routerid-compare on
```

- - -

## nv set vrf \<vrf-id\> router bgp route-reflection

Provides commands to configure BGP route reflection. When you configure an iBGP speaker as a route reflector, it can send iBGP learned routes to other iBGP peers.

- - -

## nv set vrf \<vrf-id\> router bgp route-reflection enable

Turns BGP route reflection on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp route-reflection enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp route-reflection cluster-id

Configures the cluster ID to use during route reflection. This setting is required when route-reflection is on.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp route-reflection cluster-id 10
```

- - -

## nv set vrf \<vrf-id\> router bgp route-reflection reflect-between-clients

Allows routes to be reflected between clients. Typically, routes are reflected only between clients and non-clients, with the clients of a route reflector expected to be fully meshed.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp route-reflection reflect-between-clients on
```

- - -

## nv set vrf \<vrf-id\> router bgp route-reflection outbound-policy

Allows an outbound peer policy to modify the attributes for reflected routes. Typically, reflected routes have to retain their original attributes.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp route-reflection outbound-policy on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\>

Provides commands to configure BGP peer groups.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd

Provides commands to configure Bidirectional Forwarding Detection (BFD) for BGP sessions for a peer group. When you configure BFD in BGP, PTM registers and de-registers neighbors dynamically.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd enable

Turns BFD on or off for the BGP peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE bfd enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd detect-multiplier

Configures the BFD interval multiplier for the BGP peer group. You can specify a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE bfd detect-multiplier 4
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd min-rx-interval

Configures the minimum interval between received BFD control packets for the BGP peer group. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE bfd min-rx-interval 400
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd min-tx-interval

Configures the minimum interval between sending BFD control packets for the BGP peer group. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE bfd min-tx-interval 400
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security

Provides commands to configure the TTL security hop count for the peer group to prevent attacks against eBGP, such as denial of service (DoS). By default, BGP messages to eBGP neighbors have an IP time-to-live (TTL) of 1, which requires the peer to be directly connected, otherwise, the packets expire along the way. An attacker can adjust the TTL of packets so that they look like they originate from a directly connected peer. The BGP TTL security hops option inverts the direction in which BGP counts the TTL. Instead of accepting only packets with a TTL of 1, Cumulus Linux accepts BGP messages with a TTL greater than or equal to 255 minus the specified hop count.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security enable

Turns BGP TTL security on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE ttl-security enable on 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security hops

Configures the number of hops to deduct from a TTL greater than or equal to 255 to prevent attacks against eBGP, such as denial of service (DoS).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE ttl-security hops 200 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities

Provides commands for advertising IPv4 prefixes with IPv6 next hops over global IPv6 peerings.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities extended-nexthop

Turns the extended next hop capability defined in RFC 5549 on or off. The extended nexthop is advertised to peers in the peer group. If you specify `auto`, extended next hop is `on` for unnumbered peers and `off` otherwise.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE capabilities extended-nexthop on 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities source-address

Configures the source IP address of the TCP connection for the peer group, which is often used as the BGP next hop for updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE capabilities source-address 10.10.10.1
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart

Provides commands to configure graceful restart to minimize the negative effects that occur when BGP restarts. This option enables a BGP speaker to signal to its peers that it can preserve its forwarding state and continue data forwarding during a restart. It also enables a BGP speaker to continue to use routes announced by a peer even after the peer has gone down.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart mode

Configures graceful restart mode for the peer group. If you specify `auto`, the mode is inherited from the global setting. If you specify `off`, graceful restart is not negotiated with the peer group. If you specify `helper-only`, the switch is in a helper role only, where routes originated and advertised from a BGP peer in the peer group are not deleted. If you specify `full`, the switch is in both a helper and restarter role.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINE graceful-restart mode helper-only
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as

Provides commands to configure the local AS for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as enable

Turns local AS on or off for the peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as asn

Configures the ASN you want to use for the peer group to establish the peering if it is different from the ASN of the BGP instance. The local AS configured is also attached to incoming and outgoing updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as asn 65101
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as prepend

Configures BGP to prepend the configured local AS to updates for the peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as replace

Configures BGP to either attach only the configured local AS to generated updates or attach the ASN of the BGP instance, then prepend it with the configured local AS.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES local-as replace on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers

Provides commands to configure BGP timers for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers keepalive

Configures the interval at which BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. You can specify a value between 1 and 65535. If you speciy `none`, BGP does not send keepalives. If you specify `auto`, BGP uses the global value.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers keepalive 10
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers hold

Configures the hold timer. If BGP does not receive a keepalive or update message from a peer in the peer group within the hold time, it declares the peer down and withdraws all routes received by this peer from the local BGP table. If you specify `none`, BGP does not track keepalives from the peer and the peering session does not experience a hold timeout. You can specify a value between 3 and 65535. If you specify `auto`, BGP uses the global value.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers hold 30
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers connection-retry

Configures the time interval at which BGP attempts to connect to a peer in the peer group after a failure. You can specify a value between 1 and 65535. If you specify `auto`, BGP uses the global value.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers connection-retry 30
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers route-advertisement

Configures the time between route advertisements (BGP updates). After making a new best path decision for a prefix, BGP can insert a delay before advertising the new results to a peer. This delay rate limits the amount of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. You can specify a value between 1 and 65535. If you specify `none` BGP delays and sends route advertisements in batches. If you specify `auto`, BGP uses the global value.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES timers route-advertisement 5
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family

Provides commands to configure the address family settings for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast

Provides commands to configure IPv4 settings for the BGP peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise

Provides commands to configure the BGP COMMUNITY attribute to advertise to the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise regular

Configures BGP to announce the `COMMUNITIES` attribute to the peer group. You can specify `on` or `off`.

The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise regular off
```

- - -

### nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise extended

Configures BGP to announce the `EXT_COMMUNITIES` attribute to the peer group. You can specify `on` or `off`.

The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise extended off
```

- - -

### nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise large

Configures BGP to announce the `LARGE_COMMUNITIES` attribute to the peer group. You can specify `on` or `off`.

The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise large off
```

- - -

### nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod

Provides commands to configure the BGP attribute mode for the peer group.

### nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod aspath

Configures BGP to follow normal BGP procedures when generating the `AS_PATH` attribute for the specified peer group. You can specify `on` or `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod aspath on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod med

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the specified peer group. You can specify `on` or `off`. If you set this attribute to `off`, BGP does not change the MED when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod med on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod nexthop

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the specified peer group. You can specify `on` or `off`. If you set this attribute to `off`, BGP does not change `NEXT_HOP` when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod nexthop on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath

Provides commands to configure options for handling the BGP `AS_PATH` for IPv4 prefixes from or to the specified peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn

Provides commands to configure BGP to accept a received AS_PATH that contains the ASN of the local system.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn occurrences

Configures the maximum number of times the local system's AS number is allowed in the received `AS_PATH`. You can specify a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath allow-my-asn occurrences 6
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn origin

Configures BGP to allow a received AS_PATH containing the ASN of the local system, but only if it is the originating AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath allow-my-asn origin on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath replace-peer-as

Configures BGP to replace the AS path in an outgoing update that contains the ASN of the peer with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath replace-peer-as on
```

- - -

# nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath private-as

Configures what action to take with private ASNs. You can specify`none` to take no action, `remove`, to remove any private ASNs in the update to the peer, or `replace` to replace any private ASNs in the update to the peer with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath private-as replace
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits

Provides commands to configure IPv4 prefix limits from peers in the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound

Provides commands to configure limits on the inbound IPv4 prefix from the peers in the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound maximum 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound maximum 3000
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound warning-threshold

Configures the maximum number of inbound IPv4 prefixes (as a percentage) allowed before the switch generates a syslog warning. You can set a value between 1 and 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound warning-threshold 4
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound warning-only

Configures the maximum number of inbound IPv6 prefixes (as a percentage) allowed before the switch generates a syslog warning. You can set a value between 1 and 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound warning-only on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound reestablish-wait

Configures the time in seconds to wait before establishing the BGP session again with the peers in the peer group. You can specify a value between 1-4294967295. A value of `auto` uses standard BGP timers and processing (between 2 and 3 seconds).

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound reestablish-wait 3000000000
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination

Provides commands to configure default route origination for IPv4.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Provides commands to configure an optional route map policy to control the conditions under which the default IPv4 route is originated.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Provides commands to configure the inbound unicast policy for IPv4.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound route-map

Configures the route map you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound route-map myroutemap
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound prefix-list

Configures the prefix list you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound prefix-list myprefixlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound aspath-list none

Configures the AS path filter list you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound aspath-filter myaspathlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Provides commands to configure the outbound IPv4 unicast policy for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound route-map

Configures the route map you want to apply to updates to be sent to the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound route-map myroutemap
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound unsuppress-map

Configures the route map used to unsuppress IPv4 routes selectively when advertising to the peers in the peer group; these are routes that have been suppressed due to aggregation configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound unsuppress-map myunsuppress
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound prefix-list

Configures the prefix list you want to apply to updates to be sent to the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound prefix-list myprefixlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound aspath-list none

Configures the AS path filter list you want to apply to updates sent to the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound aspath-list myaspathlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise

Provides commands to configure BGP conditional advertisement, which lets you advertise certain routes only if other routes either do or do not exist. BGP conditional advertisement is typically used in multihomed networks where BGP advertises some prefixes to one of the providers only if information from the other provider is not present. For example, a multihomed router can use conditional advertisement to choose which upstream provider learns about the routes it provides so that it can influence which provider handles traffic destined for the downstream router. This is useful for cost of service, latency, or other policy requirements that are not natively accounted for in BGP.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise enable

Turns BGP conditional advertisement for IPv4 on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise advertise-map \<instance-name\>

Configures the route map that contains the prefix list with the list of IPv4 routes or prefixes you want to advertise.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise advertise-map myadvertise 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise exist-map \<instance-name\>

Configures the route map that contains the prefix list with the conditional IPv4 routes or prefixes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise exist-map EXIST 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise non-exist-map \<instance-name\>

Configures the route map that contains the prefix list with the negative conditional IPv4 routes or prefixes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise non-exist-map NONEXIST 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast enable

Turns IPv4 on or off for the BGP peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast route-reflector-client

Configures the BGP node as a route reflector for a BGP peer.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast route-reflector-client on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast route-server-client

Configures the BGP node as a route server for a BGP peer.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast route-server-client on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft-reconfiguration

Turns on soft configuration so that received IPv4 routes from peers in the peer group that are rejected by an inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast soft-reconfiguration on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast nexthop-setting

Configures the BGP next hop value of advertised IPv4 routes for the peers in the peer group. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to ourselves for route advertisement excluding reflected routes, or `force` to set the next hop to ourselves for route advertisement including reflected routes.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast nexthop-setting force
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast add-path-tx

Configures BGP to advertise more than just the best path for a prefix. You can specify `all-paths` to advertise all known paths to the peers in the peer group or `best-per-AS` to advertise only the best path learned from each AS.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast add-path-tx all-paths
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast weight

Configures the weight applied to IPv4 routes received from peer; this is used in the BGP route selection algorithm.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast weight 65535
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast

Provides commands to configure IPv6 for the BGP peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Provides commands to configure IPv6 policies.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Provides commands to configure inbound IPv6 unicast policies.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound route-map

Configures the route map you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound route-map routemap1
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound prefix-list

Configures the prefix list you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound prefix-list myprefixlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound aspath-list none

Configures the AS path filter list you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound aspath-list MYASPATHLIST
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Provides commands to configure the outbound IPv6 unicast policy for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound aspath-list none

Configures the AS path filter list you want to apply to updates sent to the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound aspath-filter myaspathlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound prefix-list

Configures the IPv6 prefix list you want to apply to updates to be sent to the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound prefix-list myprefixlist
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound unsuppress-map

Configures the route map used to unsuppress IPv6 routes selectively when advertising to the peers in the peer group; these are routes that have been suppressed due to aggregation configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound unsuppress-map myunsuppress
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath

Provides commands to configure the AS path filter list you want to apply to updates sent to the peers in the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn

Provides commands to configure BGP to allow a received AS path to contain the ASN of the local system.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn enable

Configures BGP to allow a received AS path to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast allow-my-asn enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn origin

Configures BGP to allow a received AS path to contain the ASN of the local system only if it is the originating AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast allow-my-asn origin on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn occurrences

Configures the maximum number of times the AS number of the local system can be in the received AS path.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast allow-my-asn occurrences 5
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath replace-peer-as

Configures BGP to replace the AS path in an outgoing update that contains the ASN of the peer with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath replace-peer-as on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath private-as

Configures what action to take with private ASNs. You can specify`none` to take no action, `remove`, to remove any private ASNs in the update to the peer, or `replace` to replace any private ASNs in the update to the peer with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath private-as replace
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits

Provides commands to configure prefix limits from peers in the peer group for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound

Provides commands to configure limits on the inbound prefix from the peers in the peer group. 

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound maximum

Configures the maximum number of prefixes that BGP can receive from the peers in the peer group. By default, there is no limit.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound maximum 50000
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound warning-threshold

Configures the maximum number of inbound IPv6 prefixes (as a percentage) after which the switch generates a syslog warning. You can specify a value between 1 and 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound warning-threshold 50
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound warning-only

Turns on syslog warning generation only and does not bring down the BGP session if the number of received prefixes exceeds the limit.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound warning-only on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound reestablish-wait

Configures the time in seconds to wait before establishing the BGP session again with the peers in the peer group. You can specify a value between 1-4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound reestablish-wait 5000
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination

Provides commands to configure default route origination for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination enable

Turns default route origination for IPv6 on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast default-route-origination enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination policy

Configures the optional route map policy to control the conditions under which the default route is originated.

The default setting is `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast default-route-origination policy mypolicy
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise

Provides commands to configure the BGP `COMMUNITY` attribute to advertise to the peer group for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise regular

Configures BGP to announce the `COMMUNITIES` attribute to the peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise regular on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise extended

Configures BGP to announce the `EXT_COMMUNITIES` attribute to the peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise extended on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise large

Configures BGP to announce the `LARGE_COMMUNITIES` attribute to the peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise large on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod

Provides commands to configure the BGP attribute mode for the peer group for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod aspath

Configures BGP to follow normal BGP procedures when generating the `AS_PATH` attribute for the specified peer group. You can specify `on` or `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod aspath on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod nexthop

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the specified peer group. You can specify `on` or `off`. If you set this attribute to `off`, BGP does not change `NEXT_HOP` when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod nexthop on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod med

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the specified peer group. You can specify `on` or `off`. If you set this attribute to `off`, BGP does not change the MED when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod med on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise

Provides commands to configure BGP conditional advertisement, which lets you advertise certain routes only if other routes either do or do not exist. BGP conditional advertisement is typically used in multihomed networks where BGP advertises some prefixes to one of the providers only if information from the other provider is not present. For example, a multihomed router can use conditional advertisement to choose which upstream provider learns about the routes it provides so that it can influence which provider handles traffic destined for the downstream router. This is useful for cost of service, latency, or other policy requirements that are not natively accounted for in BGP.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise enable

Turns BGP conditional advertisement on or off for IPv6.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise advertise-map \<instance-name\>

Configures the route map that contains the prefix list with the list of IPv6 routes or prefixes you want to advertise.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise advertise-map myadvertise
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise exist-map \<instance-name\>

Configures the route map that contains the prefix list with the conditional IPv6 routes or prefixes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise exist-map EXIST  
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise non-exist-map \<instance-name\>

Configures the route map that contains the prefix list with the negative conditional IPv6 routes or prefixes.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise non-exist-map NONEXIST 
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast enable

Turns IPv6 on or off for the BGP peer group.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast route-reflector-client

Configures the BGP node as a route reflector for a BGP peer.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast route-reflector-client on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast route-server-client

Configures the BGP node as a route server for a BGP peer.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast route-server-client on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft-reconfiguration

Turns on soft configuration so that received IPv6 routes from the peers in the peer group that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast soft-reconfiguration on
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast nexthop-setting

Configures the BGP next hop value of advertised IPv6 routes for the peers in the peer group. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to itself for route advertisement excluding reflected routes, or `force` to set the next hop to itself for route advertisement including reflected routes.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast nexthop-setting force
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast add-path-tx

Configures BGP to advertise more than just the best path for a prefix. You can specify `all-paths` to advertise all known paths to the peers in the peer group or `best-per-AS` to advertise only the best path learned from each AS.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast add-path-tx all-paths
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast weight

Configures the weight applied to IPv6 routes received from peer; this is used in the BGP route selection algorithm. You can specify a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast weight 5000
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn

Provides commands to configure l2vpn EVPN for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod

Provides commands to configure the attribute mode for l2vpn EVPN.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath

Provides commands to configure options for handling the `AS_PATH` for prefixes to and from peers in the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn

Provides commands to allow the `AS_PATH` to contain the ASN of the local system.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn occurrences

Indicates the maximum number of times the local system's AS number can be in the received `AS_PATH`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Provides commands to configure policies for l2vpn EVPN for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Provides commands to configure inbound l2vpn EVPN policies for the peer group.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Provides commands to configure the outbound l2vpn-evpn policies.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> password none

Configure the password.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> description none

Configures a description for the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp route-export

Provides commands to configure exporting IPv4 and IPv6 routes from this VRF.

- - -

## nv set vrf \<vrf-id\> router bgp route-export to-evpn

Provides commands to configure exporting routes from this VRF into EVPN.

- - -

## nv set vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\>

A route target Syntax

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rt-id>`   | The route target.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp route-import

Provides commands to configure importing IPv4 and IPv6 routes from this VRF.

- - -

## nv set vrf \<vrf-id\> router bgp route-import from-evpn

Provides commands to configure importing EVPN type-2 and type-5 routes into this VRF.

- - -

## nv set vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\>

Configures the route target syntax.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rt-id>`   |  The route target.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp route-import from-evpn route-target 
```

- - -

## nv set vrf \<vrf-id\> router bgp timers

Provides commands to configure timer values for all peers in this VRF.

- - -

## nv set vrf \<vrf-id\> router bgp timers keepalive

Configures the rate (in seconds) at which BGP sends keepalive messages to all the peers in the specified VRF. BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. You can specify a value between 0 and 65535 or `none`. The default value is 3 seconds.

The keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalives.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp timers keepalive 10
```

- - -

## nv set vrf \<vrf-id\> router bgp timers hold

Configures the hold time (in seconds). By default, BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. If BGP does not receive a keepalive or update message from the peer within the hold time, it declares the peer down and withdraws all routes received by this peer from the local BGP table. 

You can specify a value between 03and 65535 or `none`. The default value is 9 seconds.

The keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalives.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp timers hold 30
```

- - -

## nv set vrf \<vrf-id\> router bgp timers connection-retry

Configures the time interval (in seconds) at which BGP connection attempts are retried after a failure. The default value is 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp timers connection-retry 
```

- - -

## nv set vrf \<vrf-id\> router bgp timers route-advertisement

Configures the delay to insert before advertising the new results to a peer after making a new best path decision for a prefix. This delay rate limits the amount of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. You can set a value between 1 and 600 or `none`. The default value is 0 for both eBGP and iBGP sessions, which allows for fast convergence. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp timers route-advertisement 5
```

- - -

## nv set vrf \<vrf-id\> router bgp timers conditional-advertise

Configures the time interval at which the BGP table is scanned for a condition that is met. You can sepcify a value between 5 and 240 or `none`.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp timers conditional-advertise 20
```

- - -

## nv set vrf \<vrf-id\> router bgp confederation

Provides commands to configure BGP Confederation options in this VRF.

- - -

## nv set vrf \<vrf-id\> router bgp confederation id

Configures the Confederation Identifier to advertise routes outside the confederation; sub-AS numbers are not visible externally. You can set a value between 1 and 4294967295 or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp confederation id 100
```

- - -

## nv set vrf \<vrf-id\> router bgp confederation member-as

Configures the confederation peer ASNs. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp confederation member-as 65101
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\>

Provides commands to configure BGP global configuration.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd

Provides commands to configure tracking BGP peering sessions using this configuration via BFD.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd detect-multiplier

Configures the BFD detect multiplier that determines the maximum number of concurrent BFD packets (including control packets and echo packets) that BGP can discard. You can set a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 bfd detect-multiplier 200
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd enable

Turns BFD on or off to configure tracking BGP peering sessions using this configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 bfd enable on
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd min-rx-interval

Configures the minimum interval for receiving single-hop BFD control packets. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 bfd min-rx-interval 30000
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd min-tx-interval

Configures the minimum interval for transmitting single-hop BFD control packets. You can specify a value between 50 and 60000. The actual value used is the smaller of this value or the value that the peer expects.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 bfd min-tx-interval 30000
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities

Configures BGP capabilities, which the switch advertises to its BGP peers to inform them about the feature it can support and tries to negotiate that capability with its neighbours.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 capabilities
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as

Configures the BGP local AS number, which allows the switch to appear to be a member of a second autonomous system (AS), in addition to its real AS.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as asn

ASN to use to establish the peering if different from the ASN of the BGP instance.  This configuration finds use during AS renumbering.  The local-as configured is also attached to incoming and outgoing updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart

Provides commands to configure BGP Graceful restart per neighbor.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security

Provides commands to configure RFC 5082.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security hops

Number of hops

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family

Provides commands to configure the IPv4 or IPv6 address family.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast

Provides commands to configure the peer IPv4 unicast address family.  Always on, unless disabled globally.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod

Provides commands to configure the attribute mode for IPv4.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath

Provides commands to configure options for handling the AS_PATH for prefixes to and from the peer for IPv4.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn

Turns on or off the option for a received AS_PATH to contain the ASN of the local system.

- - -

## nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn enable

Configures BGP to allow a received AS path to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast allow-my-asn enable on
```

- - - 

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn occurrences

Configues the maximum number of times the local system's AS number can occur in the received AS_PATH.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy

Provides commands to configure policies for ipv4 unicast.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

Provides commands to configure outbound unicast policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound aspath-list none

Configures the AS-Path filter list to apply to updates received from this peer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Provides commands to configure outbound unicast policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound aspath-list none


### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits

Provides commands to configure IPv4 prefix limits.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound

Provides commands to configure limits on inbound IPv4 prefixes from the peer.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound warning-threshold

Configures the percentage of the maximum at which a warning syslog is generated.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound reestablish-wait

Specifes the time in seconds to wait before establishing the IPv4 BGP session again with the peer. 

The default setting is auto, which uses standard BGP timers and processing (typically be 2-3 seconds).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination

Provides commands to configure the default IPv4 route origination.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise

Provides commands to configure community advertisement for IPv4.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise

Provides commands to configure conditional advertisement for IPv4.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise advertise-map \<instance-name\>

Configures the route map that contains the prefix list with a list of IPv4 routes and prefixes on which to operate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise advertise-map ADVERTISEMAP

```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise exist-map \<instance-name\>

Configures a route map that uses a prefix list with the IPv4 routes that must exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise exist-map EXIST
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise non-exist-map \<instance-name\>

Configures a route map that uses a prefix list with the IPv4 routes that must not exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise non-exist-map NONEXIST
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast weight

Configures the weights to apply to IPv4 routes from the peer; this is used in the BGP route selection algorithm.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast weight 10
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast

Provides commands to configure the BGP peer for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod

Provides commands to configure the BGP attribute mode for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath

Provides commands to configure options for handling the AS_PATH for IPv6 prefixes to and from the peer.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn

Turns on or off the option to allow the received AS_PATH to contain the ASN of the local system.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn occurrences

Configures the maximum number of times the local system's AS number can be in the received AS_PATH.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|


### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits

Provides commands to configure limits on IPv6 prefixes from the peer.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound

Provides commands to configure limits on inbound IPv6 prefixes from the peer.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound warning-threshold

Configures the percentage of the maximum at which a warning syslog is generated.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound reestablish-wait

Specifes the time in seconds to wait before establishing the BGP IPv6 session again with the peer. 

The defaults is `auto`, which uses standard BGP timers and processing (typically between 2 and 3 seconds).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination

Provides commands to configure the default IPv6 route origination.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy

Provides commands to configure IPv6 policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound

Provides commands to configure IPv6 outbound unicast policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound aspath-list none

Configures the AS-Path filter list to apply to updates received from the peer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound

Provides commands to configure IPv6 outbound unicast policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound aspath-list none

Configures the AS-Path filter list to apply to updates sent to this peer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise

Provides commands to configure community advertisement for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise

Provides commands to configure conditional advertisement for IPv6.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise advertise-map \<instance-name\>

Configures the route map that contains the prefix-list with the list of IPv6 routes and prefixes on which to operate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise exist-map \<instance-name\>

Configures a route map that uses a prefix list with the IPv6 routes that must exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise non-exist-map \<instance-name\>

Configures a route map that uses a prefix list with the IPv6 routes that must not exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast weight

Configures the weight applied to IPv6 routes from the peer; this is used in the BGP route selection algorithm.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn

Provides commands to configure the peer l2vpn EVPN address family.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod

Provides commands to configure the attribute mode for l2vpn EVPN.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath

Provides commands to configure options for handling AS_PATH for prefixes to and from the peer for l2vpn EVPN.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn

Turns on and off the option for a received AS_PATH to contain the ASN of the local system for l2vpn EVPN.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn occurrences

Configures the maximum number of times the local system's AS number can be in the received AS_PATH.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Provides commands to configure policies for l2vpn EVPN.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Provides commands to configure inbound l2vpn EVPN policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Provides commands to configure outbound l2vpn EVPN policies.

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers

Provides commands to configure BGP peer timers.

- - -

# nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers connection-retry

Configures how often the BGP process attempts to connect to a peer after a failure or when starting up. 

The default value is 10 seconds. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 timers connection-retry 30.
```

- - -

# nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers hold

Configures the hold time in seconds. If BGP does not receive a keepalive or update message from the peer within the hold time, it declares the peer down and withdraws all routes received by this peer from the local BGP table.

The default value is 9 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 timers hold 30.
```

- - -

# nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers keepalive

Configures the interval during which keepalive messages are exchanged. To decrease CPU load when there are a lot of neighbors, you can increase the values of this timer and the hold timer, or disable the exchange of keepalives. When manually configuring new values, the keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalive messages.

The default value is 3 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 timers keepalive 10
```

- - -

# nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers route-advertisement

Configures the delay in seconds before advertising new results to a peer after making a new best path decision for a prefix. This delay rate limits the number of changes advertised to downstream peers and lowers processing requirements by slowing down convergence.

The default value is 0 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The IP address of the BGP peer or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 timers route-advertisement 5
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> password

Configures MD5 authentication for a BGP peer connection to prevent interference with your routing tables. You must set the same password on each BGP peer.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 mypassword
```

- - -

## nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> description

Configures a BGP peer description. If the description is more than one word, enclose the description in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp neighbor swp51 spine01
```

- - -

## nv set vrf \<vrf-id\> router bgp dynamic-neighbor

Configures BGP dynamic neighbors that provide BGP peering to remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor that is in the IP address range and maps to a peer group. 

## nv set vrf \<vrf-id\> router bgp dynamic-neighbor limit

Configures the maximum number of dynamic neighbors from which you can accept a connection. You must also set the `nv set vrf <vrf> router bgp dynamic-neighbor listen-range` command.

You can specify a value between 1 and 5000. The default value is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp dynamic-neighbor limit 5
```

- - -

## nv set vrf \<vrf-id\> router bgp dynamic-neighbor listen-range \<ip-sub-prefix-id\> peer-group

Configures the dynamic neighbor listen range. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<ip-sub-prefix-id>` |   The IP address and prefix. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router bgp dynamic-neighbor listen-range 10.0.1.0/24 peer-group SPINE
```

- - -
