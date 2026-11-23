---
title: Log Files with NVUE
author: NVIDIA
weight: 145
toc: 3
---
NVUE provides commands to show the current system logging configuration, show the contents of the log files on the switch, and to delete log files.

## Show System Logging Configuration

To show the current system log configuration on the switch, run the `nv show system log` command:

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

## Show System Log Files

To show the contents of the most current system log file, run the `nv show system log file` command:

```
cumulus@switch:~$ nv show system log file
2025-01-15T11:59:20.314123+00:00 cumulus systemd-modules-load[322]: Inserted module 'loop'
2025-01-15T11:59:20.314357+00:00 cumulus systemd-random-seed[331]: Kernel entropy pool is not initialized yet, waiting until it is.
2025-01-15T11:59:20.314386+00:00 cumulus systemd-modules-load[322]: Inserted module 'bonding'
2025-01-15T11:59:20.314396+00:00 cumulus systemd[1]: Starting systemd-journal-flush.service - Flush Journal to Persistent Storage...
2025-01-15T11:59:20.314438+00:00 cumulus systemd[1]: modprobe@drm.service: Deactivated successfully.
2025-01-15T11:59:20.314448+00:00 cumulus systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
2025-01-15T11:59:20.314456+00:00 cumulus systemd-modules-load[322]: Inserted module 'bridge'
2025-01-15T11:59:20.314464+00:00 cumulus systemd-modules-load[322]: Inserted module 'br_netfilter'
2025-01-15T11:59:20.314472+00:00 cumulus systemd[1]: Finished systemd-journal-flush.service - Flush Journal to Persistent Storage.
2025-01-15T11:59:20.314486+00:00 cumulus systemd-modules-load[322]: Inserted module 'tun'
2025-01-15T11:59:20.314494+00:00 cumulus systemd-modules-load[322]: Inserted module 'at24'
2025-01-15T11:59:20.314502+00:00 cumulus systemd[1]: Finished systemd-random-see/var/log/syslog
...
```

The `nv show system log file` command provides the following options:

| Option  | Description |
| ------- | ----------- |
| `brief` | Shows the contents of the most current system log file but in a more concise format. |
| `follow`| Shows the contents of a system log file in real time.  The command shows the log file output continuously as it updates, similar to the `tail -f` command.|
| `list` |  Shows the available system log files on the system with their filenames and corresponding file paths. |
| `<file-name>`|  Shows the contents of a specific system log file. |

The following example shows the contents of the most current system log file:

```
cumulus@switch:~$ nv show system log file
2025-01-15T11:59:20.314123+00:00 cumulus systemd-modules-load[322]: Inserted module 'loop'
2025-01-15T11:59:20.314357+00:00 cumulus systemd-random-seed[331]: Kernel entropy pool is not initialized yet, waiting until it is.
2025-01-15T11:59:20.314386+00:00 cumulus systemd-modules-load[322]: Inserted module 'bonding'
2025-01-15T11:59:20.314396+00:00 cumulus systemd[1]: Starting systemd-journal-flush.service - Flush Journal to Persistent Storage...
2025-01-15T11:59:20.314438+00:00 cumulus systemd[1]: modprobe@drm.service: Deactivated successfully.
2025-01-15T11:59:20.314448+00:00 cumulus systemd[1]: Finished modprobe@drm.service - Load Kernel Module drm.
2025-01-15T11:59:20.314456+00:00 cumulus systemd-modules-load[322]: Inserted module 'bridge'
2025-01-15T11:59:20.314464+00:00 cumulus systemd-modules-load[322]: Inserted module 'br_netfilter'
2025-01-15T11:59:20.314472+00:00 cumulus systemd[1]: Finished systemd-journal-flush.service - Flush Journal to Persistent Storage.
2025-01-15T11:59:20.314486+00:00 cumulus systemd-modules-load[322]: Inserted module 'tun'
2025-01-15T11:59:20.314494+00:00 cumulus systemd-modules-load[322]: Inserted module 'at24'
...
```

The following example shows the contents of the most current system log file in a more concise format:

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

The following example shows the contents of the most current system log file in real-time:

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

The following example shows the available system log files on the system with their filenames and corresponding file paths:

