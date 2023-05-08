---
title: Port Mirror
author: Cumulus Networks
weight: 290
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show system port-mirror</h>

Shows <span style="background-color:#F5F5DC">[SPAN](## "Switched Port Analyzer")</span> and <span style="background-color:#F5F5DC">[ERSPAN](## "Encapsulated Remote Switched Port Analyzer")</span> configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session</h>

Shows information about SPAN and ERSPAN sessions.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\></h>

Shows information about the specified port mirror session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan</h>

Shows information about the specified <span style="background-color:#F5F5DC">[ERSPAN](## "Encapsulated Remote Switched Port Analyzer")</span> session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` |  The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan destination</h>

Shows the destination ports for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The  port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan destination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan destination dest-ip</h>

Shows the destination IP addresses for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan destination dest-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\></h>

Shows information about the specified destination IP address for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number |
| `<dest-ip>` |  The destination IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan destination dest-ip 10.10.10.234
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan destination source-ip</h>

Shows the destination source IP addresses for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan destination source-ip
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\></h>

Shows information about the specified the destination source IP address for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number |
| `<source-ip>` | The source IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan destination source-ip 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan source-port</h>

Shows the source ports configured for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan source-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan source-port \<port-id\></h>

Shows information about the specified source port (swp or bond) for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>` |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan source-port swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> erspan truncate</h>

Shows information about truncating packets for the specified ERSPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 erspan truncate
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> span</h>

Shows configuration for the specified SPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 span
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> span destination</h>

Shows the destination ports for the specified SPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 span destination
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> span destination \<port-id\></h>

Shows information about the specified destination port for the specified SPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 span destination swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> span source-port</h>

Shows the source ports for the specified SPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 span source-port
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> span source-port \<port-id\></h>

Shows information about the specified source port (swp or bond) for the specified SPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number. |
| `<port-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 span source-port swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system port-mirror session \<session-id\> span truncate</h>

Shows information about truncating packets for the specified SPAN session.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<session-id>` | The port mirror session number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session 1 span truncate
```
