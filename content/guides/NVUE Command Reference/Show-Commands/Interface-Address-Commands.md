---
title: Interface Address Commands
author: Cumulus Networks
weight: 156
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip

IP configuration for an interface

### Usage

`nv show interface <interface-id> ip [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address`               | ipv4 and ipv6 address |
| `neighbor`              | IP neighbors |
| `vrr`                   | Configuration for VRR |
| `gateway`               | default ipv4 and ipv6 gateways |
| `ipv4`                  | IPv4 configuration for an interface |
| `ipv6`                  | IPv6 configuration for an interface |
| `igmp`                  | Configuration for IGMP|
| `vrrp`                  | Configuration for VRRP |
| `neighbor-discovery`    | Neighbor discovery configuration for an interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip address \<ip-prefix-id\>

An IP address with prefix

### Usage

`nv show interface <interface-id> ip address <ip-prefix-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ip-prefix-id>`  |  IPv4 or IPv6 address and route prefix in CIDR notation|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor

IP neighbors

### Usage

`nv show interface <interface-id> ip neighbor [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ipv4`  | IPv4 neighbors |
| `ipv6`  | IPv6 neighbors |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor ipv4 \<neighbor-id\>

A neighbor

### Usage

`nv show interface <interface-id> ip neighbor ipv4 <neighbor-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>`  | The IPv4 address of the neighbor node.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show interface \<interface-id\> ip neighbor ipv6 \<neighbor-id\>

A neighbor

### Usage

`nv show interface <interface-id> ip neighbor ipv6 <neighbor-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>`  | The IPv4 address of the neighbor node.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> loopback

The loopback IP interface associated with this VRF.

### Usage

`nv show vrf <vrf-id> loopback [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `ip` |  Properties associated with the loopback IP address on this VRF. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> loopback ip

IP addresses associated with the VRF's loopback interface.

### Usage

`nv show vrf <vrf-id> loopback ip [options] [<attribute> ...]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address` |  static IPv4 or IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> loopback ip address \<ip-prefix-id\>

An IP address with prefix

### Usage

`nv show vrf <vrf-id> loopback ip address <ip-prefix-id> [options]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<ip-prefix-id>` |    IPv4 or IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

