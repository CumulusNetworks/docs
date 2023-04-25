---
title: TACACS
author: Cumulus Networks
weight: 780
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set system aaa authentication-order \<priority-id\>

Configures the authentication order so that either TACACS+ or local authentication has priority (the lower number has priority). You can specify a value of `tacacs` or `local`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa authentication-order 1 tacacs
```

- - -

## nv set system aaa tacacs accounting

Configures TACACS+ accounting. TACACS+ accounting uses the `audisp` module, with an additional plugin for `auditd` and `audisp`. The plugin maps the `auid` in the accounting record to a TACACS login, which it bases on the `auid` and sessionid.

- - -

## nv set system aaa tacacs accounting enable

Turns TACACS+ accounting on or off.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs accounting enable on
```

- - -

## nv set system aaa tacacs accounting send-records

Configures Cumulus Linux to send accounting records to all servers (`all`) or to the server that is first to respond (`first-response`). By default, Cumulus Linux sends accounting records to all servers.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs accounting send-records first-response
```

- - -

## nv set system aaa tacacs authentication

Configures TACACS+ authentication.

- - -

## nv set system aaa tacacs authentication mode

Configures the TACACS+ authentication mode. You can specify `pap` to send clear text between the user and the server, `chap` to establish a PPP connection between the user and the server, or `login`. The default is `pap`.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs authentication mode chap
```

- - -

## nv set system aaa tacacs authentication per-user-homedir

Turns per user home directory on or off to create a separate home directory for each TACACS+ user when the TACACS+ user first logs in. The default setting os `off`.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs authentication per-user-homedir on
```

- - -

## nv set system aaa tacacs debug-level

Configures the debugging level for troubleshooting. You can specify a value between 0 and 2.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs debug-level 2
```

- - -

## nv set system aaa tacacs enable

Turns TACACS+ on or off.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs enable on
```

- - -

## nv set system aaa tacacs exclude-user

Configures TACACS to exclude users from going to the TACACS+ server for authentication.

- - -

## nv set system aaa tacacs exclude-user username \<value\>

Configures TACACS to exclude a user from going to the TACACS+ server for authentication.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `value>`  | The name of the user account you want to exclude. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs exclude-user user1
```

- - -

## nv set system aaa tacacs server \<priority-id\>

Configures the TACACS server priority number. You must set a priority even if you only specify one server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs server 5
```

- - -

## nv set system aaa tacacs server \<priority-id\> host

Configures the IPv4 address or hostname of at least one TACACS+ server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs server 5 host 192.168.0.30
```

- - -

## nv set system aaa tacacs server \<priority-id\> port

Configures the TACACS+ server port to use for communication between the TACACS+ server and client. You can set a value between 0 and 65535. The default port is 49.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  |  The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs server 5 port 32
```

- - -

## nv set system aaa tacacs server \<priority-id\> prefer-ip-version 6

Configures the TACACS server to use IPv6.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  |  The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs server 5 prefer-ip-version 6 
```

- - -

## nv set system aaa tacacs server \<priority-id\> secret \<value\>

Configures the shared secret between the TACACS server and client. The TACACS client on the switch and the TACACS server must have the same shared secret key.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`  | The TACACS server priority number. NVUE commands require you to specify the priority for each TACACS+ server. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs server 5 secret mytacacskey
```

- - -

## nv set system aaa tacacs source-ip \<ipv4\>

Configures the source IP address to use when communicating with the TACACS+ server so that the server can identify the client switch. You must specify an IPv4 address, which must be valid for the interface you use. This source IP address is typically the loopback address on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `ipv4>`  | The IPv4 address. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs source-ip 10.10.10.1
```

- - -

## nv set system aaa tacacs timeout

Configures the TACACS timeout value, which is the number of seconds to wait for a response from the TACACS+ server before trying the next TACACS+ server. You can specify a value between 0 and 60.

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs timeout 10
```

- - -

## nv set system aaa tacacs vrf \<vrf-name\>

Configures the VRF you want to use to communicate with the TACACS+ server. This is typically the management VRF (`mgmt`).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `vrf-name>`  | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.4.0 (beta)

### Example

```
cumulus@leaf01:mgmt:~$ nv set system aaa tacacs vrf mgmt
```

- - -
