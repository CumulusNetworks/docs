---
title: Packet Trimming
author: Cumulus Networks
weight: 635

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> packet-trim egress-eligibility traffic-class \<tc-id\></h>

Configures the port eligibility by setting the egress port and traffic class from which to trim and recirculate dropped traffic. You can only configure physical ports; if we want to trim packets egressing bonds, specify the bond slave ports. You can specify a traffic class value between 0 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>`  |  The name of the interfaces. |
| `<tc-id>`  |  The traffic class. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set interface swp1-32 packet-trim egress-eligibility traffic-class 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim profile packet-trim-default</h>

Configures packet trimming to use the default profile called `packet-trim-default`.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim packet-trim-default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim remark dscp</h>

Configures the DSCP value you want to mark on trimmed packets. You can specify a value between 0 and 63 or `port-level` for port level packet trimming.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim remark dscp 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim service-port \<port-id\></h>

Configures the service port to use for packet trimming.

When you enable packet trimming, one service port is used. By default, this is the last service port on the switch. You can change the service port you want to use.

On a switch that supports two service ports, you can configure a bond on the service ports, then use the bond for the packet trimming service port.

{{%notice note%}}
Do not configure packet trimming port eligibility, port security, adaptive routing, QoS, ACLs, PTP, VRR, PBR, telemetry, or histograms on the packet trimming service port.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-id>`  |  The service port you want to use for packet trimming.  |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim service-port bond1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim size</h>

Configures the maximum size of the trimmed packet in bytes. You can specify a value between 256 and 1024; the value must be a multiple of 4. If the packet is smaller than the trimming size, the switch does not trim the packet but forwards the packet based on the configured switch priority for trim-eligible packets.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim size 528
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim state</h>

Enables and disables packet trimming. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim switch-priority</h>

Configures the switch priority of the trimmed packet. You can specify a value between 0 and 7. The traffic class of the trimmed packet is internally derived from the switch priority.

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim switch-priority 2
```
