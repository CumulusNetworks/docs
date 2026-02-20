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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius accounting send-records</h>

Configures where to send accounting records. By default, Cumulus Linux sends accounting records to all servers. You can change this setting to send accounting records to the server that is first to respond. If the first available server does not respond, Cumulus Linux continues trying down the list of servers (by priority) until one is reachable. If none of the servers are reachable, there is a 30-second timeout, after which Cumulus Linux retries the servers. After 10 failed retries, the switch drops the packet.

You can specify `first-response` or `all`.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa radius accounting send-records first-response
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius accounting state</h>

Enables RADIUS user command accounting, which lets you log every command that a user runs and send the commands to the RADIUS servers for auditing. Audit logs are a requirement for compliance standards, such as PCI and HIPPA.

You can specify `enabled` or `disabled`.

The RADIUS servers must be configured to accept packets from clients and have a dictionary entry for NV-Command-String.

The `/var/log/radius-cmd-acct.log` file contains the local copy of the logs, which match the logs that the servers receive.

{{%notice note%}}
In cumulus Linux 5.11 and earlier you can only send the commands to the primary RADIUS server. Cumulus Linux 5.12 and later supports more than one RADIUS server.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv set system aaa radius accounting state enabled
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

{{%notice note%}}
Cumulus Linux 5.12 and later no longer provides this command.
{{%/notice%}}

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

## <h>nv set system aaa radius require-message-authenticator</h>

Requires authentication packets to have the Message-Authenticator mode attribute; the switch discards as Access-Reject all packets that do not have the Message-Authenticator attribute. You can specify `enabled` or `disabled`.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system aaa radius require-message-authenticator enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\></h>

Configures the IP address or hostname of the RADIUS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\> port</h>

Configures the port used to communicate with the specified RADIUS Server. A port is optional. You can set a value between 0 and 65535. The default value is 1812.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 port 42
```

 <HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\> priority</h>

Configures the priority at which Cumulus Linux contacts the specified RADIUS server for load balancing. You can set a value between 1 and 100. The lower value is the higher priority.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 priority 10
```

 <HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\> secret</h>

Configures the secret key shared between the specified RADIUS server and client. If you include special characters in the key (such as `$`), you must enclose the key in single quotes (').

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 secret 'myradius$key'
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\> source-ip</h>

Configures the specific interface IPv4 or IPv6 address you want to use to reach the RADIUS server. If you configure multiple RADIUS servers, you can configure a specific interface to reach all RADIUS servers with the `nv set system aaa radius source-ip` command, described below.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 source-ip 192.168.1.10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\> timeout</h>

Configures the timeout value when a server is slow or latencies are high. You can set a value between 1 and 60. The default timeout is 3 seconds. If you configure multiple RADIUS servers, you can set a global timeout for all servers with the `nv set system aaa radius timeout` command.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 timeout 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa radius server \<server-id\> vrf \<vrf-id\></h>

Sets the VRF you want to use for the RADIUS server (if you use multiple RADIUS servers).

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<server-id>` | The IP address or hostname of the RADIUS server. |
| `<vrf-id>` | The VRF you want to use for the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system aaa radius server 192.168.0.254 vrf mgmt
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

Configures the global VRF you want to use to communicate with RADIUS servers. This is typically the management VRF (`mgmt`), which is the default VRF on the switch.

To specify a different VRF for each RADIUS server, use the `nv set system aaa radius server <server-id> vrf <vrf-id>` command (available in Cumulus Linux 5.13 and later).

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa radius vrf mgmt
```
