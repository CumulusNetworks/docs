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

## <h>nv set system security encryption db state</h>

Enables and disables password encryption in the NVUE `startup.yaml` file. By default, NVUE encrypts passwords, such as the RADIUS secret, TACACS secret, BGP peer password, OSPF MD5 key, and SNMP strings in the startup.yaml file.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system security encryption db state disabled
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
