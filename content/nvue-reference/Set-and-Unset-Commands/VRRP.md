---
title: VRRP
author: Cumulus Networks
weight: 805

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> ip vrrp</h>

Configures the <span class="a-tooltip">[VRRP](## "Virtual Router Redundancy Protocol")</span> on the interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp enable</h>

Turns VRRP on or off for the interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface swp1 ip vrrp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\></h>

Configures the group of virtual gateways used with VRRP.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<virtual-router-id>` |  The Virtual Router Syntax (VRID). |

### Version History

Introduced in Cumulus Linux 5.0.0

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> address \<ip-address-id\></h>

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
cumulus@switch:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> advertisement-interval</h>

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
cumulus@switch:~$ nv set interface swp1 ip vrrp virtual-router 44 advertisement-interval 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> preempt</h>

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
cumulus@switch:~$ nv set interface swp1 ip vrrp virtual-router 44 preempt off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> priority</h>

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
cumulus@switch:~$ nv set interface swp1 ip vrrp virtual-router 44 priority 254
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ip vrrp virtual-router \<virtual-router-id\> version</h>

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
cumulus@switch:~$ nv set interface swp1 ip vrrp virtual-router 44 address 10.0.0.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router vrrp</h>

Configures VRRP globally on the switch.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router vrrp advertisement-interval</h>

Configures the advertisement interval between successive advertisements by the master in a virtual router group. You can specify a value between 10 and 40950. The default setting is 1000 milliseconds.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router vrrp advertisement-interval 2000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router vrrp enable</h>

Turns VRRP on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router vrrp enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router vrrp preempt</h>

Configures the router to take over as master for a virtual router group if it has a higher priority than the current master. The default setting is `on`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router vrrp preempt off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router vrrp priority</h>

Configures the priority level of the virtual router within the virtual router group, which determines the role that each virtual router plays and what happens if the master fails. Virtual routers have a priority between 1 and 254; the router with the highest priority becomes the master. The default setting is 100.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set router vrrp priority 254
```
