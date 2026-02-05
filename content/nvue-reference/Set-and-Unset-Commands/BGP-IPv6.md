---
title: BGP IPv6
author: Cumulus Networks
weight: 522

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance external</h>

Configures the distance to apply to IPv6 routes from eBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast admin-distance external 150
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance internal</h>

Configures the distance to apply to IPv6 routes from iBGP peers when installed into the RIB. You can specify a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast admin-distance internal 110
```
<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast advertise-origin</h>

Configures BGP prefix independent convergence (PIC) for IPv6 to reduce data plane convergence times and improve unicast traffic convergence for remote link failures (when the BGP next hop fails). A remote link is a link between a spine and a remote leaf, or a spine and the super spine layer.

When you configure BGP PIC, Cumulus Linux assigns one next hop group for each source and the remote leaf advertises the router ID loopback route. The remote leaf tags prefix routes with a route-origin extended community so that the local leaf recognizes the routes. When the network topology changes, the local leaf obtains the router ID loopback route with the updated ECMP, allowing a O (1) next hop group replace operation for all prefixes from the remote leaf without waiting for individual BGP updates.

You enable the BGP advertise origin option on a leaf switch, so that BGP can attach the Site-of-Origin (SOO) extended community to all routes advertised to its peers from the source where the routes originate. On all switches (leaf, spine and super spine), you enable the next hop group per source option (`nv set vrf <vrf-id> router bgp address-family ipv6-unicast nhg-per-origin`) so that when BGP receives routes with the SOO extended community, it allocates a next hop group for each source.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast advertise-origin
```
-->

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> as-set</h>

Enables and disables generation of an `AS_SET` for the aggregate for the specified VRF. When `enabled`, BGP creates an aggregate address with a mathematical set of autonomous systems. The `AS_SET` option summarizes the `AS_PATH` attributes of all the individual IPv6 routes to help BGP detect and avoid loops. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 as-set enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> route-map</h>

Applies a route map to the aggregate IPv6 route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\> summary-only</h>

Ensures that BGP suppresses longer IPv6 prefixes inside the aggregate address before sending updates. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast aggregate-route 2001:db8::1/128 summary-only enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast state</h>

Enables and disables BGP for IPv6 for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths compare-cluster-length</h>

Turns on cluster length comparison for IPv6 for the specified VRF. When `on` and iBGP paths have a cluster list, their lengths must be equal to be selected as multipaths. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast compare-cluster-length enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths ebgp</h>

Configures the number of equal-cost eBGP paths allowed for the specified VRF. You can specify a value between 1 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast multipaths ebgp 120
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths ibgp</h>

Configures the number of equal-cost iBGP paths allowed for IPv6 for the specified VRF. You can specify a value between 1 and 128.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast multipaths ibgp 120
```

<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast nhg-per-origin</h>

Configures BGP prefix independent convergence (PIC) for IPv6 to reduce data plane convergence times and improve unicast traffic convergence for remote link failures (when the BGP next hop fails). A remote link is a link between a spine and a remote leaf, or a spine and the super spine layer.

When you configure BGP PIC, Cumulus Linux assigns one next hop group for each source and the remote leaf advertises the router ID loopback route. The remote leaf tags prefix routes with a route-origin extended community so that the local leaf recognizes the routes. When the network topology changes, the local leaf obtains the router ID loopback route with the updated ECMP, allowing a O (1) next hop group replace operation for all prefixes from the remote leaf without waiting for individual BGP updates.

You enable the next hop group per source option on all switches (leaf, spine and super spine), so that when BGP receives routes with the SOO extended community, it allocates a next hop group for each source. On a leaf switch, you enable the BGP advertise origin option (`nv set vrf <vrf-id> router bgp address-family ipv6-unicast advertise-origin`) so that BGP can attach the Site-of-Origin (SOO) extended community to all routes advertised to its peers from the source where the routes originate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast nhg-per-origin
```
-->
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected state</h>

