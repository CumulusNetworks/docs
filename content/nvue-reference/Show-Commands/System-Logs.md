---
title: System Logs
author: Cumulus Networks
weight: 405

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log</h>

Shows the current system log configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log
             operational      
-----------  -----------------
[file]       syslog           
[component]  apt              
[component]  audit            
[component]  auth             
[component]  boot             
[component]  csmgr            
[component]  datapath         
[component]  dpkg             
[component]  ifupdown2        
[component]  installer        
[component]  mlag             
[component]  nginx            
[component]  nvue             
[component]  otlp-telemetry   
[component]  platform-phc     
[component]  platform-thermal 
[component]  pps              
[component]  ptm              
[component]  ptp              
[component]  ptp-firefly-servo
[component]  routing          
[component]  stp              
[component]  synce
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log component</h>

Shows the components of the system generating the logs and the log severity levels associated with each component.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$  nv show system log component 
Component          Summary
-----------------  -------
apt                       
audit                     
auth                      
boot                      
csmgr                     
datapath                  
dpkg                      
ifupdown2                 
installer                 
mlag                      
nginx                     
nvue                      
otlp-telemetry            
platform-phc              
platform-thermal          
pps                       
ptm                       
ptp                       
ptp-firefly-servo         
routing                   
stp                       
synce
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log component \<component-name\> file</h>

Shows the contents of the most current file for a specific component. The system uses the less command so that you can scroll through the file interactively.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-name>` | The system component whose log file contents you want to see. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log component nvue file
2025-01-15T11:59:23.648913+00:00 cumulus nvued:    INFO: nvued:214 Starting nvued
2025-01-15T11:59:23.649568+00:00 cumulus nvued:    INFO: nvued:216 NVUE logging set to INFO, chatty deps set to INFO
2025-01-15T11:59:23.650005+00:00 cumulus nvued:    INFO: nvued:171 Attempting to extend the SystemD start/stop timeout on Cumulus/VX platform to 15 minutes
2025-01-15T11:59:23.650327+00:00 cumulus nvued:    INFO: nvued:184 Successfully sent request to SystemD to extend start timeout: True
2025-01-15T11:59:23.692508+00:00 cumulus nvued:    INFO: _access.py:137 Loaded /etc/nvue-auth.yaml
2025-01-15T11:59:23.768857+00:00 cumulus nvued:    INFO: safe_sh.py:108 <Running: '/usr/bin/platform-detect'>
2025-01-15T11:59:23.826070+00:00 cumulus nvued:    INFO: safe_sh.py:195 <Finished: '/usr/bin/platform-detect'>
2025-01-15T11:59:23.826338+00:00 cumulus nvued:    INFO: osinfo.py:298 Platform name vx
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log component \<component-name\> file list</h>

Shows a list of log files for the specified component and shows the associated logs.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-name>` | The system component whose list of log files you want to see. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log component nvue file list
File name    File path           
-----------  --------------------
nv-cli.log   /var/log/nv-cli.log 
nvued.log    /var/log/nvued.log  
nvued.log.1  /var/log/nvued.log.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file</h>

Shows the contents of the most current system log file.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file
2025-01-25T17:28:48.288450+00:00 cumulus systemd-modules-load[322]: Inserted module 'loop'
2025-01-25T17:28:48.288682+00:00 cumulus systemd-modules-load[322]: Inserted module 'bonding'
2025-01-25T17:28:48.288696+00:00 cumulus systemd-random-seed[331]: Kernel entropy pool is not initialized yet, waiting until it is.
2025-01-25T17:28:48.288720+00:00 cumulus systemd-modules-load[322]: Inserted module 'bridge'
2025-01-25T17:28:48.288729+00:00 cumulus systemd-modules-load[322]: Inserted module 'br_netfilter'
2025-01-25T17:28:48.288737+00:00 cumulus systemd-modules-load[322]: Inserted module 'tun'
2025-01-25T17:28:48.288751+00:00 cumulus systemd-modules-load[322]: Inserted module 'at24'
2025-01-25T17:28:48.288759+00:00 cumulus systemd-modules-load[322]: Inserted module 'mpls_router'
2025-01-25T17:28:48.288768+00:00 cumulus systemd-modules-load[322]: Inserted module 'mpls_iptunnel'
2025-01-25T17:28:48.288814+00:00 cumulus systemd[1]: Starting systemd-journal-flush.service - Flush Journal to Persistent Storage...
2025-01-25T17:28:48.288853+00:00 cumulus systemd[1]: modprobe@drm.service: Deactivated successfully.
2025-01-25T17:28:48.288863+00:00 cumulus systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
2025-01-25T17:28:48.288871+00:00 cumulus systemd-modules-load[322]: Inserted module 'vxlan'
2025-01-25T17:28:48.288879+00:00 cumulus systemd-modules-load[322]: Inserted module 'cumulus_vx_platform'
2025-01-25T17:28:48.288887+00:00 cumulus systemd-modules-load[322]: Inserted module 'softdog'
2025-01-25T17:28:48.288900+00:00 cumulus systemd[1]: Finished systemd-modules-load.service - Load Kernel Modules.
2025-01-25T17:28:48.288909+00:00 cumulus systemd-udevd[337]: Using default interface naming scheme 'v252'.
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file \<file-name\></h>

