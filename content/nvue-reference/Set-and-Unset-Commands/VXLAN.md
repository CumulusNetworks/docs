---
title: VXLAN
author: Cumulus Networks
weight: 810

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set nve vxlan</h>

Configures VXLAN settings on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan arp-nd-suppress</h>

Turns VXLAN ARP and ND suppression on or off. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan arp-nd-suppress off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan decapsulation</h>

Configures VXLAN decapsulation.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan decapsulation dscp action</h>

Configures the VXLAN decapsulation DSCP or COS action. You can specify one of the following options:
- `copy` (if the inner packet is IP).
- `preserve` (the inner DSCP does not change).
- `derive` (from the switch priority).

### Example

```
cumulus@switch:~$ nv set nve vxlan decapsulation dscp action derive
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan enable</h>

Turns VXLAN on or off globally.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan encapsulation</h>

Configures VXLAN encapsulation.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan encapsulation dscp action</h>

Configures the VXLAN outer DSCP action during encapsulation. You can specify one of the following options:
- `copy` (if the inner packet is IP)
- `set` (to a specific value)
- `derive` (from the switch priority).

The default setting is `derive`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp action derive
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan encapsulation dscp value</h>

Configures the DSCP value to put in outer VXLAN packets.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp 16
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan flooding</h>

Configures VXLAN flooding (how to handle BUM traffic).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan flooding enable</h>

Turns VXLAN flooding on or off.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan flooding enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan flooding head-end-replication \<hrep-id\></h>

Configures VXLAN head end replication, where the switch replicates BUM traffic and sends individual copies to remote destinations.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hrep-id>` |  The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan flooding head-end-replication 10.10.10.2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan flooding multicast-group \<ipv4-multicast\></h>

Configures the multicast group for VXLAN flooding. BUM traffic goes to the specified multicast group, where receivers with an interest in that group receive the traffic. This usually requires that you use PIM-SM in the network.

One multicast group per layer 2 VNI is optimal configuration for underlay bandwidth utilization. However, you can specify the same multicast group for more than one layer 2 VNI.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<ipv4-multicast>` |  The multicast group. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan flooding multicast-group 224.0.0.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan mac-learning</h>

Turns VXLAN MAC learning on or off.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan mac-learning on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan mlag shared-address \<shared-address\></h>

Configures the anycast IP address for VXLAN active-active.

### Command Syntax

| Syntax  | Description |
| ------- | ----------- |
| `<shared-address>` | The anycast IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan mlag shared-address 10.0.1.12
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan mtu</h>

Configures the MTU for VXLAN interfaces.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan mtu 1500
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan port</h>

Configures the UDP port for VXLAN frames.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan port 1024
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set nve vxlan source address \<source-address\></h>

Configures the local tunnel IP address for VXLAN tunnels.

### Command Syntax

| Syntax  | Description |
| ------- | ----------- |
| `<source-address>` | The IPv4 address or `auto`. `auto` sets the address to the primary loopback address of the switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set nve vxlan source address 10.10.10.1
```
