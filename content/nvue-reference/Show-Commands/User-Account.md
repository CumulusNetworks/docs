---
title: User Account
author: Cumulus Networks
weight: 430

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show system aaa</h>

Shows a list of the user accounts configured on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa authentication-order</h>

Shows the authentication order for the user accounts configured on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa authentication-order
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa authentication-order \<priority-id\></h>

Shows the authentication order so that TACACS+ authentication has priority over local (the lower number has priority).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`    |  The priority ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa authentication-order 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa role</h>

Shows the roles configured on the switch and the groups to which they belong.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa role
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa role \<role-id\></h>

Shows the permissions allowed for the specified role.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<role-id>`    |  The role ID. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa role nvue-monitor
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa user</h>

Shows the user accounts configured on the switch and their roles.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa user
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa user \<user-id\></h>

Shows information about a specific user account, such as the role and full name.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa user admin2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa user \<user-id\> ssh</h>

Shows SSH information about the specified user account.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa user admin2 ssh
```
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa user \<user-id\> ssh authorized-key</h>

Shows the SSH authorized key for the specified user account.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`    |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa user admin2 ssh authorized-key
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa user \<user-id\> ssh authorized-key \<ssh-authorized-key-id\></h>

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
cumulus@switch:~$ nv show system aaa user admin2 ssh authorized-key prod_key key 1234
```
