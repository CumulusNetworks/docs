---
title: SSH Server
author: Cumulus Networks
weight: 735
draft: true
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server allow-users \<user-id\></h>

Configures the user accounts that you to allow to establish an SSH session.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<user-id>` |   The user account name. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server allow-users user1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server authentication-retries</h>

Configures the number of login attempts allowed before rejecting the SSH session. You can set a value between 3 and 100.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server authentication-retries 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server ciphers</h>

Configures SSH ciphers. You can specify `aes256-ctr`, `aes192-ctr`, `aes128-ctr`, `aes128-gcm@openssh.com`, or `aes256-gcm@openssh.com`. The default value is `aes256-ctr`.

{{%notice note%}}
SSH cipher configuration replaces SSH strict mode that is available in Cumulus Linux 5.14 and earlier.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ssh-server ciphers aes192-ctr 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server deny-users \<user-id\></h>

Configures the user accounts that are **not** allowed to establish an SSH session.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<user-id>` |   The user account name. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server deny-users user3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server host-key-algorithms</h>

Configures SSH strict SSH host key algorithms. You can specify `ecdsa-sha2-nistp256`, `rsa-sha2-256`, or `rsa-sha2-512`. The default value is `ecdsa-sha2-nistp256`.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ssh-server host-key-algorithms rsa-sha2-256
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server inactive-timeout</h>

Configures the amount of time a session can be inactive before the SSH server terminates the connection.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server inactive-timeout 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server kex-algorithms</h>

Configures strict SSH key exchange algorithms. You can specify `curve25519-sha256`, `curve25519-sha256@libssh.org`, `diffie-hellman-group16-sha512`, `diffie-hellman-group18-sha512`, or `diffie-hellman-group14-sha256`. The default value is `curve25519-sha256`.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ssh-server kex-algorithms curve25519-sha256@libssh.org
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server login-record-period</h>

Configures the number of days on which to calculate login records, to be shown after login. You can set a value between 1 and 30.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv set system ssh-server login-record-period 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server login-timeout</h>

Configures the number of seconds allowed before login times out. You can set a value between 1 and 600.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server login-timeout 200
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server macs</h>

Configures strict SSH MACs. You can specify `hmac-sha2-256`, `hmac-sha2-512`, `hmac-sha2-512-etm@openssh.com`, or `hmac-sha2-256-etm@openssh.com`. The default value is `hmac-sha2-256`.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ssh-server macs hmac-sha2-512
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server max-sessions-per-connection </h>

Configures the maximum number of SSH sessions allowed per TCP connection. You can specify a value between 1 and 100.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server max-sessions-per-connection 10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server max-unauthenticated session-count</h>

Configures the maximum number of unauthenticated SSH sessions allowed. You can set a value between 1 and 10000.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server max-unauthenticated session-count 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server max-unauthenticated throttle-percent</h>

Configures the starting percentage of connections to reject above the throttle start count before reaching the session count limit. You can set a value between 1 and 100.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server max-unauthešticated throttle-percent 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server max-unauthenticated throttle-start</h>

Configures the number of unauthenticated SSH sessions allowed before throttling starts. You can set a value between 1 and 10000.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server max-unauthenticated throttle-start 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server permit-root-login</h>

Configures the root account to use SSH to log into the switch with one of the following:
- A password (`enabled` or `disabled`).
- A public key or any allowed mechanism that is not a password and not keyboardinteractive. This is the default setting (`prohibit-password`).
- A set of commands defined in the authorized_keys file (`forced-commands-only`).

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server permit-root-login forced-commands-only
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server port \<port-id\></h>

Configures the TCP port numbers that can listen for incoming SSH sessions.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<port-id>` |   The port number. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server port 443
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server pubkey-accepted-algorithms</h>

Configures strict SSH public key accepted algorithms. You can specify `ecdsa-sha2-nistp256-cert-v01@openssh.com`, `ecdsa-sha2-nistp384-cert-v01@openssh.com`, `ecdsa-sha2-nistp521-cert-v01@openssh.com`, `rsa-sha2-512-cert-v01@openssh.com`, `rsa-sha2-256-cert-v01@openssh.com`, `rsa-sha2-512`, `rsa-sha2-256`, `ecdsa-sha2-nistp256`, `ecdsa-sha2-nistp384`, `ecdsa-sha2-nistp521`, `ssh-ed25519`, or `ssh-ed25519-cert-v01@openssh.com`. The default value is `ecdsa-sha2-nistp256-cert-v01@openssh.com`.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv set system ssh-server pubkey-accepted-algorithms ecdsa-sha2-nistp256-cert-v01@openssh.com
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server state</h>

Enables or disables the SSH server on the switch.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server state disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server strict</h>

Enables or disables SSH strict mode. By default, SSH strict mode is `on` so that Cumulus Linux disables X11, TCP forwarding, and compression and enforces secure ciphers.

{{%notice note%}}
Cumulus Linux 5.15 and later no longer support this command.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system ssh-server strict disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server trusted-ca-keys \<key-ID\> key</h>

Sets the trusted CA key literal for certificate-based authentication. The key literal is located within a public key file.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<key-id>` |   The CA trusted certificate ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system ssh-server trusted-ca-keys KEY1 key AAAAB3NzaC1yc2EAAAADA..
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server trusted-ca-keys \<key-ID\> type \<key-type\></h>

Sets the trusted CA key type for certificate-based authentication. The key type is located within a public key file.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<key-id>` |   The CA trusted certificate ID. |

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set system ssh-server trusted-ca-keys KEY1 type ssh-rsa
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system ssh-server vrf \<vrf-id\></h>

Configures the VRFs on which you want the SSH service to run. The SSH service runs in the default VRF on the switch but listens on all interfaces in all VRFs.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<vrf-id>` |   The VRF you want to configure. |

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server vrf RED
```
