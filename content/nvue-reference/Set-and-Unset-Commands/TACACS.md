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

## <h>nv set system aaa tacacs accounting</h>

Configures TACACS+ accounting. TACACS+ accounting uses the `audisp` module, with an additional plugin for `auditd` and `audisp`. The plugin maps the `auid` in the accounting record to a TACACS login, which it bases on the `auid` and `sessionid`.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa tacacs accounting enable</h>

Turns TACACS+ accounting on or off.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs accounting enable on
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

## <h>nv set system aaa tacacs authentication</h>

Configures TACACS+ authentication.

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

Turns per user home directory on or off to create a separate home directory for each TACACS+ user when the TACACS+ user first logs in. The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@switch:~$ nv set system aaa tacacs authentication per-user-homedir on
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

Configures the TACACS server priority number. You must set a priority even if you only specify one server.

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
