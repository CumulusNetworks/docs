---
title: NTP Commands
author: Cumulus Networks
weight: 180
product: Cumulus Linux
type: nojsscroll
---
- - -

## nv show service ntp

Shows the Network Time Protocol (NTP) configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service ntp
```

- - -

## nv show service ntp \<vrf-id\>

Shows the NTP configuration in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service ntp default
```

- - -

## nv show service ntp \<vrf-id\> server \<server-id\>

Shows information about the specified remote NTP server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service ntp default server time.nist.gov
```

- - -

## nv show service ntp \<vrf-id\> pool \<server-id\>

Shows information about the specified remote NTP server pool.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service ntp default server 4.cumulusnetworks.pool.ntp.org
```
