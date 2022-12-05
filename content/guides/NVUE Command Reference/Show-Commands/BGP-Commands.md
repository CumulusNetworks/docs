---
title: BGP Commands
author: Cumulus Networks
weight: 120
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router bgp

BGP VRF configuration.

### Usage

`nv show vrf <vrf-id> router bgp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address-family`    |Address family specific configuration |
| `path-selection`    |BGP path-selection configuration. |
| `route-reflection`  |BGP route-reflection configuration. |
| `peer-group`        |Peers |
| `route-export`      |Controls for exporting ipv4 and ipv6 routes from this VRF |
| `route-import`      |Controls for importing of ipv4 and ipv6 routes from this VRF |
| `timers`            |timer values for all peers in this VRF |
| `confederation`     |BGP Confederation options.|
| `neighbor`          |Peers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router bgp address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast`  |IPv4 unicast address family |
| `l2vpn-evpn`    |BGP VRF configuration. L2VPN EVPN address family |
| `ipv6-unicast`  |IPv6 unicast address family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `redistribute`     | Route redistribute| 
| `aggregate-route`  | IPv4 aggregate routes| 
| `network`          | IPv4 static networks.| 
| `route-import `    | Route import| 
| `multipaths`       | Multipaths| 
| `admin-distance`   | Admin distances.| 
| `route-export`     | Route export| 
| `loc-rib`          | IPv4 local RIB|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`    | Route redistribution of ipv4 static routes |
| `connected` | Route redistribution of ipv4 connected routes |
| `kernel`    | Route redistribution of ipv4 kernel routes|
| `ospf`      | Route redistribution of ipv4 ospf routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute static

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute static [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute connected

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute connected [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute kernel

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute kernel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute ospf

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute ospf [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast aggregate-route \<aggregate-route-id\>

An IPv4 aggregate route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast aggregate-route <aggregate-route-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<aggregate-route-id>` |  IPv4 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast network \<static-network-id\>

An IPv4 static network.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast network <static-network-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-network-id>` |   IPv4 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import

Route import

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `from-vrf` |   Controls for VRF to VRF route leaking for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf

Controls for VRF to VRF route leaking for this address-family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `list` |  List of VRFs the routes can be imported from|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-import from-vrf list \<leak-vrf-id\>

A VRF

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-import from-vrf list <leak-vrf-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<leak-vrf-id>` |  VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast multipaths

Multipaths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast multipaths [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast admin-distance

Admin distances.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast admin-distance [options]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export

Route export

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `to-evpn` |  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast route-export to-evpn

Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast route-export to-evpn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib

IPv4 local RIB

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route` |  IPv6 routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  VRF |
| `<route-id>` |  IPv4 address and route prefix in CIDR notation |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `path` | IP route paths |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-i\> path \<path-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |  IPv4 address and route prefix in CIDR notation |
| `<path-id>` |  Path Id |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop`          | Route nexthops |
| `peer`             | Nexthop peer information |
| `flags`            | Route flags |
| `bestpath`         | A bestpath information |
| `aspath`           | AS paths |
| `community`        | Set of community names for community-list |
| `large-community`  | Set of community names for large community list |
| `ext-community`    | extended communities |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> peer

Nexthop peer information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> peer [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> flags

Route flags

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> flags [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

A bestpath information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> bestpath [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> aspath

AS paths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> aspath [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> community

Set of community names for community-list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> community [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Set of community names for large community list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> large-community [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

extended communities

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast loc-rib route <route-id> path <path-id> ext-community [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family l2vpn-evpn

BGP VRF configuration. L2VPN EVPN address family

### Usage

`nv show vrf <vrf-id> router bgp address-family l2vpn-evpn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast

IPv6 unicast address family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `aggregate-route`  | IPv6 aggregate routes|
| `network`          | IPv6 static networks.|
| `route-import`     | Route import|
| `multipaths`       | Multipaths|
| `admin-distance`   | Admin distances.|
| `route-export`     | Route export|
| `redistribute`     | Route redistribute|
| `loc-rib`          | IPv6 local RIB|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast aggregate-route \<aggregate-route-id\>

An IPv6 aggregate route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast aggregate-route <aggregate-route-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<aggregate-route-id>` |  IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast network \<static-network-id\>

An IPv6 static network.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast network <static-network-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<static-network-id>`  | IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import

Route import

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `from-vrf` |  Controls for VRF to VRF route leaking for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf

Controls for VRF to VRF route leaking for this address-family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `list` |   List of VRFs the routes can be imported from |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-import from-vrf list

Set of VRFs

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-import from-vrf list [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast multipaths

Multipaths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast multipaths [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast admin-distance

Admin distances.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast admin-distance [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export

Route export

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `to-evpn` |  Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes) |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast route-export to-evpn

Controls for exporting routes from this VRF for this address-family into EVPN (as type-5 routes)

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast route-export to-evpn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`    | Route redistribution of ipv4 static routes |
| `connected` | Route redistribution of ipv4 connected routes |
| `kernel`    | Route redistribution of ipv4 kernel routes|
| `ospf6`     | Route redistribution of ipv6 ospf routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute static

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute static [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute connected

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute connected [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute kernel

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute kernel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast redistribute ospf6

Source route type.

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast redistribute ospf6 [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib

IPv6 local RIB

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route` |   IPv6 routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |  IPv6 address and route prefix in CIDR notation |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `path` |  IP route paths |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` | IPv6 address and route prefix in CIDR notation |
| `<path-id> ` | Path Id |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `nexthop`         | Route nexthops |
| `peer`            | Nexthop peer information |
| `flags`           | Route flags |
| `bestpath`        | A bestpath information |
| `aspath`          | AS paths |
| `community`       | Set of community names for community-list |
| `large-community` | Set of community names for large community list |
| `ext-community`   | extended communities |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> nexthop \<nexthop-id\>

An IPv4/IPv6 route

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> nexthop <nexthop-id> [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> peer

Nexthop peer information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> peer [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> flags

Route flags

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> flags [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> bestpath

A bestpath information

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> bestpath [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> aspath

AS paths

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> aspath [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> community

Set of community names for community-list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> community [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> large-community

Set of community names for large community list

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> large-community [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp address-family ipv6-unicast loc-rib route \<route-id\> path \<path-id\> ext-community

extended communities

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv6-unicast loc-rib route <route-id> path <path-id> ext-community [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show vrf \<vrf-id\> router bgp path-selection

BGP path-selection configuration.

### Usage

`nv show vrf <vrf-id> router bgp path-selection [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `aspath`     | BGP aspath path-selection config, applicable to this BGP instance |
| `med`        | BGP med path-selection config, applicable to this BGP instance |
| `multipath`  | BGP multipath path-selection config, applicable to this BGP instance |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection aspath

BGP aspath path-selection config, applicable to this BGP instance

### Usage

`nv show vrf <vrf-id> router bgp path-selection aspath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection med

BGP med path-selection config, applicable to this BGP instance

### Usage

`nv show vrf <vrf-id> router bgp path-selection med [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp path-selection multipath

BGP multipath path-selection config, applicable to this BGP instance

### Usage

`nv show vrf <vrf-id> router bgp path-selection multipath [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-reflection

BGP route-reflection configuration.

### Usage

`nv show vrf <vrf-id> router bgp route-reflection [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\>

BGP global configuration.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `bfd`               | Specifies whether to track BGP peering sessions using this configuration via BFD.
| `ttl-security`      | RFC 5082
| `capabilities`      | Capabilities
| `graceful-restart`  | Graceful restart
| `local-as`          | Local AS feature
| `timers`            | Peer peer-timers
| `address-family`    | Address family specific configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> ttl-security

RFC 5082

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> ttl-security [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> capabilities

Capabilities

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> local-as

Local AS feature

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> local-as [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> timers

Peer peer-timers

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |   Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast`  | Peer IPv4 unicast address family. Always on, unless disabled globaly. |
| `ipv6-unicast`  | Peer IPv6 unicast address family. |
| `l2vpn-evpn`    | Peer l2vpn EVPN address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `community-advertise`   | Community advertise for address family.|
| `attribute-mode`        | Attribute mod for address family. |
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `prefix-limits`         | Limits on prefix from the peer for this address-family |
| `default-route-origination` | Default route origination |
| `policy`                | Policies for ipv4 unicast |
| `conditional-advertise` | Conditional advertise for address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn` | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |   Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast default-route-origination [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Outbound unicast policy |
| `outbound` | Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv4-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `policy`                | Policies for ipv4 unicast|
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family|
| `prefix-limits`         | Limits on prefix from the peer for this address-family|
| `default-route-origination` | Default route origination|
| `community-advertise`   | Community advertise for address family.|
| `attribute-mode`        | Attribute mod for address family.|
| `conditional-advertise` | Conditional advertise for address family.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Outbound unicast policy |
| `outbound` | Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn` | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |   Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast default-route-origination [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family ipv6-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>` | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode` | Attribute mod for address family. |
| `aspath`         | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `policy`         | Policies for l2vpn evpn|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`   |  If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Inbound l2vpn-evpn policy |
| `outbound` | Outbound l2vpn-evpn policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp peer-group <peer-group-id> address-family l2vpn-evpn policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<peer-group-id>`  |   Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-export

Controls for exporting ipv4 and ipv6 routes from this VRF

### Usage

`nv show vrf <vrf-id> router bgp route-export [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `to-evpn` |  Controls for exporting routes from this VRF into EVPN |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-export to-evpn

Controls for exporting routes from this VRF into EVPN

### Usage

`nv show vrf <vrf-id> router bgp route-export to-evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-target`   | List the RTs to attach to host or prefix routes when exporting them into EVPN or "auto". If "auto", the RT will be derived. This the default. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-export to-evpn route-target \<rt-id\>

A route target identifier

### Usage

`nv show vrf <vrf-id> router bgp route-export to-evpn route-target <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rt-id>` |  Route targets or "auto" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-import

Controls for importing of ipv4 and ipv6 routes from this VRF

### Usage

`nv show vrf <vrf-id> router bgp route-import [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `from-evpn` |   Controls for importing EVPN type-2 and type-5 routes into this VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-import from-evpn

Controls for importing EVPN type-2 and type-5 routes into this VRF

### Usage

`nv show vrf <vrf-id> router bgp route-import from-evpn [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `route-target`  | List the RTs to attach to host or prefix routes when importing them into VRF or "auto". If "auto", the RT will be derived. This is the default.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp route-import from-evpn route-target \<rt-id\>

 A route target identifier

### Usage

`nv show vrf <vrf-id> router bgp route-import from-evpn route-target <rt-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rt-id>` | Route targets or "auto" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp timers

timer values for all peers in this VRF

### Usage

`nv show vrf <vrf-id> router bgp timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp confederation

BGP Confederation options.

### Usage

`nv show vrf <vrf-id> router bgp confederation [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `member-as` |  Confederation ASNs of the peers, maps to BGP  confederation peers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp confederation member-as

Set of autonomous numbers

### Usage

`nv show vrf <vrf-id> router bgp confederation member-as [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\>

BGP global configuration.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |   VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `bfd`                  | Specifies whether to track BGP peering sessions using this configuration via BFD.|
| `capabilities`         | Capabilities|
| `local-as`             | Local AS feature|
| `graceful-restart`     | BGP Graceful restart per neighbor configuration|
| `ttl-security`         | RFC 5082|
| `nexthop`              | Nexthop|
| `message-stats`        | Message statistics|
| `ebgp-policy`          | EBGP Policy RFC8212|
| `address-family`       | Address family specific configuration|
| `timers`               | Peer peer-timers|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> bfd

Specifies whether to track BGP peering sessions using this configuration via BFD.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> capabilities

Capabilities

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> local-as

Local AS feature

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> local-as [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |   Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> graceful-restart

BGP Graceful restart per neighbor configuration

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ttl-security

RFC 5082

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ttl-security [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> nexthop

Nexthop

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> nexthop [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`   | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> message-stats

Message statistics

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> message-stats [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> ebgp-policy

EBGP Policy RFC8212

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> ebgp-policy [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`   Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast` | Peer IPv4 unicast address family. Always on, unless disabled globaly. |
| `ipv6-unicast` | Peer IPv6 unicast address family. |
| `l2vpn-evpn`   | Peer l2vpn EVPN address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast

Peer IPv4 unicast address family.  Always on, unless disabled globaly.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode`        | Attribute mod for address family. |
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `policy`                | Policies for ipv4 unicast |
| `prefix-limits`         | Limits on prefix from the peer for this address-familydefault-route-origination Default route origination |
| `community-advertise`   | Community advertise for address family. |
| `conditional-advertise` | Conditional advertise for address family. |
| `capabilities`          | AF capabilities advertised and received |
| `graceful-restart`      | graceful restart information |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>` |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`  | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy

Policies for ipv4 unicast

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |  Outbound unicast policy |
| `outbound` |   Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  | Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |   Limits on inbound prefix from the peer for this address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast default-route-origination [options]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast capabilities

AF capabilities advertised and received

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast graceful-restart

graceful restart information

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv4-unicast graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast

Peer IPv6 unicast address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode`        | Attribute mod for address family. |
| `aspath`                | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `prefix-limits`         | Limits on prefix from the peer for this address-family |
| `default-route-origination` | Default route origination |
| `policy`                | Policies for ipv4 unicast |
| `community-advertise`   | Community advertise for address family. |
| `conditional-advertise` | Conditional advertise for address family. |
| `capabilities`          | AF capabilities advertised and received |
| `graceful-restart`      | graceful restart information |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`    | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits

Limits on prefix from the peer for this address-family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound` |  Limits on inbound prefix from the peer for this  address-family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast prefix-limits inbound

Limits on inbound prefix from the peer for this address-family


### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast prefix-limits inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast default-route-origination

Default route origination

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast default-route-origination [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy

Policies for ipv6 unicast

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`  | Outbound unicast policy |
| `outbound` | Outbound unicast policy |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy inbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast policy outbound

Outbound unicast policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast community-advertise

Community advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast community-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast conditional-advertise

Conditional advertise for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast conditional-advertise [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast capabilities

AF capabilities advertised and received

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast graceful-restart

graceful restart information

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family ipv6-unicast graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn

Peer l2vpn EVPN address family.

## Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn [options] [<attribute> ...]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `attribute-mode`   | Attribute mod for address family. |
| `aspath`           | Options for handling AS_PATH for prefixes from/to peer for the specified address family |
| `policy`           | Policies for l2vpn evpn |
| `capabilities`     | AF capabilities advertised and received |
| `graceful-restart` | graceful restart information |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn attribute-mod

Attribute mod for address family.

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn attribute-mod [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath

Options for handling AS_PATH for prefixes from/to peer for the specified address family

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-my-asn`    | If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn aspath allow-my-asn

If enabled, it is acceptable for a received AS_PATH to contain the ASN of the local system

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn aspath allow-my-asn [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy

Policies for l2vpn evpn

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `inbound`    | Inbound l2vpn-evpn policy |
| `outbound`   | Outbound l2vpn-e |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy inbound

Inbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy inbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn policy outbound

Outbound l2vpn-evpn policy

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn policy outbound [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn capabilities

AF capabilities advertised and received

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn capabilities [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn graceful-restart

graceful restart information

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> address-family l2vpn-evpn graceful-restart [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> timers

Peer peer-timers

### Usage

`nv show vrf <vrf-id> router bgp neighbor <neighbor-id> timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<neighbor-id>`  |  Peer ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router bgp

BGP global configuration.

### Usage

`nv show router bgp [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `graceful-restart` |  BGP Graceful restart global configuration. |
| `convergence-wait` |  BGP Graceful restart global configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router bgp graceful-restart

BGP Graceful restart global configuration.

### Usage

`nv show router bgp graceful-restart [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp graceful-restart
```

## nv show router bgp convergence-wait

BGP Graceful restart global configuration.

### Usage

`nv show router bgp convergence-wait [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router bgp convergence-wait
```

