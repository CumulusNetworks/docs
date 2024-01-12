---
title: WJH
author: Cumulus Networks
weight: 820

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system wjh</h>

Provides commands to configure <span class="a-tooltip">[WJH](## "What Just Happened")</span> to provide real time visibility into network problems. You can diagnose network problems by looking at dropped packets.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\></h>

Configures a WJH channel where you want to monitor packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name.  |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh channel \<channel-id\> trigger</h>

Configures the type of packet drops you want to monitor. You can monitor layer 1 (`l1`), layer 2 (`l2`), layer 3 (`l3`), or tunnel (`tunnel1`) related packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh channel forwarding trigger l3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system wjh enable</h>

Turns the WJH service on or off. The default value is `on`.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system wjh enable off
```
