---
title: Static Routing Commands
author: Cumulus Networks
weight: 310
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router static \<route-id\>

Shows configuration information about the static route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` | The IP prefix. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router static 10.10.10.101/32
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\>

Shows information about the administrative distance for the static route for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` | The IP prefix. |
| `<distance-id>` | The path distance. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router static 10.10.10.101/32 distance 2
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\>

Shows information about the administrative distance for the static route and next hop for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` | The IP prefix. |
| `<distance-id>` | The path distance. |
| `<via-id>` | The IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router static 10.10.10.101/32 distance 2 via 10.0.1.0
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> distance \<distance-id\> via \<via-id\> flag

Shows the flag value for the static route with the specified route prefix and distance in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` | The IP prefix. |
| `<distance-id>` |  The path distance. |
| `<via-id>` | The IP address, interface, or "blackhole".|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router static 10.10.10.101/32
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\>

Shows information about the next hop for the static route in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` | The IP prefix. |
| `<via-id>` | The IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router static 10.10.10.101/32 via 10.0.1.0
```

- - -

## nv show vrf \<vrf-id\> router static \<route-id\> via \<via-id\> flag

Shows the flag value for the static route with the next hop in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|
| `<route-id>` | The IP prefix. |
| `<via-id>` | The IP address, interface, or "blackhole". |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show vrf default router static 10.10.10.101/32 via 10.0.1.0 flag
```
