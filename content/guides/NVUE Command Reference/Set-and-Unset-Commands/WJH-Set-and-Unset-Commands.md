---
title: WJH Set and Unset Commands
author: Cumulus Networks
weight: 800
product: Cumulus Linux
type: nojsscroll
---
## nv set system wjh

Provides commands to configure What Just Happened (WJH) to provide real time visibility into network problems. You can diagnose network problems by looking at dropped packets.

## nv set system wjh channel \<channel-id\>

Configures a WJH channel where you want to monitor packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name.  |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system wjh channel forwarding
```

- - -

## nv set system wjh channel \<channel-id\> trigger

Configures the type of packet drops you want to monitor. You can monitor layer 1 (`l1`), layer 2 (`l2`), layer 3 (`l3`), or tunnel (`tunnel1) related packet drops.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system wjh channel forwarding trigger l3
```

- - -

## nv set system wjh enable

Turns the WJH service on or off.

The default value is `on`.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system wjh enable off
```
