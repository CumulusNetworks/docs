---
title: NTP
author: Cumulus Networks
weight: 230

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ntp</h>

Shows the <span class="a-tooltip">[NTP](## "Network Time Protocol")</span> configuration on the switch.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service ntp`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system ntp
           operational                     applied                                                
---------  ------------------------------  ------------------------------ 
reference  local                                                          
offset     25 ms                                                          
status     synchronised                                                   
state      enabled                         enabled                        
vrf        mgmt                            mgmt                           
[server]   0.cumulusnetworks.pool.ntp.org  0.cumulusnetworks.pool.ntp.org 
[server]   1.cumulusnetworks.pool.ntp.org  1.cumulusnetworks.pool.ntp.org 
[server]   2.cumulusnetworks.pool.ntp.org  2.cumulusnetworks.pool.ntp.org 
[server]   3.cumulusnetworks.pool.ntp.org  3.cumulusnetworks.pool.ntp.org 
[listen]   eth0                            eth0                           
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ntp \<vrf-id\></h>

Shows the NTP configuration in the specified VRF.

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` |  The VRF name.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ntp default
          operational                     applied                       
--------  ------------------------------  ------------------------------
[pool]    4.cumulusnetworks.pool.ntp.org  4.cumulusnetworks.pool.ntp.org
[server]  192.168.0.254                   192.168.0.254                 
[server]  time.nist.gov                   time.nist.gov                 
listen    swp10                           swp10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ntp listen</h>

Shows the NTP listen interfaces.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service ntp <vrf-id> listen`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system ntp listen
Interface
---------
eth0   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ntp listen \<interface-id\></h>

Shows specific NTP interface configuration.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv set service ntp <vrf-id> listen <interface-name>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The NTP listen interface.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system ntp listen eth0  
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ntp \<vrf-id\> pool \<server-id\></h>

Shows information about the specified remote NTP server pool.

{{%notice note%}}
Cumulus Linux 5.15 and later no longer supports this command.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ntp default pool 4.cumulusnetworks.pool.ntp.org
        operational  applied
------  -----------  -------
iburst  on           on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ntp server \<server-id\></h>

Shows information about the specified remote NTP server.

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show service ntp <vrf-id> server <server-id>`.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<server-id>` | The hostname or IP address of the NTP server. |

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system ntp server time.nist.gov
                  operational  applied
----------------  -----------  -------
iburst            enabled      enabled
state             enabled      enabled
version           4            4      
association-type  server       server 
```
