---
title: Role-Based Access Control
author: NVIDIA
weight: 152
toc: 4
---
In addition to the {{<link url="User-Accounts/#default-roles" text="default roles">}} that Cumulus Linux provides, you can create your own roles to restrict authorization, giving you more granular control over what a user can manage on the switch. For example, you can assign a user the role of network manager and provide the user privileges for interface management, service management and system management. When the user logs in and executes an NVUE command, NVUE checks the user privileges and authorizes the user to run that command.

Custom role-based access control consists of the following elements:

| Element | Description |
| ------- | ----------- |
| Role | A virtual identifier for multiple classes (groups). You can assign only one role for a user. For example, for a user that can manage interfaces, you can create a role called `IFMgr`. |
| Class | A class is similar in concept to a Linux group. Creating and managing classes is the simplest way to configure multiple users simultaneously, especially when configuring permissions. </br></br>A class consists of:<ul><li>Command paths, which are based on the objects in the NVUE declarative model and are the same as URI paths; for example; you can use the `/vrf/` command path to allow or deny a user access to all VRFs, or `/system/nat` to allow or deny a user access to NAT configuration. Use the tab key to see available command paths (`nv set system aaa class <class-name> command-path / <<press tab>>`).<li>Permissions for the command paths: (`ro`) to run show commands, (`rw`) to run set, unset, and apply commands, (`act`) to run action commands, or (`all`) to run all commands. The default permission setting is `all`.</li></ul>|
| Action | The action for the class; `allow` or `deny`.  |

{{%notice note%}}
- You can assign a maximum of 64 classes to a role.
- You can configure a maximum of 128 command paths.
- When you configure a command path, you allow or deny a specific schema path and its children. For example the command path `/qos/` allows or denies access to QoS commands, whereas the command path `/qos/egress-scheduler` allows or denies access to QoS egress scheduler commands.
{{%/notice%}}

The following example describes the permissions for a role (ROLE1) that consists of three classes: Class1, Class2, Class3

**Class1** has the `allow` class action and the following command path permissions:

| Command Path | Permissions |
| ------------ | ----------- |
| `/interface/` | `all`|
| `/interface/*/acl/` | `ro` |
| `/interface/*/ptp/` | `ro` |

**Class2** has the `allow` class action and the following command path permissions:

| Command Path | Permissions |
| ------------ | ----------- |
| `/system/` | `ro` |
| `/vrf/` | `rw` |

**Class3** has the `deny` class action and the following command path permissions:

| Command Path | Permissions |
| ------------ | ----------- |
| `/interface/*/evpn/`| `rw` |
| `/interface/*/qos/` | `rw` |

The following table shows the permissions for a user assigned the role ROLE1. In the table, R is read only (RO), W is write, and X is action (ACT).

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

{{%notice note%}}
You assign a custom role to an existing user account. For information about creating user accounts, see {{<link url="User-Accounts" text="User Accounts">}} commands.
{{%/notice%}}

The following example assigns user1 the role of `switch-admin`. user1 can manage the entire switch except for authentication, authorization, and accounting settings (`system aaa`).

```
cumulus@switch:~$ nv set system aaa role switch-admin class RESTRICT 
cumulus@switch:~$ nv set system aaa class restrict action deny 
cumulus@switch:~$ nv set system aaa class restrict command-path /system/aaa/*/
cumulus@switch:~$ nv set system aaa user user1 role switch-admin
cumulus@switch:~$ nv config apply
```

The following example assigns user2 the role of `IFMgr`. user2 can manage the loopback, management, eth0, and swp1 through 3 interfaces.

```
cumulus@switch:~$ nv set system aaa role IFMgr class InterfaceMgmt_1 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 action allow 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/lo permission all 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/mgmt permission all 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/eth0 permission all 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/swp1 permission all
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/swp2 permission all
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/swp3 permission all
cumulus@switch:~$ nv set system aaa user user2 role IFMgr 
cumulus@switch:~$ nv config apply
```

The following example assigns user3 the role of `OSPF`. user3 does **not** have permissions to manage OSPF on an interface.

```
cumulus@switch:~$ nv set system aaa role OSPF class OSPF-DENY 
cumulus@switch:~$ nv set system aaa class OSPF-DENY action deny 
cumulus@switch:~$ nv set system aaa class OSPF-DENY command-path /interface/*/router/ospf/ permission all
cumulus@switch:~$ nv set system aaa user user3 role OSPF 
cumulus@switch:~$ nv config apply
```

## Delete Custom Roles

To delete a custom role and all its classes, you must first unassign the role from the user, then delete the role:

```
cumulus@switch:~$ nv unset system aaa user user1 role OSPF
cumulus@switch:~$ nv unset system aaa role OSPF
cumulus@switch:~$ nv config apply
```

To delete a class from a role, run the `nv unset system aaa role <role> class <class>` command:

```
cumulus@switch:~$ nv unset system aaa role OSPF class OSPF-DENY
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
user1                                                 OSPF     on             
user2                                                 IFMgr    on             
uucp              uucp                                Unknown  system         
uuidd                                                 Unknown  system         
www-data          www-data                            Unknown  system    
```

To show information about a specific user account including the role assigned to the user, run the NVUE `nv show system aaa user <user>` command:

```
cumulus@switch:~$ nv show system aaa user user2
           operational  applied
---------  -----------  -------
role       IFMgr        IFMgr  
full-name                      
enable     on           on
```

To show all the roles configured on the switch, run the NVUE `nv show system aaa role` command:

```
cumulus@switch:~$ nv show system aaa role
Role          Class          
------------  ---------------
IFMgr         InterfaceMgmt_1
OSPF          OSPF-DENY      
nvue-admin    nvapply        
nvue-monitor  nvshow         
system-admin  nvapply        
              sudo
```

To show the classes applied to specific role, run the `nv show system aaa role <role>` command:

```
cumulus@switch:~$ nv show system aaa role IFMgr
         applied        
-------  ---------------
[class]  InterfaceMgmt_1
```

To show all the classes configured on the switch, run the `nv show system aaa class` command:

```
cumulus@switch:~$ nv show system aaa class
Class Name       Command Path               Permission  Action
---------------  -------------------------  ----------  ------
InterfaceMgmt_1  /interface/eth0/           all         allow 
                 /interface/lo/             all               
                 /interface/mgmt/           all               
                 /interface/swp1/           all               
                 /interface/swp2/           all               
                 /interface/swp3/           all               
OSPF-DENY        /interface/*/router/ospf/  all         deny  
nvapply          /                          all         allow 
nvshow           /                          ro          allow 
sudo             /                          all         allow  
```

To show the configuration and state of the command-paths for a class, run the `nv show system aaa class <class>` command:

```
cumulus@switch:~$ nv show system aaa class OSPF-DENY
                applied                  
--------------  -------------------------
action          deny                     
[command-path]  /interface/*/router/ospf/
```
