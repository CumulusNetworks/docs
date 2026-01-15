---
title: FIPS
author: NVIDIA
weight: 192
toc: 4

---
<span class="a-tooltip">[FIPS](## "Federal Information Processing Standards")</span> are standards for federal computer systems and information developed by the U.S. government and published by the National Institute of Standards and Technology (NIST).

When you enable FIPS, the switch complies with FIPS 140-2 and 140-3 requirements, making it suitable for high-security applications.

## Configure FIPS Mode

To enable FIPS on the switch, run the `nv set system security fips mode enabled` command. Enabling FIPS mode requires the switch to reboot.

```
cumulus@switch:~$ nv set system security fips mode enabled
cumulus@switch:~$ nv config apply
Warning: You are about to change FIPS mode to: enabled.
  - This apply may take 1-2 minutes to complete.
  - FIPS mode change requires reboot to take full effect.
Warning: The following files have been changed since the last save, and they WILL be overwritten.
	- /etc/ssl/openssl.cnf
	- /etc/default/grub
Are you sure? [y/N]
```

To disable FIPS, run the `nv set system security fips mode disabled` command. You can also run the `nv unset system security fips` command to restore FIPS to the default setting, which is `disabled`.

{{%notice note%}}
- When you enable FIPS and apply LDAP, TACACS, or RADIUS configuration or change the authentication order, all logged in user sessions terminate and users must log back into the switch.
- NVUE prevents you from enabling FIPs if there is non-FIPS compliant configuration on the switch and provides details of violations.
{{%/notice%}}

## Show FIPS Configuration

To show if FIPS mode is configured, run the `nv show system security fips` command:

```
cumulus@switch:~$ nv show system security fips
                           operational  applied
-------------------------  -----------  -------
mode                       enabled      enabled
```

The `nv show system security` command shows if FIPS mode is enabled in addition to other security options.

```
cumulus@switch:~$ nv show system security
                           operational  applied
-------------------------  -----------  -------
fips
  mode                     enabled      enabled
password-hardening
  state                    enabled      enabled
  reject-user-passw-match  enabled      enabled
  lower-class              enabled      enabled
  upper-class              enabled      enabled
  digits-class             enabled      enabled
  special-class            enabled      enabled
  expiration-warning       15           15
  expiration               180          180
  history-cnt              10           10
  len-min                  8            8
encryption
  db
    state                               enabled
...
```
