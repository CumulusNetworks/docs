---
title: User Account
author: Cumulus Networks
weight: 790

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa class \<class-id\></h>

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<class-id>`    |  The name of the class. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
nv set system aaa class class1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa class \<class-id\> action</h>

Configures the `allow` or `deny` action for the specified class.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<class-id>`    |  The name of the class. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa class class2 action allow
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa class \<class-id\> command-path \<command-path-id\></h>

Configures the command path for the specified class.

Command paths, which Cumulus Linux bases on the objects in the NVUE declarative model and, which are the same as URI paths; for example; you can use the `/vrf/` command path to allow or deny a user access to all VRFs, or `/system/nat` to allow or deny a user access to NAT configuration. Use the tab key to see available command paths (`nv set system aaa class <class-name> command-path / <<press tab>>`).

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<class-id>`    |  The name of the class. |
| `<command-path-id>`  |  The command path. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa class class1 command-path /interface/ 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa class \<class-id\> command-path \<command-path-id\> permission</h>

Configures the permissions for the command path for the specified class.

You can specify `ro` to run show commands, `rw` to run set, unset, and apply commands, `act` to run action commands, or `all` to run all commands. The default permission setting is `all`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<class-id>`    |  The name of the class. |
| `<command-path-id>`  |  The name of the class. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa class class1 command-path /interface/*/acl/ permission ro
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa role \<role-id\></h>

Configues a role. A role is a virtual identifier for multiple classes (groups). You can assign only one role for a user. For example, for a user that can manage interfaces, you can create a role called `IFMgr`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<role-id>` |  The name of the role. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa role ROLE1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa role \<role-id\> class \<class-id\></h>

Assigns the specified class to the role.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<role-id>` |  The name of the role. |
| `<class-id>`    |  The name of the class. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv set system aaa role ROLE1 class class1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa user \<user-id\> enable</h>

Turns the user account for the switch on or off.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa user admin2 enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa user \<user-id\> full-name \<value\></h>

Configures the full name for the specified user account. If the full name includes more than one name, either separate the names with a hyphen (FIRST-LAST) or enclose the full name in quotes ("FIRST LAST").

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa user admin2 full-name "FIRST LAST"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa user \<user-id\> hashed-password</h>

Configures a hashed text password for the specified user account. You must specify the hashed password in Linux crypt format; the password must be a minimum of 15 to 20 characters long and must include special characters, digits, lower case alphabetic letters, and more.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa user admin2 hashed-password '$1$/ETjhZMJ$P73qhBZEYP20mKnRkhBol0'
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa user \<user-id\> password</h>

Configures a plain text password for the specified user account by prompting you to enter a new password and to confirm the password.

You can also run the `nv set system aaa user <user-id> password <plain-text-password>` command to specify the plain text password inline. This command bypasses the Enter new password and Confirm password prompts but displays the plain text password as you type it.

NVUE hashes the plain text password and stores the value as a hashed password.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa user admin2 password
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system aaa user \<user-id\> role</h>

Configures the role for the user accounts configured on the switch and the groups to which they belong. You can specify `system-admin`, `nvue-admin`, and `nvue-monitor`.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<user-id>`  |  The user account. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system aaa user admin2 nvue-monitor
```
