---
title: Role-Based Access Control
author: NVIDIA
weight: 152
toc: 4
---
In addition to the {{<link url="User-Accounts/#default-roles" text="default roles">}} that Cumulus Linux provides, you can create your own roles to restrict authorization, giving you more granular control over what a user can manage on the switch. For example, you can assign a user the role of network manager and provide the user privileges for interface management, service management and system management. When the user logs in and executes an NVUE command, NVUE checks the user privileges and authorizes the user to run that command.

Custom role-based access control consists of the following elements:
<!-- vale off -->
| Element | Description |
| ------- | ----------- |
| Role | A virtual identifier for multiple classes (groups). You can assign only one role for a user. For example, for a user that can manage interfaces, you can create a role called `IFMgr`. |
| Class | A class is similar in concept to a Linux group. Creating and managing classes is the simplest way to configure multiple users simultaneously, especially when configuring permissions.</br></br>A class consists of:<ul><li>Command paths, which Cumulus Linux bases on the objects in the NVUE declarative model and, which are the same as URI paths; for example; you can use the `/vrf/` command path to allow or deny a user access to all VRFs, or `/system/nat` to allow or deny a user access to NAT configuration. Use the tab key to see available command paths (`nv set system aaa class <class-name> command-path / <<press tab>>`).<li>Permissions for the command paths: (`ro`) to run show commands, (`rw`) to run set, unset, and apply commands, (`act`) to run action commands, or (`all`) to run all commands. The default permission setting is `all`.</li></ul>|
| Action | The action for the class: `allow` or `deny`.  |
<!-- vale on -->
{{%notice note%}}
- You can assign a maximum of 64 classes to a role.
- You can configure a maximum of 128 command paths for a class.
- When you configure a command path, you allow or deny a specific schema path and its children. For example the command path `/qos/` allows or denies access to QoS commands, whereas the command path `/qos/egress-scheduler` allows or denies access to QoS egress scheduler commands.
{{%/notice%}}

The following example describes the permissions for a role (`role1`) that consists of three classes: `class1`, `class2`, `class3`

**class1** has the `allow` class action and the following command path permissions:

| Command Path | Permissions |
| ------------ | ----------- |
| `/interface/` | `all`|
| `/interface/*/acl/` | `ro` |
| `/interface/*/ptp/` | `ro` |

**class2** has the `allow` class action and the following command path permissions:

| Command Path | Permissions |
| ------------ | ----------- |
| `/system/` | `ro` |
| `/vrf/` | `rw` |

**class3** has the `deny` class action and the following command path permissions:

| Command Path | Permissions |
| ------------ | ----------- |
| `/interface/*/evpn/`| `rw` |
| `/interface/*/qos/` | `rw` |
<!-- vale off -->
The following table shows the permissions for a user assigned the role `role1`. In the table, R is read only (RO), W is write, and X is action (ACT).
<!-- vale on -->
| Path     | Allow     | Deny       | Permissions |
| -------- | --------- | ---------- | ----------- |
| `/acl/` |            | RWX        | Implicit deny |
| `/qos/`  |           | RWX        | Implicit deny |
| All unspecified paths are implicit deny | | | |
| `/interface/` | RWX |  | The permissions specified |
| `/interface/*` (* matches all interfaces) | | RWX | Inherited from parent |
| `/interface/*/bond/` | RWX | | Inherited from parent |
| `/interface/*/ip/` | RWX | | Inherited from parent |
| All unspecified children of `/interface/` inherit parent permissions | RWX| | |
| `/interface/*/acl/` | R | WX | The permissions specified |
| `/interface/*/ptp/` | R |	WX | The permissions specified |
| `/interface/*/evpn/` | | RWX | The permissions specified |
| `/interface/*/qos/` | | RWX | The permissions specified |
| `/system/` | R | WX | The permissions specified |
| `/system/aaa/` | R | WX |Inherited from parent|
| `/system/api/` | R | WX |Inherited from parent|
| All unspecified children of `/system/` inherit parent permissions | R | | |
| `/vrf/` | RW | X | The permissions specified |
| All unspecified children of `/vrf/` inherit parent permissions| RW | X | |

## Assign a Custom Role to a User Account

To assign a custom role to a user account:
- Create a role and classes for the role.
- Assign the action (allow or deny) for each class.
- Add command paths and permissions for each class.
- Assign a role to a user.

You assign a custom role to an existing user account. For information about creating user accounts, see {{<link url="User-Accounts" text="User Accounts">}} commands.

{{%notice info%}}
When you create a class, then run `nv config apply`, NVUE removes LDAP configuration from the `/etc/nsswitch.conf` file. If you are using LDAP, run the `nv set system config apply ignore /etc/nsswitch.conf` command **before** you run `nv config apply` to retain the LDAP configuration.
{{%/notice%}}

The following example creates the three classes described above for role `role1`.

`class1` has permissions to manage all interfaces except for ACL and PTP interfaces, which only have `show` permissions:

```
cumulus@leaf01:mgmt:~$ nv set system aaa role ROLE1 class class1
cumulus@leaf01:mgmt:~$ nv set system aaa class class1 action allow
cumulus@leaf01:mgmt:~$ nv set system aaa class class1 command-path /interface/ permission all   
cumulus@leaf01:mgmt:~$ nv set system aaa class class1 command-path /interface/*/acl/ permission ro
cumulus@leaf01:mgmt:~$ nv set system aaa class class1 command-path /interface/*/ptp/ permission ro
cumulus@leaf01:mgmt:~$ nv config apply
```

