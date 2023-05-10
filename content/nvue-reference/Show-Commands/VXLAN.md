---
title: VXLAN
author: Cumulus Networks
weight: 450

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show nve vxlan</h>

Shows global VXLAN configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan decapsulation

Shows VXLAN decapsulation configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan decapsulation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan decapsulation dscp</h>

Shows the configured DSCP action and value during VXLAN decapsulation.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan decapsulation dscp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan encapsulation

Shows VXLAN encapsulation configuration.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan encapsulation
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

# nv show nve vxlan encapsulation dscp</h>

Shows the configured DSCP action and value during VXLAN encapsulation.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show nve vxlan encapsulation dscp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan flooding</h>

Shows VXLAN flooding configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan flooding
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan flooding head-end-replication</h>

Shows VXLAN head end replication information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan flooding head-end-replication
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan flooding head-end-replication \<hrep-id\></h>

Shows VXLAN head end replication information for the specified IP address or for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<hrep-id>` | The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan flooding head-end-replication evpn
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan mlag</h>

Shows VXLAN specfic MLAG configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan mlag
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show nve vxlan source</h>

Shows the VXLAN source address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show nve vxlan source
```
