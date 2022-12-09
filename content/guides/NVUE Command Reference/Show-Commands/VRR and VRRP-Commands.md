---
title: VRR and VRRP Commands
author: Cumulus Networkss
weight: 350
product: Cumulus Linux
type: nojsscroll
---
## nv show interface <interface-id\> ip vrr

Configuration for VRR

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

## nv show interface \<interface-id\> ip vrr address \<ip-prefix-id\>

An IP address with prefix

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<ip-prefix-id>`| IPv4 or IPv6 address and route prefix in CIDR notation|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip vrr state

The state of the interface

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

## nv show interface \<interface-id\> ip vrrp

Configuration for VRRP

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

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\>

A virtual gateway implemented with VRRP

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<virtual-router-id>` |  Virtual Router IDentifier (VRID)|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\>

An IP address

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<virtual-router-id>`    | Virtual Router IDentifier (VRID) |
| `<ip-address-id>`        | IPv4 or IPv6 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
