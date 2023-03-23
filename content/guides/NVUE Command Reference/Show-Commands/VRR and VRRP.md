---
title: VRR and VRRP
author: Cumulus Networkss
weight: 440
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip vrr

Shows VRR configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface vlan10 ip vrr
```

- - -

## nv show interface \<interface-id\> ip vrr address \<ip-prefix-id\>

Shows the information about the specified VRR IP address on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |
| `<ip-prefix-id>`| The IPv4 or IPv6 address and route prefix in CIDR notation.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface vlan10 ip vrr address 10.1.10.1/24
```

- - -

## nv show interface \<interface-id\> ip vrr state

Shows the state of the specified VRR interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface vlan10 ip vrr state
```

- - -

## nv show router vrr

Shows global VRR configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router vrr
```

- - -

## nv show interface \<interface-id\> ip vrrp

Shows VRRP configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |   The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip vrrp
```

- - -

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\>

Shows information about the virtual gateway implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID) that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip vrrp virtual-router 44
```

- - -

## nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\>

Shows information about the IP address of the virtual gateway implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID) that identifies the group of VRRP routers.|
| `<ip-address-id>`        | The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

- - -

## nv show router vrrp

Shows global VRRP configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show router vrrp
```

- - -
