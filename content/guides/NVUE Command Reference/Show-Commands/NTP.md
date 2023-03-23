---
title: NTP
author: Cumulus Networks
weight: 250
product: Cumulus Linux
type: nojsscroll
---
- - -

## nv show service ntp

Shows the <span style="background-color:#F5F5DC">[NTP](## "Network Time Protocol")</span> configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service ntp
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
cumulus@leaf01:mgmt:~$ nv show service ntp default
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
cumulus@leaf01:mgmt:~$ nv show service ntp default pool 4.cumulusnetworks.pool.ntp.org
```

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
cumulus@leaf01:mgmt:~$ nv show service ntp default server time.nist.gov
```

- - -