`class2` has permissions to only show system commands and to set, unset, and apply VRF commands:

```
cumulus@leaf01:mgmt:~$ nv set system aaa role ROLE1 class class2
cumulus@leaf01:mgmt:~$ nv set system aaa class class2 action allow
cumulus@leaf01:mgmt:~$ nv set system aaa class class2 command-path /system/ permission ro
cumulus@leaf01:mgmt:~$ nv set system aaa class class2 command-path /vrf/ permission rw
cumulus@leaf01:mgmt:~$ nv config apply
```

`class3` prevents setting, unsetting, and applying interface commands for EVPN and QOS:

```
cumulus@leaf01:mgmt:~$ nv set system aaa role ROLE1 class class3
cumulus@leaf01:mgmt:~$ nv set system aaa class class3 action deny
cumulus@leaf01:mgmt:~$ nv set system aaa class class3 command-path /interface/*/evpn/ permission rw
cumulus@leaf01:mgmt:~$ nv set system aaa class class3 command-path /interface/*/qos/ permission rw
cumulus@leaf01:mgmt:~$ nv config apply
```

The following command assigns user `admin2` the role `role1`:

```
cumulus@leaf01:mgmt:~$ nv set system aaa user admin2 role role1
cumulus@leaf01:mgmt:~$ nv config apply
```

## Delete Custom Roles

To delete a custom role and all its classes, you must first unassign the role from the user, then delete the role:

```
cumulus@switch:~$ nv unset system aaa user admin2 role role1
cumulus@switch:~$ nv unset system aaa role role1
cumulus@switch:~$ nv config apply
```

To delete a class from a role, run the `nv unset system aaa role <role> class <class>` command:

```
cumulus@switch:~$ nv unset system aaa role role1 class class2
cumulus@switch:~$ nv config apply
```

## Show Custom Role Information

To show the user accounts configured on the system, run the NVUE `nv show system aaa user` command or the Linux `sudo cat /etc/passwd` command.

```
cumulus@switch:~$ nv show system aaa user
Username          Full-name                           Role     enable  Summary
----------------  ----------------------------------  -------  ------  -------
_apt                                                  Unknown  system         
_lldpd                                                Unknown  system         
backup            backup                              Unknown  system         
bin               bin                                 Unknown  system         
cumulus           cumulus,,,                          Unknown  on             
daemon            daemon                              Unknown  system         
dnsmasq           dnsmasq,,,                          Unknown  system         
frr               Frr routing suite,,,                Unknown  system         
games             games                               Unknown  system         
gnats             Gnats Bug-Reporting System (admin)  Unknown  system         
irc               ircd                                Unknown  system         
list              Mailing List Manager                Unknown  system         
lp                lp                                  Unknown  system         
mail              mail                                Unknown  system         
man               man                                 Unknown  system         
messagebus                                            Unknown  system         
news              news                                Unknown  system         
nobody            nobody                              Unknown  off            
ntp                                                   Unknown  system         
nvue              NVIDIA User Experience              Unknown  system         
proxy             proxy                               Unknown  system         
root              root                                Unknown  system         
snmp                                                  Unknown  system         
sshd                                                  Unknown  system         
sync              sync                                Unknown  system         
sys               sys                                 Unknown  system         
systemd-coredump  systemd Core Dumper                 Unknown  system         
systemd-network   systemd Network Management,,,       Unknown  system         
systemd-resolve   systemd Resolver,,,                 Unknown  system         
systemd-timesync  systemd Time Synchronization,,,     Unknown  system         
admin2                                                role1    on             
uucp              uucp                                Unknown  system         
uuidd                                                 Unknown  system         
www-data          www-data                            Unknown  system    
```

To show information about a specific user account including the role assigned to the user, run the NVUE `nv show system aaa user <user>` command:

```
cumulus@switch:~$ nv show system aaa user admin2
           operational  applied
---------  -----------  -------
role       role1        role1  
full-name                      
enable     on           on
```

To show all the roles configured on the switch, run the NVUE `nv show system aaa role` command:

```
cumulus@switch:~$ nv show system aaa role
Role          Class  
------------  -------
nvue-admin    nvapply
nvue-monitor  nvshow 
role1         class1 
              class2 
              class3 
system-admin  nvapply
              sudo
```

To show the classes applied to specific role, run the `nv show system aaa role <role>` command:

```
cumulus@switch:~$ nv show system aaa role role1
         applied
-------  -------
[class]  class1 
[class]  class2 
[class]  class3
```

To show all the classes configured on the switch, run the `nv show system aaa class` command:

```
cumulus@switch:~$ nv show system aaa class
Class Name  Command Path        Permission  Action
----------  ------------------  ----------  ------
class1      /interface/         all         allow 
            /interface/*/acl/   ro                
            /interface/*/ptp/   ro                
class2      /system/            ro          allow 
            /vrf/               rw                
class3      /interface/*/evpn/  rw          deny  
            /interface/*/qos/   rw                
nvapply     /                   all         allow 
nvshow      /                   ro          allow 
sudo        /                   all         allow 
```

To show the configuration and state of the command paths for a class, run the `nv show system aaa class <class>` command:

```
cumulus@switch:~$ nv show system aaa class class3
               applied           
--------------  ------------------
action          deny              
[command-path]  /interface/*/evpn/
[command-path]  /interface/*/qos/
```
