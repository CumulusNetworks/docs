---
title: LLDP Commands
author: Cumulus Networks
weight: 160
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> lldp

LLDP on for an interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\>

LLDP on an interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge

An LLDP bridge

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>` |  System generated identifier for the neighbor on the interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> lldp neighbor \<neighbor-id\> bridge vlan \<vid\>

A VLAN tag identifier

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show service lldp

Global LLDP

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