Enables and disables route redistribution of IPv6 connected routes for the specified VRF. The default setting is `disabled`.

Route redistribution allows a network to use a routing protocol to route traffic dynamically based on the information learned from a different routing protocol or from static routes. Route redistribution helps increase accessibility within networks.

{{%notice note%}}
- In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
- This command does not export link-local IPv6 addresses as global addresses but treats them as neighbor entries in the EVPN fabric.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected metric</h>

Configures the metric you want to use for the redistributed connected IPv6 route for the specified VRF. You can specify auto or a value between 0 and 4294967295. If you specify `auto`, the switch chooses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected metric 4294967295
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected route-map</h>

Applies a route map to the redistributed connected IPv6 route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute connected route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel state</h>

Enables and disables redistribution of IPv6 kernel routes for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel metric</h>

Configures the metric you want to use for the redistributed kernel route for the specified VRF. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch chooses an appropriate value based on the type of route.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel metric 4294967295
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel route-map</h>

Applies a route map to the redistributed IPv6 route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute kernel route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 state</h>

Enables and disables redistribution of OSPF IPv6 routes for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 metric</h>

Configures the metric you want to use for the redistributed OSPF routes for the specified VRF. You can specify `auto` or a value between 0 and 4294967295. If you specify `auto`, the switch chooses an appropriate value based on the type of route. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf metric 4294967295
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6 route-map</h>

Applies a route map to the redistributed IPv6 route for the specified VRF. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute ospf route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static state</h>

Enables and disables route redistribution of IPv6 static routes for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static metric</h>

Configures the metric you want to use for the redistributed IPv6 route for the specified VRF. You can specify `auto`, or a value between 0 and 4294967295. If you specify `auto`, the switch chooses an appropriate value based on the type of route. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static metric 4294967295
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static route-map</h>

Applies the route map to the redistributed static IPv6 route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast redistribute static route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast rib-filter</h>

Applies a route map on IPv6 route updates from BGP to the Route Information Base (RIB) for the specified VRF. You can match on prefix, next hop, communities, and so on. You can set the metric and next hop only. Route maps do not affect the BGP internal RIB. Route maps work on multi-paths; however, BGP bases the metric setting on the best path only.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast rib-filter routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn default-route-origination</h>

Configures originating EVPN default type-5 routes for the specified VRF. The default type-5 route originates from a border (exit) leaf and advertises to all the other leafs within the pod. Any leaf within the pod follows the default route towards the border leaf for all external traffic (towards the Internet or a different pod). The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn default-route-origination enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn state</h>

Enables and disables IPv6 prefix-based routing for EVPN type-5 routes for the specified VRF. When `enabled`, the switch can announce IPv6 prefixes in the BGP RIB as EVPN type-5 routes. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn route-map</h>

Applies the route map to control how IPv6 routes export into EVPN for the specified VRF. By default, when announcing IPv6 prefixes in the BGP RIB as EVPN type-5 routes, the switch selects all routes in the BGP RIB to advertise as EVPN type-5 routes. You can use a route map to allow selective route advertisement from the BGP RIB.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unicast route-export to-evpn route-map HIGH-PRIO
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf state</h>

Enables and disables IPv6 route leaking for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list \<leak-vrf-id\></h>

Configures the VRF from which to import IPv6 routes. You can specify multiple VRFs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<leak-vrf-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf list BLUE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf route-map \<instance-name\></h>

Applies a route map to control importing IPv6 routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED router bgp address-family ipv6-unicast route-import from-vrf route-map BLUEtoRED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unreachability advertise-origin</h>

Configures BGP conditional disaggregation to attach the SOO for BGP unreachability information signaling for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unreachability advertise-origin
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unreachability advertise-unreach interfaces-match</h>

Configures unreachability advertisements for interfaces matching a network for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp address-family ipv6-unreachability advertise-unreach interfaces-match 2001:1:1::/48
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp address-family ipv6-unreachability state</h>

