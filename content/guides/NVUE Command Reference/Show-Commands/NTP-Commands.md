---
title: NTP Commands
author: Cumulus Networks
weight: 160
product: Cumulus Linux
type: nojsscroll
---
## nv show service ntp

NTPs

### Usage

`nv show service ntp [options] [<vrf-id> ...]`

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

## nv show service ntp \<vrf-id\>

Network Time Protocol

### Usage

`nv show service ntp <vrf-id> [options] [<attribute> ...]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |

### Attributes

| Attribute |  Description   |
| --------- | -------------- |
| `server` | Remote NTP Servers |
| `pool`  |  Remote NTP Servers |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp \<vrf-id\> server \<server-id\>

A remote NTP Server

### Usage

`nv show service ntp <vrf-id> server <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |   Hostname or IP address of the NTP server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```

## nv show service ntp \<vrf-id\> pool \<server-id\>

A remote NTP Server

### Usage

`nv show service ntp <vrf-id> pool <server-id> [options]`

### Identifiers

| Identifier |  Description   |
| --------- | -------------- |
| `<vrf-id>` |    VRF |
| `<server-id>` |   Hostname or IP address of the NTP server |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ 
```