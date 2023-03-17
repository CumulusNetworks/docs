---
title: TACACS Commands
author: Cumulus Networks
weight: 380
product: Cumulus Linux
type: nojsscroll
---
## nv show system aaa tacacs

Shows all TACACS+ configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa tacacs
```

- - -

## nv show system aaa tacacs accounting

Shows TACACS+ accounting configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa tacacs accounting
```

- - -

## nv show system aaa tacacs authentication

Shows TACACS+ authentication configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa tacacs authentication
```

- - -

## nv show system aaa tacacs exclude-user

Shows the list of users excluded from TACACS+ server authentication.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa tacacs exclude-user
```


## nv show system aaa tacacs server

Shows TACACS+ server configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa tacacs server
```

- - -

## nv show system aaa tacacs server \<priority-id\>

Shows TACACS+ server priority configuration on the switch. NVUE commands require you to specify the priority for each TACACS+ server. You must set a priority even if you only specify one server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`    |  The priority number. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa tacacs server 5
```

- - -
