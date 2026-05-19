---
title: LDAP
author: Cumulus Networks
weight: 195

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa ldap</h>

Shows all the LDAP configuration settings.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system aaa ldap
                      operational                                          applied                                            
--------------------  ---------------------------------------------------  ---------------------------------------------------
vrf                   default                                              mgmt                                               
bind-dn               CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test  CN=cumulus-admin,CN=Users,DC=rtp,DC=example,DC=test
base-dn               ou=support,dc=rtp,dc=example,dc=test                 ou=support,dc=rtp,dc=example,dc=test               
referrals             yes                                                  off                                                
port                  389                                                  389                                                
timeout-bind          5                                                    5                                                  
timeout-search        5                                                    5                                                  
secret                *                                                    *                                                  
version               3                                                    3                                                  
[hostname]            ldapserver1                                          ldapserver1                                        
ssl                                                                                                                           
  mode                none                                                 none                                               
  port                389                                                  636                                                
  ca-list             default                                              default                                            
  tls-ciphers         all                                                  all                                                
  crl-check           none                                                 none 
...                                              
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa ldap hostname</h>

Shows the hostnames of the LDAP servers and their priorities.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system aaa ldap hostname
Hostname     Priority
-----------  --------
ldapserver1  1
ldapserver2  2  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa ldap hostname \<hostname-id\></h>

Shows the priority for the specified LDAP server hostname.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system aaa ldap hostname ldapserver1
          operational  applied
--------  -----------  -------
priority  1            1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa ldap ssl</h>

Shows the LDAP SSL configuration settings.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system aaa ldap ssl
             operational  applied
-----------  -----------  -------
mode         none         none   
port         389          636    
ca-list      default      default
tls-ciphers  all          all    
crl-check    none         none
```
