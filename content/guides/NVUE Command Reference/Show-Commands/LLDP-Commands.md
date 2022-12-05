---
title: LLDP Commands
author: Cumulus Networks
weight: 160
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> lldp

LLDP on for an interface

### Usage

`nv show interface <interface-id> lldp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `neighbor` | LLDP neighbors |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\>

LLDP on an interface

### Usage

`nv show interface <interface-id> lldp neighbor <neighbor-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `bridge`  |  Bridge properties, such as VLANs, of the neighbor|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge

An LLDP bridge

### Usage

`nv show interface <interface-id> lldp neighbor <neighbor-id> bridge [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vlan` | Set of vlans understood by this neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan \<vid\>

A VLAN tag identifier

### Usage

`nv show interface <interface-id> lldp neighbor <neighbor-id> bridge vlan <vid> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface |
| `<vid>` | VLAN ID, or all |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service lldp

Global LLDP

### Usage

`nv show service lldp [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
