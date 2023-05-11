---
title: Bridge
author: Cumulus Networks
weight: 530
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set bridge</h>

Configures a bridge on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\></h>

Configures the bridge domain. The default bridge domain is `br_default`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain br_default ageing</h>

Configures the number of seconds that Cumulus Linux stores MAC addresses in the Ethernet switching table. You can set a value between 0 and 65535. The default setting is 1800 seconds (30 minutes). A value of 0 turns MAC ageing off.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default ageing 600
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> encap 802.1Q</h>

Configures any interfaces in this bridge domain to use 802.1Q encapsulation by default.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default encap 802.1Q
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> mac-address</h>

Configures any interfaces in this bridge domain to use this MAC address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default mac-address 00:00:00:00:00:10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> multicast</h>

Configures multicast on the bridge domain.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> multicast snooping</h>

Configures IGMP and MLD snooping to prevent hosts on a local network from receiving traffic for a multicast group they have not explicitly joined. IGMP snooping is for IPv4 environments and MLD snooping is for IPv6 environments.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> multicast snooping enable</h>

Turns IGMP and MLD snooping on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default multicast snooping enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> multicast snooping querier</h>

Configures the IGMP and MLD querier. Without a multicast router, a single switch in an IP subnet can coordinate multicast traffic flows. This switch is the querier or the designated router. The querier generates query messages to check group membership, and processes membership reports and leave messages.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> multicast snooping querier enable</h>

Turns the multicast querier on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default multicast snooping querier enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> stp</h>

Configures STP on the bridge domain.

## <h>nv set bridge domain \<domain-id\> stp priority</h>

Configures the spanning tree priority. The bridge with the lowest priority is the root bridge. The priority must be a number between 0 and 61440, and must be a multiple of 4096. The default value is 32768.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default stp priority 8192
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> stp state</h>

Configures the STP state on the bridge. You can set a value of `up`, or `down`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default stp state up
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> type vlan-aware</h>

Configures the bridge domain to be VLAN-aware.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default type vlan-aware
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> untagged

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default untagged none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\></h>

Configures the VLAN tag identifier.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>` |  The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> ptp</h>

Configures Precision Time Protocol (PTP) on the VLAN (all interfaces in this VLAN).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> ptp enable</h>

Turns PTP on or off for the specified VLAN. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan vlan10 ptp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\>

Maps a VLAN to a VNI.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10 vni 10`
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding</h>

Configures how to handle BUM traffic.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding enable</h>

Turns flooding on or off for the VNI.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10 vni 10 flooding enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding head-end-replication \<hrep-id\></h>

Configures replication of BUM traffic where individual copies send to remote destinations.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |
| `<hrep-id>`  |  The IPv4 unicast addresses or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10 vni 10 flooding head-end-replication 10.10.10.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> vni \<vni-id\> flooding multicast-group \<ipv4-multicast\></h>

Configures BUM traffic to go to the specified multicast group, where receivers who are interested in that group receive the traffic. This requires PIM-SM to be used in the network.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |
| `<ipv4-multicast>` | The multicast group.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10 vni 10 flooding multicast-group 224.0.0.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid> vni \<vni-id\> mac-learning</h>

Turns MAC learning on or off for the VNI. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.
| `<vni-id>` | The VXLAN ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan 10 vni 10 mac-learning off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> multicast</h>

Configures multicast on the VLAN.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping</h>

Configures IGMP and MLD snooping on the VLAN.

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier</h>

Configures the IGMP and MLD querier on the VLAN.

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan \<vid\> multicast snooping querier source-ip \<source-ip\></h>

Configures the source IP address you want to use to send IGMP MLD queries.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>`   | The name of the bridge domain. |
| `<vid>`   |  The VLAN identifier.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan vlan10 multicast snooping querier source-ip 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set bridge domain \<domain-id\> vlan-vni-offset</h>

Configures the VNI offset when mapping VLANs to VNIs automatically. You can set a value between 0 and 16773120. For example, if you specify an offset of 10000, the VNI is the VLAN plus 10000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set bridge domain br_default vlan-vni-offset 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge</h>

Configures the bridged interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\></h>

Configures the bridged interface domain.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> access</h>

Configures access ports to ignore all tagged packets. You can set a value between 1 and 4094, `none`, or `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default access 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> learning</h>

Turns source MAC address learning on or off for this bridged interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default learning on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp</h>

Configures STP on the bridged interface domain.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp admin-edge</h>

Turns STP PortAdminEdge on or off on the bridged interface. PortAdminEdge is equivalent to the PortFast feature offered by other vendors. It enables or disables the initial edge state of a port in a bridge. All ports with PortAdminEdge on bypass the listening and learning states and go straight to forwarding.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default stp admin-edge on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp auto-edge</h>

Turns STP AutoEdge on or off on the bridged interface. PortAutoEdge is an enhancement to the standard PortAdminEdge (PortFast) mode, which allows for the automatic detection of edge ports. PortAutoEdge enables and disables the auto transition to and from the edge state of a port in a bridge.

When a port with PortAutoEdge receives a BPDU, the port stops being in the edge port state and transitions into a normal STP port. When the interface no longer receives BPDUs, the port becomes an edge port, and transitions through the discarding and learning states before it resumes forwarding.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default stp auto-edge on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp bpdu-filter</h>

Turns `bpdufilter` on or off on a bridge domain. When on, `bpdufilter` filters BPDUs in both directions.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default stp bpdu-filter on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp bpdu-guard</h>

Turns BPDU guard on or off on the bridged interface to protect the spanning tree topology from an unauthorized device affecting the forwarding path. For example, if you add a new host to an access port off a leaf switch and the host sends an STP BPDU, BPDU guard protects against undesirable topology changes in the environment.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default stp bpdu-guard on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp network</h>

Turns bridge assurance capability for a bridged port on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default stp network
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> stp restrrole</h>

Turns STP restricted role for the bridged port on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default stp restrrole
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> untagged</h>

Configures the VLAN in which untagged packets ingressing this bridged interface are in. Egress packets are always tagged. You can set a value between 1 and 4094, `none`, or `auto`. If you specify `none`, the switch drops untagged packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default untagged none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> bridge domain \<domain-id\> vlan \<vid\></h>

Configures a VLAN for the bridged interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<domain-id>` |  The name of the bridge domain. |
| `<vid>` |  The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 bridge domain default vlan 10
```
