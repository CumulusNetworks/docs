---
title: OSPF Commands
author: Cumulus Networks
weight: 190
product: Cumulus Linux
type: nojsscroll
---
## nv show router ospf

OSPF global configuration.

### Usage

`nv show router ospf [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers` |  Timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show router ospf timers

Timers

### Usage

`nv show router ospf timers [options] [<attribute> ...]`

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lsa` |   LSA timers |
| `spf` | SPF timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show router ospf timers lsa

LSA timers

### Usage

`nv show router ospf timers lsa [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show router ospf timers spf

SPF timers

### Usage

`nv show router ospf timers spf [options]`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> router ospf

OSPF interface configuration.

### Usage

`nv show interface <interface-id> router ospf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `timers`                | `Timers configuration |
| `authentication`        | `md5 authentication configuration |
| `bfd`                   | `BFD configuration |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> router ospf timers

Timers configuration

### Usage

`nv show interface <interface-id> router ospf timers [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> router ospf authentication

md5 authentication configuration

### Usage

`nv show interface <interface-id> router ospf authentication [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show interface \<interface-id\> router ospf bfd

BFD configuration

### Usage

`nv show interface <interface-id> router ospf bfd [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<interface-id>`    |    Interface |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast

IPv4 unicast address family

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `redistribute`     | Route redistribute| 
| `aggregate-route`  | IPv4 aggregate routes| 
| `network`          | IPv4 static networks.| 
| `route-import `    | Route import| 
| `multipaths`       | Multipaths| 
| `admin-distance`   | Admin distances.| 
| `route-export`     | Route export| 
| `loc-rib`          | IPv4 local RIB|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router bgp address-family ipv4-unicast redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router bgp address-family ipv4-unicast redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`    | Route redistribution of ipv4 static routes |
| `connected` | Route redistribution of ipv4 connected routes |
| `kernel`    | Route redistribution of ipv4 kernel routes|
| `ospf`      | Route redistribution of ipv4 ospf routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf

OSPF VRF configuration.

### Usage

`nv show vrf <vrf-id> router ospf [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `area`                  | OSPF areas |
| `default-originate`     | Advertise a default route as external lsa |
| `distance`              | Administrative distance for installation into the rib |
| `max-metric`            | Set maximum metric value in router lsa to make stub router |
| `log`                   | Log configuration |
| `redistribute`          | Route redistribute |
| `timers`                | Timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\>

An OSPF area

### Usage

`nv show vrf <vrf-id> router ospf area <area-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `filter-list`  | Filters networks between OSPF areas |
| `range`        | Area ranges |
| `network`      | Area networks |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\> filter-list

Filters networks between OSPF areas
### Usage

`nv show vrf <vrf-id> router ospf area <area-id> filter-list [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\> range \<range-id\>

Filters out components of the prefix

### Usage

`nv show vrf <vrf-id> router ospf area <area-id> range <range-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |
| `<range-id>` |  Range |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf area \<area-id\> network \<network-id\>

Filters out components of the prefix

### Usage

`nv show vrf <vrf-id> router ospf area <area-id> network <network-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<area-id>` |  Area |
| `<network-id>`  | Network |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf default-originate

Advertise a default route as external lsa

### Usage

`nv show vrf <vrf-id> router ospf default-originate [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf distance

Administrative distance for installation into the rib


### Usage

`nv show vrf <vrf-id> router ospf distance [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf max-metric

Set maximum metric value in router lsa to make stub router


### Usage

`nv show vrf <vrf-id> router ospf max-metric [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf log

Log configuration

### Usage

`nv show vrf <vrf-id> router ospf log [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute

Route redistribute

### Usage

`nv show vrf <vrf-id> router ospf redistribute [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `static`      | Route redistribute of static routes |
| `connected`   | Route redistribute of connected routes |
| `kernel`      | Route redistribute of kernel routes |
| `bgp`         | Route redistribute of bgp routes |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute static

Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute static [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute connected

 Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute connected [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute kernel

Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute kernel [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf redistribute bgp

Source route type.

### Usage

`nv show vrf <vrf-id> router ospf redistribute bgp [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf timers

Timers

### Usage

`nv show vrf <vrf-id> router ospf timers [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `lsa`     | LSA timers |
| `spf`     | SPF timers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf timers lsa

LSA timers

### Usage

`nv show vrf <vrf-id> router ospf timers lsa [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router ospf timers spf

SPF timers

### Usage

`nv show vrf <vrf-id> router ospf timers spf [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
