---
title: WJH Commands
author: Cumulus Networks
weight: 320
product: Cumulus Linux
type: nojsscroll
---
## nv show system wjh

Shows <span style="background-color:#F5F5DC">[WJH](## "What Just Happened")</span>configuration on the switch. WJH provides real time visibility into network problems.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system wjh
```

- - -

## nv show system wjh channel

Shows WJH channel configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system wjh channel
```

- - -

## nv show system wjh channel \<channel-id\>

Shows configuration for the specified WJH channel on the switch.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system wjh channel forwarding
```

- - -

## nv show system wjh channel \<channel-id\> trigger

Shows the configuration for packet drop categories in a WJH channel.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system wjh channel forwarding trigger
```

- - -

## nv show system wjh packet-buffer

Shows all dropped packets monitored by WJH and the reason for the drop.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system wjh packet-buffer
```
