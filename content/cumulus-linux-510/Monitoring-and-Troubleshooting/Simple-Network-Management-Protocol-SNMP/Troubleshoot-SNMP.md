---
title: Troubleshoot SNMP
author: NVIDIA
weight: 1180
toc: 4
---

Use the following commands to troubleshoot potential SNMP issues.

To show a summary of the SNMP configuration settings on the switch:

```
cumulus@switch:~$ nv show service snmp-server
                     applied         description
-------------------  --------------  ---------------------------------------------------------------------
enable               on              Turn the feature 'on' or 'off'.  This feature is disabled by default.
[listening-address]  localhost       Collection of listening addresses
trap-link-down
  check-frequency    60              Link up or link down checking frequency in seconds
trap-link-up
  check-frequency    60              Link up or link down checking frequency in seconds
[username]           testusernoauth  Usernames
[username]           user1
[username]           user2
[username]           user3
[username]           user666
[username]           user999
```

To show a summary of the SNMP configuration settings in json format, run the `nv show service snmp-server  --output json --applied` command.

To show the SNMP trap CPU load average, run the `nv show service snmp-server trap-cpu-load-average` command.

To show SNMP trap authentication failures, run the `nv show service snmp-server trap-snmp-auth-failures` command.

To see all the show commands for SNMP troubleshooting, run `nv show service snmp-server` and press the Tab key:

```
cumulus@switch:~$ nv show service snmp-server  <<press Tab>>
listening-address        readonly-community-v6    trap-link-down           username
mibs                     trap-cpu-load-average    trap-link-up             viewname
readonly-community       trap-destination         trap-snmp-auth-failures  
```
