---
title: RIB Commands
author: Cumulus Networks
weight: 370
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router rib \<afi\>

Vrf aware Routing-table per address-family

### Usage

`nv show vrf <vrf-id> router rib <afi> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |  Route address family. |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `protocol` |   Import protocols from RIB to FIB |
| `route` |  RIB Routes with info.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\>

Import Protocols from where routes are known

### Usage

`nv show vrf <vrf-id> router rib <afi> protocol <import-protocol-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |   Route address family. |
| `<import-protocol-id>` |  Import protocol list. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf <\<vrf-id\> router rib \<afi\> route \<route-id\>

A route

### Usage

`nv show vrf <vrf-id> router rib <afi> route <route-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |   Route address family. |
| `<route-id>`   | IP prefix |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `protocol` |   Route entries |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\>

Protocol types from where routes are known

### Usage

`nv show vrf <vrf-id> router rib <afi> route <route-id> protocol <protocol-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>`          | The route address family.|
| `<route-id>`     | The IP prefix|
| `<protocol-id>`  | The route entry list keys.|

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `entry-index` | Route entries |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\>

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> flags

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> flags

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> label

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index \<entry-index\> via \<via-id\> resolved-via

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\> entry-index via \<via-id\> resolved-via \<resolved-via-id\>
