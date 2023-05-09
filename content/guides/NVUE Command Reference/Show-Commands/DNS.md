---
title: DNS
author: Cumulus Networks
weight: 160
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show service dns</h>

Shows <span style="background-color:#F5F5DC">[DNS](## "Domain Name Service")</span> configuration settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dns \<vrf-id\></h>

Shows <span style="background-color:#F5F5DC">[DNS](## "Domain Name Service")</span> configuration settings for the specified VRF.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service dns \<vrf-id\> server \<dns-server-id\></h>

Shows information about the specified remote DNS server.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<dns-server-id>` | The IPv4 or IPv6 address of a DNS server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service dns default server 192.0.2.1
```
