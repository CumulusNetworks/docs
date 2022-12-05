---
title: IGMP Commands
author: Cumulus Networks
weight: 155
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip igmp

Configuration for IGMP

### Usage

`nv show interface <interface-id> ip igmp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static-group`    | IGMP static mutlicast mroutes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip igmp static-group \<static-group-id\>

IGMP static multicast mroute

### Usage

`nv show interface <interface-id> ip igmp static-group <static-group-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<static-group-id>` |  IGMP static multicast mroute destination |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router igmp

IGMP global configuration.

### Usage

`nv show router igmp [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
