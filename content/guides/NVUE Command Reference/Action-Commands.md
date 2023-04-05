---
title: Action Commands
author: Cumulus Networks
weight: 55
product: Cumulus Linux
---
{{%notice note%}}
This document is in Beta.
{{%/notice%}}

## nv action

Resets counters for interfaces, QoS buffers and pools, removes conflicts from protodown MLAG bonds, and disconnects system users.

- - -

## nv action clear interface \<interface\\> bond mlag lacp-conflict

Clears the MLAG LACP conflict on the specified interface bond. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface>` | The interface that has an LACP conflict. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 bond mlag lacp-conflict 
```

- - -

## nv action clear interface \<interface-id\> ptp counters

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear PTP counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 ptp counters
```

- - -

## nv action clear interface \<interface-id\> qos buffer

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear the QoS buffer. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 qos buffer
```

- - -

## nv action clear interface \<interface-id\> qos counter

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear QoS counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 qos counter
```

- - -

## nv action clear interface \<interface-id\> qos roce counters

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear RoCE counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 qos roce counter
```

- - -

## nv action clear interface \<interface-id\> synce counters

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear synce counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 synce counters
```

- - -

## nv action clear mlag lacp-conflict

Clears the MLAG LACP conflict. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear mlag lacp-conflict 
```

- - -

## nv action clear qos buffer multicast-switch-priority

Clears the QoS multicast switch priority buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear qos buffer multicast-switch-priority 
```

- - -

## nv action clear qos buffer pool

Clears the QoS pool buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear qos buffer pool 
```

- - -

## nv action clear router policy route-map \<route-map-id\>

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<route-map-id>` | The route map you want to clear. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear router policy route-map ROUTEMAP1
```

## nv action clear service ptp \<instance-id\> monitor violations log max-offset

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear service ptp 1 monitor violations log max-offset
```

- - -

## nv action clear service ptp \<instance-id\> monitor violations log min-offset

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear service ptp 1 monitor violations log min-offset
```

- - -

## nv action clear service ptp \<instance-id\> monitor violations log path-delay

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear service ptp 1 monitor violations log path-delay
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast in

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family ipv4-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast out

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family ipv4-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast soft in

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast soft out

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast in

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family ipv6-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast out

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family ipv6-unicast out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn in

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family l2vpn-evpn in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn out

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family l2vpn-evpn out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn soft in

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn soft out

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast soft out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn out
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft in

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn soft in
```

- - -

## nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft out

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn soft out
```

- - -

## nv action clear vrf \<vrf-id\> router ospf interface \<interface-id\>

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<interface-id>` | The interface. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router ospf interface swp2
```

- - -

## nv action disconnect system aaa user \<user\>

Disconnects authenticated and authorized users.

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<user>` | The user you want to disconnect. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action disconnect system aaa user admin2
```

- - -

## nv show action

Shows the actions taken, such interface counter resets, removed protodown MLAG bond conflicts, and disconnected system users.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show action
```

- - -

## nv show action \<action-job-id\>

Shows information about the specified action.

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<action-job-id>` | The action ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show action 3
```

- - -
