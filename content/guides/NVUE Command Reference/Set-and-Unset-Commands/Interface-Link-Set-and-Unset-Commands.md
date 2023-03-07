---
title: Interface Link Set and Unset Commands
author: Cumulus Networks
weight: 570
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> link

Provides commands to configure physical interface settings, such as the link state, auto-negotiation, breakouts, FEC, MTU, speed, 802.1X, and MAC authentication bypass (MAB).

- - -

## nv set interface \<interface-id\> link state

Brings an interface up or down administratively (admin up or admin down). You can specify `up` or `down`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link state up
```

- - -

## nv set interface \<interface-id\> link breakout \<mode-id\>

Configures a port break out (split) with the following options:
- 1x does not split the port. This is the default port setting.
- 2x splits the port into two interfaces.
- 4x splits the port into four interfaces.
- 8x splits the port into eight interfaces.

If you split a 100G port into four interfaces and auto-negotiation is on (the default setting), Cumulus Linux advertises the speed for each interface up to the maximum speed possible for a 100G port (100/4=25G). You can overide this configuration and set specific speeds for the split ports if necessary.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<mode-id>` | The breakout mode: 1x, 2x, 4x, 8x. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link breakout 4x
```

## nv set interface \<interface-id\> link breakout \<mode-id\> lanes-per-port \<lanes-per-port\>

Configures the number of lanes per split port. By default, to calculate the split port width, Cumulus Linux uses the formula: split port width = full port width / breakout. For example, a port split into two interfaces (2x breakout) => 8 lanes width / 2x breakout = 4 lanes per split port. If you need to use a different port width than the default, you can set the number of lanes per port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |
|`<mode-id>` | The breakout mode: 1x, 2x, 4x, 8x. |
|`<lanes-per-port>` | The breakout mode: 1x, 2x, 4x, 8x. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link breakout 2x lanes-per-port 2
```
- - -

## nv set interface \<interface-id\> link auto-negotiate

Configures auto-negotiation for the interface.

The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link auto-negotiate off
```

- - -

## nv set interface \<interface-id\> link duplex

Configures duplex mode for the interface; full or half.

The default setting is `full`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link duplex half
```

- - -

## nv set interface \<interface-id\> link lanes

Configures the number of lanes for a port to override the default behavior for supported speeds and platforms.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link lanes 1
```

- - -

## nv set interface \<interface-id\> link speed

Configures the speed for the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link speed 10G
```

- - -

## nv set interface \<interface-id\> link fec

Configures Forward Error Correction (FEC) for the interface. FEC enables the switch to detect and correct bit errors introduced over the cable between two interfaces.

The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link fec baser
```

- - -

## nv set interface \<interface-id\> link mtu

Configures the maximum transmission unit (MTU) for the interface. You can set a value between 552 and 9216.

The default setting is 9216

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link mtu 1500
```

- - -

## nv set interface \<interface-id\> link fast-linkup

Configures fast linkup on interfaces on NVIDIA Spectrum1 switches. Fast linkup enables you to bring up ports with cards that require links to come up fast, such as certain 100G optical network interface cards. You can specify `on` or `off`.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link fast-linkup on
```
