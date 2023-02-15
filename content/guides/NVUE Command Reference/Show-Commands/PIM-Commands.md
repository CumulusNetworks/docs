---
title: PIM Commands
author: Cumulus Networks
weight: 220
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> router pim

Shows <span style="background-color:#F5F5DC">[PIM](## "Protocol Independent Multicast")</span> configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface vlan10 router pim
```

- - -

## nv show interface \<interface-id\> router pim timers

Shows PIM timer settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface vlan10 router pim timers
```

- - -

## nv show interface \<interface-id\> router pim bfd

Shows PIM BFD configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface vlan10 router pim bfd
```

- - -

## nv show interface \<interface-id\> router pim address-family

Shows PIM configuration settings for all address families for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface vlan10 router pim address-family
```

- - -

## nv show interface \<interface-id\> router pim address-family ipv4-unicast

Shows IPv4 PIM configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface vlan10 router pim address-family ipv4-unicast
```

- - -

## nv show interface \<interface-id\> router pim address-family ipv4-unicast allow-rp

Shows PIM allow RP configuration settings for IPv4 for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface vlan10 router pim address-family ipv4-unicast allow-rp
```

- - -

## nv show router pim

Shows global PIM configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pim
```

- - -

## nv show router pim timers

Shows global PIM timer settings on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router pim timers
```

- - -

## nv show vrf \<vrf-id\> router pim

Shows PIM configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim
```

- - -

## nv show vrf \<vrf-id\> router pim timers

Shows PIM timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim timers
```

- - -

## nv show vrf \<vrf-id\> router pim ecmp

Shows PIM ECMP settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim ecmp
```

- - -

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\>

Shows information about the specified MSDP mesh group for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<msdp-mesh-group-id>` |  The MSDP mesh group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim msdp-mesh-group pod1
```

- - -

## nv show vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\>

Shows information about the specified MSDP mesh group member for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<msdp-mesh-group-id>` |  The MSDP mesh group name. |
| `<mesh-member-id>`      | The IP address of the MSDP mesh group member.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim msdp-mesh-group pod1 member-address 10.1.10.102
```

- - -

## nv show vrf \<vrf-id\> router pim address-family

Shows address family specific PIM configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim address-family
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast

Shows IPv4 PIM configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim address-family ipv4-unicast
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover

Shows IPv4 PIM <span style="background-color:#F5F5DC">[SPT](## "SPT Shortest Path Tree")</span> switchover configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim address-family ipv4-unicast spt-switchover
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\>

Shows IPv4 PIM configuration for the specified <span style="background-color:#F5F5DC">[RP](## "Rendezvous Point")</span> for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rp-id>` |  RP IP address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim address-family ipv4-unicast rp 10.10.10.101
```

- - -

## nv show vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> group-range \<group-range-id\>

Shows IPv4 PIM configuration for the specified <span style="background-color:#F5F5DC">[RP](## "Rendezvous Point")</span> group range for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|
| `<rp-id>`  | RP IP address |
| `<group-range-id>`  |  The group range associated with the RP. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router pim address-family ipv4-unicast rp 10.100.100.100 group-range 224.0.0.0/4
```
