---
title: BGP
author: Cumulus Networks
weight: 520

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp</h>

Configures BGP globally on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp autonomous-system</h>

Configures the BGP <span class="a-tooltip">[ASN](## "Autonomous System Number ")</span> on the switch to identify the BGP node. You can set a value between 1 and 4294967295. To use auto BGP to assign an ASN automatically on the leaf, set the value to `leaf`. To use auto BGP to assign an ASN automatically on the spine, set the value to `spine`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp autonomous-system 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp convergence-wait</h>

Configures BGP readonly mode. Sometimes, as Cumulus Linux establishes BGP peers and receives updates, it installs prefixes in the RIB and advertises them to BGP peers before receiving and processing information from all the peers. Also, depending on the timing of the updates, Cumulus Linux sometimes installs prefixes, then withdraws and replaces them with new routing information. Readonly mode minimizes this BGP route churn in both the local RIB and with BGP peers.

Enable readonly mode to reduce CPU and network usage when restarting the BGP process. Because intermediate best paths are possible for the same prefix as peers establish and start receiving updates at different times, readonly mode is useful in topologies where BGP learns a prefix from a large number of peers and the network has a high number of prefixes.

While in readonly mode, BGP does not run best-path or generate any updates to its peers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp convergence-wait establish-wait-time</h>

Configures BGP readonly mode by setting the establish wait time. You can set a value between 0 and 3600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp convergence-wait establish-wait-time 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp convergence-wait time</h>

Configures BGP readonly mode by setting the convergence wait time. You can set a value between 0 and 3600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp convergence-wait time 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp enable</h>

Turns BGP `on` or `off` globally on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp graceful-restart</h>

Configures BGP graceful restart globally on the switch to minimize the negative effects that occur when BGP restarts. All BGP peers inherit the graceful restart capability.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp graceful-restart mode</h>

Configures the BGP graceful restart mode globally on the switch. You can specify the following settings:
- `off`, where graceful restart is not negotiated with peers.
- `helper-only`, where the switch is in a helper role only, and routes originated and advertised from a BGP neighbor in the peer group are not deleted.
- `full`, where the switch is in both a helper and restarter role.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp graceful-restart mode helper-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp graceful-restart path-selection-deferral-time</h>

Configures the number of seconds a restarting neighbor defers path-selection when waiting for the EOR marker from peers. The default is 120 seconds. You can set a value between 0 and 3600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp graceful-restart path-selection-deferral-time 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp graceful-restart restart-time</h>

Configures the number of seconds to wait for a graceful restart capable neighbor to re-establish BGP peering. The default is 120 seconds. You can set a value between 0 and 4095.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp graceful-restart restart-time 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp graceful-restart stale-routes-time</h>

Configures the number of seconds to hold stale routes for a restarting neighbor. The default is 360 seconds. You can set a value between 1 and 4095.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp graceful-restart stale-routes-time 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp graceful-shutdown</h>

Turns BGP graceful shutdown on or off on the switch to reduce packet loss during planned maintenance of a router or link. BGP graceful shutdown forces traffic to route around the BGP node.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp graceful-shutdown on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp policy-update-timer</h>

Configures the BGP policy update timer globally on the switch to wait the specified number of seconds before processing updates to policies to ensure that a series of changes process together. You can set a value between 0 and 600.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp policy-update-timer 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp queue-limit input</h>

Configures the input message queue limit for all peers. You can set a value between 1 and 4294967295 messages. The default setting is 10000.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set router bgp queue-limit input 2048
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp queue-limit output</h>

Configures the output message queue limit for all peers. You can set a value between 1 and 4294967295 messages. The default setting is 10000.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set router bgp queue-limit output 2048
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp router-id</h>

Configures the BGP router ID on the switch. NVUE automatically assigns the loopback address of the switch to be the router ID. FRR automatically assigns the router ID to be the loopback address or the highest IPv4 address for the interface. If you do not have a loopback address configured or want to use a specific router ID, set the router ID globally.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp router-id 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router bgp wait-for-install</h>

Turns BGP wait for install on or off. When BGP *wait for install* is on, BGP waits for a response from the RIB indicating that the routes installed in the RIB are also installed in the ASIC before sending updates to peers.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router bgp wait-for-install on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance external</h>

Configures the distance to apply to IPv4 routes from eBGP peers when installed into the RIB. You can specify a value between 1 and 255.

The BGP administrative distance lets the switch choose which routing protocol to use when two different protocols provide IPv4 route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from BGP with an administrative distance of 100, the switch chooses BGP.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance external 150
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance internal</h>

Configures the distance to apply to IPv4 routes from iBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast admin-distance internal 110
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast advertise-origin</h>

BGP prefix independent convergence (PIC) reduces convergence times and improves unicast traffic convergence for remote link and node failures (when the BGP next hop fails) regardless of route scale. A remote link is a link between a spine and a remote leaf, or a spine and the super spine layer.

When you configure BGP PIC, Cumulus Linux assigns one next hop group for each source and the remote leaf advertises a route with a prefix derived from the router ID. The remote leaf tags prefix routes with a route-origin extended community (SOO) so that the local leaf recognizes the routes. When the network topology changes, the local leaf obtains the router ID route with the updated ECMP, allowing a O (1) next hop group replace operation for all prefixes from the remote leaf without waiting for individual BGP updates.

You enable the BGP advertise origin option on a leaf switch, so that BGP can attach the Site-of-Origin (SOO) extended community to all routes advertised to its peers from the source where the routes originate. On all switches (leaf, spine and super spine), you enable the next hop group per source option (`nv set vrf <vrf-id> router bgp address-family ipv4-unicast nhg-per-origin`) so that when BGP receives routes with the SOO extended community, it allocates a next hop group for each source.

{{%notice note%}}
On a spine and super spine, you must set the read-only mode BGP convergence wait time to 30 (`nv set router bgp convergence-wait time 30`)and the convergence wait establish wait time to 15 (`nv set router bgp convergence-wait establish-wait-time 15`). These are the minimum recommended timer settings to ensure optimal convergence when using PIC.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast advertise-origin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast nhg-per-origin</h>

BGP prefix independent convergence (PIC) reduces convergence times and improves unicast traffic convergence for remote link and node failures (when the BGP next hop fails) regardless of route scale. A remote link is a link between a spine and a remote leaf, or a spine and the super spine layer.

When you configure BGP PIC, Cumulus Linux assigns one next hop group for each source and the remote leaf advertises a route with a prefix derived from the router ID. The remote leaf tags prefix routes with a route-origin extended community (SOO) so that the local leaf recognizes the routes. When the network topology changes, the local leaf obtains the router ID route with the updated ECMP, allowing a O (1) next hop group replace operation for all prefixes from the remote leaf without waiting for individual BGP updates.

You enable the next hop group per source option on all switches (leaf, spine and super spine), so that when BGP receives routes with the SOO extended community, it allocates a next hop group for each source. On a leaf switch, you enable the BGP advertise origin option (`nv set vrf <vrf> router bgp address-family ipv4-unicast advertise-origin`) so that BGP can attach the Site-of-Origin (SOO) extended community to all routes advertised to its peers from the source where the routes originate.

{{%notice note%}}
On a spine and super spine, you must set the read-only mode BGP convergence wait time to 30 (`nv set router bgp convergence-wait time 30`)and the convergence wait establish wait time to 15 (`nv set router bgp convergence-wait establish-wait-time 15`). These are the minimum recommended timer settings to ensure optimal convergence when using PIC.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast nhg-per-origin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\> as-set</h>

Turns generation of an `AS_SET` for route aggregate on or off for the specified VRF. When `on`, BGP creates an aggregate address with a mathematical set of autonomous systems. The `AS_SET` option summarizes the `AS_PATH` attributes of all the individual routes to help BGP detect and avoid loops. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 as-set on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\> route-map</h>

Applies a route map to the IPv4 aggregate route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\> summary-only</h>

Configures BGP to suppress longer IPv4 prefixes inside the aggregate address before sending updates. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16 summary-only on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast enable</h>

Tuns the BGP IPv4 address family on or off for the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths</h>

Configures the maximum number of equal-cost BGP paths allowed for IPv4 for the specified VRF. The BGP multipath option is on by default and the maximum number of paths is 64 so that the switch can install multiple equal-cost BGP paths to the forwarding table and load balance traffic across multiple links. You can change the number of paths allowed, according to your needs. 1 disables the BGP multipath option.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast multipaths 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths ebgp</h>

Configures the number of equal-cost eBGP paths allowed for IPv4 for the specified VRF. The default value is 64.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ebgp 120
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths ibgp</h>

Configures the number of equal-cost iBGP paths allowed for IPv4 for the specified VRF. The default value is 64.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast multipaths ibgp 120
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths compare-cluster-length</h>

Turns on cluster length comparison for IPv4 for the specified VRF. When `on` and iBGP paths have a cluster list, their lengths must be equal to be selected as multipaths. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast compare-cluster-length on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\></h>

Configures the IPv4 prefixes to originate from a BGP node for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\> route-map</h>

Applies a route map to the IPv4 prefixes that originate from a BGP node for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<static-network-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32 route-map HI-PRIO
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast rib-filter</h>

Applies a route map on IPv4 route updates from BGP to the Route Information Base (RIB). You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast rib-filter routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn default-route-origination</h>

Configures originating EVPN default type-5 routes for the specified VRF. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod). The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn default-route-origination on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn enable</h>

