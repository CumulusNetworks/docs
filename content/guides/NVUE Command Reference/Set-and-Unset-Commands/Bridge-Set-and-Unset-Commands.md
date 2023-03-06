---
title: Bridge Set and Unset Commands
author: Cumulus Networks
weight: 515
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set bridge

Configures a bridge on the switch.

### Attributes

| Atrribute |  Description   |
| ---------  | -------------- |
| `domain` |  Configures the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set bridge domain \<domain-id\>

Configures the bridge domain. The default bridge domain is `br_default`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0 

- - -

## nv set bridge domain \<domain-id\> stp

Configures STP on the bridge domain.

## nv set bridge domain \<domain-id\> stp priority

Configures the spanning tree priority. The bridge with the lowest priority is the root bridge. The priority must be a number between 0 and 61440, and must be a multiple of 4096. The default value is 32768.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default stp priority 8192
```

- - -

## nv set bridge domain \<domain-id\> multicast

Configures multicast on the bridge domain.

- - -

## nv set bridge domain \<domain-id\> multicast snooping

Configures IGMP and MLD snooping to prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments and MLD snooping is for IPv6 environments.

- - -

## nv set bridge domain \<domain-id\> multicast snooping querier

Configures the IGMP and MLD querier. Without a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

- - -

## nv set bridge domain \<domain-id\> multicast snooping querier enable

Turns the multicast querier on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default multicast snooping querier enable on
```

- - -

## nv set bridge domain \<domain-id\> multicast snooping enable

Turns IGMP and MLD snooping on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default multicast snooping enable on
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\>

Configures the VLAN tag identifier.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

Maps a VLAN to a VNI.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10`
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding

Configures how to handle BUM traffic.

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication \<hrep-id\>

Configures replication of BUM traffic where individual copies send to remote destinations.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |
| `<hrep-id>`  |  The IPv4 unicast addresses or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding enable

Turns flooding on or off for the VNI.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 flooding enable on
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding multicast-group \<ipv4-multicast\>

Configures BUM traffic to go to the specified multicast group, where receivers who are interested in that group recieve the traffic. This requires PIM-SM to be used in the network.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |
| `<ipv4-multicast>` | The multicast group.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 flooding multicast-group 224.0.0.10
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid> vni \<vni-id\> mac-learning

Turns MAC learning on or off for the VNI. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan 10 vni 10 mac-learning off
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> ptp

Configures Precision Time Protocol (PTP) on the VLAN (all interfaces in this VLAN).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> ptp enable

Turns PTP on or off for the specified VLAN. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan vlan10 ptp enable on
```

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast

Configures multicast on the VLAN.

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping

Configures IGMP and MLD snooping on the VLAN.

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier

Configures the IGMP and MLD querier on the VLAN.

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier source-ip \<source-ip\>

Configures the source IP address you want to use to send IGMP MLD queries.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` | The bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan vlan10 multicast snooping querier source-ip 10.10.10.1
```

- - -

## nv set bridge domain \<domain-id\> type vlan-aware

Configures the bridge domain to be VLAN-aware.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default type vlan-aware
```

- - -

## nv set bridge domain \<domain-id\> untagged

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default untagged none
```

- - -

## nv set bridge domain \<domain-id\> encap 802.1Q

Configures any interfaces in this bridge domain to use 802.1Q encapsulation by default.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default encap 802.1Q
```

- - -

## nv set bridge domain \<domain-id\> mac-address

Configures any interfaces in this bridge domain to use this MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default mac-address 00:00:00:00:00:10
```

- - -

## nv set bridge domain \<domain-id\> vlan-vni-offset

Configures the VNI offset when mapping VLANs to VNIs automatically. You can set a value between 0 and 16773120. For example, if you specify an offset of 10000, the VNI is the VLAN plus 10000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The bridge domain. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set bridge domain br_default vlan-vni-offset 10000
```

- - -
