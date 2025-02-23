---
title: SyncE
author: Cumulus Networks
weight: 745

type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> synce bundle-id</h>

Configures the SyncE bundle that this interface belongs to. You can specify a value between 0 and 256. A value of zero indicates no bundle.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface on which you want to configure SyncE. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set interface swp1 synce bundle-id 0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> synce enable</h>

Turns <span class="a-tooltip">[SynCe](## "Synchronous Ethernet")</span> on or off on the specified interface. The default setting is `off`.

SyncE is a standard for transmitting clock signals over the Ethernet physical layer to synchronize clocks across the network by propagating frequency using the transmission rate of symbols in the network. A dedicated Ethernet channel, (ESMC), manages this synchronization.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface on which you want to configure SyncE. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set interface swp1 synce enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> synce provider-priority</h>

Configures the frequency source priority for the interface. The clock selection algorithm uses the frequency source priority to choose between two sources that have the same <span class="a-tooltip">[QL](## "Quality Level")</span>. You can specify a value between 1 (the highest priority) and 254 (the lowest priority). The default value is 100.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
|`<interface-id>` | The interface on which you want to configure the frequency source priority. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set interface swp1 synce provider-priority 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system synce enable</h>

Turns the SyncE service on or off. The default setting is `off`.

The SyncE service (`synced.service`) manages:
- Transmitting and receiving <span class="a-tooltip">[SSMs](## "Synchronization Status Messages")</span> on all SyncE enabled ports using the <span class="a-tooltip">[ESMC](## "Ethernet Synchronization Messaging Channel")</span>.
- The synchronization hierarchy and runs the master selection algorithm to choose the best reference clock from the QL in the SSM.
- Using to the next best clock when the master clock fails. The selection algorithm only selects the best source, which is the Primary Clock source.
- The switchover time if the algorithm also selects a secondary reference clock in case of primary failure.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system synce enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system synce log-level</h>

Configures the logging level that the SyncE service uses. You can set the following values:
- `critical` level logs critical errors and notices.
- `debug` logs fine-grained informational events that are most useful to debug an application.
- `error` logs errors.
- `info` logs informational messages.
- `notice` logs notices.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system synce log-level debug
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system synce min-acceptable-ql</h>

Configures SyncE to not track a source with a quality level lower than a specific value. The quality level can be: `eec1`, `eeec`, `ssu-b`, `ssu-a`, `prc`, `eprc`, `prtc`, or `eprtc`, where `eec1` is the lowest quality level and `eprtc` is the highest quality level.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system synce min-acceptable-ql ssu-b
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system synce provider-default-priority</h>

Configures the priority for the clock source. You can set a value between 1 and 256. The lowest priority is 1 and the highest priority is 256. If two clock sources has the same priority, the switch uses the lowest clock source.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system synce provider-default-priority 256
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system synce wait-to-restore-time</h>

Configures the number of seconds SyncE waits for each port to be up before opening the <span class="a-tooltip">[ESMC](## "Ethernet Synchronization Message Channel")</span> for messages. You can set a value between 0 and 720 seconds (12 minutes). The default value is 300 seconds (5 minutes).

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system synce wait-to-restore-time 180
```
