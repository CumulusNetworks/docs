---
title: Interface Address Set and Unset Commands
author: Cumulus Networks
weight: 560
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set interface \<interface-id\> ip

Configures IP addressing for an interface.

- - -

## nv set interface \<interface-id\> ip address \<ip-prefix-id\>

Configures an IP address with a route prefix for the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-prefix-id>` | The IPv4 or IPv6 address and route prefix in CIDR notation. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip address 10.0.0.1/30
```

- - -

## nv set interface \<interface-id\> ip gateway \<ip-address-id\>

Configures the gateway IP address on the specified interface.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |
| `<ip-address-id>` | The IP address.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip gateway 10.10.10.1
```

- - -

## nv set interface \<interface-id\> ip ipv4

Configures IPv4 settings for an interface.

- - -

## nv set interface \<interface-id\> ip ipv4 forward

Turns IPv4 forwarding on or off for the specified interface. The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv4 forward on
```

- - -

## nv set interface \<interface-id\> ip ipv6

Configures IPv6 settings for an interface.

### Version History

Introduced in Cumulus Linux 5.0.0

- - -

## nv set interface \<interface-id\> ip ipv6 enable

Turns IPv6 on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv6 enable off
```

- - -

## nv set interface \<interface-id\> ip ipv6 forward

Turns IPv6 forwarding on or off. The default setting is `on`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` | The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip ipv6 forward off
```

- - -
