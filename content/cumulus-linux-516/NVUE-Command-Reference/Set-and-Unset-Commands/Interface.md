---
title: Interface
author: Cumulus Networks
weight: 580

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> base-interface</h>

Configures the specified interface to be the base interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp5 base-interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond down-delay</h>

Configures the down delay on the bonded interface. You can set a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface bond1 bond down-delay 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond lacp-bypass</h>

Enables and disables LACP bypass on the specified bond to 802.3ad mode so that it becomes active and forwards traffic even when there is no LACP partner. You can specify `enabled` or `disabled`. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface bond1 bond lacp-bypass enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond lacp-rate</h>

Configures the rate at which the link partner transmits LACP control packets. You can set a value of `fast` or `slow`. The default setting is `fast`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface bond1 bond lacp-rate slow
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond member \<member-id\></h>

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
cumulus@switch:~$ nv set interface bond1 bond member swp1-4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond mode</h>

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
cumulus@switch:~$ nv set interface swp1 bond mode static
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bond up-delay</h>

Configures the up delay on the bonded interface. You can set a value between 0 and 65535.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp5 bond up-delay 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> description</h>

Configures a description for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 description hypervisor_port_1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 address \<ip-prefix-id\></h>

Configures an IP address with a route prefix for the specified interface. For IPv6, run the `nv set interface <interface-id> ipv6 address <ip-prefix-id>` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier the command is `nv set interface <interface-id> ip address`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | The IP address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ipv4 address 10.0.0.1/30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 gateway \<ip-address\></h>

Configures the gateway IP address on the specified interface. For IPv6, run the `nv set interface <interface-id> ipv6 gateway <ip-address>` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv set interface <interface-id> ip gateway <ip-address>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-address>` | The IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ipv4 gateway 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 forward</h>

Enables and disables IPv4 forwarding for the specified interface. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier:
- the command is `nv set interface <interface-id> ip ipv4 forward`.
- You specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ipv4 forward enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv6 state</h>

Enables and disables IPv6. The default setting is `enabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier:
- The command is `nv set interface <interface-id> ip ipv6 state`.
- You specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ipv6 state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv6 forward</h>

