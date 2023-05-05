---
title: Router Nexthop
author: Cumulus Networks
weight: 340
product: Cumulus Linux
type: nojsscroll
---
## nv show router nexthop

Shows information about the next hops in the RIB, such as the IP address, VRF, interface, type, and so on.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop group

Shows the next hop groups in the RIB. Nexthop groups are a way to encapsulate ECMP information together.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop groups
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop group \<nexthop-group-id\>

Shows information about the specified next hop group in the RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop group \<nexthop-group-id\> via

Shows information about the next hop addresses for the specified next hop group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 1 via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop group \<nexthop-group-id\> via \<via-id\>

Shows details of a particular next hop group specified by the next hop address.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |
| `<via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop 10 via fe80::a00:27ff:fea6:b9fe
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib

Shows information about the next hops in RIB, such as the IP address, VRF, interface, type, and so on.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\>

Shows information about the specified next hop in the RIB.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router next hop rib 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\> depends

Shows information about the next hops on which a specific next hop relies on.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 depends
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\> dependents

Shows information about the next hop dependents on which a specific next hop relies on.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 dependents
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\> resolved-via

Shows details the next-hop address for a particular next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router next hop rib 10 resolved-via
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\> resolved-via \<resolved-via-id\>

Shows details of a particular next hop specified by the next hop IP address.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The next hop IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 10 resolved-via fe80::a00:27ff:fea6:b9fe
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\> resolved-via-backup

Shows information about the backup next hops for the specified next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router next hop 10 resolved-via-backup
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router nexthop rib \<nhg-id\> resolved-via-backup \<resolved-via-id\>

Shows information about a specific backup next hop.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nhg-id>` | The next hop group ID. |
| `<resolved-via-id>` | The IP address. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router nexthop rib 20 resolved-via-backup 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router nexthop-tracking

Shows the IPv4 and IPv6 next hop tracking information for the specified VRF. Next hop tracking is an optimization feature that reduces the processing time involved in the BGP bestpath algorithm by monitoring changes to the routing table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router nexthop-tracking
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router nexthop-tracking \<afi\>

Shows the IPv4 or IPv6 next hop tracking information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family: `ipv4` or `ipv6`. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router nexthop-tracking ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map

Shows the IPv4 or IPv6 next hop tracking information for all route maps for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family: `ipv4` or `ipv6`. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\>

Shows the IPv4 or IPv6 next hop tracking information for a specific route map for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family: `ipv4` or `ipv6`. |
| `<nht-routemap-id>` | The next hop tracking route map name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol

Shows the IPv4 or IPv6 next hop tracking information for all protocols in the route map: BGP, OSPF, OSPF6, or static for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family: `ipv4` or `ipv6`. |
| `<nht-routemap-id>` | The next hop tracking route map name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol \<nht-protocol-id\>

Shows the IPv4 or IPv6 next hop tracking information for a specific route map protocol for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<afi>` | The address family: `ipv4` or `ipv6`. |
| `<nht-routemap-id>` | The next hop tracking route map name. |
| `<nht-protocol-id>` | The protocol: `bgp`, `ospf`, `ospf6`, or `static`. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 bgp
```
