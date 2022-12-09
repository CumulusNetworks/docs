---
title: QoS Commands
author: Cumulus Networks
weight: 260
product: Cumulus Linux
type: nojsscroll
---
## nv show interface \<interface-id\> qos

### Usage

`nv show interface <interface-id> qos [options] [<attribute> ...]

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `counters` | |
| `roce` | |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> qos counters

Interface QoS counters

### Usage

`nv show interface <interface-id> qos counters [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `port-stats`            | `QoS Statistics for Interface`
| `egress-queue-stats`    | `Egress queue statistics per egress traffic-class`
| `ingress-buffer-stats`  | `Ingress Buffer statistics per priority-group`
| `pfc-stats`             | `PFC statistics per internal switch-priority`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> qos counters port-stats

QoS Statistics for Interface

### Usage

`nv show interface <interface-id> qos counters port-stats [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `rx-stats`   | QoS Rx Statistics for Interface |
| `tx-stats` |  QoS Tx Statistics for Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> qos counters port-stats rx-stats

QoS Rx Statistics for Interface

### Usage

`nv show interface <interface-id> qos counters port-stats rx-stats [options]`

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

## nv show interface \<interface-id\> qos counters port-stats tx-stats

QoS Tx Statistics for Interface

### Usage

`nv show interface <interface-id> qos counters port-stats tx-stats [options]`

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

## nv show interface \<interface-id\> qos counters egress-queue-stats

Egress queue statistics per egress traffic-class

### Usage

`nv show interface <interface-id> qos counters egress-queue-stats [options]`

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

## nv show interface \<interface-id\> qos counters ingress-buffer-stats

Ingress Buffer statistics per priority-group

### Usage

`nv show interface <interface-id> qos counters ingress-buffer-stats [options]`

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

## nv show interface \<interface-id\> qos counters pfc-stats

PFC statistics per internal switch-priority

### Usage

`nv show interface <interface-id> qos counters pfc-stats [options]`

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

## nv show interface \<interface-id\> qos roce

### Usage

`nv show interface <interface-id> qos roce [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `counters` | |
| `status` | |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> qos roce counters

Interface roce counters

### Usage

`nv show interface <interface-id> qos roce counters [options]`

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

## nv show interface \<interface-id\> qos roce status

Interface status

### Usage

`nv show interface <interface-id> qos roce status [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `pool-map`   |  Interface Roce pools|
| `prio-map`  |  RoCE PCP/DSCP->SP mapping configurations|
| `tc-map  | RoCE SP->TC mapping and ETS configurations|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> qos roce status pool-map

Interface Roce pools

### Usage

`nv show interface <interface-id> qos roce status pool-map [options]`

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

## nv show interface \<interface-id\> qos roce status prio-map

RoCE PCP/DSCP->SP mapping configurations

### Usage

`nv show interface <interface-id> qos roce status prio-map [options]`

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

## nv show interface \<interface-id\> qos roce status tc-map

RoCE SP->TC mapping and ETS configurations

### Usage

`nv show interface <interface-id> qos roce status tc-map [options]`

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
