---
title: PIM Set and Unset Commands
author: Cumulus Networks
weight: 505
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set router pim

Configures PIM globally on the switch.

- - -

## nv set router pim timers

Configures PIM timers.

- - -

## nv set router pim timers hello-interval

Configures the interval in seconds at which the PIM router sends hello messages to discover PIM neighbors and maintain PIM neighbor relationships. You can specify a value between 1 and 180. The default setting is 30 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers hello-interval 60
```

- - -

## nv set router pim timers register-suppress

The number of seconds during which to stop sending register messages to the RP. You can specify a value between 5 and 60000 seconds. The default setting is 60 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers register-suppress 20000
```

- - -

## nv set router pim timers join-prune-interval

Configures the interval in seconds at which a PIM router sends join and prune messages to its upstream neighbors for a state update. You can specify a value between 60 and 600 seconds. The default setting is 60 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers join-prune-interval 100
```

- - -

## nv set router pim timers keep-alive

Configures the timeout value for the S,G stream in seconds. You can specify a value between 31 and 60000. The default setting is 210 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers keep-alive 10000
```

- - -

## nv set router pim timers rp-keep-alive

Configures the timeout value for the RP in seconds. You can specify a value between 31 and 60000. The default setting is 185 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim timers rp-keep-alive 10000
```

- - -

## nv set router pim enable

Turns PIM on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim enable on
```

- - -

## nv set router pim packets

Configures the number of incoming packets from the neighbor that PIM can process. You can specify a value between 1 and 100.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router pim packets 50
```

- - -

## nv set interface \<interface-id\> router pim

Configures PIM on an interface.

- - -

## nv set interface \<interface-id\> router pim timers

Configures PIM timers on an interface.

- - -

## nv set interface \<interface-id\> router pim timers hello-interval

Configures the PIM Hello packets periodic interval on the enabled PIM interface. The hold time is 3.5 times the `hello-interval`, the amount of time the neighbor must be in a reachable state.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface router pim timers hello-interval 100
```

- - -

## nv set interface \<interface-id\> router pim bfd

Configures BFD for the PIM enabled interface.

- - -

## nv set interface \<interface-id\> router pim bfd enable

Turns BFD on or off on the PIM enabled interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface router pim bfd on
```

- - -

## nv set interface \<interface-id\> router pim bfd detect-multiplier

Configures the BFD detect multiplier value for a PIM enabled interface. You can set a value between 2 and 255.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim bfd detect-multiplier  10
```

- - -

## nv set interface \<interface-id\> router pim bfd min-receive-interval

Configures the BFD minimum receive interval in milliseconds or a PIM enabled interface. You can set a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim bfd min-receive-interval 300
```

- - -

## nv set interface \<interface-id\> router pim bfd min-transmit-interval

Configures the BFD minimum transmit interval in milliseconds or a PIM enabled interface. You can set a value between 50 and 60000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim bfd min-transmit-interval 300
```

- - -

## nv set interface \<interface-id\> router pim address-family

Configures the address family on the PIM enabled interface.

- - -

## nv set interface \<interface-id\> router pim address-family ipv4-unicast

Configures the IPv4 unicast address family.

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set interface \<interface-id\> router pim address-family ipv4-unicast allow-rp

Configures the interface to ignore the RP check for all upstream neighbors. The default value is `off`.

- - -

## nv set interface \<interface-id\> router pim address-family ipv4-unicast allow-rp enable

Configures PIM to ignore the RP check for all upstream neighbors. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast allow-rp enable on
```

- - -

## nv set interface \<interface-id\> router pim address-family ipv4-unicast allow-rp rp-list

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
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast allow-rp rp-list myprefixlist
```

- - -

## nv set interface \<interface-id\> router pim address-family ipv4-unicast multicast-boundary-oil

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
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast multicast-boundary-oil MyPrefixList
```

- - -

## nv set interface \<interface-id\> router pim address-family ipv4-unicast use-source

Configures the PIM enabled interface to use the unique source address in the PIM Hello source field.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim address-family ipv4-unicast use-source 10.100.100.100
```

- - -

## nv set interface \<interface-id\> router pim enable

Turns PIM on or off on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim enable on
```

- - -

## nv set interface \<interface-id\> router pim dr-priority

Configures the Designated Router Election (DR) priority. You can specify a value between 1 and 4294967295.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 router pim dr-priority 100
```

- - -

