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
cumulus@leaf04:mgmt:~$ nv show vrf default router rib ipv4
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
cumulus@leaf04:mgmt:~$ nv show vrf default router rib ipv4 protocol bgp
```

- - -

## nv show vrf <\<vrf-id\> router rib \<afi\> route \<route-id\>

A route

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
cumulus@leaf04:mgmt:~$ nv show vrf default router rib ipv4 route default
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\>

Protocol types from where routes are known

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<afi>` |  The route address family (IPv4 or IPv6). |
| `<route-id>`   | The IP prefix. |
| `<protocol-id>`  | The protocol name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router rib ipv4 route default protocol bgp
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\>

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> flags

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> flags

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> label

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> resolved-via

### Command Syntax

### Version History

### Example

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index via \<via-id\> resolved-via \<resolved-via-id\>

### Command Syntax

### Version History

### Example
