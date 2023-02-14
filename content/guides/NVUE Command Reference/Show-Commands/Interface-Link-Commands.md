---
title: Interface Link Commands
author: Cumulus Networks
weight: 157
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> link

Shows configuration and statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 link
```

- - -

## nv show interface \<interface-id\> link state

Shows the state of the specified interface; if the link is up or down.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 link state
```

- - -

## nv show interface \<interface-id\> link stats

Shows statistics for the specified interface, such as packet size, packet drops, and packet errors.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 link stats
```

- - -

## nv show interface \<interface-id\> link traffic-engineering

Shows traffic engineering statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 link traffic-engineering
```

- - -

## nv show interface \<interface-id\> link flag

Shows link flags for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 link flag
```
