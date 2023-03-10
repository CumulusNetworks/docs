---
title: Static Routing Set and Unset Commands
author: Cumulus Networks
weight: 700
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set vrf \<vrf-id\> router static \<route-id\>

Configures static routes in a VRF. You can use static routing if you do not require the complexity of a dynamic routing protocol (such as BGP or OSPF), if you have routes that do not change frequently and for which the destination is only one or two paths away.

With static routing, you configure the switch manually to send traffic with a specific destination prefix to a specific next hop. When the switch receives a packet, it looks up the destination IP address in the routing table and forwards the packet accordingly.

Cumulus Linux adds static routes to the FRR routing table and then to the kernel routing table.

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\>

Configures static route settings with the destination path distance.

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\>

Configures the destination path distance and next hop for a specific static route in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<distance-id>` |  A path distance. |
| `<via-id>`       | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag onlink

Configures the destination path distance and next hop for a specific static route in the specified VRF, and adds the `onlink` flag, which configures the switch to pretend that the nexthop is directly attached to the link, even if it does not match any interface prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 flag onlink 
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> interface \<interface-id\>

Configures the destination path distance and next hop for a specific static route in the specified VRF and the interface to use for egress.  If you do not specify an interface, Cumulus Linux determines the interface automatically. This command is only valid when the next hop (via) type is an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the nexthop router. |
| `<interface-id>`  | The interface to use for egress. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 interface swp1
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> vrf

Configures the destination path distance and next hop for a specific static route in the specified VRF and the VRF to use for egress.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the nexthop router. |
| `<vrf-id>`  | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 vrf RED
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> type

Configures the destination path distance and next hop type for a specific static route in the specified VRF. The next hop type can be `interface`, `ipv4-address`, `ipv6-address`, `blackhole`, or `reject`.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 type interface
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> tag

Configures the destination path distance and tag for a specific static route in the specified VRF. The tag provides additional information about the static route, such as the community tag or a route metric, and is included with the route in the routing table. The tag can be a value between 1 and 4294967295, or `none`.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<distance-id>` |  The path distance. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 distance 2 tag none
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\>

Configures the next hop for a specific static route in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<via-id>`       | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag onlink

Configures the next hop for a specific static route in the specified VRF, and adds the `onlink` flag, which configures the switch to pretend that the nexthop is directly attached to the link, even if it does not match any interface prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<via-id>`       | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 flag onlink 
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> interface \<interface-name\>

Configures the next hop for a specific static route in the specified VRF, and the interface to use for egress. If you do not specify an interface, Cumulus Linux determines the interface automatically. This command is only valid when the next hop (via) type is an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<via-id>`       | The IP address of the nexthop router. |
| `<interface-name>`  | The interface to use for egress. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 interface swp1
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> vrf \<vrf-id\>

Configures the next hop for a specific static route in the specified VRF, and the VRF to use for egress. If you do not specify a VRF, Cumulus Linux uses the default VRF.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<via-id>`   | The IP address of the nexthop router. |
| `<vrf-id>`   | The egress VRF. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 vrf RED
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> type

Configures the next hop type for a specific static route in the specified VRF. The next hop type can be `interface`, `ipv4-address`, `ipv6-address`, `blackhole`, or `reject`.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |
| `<via-id>`   | The IP address of the nexthop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 via 10.0.1.0 type interface
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> tag

Configures the static route tag in the specified VRF. The tag provides additional information about the static route, such as the community tag or a route metric, and is included with the route in the routing table. The tag can be a value between 1 and 4294967295, or `none`.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 tag none
```

- - -

## nv set vrf \<vrf-id\> router static \<route-id\> address-family

Enables and disables the address family (`ipv4-unicast` or `ipv6-unicast`) for the static route in the specified VRF.

## Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IP prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set vrf default router static 10.10.10.101/32 address-family ipv6-unicast
```

- - -
