---
title: VRR and VRRP
author: Cumulus Networks
weight: 800
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> ip vrr

Configures Virtual Router Redundancy (VRR) for an interface. VRR enables hosts to communicate with any redundant switch without reconfiguration by running dynamic router protocols or router redundancy protocols. Redundant switches respond to ARP requests from hosts. The switches respond in an identical manner, but if one fails, the other redundant switches continue to respond. You use VRR with MLAG.

- - -

## nv set interface \<interface-id\> ip vrr address \<ip-prefix-id\>

Configures the virtual address and prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr address 10.1.10.1/24 
```

- - -

## nv set interface \<interface-id\> ip vrr enable

Turns VRR on or off on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr enable on 
```

- - -

## nv set interface \<interface-id\> ip vrr mac-address \<mac-address\>

Configures anycast MAC override on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<mac-address>` | The anycast MAC address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr mac-address 00:00:5E:00:01:00
```

- - -

## nv set interface \<interface-id\> ip vrr mac-id \<fabric-id\>

Configures the fabric ID override on the interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<fabric-id>` | The fabric ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr mac-id 1
```

- - -

## nv set interface \<interface-id\> ip vrr state

Configures the state of the interface: up or down. The default setting is `down`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface vlan10 ip vrr state up 
```

- - -

## nv set router vrr

Configures VRR globally on the switch.

- - -

## nv set router vrr enable

Turns VRR on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrr enable on
```

- - -

## nv set interface \<interface-id\> ip vrrp

Configures the Virtual Router Redundancy Protocol (VRRP) on the interface.

- - -

## nv set interface \<interface-id\> ip vrrp enable

Turns on VRRP on the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp enable on
```

- - -

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\>

Configures the group of virtual gateways implemented with VRRP.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\>

Configures a virtual address for VRRPv3.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |
| `<ip-address-id>` |  The IPv4 or IPv6 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

- - -

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> advertisement-interval

Configures the interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950 milliseconds. The default setting is 1000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 advertisement-interval 2000
```

- - -

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> preempt

Configures preempt mode, which lets the router take over as master for a virtual router group if it has a higher priority than the current master. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 preempt off
```

- - -

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> priority

Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. The default setting is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 priority 254
```

- - -

## nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> version

Configures the VRRP protocol version for the interface. You can specify a value of 2 or 3. The default setting is 3.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

- - -

## nv set router vrrp

Configures VRRP globally on the switch.

- - -

## nv set router vrrp advertisement-interval

Configures the advertisement interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950. The default setting is 1000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp advertisement-interval 2000
```

- - -

## nv set router vrrp enable

Turns VRRP on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp enable on
```

- - -

## nv set router vrrp preempt

Configures the router to take over as master for a virtual router group if it has a higher priority than the current master. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp preempt off
```

- - -

## nv set router vrrp priority

Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. The default setting is 100.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router vrrp priority 254
```

- - -
