---
title: Static Routing Commands
author: Cumulus Networks
weight: 310
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router static \<route-id\>

A route 

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\>

A path

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<distance-id>` |  A path distance |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\>

A via

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag

Nexthop flags

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\>

A via

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<route-id>` |   IP prefix |
| `<via-id>` | IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag

Nexthop flags

### Command Syntax

| Syntax |  Description   |
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
