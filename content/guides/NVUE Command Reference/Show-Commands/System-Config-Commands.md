---
title: System Config Commands
author: Cumulus Networks
weight: 360
product: Cumulus Linux
type: nojsscroll
---
## nv show system config

Shows the system configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config
```

- - -

## nv show system config apply

Shows the system configuration apply settings.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config apply
```

- - -

## nv show system config apply ignore

Shows which files are ignored when you run the `nv config apply` command.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ 
```

- - -

## nv show system config apply ignore \<ignore-id\>

Shows information about the specified file you set to ignore when you run the `nv config apply` command.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<ignore-id>` | The ignored file. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config apply ignore /etc/frr/frr.conf
```

## nv show system config auto-save

Shows if configuration auto save is on or off.

By default, when you run the `nv config apply` command to apply a configuration setting, NVUE applies the pending configuration to become the applied configuration but does not update the startup configuration file (`/etc/nvue.d/startup.yaml`). To save the applied configuration to the startup configuration so that the changes persist after the reboot, you must run the `nv config save` command. The auto save option lets you save the pending configuration to the startup configuration automatically when you run `nv config apply` so that you do not have to run the `nv config save` command.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config auto-save
```

- - -

## nv show system config snippet

Shows the file snippets you configure on the system.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv show system config snippet
```
