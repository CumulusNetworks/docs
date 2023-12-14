---
title: Port Mirror
author: Cumulus Networks
weight: 660

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system port-mirror</h>

Configures <span class="a-tooltip">[SPAN](## "Switched Port Analyzer")</span> and <span class="a-tooltip">[ERSPAN](## "Encapsulated Remote Span")</span>.
- SPAN enables you to mirror all packets that come in from or go out of an interface (the SPAN source), and copy and transmit the packets out of a local port or CPU (the SPAN destination) for monitoring.
- ERSPAN enables the mirrored packets to go to a monitoring node located anywhere across the routed network.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\></h>

Configures the port mirror session number, which is a number between 0 and 7.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span</h>

Configures SPAN, which enables you to mirror all packets that come in from or go out of an interface (the SPAN source), and copy and transmit the packets out of a local port or CPU (the SPAN destination) for monitoring.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span destination \<port-id\></h>

Configures the SPAN destination port.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>`  |  The interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 span destination swp2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span direction</h>

Configures the SPAN direction. You can specify ingress or egress.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 span direction ingress
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span enable</h>

Turns port mirroring on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 span enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span source-port \<port-id\></h>

Configures the port mirror source port (switch ports or bonds only).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>`  |  The interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 span source-port swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span truncate</h>

Configures truncation to decrease bandwidth by reducing the size of monitored packets.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span truncate enable</h>

Turns truncation on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 span truncate enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> span truncate size</h>

Configures the size in bytes at which to truncate mirrored frames. You can specify a value between 4 and 4088.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 span truncate size 40
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan</h>

Configures Encapsulated Remote Switched Port Analyzer (ERSPAN).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan destination</h>

Configures the ERSPAN destination.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\></h>

Configures the destination IP address to which you want to transmit packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<dest-ip>` | The destination IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\></h>

Configures the source IP address from where to copy packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<source-ip>` | The source IP address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan direction</h>

Configures the ERSPAN direction. You can specify ingress or egress.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 direction ingress
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan enable</h>

Turns ERSPAN on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan source-port \<port-id\></h>

Configures the ERSPAN source port (switch ports or bonds only).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>`   |  The interface. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan source-port swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan truncate</h>

Configures truncation to decrease bandwidth by reducing the size of monitored packets.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan truncate enable</h>

Turns truncation on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan truncate enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system port-mirror session \<session-id\> erspan truncate size</h>

Configures the size in bytes at which to truncate mirrored frames. You can specify a value between 4 and 4088.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system port-mirror session 1 erspan truncate size 4000
```
