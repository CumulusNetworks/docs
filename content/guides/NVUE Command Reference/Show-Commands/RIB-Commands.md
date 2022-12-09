---
title: RIB Commands
author: Cumulus Networks
weight: 370
product: Cumulus Linux
type: nojsscroll
---
## nv show vrf \<vrf-id\> router rib \<afi\>

Vrf aware Routing-table per address-family

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |  Route address family. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> protocol \<import-protocol-id\>

Import Protocols from where routes are known

### Command Syntax

| Syntax |  Description   |
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

- - -

## nv show vrf <\<vrf-id\> router rib \<afi\> route \<route-id\>

A route

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>` |   Route address family. |
| `<route-id>`   | IP prefix |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show vrf \<vrf-id\> router rib \<afi\> route \<route-id\> protocol \<protocol-id\>

Protocol types from where routes are known

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<afi>`          | The route address family.|
| `<route-id>`     | The IP prefix|
| `<protocol-id>`  | The route entry list keys.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
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
