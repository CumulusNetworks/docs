---
title: Interface Address Commands
author: Cumulus Networks
weight: 156
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip

IP configuration for an interface

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip address \<ip-prefix-id\>

An IP address with prefix

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ip-prefix-id>`  |  IPv4 or IPv6 address and route prefix in CIDR notation|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor

IP neighbors

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor ipv4 \<neighbor-id\>

A neighbor

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>`  | The IPv4 address of the neighbor node.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip neighbor ipv6 \<neighbor-id\>

A neighbor

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<neighbor-id>`  | The IPv4 address of the neighbor node.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> loopback

The loopback IP interface associated with this VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> loopback ip

IP addresses associated with the VRF's loopback interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> loopback ip address \<ip-prefix-id\>

An IP address with prefix

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<ip-prefix-id>` |    IPv4 or IPv6 address and route prefix in CIDR notation |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
