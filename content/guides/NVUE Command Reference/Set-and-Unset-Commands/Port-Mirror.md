---
title: Port Mirror
author: Cumulus Networks
weight: 660
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set system port-mirror

Configures Switched Port Analyzer (SPAN) and Encapsulated Remote Span (ERSPAN). SPAN enables you to mirror all packets that come in from or go out of an interface (the SPAN source), and copy and transmit the packets out of a local port or CPU (the SPAN destination) for monitoring. ERSPAN enables the mirrored packets to go to a monitoring node located anywhere across the routed network.

- - -

## nv set system port-mirror session \<session-id\>

Configures the port mirror session number, which is a number between 0 and 7.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set system port-mirror session \<session-id\> span

Configures SPAN, which enables you to mirror all packets that come in from or go out of an interface (the SPAN source), and copy and transmit the packets out of a local port or CPU (the SPAN destination) for monitoring.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number, which is a number between 0 and 7. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set system port-mirror session \<session-id\> span destination \<port-id\>

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
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span destination swp2
```

- - -

## nv set system port-mirror session \<session-id\> span direction

Configures the SPAN direction. You can specify ingress or egress.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span direction ingress
```

- - -

## nv set system port-mirror session \<session-id\> span enable

Turns port mirroring on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span enable on
```

- - -

## nv set system port-mirror session \<session-id\> span source-port \<port-id\>

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
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span source-port swp1
```

- - -

## nv set system port-mirror session \<session-id\> span truncate

Configures truncation to decrease bandwidth by reducing the size of monitored packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set system port-mirror session \<session-id\> span truncate enable

Turns truncation on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span truncate enable on
```

- - -

## nv set system port-mirror session \<session-id\> span truncate size

Configures the size in bytes at which to truncate mirrored frames. You can specify a value between 4 and 4088.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 span truncate size 40
```

- - -

## nv set system port-mirror session \<session-id\> erspan

Configures Encapsulated Remote Switched Port Analyzer (ERSPAN).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set system port-mirror session \<session-id\> erspan destination

Configures the ERSPAN destination.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\>

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
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan destination dest-ip 10.10.10.234
```

- - -

## nv set system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\>

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
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan destination source-ip 10.10.10.1
```

- - -

## nv set system port-mirror session \<session-id\> erspan direction

Configures the ERSPAN direction. You can specify ingress or egress.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 direction ingress
```

- - -

## nv set system port-mirror session \<session-id\> erspan enable

Turns ERSPAN on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan enable on
```

- - -

## nv set system port-mirror session \<session-id\> erspan source-port \<port-id\>

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
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan source-port swp1
```

- - -

## nv set system port-mirror session \<session-id\> erspan truncate

Configures truncation to decrease bandwidth by reducing the size of monitored packets.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set system port-mirror session \<session-id\> erspan truncate enable

Turns truncation on or off. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan truncate enable on
```

- - -

## nv set system port-mirror session \<session-id\> erspan truncate size

Configures the size in bytes at which to truncate mirrored frames. You can specify a value between 4 and 4088.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<session-id>` | The port mirror session number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system port-mirror session 1 erspan truncate size 4000
```

- - -
