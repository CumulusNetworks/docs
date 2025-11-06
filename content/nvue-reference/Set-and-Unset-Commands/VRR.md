---
title: VRR
author: Cumulus Networks
weight: 800

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 vrr address \<ip-prefix-id\></h>

Configures the VRR virtual address and prefix. For IPv6, run the `nv set interface <interface-id> ipv6 vrr address` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv set interface <interface-id> ip vrr address`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface vlan10 ipv4 vrr address 10.1.10.1/24 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 vrr state</h>

Enables and disables VRR on the interface. The default setting is `disabled`.

Virtual Router Redundancy (VRR) enables hosts to communicate with any redundant switch without reconfiguration by running dynamic router protocols or router redundancy protocols. Redundant switches respond to ARP requests from hosts. The switches respond in an identical manner, but if one fails, the other redundant switches continue to respond. You use VRR with MLAG.

For IPv6, run the `nv set interface <interface-id> ipv6 vrr state` command.

{{%notice note%}}
- In Cumulus Linux 5.14 and earlier, the command is `nv set interface <interface-id> ip vrr state`.
- In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface vlan10 ipv4 vrr state enabled 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 vrr mac-address \<mac-address\></h>

Configures anycast MAC override on the interface. For IPv6, run the `nv set interface <interface-id> ipv6 vrr mac-address <mac-address>` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv set interface <interface-id> ip vrr mac-address`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<mac-address>` | The anycast MAC address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface vlan10 ipv4 vrr mac-address 00:00:5E:00:01:00
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 vrr mac-id \<fabric-id\></h>

Configures the fabric ID override on the interface. For IPv6, run the `nv set interface <interface-id> ipv6 vrr mac-id <fabric-id>` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv set interface <interface-id> ip vrr mac-id`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<fabric-id>` | The fabric ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface vlan10 ipv4 vrr mac-id 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> ipv4 vrr vrr-state</h>

Configures the state of the interface: `up` or `down`. The default setting is `down`. For IPv6, run the `nv set interface <interface-id> ipv6 vrr vrr-state` command.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, the command is `nv set interface <interface-id> ip vr vrr-state`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set interface vlan10 ipv4 vrr vrr-state up 
```
