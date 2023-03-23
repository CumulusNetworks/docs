---
title: Interface
author: Cumulus Networks
weight: 580
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

- - -

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

## nv set interface \<interface-id\> ip

Configures IP addressing for an interface.

- - -

## nv set interface \<interface-id\> ip address \<ip-prefix-id\>

Configures an IP address with a route prefix for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip address 10.0.0.1/30
```

- - -

## nv set interface \<interface-id\> ip gateway \<ip-address-id\>

Configures the gateway IP address on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-address-id>` | The IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip gateway 10.10.10.1
```

- - -

## nv set interface \<interface-id\> ip ipv4

Configures IPv4 settings for an interface.

- - -

## nv set interface \<interface-id\> ip ipv4 enable

Turns IPv4 on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv4 enable off
```

- - -

## nv set interface \<interface-id\> ip ipv4 forward

Turns IPv4 forwarding on or off for the specified interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv4 forward on
```

- - -

## nv set interface \<interface-id\> ip ipv6

Configures IPv6 settings for an interface.

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set interface \<interface-id\> ip ipv6 enable

Turns IPv6 on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv6 enable off
```

- - -

## nv set interface \<interface-id\> ip ipv6 forward

Turns IPv6 forwarding on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv6 forward off
```

- - -
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

If you split a 100G port into four interfaces and auto-negotiation is on (the default setting), Cumulus Linux advertises the speed for each interface up to the maximum speed possible for a 100G port (100/4=25G). You can override this configuration and set specific speeds for the split ports if necessary.

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

- - -

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

- - -
