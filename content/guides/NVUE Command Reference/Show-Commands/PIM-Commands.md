---
title: PIM Commands
author: Cumulus Networks
weight: 220
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router pim

PIM interface configuration.

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

## nv show interface \<interface-id\> router pim timers

Timers

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

## nv show interface \<interface-id\> router pim bfd

BFD configuration

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

## nv show interface \<interface-id\> router pim address-family

Address family specific configuration

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

## nv show interface \<interface-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

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

## nv show interface \<interface-id\> router pim address-family ipv4-unicast allow-rp

Allow RP feature, which allows RP address to be accepts for the received

`nv show interface <interface-id> router pim address-family ipv4-unicast allow-rp [options]`

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

## nv show router pim

PIM global configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show router pim timers

Timers

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim

PIM VRF configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim timers

Timers

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim ecmp

Choose all available ECMP paths for a particular RPF.  If 'off', the first nexthop found will be used.  This is the default.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\>

MSDP mesh-group

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<msdp-mesh-group-id>` |  MSDP mesh group name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\>

A MSDP mesh member

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show vrf \<vrf-id\> router pim address-family

Address family specific configuration

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast

IPv4 unicast address family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover

Build shortest path tree towards source.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\>

RP

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<rp-id>` |  RP IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> group-range \<group-range-id\>

A group range

### Command Syntax

| Syntax |  Description   |
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
