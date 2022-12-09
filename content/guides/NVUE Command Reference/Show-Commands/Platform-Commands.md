---
title: Platform Commands
author: Cumulus Networks
weight: 230
product: Cumulus Linux
type: nojsscroll
---
## nv show platform

Top-level container for the components in the system. This node represents a system component inventory, which includes hardware and software elements.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform capabilities

Capabilities of this platform

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware

The platform's hardware

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware component

Set of components making up the platform.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware component \<component-id\>

A component in the platform.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware component \<component-id\> linecard

Properties of a linecard component

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware component \<component-id\> port

Set of physical ports on this component

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` |  Physical port identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware component \<component-id\> port \<port-id\>

A physical port on the component.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  Component identifier |
| `<port-id>` |  Physical port identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform hardware component \<component-id\> port \<port-id\> breakout-mode

Set of breakout modes

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show platform hardware component \<component-id\> port \<port-id\> breakout-mode \<mode-id\>

A breakout mode

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show platform environment

Platform environment information

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment fan

The fans on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<fan-id>` |   Physical fan identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment fan \<fan-id\>

A physical fan on the component.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<fan-id>` |   Physical fan identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment sensor

The sensors on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  Physical sensor identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment sensor \<sensor-id\>

A physical sensor on the component.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  Physical sensor identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment psu

The PSUs on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<psu-id>` |  Physical PSU identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment psu \<psu-id\>

A PSU

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<psu-id>` |  Physical PSU identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment led

The LEDs on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<led-id>` |  Physical LED identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform environment led \<led-id\>

A LED

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<led-id>` |  Physical LED identifier |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform software

The platform's software

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform software installed

List of installed software

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<installed-id>` | Package name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show platform software installed \<installed-id\>

An installed package

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<installed-id>` |  Package name |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
