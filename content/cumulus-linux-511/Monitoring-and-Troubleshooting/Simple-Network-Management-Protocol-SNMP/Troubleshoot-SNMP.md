---
title: Troubleshoot SNMP
author: NVIDIA
weight: 1180
toc: 4
---

Use the following commands to troubleshoot potential SNMP issues.

To show a summary of the SNMP configuration settings on the switch:

```
cumulus@switch:~$ nv show system snmp-server
                     applied
-------------------  -----------------
[username]           snmpv3user
trap-link-up
  check-frequency    60
trap-link-down
  check-frequency    60
[listening-address]  10.10.10.10
system-name          switch-name
system-contact       Administrator
system-location      Site
state                enabled

To show a summary of the SNMP configuration settings in json format, run the `nv show system snmp-server --applied --output json` command.

To show the SNMP trap CPU load average, run the `nv show system snmp-server trap-cpu-load-average` command.

To show SNMP trap authentication failures, run the `nv show system snmp-server trap-snmp-auth-failures` command.

To see all the show commands for SNMP troubleshooting, run `nv show system snmp-server` and press the Tab key:

```
cumulus@switch:~$ nv show service snmp-server  <<press Tab>>
listening-address        readonly-community-v6    trap-link-down           username
mibs                     trap-cpu-load-average    trap-link-up             viewname
readonly-community       trap-destination         trap-snmp-auth-failures  
```
