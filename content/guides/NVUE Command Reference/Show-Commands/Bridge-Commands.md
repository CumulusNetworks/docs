---
title: Bridge Commands
author: Cumulus Networks
weight: 130
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> bridge

attributed related to a bridged interface

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

## nv show interface \<interface-id\> bridge domain \<domain-id\>

Bridge domain on this interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> bridge domain \<domain-id\> stp

attributed related to a stpd interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\>

A VLAN tag identifier

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |
| `<vid>`     | VLAN ID, or all |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge

Properties associated with an instance of a bridge.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain

Bridge domains

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\>

Bridge domain

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> stp

attributes related to global stp

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> stp state

The state of STP on the bridge

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> multicast

Configure multicast on the bridge

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` Domain | 

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> multicast snooping

IGMP/MLD snooping configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> multicast snooping querier

IGMP/MLD querier configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\>

A VLAN tag identifier

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid> |     VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

VNI

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>`          | Domain |
| `<vid>`                | VLAN ID |
| `<vni-id>`             | VxLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding

Handling of BUM traffic

### Command Syntax

| --------- | -------------- |
| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>`          | Domain |
| `<vid>`                | VLAN ID |
| `<vni-id>`             | VxLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication <hrep-id>

Set of IPv4 unicast addresses or "evpn".

### Command Syntax

| --------- | -------------- |
| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |
| `<vni-id>`   | VxLAN ID |
| `<hrep-id>`  | IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> ptp

VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast

Configure multicast on the vlan

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping

IGMP/MLD snooping configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier

IGMP/MLD querier configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> mac-table

L2 FDB

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> mdb

Set of mdb entries in the bridge domain

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show bridge domain \<domain-id\> router-port

Set of multicast router ports

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

