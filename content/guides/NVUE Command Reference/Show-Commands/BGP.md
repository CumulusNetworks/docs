---
title: BGP
author: Cumulus Networks
weight: 130
product: Cumulus Linux
type: nojsscroll
---
## nv show router bgp

Shows global BGP configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router bgp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router bgp convergence-wait

Shows global read-only mode configuration. Read-only mode reduces CPU and network usage when restarting the BGP process.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router bgp convergence-wait
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router bgp graceful-restart

Shows global BGP graceful restart configuration. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router bgp graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp

Shows a summary of the BGP configuration information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family

Shows a summary of the BGP configuration information for the specified VRF for all address families: IPv4 unicast, IPv6 unicast, and EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast

Shows a summary of the BGP IPv4 configuration information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Shows configuration information for BGP IPv4 route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static

Shows configuration information for IPv4 BGP static route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute static 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected

Shows configuration information for BGP IPv4 connected route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute connected
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel

Shows configuration information for BGP IPv4 kernel route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute kernel
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf

Shows configuration information for redistributing OSPF IPv4 routes into BGP for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute ospf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route

Shows BGP IPv4 aggregate routes (a range of networks in your routing table aggregated into a single prefix) for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast aggregate-route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\>

Shows information about a specific BGP IPv4 aggregate route (a range of networks in your routing table aggregated into a single prefix).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.  |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast network

Shows BGP IPv4 static networks for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast network
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\>

Shows information about the specified BGP IPv4 static network for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |
| `<static-network-id>` |   The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast network 10.10.10.101/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import

Shows configuration information about BGP IPV4 route import (route leaking) for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf

Shows configuration information about VRF to VRF IPv4 route leaking.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list

Shows the IPv4 routes in the BGP RIB imported from the VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\>

Shows IPv4 routes in the BGP RIB that leak between VRFs.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<leak-vrf-id>` |  The VRF from which routes are leaked. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf list BLUE
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths

Shows BGP IPv4 multipath configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast multipaths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance

Shows the BGP IPv4 admin distances configured for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast admin-distance
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export

Shows BGP IPv4 route export configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-export
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn

Shows the controls for exporting IPv4 routes from the specified VRF into EVPN (as type-5 routes).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-export to-evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib

Shows the IPv4 local RIB for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route

Shows information about the IPv4 routes in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\>

Shows information about for the specified IPv4 route in the local RIB, such as the BGP peer to which the path is advertised and the path count.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path

Shows information about the paths for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\>

Shows information about a specific IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop

Shows information about the nexthops for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

Shows next hop information for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation |
| `<path-id>` |  The path ID. |
| `<nexthop-id>` | The next hop. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 nexthop 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> peer

Shows BGP peer information for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 peer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> flags

Shows route path flags for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 flags
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

Shows best path information, such as the selection reason, for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 bestpath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> aspath

Shows the AS paths for the specified IPv4 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> community

Shows the community names for the community list for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Shows the community names for the large community list for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` |  The IPv4 address and route prefix in CIDR notation. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

Shows the community names for the extended communities list for the specified IPv4 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<route-id>` | The IPv4 address and route prefix in CIDR notation. |
| `<path-id>`  | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast loc-rib route 10.10.10.3/32 path 2 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group

Shows the BGP IPv4 update groups for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast update-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group \<group-id\>

Shows information about a specific BGP IPv4 update group in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast update-group \<group-id\> sub-group

Shows the subgroups for a specific BGP IPv4 update group in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast update-group 2 subgroups
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast

Shows BGP IPv6 configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route

Shows BGP IPv6 aggregate routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast aggregate-route 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\>

Shows IPv6 aggregate routes. Aggregating a range of networks in your routing table into a single prefix can minimize the size of the routing table and save bandwidth.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<aggregate-route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast aggregate-route 0:0:0:0:0:ffff:0a01:0/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network

Shows the IPv6 static networks for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast network
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\>

Shows information about a specific IPv6 static network for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<static-network-id>`  | The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast network 2001:db8::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import

Shows BGP IPv6 route import configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast route-import
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf

Shows configuration information about VRF to VRF IPv6 route leaking.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast route-import from-vrf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list

