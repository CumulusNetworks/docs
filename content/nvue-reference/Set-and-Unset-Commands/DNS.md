---
title: DNS
author: Cumulus Networks
weight: 550

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dns \<vrf-id\> search \<domain-id\></h>

Configures the domains you want to search for name matches.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` | The VRF you want to configure. |
| `<domain-id>` | The domain name or IPv4 address.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set service dns default search nvidia.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dns \<vrf-id\> server \<dns-server-id\></h>

Configures a remote DNS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>`         | The VRF you want to configure. |
| `<dns-server-id>`  | The IPv4 or IPv6 address of the remote DNS server.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set service dns default server 192.0.2.44
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns domain \<domain-name\></h>

Configures the domain name on the Cumulus Linux switch, which is critical for accurate DNS resolution, network service integration, and compliance with networking standards. Cumulus Linux adds the domain name to the hostname and displays both the hostname and domain name in the shell prompt (after you log back in).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-name>`  | The domain name you want to set on the switch. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv set system dns domain nvidia.com
```
