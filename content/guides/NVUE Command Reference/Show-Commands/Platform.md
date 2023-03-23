---
title: Platform
author: Cumulus Networks
weight: 270
product: Cumulus Linux
type: nojsscroll
---
## nv show platform

Shows a list of all the software and hardware components on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform
```

- - -

## nv show platform capabilities

Shows the platform capabilities of the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform capabilities
```

- - -

## nv show platform environment

Shows a list of sensors, fans, LEDs, and PSUs on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment
```

- - -

## nv show platform environment fan

Shows information about the fans on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment fan
```

- - -

## nv show platform environment fan \<fan-id\>

Shows information about the specified fan on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<fan-id>` |   The physical fan identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment fan Fan2
```

- - -

## nv show platform environment led

Shows information about the LEDs on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment led
```

- - -

## nv show platform environment led \<led-id\>

Shows information about the specified LED.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<led-id>` |  The physical LED identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment led Fan
```

- - -

## nv show platform environment psu

Shows information about the PSUs on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment psu
```

- - -

## nv show platform environment psu \<psu-id\>

Shows information about the specified PSU on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<psu-id>` |  The physical PSU identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment psu PSU1
```

- - -

## nv show platform environment sensor

Shows information about the physical sensors on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment sensor 
```

- - -

## nv show platform environment sensor \<sensor-id\>

Shows information about the specified physical sensor on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  The physical sensor identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform environment sensor Temp
```

- - -

## nv show platform hardware

Shows platform hardware information on the switch, such as the base MAC address, model and manufacturer, memory, Cumulus Linux release, serial numner and system MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform hardware
```

- - -

## nv show platform hardware component

Shows the hardware components on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform hardware component
```

- - -

## nv show platform hardware component \<component-id\>

Shows information about the specified platform component.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  The component name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform hardware component device
```

- - -

## nv show platform software

Shows the software installed on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform software
```

- - -

## nv show platform software installed

Shows a list of the installed software on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform software installed
```

- - -

## nv show platform software installed \<installed-id\>

Shows information about the specified installed package, such the package description and version number.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<installed-id>` |  The package name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show platform software installed what-just-happened
```

- - -
