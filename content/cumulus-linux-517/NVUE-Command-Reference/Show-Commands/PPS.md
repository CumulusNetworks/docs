---
title: PPS
author: Cumulus Networks
weight: 295

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform pulse-per-second</h>

Shows a summary of the PPS In and PPS Out configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show platform pulse-per-second
                        applied
----------------------  -----------
in
  state                 enabled
  pin-index             0
  channel-index         0
  signal-width          500000000
  signal-polarity       rising-edge
  timestamp-correction  0
  logging-level         info
out
  state                 disabled
  pin-index             1
  channel-index         0
  frequency-adjustment  1000000000
  phase-adjustment      0
  signal-width          500000000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform pulse-per-second in</h>

Shows a summary of the PPS In configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show platform pulse-per-second in
                      applied
--------------------  -----------
state                 enabled
pin-index             0
channel-index         0
signal-width          500000000
signal-polarity       rising-edge
timestamp-correction  0
logging-level         info
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform pulse-per-second out</h>

Shows a summary of the PPS Out configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show platform pulse-per-second out
                      applied
--------------------  ----------
state                 disabled
pin-index             1
channel-index         0
frequency-adjustment  1000000000
phase-adjustment      0
signal-width          500000000
```