Enables and disables BGP unreachability (failure signaling) globally for BGP conditional disaggregation for IPv6. You can specify `enabled` or `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ cumulus@leaf01:~$ nv set vrf default router bgp address-family ipv6-unreachability state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn enable</h>

Enables or disables the option to allow the received AS_PATH to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath allow-my-asn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn occurrences</h>

Configures the maximum number of times the local system's AS number can be in the received AS_PATH.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath allow-my-asn occurrences
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn origin</h>

Configures whether a received AS_PATH containing the ASN of the local system is allowed, but only if it is the originating AS. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath allow-my-asn origin enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod aspath</h>

Configures BGP to follow normal IPv6 BGP procedures when generating the `AS_PATH` attribute for the neighbor in the specified VRF. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast attribute-mod aspath enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod nexthop</h>

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the specified neighbor. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change `NEXT_HOP` when sending an update to the neighbor.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast attribute-mod nexthop enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod med</h>

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the specified neighbor. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change the `MED` when sending an update to the neighbor.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast attribute-mod med enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise regular</h>

Configures BGP to announce the `COMMUNITIES` attribute to the neighbor for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast community-advertise regular enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise extended</h>

Configures BGP to announce the `EXT_COMMUNITIES` attribute to the neighbor for the specified VRF. The default setting is `enabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast community-advertise extended enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise large</h>

Configures BGP to announce the `LARGE_COMMUNITIES` attribute to the neighbor for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast community-advertise large enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise advertise-map \<instance-name\></h>

Configures the route map that contains the prefix-list with the list of IPv6 routes and prefixes on which to operate.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise advertise-map MAP2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise enable</h>

Enables and disables community advertisement on the neighbor for IPv6.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise exist-map \<instance-name\></h>

Applies a route map that uses a prefix list with the IPv6 routes that must exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise exist-map MAP3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise non-exist-map \<instance-name\></h>

Configures a route map that uses a prefix list with the IPv6 routes that must not exist in the routing table.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise non-exist-map MAP4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination state</h>

Enables and disables IPv6 default route origination for the neighbor. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast default-route-origination state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination policy</h>

Configures the optional route map policy to control the conditions under which the IPv6 default route is originated for the neighbor. The default setting is `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast default-route-origination policy mypolicy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast state</h>

Enables and disables IPv6 for the neighbor. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast nexthop-setting</h>

Configures the BGP next hop value of advertised IPv6 routes for the BGP neighbor. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to itself for route advertisement excluding reflected routes, or `force` to set the next hop to itself for route advertisement including reflected routes. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast nexthop-setting force
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound aspath-list</h>

Configures the AS-Path filter list to apply to updates received from the neighbor.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy inbound aspath-list myaspathlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound prefix-list</h>

Configures the prefix list you want to apply to updates received from the neighbor for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy inbound prefix-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound route-map</h>

Configures the route map you want to apply to updates received from the neighbor for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy inbound route-map myroutemap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound aspath-list</h>

Configures the AS-Path filter list to apply to updates sent to this neighbor.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound aspath-list LISTOUT
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound prefix-list</h>

Configures the prefix list you want to apply to updates sent to the neighbor for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound prefix-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound route-map</h>

Configures the route map you want to apply to updates sent to the neighbor for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound route-map myroutemap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound unsuppress-map</h>

Configures the route map you want to use to unsuppress routes selectively when advertising to this neighbor; these are routes that have been suppressed due to aggregation configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound unsuppress-map none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound maximum</h>

Configures the maximum number of IPv6 prefixes that BGP can receive from the neighbor for the specified VRF. By default, there is no limit.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits inbound maximum 50000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound reestablish-wait</h>

Specifes the time in seconds to wait before establishing the BGP IPv6 session again with the neighbor after reaching the prefix limit. The defaults is `auto`, which uses standard BGP timers and processing (typically between 2 and 3 seconds).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits inbound reestablish-wait 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound warning-only</h>

Configures the switch to generate a warning syslog only (without bringing down the BGP session) when the number of prefixes received reaches the threshold. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp1 address-family ipv6-unicast prefix-limits inbound warning-only on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound warning-threshold</h>

Configures when to generate a warning syslog message and bring down the BGP session. This is a percentage of the maximum inbound prefix limit. You can set a value between 0 and 100. Alternatively, you can configure the switch to generate a warning syslog message only without bringing down the BGP session with the `nv set vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound warning-only on` command.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp1 address-family ipv6-unicast prefix-limits inbound warning-threshold 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast route-reflector-client</h>

Configures the BGP node as a route reflector for the BGP neighbor. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast route-reflector-client enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft-reconfiguration</h>

Turns on soft configuration so that received IPv6 routes from the neighbor that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast soft-reconfiguration enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast weight</h>

Configures the weight applied to IPv6 routes from the neighbor; this is used in the BGP route selection algorithm. You can set a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<neighbor-id>`   | The IPv6 address of the BGP neighbor or the interface if you are using unnumbered BGP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unicast weight 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath allow-my-asn occurrences</h>

