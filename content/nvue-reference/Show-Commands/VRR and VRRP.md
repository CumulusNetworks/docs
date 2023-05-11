---
title: VRR and VRRP
author: Cumulus Networkss
weight: 440

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrr</h>

Shows VRR configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 ip vrr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrr address \<ip-prefix-id\></h>

Shows the information about a specific VRR IP address on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |  The interface name. |
| `<ip-prefix-id>`| The IPv4 or IPv6 address and route prefix in CIDR notation.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 ip vrr address 10.1.10.1/24
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrr state</h>

Shows the state of the specified VRR interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface vlan10 ip vrr state
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router vrr</h>

Shows global VRR configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router vrr
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp</h>

Shows VRRP configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |   The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router</h>

Shows the virtual gateways implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\></h>

Shows information about a specific virtual gateway implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID) that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address</h>

Shows the IP addresses of the virtual gateway implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID) that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44 address
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\></h>

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
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address-family</h>

Shows the IP addresses for all address families for the virtual gateway implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
|| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID) that identifies the group of VRRP routers.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44 address-family
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address-family \<afi\></h>

Shows the IP addresses for a specific address family (IPv4 or IPv6) for the virtual gateway implemented with VRRP for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |
| `<virtual-router-id>` |  The Virtual Router IDentifier (VRID) that identifies the group of VRRP routers.|
| `<afi>` |  The address family; `ipv4` or `ipv6`.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ip vrrp virtual-router 44 address-family ipv4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router vrrp</h>

Shows global VRRP configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show router vrrp
```
