---
title: System Config Set and Unset Commands
author: Cumulus Networks
weight: 740
product: Cumulus Linux
type: nojsscroll
---
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## nv set system config

Configures system configuration settings.

- - -

## nv set system config auto-save

Configures the configuration auto save feature.

- - -

## nv set system config auto-save enable

Turns auto save on or off. The auto save option lets you save the pending configuration to the startup configuration automatically when you run `nv config apply` so that you do not have to run the `nv config save` command.

## Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system config auto-save enable on
```

- - -

## nv set system config apply

Configures how NVUE performs `config apply` operations.

- - -

## nv set system config apply ignore \<ignore-id\>

Configures NVUE to ignore a specific underlying Linux file when applying configuration changes. For example, if you push certain configuration to the switch using Ansible and Jinja2 file templates or you want to use custom configuration for a particular service such as PTP, you can ensure that NVUE never writes to those configuration files.

## Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system config apply ignore /etc/ptp4l.conf
```

## nv set system config apply overwrite

Configures which files NVUE overwrites during `nv config apply`. You can specify:
- `all` to overwrite all files.  If you modify a file locally, you see a warning when you try to apply the configuration and you can stop the apply before NVUE overwrites the local modification.  This is the default setting.
- `controlled` overwrites only the files that NVUE most recently changes.  If you change a file locally, you see a warning but NVUE does not overwrite the file.

## Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system config apply overwrite controlled
```

- - -

## nv set system control-plane

Configures control plane settings.

- - -

## nv set system control-plane trap \<trap-id\>

Configures control plane traps.

- - -

## nv set system control-plane trap \<trap-id\> state

Turns the specified control plane trap on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-id>` |  The trap ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane trap l3-mtu-err state on
```

- - -

## nv set system control-plane policer \<policer-id\>

Configures control plane policers.

- - -

## nv set system control-plane policer \<policer-id\> state

Turns the specified control plane policer on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The policer ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane policer acl-log state on
```

- - -

## nv set system control-plane policer \<policer-id\> burst

Configures the control plane policer burst rate, which is the number of packets or kilobytes (KB) allowed to arrive sequentially. You can specify a value between 10 and 10000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The policer ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane policer acl-log burst 1000
```

- - -

## nv set system control-plane policer \<policer-id\> rate

Configures the control plane policer forwarding rate, which is the maximum rate in kilobytes (KB) or packets. You can specify a value between 10 and 50000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The policer ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system control-plane policer acl-log burst 5000
```

- - -

# nv set system counter

Configures the system counter polling intervals.

- - -

## nv set system counter polling-interval

Configures the system counter polling interval for logical and physical interfaces

- - -

## nv set system counter polling-interval logical-interface

Configures the system counter polling interval in seconds for logical interfaces. You can set a value between 1 and 30.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system counter polling-interval logical-interface 20
```

- - -

## nv set system counter polling-interval physical-interface

Configures the system counter polling interval in seconds for physical interfaces. You can set a value between 1 and 10.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system counter polling-interval physical-interface 5
```

- - -

## nv set system message

Configures the message you want users of the switch to see before and after they log in.

- - -

## nv set system message pre-login

Configures the message you want users to see before they log into the switch.

If the message contains more than one word, you must enclose it in quotes (").

## Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system message pre-login "This switch is under maintenance"
```

- - -

## nv set system message post-login

Configures the message you want users to see after they log into the switch.

If the message contains more than one word, you must enclose it in quotes (").

## Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set system message post-login "This switch is being used for testing"
```

- - -
