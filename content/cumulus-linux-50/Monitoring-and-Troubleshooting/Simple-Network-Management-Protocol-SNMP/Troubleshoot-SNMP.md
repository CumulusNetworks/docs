---
title: Troubleshoot SNMP
author: NVIDIA
weight: 1180
toc: 4
---

Use the following commands to troubleshoot potential SNMP issues:

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

```
cumulus@switch:~$ net show configuration snmp-server
snmp-server
  listening-address 127.0.0.1
  readonly-community public access default
  readonly-community allpass access any
  readonly-community temp2 access 1.1.1.1
  readonly-community temp2 access 2.2.2.2
  trap-destination 1.1.1.1 community-password public version 2c
  trap-link-up check-frequency 10
  trap-snmp-auth-failures
```

```
cumulus@switch:~$ net show configuration commands
...
net add snmp-server listening-address all
net add snmp-server readonly-community allpass access any
net add snmp-server readonly-community temp2 access 1.1.1.1
net add snmp-server readonly-community temp2 access 2.2.2.2
net add snmp-server trap-destination 1.1.1.1 community-password public version 2c
net add snmp-server trap-link-up check-frequency 10
net add snmp-server trap-snmp-auth-failures
...
```
