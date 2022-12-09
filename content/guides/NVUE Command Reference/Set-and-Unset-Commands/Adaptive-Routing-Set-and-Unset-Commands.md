---
title: Adaptive Routing Set and Unset Commands
author: Cumulus Networks
weight: 520
product: Cumulus Linux
type: nojsscroll
---
## nv set interface \<interface-id\> router adaptive-routing

Configures adaptive routing on the specified interface. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

### Usage

`nv [options] set interface <interface-id> router adaptive-routing [enable ...]`

`nv [options] set interface <interface-id> router adaptive-routing [link-utilization-threshold ...]`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `interface-id` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

- - -

## nv set interface \<interface-id\> router adaptive-routing enable (on|off)

Turns adaptive routing on the specified interface on or off.

### Usage

`nv [options] set interface <interface-id> router adaptive-routing enable [<arg> ...]`

### Default Setting

`off`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `interface-id` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 router adaptive-routing enable on
```

- - -

## nv set interface \<interface-id\> router adaptive-routing link-utilization-threshold

Configures the link utilization threshold percentage. You can specify a value between 1 and 100.

### Usage

`nv [options] set interface <interface-id> router adaptive-routing link-utilization-threshold <arg>`

### Default Setting

`70`

### Identifiers

| Identifier |  Description   |
| ---------  | -------------- |
| `interface-id` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 router adaptive-routing link-utilization-threshold 50
```

- - -

## nv set router adaptive-routing

Configures adaptive routing globally on the switch. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

### Usage

`nv [options] set router adaptive-routing [enable ...]`

### Version History

Introduced in Cumulus Linux 5.1.0

- - -

## nv set router adaptive-routing enable

Turns adaptive routing on or off.

### Usage

`nv [options] set router adaptive-routing enable [<arg> ...]`

### Default Setting

`off`

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router adaptive-routing enable on
```
