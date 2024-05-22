---
title: TACACS
author: Cumulus Networks
weight: 420

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa tacacs</h>

Shows all TACACS+ configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa tacacs
                    applied       
------------------  --------------
enable              on            
source-ip           10.10.10.1    
timeout             10            
vrf                 mgmt          
accounting                        
  enable            off           
  send-records      first-response
authentication                    
  mode              chap          
  per-user-homedir  on            
[authorization]     0             
[exclude-user]      USER1         
[server]            5             
[server]            10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa tacacs accounting</h>

Shows TACACS+ accounting configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa tacacs accounting
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa tacacs authentication</h>

Shows TACACS+ authentication configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa tacacs authentication
              applied       
------------  --------------
enable        off           
send-records  first-response
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa tacacs exclude-user</h>

Shows the list of users excluded from TACACS+ server authentication.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa tacacs exclude-user
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa tacacs server</h>

Shows TACACS+ server configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa tacacs server
   host          port  prefer-ip-version  secret
--  ------------  ----  -----------------  ------
5   192.168.0.30  32    4                  *     
10  192.168.1.30  49    4                  *
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa tacacs server \<priority-id\></h>

Shows TACACS+ server priority configuration on the switch. NVUE commands require you to specify the priority for each TACACS+ server. You must set a priority even if you only specify one server.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<priority-id>`    |  The priority number. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system aaa tacacs server 5
                   applied     
-----------------  ------------
host               192.168.0.30
port               32          
prefer-ip-version  4           
secret             *
```
