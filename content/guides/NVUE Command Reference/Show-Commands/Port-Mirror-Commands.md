---
title: Port Mirror Commands
author: Cumulus Networks
weight: 225
product: Cumulus Linux
type: nojsscroll
---
## nv show system port-mirror

Shows <span style="background-color:#F5F5DC">[SPAN](## "Switched Port Analyzer")</span> and <span style="background-color:#F5F5DC">[ERSPAN](## "Encapsulated Remote Switched Port Analyzer")</span> configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror
```

- - -

## nv show system port-mirror session

Shows information about SPAN and ERSPAN sessions.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system port-mirror session
```

- - -

## nv show system port-mirror session \<session-id\>

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

- - -

## nv show system port-mirror session \<session-id\> span

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

- - -

## nv show system port-mirror session \<session-id\> span source-port

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

- - -

## nv show system port-mirror session \<session-id\> span source-port \<port-id\>

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

- - -

## nv show system port-mirror session \<session-id\> span destination

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

- - -

## nv show system port-mirror session \<session-id\> span destination \<port-id\>

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

- - -

## nv show system port-mirror session \<session-id\> span truncate

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

- - -

## nv show system port-mirror session \<session-id\> erspan

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

- - -

## nv show system port-mirror session \<session-id\> erspan source-port

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

- - -

## nv show system port-mirror session \<session-id\> erspan source-port \<port-id\>

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

- - -

## nv show system port-mirror session \<session-id\> erspan destination

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

- - -

## nv show system port-mirror session \<session-id\> erspan destination source-ip

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

- - -

## nv show system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\>

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

- - -

## nv show system port-mirror session \<session-id\> erspan destination dest-ip

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

- - -

## nv show system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\>

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

- - -

## nv show system port-mirror session \<session-id\> erspan truncate

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
