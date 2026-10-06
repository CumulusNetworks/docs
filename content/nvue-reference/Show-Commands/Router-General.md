---
title: Router General
author: Cumulus Networks
weight: 335

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router allow-reserved-range</h>

Shows the reserved IPv4 ranges that the switch can use.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv show router allow-reserved-range
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router allow-reserved-range \<allow-reserved-range-id\></h>

Shows a specific reserved IPv4 range that the switch can use.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<allow-reserved-range-id>` |  The reserved IPv4 range. The only valid value is `class-e`. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv show router allow-reserved-range class-e
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router resource-limit</h>

Shows the router resource limits.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv show router resource-limit
```