Turns IPv4 prefix-based routing using EVPN type-5 routes on or off for the specified VRF. When `on`, the switch can announce IP prefixes in the BGP RIB as EVPN type-5 routes. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn route-map</h>

Sets the route map to control the export of IPv4 routes into EVPN for the specified VRF. By default, when announcing IP prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv4-unicast route-export to-evpn route-map HIGH-PRIO
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\></h>

Configures the VRF from which to import (leak) IPv4 routes. You can specify multiple VRFs.

VRF route leaking is where a destination VRF wants to know the routes of a source VRF. As routes come and go in the source VRF, they dynamically leak to the destination VRF through BGP.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<leak-vrf-id>`  | The VRF from which you want to leak routes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf list BLUE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf enable</h>

Turns IPv4 VRF route leaking on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf route-map \<instance-name\></h>

Applies a route map to control importing IPv4 routes for the specified VRF. For example, to exclude certain prefixes from the import process, configure the prefixes in a route map.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv4-unicast route-import from-vrf route-map BLUEtoRED
```

## <h>nv set vrf \<vrf-id\> router bgp autonomous-system</h>

Configures the BGP <span class="a-tooltip">[ASN](## "Autonomous System Number ")</span> in the specified VRF to identify the BGP node. You can set a value between 1 and 4294967295. To use auto BGP to assign an ASN automatically on the leaf, set the value to `leaf`. To use auto BGP to assign an ASN automatically on the spine, set the value to `spine`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp autonomous-system 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp confederation id</h>

Configures the Confederation Identifier to advertise routes outside the confederation; sub-AS numbers are not visible externally. You can set a value between 1 and 4294967295 or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp confederation id 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp confederation member-as</h>

Configures the confederation neighbor ASNs. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp confederation member-as 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp dynamic-neighbor</h>

Configures BGP dynamic neighbors that provide BGP peering to remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

After you configure the dynamic neighbors, a BGP speaker can listen for, and form neighbor relationships with, any neighbor that is in the IP address range and maps to a peer group.

## <h>nv set vrf \<vrf-id\> router bgp dynamic-neighbor limit</h>

Configures the maximum number of dynamic neighbors from which you can accept a connection. You must also set the `nv set vrf <vrf-id> router bgp dynamic-neighbor listen-range` command. You can specify a value between 1 and 5000. The default value is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp dynamic-neighbor limit 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp dynamic-neighbor listen-range \<ip-sub-prefix-id\> peer-group</h>

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
cumulus@switch:~$ nv set vrf default router bgp dynamic-neighbor listen-range 10.0.1.0/24 peer-group SPINES
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp enable</h>

Turns BGP on or off for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd detect-multiplier</h>

Configures the BFD detect multiplier that determines the maximum number of concurrent BFD packets (including control packets and echo packets) that BGP can discard. You can set a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd detect-multiplier 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd enable</h>

Turns BFD on or off to configure tracking BGP peering sessions using this configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd min-rx-interval</h>

Configures the minimum interval for receiving single-hop BFD control packets. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`  | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd min-rx-interval 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd min-tx-interval</h>

Configures the minimum interval for transmitting single-hop BFD control packets. You can specify a value between 50 and 60000. The actual value used is the smaller of this value or the value that the neighbor expects.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 bfd min-tx-interval 30000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities</h>

Configures BGP capabilities, which the switch advertises to its BGP peers to inform them about the feature it can support and tries to negotiate that capability with its neighbours.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities extended-nexthop</h>

Turns on or off advertisement of IPv4 prefixes with IPv6 next hops over global IPv6 peerings. You must add the extended nexthop capability to the global IPv6 neighbor statements on each end of the BGP sessions.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 capabilities extended-nexthop on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities source-address</h>

Configures the source IP address of the TCP connection, which is often used as the BGP next hop for updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 capabilities source-address 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> description</h>

Configures a description for the BGP neighbor in the specified VRF. If the description is more than one word, enclose it in double quotes (").

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 description SPINE01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> enforce-first-as</h>

Configures BGP to check that the first AS matches the AS of the neighbor when BGP updates are received from eBGP neighbors with this configuration. You can specify `on` or `off`.


### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 enforce-first-as on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as</h>

Configures BGP local AS, which allows the switch to appear to be a member of a second autonomous system (AS), in addition to its real AS.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as asn</h>

Configures the ASN to use to establish the peering if different from the ASN of the BGP instance. The local configured AS is also attached to incoming and outgoing updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 local-as asn 65532
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as enable</h>

Turns BGP local AS on or off, which allows the switch to appear to be a member of a second autonomous system (AS), in addition to its real AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 local-as enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as prepend</h>

Turns local AS prepend on or off. When on, BGP prepends the configured local AS to received updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>` | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 local-as prepend on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> multihop-ttl</h>

Configures the maximum number of hops allowed. You can specify a value between 1 and 255 or `auto`. The default setting is `auto`, where the type of neighbor determines the appropriate value (255 for iBGP and 1 for eBGP).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 multihop-ttl 25
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> nexthop-connected-check</h>

Turns next hop connected check on or off. If you set the value to `on`, BGP disables checking that a non-multihop eBGP neighbor is directly connected and only announces connected next hops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 nexthop-connected-check on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> passive-mode</h>

Turns passive mode on so that the switch does not initiate the BGP connection but waits for an incoming connection. If you set the command to `off`, the switch initiates the BGP connection without waiting for an incoming connection.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 passive-mode on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as replace</h>

Turns local AS replace on or off. When on, BGP attaches only the configured local AS to generated updates, *replacing* the AS number configured for the BGP instance with the local AS applicable for the peering. When off, BGP attach the AS number of the BGP instance and then prepends it with the configured local AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 local-as replace on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart mode</h>

Configures the BGP graceful restart mode for the neighbor session. You can specify the following settings:
- `off`, where graceful restart is not negotiated with peers.
- `helper-only`, where the switch is in a helper role only, and routes originated and advertised from a BGP neighbor in the peer group are not deleted. 
- `full`, where the switch is in both a helper and restarter role.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 graceful-restart mode helper-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security enable</h>

Turns TTL security (RFC 5082) on or off for the neighbor session.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 ttl-security enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security hops</h>

Configures the TTL security hop count to prevent attacks against eBGP, such as denial of service (DoS) attacks. By default, BGP messages to eBGP neighbors have an IP time-to-live (TTL) of 1, which requires the neighbor to be directly connected, otherwise, the packets expire along the way. You can adjust the TTL with the eBGP multihop option. An attacker can adjust the TTL of packets so that they look like they originate from a directly connected neighbor.

The BGP TTL security hops option inverts the direction in which BGP counts the TTL. Instead of accepting only packets with a TTL of 1, Cumulus Linux accepts BGP messages with a TTL greater than or equal to 255 minus the specified hop count.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 ttl-security hops 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn enable</h>

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
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast allow-my-asn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>
 

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn occurrences</h>

Configures the maximum number of times the local system AS number can occur in the received AS_PATH.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast allow-my-asn occurrences 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound aspath-list</h>

Configures the AS Path filter list to apply to updates received from this neighbor.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound aspath-list ASPATHIN
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound aspath-list none</h>

Applies the IPv4 outbound policy for the specified AS_PATH list.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound aspath-list ASPATHOUT
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound warning-threshold</h>

Configures the percentage of the maximum at which a warning syslog is generated. You can set a value between 1 and 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits inbound warning-threshold 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound reestablish-wait</h>

Specifes the time in seconds to wait before establishing the IPv4 BGP session again with the neighbor. You can set a value between 1 and 4294967295. The default setting is auto, which uses standard BGP timers and processing (typically between 2-3 seconds).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits inbound reestablish-wait 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise advertise-map \<instance-name\></h>

Configures the route map that contains the prefix list with a list of IPv4 routes and prefixes on which to operate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise advertise-map ADVERTISEMAP

```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise exist-map \<instance-name\></h>

Configures a route map that uses a prefix list with the IPv4 routes that must exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise exist-map EXIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise non-exist-map \<instance-name\></h>

Configures a route map that uses a prefix list with the IPv4 routes that must not exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise non-exist-map NONEXIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast weight</h>

Configures the weights to apply to IPv4 routes from the neighbor; this is used in the BGP route selection algorithm.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv4 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv4-unicast weight 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> enable</h>

Turns the exchange of information with a BGP neighbor on or off in the specified VRF. The default value is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> shutdown</h>

Administratively shuts down a specific neighbor in the specified VRF. You can specify `on` or `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 shutdown on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers connection-retry</h>

Configures how often the BGP process attempts to connect to a neighbor after a failure or when starting up. The default value is 10 seconds. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 timers connection-retry 30.
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers hold</h>

Configures the hold time in seconds. If BGP does not receive a keepalive or update message from the neighbor within the hold time, it declares the neighbor down and withdraws all routes received by this neighbor from the local BGP table. The default value is 9 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 timers hold 30.
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers keepalive</h>

Configures the interval during which keepalive messages are exchanged. To decrease CPU load when there are a lot of neighbors, you can increase the values of this timer and the hold timer, or disable the exchange of keepalives. When manually configuring new values, the keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalive messages. The default value is 3 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 timers keepalive 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers route-advertisement</h>

Configures the delay in seconds before advertising new results to a neighbor after making a new best path decision for a prefix. This delay rate limits the number of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. The default value is 0 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   |  The IP address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 timers route-advertisement 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> password</h>

Configures MD5 authentication for a BGP neighbor connection to prevent interference with your routing tables. You must set the same password on each BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 mypassword
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> peer-group</h>

Configures the peer group in which the specified BGP neighbor belongs. The BGP neighbor inherits the group's configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 peer-group SPINES
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> remote-as</h>

Configures BGP to establish a connection between two eBGP peers that are not directly connected. You can set a value between 1 and 4294967295, `auto`, `internal`, or `external`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor 10.10.10.101 peer-group remote-as external
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> type</h>

Configures the BGP neighbor type in the specified VRF. You can set a value of `numbered` or `unnumbered`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 type unnumbered
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> update-source</h>

Configures the BGP source of routing updates. You can specify an interface, or an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IP address of the BGP neighbor or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 update-source 10.10.10.5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection aspath compare-lengths</h>

Configures BGP to select the AS based on path length for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp path-selection aspath compare-lengths on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection aspath compare-confed</h>

Configures BGP to select the AS based on confederations for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp path-selection aspath compare-confed on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection med compare-always</h>

Configures BGP to always compare the MED on routes even when received from different neighboring autonomous systems. When enabled, BGP compares MEDs for all paths.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection med compare-always on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection med compare-deterministic</h>

Applies route selection for the specified VRF in a way that produces deterministic answers locally.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection med compare-deterministic on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection med compare-confed</h>

Configures MED for route-selection based on confederations for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection med compare-confed on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection med missing-as-max</h>

Turns BGP MED missing-as-max on or off for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection med missing-as-max on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection multipath aspath-ignore</h>

Configures BGP to ignore the AS path when determining multipath routing for the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection multipath aspath-ignore on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection multipath generate-asset</h>

Turns BGP multipath generate asset on or off for the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection multipath generate-asset on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection multipath bandwidth</h>

Configures multipath route selection based on bandwidth for the specified VRF. You can specify `bandwidth`, `all-paths`, `skip-missing`, `default-weight-for-missing`, or `ignore`. The default setting is `ignore`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection multipath bandwidth all-paths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp path-selection routerid-compare</h>

Configures BGP to use the router ID to decide the best path when the switch receives two identical routes from two different peers. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp path-selection routerid-compare on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast add-path-tx</h>

Configures BGP to advertise more than just the best path for a prefix. You can specify `all-paths` to advertise all known paths to the peers in the peer group or `best-per-AS` to advertise only the best path learned from each AS. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast add-path-tx all-paths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn occurrences</h>

Configures the maximum number of times BGP allows the ASN for the local system in the received `AS_PATH`. You can specify a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath allow-my-asn occurrences 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn origin</h>

Configures BGP to allow a received `AS_PATH` containing the ASN of the local system, but only if it is the originating AS.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath allow-my-asn origin on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath replace-peer-as</h>

Configures BGP to replace the AS path in an outgoing update that contains the ASN of the neighbor with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath replace-peer-as on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath private-as</h>

Configures what action to take with private ASNs for the peer group in the specified VRF. You can specify `none` to take no action, `remove`, to remove any private ASNs in the update to the neighbors, or `replace` to replace any private ASNs in the update to the neighbors with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath private-as replace
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod aspath</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod aspath on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod med</h>

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the peer group in the specified VRF. You can specify `on` or `off`. If you set this attribute to `off`, BGP does not change the `MED` when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod med on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod nexthop</h>

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the peer group in the specified VRF. You can specify `on` or `off`. If you set this attribute to `off`, BGP does not change `NEXT_HOP` when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod nexthop on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise regular</h>

Configures BGP to announce the `COMMUNITIES` attribute to the peer group in the specified VRF. You can specify `on` or `off`. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise regular off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise extended</h>

Configures BGP to announce the `EXT_COMMUNITIES` attribute to the peer group in the specified VRF. You can specify `on` or `off`. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise extended off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise large</h>

Configures BGP to announce the `LARGE_COMMUNITIES` attribute to the peer group in the specified VRF. You can specify `on` or `off`. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise large off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise enable</h>

Turns BGP conditional advertisement for IPv4 on or off. The default setting is `off`.

BGP conditional advertisement lets you advertise certain routes only if other routes either do or do not exist. BGP conditional advertisement is typically used in multihomed networks where BGP advertises some prefixes to one of the providers only if information from the other provider is not present. For example, a multihomed router can use conditional advertisement to choose which upstream provider learns about the routes it provides so that it can influence which provider handles traffic destined for the downstream router. This is useful for cost of service, latency, or other policy requirements that are not natively accounted for in BGP.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise advertise-map \<instance-name\></h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise advertise-map myadvertise 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise exist-map \<instance-name\></h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise exist-map EXIST 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise non-exist-map \<instance-name\></h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise non-exist-map NONEXIST 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast enable</h>

Turns IPv4 on or off for the BGP peer group in the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast nexthop-setting</h>

Configures the BGP next hop value of advertised IPv4 routes for the peers in the peer group. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to ourselves for route advertisement excluding reflected routes, or `force` to set the next hop to ourselves for route advertisement including reflected routes. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast nexthop-setting force
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound maximum</h>

Configures the maximum number of inbound IPv4 prefixes allowed from the peer group in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound maximum 3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound warning-threshold</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound warning-threshold 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound reestablish-wait</h>

Configures the time in seconds to wait before establishing the BGP session again with the peers in the peer group. You can specify a value between 1 and 4294967295. A value of `auto` uses standard BGP timers and processing (between 2 and 3 seconds). The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound reestablish-wait 3000000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound route-map</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound route-map myroutemap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound prefix-list</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound prefix-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound aspath-list none</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound aspath-filter myaspathlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound aspath-list none</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound aspath-list myaspathlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound prefix-list</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound prefix-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound route-map</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound route-map myroutemap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound unsuppress-map</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound unsuppress-map myunsuppress
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast route-reflector-client</h>

Configures the BGP node as a route reflector for the BGP peer group in the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast route-reflector-client on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft-reconfiguration</h>

Turns on soft configuration so that received IPv4 routes from peers in the peer group that are rejected by an inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast soft-reconfiguration on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast weight</h>

Configures the weight applied to IPv4 routes received from peer group in the specified VRF. This is used in the BGP route selection algorithm.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv4-unicast weight 65535
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd enable</h>

Turns BFD on or off for the BGP peer group in the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES bfd enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd detect-multiplier</h>

Configures the BFD interval multiplier for the BGP peer group in the specified VRF. You can specify a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES bfd detect-multiplier 4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd min-rx-interval</h>

Configures the minimum interval between received BFD control packets for the BGP peer group in the specified VRF. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES bfd min-rx-interval 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd min-tx-interval</h>

Configures the minimum interval between sending BFD control packets for the BGP peer group in the specified VRF. You can specify a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES bfd min-tx-interval 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities extended-nexthop</h>

Turns the extended next hop capability defined in RFC 5549 on or off in the specified VRF. The extended nexthop is advertised to peers in the peer group. If you specify `auto`, extended next hop is `on` for unnumbered peers and `off` otherwise. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES capabilities extended-nexthop on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities source-address</h>

Configures the source IP address of the TCP connection for the peer group, which is often used as the BGP next hop for updates.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES capabilities source-address 10.10.10.1
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> description</h>

Configures a description for the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES description none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-shutdown</h>

Enables and disables graceful shutdown on a peer group. You can specify `on` or `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group underlay graceful-shutdown on  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as asn</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES local-as asn 65101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as enable</h>

Turns local AS on or off for the peer group. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES local-as enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as prepend</h>

Configures BGP to prepend the configured local AS to updates for the peer group in the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES local-as enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as replace</h>

Configures BGP to either attach only the configured local AS to generated updates or attach the ASN of the BGP instance, then prepend it with the configured local AS. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES local-as replace on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> password none</h>

Configures a password for the BGP peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES password none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers connection-retry</h>

Configures the time interval at which BGP attempts to connect to a neighbor in the peer group after a failure. You can specify a value between 1 and 65535. If you specify `auto`, BGP uses the global value. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES timers connection-retry 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers keepalive</h>

Configures the interval at which BGP exchanges periodic keepalive messages to measure and ensure that a peer is still alive and functioning. You can specify a value between 1 and 65535. If you specify `none`, BGP does not send keepalives. If you specify `auto`, BGP uses the global value. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES timers keepalive 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers hold</h>

Configures the hold timer for the peer group in the specified VRF. If BGP does not receive a keepalive or update message from a neighbor in the peer group within the hold time, it declares the neighbor down and withdraws all routes received by this neighbor from the local BGP table. If you specify `none`, BGP does not track keepalives from the neighbor and the peering session does not experience a hold timeout. You can specify a value between 3 and 65535. If you specify `auto`, BGP uses the global value. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES timers hold 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers route-advertisement</h>

Configures the time between route advertisements (BGP updates) for the BGP group in the specified VRF. After making a new best path decision for a prefix, BGP can insert a delay before advertising the new results to a neighbor. This delay rate limits the number of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. You can specify a value between 1 and 65535. If you specify `none`, BGP delays and sends route advertisements in batches. If you specify `auto`, BGP uses the global value. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES timers route-advertisement 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security enable</h>

Turns BGP TTL security on or off in the specified VRF.

Use this option to prevent attacks against eBGP, such as denial of service (DoS). By default, BGP messages to eBGP neighbors have an IP time-to-live (TTL) of 1, which requires the neighbor to be directly connected, otherwise, the packets expire along the way. An attacker can adjust the TTL of packets so that they look like they originate from a directly connected neighbor. The BGP TTL security hops option inverts the direction in which BGP counts the TTL. Instead of accepting only packets with a TTL of 1, Cumulus Linux accepts BGP messages with a TTL greater than or equal to 255 minus the specified hop count.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES ttl-security enable on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security hops</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES ttl-security hops 200 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp rd</h>

Configures the BGP route distinguisher (RD) in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf RED router bgp rd 10.1.20.2:5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\></h>

Configures the tenant VRF <span class="a-tooltip">[RTs](## "route targets")</span> (layer 3 RTs) for BGP route export.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rt-id>`   | The route target.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp route-export to-evpn route-target 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\></h>

Configures the tenant VRF <span class="a-tooltip">[RTs](## "route targets")</span> (layer 3 RTs) for BGP route import.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rt-id>`   |  The route target.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp route-import from-evpn route-target 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp route-reflection enable</h>

Turns BGP route reflection on or off. The default setting is `off`.

When you configure an iBGP speaker as a route reflector, it can send iBGP learned routes to other iBGP peers.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp route-reflection enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp route-reflection cluster-id</h>

Configures the cluster ID to use during route reflection. When route reflection is on, you must set the cluster ID.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp route-reflection cluster-id 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp route-reflection reflect-between-clients</h>

Allows routes to be reflected between clients for the specified VRF. Typically, routes are reflected only between clients and non-clients, with the clients of a route reflector expected to be fully meshed. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp route-reflection reflect-between-clients on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp route-reflection outbound-policy</h>

Allows an outbound neighbor policy to modify the attributes for reflected routes. Typically, reflected routes have to retain their original attributes. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp route-reflection outbound-policy on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp router-id</h>

Configures the router ID in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example 

```
cumulus@switch:~$ nv set vrf default router bgp router-id 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp timers conditional-advertise</h>

Configures the time interval at which the BGP table is scanned for a condition that is met. You can sepcify a value between 5 and 240 or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp timers conditional-advertise 20
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp timers connection-retry</h>

Configures the time interval (in seconds) at which BGP connection attempts are retried after a failure. The default value is 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp timers connection-retry 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp timers hold</h>

Configures the hold time (in seconds). By default, BGP exchanges periodic keepalive messages to measure and ensure that a neighbor is still alive and functioning. If BGP does not receive a keepalive or update message from the neighbor within the hold time, it declares the neighbor down and withdraws all routes received by this neighbor from the local BGP table. 

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
cumulus@switch:~$ nv set vrf default router bgp timers hold 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp timers keepalive</h>

Configures the rate (in seconds) at which BGP sends keepalive messages to all the peers in the specified VRF. BGP exchanges periodic keepalive messages to measure and ensure that a neighbor is still alive and functioning. You can specify a value between 0 and 65535 or `none`. The default value is 3 seconds.

The keepalive interval can be less than or equal to one third of the hold time, but cannot be less than 1 second. Setting the keepalive and hold time values to 0 disables the exchange of keepalives.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp timers keepalive 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp timers route-advertisement</h>

Configures the delay to insert before advertising the new results to a neighbor after making a new best path decision for a prefix. This delay rate limits the number of changes advertised to downstream peers and lowers processing requirements by slowing down convergence. You can set a value between 1 and 600 or `none`. The default value is 0 for both eBGP and iBGP sessions, which allows for fast convergence. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp timers route-advertisement 5
```
