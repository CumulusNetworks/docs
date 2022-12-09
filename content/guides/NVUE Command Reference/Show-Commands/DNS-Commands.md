---
title: DNS Commands
author: Cumulus Networks
weight: 145
product: Cumulus Linux
type: nojsscroll
---
## nv show service dns

collection of DNS

### Usage

`nv show service dns [options] [<vrf-id> ...]`

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

## nv show service dns \<vrf-id\>

Domain Name Service

### Usage

`nv show service dns <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server` |   Remote DNS servers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service dns \<vrf-id\> server \<dns-server-id\>

A remote DNS server

### Usage

`nv show service dns <vrf-id> server <dns-server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<dns-server-id>`  | IPv4 or IPv6 address of a DNS server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
