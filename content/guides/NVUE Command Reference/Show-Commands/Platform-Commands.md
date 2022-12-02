---
title: Platform Commands
author: Cumulus Networks
weight: 150
product: Cumulus Linux
type: nojsscroll
---
## nv show platform

Top-level container for the components in the system. This node represents a system component inventory, which includes hardware and software elements.

### Usage

`nv show platform [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `capabilities` |  Capabilities of this platform |
| `hardware`   | The platform's hardware |
| `environment` |   Platform environment information |
| `software` |    The platform's software |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform capabilities

Capabilities of this platform

### Usage

`nv show platform capabilities [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware

The platform's hardware

### Usage

`nv show platform hardware [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `component` | Set of components making up the platform. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component

Set of components making up the platform.

### Usage

`nv show platform hardware component [options] [<component-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\>

A component in the platform.

### Usage

`nv show platform hardware component <component-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `linecard` | Properties of a linecard component |
| `port` |   Set of physical ports on this component |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> linecard

Properties of a linecard component

### Usage

`nv show platform hardware component <component-id> linecard [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port

Set of physical ports on this component

### Usage

`nv show platform hardware component <component-id> port [options] [<port-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` |  Physical port identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port \<port-id\>

A physical port on the component.

### Usage

`nv show platform hardware component <component-id> port <port-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` |  Physical port identifier |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `breakout-mode` | Set of breakout modes supported by this port |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port \<port-id\> breakout-mode

Set of breakout modes

### Usage

`nv show platform hardware component <component-id> port <port-id> breakout-mode [options] [<mode-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` | Physical port identifier |
| `<mode-id>` |  Breakout mode identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform hardware component \<component-id\> port \<port-id\> breakout-mode \<mode-id\>

A breakout mode

### Usage

`nv show platform hardware component <component-id> port <port-id> breakout-mode <mode-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` | Physical port identifier |
| `<mode-id>` |  Breakout mode identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment

Platform environment information

### Usage

`nv show platform environment [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `fan` | The fans on the switch. |
| `sensor` | The sensors on the switch. |
| `psu` |  The PSUs on the switch. |
| `led` |  The LEDs on the switch. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment fan

The fans on the switch.

### Usage

`nv show platform environment fan [options] [<fan-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<fan-id>` |   Physical fan identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment fan \<fan-id\>

A physical fan on the component.

### Usage

`nv show platform environment fan <fan-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<fan-id>` |   Physical fan identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment sensor

The sensors on the switch.

### Usage

`nv show platform environment sensor [options] [<sensor-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  Physical sensor identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment sensor \<sensor-id\>

A physical sensor on the component.

### Usage

`nv show platform environment sensor <sensor-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  Physical sensor identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment psu

The PSUs on the switch.

### Usage

`nv show platform environment psu [options] [<psu-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<psu-id>` |  Physical PSU identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment psu \<psu-id\>

A PSU

### Usage

`nv show platform environment psu <psu-id> [options]`


### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<psu-id>` |  Physical PSU identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment led

The LEDs on the switch.

### Usage

`nv show platform environment led [options] [<led-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<led-id>` |  Physical LED identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform environment led \<led-id\>

A LED

### Usage

nv show platform environment led \<led-id\> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<led-id>` |  Physical LED identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform software

The platform's software

### Usage

`nv show platform software [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `installed` |  List of installed software |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform software installed

List of installed software

### Usage

`nv show platform software installed [options] [<installed-id> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<installed-id>` | Package name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show platform software installed \<installed-id\>

An installed package

### Usage

`nv show platform software installed <installed-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<installed-id>` |  Package name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
