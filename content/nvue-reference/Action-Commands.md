---
title: Action Commands
author: Cumulus Networks
weight: 55

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
This document is in Beta.
{{%/notice%}}

## <h>nv action

Resets counters for interfaces, BGP, QoS buffers and pools, removes conflicts from protodown MLAG bonds, and disconnects system users.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface counters</h>

Clears all interface-specific counters from all interfaces. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded even though the switch detected no errors, the number of inbound and outbound packets not transmitted because of errors, and so on.

This command does not clear counters in the kernel or hardware.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface\> bond mlag lacp-conflict</h>

Clears the MLAG LACP conflict on the specified interface bond. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface>` | The interface that has an LACP conflict. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 bond mlag lacp-conflict 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface\> counters</h>

Clears all interface-specific counters from the specified interface. Interface counters provide information about an interface, such as the number of packets intentionally or intentionally dropped, the number of inbound and outbound packets discarded even though the switch detected no errors, the number of inbound and outbound packets not transmitted because of errors, and so on.

This command does not clear counters in the kernel or hardware.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> counters ptp</h>

Clears PTP counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear PTP counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 counters ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> qos buffer</h>

Clears QoS buffer counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear the QoS buffer. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 qos buffer
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear interface \<interface-id\> qos roce counters</h>

Clears QoS RoCE counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear RoCE counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 qos roce counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

<!--
## <h>nv action clear interface \<interface-id\> synce counters</h>

Clears SyncE counters on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<interface-id>` | The interface on which you want to clear synce counters. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear interface swp1 synce counters
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

-->
## <h>nv action clear mlag lacp-conflict</h>

Clears the MLAG LACP conflict. A conflict can be an LACP partner MAC address mismatch or a duplicate LACP partner MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv action clear mlag lacp-conflict 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear qos buffer multicast-switch-priority</h>

Clears the QoS multicast switch priority buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv action clear qos buffer multicast-switch-priority 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear qos buffer pool</h>

Clears the QoS pool buffers.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv action clear qos buffer pool 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear router policy route-map \<route-map-id\></h>

Clears counters for the specified route map.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<route-map-id>` | The route map you want to clear. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear router policy route-map ROUTEMAP1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear service ptp \<instance-id\> monitor violations log max-offset</h>

Clears PTP monitor violation log maximum offset value.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear service ptp 1 monitor violations log max-offset
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear service ptp \<instance-id\> monitor violations log min-offset</h>

Clears PTP monitor violation log minumum offset value.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear service ptp 1 monitor violations log min-offset
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear service ptp \<instance-id\> monitor violations log path-delay</h>

Clears the PTP  monitor violation log path delay value.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<instance-id>` |  The PTP instance number used for management purposes. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear service ptp 1 monitor violations log path-delay
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast in</h>

Clears BGP IPv4 inbound routes.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv4-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast out</h>

Clears BGP IPv4 outbound routes.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv4-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast soft in</h>

Clears BGP IPv4 inbound routes for all BGP peers.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv4-unicast soft out</h>

Clears BGP IPv4 outbound routes for all BGP peers.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast in</h>

Clears BGP IPv6 inbound routes.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast out</h>

Clears BGP IPv6 outbound routes.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast soft in</h>

Clears BGP IPv6 inbound routes for all BGP peers.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family ipv6-unicast soft out</h>

Clears BGP IPv6 outbound routes for all BGP peers.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family ipv6-unicast soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn in</h>

Clears BGP EVPN inbound routes.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn out</h>

Clears BGP EVPN outbound routes.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn soft in</h>

Clears BGP EVPN inbound routes for all BGP peers.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp address-family l2vpn-evpn soft out</h>

Clears BGP EVPN outbound routes for all BGP peers.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp address-family l2vpn-evpn soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> in</h>

Clears inbound routes for a specific BGP peer in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> out</h>

Clears outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> soft in</h>

