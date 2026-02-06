---
title: FIPS
author: NVIDIA
weight: 192
toc: 4

---

<span class="a-tooltip">[FIPS](## "Federal Information Processing Standards")</span> are standards for federal computer systems developed by the U.S. government and published by the National Institute of Standards and Technology (NIST).

When you enable FIPS mode, the switch enforces FIPS 140-2 and 140-3 compliant cryptographic operations, making it suitable for high-security and regulated environments.

{{%notice note%}}
- Enabling or disabling FIPS mode takes approximately one to two minutes and requires a switch reboot to take full effect.
- NVUE prevents you from enabling FIPS if non-compliant configuration exists on the switch and provides details of the violations.
- When FIPS mode is enabled and you apply LDAP, TACACS, RADIUS, or authentication order configuration, all logged-in user sessions terminate and users must re-authenticate (except for root user).
- Factory reset returns FIPS mode to disabled mode (except when you use the `keep all-config` option).
- If FIPS is enabled when you upgrade the switch with `onie-install -t`, an additional reboot is required after the upgrade for FIPS mode to take full effect.
{{%/notice%}}

## Configure FIPS Mode

FIPS mode is disabled by default. To enable FIPS on the switch, run the `nv set system security fips mode enabled` command. When you apply the configuration, NVUE shows a warning message.

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

To disable FIPS, run the `nv set system security fips mode disabled` command. You can also run the `nv unset system security fips` command to restore FIPS to the default setting (`disabled`).

## Show FIPS Configuration

To show if FIPS mode is enabled, run the `nv show system security fips` command or the `nv show system security` command:

```
cumulus@switch:~$ nv show system security fips
                           operational  applied
-------------------------  -----------  -------
mode                       enabled      enabled
```

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

## FIPS Restricted Configurations

When you enable FIPS mode, NVUE blocks the following configurations that use non-FIPS compliant algorithms:

| Feature | Restriction | Blocked Configuration |
| ------- | ----------- | --------------------- |
| SNMP    | MD5 authentication | `nv set system snmp-server username <username> auth-md5` |
| SNMP    | SHA authentication | `nv set system snmp-server username <username> auth-sha` |
| SNMP traps |MD5 authentication | `nv set system snmp-server trap-destination <dest-id> username <username> auth-md5` |
| SNMP traps | SHA authentication | `nv set system snmp-server trap-destination <dest-id> username <username> auth-sha` |
| OSPF | MD5 authentication | `nv set interface <interface> router ospf authentication` |
| BGP&nbsp;neighbor | MD5 password | `nv set vrf <vrf> router bgp neighbor <neighbor-id> password` |
| BGP&nbsp;peer&nbsp;group | MD5 password | `nv set vrf <vrf> router bgp peer-group <peer-group-id> password` |
| RADIUS | PAP or MSCHAPv2 authentication types | `nv set system aaa radius auth-type pap`<br><br>`nv set system aaa radius auth-type mschapv2` |
| RADIUS server | PAP or MSCHAPv2 authentication types | `nv set system aaa radius server <server-id> auth-type pap`<br><br>`nv set system aaa radius server <server-id> auth-type mschapv2` |
| LDAP | SSL or TLS mode |`nv set system aaa ldap ssl mode start-tls`<br><br>`nv set system aaa ldap ssl mode ssl` |
| User accounts | MD5 hashed passwords | `nv set system aaa user <user> hashed-password`|
| SSH server | Non-FIPS key exchange | `nv set system ssh-server kex-algorithms curve25519-sha256` |
| SSH server | Non-FIPS public key algorithms | `nv set system ssh-server pubkey-accepted-algorithms ssh-ed25519` |
| Certificates | Non-FIPS algorithms or key sizes |Imported certificates, CAs, and CRLs must use RSA 2048 or more bits, ECDSA P-256, P-384, or P-521, SHA-256, 384, or 512 signatures. |

If you try to enable FIPS with any of these configurations present, NVUE rejects the apply and displays the specific violations.
