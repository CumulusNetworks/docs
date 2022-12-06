---
title: IGMP Commands
author: Cumulus Networks
weight: 155
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip igmp

Shows IGMP configuration information. IGMP prevents hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments.

### Usage

`nv show interface <interface-id> ip igmp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`  | The interface name. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static-group`  | Shows the IGMP static mutlicast mroutes. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 ip igmp
```

## nv show interface \<interface-id\> ip igmp static-group

Shows information about IGMP static multicast groups configured on the interface.

### Usage

`nv show interface <interface-id> ip igmp static-group [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 ip igmp static-group
```

## nv show interface \<interface-id\> ip igmp static-group \<static-group-id\>

Shows information about IGMP static multicast groups configured on the interface.

### Usage

`nv show interface <interface-id> ip igmp static-group <static-group-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<static-group-id>` | The IGMP static multicast mroute destination. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp1 ip igmp static-group 224.10.0.0
```

## nv show router igmp

Shows global IGMP configuration information.

### Usage

`nv show router igmp [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router igmp
```
