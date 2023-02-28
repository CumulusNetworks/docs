---
title: Adaptive Routing Commands
author: Cumulus Networks
weight: 115
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router adaptive-routing

Shows adaptive routing interface configuration. This command shows if adaptive routing is on or off for the interface and the link utilization threshold (as a percentage).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 router adaptive-routing
```

- - -

## nv show router adaptive-routing

Shows global adaptive routing configuration. This command shows if adaptive routing is on or off.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router adaptive-routing
```

- - -
