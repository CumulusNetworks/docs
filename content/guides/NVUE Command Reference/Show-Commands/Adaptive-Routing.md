---
title: Adaptive Routing
author: Cumulus Networks
weight: 120
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router adaptive-routing

Shows if adaptive routing is enabled on the interface and the link utilization threshold (as a percentage).

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show router adaptive-routing

Shows global adaptive routing configuration. This command shows if adaptive routing is enabled.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router adaptive-routing
```
