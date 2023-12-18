---
title: RADIUS
author: Cumulus Networks
weight: 695

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system aaa radius server \<hostname-id\></h>

Configures the IP address or hostname of the RADIUS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<hostname-id\> port</h>

Configures the port used to communicate with the specified RADIUS Server. A port is optional. You can set a value between 0 and 65535. The default value is 1812.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 port 42
```

 <HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<hostname-id\> priority</h>

Configures the priority at which Cumulus Linux contacts the specified RADIUS server for load balancing. You can set a value between 1 and 100. The lower value is the higher priority.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 priority 10
```

 <HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<hostname-id\> secret</h>

Configures the secret key shared between the specified RADIUS server and client. If you include special characters in the key (such as `$`), you must enclose the key in single quotes (').

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 secret 'myradius$key'
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<hostname-id\> source-ipv4</h>

Configures the specific interface IPv4 address you want to use to reach the specified RADIUS server. If you configure multiple RADIUS servers, you can configure a specific interface to reach all RADIUS servers with the `nv set system aaa radius source-ipv4` command, described below.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 source-ipv4 192.168.1.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<hostname-id\> source-ipv6</h>

Configures the specific interface IPv6 address you want to use to reach the specified RADIUS server. If you configure multiple RADIUS servers, you can configure a specific interface to reach all RADIUS servers with the `nv set system aaa radius source-ipv6` command, described below.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 source-ipv6 0:0:0:0:0:ffff:c0a8:010a
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<hostname-id\> timeout</h>

Configures the timeout value when a server is slow or latencies are high. You can set a value between 1 and 60. The default timeout is 3 seconds. If you configure multiple RADIUS servers, you can set a global timeout for all servers with the `nv set system aaa radius timeout` command.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 timeout 10
```

 <HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius debug</h>

Configures the debug option for troubleshooting. The debugging messages write to `/var/log/syslog`. When the RADIUS client is working correctly, you can disable the debug option. You can specify `enable` or `disable`.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius debug enable
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius enable</h>

Enables (`on`) and disables (`off`) RADIUS.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius port</h>

Configures the port you want to use for all RADIUS communication. You can specify a value between 0 and 65535. The default value is 1812.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius privilege-level</h>

Configures the minimum privilege level that determines if users can configure the switch with NVUE commands and sudo, or have read-only rights. The default privilege level is 15, which provides full administrator access. This is a global option only; you cannot set the minimum privilege level for specific RADIUS servers.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius privilege-level 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius retransmit</h>

Configures the maximum number of retransmission attempts allowed for requests when a RADIUS authentication request times out. This is a global option only; you cannot set the number of retransmission attempts for specific RADIUS servers.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius retransmit 8
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius source-ipv4</h>

Configures the specific interface IPv4 address to reach all RADIUS servers.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius source-ipv4 192.168.1.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius source-ipv6</h>

Configures the specific interface IPv6 address to reach all RADIUS servers.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius source-ipv6 0:0:0:0:0:ffff:c0a8:010a
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius timeout</h>

Configures the global timeout value when servers are slow or latencies are high. You can set a value between 1 and 60. The default timeout is 3 seconds.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius timeout 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius vrf \<vrf-name\></h>

Configures the VRF you want to use to communicate with RADIUS servers. This is typically the management VRF (`mgmt`), which is the default VRF on the switch. You cannot specify more than one VRF.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius vrf mgmt
```
