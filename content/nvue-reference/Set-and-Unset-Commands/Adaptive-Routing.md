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

## <h>nv set interface \<interface-id\> router adaptive-routing</h>

Provides commands to configure adaptive routing on the specified interface. Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization.

{{%notice note%}}
Cumulus Linux 5.6 supports adaptive routing on Spectrum-4.
Cumulus Linux 5.5 and earlier supports adaptive routing on Spectrum-3 and Spectrum-2 as a beta feature for evaluation.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router adaptive-routing enable</h>

Turns adaptive routing on the specified interface on or off. The default setting is `off`.

- Adaptive routing does not make use of resilient hashing.
- Cumulus Linux does not support adaptive routing on layer 3 subinterfaces, SVIs, bonds or bond members.

{{%notice note%}}
NVUE must restart `switchd` to apply the setting.
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

## <h>nv set router adaptive-routing</h>

Provides commands to configure adaptive routing globally on the switch. Adaptive routing is a load balancing feature that improves network utilization for eligible IP packets by selecting forwarding paths dynamically based on the state of the switch, such as queue occupancy and port utilization.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing enable</h>

Turns adaptive routing on or off globally. The default setting is `off`.

{{%notice note%}}
NVUE restarts `switchd` to apply the setting.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing enable on
```
<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing link-utilization-threshold</h>

Turns on link utilization. The default setting is `off`. When link utilization is on, the default link utilization threshold percentage for an adaptive routing interface is 70. YOu can change the threshold percentage with the `nv set interface <interface-id> router adaptive-routing link-utilization-threshold` command.

When you enable or disable link utilization, NVUE reloads `switchd`.

{{%notice note%}}
In Cumulus Linux 5.5 and earlier, link utilization is `on` by default. If you configured link utilization in a previous release, be sure to enable link utilization after you upgrade to Cumulus Linux 5.6.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing link-utilization-threshold on
```
-->