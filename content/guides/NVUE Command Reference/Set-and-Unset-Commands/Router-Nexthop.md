---
title: Router Nexthop
author: Cumulus Networks
weight: 695
product: Cumulus Linux
type: nojsscroll
---
## nv set router nexthop

Configures next hop groups.

- - -

## nv set router nexthop group \<nexthop-group-id\>

Configures a next hop group ID.

- - -

## nv set router nexthop group \<nexthop-group-id\> via \<via-id\>

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
cumulus@leaf01:mgmt:~$ nv set router nexthop group 10 via 10.0.1.0
```

- - -

## nv set router nexthop group \<nexthop-group-id\> via \<via-id\> interface \<interface-name\>

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
cumulus@leaf01:mgmt:~$ nv set router nexthop group 10 via 10.10.10.101 interface swp51
```

- - -

## nv set router nexthop group \<nexthop-group-id\> via \<via-id\> vrf \<vrf-name\>

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
cumulus@leaf01:mgmt:~$ nv set router nexthop group 10 via 10.10.10.101 vrf default
```

- - -
