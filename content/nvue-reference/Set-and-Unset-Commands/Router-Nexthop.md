---
title: Router Nexthop
author: Cumulus Networks
weight: 710

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv set router nexthop</h>

Configures next hop groups.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router nexthop group \<nexthop-group-id\></h>

Configures a next hop group ID.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router nexthop group \<nexthop-group-id\> via \<via-id\></h>

Configures the next hop router for the next hop group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |
| `<via-id>`  | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set router nexthop group 10 via 10.0.1.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router nexthop group \<nexthop-group-id\> via \<via-id\> interface \<interface-name\></h>

Configures the next hop router and interface for the next hop group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |
| `<via-id>`  | The IP address of the nexthop router. |
| `<interface-name>`  | The interface name.  |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set router nexthop group 10 via 10.10.10.101 interface swp51
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router nexthop group \<nexthop-group-id\> via \<via-id\> vrf \<vrf-name\></h>

Configures the next hop router and VRF for the next hop group.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<nexthop-group-id>` | The next hop group ID. |
| `<via-id>`  | The IP address of the nexthop router. |
| `<vrf-name>`  | The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set router nexthop group 10 via 10.10.10.101 vrf default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router nexthop-tracking \<afi\> resolved-via-default</h>

Turns nexthop tracking resolved via default on or off.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-name>`  | The VRF name.  |
| `<afi>`  | The address family: IPv4 or IPv6.  |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set vrf default router nexthop-tracking ipv4 resolved-via-default on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router nexthop-tracking \<afi\></h>

Configures next hop tracking for the specified address family. Next hop tracking reduces the BGP convergence time by monitoring next hop address changes in the routing table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-name>`  | The VRF name.  |
| `<afi>`  | The address family: IPv4 or IPv6.  |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set router nexthop-tracking ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\></h>

Applies the specified nexthop tracking route map.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-name>`  | The VRF name.  |
| `<afi>`  | The address family: IPv4 or IPv6.  |
| `<nht-routemap-id>`  | The next hop tracking route map name.  |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set router nexthop-tracking ipv4 route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router nexthop-tracking \<afi\> route-map \<nht-routemap-id\> protocol</h>

Applies the specified nexthop tracking route map for the specified protocol. You can specify `bgp`, `ospf`, `ospf6`, or `static`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-name>`  | The VRF name.  |
| `<afi>`  | The address family: IPv4 or IPv6.  |
| `<nht-routemap-id>`  | The next hop tracking route map name.  |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set vrf default router nexthop-tracking ipv4 route-map ROUTEMAP1 bgp
```
