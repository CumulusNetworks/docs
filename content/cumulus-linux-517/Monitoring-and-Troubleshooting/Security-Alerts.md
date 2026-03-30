---
title: Security Alerts
author: NVIDIA
weight: 149
toc: 3
---
Cumulus Linux can send proactive alerts as SNMPv3 traps to configured trap destinations and as syslog messages (facility LOG_DAEMON, severity CRIT) when audit processing failures occur, such as when the audit daemon crashes or disk space runs low on the audit partition.

### Detection Events

| Event | Trigger  | Alert Reason |
| -------- | -------- | ------------ |
| Daemon crash | `auditd` killed or exits abnormally | `daemon-crash` |
| Disk space low | Free space below space_left threshold | `space_left` |
| Disk space emergency | Free space below `admin_space_left` threshold | `admin_space_left` |
| Disk full | Zero free space on audit partition | Logged to syslog only. |
| Disk I/O error | Write failure to audit log | Logged to syslog only.|

{{%notice note%}}
- To send security alerts through SNMP traps, you must have at least one SNMPv3 trap destination configured with a valid engine ID (a minimum 5 bytes or 10 hex characters after the 0x prefix).
- Cumulus Linux reuses trap destinations from the existing SNMP server configuration (`nv set system snmp-server trap-destination`). You do not need to configure a separate alert destination.
- Only SNMPv3 (`authPriv`) destinations receive traps.
- Disk full and disk I/O error events are logged to syslog only (no SNMP traps). The `space_left` and `admin_space_left` thresholds provide an early warning through SNMP traps before these critical conditions are reached.
- A clean `auditd` restart (`sudo service auditd restart`) does not trigger an alert.
- The security alerts manage only the `alert-related` action parameters in the `auditd` configuration (`space_left_action`, `admin_space_left_action`, `disk_full_action`, `disk_error_action`).
- If the `auditd.conf` file contains invalid values (for example, if `admin_space_left` has a higher setting than `space_left`), enabling or disabling security alerts fails because the `auditd` service cannot restart. To recover, correct the values in `/etc/audit/auditd.conf` file, then run the `sudo systemctl reset-failed auditd` and 
`sudo systemctl restart auditd` commands.
{{%/notice%}}

### Enable Security Alerts

Security alerts are disabled by default. To enable security alerts:

```
cumulus@switch:~$ nv set system security alerts state enabled
cumulus@switch:~$ nv config apply
```

To disable security alerts run the `nv set system security alerts state disabled` command.

You can enable or disable individual alert categories. Currently, `audit-failure` is the only supported category, which is enabled by default.

To disable audit failure alerts:

```
cumulus@switch:~$ nv set system security alerts audit-failure disabled
cumulus@switch:~$ nv config apply
```

To re-enable audit failure alerts, run the `nv set system security alerts audit-failure enabled` command.

{{%notice note%}}
When you enable specific alert categories, no alerts trigger if global security alerts are disabled.
{{%/notice%}}

To show the current alert configuration and status, run the `nv show system security alerts` command:

```
cumulus@switch:~$ nv show system security alerts
               operational  applied
-------------  -----------  --------
state          disabled     enabled
audit-failure  enabled      disabled 
```

The `nv show system security` command also shows if security alerts are enabled.
