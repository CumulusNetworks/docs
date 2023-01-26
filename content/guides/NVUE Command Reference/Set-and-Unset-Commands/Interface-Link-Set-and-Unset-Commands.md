---
title: Interface Link Set and Unset Commands
author: Cumulus Networks
weight: 600
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if there is a difference between the `nv set` and `nv unset` command.
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

## nv set interface \<interface-id\> link dot1x

Provides commands to configure the IEEE 802.1X protocol for the specified interface.

- - -

## nv set interface \<interface-id\> link dot1x mab

Configures MAC authentication bypass (MAB), which enables bridge ports to allow devices to bypass authentication based on their MAC address. This is useful for devices that do not support PAE, such as printers or phones. You can specify `on` or `off`.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link dot1x mab on
```

- - -

## nv set interface \<interface-id\> link dot1x parking-vlan

Configures a Parking VLAN. If a non-authorized supplicant tries to communicate with the switch, you can route traffic from that device to a different VLAN and associate that VLAN with one of the switch ports to which the supplicant is attached. You can specify `on` or `off`.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link dot1x parking-vlan on
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

## nv set interface \<interface-id\> link breakout

Configures breakout ports for the interface. You can specify 1x, 2x20G, 2x40G, 2x50G, 2x100G, 2x200G, 4x10G, 4x25G, 4x50G, 4x100G, 8x50G, disabled, or loopback.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link breakout 4x25G
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

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 link fast-linkup on
```