Shows IPv6 routes in the BGP RIB that are dynamically leaked between VRFs.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast route-import from-vrf list
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths

Shows BGP IPv6 multipath configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast multipaths
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance

Shows the BGP IPv6 admin distances configured for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast admin-distance
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export

Shows BGP IPv6 route export configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast route-export
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn

Shows BGP IPv6 route export to EVPN configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast route-export to-evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute

Shows configuration information for BGP IPv6 route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static

Shows configuration information for BGP IPv6 static route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute static
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected

Shows configuration information for BGP IPv6 connected route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute connected
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel

Shows configuration information for BGP IPv6 kernel route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute kernel
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6

Shows configuration information for BGP OSPF IPv6 route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast redistribute ospf6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib

Shows the IPv6 local RIB for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\>

Shows information about for the specified IPv6 route in the local RIB, such as the BGP peer to which the path is advertised and the path count.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<route-id>` |  The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path

Shows the paths for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\>

Shows information about the paths for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop

Shows the next hops for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

Shows next hop information for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |
| `<nexthop-id>` | The next hop. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 nexthop 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> peer

Shows BGP peer information for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 peer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> flags

Shows route path flags for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 flags
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

Shows best path information, such as the selection reason, for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 bestpath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> aspath

Shows the AS paths for the specified IPv6 route in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> community

Shows the community names for the community list for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Shows the community names for the large community list for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 large-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

Shows the community names for the extended community list for the specified IPv6 route path in the local RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   The VRF name.|
| `<route-id>` | The IPv6 address and route prefix in CIDR notation. |
| `<path-id> ` | The path ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast loc-rib route 2001:db8::1/128 path 2 ext-community
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast update-group

Shows the BGP IPv6 update groups for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast update-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast update-group \<group-id\>

Shows information about a specific BGP IPv6 update group in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast update-group 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast update-group \<group-id\> sub-group

Shows the subgroups for a specific BGP IPv6 update group in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<group-id>` | The group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family ipv6-unicast update-group 2 subgroups
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn

Shows EVPN BGP configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib

Shows the EVPN local RIB for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd

