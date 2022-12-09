---
title: Syslog Commands
author: Cumulus Networks
weight: 320
product: Cumulus Linux
type: nojsscroll
---
## nv show service syslog

collection of syslog

### Usage

`nv show service syslog [options] [<vrf-id> ...]`

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

## nv show service syslog \<vrf-id\>

Domain Name Service

### Usage

`nv show service syslog <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server` | Remote DNS servers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

- - -

## nv show service syslog \<vrf-id\> server \<server-id\>

A remote DNS server

### Usage

`nv show service syslog <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` | Hostname or IP address of a syslog server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```
