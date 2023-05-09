---
title: NTP
author: Cumulus Networks
weight: 230
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ntp</h>

Shows the <span style="background-color:#F5F5DC">[NTP](## "Network Time Protocol")</span> configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ntp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ntp \<vrf-id\></h>

Shows the NTP configuration in the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ntp default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ntp \<vrf-id\> pool \<server-id\></h>

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
cumulus@switch:~$ nv show service ntp default pool 4.cumulusnetworks.pool.ntp.org
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ntp \<vrf-id\> server \<server-id\></h>

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
cumulus@switch:~$ nv show service ntp default server time.nist.gov
```