```
cumulus@switch:~$ nv show system log file list
File name  File path      
---------  ---------------
syslog     /var/log/syslog
```

The following example shows the contents of the `syslog` file:

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

## Show Components Generating the Logs

To show the components of the system generating the logs, run the `nv show system log component` command.

```
cumulus@switch:~$ nv show system log component 
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

The `nv show system log component` command provides the following options:

| Option  | Description |
| ------- | ----------- |
| `<component-name> file` | Shows the contents of the most current file for a specific component. |
|  `<component-name> file list` | Provides a list of log files for the specified component and shows the associated logs.|

{{< expand "Component File List" >}}
| System Component  | Files |
| ---------- | ----------- |
| `apt` | All files in the `/var/log/apt` directory. The most current file is `history.log`. |
| `audit` | All files in the `/var/log/audit` directory.|
| `auth` | `auth.log` |
| `boot` | `boot.log`|
| `csmgr` | `csmgrd.log`, `cl-system-services.log` |
| `datapath` | `mswitchd.log` |
| `dpkg` | All files in the `/var/log/dpkg` directory. |
| `ifupdown2` | `ifupdown2/*/ifupdown2.debug.log` |
| `installer` | All files in the `/var/log/installer` directory. |
| `mlag` | `clagd.log` |
| `nginx` | All files in the `nginx` folder. The most current file is `access.log`. |
| `nvue` | `nvued.log`, `nv-cli.log`. The most current file is `nvued.log` |
| `otlp-telemetry` | All files in the `/var/log/otlp-telemetry` directory. |
| `platform-phc` | `phc2sys.log` |
| `platform-thermal` | `tc_log` |
| `pps` | `ts2phc.log` |
| `ptm` | `ptmd.log` |
| `ptp` | `ptp4l.log` |
| `ptp-firefly-servo` |
| `routing` | All files in `/var/log/frr` directory. The most current file is `frr.log`.  |
| `stp` | `mstpd.log` |
| `synce` | `synced.log`, `synced.log`, `synced-selector.log` |
{{< /expand >}}

The following example shows the contents of the most current log file for NVUE:

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

The following example shows the log files and associated logs for NVUE:

```
cumulus@switch:~$ nv show system log component nvue file list
File name    File path           
-----------  --------------------
nv-cli.log   /var/log/nv-cli.log 
nvued.log    /var/log/nvued.log  
nvued.log.1  /var/log/nvued.log.1
```
<!--
## Upload System Log Files to a Remote URL

You can transfer specific log files or system component-specific log files for remote analysis, backup, or troubleshooting, you can upload the file to a remote URL or server.

To upload a specific system log file to a remote URL, run the `nv action upload system log file <file-name> <remote-url-upload>` command:

```
cumulus@switch:~$ nv action upload system log file mstpd.log <remote-url-upload> 
```

To upload a system component-specific log file to a remote URL, run the `nv action upload system log component <component-name> file <file-name> <remote-url-upload>` command.

```
cumulus@switch:~$ nv action upload system log component nvue file nvued.log <remote-url-upload> 
```

You can perform the upload within a specific VRF context; for example:

```
cumulus@switch:~$ nv action upload system log component nvue file nvued.log <remote-url-upload> vrf RED
```
-->
## Delete System Log Files

Deleting log files enables you to manage storage space and ensure that only relevant logs remain. You typically delete log files after you upload or archive them, or when you no longer need the logs for troubleshooting or auditing.
Log file deletion is a crucial step in log management to ensure that outdated or irrelevant data does not occupy system resources.

To delete a log file, run the `nv action delete system log file <file-name>` command:

```
cumulus@switch:~$ nv action delete system log file mstpd.log 
```

To delete a log file from a specific system component, run the `nv action delete system log component <component-name> file <file-name>` command:

```
cumulus@switch:~$ nv action delete system log component nvue file nvued.log
```

## Rotate the System Log File

To rotate the system log file:

```
cumulus@switch:~$ nv action rotate system log
Action executing ...
Log rotation successful
Action succeeded
```

Cumulus Linux automatically manages log file size, preventing the logs from filling the storage space and slowing down the system.
