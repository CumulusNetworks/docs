---
title: RIB Commands
author: Cumulus Networks
weight: 370
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router rib \<afi\>

Shows the IPv4 or IPv6 routing table for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> protocol \<protocol\>

Shows the IPv4 or IPv6 routing table for the specified protocol (bgp, isis, ospf, rip, sharp, table, connected, kernel, ospf6, ripng, or static) for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<import-protocol-id>` |  The protocol name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 protocol bgp
```

- - -

## nv show vrf <\<vrf-id\> router rib \<afi\> route \<route-id\>

Shows the routing table for the specified route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\>

Shows the routing table for the specified protocol route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index

Shows the routing table entry index for the specified protocol route.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\>

Shows information about the routing table entry for the specified protocol route.

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> flags

Shows the routing table entry flags for the specified protocol route.

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 flags
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via

Shows

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> flags

Shows

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` |  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via ??? flags
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> label

Shows

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` |  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via ??? label
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> resolved-via

Shows

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` |  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via ??? resolved-via
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index via \<via-id\> resolved-via \<resolved-via-id\>

Shows 

### Command Syntax

| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name, such as bgp or ospf.|
| `<entry-index>` | The routing table entry index.|
| `<via-id>` |  |
| `<resolved-via-id>` |  |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example


```
cumulus@leaf01:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp entry-index 10 via ??? resolved-via ???
```