Enables and disables IPv6 forwarding. The default setting is `enabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier:
- The command is `nv set interface <interface-id> ip ipv6 forward`.
- You specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ipv6 forward disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link auto-negotiate</h>

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
cumulus@switch:~$ nv set interface swp1 link auto-negotiate off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link breakout \<mode-id\></h>

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
cumulus@switch:~$ nv set interface swp1 link breakout 4x
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link breakout \<mode-id\> lanes-per-port \<lanes-per-port\></h>

Configures the number of lanes per split port. By default, to calculate the split port width, Cumulus Linux uses the formula: split port width = full port width / breakout. For example, a port split into two interfaces (2x breakout) = 8 lanes width / 2x breakout = 4 lanes per split port. If you need to use a different port width than the default, you can set the number of lanes per port.

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
cumulus@switch:~$ nv set interface swp1 link breakout 2x lanes-per-port 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link duplex</h>

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
cumulus@switch:~$ nv set interface swp1 link duplex half
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link fast-linkup</h>

Configures fast linkup on interfaces on NVIDIA Spectrum 1 switches. Fast linkup enables you to bring up ports with cards that require links to come up fast, such as certain 100G optical network interface cards. You can specify `enabled` or `disabled`. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link fast-linkup enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link fec</h>

Configures Forward Error Correction (FEC) for the interface. FEC enables the switch to detect and correct bit errors introduced over the cable between two interfaces. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link fec baser
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link flap-protection state</h>

Enables and disables link flap protection on the specified interface. Cumulus Linux enables link flap detection by default. Link flap detection triggers when there are five link flaps within ten seconds, at which point the interface goes into a protodown state and shows `linkflap` as the reason. The `switchd` service also shows a log message.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link flap-protection state disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link lanes</h>

Configures the number of lanes for a port to override the default behavior for supported speeds and platforms.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link lanes 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link mac-address \<mac-address\></h>

Configures a MAC address for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |
|`<mac-address>` |  The MAC address you want to configure for the interface. |

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link mac-address 00:02:00:00:00:05
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link mtu</h>

Configures the maximum transmission unit (MTU) for the interface. You can set a value between 552 and 9216. The default setting is 9216.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link mtu 1500
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link speed</h>

Configures the speed for the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link speed 10G
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link state</h>

Brings an interface up or down administratively (admin up or admin down). You can specify `up` or `down`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link state up
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> link tx-squelch</h>

{{%notice note%}}
Tx squelch control is a Beta feature.
{{%/notice%}}

Configures Tx squelch control, which is a PHY‑level feature that controls if the local port continues transmitting when the remote side is logically down (for example, when the remote side is in a fault state or needs to restart auto-negotiation).

{{%notice note%}}
- Switches with Spectrum-4 and later support Tx squelch control.
- Cumulus Linux supports Tx squelch control on physical ports only (including breakout ports).
- Enabling or disabling Tx squelch control is disruptive on admin UP ports. The switch performs a port admin‑status down, then port admin‑status up for the changes to take effect.
- Enabling or disabling Tx squelch control is not disruptive on admin DOWN ports. When you enable or disable Tx squelch control on an admin DOWN port, the new setting becomes effective the next time the port is admin UP.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link tx-squelch enabled 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> storm-control broadcast</h>

Configures the number of broadcast packets per second (pps) that signifies a broadcast storm. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 storm-control broadcast 400
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> storm-control multicast</h>

Configures the number of multicast packets per second (pps) that signifies a multicast storm. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 storm-control multicast 3000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> storm-control unknown-unicast</h>

Configures the number of unknown unicast packets per second (pps) that signifies an unknown unicast storm. You can set a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 storm-control unknown-unicast 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> tunnel dest-ip</h>

Configures the destination IP address for the GRE tunnel on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface tunnelR2 tunnel dest-ip 10.10.10.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> tunnel interface \<interface-name\></h>

Configures the GRE tunnel interface name.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface tunnelR2 tunnel interface MYGRETUNNEL
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> tunnel mode gre</h>

Enables GRE mode for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface tunnelR2 tunnel mode gre 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> tunnel source-ip</h>

Configures the source IP address for the GRE tunnel on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface tunnelR2 tunnel source-ip 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> tunnel ttl</h>

Configures the TTL for the GRE tunnel on the specified interface. You can set a value between 1 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface tunnelR2 tunnel ttl 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> type</h>

Configures the interface type. The type can be `swp`, `eth`, `bond`, `loopback`, `svi`, `sub`, `peerlink`, `tunnel`, `bridge` or `vrf`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 type swp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> vlan</h>

Configures the VLAN on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system link flap-protection interval</h>

Configures the duration in seconds during which a link must flap the number of times set in the link flap threshold before link flap protection triggers.

Cumulus Linux enables link flap detection by default. By default, link flap detection triggers when there are five link flaps within ten seconds, at which point the interface goes into a protodown state and shows link flap as the reason. The `switchd` service also shows a log message.

You can specify a value between 0 (off) and 300. The default setting is 10.

{{%notice note%}}
In Cumulus Linux 5.10 and earlier, you can specify a value between 0 (off) and 60.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link flap-protection interval 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system link flap-protection threshold 0-30</h>

Configures the number of times the link can flap within the link flap window before link flap protection triggers. You can specify a value between 0 (off) and 30. The default setting is 5.

Cumulus Linux enables link flap detection by default. By default, link flap detection triggers when there are five link flaps within ten seconds, at which point the interface goes into a protodown state and shows link flap as the reason. The `switchd` service also shows a log message.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1 link flap-protection threshold 8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> loopback ip address \<ip-prefix-id\></h>

Configures the loopback IP address in the specified VRF.

{{%notice note%}}
For the default VRF, use the `nv set interface lo ip address <ip-prefix-id>` command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<ip-prefix-id>` |  The IPv4 or IPv6 address and route prefix in CIDR notation.  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf RED loopback ip address 10.10.10.1/32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform transceiver \<interface-id\> temperature setpoint</h>

Configures the temperature thresholds for fan activation in the FAN algorithm, ensuring that they are below the module’s high warning threshold to optimize transceiver thermal performance and maintain a cooler operating environment before reaching critical temperatures. Lowering the thresholds leads to earlier and more frequent fan operation, increasing power usage and noise but protecting hardware performance and lifespan.

You can set a value between 30 and 80. The temperature threshold for an interface must be below the module advertised high warning threshold. If you configure the setpoint to be above the module advertised high temperature warning threshold, the FAN algorithm uses the module advertised threshold.

Setting the temperature thresholds does not change the module EEPROM-based alarm thresholds. The optical module continues reporting temperature alarms based on alarms or warning thresholds preprogrammed in the transceiver EEPROM.

{{%notice info%}}
Setting the temperature thresholds without proper guidance can result in transceiver damage, and might void your warranty and support agreements. This is an advanced configuration task; NVIDIA recommends you use the default transceiver temperature settings. Only modify this setting with approval from NVIDIA Technical Support.
{{%/notice%}}

- You can set temperature thresholds on the SN5610 switch only.
- Always use the parent transceiver name for configuration; for example, use swp1 not swp1s0.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set platform transceiver swp2 temperature setpoint 60
```
