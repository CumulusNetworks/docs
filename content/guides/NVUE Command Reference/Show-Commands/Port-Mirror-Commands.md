---
title: Port Mirror Commands
author: Cumulus Networks
weight: 235
product: Cumulus Linux
type: nojsscroll
---
## nv show system port-mirror

Port mirror

### Usage

`nv show system port-mirror [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `session` |   sessions |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session

sessions

### Usage

`nv show system port-mirror session [options] [<session-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>`  |port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\>

port mirror session number

### Usage

`nv show system port-mirror session <session-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `span` | Switched Port Analyzer |
| `erspan` |  Encapsulated Remote Switched Port Analyzer.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> span

Switched Port Analyzer

### Usage

`nv show system port-mirror session <session-id> span [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |   port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port` | Set of source ports.|
| `destination` |  The SPAN destination port.|
| `truncate` |  TBD|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> span source-port

Set of source ports.

### Usage

`nv show system port-mirror session <session-id> span source-port [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> span source-port \<port-id\>

A port-mirror source port (swps or bonds only)

### Usage

`nv show system port-mirror session <session-id> span source-port <port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> span destination

The SPAN destination port.

### Usage

`nv show system port-mirror session <session-id> span destination [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> span destination \<port-id\>

The SPAN destination port.

### Usage

`nv show system port-mirror session <session-id> span destination <port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` | Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> span truncate

TBD

### Usage

`nv show system port-mirror session <session-id> span truncate [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan

Encapsulated Remote Switched Port Analyzer.

### Usage

`nv show system port-mirror session <session-id> erspan [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-port` |   Set of source ports. |
| `destination` |   erspan destination |
| `truncate` |   TBD|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan source-port

Set of source ports.

### Usage

`nv show system port-mirror session <session-id> erspan source-port [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` |   Port interface` |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan source-port \<port-id\>

A port-mirror source port (swps or bonds only)

### Usage

`nv show system port-mirror session <session-id> erspan source-port <port-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<port-id>` |   Port interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan destination

erspan destination

### Usage

`nv show system port-mirror session <session-id> erspan destination [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `source-ip` | TBD |
| `dest-ip` |   TBD |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan destination source-ip

Set of IPv4 addresses

### Usage

`nv show system port-mirror session <session-id> erspan destination source-ip [options] [<source-ip> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<source-ip>` | IPv4 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan destination source-ip \<source-ip\>

An IPv4 address

### Usage

`nv show system port-mirror session <session-id> erspan destination source-ip <source-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan destination dest-ip

Set of IPv4 addresses

### Usage

`nv show system port-mirror session <session-id> erspan destination dest-ip [options] [<dest-ip> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |
| `<dest-ip>` |  IPv4 address |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan destination dest-ip \<dest-ip\>

An IPv4 address

### Usage

`nv show system port-mirror session <session-id> erspan destination dest-ip <dest-ip> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show system port-mirror session \<session-id\> erspan truncate

TBD

### Usage

`nv show system port-mirror session <session-id> erspan truncate [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<session-id>` |  port mirror session number |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