Configures the maximum number of occurrences of the local system's AS number in the received AS_PATH. You can set a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath allow-my-asn occurrences 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath allow-my-asn origin</h>

Configures BGP to allow a received AS_PATH containing the ASN of the local system but only if it is the originating AS. You can specify `enabled` or `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath allow-my-asn origin enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath allow-my-asn route-map</h>

Applies the route map to filter IPv6 routes with my AS in the AS_PATH. Allows selective application of `allowas-in` based on route map matching.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath allow-my-asn route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath allow-my-asn state</h>

Enables and disables the local system's AS number in the received AS_PATH. You can specify `enabled` or `disabled`. The default setting is `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath allow-my-asn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath private-as</h>

Configures how to handle private ASNs in the update to the peer. You can specify:
- `none` to take no action. This is the default setting.
- `remove` to remove any private ASNs in the update to the peer
- `replace` to replace any private ASNs in the update to the peer  with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath private-as replace
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability aspath replace-peer-as</h>

Configures BGP to replace the ASN of the peer in the AS_PATH of an outgoing update with the ASN of the local system. You can specify `enabled` or `disabled`. The default setting is `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability aspath replace-peer-as enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability prefix-limits maximum </h>

Configures the maximum number of unreachability prefixes that can be received from the peer. This is CRITICAL for security to prevent state exhaustion.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability prefix-limits maximum 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability prefix-limits reestablish-wait</h>

Configures the time in minutes to wait before establishing the BGP session again with the peer for unreachability. The default value is `auto`, which uses standard BGP timers and processing.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability prefix-limits reestablish-wait 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability prefix-limits warning-only</h>

Configures the switch to only generate a warning syslog if the number of received unreachability prefixes exceeds the limit, but does not bring down the BGP session. You can set this option to `enabled` or `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability prefix-limits warning-only enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability prefix-limits warning-threshold</h>

Configures the prefix limits for a neighbor for BGP conditional disaggregation. Sets the percentage of the maximum at which a syslog warning is generated. You can set the value between 1 and 100. The default value is 75.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability prefix-limits warning-threshold 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unreachability state</h>

Enables and disables BGP unreachability (failure signaling) on the neighbor. The default value is disabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp neighbor swp51 address-family ipv6-unreachability state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast add-path-tx</h>

Configures BGP to advertise more than just the best path for a prefix. You can specify `all-paths` to advertise all known paths to the peers in the peer group or `best-per-AS` to advertise only the best path learned from each AS. The default setting is disabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast add-path-tx all-paths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn enable</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast allow-my-asn enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn occurrences</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast allow-my-asn occurrences 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn origin</h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast allow-my-asn origin on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath private-as</h>

