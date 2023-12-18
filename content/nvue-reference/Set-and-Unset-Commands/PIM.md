---
title: PIM
author: Cumulus Networks
weight: 650

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> router pim</h>

Configures PIM on an interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim active-active</h>

Turns PIM active-active on or off on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim active-active on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family</h>

Configures the address family on the PIM interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family ipv4</h>

Configures the IPv4 address family on the interface.

{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the `nv set interface <interface-id> router pim address-family ipv4` command is `nv set interface <interface-id> router pim address-family ipv4-unicast`
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family ipv4 allow-rp</h>

Configures the PIM interface to ignore the RP check for all upstream neighbors. The default value is `off`.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family ipv4 allow-rp enable</h>

Configures the PIM interface to ignore the RP check for all upstream neighbors. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim address-family ipv4 allow-rp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family ipv4 allow-rp rp-list</h>

Configures PIM to only ignore the RP check for the upstream neighbors in the specified prefix list.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<instance-name>` | The name of the prefix list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim address-family ipv4 allow-rp rp-list myprefixlist
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family ipv4 multicast-boundary-oil</h>

Configures multicast boundaries to limit the distribution of multicast traffic and push multicast to a subset of the network.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<instance-name>` | The name of the prefix list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim address-family ipv4 multicast-boundary-oil MyPrefixList
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim address-family ipv4 use-source</h>

Configures the PIM interface to use the unique source address in the PIM Hello source field.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim address-family ipv4 use-source 10.100.100.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim bfd</h>

Configures BFD for the PIM interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim bfd detect-multiplier</h>

Configures the BFD detect multiplier value for a PIM interface. You can set a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim bfd detect-multiplier  10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim bfd enable</h>

Turns BFD on or off on the PIM interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface router pim bfd on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim bfd min-receive-interval</h>

Configures the BFD minimum receive interval in milliseconds for a PIM interface. You can set a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim bfd min-receive-interval 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim bfd min-transmit-interval</h>

Configures the BFD minimum transmit interval in milliseconds for a PIM interface. You can set a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim bfd min-transmit-interval 300
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim dr-priority</h>

Configures the Designated Router Election (DR) priority for the PIM interface. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 router pim dr-priority 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim enable</h>

Turns PIM on or off for an interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp51 router pim enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim timers</h>

Configures PIM timers on the interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router pim timers hello-interval</h>

Configures the PIM Hello packets periodic interval on the PIM interface. The hold time is 3.5 times the `hello-interval`, the amount of time the neighbor must be in a reachable state.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface router pim timers hello-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim</h>

Configures PIM globally on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim enable</h>

Turns PIM on or off globally. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pim enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim packets</h>

Configures the number of incoming packets from the neighbor that PIM can process. You can specify a value between 1 and 100.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pim packets 50
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim timers</h>

Configures PIM timers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim timers hello-interval</h>

Configures the interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships. You can specify a value between 1 and 180. The default setting is 30 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pim timers hello-interval 60
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim timers join-prune-interval</h>

Configures the interval in seconds at which a PIM router sends join and prune messages to its upstream neighbors for a state update. You can specify a value between 60 and 600 seconds. The default setting is 60 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pim timers join-prune-interval 100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim timers keep-alive</h>
<!--
## <h>nv set router pim timers keepalive</h>
-->
Configures the timeout value for the S,G stream in seconds. You can specify a value between 31 and 60000. The default setting is 210 seconds.
<!--
{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the command is `nv set router pim timers keep-alive`.
{{%/notice%}}
-->
### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pim timers keep-alive 10000
```
<!--
```
cumulus@switch:~$ nv set router pim timers keepalive 10000
```
-->
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim timers register-suppress</h>

The number of seconds during which to stop sending register messages to the RP. You can specify a value between 5 and 60000 seconds. The default setting is 60 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router pim timers register-suppress 20000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router pim timers rp-keepalive</h>

Configures the timeout value for the RP in seconds. You can specify a value between 31 and 60000. The default setting is 185 seconds.

{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the command is `nv set router pim timers rp-keep-alive`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set router pim timers rp-keepalive 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim</h>

Configures PIM on the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family</h>

Configures the address family for PIM on the specified VRF.

{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the `nv set vrf <vrf-id> router pim address-family ipv4` command is `nv set vrf <vrf-id> router pim address-family ipv4-unicast`
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4</h>

Configures the IPv4 unicast address family on the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 register-accept-list</h>

Applies a prefix-list that specifies the source list to accept PIM register messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4 register-accept-list MYACCEPTLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 rp \<rp-id\></h>

Configures RP settings for the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 rp \<rp-id\> group-range \<group-range-id\></h>

Configures the group to RP mapping using the anycast address on the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rp-id>`  | The RP IP address.|
| `<group-range-id>` |  The group range associated with the RP.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4 rp 10.100.100.100 group-range 224.0.0.0/4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 rp \<rp-id\> prefix-list \<instance-name\></h>

Applies a prefix list that specifies the multicast group range on the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rp-id>`  | The RP IP address. |
| `<instance-name>`  | The name of the prefix list. |

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 send-v6-secondary</h>

Turns sending IPv6 addresses as secondary addresses on or off on the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4 send-v6-secondary on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 spt-switchover</h>

Configures PIM SPT switchover for the specified VRF. When the LHR receives the first multicast packet, it sends a PIM (S,G) join towards the FHR to forward traffic through the network. This builds the SPT, or the tree that is the shortest path to the source. When the traffic arrives over the SPT, a PIM (S,G) RPT prune goes up the shared tree towards the RP. This removes multicast traffic from the shared tree; multicast data only goes over the SPT.

You can configure SPT switchover per group (SPT infinity), which allows for some groups to never switch to a shortest path tree. The LHR now sends both (*,G) joins and (S,G) RPT prune messages towards the RP.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 spt-switchover action</h>

Configures the SPT switchover action in the specified VRF. You can set the action to be `immediate` or `infinite`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4 spt-switchover action immediate
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 spt-switchover prefix-list \<instance-name\></h>

Applies the prefix list that specifies the multicast group range on the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<instance-name>` |   The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4 spt-switchover prefix-list SPTrange
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim address-family ipv4 ssm-prefix-list</h>

Applies a prefix-list to specify the Source Specific Multicast (SSM) group range on the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim address-family ipv4 ssm-prefix-list SSMPREFIXLIST
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim ecmp</h>

Configures PIM ECMP on the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim ecmp enable</h>

Turns ECMP for PIM on or off on the specified VRF. PIM uses RPF to choose an upstream interface to build a forwarding state. If you configure ECMP, PIM chooses the RPF based on the ECMP hash algorithm. The default value is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim ecmp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim ecmp rebalance</h>

Turns ECMP rebalance on or off on the specified VRF. ECMP rebalance recalculate all stream paths over one of the ECMP paths if the switch loses a path.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim ecmp rebalance on 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim enable</h>

Turns PIM on or off in the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\></h>

Configures the MSDP mesh group on the specified VRF. The mesh group must include all RPs in the domain as members, with a unique address as the source. This configuration results in MSDP peerings between all RPs.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\></h>

Configures the MSDP mesh member IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<msdp-mesh-group-id>`  | The MSDP mesh group name. |
| `<mesh-member-id>`  | The MSDP mesh-group member IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> source-address \<ipv4\></h>

Configures the MSDP mesh group source IP address on the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<msdp-mesh-group-id>`  | The MSDP mesh group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim msdp-mesh-group cumulus source-address 10.10.10.101
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim timers</h>

Configures PIM timers on the specified VRF.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim timers keep-alive</h>
<!--
## <h>nv set vrf \<vrf-id\> router pim timers keepalive</h>
-->
Configures the timeout value for the S,G stream in seconds for the specified VRF. You can set a value between 31 and 60000. The default setting is 210 seconds.

<!--
{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the command is `nv set vrf <vrf-id> router pim timers keep-alive`.
{{%/notice%}}
-->
### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim timers keep-alive 10000
```
<!--
```
cumulus@switch:~$ nv set vrf default router pim timers keepalive 10000
```
-->

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router pim timers rp-keep-alive</h>
<!--
## <h>nv set vrf \<vrf-id\> router pim timers rp-keepalive</h>
-->
Configures the timeout value for the RP in seconds on the specified VRF. You can specify a value between 31 and 60000. The default setting is 185 seconds.
<!--
{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the command is `nv set vrf <vrf-id> router pim timers rp-keep-alive`.
{{%/notice%}}
-->
### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router pim timers rp-keep-alive 1000
```
<!--
```
cumulus@switch:~$ nv set vrf default router pim timers rp-keepalive 1000
```
-->
