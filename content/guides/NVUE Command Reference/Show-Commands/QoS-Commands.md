---
title: QoS Commands
author: Cumulus Networks
weight: 260
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> qos

Shows QoS configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos
```

- - -

## nv show interface \<interface-id\> qos counter

Shows the QoS counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter
```

- - -

## nv show interface \<interface-id\> qos counter port-stats

Shows QoS port statistics for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter port-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats rx-stats

Shows QoS statistics for received packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter port-stats rx-stats
```

- - -

## nv show interface \<interface-id\> qos counter port-stats tx-stats

Shows QoS statistics for transmitted packets on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter port-stats tx-stats
```

- - -

## nv show interface \<interface-id\> qos counter egress-queue-stats

Shows egress queue statistics per egress traffic class for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter egress-queue-stats
```

- - -

## nv show interface \<interface-id\> qos counter ingress-buffer-stats

Shows ingress buffer statistics per priority group for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter ingress-buffer-stats
```

- - -

## nv show interface \<interface-id\> qos counter pfc-stats

Shows PFC statistics per internal switch priority for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos counter pfc-stats
```

- - -

## nv show interface \<interface-id\> qos roce

Shows a summary of RoCE information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos roce
```

- - -

## nv show interface \<interface-id\> qos roce counters

Shows RoCE counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos roce counters
```

- - -

## nv show interface \<interface-id\> qos roce status

Shows RoCE status information for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos roce status
```

- - -

## nv show interface \<interface-id\> qos roce status pool-map

Shows ingress and egress service pool configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos roce pool-map
```

- - -

## nv show interface \<interface-id\> qos roce status prio-map

Shows the RoCE PCP or DSCP to switch priority mapping configuration for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos roce prio-map
```

- - -

## nv show interface \<interface-id\> qos roce status tc-map

 Shows the RoCE switch priority to traffic class mapping and ETS configurations for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp5 qos roce status tc-map
```
