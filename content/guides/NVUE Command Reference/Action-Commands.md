---
title: Action Commands
author: Cumulus Networks
weight: 55
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
This document is in Beta.
{{%/notice%}}

## nv action

Resets counters for interfaces, BGP, QoS buffers and pools, removes conflicts from protodown MLAG bonds, and disconnects system users.

- - -

## nv action clear interface counters

Clears all interface-specific counters from all interfaces. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded even though the switch detected no errors, the number of inbound and outbound packets not transmitted because of errors, and so on.

This command does not clear counters in the kernel or hardware.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface counters
```

- - -

## nv action clear interface \<interface\> bond mlag lacp-conflict

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

## nv action clear interface \<interface\> counters

Clears all interface-specific counters from the specified interface. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded even though the switch detected no errors, the number of inbound and outbound packets not transmitted because of errors, and so on.

This command does not clear counters in the kernel or hardware.

### Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear interface swp1 counters
```

- - -

## nv action clear interface \<interface-id\> ptp counters

Clears PTP counters on the specified interface.

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

Clears QoS buffer counters on the specified interface.

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

Clears QoS counters on the specified interface.

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

Clears QoS RoCE counters on the specified interface.

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

Clears SyncE counters on the specified interface.

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

Clears counters for the specified route map.

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

Clears PTP monitor violation log maximum offset value.

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

Clears PTP monitor violation log minumum offset value.

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

Clears the PTP  monitor violation log path delay value.

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

Clears BGP IPv4 inbound routes.

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

Clears BGP IPv4 outbound routes.

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

Clears BGP IPv4 inbound routes for all BGP peers without resetting the peer sessions.

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

Clears BGP IPv4 outbound routes for all BGP peers without resetting the peer sessions.

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

Clears BGP IPv6 inbound routes.

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

Clears BGP IPv6 outbound routes.

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

Clears BGP IPv6 inbound routes for all BGP peers without resetting the peer sessions.

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

Clears BGP IPv6 outbound routes for all BGP peers without resetting the peer sessions.

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

Clears BGP layer 2 VPN EVPN inbound routes.

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

Clears BGP layer 2 VPN EVPN outbound routes.

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

Clears BGP layer 2 VPN EVPN inbound routes for all BGP peers without resetting the peer sessions.

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

Clears BGP layer 2 VPN EVPN outbound routes for all BGP peers without resetting the peer sessions.

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

Clears inbound routes for a specific BGP peer in the specified VRF.

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

Clears outbound routes for a specific BGP peer in the specified VRF.

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

Clears inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears IPv4 inbound routes for a specific BGP peer in the specified VRF.

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

Clears IPv4 outbound routes for a specific BGP peer in the specified VRF.

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

Clears IPv4 inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears IPv4 outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears IPv6 inbound routes for a specific BGP peer in the specified VRF.

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

Clears IPv6 outbound routes for a specific BGP peer in the specified VRF.

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

Clears IPv6 inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears IPv6 outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears layer 2 VPN EVPN inbound routes for a specific BGP peer in the specified VRF.

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

Clears layer 2 VPN EVPN outbound routes for a specific BGP peer in the specified VRF.

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

Clears layer 2 VPN EVPN inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears layer 2 VPN EVPN outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

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

Clears inbound routes for a specific BGP peer group in the specified VRF.

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

Clears outbound routes for a specific BGP peer group in the specified VRF.

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

Clears inbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears outbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears IPv4 inbound routes for a specific BGP peer group in the specified VRF.

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

Clears IPv4 outbound routes for a specific BGP peer group in the specified VRF.

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

Clears IPv4 inbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears IPv4 outbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears IPv6 inbound routes for a specific BGP peer group in the specified VRF.

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

Clears IPv6 outbound routes for a specific BGP peer group in the specified VRF.

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

Clears IPv6 inbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears IPv6 outbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears layer 2 VPN EVPN inbound routes for a specific BGP peer group in the specified VRF.

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

Clears layer 2 VPN EVPN outbound routes for a specific BGP peer group in the specified VRF.

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

Clears layer 2 VPN EVPN inbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

Clears layer 2 VPN EVPN outbound routes for a specific BGP peer group in the specified VRF without resetting the peer sessions.

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

## nv action clear vrf \<vrf-id\> router ospf interface

Clears all counters for the OSPF interfaces.

## Command Syntax

| \<div style="width:250px">Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router ospf interface
```

- - -

## nv action clear vrf \<vrf-id\> router ospf interface \<interface-id\>

Clears OSPF neighbor adjacency on the specified interface.

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

Shows the actions taken, such cleared interface counters and routes, and removed protodown MLAG bond conflicts, and disconnected system users.

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
