---
title: OSPF Commands
author: Cumulus Networks
weight: 190
product: Cumulus Linux
type: nojsscroll
---
## nv show router ospf

Shows global OSPF configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router ospf
```

- - -

## nv show router ospf timers

Shows all OSPF timer settings, such as <span style="background-color:#F5F5DC">[LSA](## "Link State Advertisement")</span> timers and <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> timers that prevent consecutive SPF from overburdening the CPU.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router ospf timers
```

- - -

## nv show router ospf timers lsa

Shows <span style="background-color:#F5F5DC">[LSA](## "Link State Advertisement")</span> throttle timer settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router ospf timers lsa
```

- - -

## nv show router ospf timers spf

Shows <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> timer settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router ospf timers spf
```

- - -

## nv show interface \<interface-id\> router ospf

Shows all OSPF configuration settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp51 router ospf
```

- - -

## nv show interface \<interface-id\> router ospf timers

Shows <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> timer settings for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp51 router ospf timers
```

- - -

## nv show interface \<interface-id\> router ospf authentication

Shows the MD5 authentication configuration settings on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp51 router ospf authentication
```

- - -

## nv show interface \<interface-id\> router ospf bfd

Shows the BFD configuration settings on the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`    | The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show interface swp51 router ospf bfd
```

- - -

## nv show vrf \<vrf-id\> router ospf

Shows the OSPF configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\>

Shows the specified OSPF area configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf area 0
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\> filter-list

Shows the filter list for the specified OSPF area for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf area 0 filter-list
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\>

Shows the configuration settings for the specified OSPF area prefix range for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  The area ID. |
| `<range-id>` |  The IPv4 prefix range. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf area 0 range 172.16.1.0/24
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\>

Shows the configuration settings for the specified OSPF area network subnet for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<area-id>` |  The area ID. |
| `<network-id>`  | The IPv4 network subnet. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf area 0 network 10.10.10.1/32
```

- - -

## nv show vrf \<vrf-id\> router ospf default-originate

Shows OSPF default originate information for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf default-originate
```

- - -

## nv show vrf \<vrf-id\> router ospf distance

Shows the OSPF administrative distance configuration for the specified VRF. You configure the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf distance
```

- - -

## nv show vrf \<vrf-id\> router ospf max-metric

Shows the maximum metric configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf max-metric
```

- - -

## nv show vrf \<vrf-id\> router ospf log

Shows the OSPF log configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf log
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute

Shows the OSPF route redistribute settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf redistribute
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute static

Shows configuration settings for OSPF redistribute static routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf redistribute static
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute connected

Shows configuration settings for OSPF redistribute connected routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf redistribute connected
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute kernel

Shows configuration settings for OSPF redistribute kernel routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf redistribute kernel
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute bgp

Shows configuration settings for OSPF redistribute BGP routes for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf redistribute bgp
```

- - -

## nv show vrf \<vrf-id\> router ospf timers

Shows OSPF timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf timers 
```

- - -

## nv show vrf \<vrf-id\> router ospf timers lsa

Shows the <span style="background-color:#F5F5DC">[LSA](## "Link State Advertisement")</span> throttle timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf timers lsa
```

- - -

## nv show vrf \<vrf-id\> router ospf timers spf

Shows <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> timer settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show vrf default router ospf timers spf
```
