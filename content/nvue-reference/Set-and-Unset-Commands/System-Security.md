---
title: System Security
author: Cumulus Networks
weight: 775

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security alerts audit-failure</h>

Enables or disables audit-failure alerts. Audit-failure alerts are enabled by default.

{{%notice note%}}
No audit failure alerts trigger if global security alerts are disabled with the `nv set system security alerts state disabled` command.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.17.0

### Example

```
cumulus@switch:~$ nv set system security alerts audit-failure disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security alerts state</h>

Configures the switch to send proactive alerts as SNMPv3 traps to configured trap destinations and as syslog messages (facility LOG_DAEMON, severity CRIT) when audit processing failures occur, such as when the audit daemon crashes or disk space runs low on the audit partition.

{{%notice note%}}
- To send security alerts through SNMP traps, you must have at least one SNMPv3 trap destination configured with a valid engine ID (a minimum 5 bytes or 10 hex characters after the 0x prefix).
- Cumulus Linux reuses trap destinations from the existing SNMP server configuration (`nv set system snmp-server trap-destination`). You do not need to configure a separate alert destination.
- Only SNMPv3 (authPriv) destinations receive traps.
- Disk full and disk I/O error events are logged to syslog only (no SNMP traps). The `space_left` and `admin_space_left` thresholds provide an early warning through SNMP traps before these critical conditions are reached.
- A clean `auditd` restart (`sudo service auditd restart`) does not trigger an alert.
- The security alerts manage only the alert-related action parameters in the `auditd` configuration (`space_left_action`, `admin_space_left_action`, `disk_full_action`, `disk_error_action`).
- If the `auditd.conf` file contains invalid values (for example, if `admin_space_left` has a higher setting than `space_left`), enabling or disabling security alerts fails because the `auditd` service cannot restart. To recover, correct the values in the `/etc/audit/auditd.conf` file, then run the `sudo systemctl reset-failed auditd` and `sudo systemctl restart auditd` commands.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.17.0

### Example

```
cumulus@switch:~$ nv set system security alerts state enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security encryption db state</h>

Enables and disables password encryption in the NVUE `startup.yaml` file. By default, NVUE encrypts passwords, such as the RADIUS secret, TACACS secret, BGP peer password, OSPF MD5 key, and SNMP strings in the startup.yaml file.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system security encryption db state disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security encryption folder-encrypt encrypted-folder</h>

Configures the absolute path to other directories you want to encrypt when you enable secure mount directory encryption. by default the switch encrypts the `/var/log`, `/var/home`, and `/var/lib` directories.

You enable secure mount directory encryption with the `nv action enable system security encryption folder-encrypt password <password>` command.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system security encryption folder-encrypt encrypted-folder /my_user/my_data
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security encryption folder-encrypt storage</h>

Configures the storage type for the folder encryption key. To protect sensitive data at rest, you can configure secure mount directory encryption on the switch with a USB device.

You enable secure mount directory encryption with the `nv action enable system security encryption folder-encrypt password <password>` command.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system security encryption folder-encrypt storage usb
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security fips mode</h>

Configures FIPS mode.

FIPS are standards for federal computer systems developed by the U.S. government and published by the National Institute of Standards and Technology (NIST).

When you enable FIPS mode, the switch enforces FIPS 140-2 and 140-3 compliant cryptographic operations, making it suitable for high-security and regulated environments.

{{%notice note%}}
- Enabling or disabling FIPS mode takes approximately one to two minutes and requires a switch reboot to take full effect.
NVUE prevents you from enabling FIPS if non-compliant configuration exists on the switch and provides details of the violations.
- When FIPS mode is enabled and you apply LDAP, TACACS, RADIUS, or authentication order configuration, all logged-in user sessions terminate and users must re-authenticate (except for root user).
- Factory reset returns FIPS mode to disabled mode (except when you use the factory reset `keep all-config` option).
- If FIPS is enabled when you upgrade the switch with `onie-install -t`, an additional reboot is required after the upgrade for FIPS mode to take full effect.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system security fips mode enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening digits-class</h>

Configures the password policy so that passwords must include at least one digit. You can specify `enabled` or `disabled`. The default setting is `enabled` when password security is enabled.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening digits-class disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening expiration</h>

Configures the duration in days after which system passwords expire. You can set a value between 1 and 365 days. The default value is 180 days.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening expiration 30
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening expiration-warning</h>

Configures the number of days before a password expires to send a warning. You can set a value between 1 and 30 days. The default value is 15 days.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening expiration-warning 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening history-cnt</h>

Configures the number of times you can reuse the same password. You can set a value between 1 and 100. The default value is 10.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening history-cnt 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening len-min</h>

Configures minimum password length. You can specify a value between 6 and 32 characters. The default value is 8.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening len-min 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening lower-class</h>

Configures the password policy so that passwords must include at least one lower case character. You can specify `enabled` or `disabled`. The default setting is `enabled` when password security is enabled.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening lower-class disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening reject-user-passw-match</h>

Configures the password policy so that usernames can be passwords. You can specify `enabled` or `disabled`. The default setting is `enabled` when password security is enabled.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening reject-user-passw-match disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening special-class</h>

Configures the password policy so that passwords must include at least one special character. The default setting is `enabled` when password security is enabled.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening special-class disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening state</h>

Enables or disables password security. The default setting is `enabled`.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening state disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system security password-hardening upper-class</h>

Configures the password policy so that passwords must include at least one uppercase letter. The default setting is `enabled` when password security is enabled.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system security password-hardening upper-class disabled
```
