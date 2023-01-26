---
title: IGMP Set and Unset Commands
author: Cumulus Networks
weight: 590
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if there is a difference between the `nv set` and `nv unset` command.
{{%/notice%}}

## nv set interface \<interface-id\> ip igmp

Provides commands to configure Internet Group Management Protocol (IGMP).

- - -

## nv set interface \<interface-id\> ip igmp static-group \<static-group-id\>

Configures the IGMP static multicast mroute destination. This is the IPv4 address of the member associated with the specified multicast group address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<static-group-id>` | The IGMP static multicast mroute destination. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp static-group 234.10.10.10
```

- - -

## nv set interface \<interface-id\> ip igmp static-group \<static-group-id\> source-address \<ipv4-unicast\>

Configures the IPv4 unicast address of the IGMP static multicast mroute source.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |
| `<static-group-id>` | The IGMP static multicast mroute destination. |
| `<ipv4-unicast>` | The IPv4 unicast address. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp static-group 234.10.10.10 source-address 234.1.1.1
```

- - -

## nv set interface \<interface-id\> ip igmp enable

Turns IGMP on or off on the specified interface.

The default setting is `off`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp enable on
```

- - -

## nv set interface \<interface-id\> ip igmp version

Configures the IGMP version. You can specify version 2 or version 3.

The default setting is `2`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp version 3
```

- - -

## nv set interface \<interface-id\> ip igmp query-interval

Configures how often IGMP sends query-host messages to discover which multicast groups have members on the attached networks. You can specify a value between 1 and 1800 seconds.

The default setting is `125`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp query-interval 1000
```

- - -

## nv set interface \<interface-id\> ip igmp query-max-response-time

Configures the maximum response time for IGMP general queries. You can specify a value between 10 and 250 seconds.

The default setting is `10`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp query-max-response-time 100
```

- - -

## nv set interface \<interface-id\> ip igmp last-member-query-interval

Configures the maximum response time advertised in IGMP group-specific queries . You can specify a value between 1 and 255 seconds.

The default setting is `1`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set interface swp1 ip igmp last-member-query-interval 10
```

- - -

## nv set router igmp

Provides commands to configure global IGMP settings.

- - -

## nv set router igmp enable

Turns IGMP on or off globally.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router igmp on
```
