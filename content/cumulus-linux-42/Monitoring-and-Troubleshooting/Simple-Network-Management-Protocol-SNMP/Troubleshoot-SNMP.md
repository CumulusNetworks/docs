---
title: Troubleshoot SNMP
author: NVIDIA
weight: 1180
toc: 4
---

Use the following commands to troubleshoot potential SNMP issues.

## Troubleshoot with NCLU

To check the status of `snmpd` using NCLU, run the `net show snmp-server status` command. If there are issues, you might see errors like the following:

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

You can review the SNMP server configuration when you run:

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

You can see which NCLU commands were used to configure SNMP. Look for `snmp-server` in the output when you run:

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

## Troubleshoot with SNMP Commands

The `snmp` Debian package contains `snmpget`, `snmpwalk` and other programs that are useful for checking daemon functionality from the switch itself or from another workstation.

From a client, you access the MIB with the correct credentials.

```
cumulus@switch:~$ snmpwalk -v 3 -u userMD5withDES -l authPriv -a MD5 -x DES -A md5authpass -X desprivpass localhost 1.3.6.1.2.1.1.1
cumulus@switch:~$ snmpwalk -v 3 -u userSHAwithAES -l authPriv -a SHA -x AES -A shaauthpass -X aesprivpass localhost 1.3.6.1.2.1.1.1
```

This command gets the first MIB object in the system table; in this case, the SNMPv2 system name specified above:

```
cumulus@switch:~$ snmpgetnext -v 2c -c mynotsosecretpassword localhost SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: my little router
```

The following commands check the access for each user from the localhost.

To check user1, which has no authentication or encryption (*NoauthNoPriv*):

```
cumulus@switch:~$ snmpget -v 3 -u user1 -l NoauthNoPriv localhost 1.3.6.1.2.1.1.1.0
cumulus@switch:~$ snmpwalk -v 3 -u user1 -l NoauthNoPriv localhost 1.3.6.1.2.1.1
```

To check user2, which has authentication but no encryption (*authNoPriv*):

```
cumulus@switch:~$ snmpget -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1.1.1.0
cumulus@switch:~$ snmpget -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1.2.1.0
cumulus@switch:~$ snmpwalk -v 3 -u user2 -l authNoPriv -a MD5 -A user2password localhost 1.3.6.1.2.1
```

To check user3, which has both authentication and encryption (*authPriv*):

```
cumulus@switch:~$ snmpget -v 3 -u user3 -l authPriv -a MD5 -A user3password -x DES -X user3encryption localhost .1.3.6.1.2.1.1.1.0
cumulus@switch:~$ snmpwalk -v 3 -u user3 -l authPriv -a MD5 -A user3password -x DES -X user3encryption localhost .1.3.6.1.2.1
cumulus@switch:~$ snmpwalk -v 3 -u user666 -l authPriv -a SHA -x AES -A user666password -X user666encryption localhost 1.3.6.1.2.1.1
cumulus@switch:~$ snmpwalk -v 3 -u user999 -l authPriv -a MD5 -x DES -A user999password -X user999encryption localhost 1.3.6.1.2.1.1
```

{{%notice note%}}

As mentioned in {{<link url="Configure-SNMP/#snmp-and-vrfs" text="Configure SNMP">}}, SNMP is VRF-aware. To run commands like `snmpget` or `snmpwalk` in a VRF, preface the command with `sudo ip vrf exec <VRF>`, like this:

```
cumulus@switch:~$ sudo ip vrf exec default snmpgetnext -v 2c -c mynotsosecretpassword localhost SNMPv2-MIB::sysName
SNMPv2-MIB::sysName.0 = STRING: my little router
```

{{%/notice%}}
