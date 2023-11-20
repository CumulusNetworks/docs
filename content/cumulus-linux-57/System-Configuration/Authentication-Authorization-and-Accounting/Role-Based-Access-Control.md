---
title: Role-Based Access Control
author: NVIDIA
weight: 152
toc: 4
---
In addition to the default roles that Cumulus Linux provides, you can create your own roles to restrict authorization, giving you more granular control over what a user can manage on the switch. For example, you can assign a user the role of Network Manager and provide the user privileges for interface management, service management and system management. When the user logs in and executes an NVUE command, NVUE checks the user privileges and authorizes the user to run that command.

Custom role-based access control consists of the following elements:

| Element | Description |
| ------- | ----------- |
| Role | A virtual identifier for multiple classes (groups). You can assign only one role for a user. For example, for a user that can manage interfaces, you can create a role called `IFMgr`. |
| Class | A class is similar in concept to a Linux group. Creating and managing classes is the simplest way to configure multiple users simultaneously, especially when configuring permissions. </br></br>A class consists of:<ul><li>Command paths, which are based on the objects in the NVUE declarative model and are the same as URI paths; for example; you can use the `/vrf/` command path to allow or deny a user access to all VRFs, or `/system/nat` to allow or deny a user access to NAT configuration. Use the tab key to see available command paths (`nv set system aaa class <class-name> command-path <<press tab>>`).<li>Permissions for the command paths: (`ro`) to run show commands, (`rw`) to run set, unset, and apply commands, (`act`) to run action commands, or (`all`) to run all commands. The default permission setting is `all`.</li></ul>|
| Action | The action for the class; `allow` or `deny`.  |

{{%notice note%}}
- You can assign a maximum of 64 classes to a role.
- You can configure a maximum of 128 command paths.
- When you configure a command path, you are authorize a specific schema path and its children.
{{%/notice%}}

## Assign a Custom Role to a User Account

To assign custom role to a user account:
- Assign a role to a user.
- Create classes for the role.
- Add command paths and permissions for each class.
- Assign the action (`allow` or `deny`) for each class.

{{%notice note%}}
You assign a custom role to an existing user account. For information about creating user accounts, see {{<link url="User-Accounts" text="User Accounts">}} commands.
{{%/notice%}}

The following example assigns user1 the role of `switch-admin`. user1 can manage the entire switch except for authentication, authorization, and accounting settings (`system aaa`).

```
cumulus@switch:~$ nv set system aaa user user1 role switch-admin 
cumulus@switch:~$ nv set system aaa role switch-admin class RESTRICT 
cumulus@switch:~$ nv set system aaa class restrict action deny 
cumulus@switch:~$ nv set system aaa class restrict command-path /system/aaa/*/
cumulus@switch:~$ nv config apply
```

The following example assigns user2 the role of `IFMgr`. user2 can manage the loopback, management, eth0, and swp1 through 3 interfaces.

```
cumulus@switch:~$ nv set system aaa user user2 role IFMgr 
cumulus@switch:~$ nv set system aaa role IFMgr class InterfaceMgmt_1 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 action allow 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/lo permission all 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/mgmt permission all 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/eth0 permission all 
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/swp1 permission all
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/swp2 permission all
cumulus@switch:~$ nv set system aaa class InterfaceMgmt_1 command-path /interface/swp3 permission all
cumulus@switch:~$ nv config apply
```

The following example assigns user3 the role of `OSPF`. user3 does **not** have permissions to manage OSPF on an interface.

```
cumulus@switch:~$ nv set system aaa user user3 role OSPF 
cumulus@switch:~$ nv set system aaa role OSPF class OSPF-DENY 
cumulus@switch:~$ nv set system aaa class OSPF-DENY action deny 
cumulus@switch:~$ nv set system aaa class OSPF-DENY command-path /interface/*/router/ospf/ permission all 
cumulus@switch:~$ nv config apply
```

## Show Custom Role Information

To show the user accounts configured on the system, run the NVUE `nv show system aaa user` command or the linux `sudo cat /etc/passwd` command.

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

To show information about a specific user account including the role assigned to the user, run the run the NVUE `nv show system aaa user <user>` command:

```
cumulus@switch:~$ nv show system aaa user admin2
           operational  applied
---------  -----------  -------
role       IFMgr        IFMgr  
full-name                      
enable     on           on
```

To show all the roles configured on the switch:

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

To the classes applied to specific role:

```
cumulus@switch:~$ nv show system aaa role IFMgr
         applied        
-------  ---------------
[class]  InterfaceMgmt_1
```

To show all the classes configured on the switch:

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

To show the configuration and state of the command-paths for a class:

```
cumulus@switch:~$ nv show system aaa class OSPF-DENY
                applied                  
--------------  -------------------------
action          deny                     
[command-path]  /interface/*/router/ospf/
```