Shows the EVPN local RIB <span style="background-color:#F5F5DC">[RDs](## "Route Distinguisher")</span> for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\>

Shows a specific EVPN local RIB <span style="background-color:#F5F5DC">[RD](## "Route Distinguisher")</span> for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type

Shows the EVPN local RIB <span style="background-color:#F5F5DC">[RD](## "Route Distinguisher")</span> route distinguisher route types (`ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5) for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\>

Shows information about a specific EVPN local RIB <span style="background-color:#F5F5DC">[RD](## "Route Distinguisher")</span> route distinguisher route type for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\> route

Shows the routes in the EVPN local RIB for the specified VRF with a specific <span style="background-color:#F5F5DC">[RD](## "Route Distinguisher")</span> and route type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast route
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn loc-rib rd \<rd-id\> route-type \<route-type-id\> route \<evpn-route-id\>

Shows the routes in the EVPN local RIB for the specified VRF with a specific <span style="background-color:#F5F5DC">[RD](## "Route Distinguisher")</span> route type and EVPN route type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<rd-id>` |  The route distinguisher ID.|
| `<route-type-id>` |  The route type: `ead`, `macip`, `multicast`, `ethernet-segment`, `prefix`, or an integer between 1 and 5.|
| `<evpn-route-id>` |  The EVPN route type.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn loc-rib rd 10.10.10.1:20 route-type multicast route 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group

Shows information about BGP EVPN update group events.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group \<group-id\>

Shows information about a specific BGP EVPN update group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<group ID>` |  The BGP group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn update-group \<group-id\> sub-group

Shows the subgroup information for a specific BGP EVPN update group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<group ID>` |  The BGP group ID.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp address-family l2vpn-evpn update-group 5 sub-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast route-counters

Shows the number of IPv4 routes for a specific BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast route-counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes

Shows information about the IPv4 advertised routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\>

Shows information about a specific IPv4 advertised route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path

Shows path information about a specific IPv4 advertised route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\>

Shows information about a specific IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> nexthop

Shows information about the next hops for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

Shows information about the a specific next hop for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |
| `<nexthop-id>` |   The next hop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 nexthop 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> peer

Shows information about the peers for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 peer -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> flags

Shows information about the flags for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 flags -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> bestpath

Shows information about the bestpath for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> aspath

Shows information about the AS path for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> community

Shows information about the communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> large-community

Shows information about the large communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast advertised-routes \<route-id\> path \<path-id\> ext-community

Shows information about the extended communities for an IPv4 advertised route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The VRF name. |
| `<route-id>` |   The IPv4 advertised route. |
| `<path-id>` |   The IPv4 advertised route path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast advertised-routes 10.10.10.1/32 path 1 ext-community -o json
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes

Shows information about the IPv4 received routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\>

Shows information about a specific IPv4 received route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv4 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path

Shows information about a specific IPv4 received route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv4 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\>

Shows information about a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> nexthop

Shows information about the next hops for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

Shows information about a specific next hop for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |
| `<nexthop-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 nexthop 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> peer

Shows information about peers for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 peer -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> flags

Shows information about flags for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 flags -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> bestpath

Shows information about the best paths for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> aspath

Shows information about the AS paths for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> community

Shows information about the communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> large-community

Shows information about the large communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast received-routes \<route-id\> path \<path-id\> ext-community

Shows information about the extended communities for a specific IPv4 received route path ID for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv4 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast received-routes 10.0.1.2/32 path 1 ext-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes

Shows information about the IPv6 received routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\>

Shows information about a specific IPv6 received route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path

Shows information about IPv6 received route paths for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\>

Shows information about a specific IPv6 received route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> nexthop

Shows information about the IPv6 received route path nexthops for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1  nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

Shows information about a specific IPv6 received route path nexthop for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |
| `<nexthop-id>` |   The nexthop ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 nexthop 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> peer

Shows information about the IPv6 received route path peers for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 peer 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> flags

Shows information about the IPv6 received route path flags for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 flags -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> bestpath

Shows information about the IPv6 received route path bestpath for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> aspath

Shows information about the IPv6 received route path AS path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> community

Shows information about the IPv6 received route path communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> large-community

Shows information about the IPv6 received route path large communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast received-routes \<route-id\> path \<path-id\> ext-community

Shows information about the IPv6 received route path extended communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast received-routes 2001:db8::1/128 path 1 ext-community -o json
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast route-counters

Shows the number of IPv6 routes for a specific BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast route-counters -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes

Shows information about the IPv6 advertised routes for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\>

Shows information about a specific IPv6 advertised route for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |   The VRF name. |
| `<route-id>` |   The IPv6 route. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path

Shows information about the IPv6 advertised route paths for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\>

Shows information about a specific IPv6 advertised route path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path 1 -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> nexthop

Shows information about the IPv6 advertised route nexthops for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path 1 nexthop -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> peer

Shows information about the IPv6 advertised route peers for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path 1 peers -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> flags

Shows information about the IPv6 advertised route flags for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes  2001:db8::1/128 path 1 flags -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> bestpath

Shows information about the IPv6 advertised route best path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 bestpath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> aspath

Shows information about the IPv6 advertised route AS path for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 aspath -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> community

Shows information about the IPv6 advertised route communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> large-community

Shows information about the IPv6 advertised route large communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 large-community -o json
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast advertised-routes \<route-id\> path \<path-id\> ext-community

Shows information about the IPv6 advertised route extended communities for a BGP neighbor in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF name or interface (for unnumbered BGP). |
| `<neighbor-id>` |  The IP address of the BGP peer or the interface if you are using unnumbered BGP. |
| `<route-id>` |   The IPv6 route. |
| `<path-id>` |   The path ID. |


### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast advertised-routes 2001:db8::1/128 path 1 ext-community -o json
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show evpn vni \<vni-id\> bgp-info

Shows BGP information for the specified EVPN VNI.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vni-id>` |   The VNI name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show evpn vni 10 bgp-info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> evpn bgp-info

Shows layer 3 VNI BGP information from BGP for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default evpn bgp-info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp confederation

Shows BGP confederation configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp confederation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp confederation member-as

Shows the BGP confederation member AS. A BGP confederation divides a large AS into subautonomous systems, which are uniquely identified by a sub-AS number.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp confederation member-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp dynamic-neighbor

Shows BGP dynamic neighbor configuration on the switch. BGP dynamic neighbors provides BGP peering to remote neighbors within a specified range of IPv4 or IPv6 addresses for a BGP peer group. You can configure each range as a subnet IP address.

After you configure the dynamic neighbors, a BGP speaker can listen for, and form peer relationships with, any neighbor that is in the IP address range and maps to a peer group.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp dynamic-neighbor
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp dynamic-neighbor listen-range

Shows the address range configuration for BGP peering to remote neighbors.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp dynamic-neighbor listen-range
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp dynamic-neighbor listen-range \<ip-sub-prefix-id\>

Shows information about a specific address range for BGP peering to remote neighbors.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp dynamic-neighbor listen-range 10.0.1.0/24
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\>

Shows global configuration for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  | The BGP neighbor name or interface (for BGP unnumbered). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd

Shows BFD configuration for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 bfd
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities

Shows the capabilities for the specified BGP neighbor, such as if extended next hop and 32-bit ASN transmission are enabled.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as

Shows the local AS for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 local-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart

Shows BGP graceful restart configuration for the specified BGP neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security

Shows BGP TTL security configuration for the specified BGP neighbor. BGP TTL security prevents attacks against eBGP, such as denial of service (DoS) attacks.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 ttl-security
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> nexthop

Shows the BGP neighbor next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> message-stats

Message statistics

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ebgp-policy

Shows the Default External BGP (EBGP) route propagation behavior for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 ebgp-policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family

Shows all address family configuration for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast

Shows configuration information for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod

Shows the attribute modification configuration settings for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn

Shows if it is acceptable for a received AS path from the specified IPv4 neighbor to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy

Shows the policies for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

Shows the inbound policy for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Shows the outbound policy for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits

Shows the limits on prefixes from the specified IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound

Shows the limits on inbound prefixes from the specified IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination

Shows default route origination configuration for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast default-route-origination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise

Shows community advertise configuration information for the specified BGP IPv4 neighbor. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast community-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise

Shows conditional advertisement configuration information for the specified BGP IPv4 neighbor. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast capabilities

Shows all advertised and received capabilities for the specified BGP IPv4 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart

Shows BGP graceful restart configuration information for the specified BGP IPv4 neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast

Shows configuration information for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod

Shows the attribute modification configuration settings for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn

Shows if it is acceptable for a received AS path from the specified IPv6 neighbor to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits

Shows limits on prefixes from the specified IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound

Shows the limits on inbound prefixes from the specified IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination

Shows default route origination configuration for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast default-route-origination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy

Shows policies for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound

Shows the inbound policy for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound

Shows the outbound policy for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise

Shows community advertise configuration information for the specified BGP IPv6 neighbor. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast community-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise

Shows conditional advertisement configuration information for the specified BGP IPv6 neighbor. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast capabilities

Shows all advertised and received capabilities for the specified BGP IPv6 neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart

Shows BGP graceful restart configuration information for the specified BGP IPv6 neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn

Shows EVPN configuration for the specified BGP neighbor.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod

Shows the attribute modification configuration settings for the specified neighbor for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath

Shows the configuration options for handling the AS path for prefixes to and from the specified BGP neighbor for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn

Shows if it is acceptable for a received AS path to contain the ASN of the local system for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Shows EVPN policies for the specified neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Shows the inbound EVPN policy for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Shows the outbound EVPN policy for the specified BGP neighbor.


### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn capabilities

Shows all advertised and received EVPN capabilities for the specified BGP neighbor.


### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart

Shows graceful restart configuration for the specified BGP peer for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers

Shows timer configuration for the specified BGP peer, such as the reconnect, advertisement and keepalive intervals, and the hold time.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp neighbor swp52 timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop

Shows BGP next hop information for the specified VRF.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop \<afi\>

Shows BGP next hop information for IPv4 or IPv6 for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address

Shows BGP IPv4 or IPv6 next hops for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\>

Shows information about a specific BGP IPv4 or IPv6 next hop for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\> resolved-via

Shows the recursive BGP IPv4 or IPv6 next hops for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 10.10.10.101 resolved-via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\> path

Shows all paths associated with BGP IPv4 or IPv6 nexthops for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 2001:2:2::4 path
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp nexthop \<afi\> ip-address \<ip-address-id\> path \<path-id\>

Shows information about a specific path associated with BGP IPv4 or IPv6 nexthops for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<afi>` |  The address family: IPv4 or IPv6. |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |
| `<path-id>` |  The path ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp nexthop ipv4 ip-address 2001:2:2::4 path 1 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp path-selection

Shows the BGP path selection configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp path-selection
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp path-selection aspath

Shows the BGP aspath path selection configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp path-selection med

Shows the BGP med path selection configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp path-selection med
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp path-selection multipath

Shows BGP multipath path-selection configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp path-selection multipath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group

Shows the peer groups configured for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\>

Shows global configuration for the specified peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd

Shows BFD configuration for the specified BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES bfd
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security

Shows BGP TTL security configuration for the specified BGP peer group. BGP TTL security prevents attacks against eBGP, such as denial of service (DoS) attacks.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES ttl-security
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities

Shows the capabilities for the specified BGP peer group, such as if extended next hop and 32-bit ASN transmission are enabled.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES capabilities
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart

Shows BGP graceful restart configuration for the specified peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES graceful-restart
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as

Shows the local AS for the specified BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES local-as
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers

Shows BGP timer configuration for the peer group in the specified VRF, such the conditional advertisement, connection retry,
and keepalive interval and the hold time for keepalive messages.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES timers
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family

Shows configuration information for the address families (IPv4, IPv6, EVPN).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast

Shows the configuration for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise

Shows community advertise configuration information for the specified BGP IPv4 peer group. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast community-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod

Shows the attribute modification configuration settings for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn

Shows if it is acceptable for a received AS path from the specified BGP IPv4 peer group to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits

Shows the limits on prefixes from the specified IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound

Shows the limits on inbound prefixes from the specified IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast prefix-limits inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination

Shows default route origination configuration for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast default-route-origination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Shows the policies configured for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Shows the inbound policy for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Shows the outbound policy for the specified BGP IPv4 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise

Shows conditional advertisement configuration information for the specified BGP IPv4 peer group. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv4-unicast conditional-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast

Shows the configuration for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Shows the policies for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Shows the inbound policy for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Shows the outbound policy for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn

Shows if it is acceptable for a received AS path from the specified BGP IPv6 peer group to contain the ASN of the local system.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits

Shows the limits on prefixes from the specified IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound

Shows the limits on inbound prefixes from the specified IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast prefix-limits inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination

Shows default route origination configuration for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast default-route-origination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise

Shows community advertise configuration information for the specified BGP IPv6 peer group. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast community-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod

Shows the attribute modification configuration settings for the specified BGP IPv6 peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise

Shows conditional advertisement configuration information for the specified BGP IPv6 peer group. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family ipv6-unicast conditional-advertise
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn

Show configuration information for the specified BGP peer group for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>` | The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod

Shows the attribute modification configuration settings for the specified BGP peer group for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn attribute-mod
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified BGP peer group for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn

Shows if it is acceptable for a received AS path from the specified BGP peer group to contain the ASN of the local system for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn aspath allow-my-asn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Shows the EVPN policies for the specified BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Shows the inbound EVPN policy for the specified BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |   The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy inbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Shows the outbound EVPN policy for the specified BGP peer group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<peer-group-id>`  |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp peer-group SPINES address-family l2vpn-evpn policy outbound
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-export

Shows BGP route export configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-export
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-export to-evpn

Shows BGP route export to EVPN configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-export to-evpn route-target 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target

Shows the RTs configured for BGP route export for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-export to-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\>

Shows BGP route export configuration for the specified RT in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<rt-id>` |  The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-export to-evpn route-target 65101:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-import

Shows BGP route import configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-import
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-import from-evpn

Shows BGP route import from EVPN configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-import from-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target

Shows the RTs configured for BGP route import from EVPN for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-import from-evpn route-target
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\>

Shows configuration for the specified RD and layer 3 RT for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rt-id>` | The route target. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-import from-evpn route-target 65102:4001
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp route-reflection

Shows BGP route-reflection configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp route-reflection
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router bgp timers

Shows BGP timer configuration for all peers in the specified VRF, such the conditional advertisement, connection retry,
and keepalive interval and the hold time for keepalive messages.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router bgp timers
```
