---
title: VRR and VRRP Commands
author: Cumulus Networkss
weight: 350
product: Cumulus Linux
type: nojsscroll
---
## nv show interface <interface-id\> ip vrr

Configuration for VRR

### Usage

`nv show interface <interface-id> ip vrr [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address`  | Virtual addresses with prefixes
| `state`  | The state of the interface

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip vrr address \<ip-prefix-id\>

An IP address with prefix

### Usage

`nv show interface <interface-id> ip vrr address <ip-prefix-id> [options]`

### Identifiers

| Identifier |  Description   |
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

### Usage

`nv show interface <interface-id> ip vrr state [options]`

### Identifiers

| Identifier |  Description   |
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

### Usage

`nv show interface <interface-id> ip vrrp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `virtual-router`   | Group of virtual gateways implemented with VRRP|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\>

A virtual gateway implemented with VRRP

### Usage

`nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |
| `<virtual-router-id>` |  Virtual Router IDentifier (VRID)|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `address`  |     A set of virtual addresses for VRRPv3|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\>

An IP address

### Usage

`nv show interface <interface-id> ip vrrp virtual-router <virtual-router-id> address <ip-address-id> [options]`

### Identifiers

| Identifier |  Description   |
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
