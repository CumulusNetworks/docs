---
title: PPS
author: Cumulus Networks
weight: 665

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set platform pulse-per-second in channel-index</h>

Sets the channel index for PPS In. You can set a value of 1 or 0. The default value is 0.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in channel-index 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second in logging-level</h>

Sets the logging level for PPS In. You can specify emergency, alert, critical, error, warning, notice, info, or debug. The default logging level is info.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in logging-level warning
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second in pin-index</h>

Sets the pin index for PPS In. You can set a value of 1 or 0. The default value is 0.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in pin-index 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second in signal-polarity</h>

Sets the polarity of the PPS In signal. You can specify rising-edge, falling-edge, or both. The default setting is rising-edge.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in signal-polarity falling-edge
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second in signal-width</h>

Sets the pulse width of the PPS In signal. You can set a value between 1000000 and 999000000. The default value is 500000000.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in signal-width 999000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second in state</h>

Enables and disables PPS In.

{{%notice note%}}
When you configure and enable PPS In, you must configure a PTP slave port on the switch.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second in timestamp-correction</h>

Sets the value, in nanoseconds, to add to each PPS time stamp. You can set a value between -1000000000 and 1000000000. The default value is 0.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second in timestamp-correction 1000000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second out channel-index</h>

Sets the channel index for PPS Out. You can set a value of 1 or 0. The default value is 0.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second out channel-index 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second out frequency-adjustment</h>

Sets the frequency adjustment of the PPS Out signal. You can set a value between 1000000000 and 2147483647. The default value is 1000000000.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second out frequency-adjustment 2147483647
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second out phase-adjustment</h>

The NVUE CLI includes the `phase adjustment` setting for PPS Out. Cumulus Linux 5.7 does not support this setting.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second out pin-index</h>

Sets the pin index for PPS Out. Cumulus Linux supports only pin 1.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second out pin-index 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second out signal-width</h>

Sets the pulse width of the PPS Out signal. You can set a value between 1000000 and 999000000. The default value is 500000000.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second out signal-width 999000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform pulse-per-second state</h>

Enables and disables PPS Out.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set platform pulse-per-second out state enabled
```
