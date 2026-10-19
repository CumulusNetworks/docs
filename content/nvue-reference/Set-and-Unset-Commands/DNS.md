---
title: DNS
author: Cumulus Networks
weight: 640

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set system dns search <dns-search-id>`.
{{%/notice%}}

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

{{%notice note%}}
In Cumulus Linux 5.15 and later, this command is `nv set system dns server <dns-server-id>`.
{{%/notice%}}

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns search \<dns-search-id\></h>

Configures the domains you want to search for name matches.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dns <vrf-id> search <domain-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<domain-id>` | The domain name or IPv4 address.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system dns search nvidia.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns server \<dns-server-id\></h>

Configures a remote DNS server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dns <vrf-id> server <dns-server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<dns-server-id>`  | The IPv4 or IPv6 address of the remote DNS server. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system dns server 192.0.2.44
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns server \<dns-server-id\> priority</h>

Configures a remote DNS server priority.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<dns-server-id>`  | The IPv4 or IPv6 address of the remote DNS server. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system dns server 192.0.2.44 priority 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns server \<dns-server-id\> source-interface \<interface-id\></h>

Configures the interface that the switch uses to source upstream DNS queries to the specified DNS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<dns-server-id>` |  The IPv4 or IPv6 address of the remote DNS server. |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-interface swp1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns server \<dns-server-id\> source-interface \<interface-id\> address</h>

Configures the address on the source interface that the switch uses for upstream DNS queries. You can set a value of `auto`, an IPv4 address, or an IPv6 address. When set to `auto`, the switch selects the first address of the DNS server address family, in configuration order, that it can use as a query source. The default setting is `auto`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<dns-server-id>` |  The IPv4 or IPv6 address of the remote DNS server. |
| `<interface-id>` |  The interface you want to configure. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-interface swp1 address 198.51.100.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns server \<dns-server-id\> source-ip</h>

Configures the source IP address that the switch uses for upstream DNS queries. You can specify an IPv4 or an IPv6 address.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<dns-server-id>` |  The IPv4 or IPv6 address of the remote DNS server. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set system dns server 192.0.2.1 source-ip 198.51.100.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system dns server \<dns-server-id\> vrf \<vrf-id\></h>

Configures a remote DNS server under a specific VRF.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service dns <vrf-id> server <dns-server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<dns-server-id>`  | The IPv4 or IPv6 address of the remote DNS server. |
| `<vrf-id>`  | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system dns server 192.0.2.44 vrf RED
```
