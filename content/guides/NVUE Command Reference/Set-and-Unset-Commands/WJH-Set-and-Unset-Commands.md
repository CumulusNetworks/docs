---
title: WJH Set and Unset Commands
author: Cumulus Networks
weight: 800
product: Cumulus Linux
type: nojsscroll
---
## nv set system wjh

Configures What Just Happened (WJH) to provide real time visibility into network problems. You can diagnose network problems by looking at dropped packets.

### Usage

`nv [options] set system wjh [channel ...]`

`nv [options] set system wjh [enable ...]`

### Version History

Introduced in Cumulus Linux 5.3.0

- - -

## nv set system wjh channel \<channel-id\>

Configures a WJH channel where you want to monitor packet drops.

### Usage

`nv [options] set system wjh channel <channel-id>`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `<channel-id>` | The channel name.  |

### Attributes

| Attribute |  Description   |
| ---------  | -------------- |
| `trigger` | Configures the type of packet drops you want to monitor. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system wjh channel forwarding
```

- - -

## nv set system wjh channel \<channel-id\> trigger

Configures the type of packet drops you want to monitor. You can monitor layer 1, layer 2, or layer 3 packet drops.

### Usage

`nv [options] set system wjh channel <channel-id> trigger [l1 ...]`

`nv [options] set system wjh channel <channel-id> trigger [l2 ...]`

`nv [options] set system wjh channel <channel-id> trigger [l3 ...]`

### Identifiers

| Identifier |  Description   |
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

### Usage

`nv [options] set system wjh enable [<arg> ...]`

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system wjh enable off
```
