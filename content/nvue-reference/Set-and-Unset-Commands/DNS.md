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

## <h>nv set service dns \<vrf-id\></h>

Provides commands to configure the Domain Name Server (DNS) service.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set service dns \<vrf-id\> search \<domain-id\></h>

Configures the domains to search for name matches.

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
