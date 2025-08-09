---
title: Adaptive Routing
author: Cumulus Networks
weight: 510

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router adaptive-routing enable</h>

Turns adaptive routing on the specified interface on or off. The default setting is `off`.

Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization.

- Adaptive routing does not make use of resilient hashing.
- Cumulus Linux does not support adaptive routing on layer 3 subinterfaces, SVIs, bonds or bond members.

{{%notice note%}}
- In cumulus Linux 5.12 and earlier, NVUE restarts `switchd` when applying the setting.
- In Cumulus Linux 5.13 and later, NVUE reloads `switchd` when applying the setting.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `interface-id` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 router adaptive-routing enable on
```
<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router adaptive-routing link-utilization-threshold</h>

Configures the link utilization threshold percentage at which adaptive routing considers the port congested. You can specify a value between 1 and 100. The default setting is `70`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `interface-id` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set interface swp1 router adaptive-routing link-utilization-threshold 50
```
-->

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing enable</h>

Turns adaptive routing on or off globally. The default setting is `off`.

Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization.

{{%notice note%}}
- In cumulus Linux 5.12 and earlier, NVUE restarts `switchd` when applying the setting.
- In Cumulus Linux 5.13 and later, NVUE reloads `switchd` when applying the setting.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing link-utilization-threshold</h>

Turns on link utilization. The default setting is `off`. When link utilization is on, the default link utilization threshold percentage for an adaptive routing interface is 70. If you enable the adaptive routing `custom-profile`, you can change the percentage to a value between 1 and 100.

Link utilization is off by default; you must enable the global link utilization setting to use the link utilization thresholds set on adaptive routing interfaces. You cannot enable or disable link utilization per interface.

{{%notice note%}}
- You can enable link utilization only when you enable the adaptive routing `custom-profile`.
- When you enable or disable link utilization, NVUE reloads `switchd`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing link-utilization-threshold on
```
