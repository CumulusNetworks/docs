---
title: BGP Commands
author: Cumulus Networks
weight: 120
product: Cumulus Linux
type: nojsscroll
---
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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family

Shows a summary of the BGP configuration information for the specified VRF for all address families: IPv4 unicast, IPv6 unicast, and layer 2 VPN - EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast

Shows a summary of the IPv4 BGP configuration information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Shows configuration information for IPv4 BGP route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute static 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected

Shows configuration information for IPv4 BGP connected route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute connected
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel

Shows configuration information for IPv4 BGP kernel route redistribution for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute kernel
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf

Shows configuration information for redistributing IPv4 OSPF routes into BGP for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast redistribute ospf
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\>

Shows information about the specified BGP IPv4 aggregate route (a range of networks in your routing table aggregated into a single prefix).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.  |
| `<aggregate-route-id>` |  The IPv4 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast aggregate-route 10.1.0.0/16
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast 10.10.10.101/32
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\>

Shows routes in the BGP routing table of VRF BLUE dynamically leak into VRF RED.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<leak-vrf-id>` |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp address-family ipv4-unicast route-import from-vrf list BLUE
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths

Multipaths

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance

Admin distances.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export

Route export

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn

Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib

IPv4 local RIB

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\>

An IPv4/IPv6 route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` |  IPv4 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-i\> path \<path-id\>

An IPv4/IPv6 route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |  IPv4 address and route prefix in CIDR notation |
| `<path-id>` |  Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

An IPv4/IPv6 route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>`   | IPv4 address and route prefix in CIDR notation|
| `<path-id>`    | Path Id|
| `<nexthop-id>` | Nexthop Id|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> peer

Nexthop peer information

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> flags

Route flags

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

A bestpath information

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`  | IPv4 address and route prefix in CIDR notation |
| `<path-id>`   | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> aspath

AS paths

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>`   | IPv4 address and route prefix in CIDR notation |
| `<path-id>`    | Path| 

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> community

Set of community names for community-list

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>`  | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Set of community names for large community list

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>`  | IPv4 address and route prefix in CIDR notation |
| `<path-id>`   | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

extended communities

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` | IPv4 address and route prefix in CIDR notation |
| `<path-id>`  | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn

BGP VRF configuration. L2VPN EVPN address family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast

IPv6 unicast address family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\>

An IPv6 aggregate route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<aggregate-route-id>` |  IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\>

An IPv6 static network.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-network-id>`  | IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import

Route import

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf

Controls for VRF to VRF route leaking for this address-family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list

Set of VRFs

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths

Multipaths

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance

Admin distances.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export

Route export

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn

Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute

Route redistribute

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static

Source route type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected

Source route type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel

Source route type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6

Source route type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib

IPv6 local RIB

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\>

An IPv4/IPv6 route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |  IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\>

An IPv4/IPv6 route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` | IPv6 address and route prefix in CIDR notation |
| `<path-id> ` | Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

An IPv4/IPv6 route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |
| `<nexthop-id>` |Nexthop Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> peer

Nexthop peer information

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> flags

Route flags

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

A bestpath information

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> aspath

AS paths

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> community

Set of community names for community-list

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Set of community names for large community list

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

extended communities

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | VRF |
| `<route-id>`   |IPv6 address and route prefix in CIDR notation |
| `<path-id>`    |Path Id |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp path-selection

BGP path-selection configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp path-selection aspath

BGP aspath path-selection config, applicable to this BGP instance

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp path-selection med

BGP med path-selection config, applicable to this BGP instance

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp path-selection multipath

BGP multipath path-selection config, applicable to this BGP instance

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-reflection

BGP route-reflection configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\>

BGP global configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security

RFC 5082

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities

Capabilities

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as

Local AS feature

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers

Peer peer-timers

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family

Address family specific configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise

Conditional advertise for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options]`

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-export

Controls for exporting ipv4 and ipv6 routes from this VRF

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-export to-evpn

Controls for exporting routes from this VRF into EVPN

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\>

