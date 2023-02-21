---
title: Syslog Commands
author: Cumulus Networks
weight: 320
product: Cumulus Linux
type: nojsscroll
---
## nv show service syslog

Shows the syslog configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service syslog
```

- - -

## nv show service syslog \<vrf-id\>

Shows the syslog configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service syslog default
```

- - -

## nv show service syslog \<vrf-id\> server \<server-id\>

Shows information about the specified remote DNS server for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name. |
| `<server-id>` | The hostname or IP address of a syslog server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show service syslog default server 192.168.0.254
```
