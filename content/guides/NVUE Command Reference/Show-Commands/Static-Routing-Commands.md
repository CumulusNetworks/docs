---
title: Static Routing Commands
author: Cumulus Networks
weight: 310
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router static \<route-id\>

A route 

### Usage

`nv show vrf <vrf-id> router static <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `distance` |  Paths |
| `via` |  Nexthops |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\>

A path

### Usage

`nv show vrf <vrf-id> router static <route-id> distance <distance-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `via`  |  Nexthops |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\>

A via

### Usage

`nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |
| `<via-id>` | IP address, interface, or "blackhole". |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flag` |  Nexthop flags |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag

Nexthop flags

### Usage

`nv show vrf <vrf-id> router static <route-id> distance <distance-id> via <via-id> flag [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |
| `<via-id>` | IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\>

A via

### Usage

`nv show vrf <vrf-id> router static <route-id> via <via-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<via-id>` | IP address, interface, or "blackhole". |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `flag` |  Nexthop flags |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag

Nexthop flags

### Usage

`nv show vrf <vrf-id> router static <route-id> via <via-id> flag [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<via-id>` |   IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