Shows the contents of a specific system log file. If the file is a regular log file (such as syslog.1), the system uses less so that you can scroll and search through the log entries. If the file is compressed (such as syslog.2.gz), the system displays the contents without decompressing the file. This command is useful for viewing both archived and compressed log files.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-name>` | The system log file you want to view. |

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file syslog
2025-01-15T11:59:20.314123+00:00 cumulus systemd-modules-load[322]: Inserted mod
ule 'loop'
2025-01-15T11:59:20.314357+00:00 cumulus systemd-random-seed[331]: Kernel entropy pool is not initialized yet, waiting until it is.
2025-01-15T11:59:20.314386+00:00 cumulus systemd-modules-load[322]: Inserted module 'bonding'
2025-01-15T11:59:20.314396+00:00 cumulus systemd[1]: Starting systemd-journal-flush.service - Flush Journal to Persistent Storage...
2025-01-15T11:59:20.314438+00:00 cumulus systemd[1]: modprobe@drm.service: Deactivated successfully.
2025-01-15T11:59:20.314448+00:00 cumulus systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
2025-01-15T11:59:20.314456+00:00 cumulus systemd-modules-load[322]: Inserted module 'bridge'
2025-01-15T11:59:20.314464+00:00 cumulus systemd-modules-load[322]: Inserted module 'br_netfilter'
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file brief</h>

Shows the contents of the most current system log file in a concise format.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file brief
2025-01-15T11:59:20.314123+00:00 cumulus systemd-modules-load[322]: Inserted module 'loop'
2025-01-15T11:59:20.314357+00:00 cumulus systemd-random-seed[331]: Kernel entropy pool is not initialized yet, waiting until it is.
2025-01-15T11:59:20.314386+00:00 cumulus systemd-modules-load[322]: Inserted module 'bonding'
2025-01-15T11:59:20.314396+00:00 cumulus systemd[1]: Starting systemd-journal-flush.service - Flush Journal to Persistent Storage...
2025-01-15T11:59:20.314438+00:00 cumulus systemd[1]: modprobe@drm.service: Deactivated successfully.
2025-01-15T11:59:20.314448+00:00 cumulus systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
2025-01-15T11:59:20.314456+00:00 cumulus systemd-modules-load[322]: Inserted module 'bridge'
2025-01-15T11:59:20.314464+00:00 cumulus systemd-modules-load[322]: Inserted module 'br_netfilter'
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file follow</h>

Shows the contents of a system log file in real-time. The command shows the log file output continuously as it is updated, similar to the behavior of the `tail -f` command.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file follow
2025-01-16T22:00:08.749566+00:00 leaf01 sshd[17758]: pam_unix(sshd:session): session closed for user cumulus
2025-01-16T22:00:19.589388+00:00 leaf01 sshd[18387]: Accepted publickey for cumulus from 192.168.200.1 port 39400 ssh2: RSA SHA256:l/CnwXBKo6zp1gdL48W0Qpntk4wpJuV0567K+sPF66w
2025-01-16T22:00:19.590984+00:00 leaf01 sshd[18387]: pam_unix(sshd:session): session opened for user cumulus(uid=1000) by (uid=0)
2025-01-16T22:00:19.626551+00:00 leaf01 sshd[18387]: pam_env(sshd:session): deprecated reading of user environment enabled
2025-01-16T22:00:29.900648+00:00 leaf01 sudo:  cumulus : TTY=pts/0 ; PWD=/var/home/cumulus ; USER=root ; COMMAND=/usr/bin/nv show system log file brief
2025-01-16T22:00:30.525635+00:00 leaf01 systemd[1]: mnt-air.mount: Deactivated successfully.
2025-01-16T22:01:00.534717+00:00 leaf01 systemd[1]: mnt-air.mount: Deactivated successfully.
2025-01-16T22:01:30.544233+00:00 leaf01 systemd[1]: mnt-air.mount: Deactivated successfully.
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system log file list</h>

Shows the available system log files on the system with their filenames and corresponding file paths.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system log file list
File name  File path      
---------  ---------------
syslog     /var/log/syslog
```
