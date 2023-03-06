---
title: Adaptive Routing Set and Unset Commands
author: Cumulus Networks
weight: 510
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> router adaptive-routing

Provides commands to configure adaptive routing on the specified interface. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

- - -

## nv set interface \<interface-id\> router adaptive-routing enable

Turns adaptive routing on the specified interface on or off.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
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

Configures the link utilization threshold percentage at which adaptive routing considers the port congested. You can specify a value between 1 and 100.

The default setting is `70`.

### Command Syntax

| Syntax |  Description   |
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

Provides commands to configure adaptive routing globally on the switch. Adaptive routing is a load balancing mechanism that improves network utilization by selecting routes dynamically based on the immediate network state, such as switch queue length and port utilization.

- - -

## nv set router adaptive-routing enable

Turns adaptive routing on or off.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router adaptive-routing enable on
```
