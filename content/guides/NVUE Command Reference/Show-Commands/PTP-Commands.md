---
title: PTP Commands
author: Cumulus Networks
weight: 240
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ptp

Interface Specific PTP configuration.

### Usage

`nv show interface <interface-id> ptp [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers`  |  Interface PTP timers |
| `counters`  |  Interface PTP counters |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ptp timers

Interface PTP timers

### Usage

`nv show interface <interface-id> ptp timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ptp counters

Interface PTP counters

### Usage

`nv show interface <interface-id> ptp counters [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp

Collection of PTP instances

### Usage

`nv show service ptp [options] [<instance-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\>

Global PTP configuration.

### Usage

`nv show service ptp <instance-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `acceptable-master`     | Collection of acceptable masters |
| `monitor`               | PTP monitor configuration |
| `current`               | Local states learned from the exchange of PTP messages |
| `clock-quality`         | Clock Quality Status |
| `parent`                | Local states learned from the exchange of PTP messages |
| `time-properties`       | Time attributes of the clock |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> acceptable-master

Collection of acceptable masters

### Usage

`nv show service ptp <instance-id> acceptable-master [options] [<clock-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |
| `<clock-id>`  |  Clock ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> acceptable-master <clock-id>

List of clocks that the local clock can accept as master clock

### Usage

`nv show service ptp <instance-id> acceptable-master <clock-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |
| `<clock-id>`  |  Clock ID |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor

PTP monitor configuration

### Usage

`nv show service ptp <instance-id> monitor [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timestamp-log`  | Collection of violations logs |
| `violations`     | PTP violations |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor timestamp-log

### Usage

`nv show service ptp <instance-id> monitor timestamp-log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations

PTP violations

### Usage

`nv show service ptp <instance-id> monitor violations [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `log` |  PTP violations log |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log

PTP violations log

### Usage

`nv show service ptp <instance-id> monitor violations log [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `acceptable-master`     | Collection of master violations |
| `forced-master`         | Collection of master violations |
| `max-offset`            | Collection of violations logs |
| `min-offset`            | Collection of violations logs |
| `path-delay`            | Collection of violations logs |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log acceptable-master

Collection of master violations

### Usage

`nv show service ptp <instance-id> monitor violations log acceptable-master [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log forced-master

Collection of master violations

### Usage

`nv show service ptp <instance-id> monitor violations log forced-master [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log max-offset

Collection of violations logs

### Usage

`nv show service ptp <instance-id> monitor violations log max-offset [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log min-offset

Collection of violations logs

### Usage

`nv show service ptp <instance-id> monitor violations log min-offset [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log path-delay

Collection of violations logs

### Usage

`nv show service ptp <instance-id> monitor violations log path-delay [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> current

Local states learned from the exchange of PTP messages

### Usage

`nv show service ptp <instance-id> current [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> clock-quality

Clock Quality Status

### Usage

`nv show service ptp <instance-id> clock-quality [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> parent

Local states learned from the exchange of PTP messages 

### Usage

`nv show service ptp <instance-id> parent [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
|`grandmaster-clock-quality` | Clock Quality Status |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> parent grandmaster-clock-quality

Clock Quality Status

### Usage

`nv show service ptp <instance-id> parent grandmaster-clock-quality [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> time-properties

Time attributes of the clock

### Usage

`nv show service ptp <instance-id> time-properties [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<instance-id>` | PTP instance number. It is used for management  purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
