---
title: Interface Address Commands
author: Cumulus Networks
weight: 190
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ip

Shows IP address configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip
```

- - -

## nv show interface \<interface-id\> ip address \<ip-prefix-id\>

Shows details about the specified IP address for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<ip-prefix-id>`  | The IPv4 or IPv6 address and route prefix in CIDR notation.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp1 ip address 10.10.10.1/32
```

- - -

## nv show interface \<interface-id\> ip neighbor

Shows information about the IP neighbors configured for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 ip neighbor
```

- - -

## nv show interface \<interface-id\> ip neighbor ipv4 \<neighbor-id\>

Shows information about the specified IPv4 neighbor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<neighbor-id>`  | The IPv4 address of the neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 ip neighbor ipv4 169.254.0.1
```

- - -

## nv show interface \<interface-id\> ip neighbor ipv6 \<neighbor-id\>

Shows information about the specified IPv6 neighbor for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|
| `<neighbor-id>`  | The IPv4 address of the neighbor.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show interface swp51 ip neighbor ipv6 2001:db8:0002::0a00:0002
```

- - -

## nv show vrf \<vrf-id\> loopback

Shows the loopback interfaces associated with this VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default loopback
```

- - -

## nv show vrf \<vrf-id\> loopback ip

Shows the IP addresses associated with the loopback interface for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default loopback ip
```

- - -

## nv show vrf \<vrf-id\> loopback ip address \<ip-prefix-id\>

Shows details about the specified loopback IP address for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default loopback ip address 10.10.10.1/32
```