Clears inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> soft out</h>

Clears outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast in</h>

Clears IPv4 inbound routes for a specific BGP peer in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast out</h>

Clears IPv4 outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast soft in</h>

Clears IPv4 inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv4-unicast soft out</h>

Clears IPv4 outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv4-unicast soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast in</h>

Clears IPv6 inbound routes for a specific BGP peer in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast out</h>

Clears IPv6 outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft in</h>

Clears IPv6 inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family ipv6-unicast soft out</h>

Clears IPv6 outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family ipv6-unicast soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn in</h>

Clears EVPN inbound routes for a specific BGP peer in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn out</h>

Clears EVPN outbound routes for a specific BGP peer in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft in</h>

Clears EVPN inbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp neighbor \<neighbor-id\> address-family l2vpn-evpn soft out</h>

Clears EVPN outbound routes for a specific BGP peer in the specified VRF without resetting the peer session.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<neighbor-id>` | The IP address of the BGP peer or the interface if you are using unnumbered BGP. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp neighbor swp51 address-family l2vpn-evpn soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> in</h>

Clears inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> out</h>

Clears outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> soft in</h>

Clears inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> soft out</h>

Clears outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast in</h>

Clears IPv4 inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast out</h>

Clears IPv4 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft in</h>

Clears IPv4 inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv4-unicast soft out</h>

Clears IPv4 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv4-unicast soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast in</h>

Clears IPv6 inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast out</h>

Clears IPv6 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft in</h>

Clears IPv6 inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family ipv6-unicast soft out</h>

Clears IPv6 outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family ipv6-unicast soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn in</h>

Clears EVPN inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn out</h>

Clears EVPN outbound routes for a specific BGP peer group in the specified VRF.

This command does not:
- Clear counters in the kernel or hardware.
- Reset BGP neighbor adjacencies.
- Readvertise all routes to BGP peers.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft in</h>

Clears EVPN inbound routes for a specific BGP peer group in the specified VRF.

This command do not clear counters in the kernel or hardware and does not reset BGP neighbor adjacencies.

- When the switch has a neighbor configured with `soft-reconfiguration inbound` enabled, this command clears the routes in the soft reconfiguration table for the address family. This results in reevaluating routes in the BGP table against any applied input policies.
- When the switch has a neighbor configured *without* the `soft-reconfiguration inbound` option enabled, this command sends the peer a route refresh message.
- If you do not specify the direction `in`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn soft in
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router bgp peer-group \<peer-group-id\> address-family l2vpn-evpn soft out</h>

Clears EVPN outbound routes for a specific BGP peer group in the specified VRF.

This command:
- Does not clear counters in the kernel or hardware
- Does not reset BGP neighbor adjacencies.
- Does not readvertise all routes to BGP peers.

If you do not specify the direction `out`, the command affects both inbound and outbound routes depending on whether soft-reconfiguration inbound is enabled.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<peer-group-id>` |  The peer group name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router bgp peer-group SPINES address-family l2vpn-evpn soft out
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router ospf interface</h>

Clears all counters for the OSPF interfaces.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router ospf interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action clear vrf \<vrf-id\> router ospf interface \<interface-id\></h>

Clears OSPF neighbor adjacency on the specified interface.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<vrf-id>` |  The VRF name.  |
| `<interface-id>` | The interface on which you want to clear OSPF neighbor adjacency. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv action clear vrf default router ospf interface swp2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv action disconnect system aaa user \<user\>

Disconnects authenticated and authorized users.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<user>` | The user you want to disconnect. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv action disconnect system aaa user admin2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show action</h>

Shows the actions taken, such cleared interface counters and routes, and removed protodown MLAG bond conflicts, and disconnected system users.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show action
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show action \<action-job-id\></h>

Shows information about the specified action.

### Command Syntax

| Syntax   |  Description  |
| ----------    | ------------  |
| `<action-job-id>` | The action ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show action 3
```
