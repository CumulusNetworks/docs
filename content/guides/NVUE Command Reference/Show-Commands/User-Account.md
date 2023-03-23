---
title: User Account
author: Cumulus Networks
weight: 430
product: Cumulus Linux
type: nojsscroll
---
## nv show system aaa

Shows a list of the user accounts configured on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa
```

- - -

## nv show system aaa authentication-order

Shows the authentication order for the user accounts configured on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa authentication-order
```

- - -

## nv show system aaa authentication-order \<priority-id\>

Shows the authentication order so that TACACS+ authentication has priority over local (the lower number has priority).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`    |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa authentication-order 5
```

- - -

## nv show system aaa role

Shows the roles configured on the switch and the groups to which they belong.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa role
```

- - -

## nv show system aaa role \<role-id\>

Shows the permissions allowed for the specified role.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<role-id>`    |  The role ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa role nvue-monitor
```

- - -

## nv show system aaa user

Shows the user accounts configured on the switch and their roles.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa user
```

- - -

## nv show system aaa user \<user-id\>

Shows information about a specific user account, such as the role and full name.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa user admin2
```

- - -

## nv show system aaa user \<user-id\> ssh

Shows SSH information about the specified user account.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa user admin2 ssh
```
- - -

## nv show system aaa user \<user-id\> ssh authorized-key

Shows the SSH authorized key for the specified user account.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa user admin2 ssh authorized-key
```

- - -

## nv show system aaa user \<user-id\> ssh authorized-key \<ssh-authorized-key-id\>

Shows information about a specific SSH authorized key for the specified user account.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |
| `<ssh-authorized-key-id>`    |  The SSH authorized key ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system aaa user admin2 ssh authorized-key prod_key key 1234
```

- - -
