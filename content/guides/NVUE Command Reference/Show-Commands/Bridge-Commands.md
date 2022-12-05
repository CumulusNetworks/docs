---
title: Bridge Commands
author: Cumulus Networks
weight: 130
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> bridge

attributed related to a bridged interface

### Usage

`nv show interface <interface-id> bridge [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain`  |  Bridge domains on this interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge domain \<domain-id\>

Bridge domain on this interface

### Usage

`nv show interface <interface-id> bridge domain <domain-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `stp`  |attributed related to a stpd interface
| `vlan` | Set of allowed vlans for this bridge domain on this  interface. If "all", inherit all vlans from the bridge domain, if appropriate. This is the default. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge domain \<domain-id\> stp

attributed related to a stpd interface

### Usage

`nv show interface <interface-id> bridge domain <domain-id> stp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<domain-id>`   | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\>

A VLAN tag identifier

### Usage

`nv show interface <interface-id> bridge domain <domain-id> vlan <vid> [options]`

### Identifiers

| Identifier |  Description   |
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

## nv show bridge

Properties associated with an instance of a bridge.

### Usage

`nv show bridge [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `domain` |  Bridge domains |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain

Bridge domains

### Usage

`nv show bridge domain [options] [<domain-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\>

Bridge domain

### Usage

`nv show bridge domain <domain-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `stp`  |   attributes related to global stp |
| `multicast`    | Configure multicast on the bridge |
| `vlan`         | Set of vlans in the bridge domain. Only applicable when the domain type is "vlan-aware". |
| `mac-table`    | L2 FDB |
| `mdb`          | Set of mdb entries in the bridge domain |
| `router-port`  | Set of multicast router ports |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> stp

attributes related to global stp

### Usage

`nv show bridge domain <domain-id> stp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `state` | The state of STP on the bridge |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> stp state

The state of STP on the bridge

### Usage

`nv show bridge domain <domain-id> stp state [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> multicast

Configure multicast on the bridge

### Usage

`nv show bridge domain <domain-id> multicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` Domain | 

### Attributes

| Attribute |  Description   |
| --------- | -------------- |

  snooping              IGMP/MLD snooping configuration

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> multicast snooping

IGMP/MLD snooping configuration

### Usage

`nv show bridge domain <domain-id> multicast snooping [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` |  Domain |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `querier` |  IGMP/MLD querier configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> multicast snooping querier

IGMP/MLD querier configuration

### Usage

`nv show bridge domain <domain-id> multicast snooping querier [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\>

A VLAN tag identifier

### Usage

`nv show bridge domain <domain-id> vlan <vid> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid> |     VLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `vni`       | L2 VNI |
| `ptp`       | VLAN PTP configuration. Inherited by interfaces in this VLAN. |
| `multicast` | Configure multicast on the vlan |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

VNI

### Usage

`nv show bridge domain <domain-id> vlan <vid> vni <vni-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>`          | Domain |
| `<vid>`                | VLAN ID |
| `<vni-id>`             | VxLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flooding`  | Handling of BUM traffic |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding

Handling of BUM traffic

### Usage

`nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding [options] [<attribute> ...]`

### Identifiers

| --------- | -------------- |
| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>`          | Domain |
| `<vid>`                | VLAN ID |
| `<vni-id>`             | VxLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `head-end-replication` | BUM traffic is replicated and individual copies sent to remote destinations.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication <hrep-id>

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv show bridge domain <domain-id> vlan <vid> vni <vni-id> flooding head-end-replication <hrep-id> [options]`

### Identifiers

| --------- | -------------- |
| Identifier |  Description   |
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

## nv show bridge domain \<domain-id\> vlan \<vid\> ptp

VLAN PTP configuration.  Inherited by interfaces in this VLAN.

### Usage

`nv show bridge domain <domain-id> vlan <vid> ptp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast

Configure multicast on the vlan

### Usage

`nv show bridge domain <domain-id> vlan <vid> multicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `snooping`  | IGMP/MLD snooping configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping

IGMP/MLD snooping configuration

### Usage

`nv show bridge domain <domain-id> vlan <vid> multicast snooping [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `querier`  | IGMP/MLD querier configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier

IGMP/MLD querier configuration

### Usage

`nv show bridge domain <domain-id> vlan <vid> multicast snooping querier [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |
| `<vid>`      | VLAN ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> mac-table

L2 FDB

### Usage

`nv show bridge domain <domain-id> mac-table [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> mdb

Set of mdb entries in the bridge domain

### Usage

`nv show bridge domain <domain-id> mdb [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show bridge domain \<domain-id\> router-port

Set of multicast router ports

### Usage

`nv show bridge domain <domain-id> router-port [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<domain-id>` | Domain |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

