---
title: Packet Trimming
author: Cumulus Networks
weight: 790

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

## <h>nv set interface \<interface-id\> packet-trim notify-sender tail-drop egress-eligibility traffic-class \<tc-id\></h>

Configures a traffic class that is eligible for tail drop sender notification on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<tc-id>` |  The traffic class. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set interface swp1 packet-trim notify-sender tail-drop egress-eligibility traffic-class 3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> packet-trim spxm notify-sender link-down ingress-eligibility dscp \<dscp-id\></h>

Configures a DSCP value that is eligible for link-down sender notification on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<dscp-id>` |  The DSCP value. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set interface swp1 packet-trim spxm notify-sender link-down ingress-eligibility dscp 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim ingress-eligibility dscp</h>

Configures the DSCP values whose traffic is eligible for packet trimming. The switch keeps one device-wide list that both trim directions share. You can specify a value between 0 and 63. When you do not set this option, every DSCP value is eligible. A list with any entries also makes non-IP packets ineligible in both directions; leaving the list unset is the only way to keep them eligible.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim ingress-eligibility dscp 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim ingress-eligibility interface</h>

Configures the ingress ports on which the DSCP eligibility list applies, as a range or a list. On a broken-out port, specify the child ports, such as swp1s0, instead of the port. When you do not set this option, the list follows whichever ports the switch has at each apply. A list you configure contains exactly the ports you name, less service ports and ports that are not present, and setting it again replaces the previous list.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim ingress-eligibility interface swp1-4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim notify-sender link-down remark dscp</h>

Configures the DSCP value that the switch marks on trimmed packets it notifies back to the sender of a link-down drop. You can specify a value between 0 and 63, or `port-level` to mark each packet with the DSCP value configured on its ingress port.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down remark dscp 8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim notify-sender link-down service-port</h>

Configures the service port that the switch uses to recirculate link-down packets. You can specify swp65s0, swp65s1, or a bond whose members are only those ports. The default setting is `swp65s0`.

{{%notice note%}}
This setting requires an NVIDIA Spectrum-6 switch.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down service-port swp65s1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim notify-sender link-down size</h>

Configures the trimmed packet size, in bytes, for link-down sender notification. You can specify a value between 256 and 1024 that is a multiple of four. The default value is 256.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down size 512
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim notify-sender link-down state</h>

Enables and disables link-down sender notification for packet trimming. You can set a value of `enabled`, or `disabled`. The default setting is `disabled`.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim notify-sender link-down switch-priority</h>

Configures the switch priority for the trimmed packets that the switch sends as link-down notifications. You can specify a value between 0 and 7. The default value is 4.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender link-down switch-priority 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system forwarding packet-trim notify-sender tail-drop remark dscp</h>

Configures the DSCP value that the switch marks on trimmed packets it notifies back to the sender of a tail drop. You can specify a value between 0 and 63, or `port-level` to mark each packet with the DSCP value configured on its ingress port. This setting is independent of the trim and forward marking, which the `remark dscp` option on the shared packet-trim parent controls.

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system forwarding packet-trim notify-sender tail-drop remark dscp 8
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
