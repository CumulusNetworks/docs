---
title: PIM Commands
author: Cumulus Networks
weight: 130
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router pim

PIM interface configuration.

### Usage

`nv show interface <interface-id> router pim [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`timers`                | Timers |
|`bfd`                   | BFD configuration |
|`address-family`        | Address family specific configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim timers

Timers

### Usage

`nv show interface <interface-id> router pim timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim bfd

BFD configuration

### Usage

`nv show interface <interface-id> router pim bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim address-family

Address family specific configuration

### Usage

`nv show interface <interface-id> router pim address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast` | IPv4 unicast address family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show interface <interface-id> router pim address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `allow-rp` |   Allow RP feature, which allows RP address to be accepts for the received |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> router pim address-family ipv4-unicast allow-rp

Allow RP feature, which allows RP address to be accepts for the received

### Usage

`nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router pim

PIM global configuration.

### Usage

`nv show router pim [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers` |    Timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show router pim timers

Timers

### Usage

`nv show router pim timers [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim

PIM VRF configuration.

### Usage

`nv show vrf <vrf-id> router pim [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers`                | Timers |
| `ecmp`                  | Choose all available ECMP paths for a particular RPF. If 'off', the first nexthop found will be used. This is the default.|
| `msdp-mesh-group`       | To connect multiple PIM-SM multicast domains using RPs. |
| `address-family`        | Address family specific configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim timers

Timers

### Usage

`nv show vrf <vrf-id> router pim timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim ecmp

Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Usage

`nv show vrf <vrf-id> router pim ecmp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\>

MSDP mesh-group

### Usage

`nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<msdp-mesh-group-id>` |  MSDP mesh group name |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `member-address` | Set of member-address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\>

A MSDP mesh member

### Usage

`nv show vrf <vrf-id> router pim msdp-mesh-group <msdp-mesh-group-id> member-address <mesh-member-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<msdp-mesh-group-id>`  | MSDP mesh group name |
| `<mesh-member-id>`      | MSDP mesh-group member IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family

Address family specific configuration

### Usage

`nv show vrf <vrf-id> router pim address-family [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4-unicast`   |  IPv4 unicast address family |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`spt-switchover`   | Build shortest path tree towards source. |
| `rp`  |  RP address and associated group range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover

Build shortest path tree towards source.

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast spt-switchover [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\>

RP

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rp-id>` |  RP IP address |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `group-range`   |  Set of group range assocaited to RP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> group-range \<group-range-id\>

A group range

### Usage

`nv show vrf <vrf-id> router pim address-family ipv4-unicast rp <rp-id> group-range <group-range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rp-id>`  | RP IP address |
| `<group-range-id>`  |  Group range associated to RP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
