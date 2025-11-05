---
title: NTP
author: Cumulus Networks
weight: 620

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ntp vrf \<vrf-id\></h>

Configures the Network Time Protocol (NTP) in a specific VRF. The default VRF is `default`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service ntp <vrf-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |  The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ntp vrf default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ntp listen \<interface-name\></h>

Configures the NTP interface on which to listen. The default setting is `eth0`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service ntp <vrf-id> listen <interface-name>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<interface-name>` |  The NTP interface on which to listen. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ntp listen swp10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service ntp \<vrf-id\> pool \<server-id\></h>

Configures the remote NTP server pool.

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |
| `<server-id>` |  The NTP server pool. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service ntp default pool 4.cumulusnetworks.pool.ntp.org
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ntp server \<server-id\></h>

Configures the remote NTP server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service ntp <vrf-id> server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ntp server time.nist.gov
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ntp server \<server-id\> iburst</h>

Configures NTP to send a burst of eight packets instead of the usual one packet when the server pool is unreachable. You can specify `enabled` or `disabled`. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service ntp <vrf-id> server <server-id> iburst` and the value is `on` or `off`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The NTP server pool. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ntp server 192.168.200.1 iburst
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ntp state</h>

Enables and disables NTP. You can specify `enabled` or `disabled`. The default setting is `enabled`.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ntp state disabled
```
