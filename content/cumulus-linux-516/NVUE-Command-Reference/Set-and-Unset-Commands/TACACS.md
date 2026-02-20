---
title: TACACS
author: Cumulus Networks
weight: 780

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs accounting state</h>

Enables and disables TACACS+ accounting.

TACACS+ accounting uses the `audisp` module, with an additional plugin for `auditd` and `audisp`. The plugin maps the `auid` in the accounting record to a TACACS login, which it bases on the `auid` and `sessionid`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `enable on` or `enable off` instead of `state enabled` or `state disabled`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs accounting state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs accounting send-records</h>

Configures Cumulus Linux to send accounting records to all servers (`all`) or to the server that is first to respond (`first-response`). By default, Cumulus Linux sends accounting records to all servers.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs accounting send-records first-response
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs authentication mode</h>

Configures the TACACS+ authentication mode. You can specify `pap` to send clear text between the user and the server, `chap` to establish a PPP connection between the user and the server, or `login`. The default is `pap`.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs authentication mode chap
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa authentication-order \<priority-id\></h>

Configures the authentication order so that either TACACS+ or local authentication has priority (the lower number has priority). You can specify a value of `tacacs` or `local`.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa authentication-order 1 tacacs
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs authentication per-user-homedir</h>

Enables and disables per user home directory to create a separate home directory for each TACACS+ user when the TACACS+ user first logs in. The default setting is `disabled`.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, you specify `on` or `off`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs authentication per-user-homedir enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs debug-level</h>

Configures the debugging level for troubleshooting:
- 0 disables debugging.
- 1 enables debugging and sends log messages to syslog.
- 2 enables debugging and sends some additional log messages to syslog.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa tacacs debug-level 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs enable</h>

Turns TACACS+ on or off.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs exclude-user</h>

Configures TACACS to exclude users from going to the TACACS+ server for authentication.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs exclude-user username \<value\></h>

Configures TACACS to exclude the specified user from going to the TACACS+ server for authentication.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `value>`  | The name of the user account you want to exclude. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs exclude-user user1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<priority-id\></h>

Configures the TACACS server priority number. You must set a priority even if you only specify one server. You can specify a value between 1 and 8.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command; Use `nv set system aaa tacacs server <server-id> priority <priority>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<priority-id\> host</h>

Configures the IPv4 address or hostname of the TACACS+ server. You must configure at least one TACACS+ server.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command; Use `nv set system aaa tacacs server <server-id> priority <priority>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 5 host 192.168.0.30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<priority-id\> port</h>

Configures the TACACS+ server port to use for communication between the TACACS+ server and client. You can set a value between 0 and 65535. The default port is 49.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command; Use `nv set system aaa tacacs server <server-id> port <port-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  |  The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 5 port 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<priority-id\> prefer-ip-version 6</h>

Configures the TACACS server to use IPv6.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command; Use `nv set system aaa tacacs server <server-id> prefer-ip-version 6`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  |  The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 5 prefer-ip-version 6 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<priority-id\> secret \<value\></h>

Configures the shared secret between the TACACS server and client. The TACACS client on the switch and the TACACS server must have the same shared secret key.

{{%notice note%}}
Cumulus Linux 5.12 and later does not provide this command; Use `nv set system aaa tacacs server <server-id> secret <secret>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 5 secret mytacacskey
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<server-id\> port \<port-id\></h>

Configures the port number you want to use for communication between the TACACS+ server and client. By default, Cumulus Linux uses IP port 49.

{{%notice note%}}
Cumulus Linux 5.11 and earlier uses `nv set system aaa tacacs server <priority-id> port <port-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-id>`  | The TACACS server IP address or hostname. |
| `<port-id>`  | The port number. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 192.168.0.30 port 32
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<server-id\> priority \<priority-id\></h>

Configures the TACACS server priority number. You must set a priority even if you only specify one server.

{{%notice note%}}
Cumulus Linux 5.11 and earlier uses `nv set system aaa tacacs server <priority-id> host <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-id>`  | The TACACS server IP address or hostname. |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 192.168.0.30 priority 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<server-id\> secret \secret-key\></h>

Configures the TACACS server secret key shared between the TACACS+ server and client.

{{%notice note%}}
Cumulus Linux 5.11 and earlier uses `nv set system aaa tacacs server <priority> secret <secret-key>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-id>`  | The TACACS server IP address or hostname. |
| `<secret-key>`  | The TACACS server secret key. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server 192.168.0.30 secret abcdefghijklmnopqrstuvwxyz
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs server \<server-id\> prefer-ip-version 6</h>

Configures the TACACS server to use IPv6.

{{%notice note%}}
Cumulus Linux 5.11 and earlier uses `nv set system aaa tacacs server <priority-id> prefer-ip-version 6`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-id>`  |  The TACACS server IP address or hostname. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv set system aaa tacacs server SERVER1 prefer-ip-version 6 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs source-ip \<ipv4\></h>

Configures the source IP address to use when communicating with the TACACS+ server so that the server can identify the client switch. You must specify an IPv4 address, which must be valid for the interface you use. This source IP address is typically the loopback address on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `ipv4>`  | The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs source-ip 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs timeout</h>

Configures the TACACS timeout value, which is the number of seconds to wait for a response from the TACACS+ server before trying the next TACACS+ server. You can specify a value between 0 and 60.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs timeout 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs vrf \<vrf-name\></h>

Configures the VRF you want to use to communicate with the TACACS+ server. This is typically the management VRF (`mgmt`).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `vrf-name>`  | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs vrf mgmt
```
