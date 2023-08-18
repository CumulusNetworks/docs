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

Provides commands to configure adaptive routing on the specified interface. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> router adaptive-routing enable</h>

Turns adaptive routing on the specified interface on or off. The default setting is `off`.

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing</h>

Provides commands to configure adaptive routing globally on the switch. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing enable</h>

Turns adaptive routing on or off globally. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing link-utilization-threshold</h>

Turns on link utilization. The default setting is off. When link utilization is on, the default link utilization threshold percentage for an adaptive routing interface is 70. YOu can change the threshold percentage with the `nv set interface <interface> router adaptive-routing link-utilization-threshold` command.

When you enable or disable link utilization, NVUE reloads switchd.

{{%notice note%}}
In Cumulus Linux 5.5 and earlier, link utilization is on by default. If you configured link utilization in a previous release, be sure to enable link utilization after you upgrade to Cumulus Linux 5.6.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing link-utilization-threshold on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router adaptive-routing profile</h>

Applies the adaptive routing profile you want to use. Cumulus Linux provides these adaptive routing profiles:
- `ar-profile-1` is the default profile for a switch with the Spectrum-2 and Spectrum-3 ASIC.
- `ar-profile-2` is the default profile for a switch with the Spectrum-4 ASIC.
- `ar-profile-custom` includes adaptive routing settings you can change.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set router adaptive-routing profile ar-profile-custom
```
