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

## nv set system aaa authentication-order \<priority-id\> (tacacs|local)

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

## nv set system aaa tacacs

- - -

## nv set system aaa tacacs authentication

- - -

## nv set system aaa tacacs authentication mode

pap|chap|login)

- - -

## nv set system aaa tacacs authentication per-user-homedir

on|off)

- - -

## nv set system aaa tacacs accounting

- - -

## nv set system aaa tacacs accounting enable

on|off)

- - -

## nv set system aaa tacacs accounting send-records

all|first-response)

- - -

## nv set system aaa tacacs server \<priority-id\>

- - -

## nv set system aaa tacacs server \<priority-id\> host (<idn-hostname\>|<ipv4\>)

- - -

## nv set system aaa tacacs server \<priority-id\> port 0-65535

- - -

## nv set system aaa tacacs server \<priority-id\> secret \<value\>

- - -

## nv set system aaa tacacs exclude-user

- - -

## nv set system aaa tacacs exclude-user username \<value\>

- - -

## nv set system aaa tacacs enable 

(on|off)

- - -

## nv set system aaa tacacs timeout

0-60

- - -

## nv set system aaa tacacs debug-level

0-2

- - -

## nv set system aaa tacacs source-ip \<ipv4\>

- - -

## nv set system aaa tacacs vrf \<vrf-name\>

- - -
