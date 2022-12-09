---
title: PTP Commands
author: Cumulus Networks
weight: 240
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> ptp

Interface Specific PTP configuration.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> ptp timers

Interface PTP timers

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> acceptable-master

Collection of acceptable masters

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor timestamp-log

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log

PTP violations log

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> monitor violations log acceptable-master

Collection of master violations

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  |  PTP instance number. It is used for management purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service ptp \<instance-id\> parent grandmaster-clock-quality

Clock Quality Status

### Command Syntax

| Syntax |  Description   |
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

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | PTP instance number. It is used for management  purpose. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
