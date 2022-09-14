---
title: Troubleshoot SNMP
author: NVIDIA
weight: 1180
toc: 4
---

Use the following commands to troubleshoot potential SNMP issues.

To see the current SNMP configuration status:

```
cumulus@switch:~$ net show snmp-server status
Simple Network Management Protocol (SNMP) Daemon.
---------------------------------  ------------------------------------------------------------------------------------
Current Status                     failed (failed)
Reload Status                      enabled
Listening IP Addresses             localhost 9.9.9.9
Main snmpd PID                     0
Version 1 and 2c Community String  Configured
Version 3 Usernames                Not Configured
Last Logs (with Errors)            -- Logs begin at Thu 2017-08-03 16:23:05 UTC, end at Fri 2017-08-04 18:17:24 UTC. --
                                   Aug 04 18:17:19 cel-redxp-01 snmpd[8389]: Error opening specified endpoint "9.9.9.9"
                                   Aug 04 18:17:19 cel-redxp-01 snmpd[8389]: Server Exiting with code 1
---------------------------------  ------------------------------------------------------------------------------------
```

To show a summary of the SNMP configuration settings on the switch:

```
cumulus@switch:~$ nv show service snmp-server
                       applied  description
---------------------  -------  -------------------------------------------------------------------
enable                 on       Turn the feature 'on' or 'off'.  The default is 'off'.
trap-cpu-load-average
  [one-minute]         12       Collection of One Minute load average thresholds to send SNMP traps
trap-link-down
  check-frequency      10       Link up or link down checking frequency in seconds
trap-link-up
  check-frequency      15       Link up or link down checking frequency in seconds
```

To show the SNMP server listening address:

```
cumulus@switch:~$ nv show service snmp-server listening-address
```
