---
title: Router General
author: Cumulus Networks
weight: 705

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router allow-reserved-range \<allow-reserved-range-id\></h>

Configures the switch to permit a reserved IPv4 range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<allow-reserved-range-id>` |  The reserved IPv4 range. The only valid value is `class-e`. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set router allow-reserved-range class-e
```


<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router resource-limit max-file-descriptors</h>

Configures the maximum number of file descriptors, which includes open sockets and files, that each routing daemon can use. You can specify a value between 1024 and 65536. When you do not set this option, routing daemons use the system default of 2048.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set router resource-limit max-file-descriptors 8192
```