Configures what action to take with private ASNs. You can specify `none` to take no action, `remove`, to remove any private ASNs in the update to the peers in the peer group, or `replace` to replace any private ASNs in the update to the peers with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath private-as replace
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath replace-peer-as</h>

Configures BGP to replace the AS path in an outgoing update that contains the ASN of the peers in the peer group with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath replace-peer-as on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod aspath</h>

Configures BGP to follow normal IPv6 BGP procedures when generating the `AS_PATH` attribute for the peer group in the specified VRF. You can specify `enabled` or `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod aspath enabled
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod med</h>

Configures BGP to follow normal BGP procedures when generating the `MED` attribute for the specified peer group. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change the `MED` when sending an update to the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod med enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod nexthop</h>

Configures BGP to follow normal BGP procedures when generating the `NEXT_HOP` attribute for the specified peer group. You can specify `enabled` or `disabled`. If you set this attribute to `disabled`, BGP does not change `NEXT_HOP` when sending an update to the peer group.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod nexthop enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise regular</h>

Configures BGP to announce the `COMMUNITIES` attribute to the peer group for the specified VRF. Ypu can specify `enabled` or `disabled`. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise regular enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise extended</h>

Configures BGP to announce the `EXT_COMMUNITIES` attribute to the peer group for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise extended enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise large</h>

Configures BGP to announce the `LARGE_COMMUNITIES` attribute to the peer group for the specified VRF. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise large enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise state</h>

Enables or disables BGP conditional advertisement for IPv6 for the peer group. The default setting is `disabled`.

BGP conditional advertisement lets you advertise certain routes only if other routes either do or do not exist. BGP conditional advertisement is typically used in multihomed networks where BGP advertises some prefixes to one of the providers only if information from the other provider is not present. For example, a multihomed router can use conditional advertisement to choose which upstream provider learns about the routes it provides so that it can influence which provider handles traffic destined for the downstream router. This is useful for cost of service, latency, or other policy requirements that are not natively accounted for in BGP.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise advertise-map \<instance-name\></h>

Configures the route map that contains the prefix list with the list of IPv6 routes or prefixes you want to advertise for the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise advertise-map myadvertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise exist-map \<instance-name\></h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise exist-map EXIST  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise non-exist-map \<instance-name\></h>

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
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise non-exist-map NONEXIST 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination state</h>

Enables and disables IPv6 default route origination. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast default-route-origination state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination policy</h>

Configures the optional route map policy to control the conditions under which the IPv6 default route is originated. The default setting is `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast default-route-origination policy mypolicy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast state</h>

Enables and disables IPv6 for the BGP peer group. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast nexthop-setting</h>

Configures the BGP next hop value of advertised IPv6 routes for the peers in the peer group. You can specify `auto` to follow regular BGP next hop determination rules, `self` to set the next hop to itself for route advertisement excluding reflected routes, or `force` to set the next hop to itself for route advertisement including reflected routes. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast nexthop-setting force
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound route-map</h>

Configures the IPv6 route map you want to apply to updates received from the peers in the peer group.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound route-map routemap1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound prefix-list</h>

Configures the prefix list you want to apply to updates received from the peers in the peer group for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound prefix-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound aspath-list none</h>

Configures the AS path filter list you want to apply to updates received from the peers in the peer group for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound aspath-list MYASPATHLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound aspath-list none</h>

Configures the AS path filter list you want to apply to updates sent to the peers in the peer group for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound aspath-list myaspathlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound prefix-list</h>

Configures the IPv6 prefix list you want to apply to updates to be sent to the peers in the peer group for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound prefix-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound unsuppress-map</h>

Configures the route map used to unsuppress IPv6 routes selectively when advertising to the peers in the peer group for the specified VRF. These are routes that have been suppressed due to aggregation configuration.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound unsuppress-map myunsuppress
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound maximum</h>

