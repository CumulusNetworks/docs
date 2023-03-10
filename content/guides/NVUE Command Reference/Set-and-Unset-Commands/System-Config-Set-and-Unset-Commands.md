---
title: System Config Set and Unset Commands
author: Cumulus Networks
weight: 720
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
