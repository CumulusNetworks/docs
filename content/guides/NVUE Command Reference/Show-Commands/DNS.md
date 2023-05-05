---
title: DNS
author: Cumulus Networks
weight: 160
product: Cumulus Linux
type: nojsscroll
---
## nv show service dns

Shows <span style="background-color:#F5F5DC">[DNS](## "Domain Name Service")</span> configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dns
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show service dns \<vrf-id\>

Shows <span style="background-color:#F5F5DC">[DNS](## "Domain Name Service")</span> configuration settings for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dns default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 1.0PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 6.0PX;"/>

## nv show service dns \<vrf-id\> server \<dns-server-id\>

Shows information about the specified remote DNS server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<dns-server-id>`  | The IPv4 or IPv6 address of a DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show service dns default server 192.0.2.1
```
