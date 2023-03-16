---
title: VXLAN Commands
author: Cumulus Networks
weight: 310
product: Cumulus Linux
type: nojsscroll
---
## nv show nve vxlan

Shows global VXLAN configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan
```

- - -

## nv show nve vxlan mlag

Shows VXLAN specfic MLAG configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan mlag
```

- - -

## nv show nve vxlan source

Shows the VXLAN source address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan source
```

- - -

## nv show nve vxlan flooding

Shows VXLAN flooding configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan flooding
```

- - -

## nv show nve vxlan flooding head-end-replication

Shows VXLAN head end replication information.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan flooding head-end-replication
```

- - -

## nv show nve vxlan flooding head-end-replication \<hrep-id\>

Shows VXLAN head end replication information for the specified IP address or for EVPN.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<hrep-id>` | The IPv4 unicast address or `evpn`. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan flooding head-end-replication evpn
```

- - -

## nv show nve vxlan encapsulation

Show VXLAN encapsulation configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan encapsulation
```

- - -

## nv show nve vxlan encapsulation dscp

Shows the configured DSCP action and value during VXLAN encapsulation.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan encapsulation dscp
```

- - -

## nv show nve vxlan decapsulation

Show VXLAN decapsulation configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan decapsulation
```

- - -

## nv show nve vxlan decapsulation dscp

Shows the configured DSCP action and value during VXLAN decapsulation.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show nve vxlan decapsulation dscp
```
