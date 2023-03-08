---
title: VXLAN Set and Unset Commands
author: Cumulus Networks
weight: 740
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set nve vxlan

Configures VXLAN settings on the switch.

- - -

## nv set nve vxlan mlag shared-address \<shared-address\>

Configures the anycast IP address for VXLAN active-active.

### Command Syntax

| Syntax  | Description |
| ------- | ----------- |
| `<shared-address>` | The anycast IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan mlag shared-address 10.0.1.12
```

- - -

## nv set nve vxlan source address \<source-address\>

Configures the local tunnel IP address for VXLAN tunnels.

### Command Syntax

| Syntax  | Description |
| ------- | ----------- |
| `<source-address>` | The IPv4 address or `auto`. `auto` sets the address to the primary loopback address of the switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan source address 10.10.10.1
```

- - -

## nv set nve vxlan flooding

Configures VXLAN flooding (how to handle BUM traffic).

- - -

## nv set nve vxlan flooding head-end-replication \<hrep-id\>

Configures VXLAN head end replication where BUM traffic is replicated and individual copies sent to remote destinations.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hrep-id>` |  The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan flooding head-end-replication 10.10.10.2
```

- - -

## nv set nve vxlan encapsulation

Configures VXLAN encapsulation.

- - -

## nv set nve vxlan encapsulation dscp value

Configures the DSCP value to put in outer VXLAN packet.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan encapsulation dscp 16
```

- - -

## nv set nve vxlan encapsulation dscp action

Configures the VXLAN outer DSCP action during encapsulation. You can specify one of the following options:
- `copy` (if the inner packet is IP)
- `set` (to a specific value)
- `derive` (from the switch priority).

The default setting is `derive`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan encapsulation dscp action derive
```

- - -

## nv set nve vxlan decapsulation

Configures VXLAN decapsulation.  You can specify one of the following options:

- - -

## nv set nve vxlan decapsulation dscp action

Configures the VXLAN decapsulation DSCP/COS action. You can specify one of the following options:
- `copy` (if the inner packet is IP).
- `preserve` (the inner DSCP does not change).
- `derive` (from the switch priority).

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan decapsulation dscp action derive
```

- - -

## nv set nve vxlan flooding enable

Turns VXLAN flooding on or off.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan flooding enable on
```

- - -

## nv set nve vxlan flooding multicast-group \<ipv4-multicast\>

Configures the multicast group for VXLAN flooding. BUM traffic goes to the specified multicast group and is received by receivers that are interested in that group. This usually requires that you use PIM-SM in the network.

One multicast group per layer 2 VNI is optimal configuration for underlay bandwidth utilization. However, you can specify the same multicast group for more than one layer 2 VNI.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<ipv4-multicast>` |  The multicast group. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan flooding multicast-group 224.0.0.10
```

- - -

## nv set nve vxlan enable

Turns VXLAN on or off globally.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan enable on
```

- - -
## nv set nve vxlan mac-learning

Turns VXLAN MAC learning on or off.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan mac-learning on
```

- - -

## nv set nve vxlan port

Configures the UDP port for VXLAN frames.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan port 1024
```

- - -

## nv set nve vxlan arp-nd-suppress

Turns VXLAN ARP and ND suppression on or off. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan arp-nd-suppress off
```

- - -

## nv set nve vxlan mtu

Configures the MTU for VXLAN interfaces.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set nve vxlan mtu 1500
```

- - -
