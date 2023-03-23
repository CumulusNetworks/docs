---
title: Interface
author: Cumulus Networks
weight: 505
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> base-interface

Configures the specified interface to be the base interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp5 base-interface
```

- - -

## nv set interface \<interface-id\> description

Configures a description for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 description hypervisor_port_1
```

## nv set interface \<interface-id\> bond down-delay

Configures the down delay on the bonded interface. You can set a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond down-delay 100
```

- - -

## nv set interface \<interface-id\> bond lacp-bypass

Turns LACP bypass on the specified bond to 802.3ad mode so that it becomes active and forwards traffic even when there is no LACP partner. You can specify on or off. The default setting is off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond lacp-bypass on
```

- - -

## nv set interface \<interface-id\> bond lacp-rate

Configures the rate at which the link partner transmits LACP control packets. You can set a value of `fast` or `slow`. The default setting is `fast`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond lacp-rate slow
```

- - -

## nv set interface \<interface-id\> bond member \<member-id\>

Configures the bonded interface by specifying the bond members.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<member-id>` |  The bond member names. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface bond1 bond member swp1-4
```

- - -

## nv set interface \<interface-id\> bond mode

Configures link aggregation mode on the bond to 802.3ad or balance-xor mode. You can specify `lacp` (802.3ad) or `static` (balance-xor mode). The default mode is 802.3ad.

Set balance-xor mode only if you cannot use LACP; LACP can detect mismatched link attributes between bond members and can even detect misconnections.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 bond mode static
```

- - -

## nv set interface \<interface-id\> bond up-delay

Configures the up delay on the bonded interface. You can set a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp5 bond up-delay 100
```

- - -

## nv set interface \<interface-id\> storm-control

Configures storm control on the specified interface. Storm control provides protection against excessive inbound BUM (broadcast, unknown unicast, multicast) traffic on layer 2 switch port interfaces, which can cause poor network performance.

- - -

## nv set interface \<interface-id\> storm-control broadcast

Configures the number of broadcast packets per second (pps) that signifies a broadcast storm. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 storm-control broadcast 400
```

- - -

## nv set interface \<interface-id\> storm-control multicast

Configures the number of multicast packets per second (pps) that signifies a multicast storm. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 storm-control multicast 3000
```

- - -

## nv set interface \<interface-id\> storm-control unknown-unicast

- - -

Configures the number of unknown unicast packets per second (pps) that signifies an unknown unicast storm. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 storm-control unknown-unicast 2000
```

- - -

## nv set interface \<interface-id\> tunnel

Configures GRE tunneling.

- - -

## nv set interface \<interface-id\> tunnel source-ip

Configures the source IP address for the GRE tunnel on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel source-ip 10.10.10.1
```

- - -

## nv set interface \<interface-id\> tunnel dest-ip

Configures the destination IP address for the GRE tunnel on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel dest-ip 10.10.10.3
```

- - -

## nv set interface \<interface-id\> tunnel ttl

Configures the TTL for the GRE tunnel on the specified interface. You can set a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel ttl 50
```

- - -

## nv set interface \<interface-id\> tunnel mode gre

Enables GRE mode for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel mode gre 
```

- - -

## nv set interface \<interface-id\> tunnel interface \<interface-name\>

Configures the GRE tunnel interface name.

## Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface tunnelR2 tunnel interface MYGRETUNNEL
```

- - -

## nv set interface \<interface-id\> type

Configures the interface type. The typ can be `swp`, `eth`, `bond`, `loopback`, `svi`, `sub`, `peerlink`, `tunnel`, `bridge` or `vrf`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 type swp
```

- - -

## nv set interface \<interface-id\> vlan

Configures the VLAN on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 vlan 10
```

- - -
