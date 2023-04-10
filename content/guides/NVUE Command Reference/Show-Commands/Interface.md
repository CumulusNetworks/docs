---
title: Interface
author: Cumulus Networks
weight: 190
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> bond member

Shows the bond member configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 bond member
```

- - -

## nv show interface \<interface-id\> bond member \<member-id\>

Shows specific bond member configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 bond member bond1
```

- - -

## nv show interface \<interface\> counters

Shows all statistics for a specific interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 counters
```

- - -

## nv show interface \<interface\> counters drops

Shows packet drop counters for a specific interface.

## Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 counters drops
```

- - -

## nv show interface \<interface\> counters errors

Shows error counters for a specific interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 counters errors
```

- - -

## nv show interface \<interface\> counters pktdist

Shows packet distribution counters for a specific interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 counters pktdist
```

- - -

## nv show interface \<interface-id\> ip

Shows the IP address configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip
```

- - -

## nv show interface \<interface-id\> ip address

Shows the IP addresses configured for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip address
```

- - -

## nv show interface \<interface-id\> ip address \<ip-prefix-id\>

Shows details about the specified IP address for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ip-prefix-id>`  | The IPv4 or IPv6 address and route prefix in CIDR notation.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip address 10.10.10.1/32
```

- - -

## nv show interface \<interface-id\> ip gateway

Shows the gateway IP address for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip gateway
```

- - -

## nv show interface \<interface-id\> ip gateway \<ip-address-id\>

Shows information about a specific gateway IP address for the specified interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip gateway 10.10.10.1
```

- - -

## nv show interface \<interface-id\> ip ipv4

Shows IPv4 information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip ipv4
```

- - -

## nv show interface \<interface-id\> ip ipv6

Shows IPv6 information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip ipv6
```

- - -

## nv show interface \<interface-id\> ip neighbor

Shows information about the IP neighbors configured for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 ip neighbor
```

- - -

## nv show interface \<interface-id\> ip neighbor ipv4 \<neighbor-id\>

Shows information about the specified IPv4 neighbor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<neighbor-id>`  | The IPv4 address of the neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 ip neighbor ipv4 169.254.0.1
```

- - -

## nv show interface \<interface-id\> ip neighbor ipv6 \<neighbor-id\>

Shows information about the specified IPv6 neighbor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<neighbor-id>`  | The IPv4 address of the neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 ip neighbor ipv6 2001:db8:0002::0a00:0002
```

- - -

## nv show interface \<interface-id\> link

Shows configuration and statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link
```

- - -

## nv show interface \<interface-id\> link breakout

Shows the port breakouts for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link breakout 2x
```

- - -

## nv show interface \<interface-id\> link breakout \<mode-id\>

Shows information about a specific port breakout for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|
| `<mode-id>`    |  The breakout mode identifier: 1x, 2x, 4x, 8x, disabled, or loopback. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link breakout 2x
```

- - -

## nv show interface \<interface-id\> link flag

Shows link flags for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link flag
```

- - -

## nv show interface \<interface-id\> link state

Shows the state of the specified interface; if the link is up or down.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link state
```

- - -

## nv show interface \<interface-id\> link stats

Shows statistics for the specified interface, such as packet size, packet drops, and packet errors.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link stats
```

- - -

## nv show interface \<interface-id\> link traffic-engineering

Shows traffic engineering statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 link traffic-engineering
```

- - -

## nv show interface \<interface-id\> pluggable

Shows the <span style="background-color:#F5F5DC">[SFP](## "Small Form-Factor Pluggable")</span> module information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`  |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 pluggable
```

- - -

## nv show interface \<interface-id\> storm-control

Shows storm control configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 storm-control
```

- - -

## nv show interface \<interface-id\> tunnel

Shows tunnel information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 tunnel
```

- - -

## nv show interface --view=counters

Shows all statistics for all the interfaces configured on the switch.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface --view=counters
```

- - -

## nv show vrf \<vrf-id\> loopback

Shows the loopback interfaces associated with this VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default loopback
```

- - -

## nv show vrf \<vrf-id\> loopback ip

Shows the IP addresses associated with the loopback interface for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default loopback ip
```

- - -

## nv show vrf \<vrf-id\> loopback ip address \<ip-prefix-id\>

Shows details about the specified loopback IP address for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default loopback ip address 10.10.10.1/32
```

- - -
