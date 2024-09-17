---
title: Static Routing
author: Cumulus Networks
weight: 740

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set vrf \<vrf-id\> router static \<route-id\></h>

Configures static routes in a VRF. You can use static routing if you do not require the complexity of a dynamic routing protocol (such as BGP or OSPF), if you have routes that do not change frequently and for which the destination is only one or two paths away.

With static routing, you configure the switch manually to send traffic with a specific destination prefix to a specific next hop. When the switch receives a packet, it looks up the destination IP address in the routing table and forwards the packet accordingly.

Cumulus Linux adds static routes to the FRR routing table and then to the kernel routing table.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\></h>

Configures static route settings with the destination path distance.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\></h>

Configures the destination path distance and next hop for a specific static route in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<distance-id>` |  A path distance. |
| `<via-id>`       | The IP address of the next hop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag onlink</h>

Configures the destination path distance and next hop for a specific static route in the specified VRF, and adds the `onlink` flag, which configures the switch to pretend that the next hop is directly attached to the link, even if it does not match any interface prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the next hop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 flag onlink 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> interface \<interface-id\></h>

Configures the destination path distance and next hop for a specific static route in the specified VRF and the interface to use for egress. If you do not specify an interface, Cumulus Linux determines the interface automatically. This command is only valid when the next hop (via) type is an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the next hop router. |
| `<interface-id>`  | The interface to use for egress. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0 interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> tag</h>

Configures the destination path distance and tag for a specific static route in the specified VRF. The tag provides additional information about the static route, such as the community tag or a route metric and is with the route in the routing table. The tag can be a value between 1 and 4294967295, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<distance-id>` |  The path distance. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 tag none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> type</h>

Configures the destination path distance and next hop type for a specific static route in the specified VRF. The next hop type can be `interface`, `ipv4-address`, `ipv6-address`, `blackhole`, or `reject`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the next hop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.10.10.1 type interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> vrf</h>

Configures the destination path distance and next hop for a specific static route in the specified VRF, and the VRF to use for egress.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>`       | The IP address of the next hop router. |
| `<vrf-id>`  | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 distance 2 via 10.10.10.1 vrf RED
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> tag</h>

Configures the static route tag in the specified VRF. The tag provides additional information about the static route, such as the community tag or a route metric, and is included with the route in the routing table. The tag can be a value between 1 and 4294967295, or `none`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 tag none
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\></h>

Configures the next hop for a specific static route in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<via-id>`       | The IP address of the next hop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag onlink</h>

Configures the next hop for a specific static route in the specified VRF, and adds the `onlink` flag, which configures the switch to pretend that the next hop is directly attached to the link, even if it does not match any interface prefix.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<via-id>`       | The IP address of the next hop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.10.10.1 flag onlink 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> interface \<interface-name\></h>

Configures the next hop for a specific static route in the specified VRF, and the interface to use for egress. If you do not specify an interface, Cumulus Linux determines the interface automatically. This command is only valid when the next hop (via) type is an IPv4 or IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<via-id>`       | The IPv4 or IPv6 address of the next hop router. |
| `<interface-name>`  | The interface to use for egress. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.10.10.1 interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> type</h>

Configures the next hop type for a specific static route in the specified VRF. The next hop type can be `interface`, `ipv4-address`, `ipv6-address`, `blackhole`, or `reject`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<via-id>`   | The IP address of the next hop router. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.10.10.1 type interface
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set vrf \<vrf-id\> router static \<route-id\> via \<via-id\> vrf \<vrf-id\></h>

Configures the next hop for a specific static route in the specified VRF, and the VRF to use for egress. If you do not specify a VRF, Cumulus Linux uses the default VRF.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<route-id>` |  The IPv4 or IPv6 prefix. |
| `<via-id>`   | The IP address of the next hop router. |
| `<vrf-id>`   | The egress VRF. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set vrf default router static 10.10.10.101/32 via 10.10.10.1 vrf RED
```
