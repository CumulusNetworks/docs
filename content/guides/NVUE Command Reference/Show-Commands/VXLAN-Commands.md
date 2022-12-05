---
title: VXLAN Commands
author: Cumulus Networks
weight: 340
product: Cumulus Linux
type: nojsscroll
---
## nv show nve vxlan

VxLAN

### Usage

`nv show nve vxlan [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `mlag`      | VxLAN specific MLAG address |
| `source`    | Source address |
| `flooding`  | Configuration to specify how BUM traffic in the overlay is handled. This applies to all overlays (VNIs), but can be overridden by VNI-specific configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan mlag

VxLAN specfic MLAG configuration

### Usage

`nv show nve vxlan mlag [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan source

Source address

### Usage

`nv show nve vxlan source [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding

Handling of BUM traffic

### Usage

`nv show nve vxlan flooding [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `head-end-replication` |  BUM traffic is replicated and individual copies sent to remote destinations.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding head-end-replication

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv show nve vxlan flooding head-end-replication [options] [<hrep-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<hrep-id>` |  IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan flooding head-end-replication \<hrep-id\>

Set of IPv4 unicast addresses or "evpn".

### Usage

`nv show nve vxlan flooding head-end-replication <hrep-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<hrep-id>` |  IPv4 unicast addresses or "evpn" |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan encapsulation

### Usage

`nv show nve vxlan encapsulation [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan encapsulation dscp

### Usage

`nv show nve vxlan encapsulation [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan decapsulation

### Usage

`nv show nve vxlan encapsulation [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show nve vxlan decapsulation dscp
