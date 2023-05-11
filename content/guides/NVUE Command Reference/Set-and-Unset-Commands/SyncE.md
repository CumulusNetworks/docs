---
title: SyncE
author: Cumulus Networks
weight: 745
product: Cumulus Linux
type: nojsscroll
draft: true
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set interface \<interface-id\> synce</h>

Configures Synce on the specified interface.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set interface \<interface-id\> synce enable</h>

Turns SyncE on or off on the specified interface. The default setting is `off`.

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

Configures the frequency source priority for the interface. The clock selection algorithm uses the frequency source priority to choose between two sources that have the same QL. You can specify a value between 1 (the highest priority) and 254 (the lowest priority). The default value is 100.

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

## <h>nv set service synce</h>

Configures the SyncE service (`synced.service`).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service synce enable</h>

Turns the SyncE service on or off. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set service synce enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service synce log-level</h>

Configures the logging level that the SyncE service uses. You can set the following values:
- `critical` level logs critical errors and notices.
- `debug` level logs fine-grained informational events that are most useful to debug an application.
- `error` level logs errors.
- `info` level logs informational messages.
- `notice` level logs notices.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set service synce log-level debug
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service synce provider-default-priority</h>

Configures the priority for the clock source. You can set a value between 1 and 256. The lowest priority is 1 and the highest priority is 256. If two clock sources has the same priority, the switch uses the lowest clock source.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set service synce provider-default-priority 256
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service synce wait-to-restore-time</h>

Configures the number of seconds SyncE waits for each port to be up before opening the Ethernet Synchronization Message Channel (ESMC) for messages. You can set a value between 0 and 720 (12) minutes. The default value is 300 seconds (5 minutes).

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set service synce wait-to-restore-time 180
```