A route target identifier

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rt-id>` |  Route targets or "auto" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-import

Controls for importing of ipv4 and ipv6 routes from this VRF

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-import from-evpn

Controls for importing EVPN type-2 and type-5 routes into this VRF

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\>

 A route target identifier

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rt-id>` | Route targets or "auto" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp timers

timer values for all peers in this VRF

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp confederation

BGP Confederation options.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp confederation member-as

Set of autonomous numbers

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\>

BGP global configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities

Capabilities

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as

Local AS feature

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |   Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security

RFC 5082

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> nexthop

Nexthop

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`   | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 ebgp-policy
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast

Show configuration information for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod

Shows the attribute modification configuration settings for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast attribute-mod
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast aspath allow-my-asn
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy

Shows the policies for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

Shows the inbound policy for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy inbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Shows the outbound policy for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast policy outbound
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast prefix-limits inbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination

Shows default route origination configuration for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast default-route-origination
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise

Shows community advertise configuration information for the specified IPv4 BGP neighbor. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast community-advertise
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise

Shows conditional advertisement configuration information for the specified IPv4 BGP neighbor. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast conditional-advertise
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast capabilities

Shows all advertised and received capabilities for the specified IPv4 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast capabilities
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart

Shows BGP graceful restart configuration information for the specified IPv4 BGP neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv4-unicast graceful-restart
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast

Show configuration information for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod

Shows the attribute modification configuration settings for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast attribute-mod
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath

Shows the configuration settings for handling the AS path for prefixes to and from the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast aspath allow-my-asn
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast prefix-limits inbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination

Shows default route origination configuration for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast default-route-origination
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy

Shows policies for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound

Shows the inbound policy for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy inbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound

Shows the outbound policy for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast policy outbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise

Shows community advertise configuration information for the specified IPv6 BGP neighbor. The community advertise option determines if the neighbor can advertise a prefix to any iBGP or eBGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast community-advertise
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise

Shows conditional advertisement configuration information for the specified IPv6 BGP neighbor. The BGP conditional advertisement option lets you advertise certain routes only if other routes either do or do not exist.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast conditional-advertise
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast capabilities

Shows all advertised and received capabilities for the specified IPv6 BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast capabilities
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart

Shows BGP graceful restart configuration information for the specified IPv6 BGP neighbor. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family ipv6-unicast graceful-restart
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn

Shows layer 2 VPN EVPN configuration for the specified BGP neighbor.

- - -

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod

Shows the attribute modification configuration settings for the specified neighbor for layer 2 VPN EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn attribute-mod
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath

Shows the configuration options for handling the AS path for prefixes to and from the specified BGP neighbor for layer 2 VPN EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn

Shows if it is acceptable for a received AS path to contain the ASN of the local system for layer 2 VPN EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn aspath allow-my-asn
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Shows layer 2 VPN EVPN policies for the specified neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Shows the inbound layer 2 VPN EVPN policy for the specified BGP neighbor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy inbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Shows the outbound layer 2 VPN EVPN policy for the specified BGP neighbor.


### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn policy outbound
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn capabilities

Shows all advertised and received layer 2 VPN EVPN capabilities for the specified BGP neighbor.


### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn capabilities
```

- - -

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart

Shows graceful restart configuration for the specified BGP peer for layer 2 VPN EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    The VRF name.|
| `<neighbor-id>`  |  The BGP neighbor name or interface (for BGP unnumbered).  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp51 address-family l2vpn-evpn graceful-restart
```

- - -

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
cumulus@leaf04:mgmt:~$ nv show vrf default router bgp neighbor swp52 timers
```

- - -

## nv show router bgp

Shows global BGP configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp
```

- - -

## nv show router bgp graceful-restart

Shows global BGP graceful restart configuration. BGP graceful restart minimizes the negative effects that occur when BGP restarts.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp graceful-restart
```

- - -

## nv show router bgp convergence-wait

Shows global read-only mode configuration. Read-only mode reduces CPU and network usage when restarting the BGP process. 
### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp convergence-wait
```
