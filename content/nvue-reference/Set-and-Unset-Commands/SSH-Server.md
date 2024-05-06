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

## <h>nv set system ssh-server deny-users \<user-id\></h>

Configures the user accounts that are **not** allowed to establish an SSH session.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server deny-users user3
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

## <h>nv set system ssh-server authentication-retries</h>

Configures the number of login attempts allowed before rejecting the SSH session. You can set a value between 3 and 100.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server authentication-retries 10
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

## <h>nv set system ssh-server inactive-timeout</h>

Configures the amount of time a session can be inactive before the SSH server terminates the connection.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server inactive-timeout 5
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

## <h>nv set system ssh-server max-sessions-per-connection </h>

Configures the maximum number of SSH sessions allowed per TCP connection. You can specify a value between 1 and 100.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv set system ssh-server max-sessions-per-connection 10
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

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv set system ssh-server strict disabled
```