## nv set interface \<interface-id\> router pim active-active

Turns PIM active-active on or off on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp51 router pim active-active on
```

- - -

## nv set vrf \<vrf-id\> router pim

Configures PIM on the specified VRF.

- - -

## nv set vrf \<vrf-id\> router pim timers

Configures PIM timers on the specified VRF.

- - -

## nv set vrf \<vrf-id\> router pim timers keep-alive

Configures the timeout value for the S,G stream in seconds for the specified VRF. You can set a value between 31 and 60000. The default setting is 210 seconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim timers keep-alive 10000
```

- - -

## nv set vrf \<vrf-id\> router pim timers rp-keep-alive

Configures the timeout value for the RP in seconds on the specified VRF. You can specify a value between 31 and 60000. The default setting is 185 seconds.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim timers rp-keep-alive 1000
```

- - -

## nv set vrf \<vrf-id\> router pim ecmp

Configures PIM ECMP on the specified VRF.

- - -

## nv set vrf \<vrf-id\> router pim ecmp enable

Turns ECMP for PIM on or off on the specified VRF. PIM uses RPF to choose an upstream interface to build a forwarding state. If you configure ECMP, PIM chooses the RPF based on the ECMP hash algorithm. The default value is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim ecmp enable on
```

- - -

## nv set vrf \<vrf-id\> router pim ecmp rebalance

Turns ECMP rebalance on or off on the specified VRF. ECMP rebalance recalculate all stream paths over one of the ECMP paths if the switch loses a path.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim ecmp rebalance on 
```

- - -

## nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\>

Configures the MSDP mesh group on the specified VRF. The mesh group must include all RPs in the domain as members, with a unique address as the source. This configuration results in MSDP peerings between all RPs.

- - -

## nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> member-address \<mesh-member-id\>

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
cumulus@leaf01:mgmt:~$ nv set vrf default router pim msdp-mesh-group cumulus member-address 100.1.1.2
```

- - -

## nv set vrf \<vrf-id\> router pim msdp-mesh-group \<msdp-mesh-group-id\> source-address \<ipv4\>

Configures the MSDP mesh group source IP address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<msdp-mesh-group-id>`  | The MSDP mesh group name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim msdp-mesh-group cumulus source-address 10.10.10.101
```

- - -

## nv set vrf \<vrf-id\> router pim address-family

Configures the address family for PIM.

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast

Configures the IPv4 unicast address family.

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover

Configures PIM SPT switchover for the specified VRF. When the LHR receives the first multicast packet, it sends a PIM (S,G) join towards the FHR to forward traffic through the network. This builds the SPT, or the tree that is the shortest path to the source. When the traffic arrives over the SPT, a PIM (S,G) RPT prune goes up the shared tree towards the RP. This removes multicast traffic from the shared tree; multicast data only goes over the SPT.

You can configure SPT switchover per group (SPT infinity), which allows for some groups to never switch to a shortest path tree. The LHR now sends both (*,G) joins and (S,G) RPT prune messages towards the RP.

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover action

Configures the SPT switchover action in the specified VRF. You can set the action to be `immediate` or `infinite`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim address-family ipv4-unicast spt-switchover action immediate
```

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast spt-switchover prefix-list \<instance-name\>

Applies the prefix list that specifies the multicast group range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<instance-name>` |   The prefix list name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim address-family ipv4-unicast spt-switchover prefix-list SPTrange
```

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\>

Configures RP settings for the specified VRF.

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> group-range \<group-range-id\>

Configures the group to RP mapping using the anycast address.

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
cumulus@leaf01:mgmt:~$ nv set vrf default router pim address-family ipv4-unicast rp 10.100.100.100 group-range 224.0.0.0/4
```

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast rp \<rp-id\> prefix-list \<instance-name\>

Applies a prefix list that specifies the multicast group range.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<rp-id>`  | The RP IP address. |
| `<instance-name>`  | The name of the prefix list. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast register-accept-list

Applies a prefix-list that specifies the source list to accept PIM register messages.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim address-family ipv4-unicast register-accept-list MYACCEPTLIST
```

## nv set vrf \<vrf-id\> router pim address-family ipv4-unicast send-v6-secondary

Turns sending IPv6 addresses as secondary addresses on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim address-family ipv4-unicast send-v6-secondary on
```

## nv set vrf \<vrf-id\> router pim enable

Turns PIM on or off in the specified VRF. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router pim enable on
```
- - -
