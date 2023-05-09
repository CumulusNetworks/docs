---
title: Adaptive Routing
author: Cumulus Networks
weight: 120
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show interface \<interface-id\> router adaptive-routing</h>

Shows if adaptive routing is enabled on the interface and the link utilization threshold (as a percentage).

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show interface swp1 router adaptive-routing
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router adaptive-routing</h>

Shows global adaptive routing configuration. This command shows if adaptive routing is enabled.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv show router adaptive-routing
```
