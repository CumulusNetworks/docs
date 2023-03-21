---
title: Interface Set and Unset Commands
author: Cumulus Networks
weight: 505
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

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