Configures the maximum number of IPv6 prefixes that BGP can receive from the peers in the peer group for the specified VRF. By default, there is no limit.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound maximum 50000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound warning-threshold</h>

Configures when to generate a warning syslog message and bring down the BGP session. This is a percentage of the maximum inbound prefix limit. You can set a value between 0 and 100. Alternatively, you can configure the switch to generate a warning syslog message only without bringing down the BGP session with the `nv set vrf <vrf-id> router bgp peer-group <peeer-group> address-family ipv6-unicast prefix-limits inbound warning-only on` command.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound warning-threshold 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound warning-only</h>

Configures the switch to generate a warning syslog message only (without bringing down the BGP session) when the number of prefixes received reaches the threshold. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound warning-only on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound reestablish-wait</h>

Configures the time in seconds to wait before establishing the BGP session again with the peers in the peer group. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound reestablish-wait 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast route-reflector-client</h>

Configures the BGP node as a route reflector for the BGP peer group. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast route-reflector-client enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft-reconfiguration</h>

Turns on soft configuration so that received IPv6 routes from the peers in the peer group that are rejected by inbound policy are still stored. This allows policy changes to take effect without any exchange of BGP updates. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast soft-reconfiguration enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast weight</h>

Configures the weight applied to IPv6 routes received from the peer group; this is used in the BGP route selection algorithm. You can specify a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group SPINES address-family ipv6-unicast weight 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath allow-my-asn occurrences</h>

Configures the maximum number of occurrences of the local system's AS number in the received AS_PATH for the peer group. You can set a value between 1 and 10.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability aspath allow-my-asn occurrences 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath allow-my-asn origin</h>

Configures BGP to allow a received AS_PATH containing the ASN of the local system but only if it is the originating AS for the peer group. You can specify `enabled` or `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability aspath allow-my-asn origin enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath allow-my-asn route-map</h>

Applies the route map to filter IPv6 routes with my AS in the AS_PATH. Allows selective application of `allowas-in` based on route map matching. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability aspath allow-my-asn route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath allow-my-asn state</h>

Enables and disables the local system's AS number in the received AS_PATH for the peer group. You can specify `enabled` or `disabled`. The default setting is `disabled`. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability aspath allow-my-asn state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath private-as</h>

Configures how to handle private ASNs in the update to the peer group. You can specify:
- `none` to take no action. This is the default setting.
- `remove` to remove any private ASNs in the update to the peer.
- `replace` to replace any private ASNs in the update to the peer  with the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability aspath private-as replace
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability aspath replace-peer-as</h>

Configures BGP to replace the ASN of the peer in the AS_PATH of an outgoing update with the ASN of the local system for the peer group. You can specify `enabled` or `disabled`. The default setting is `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability aspath replace-peer-as enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability prefix-limits maximum</h>

Configures the maximum number of unreachability IPv6 prefixes that can be received from the peer group. This is CRITICAL for security to prevent state exhaustion.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability prefix-limits maximum 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability prefix-limits reestablish-wait</h>

Configures the time in minutes to wait before establishing the BGP session again with the peer group for unreachability. The default value is `auto`, which uses standard BGP timers and processing. 

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability prefix-limits reestablish-wait 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability prefix-limits warning-only</h>

Configures the switch to only generate a warning syslog if the number of received unreachability IPv6 prefixes exceeds the limit, but does not bring down the BGP session. You can set this option to `enabled` or `disabled`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability prefix-limits warning-only enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability prefix-limits warning-threshold</h>

Configures the prefix limits for a peer group for BGP conditional disaggregation. Sets the percentage of the maximum at which a syslog warning is generated. You can set the value between 1 and 100. The default value is 75.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability prefix-limits warning-threshold 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unreachability state</h>

Enables and disables IPv6 BGP unreachability (failure signaling) for the peer group. The default value is disabled.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set vrf default router bgp peer-group UNDERLAY-LEAF address-family ipv6-unreachability state enabled
```
