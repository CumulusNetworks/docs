---
title: Config Commands
author: Cumulus Networks
weight: 50
product: Cumulus Linux
---
## nv config apply

Applies the current pending configuration or a specific revision. This command does not save the configuration; the configuration does not persist after a reboot. You can specify the following options with this command:

- `--y` or `--assume-yes` automatically replies yes to all prompts.
- `--assume-no` automatically replies no to all prompts.
- `--confirm` applies the configuration change but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the apply `--confirm <time>` command. For example, `nv config apply --confirm 60` requires you to confirm within one hour.
- `--confirm-status` shows the amount of time left before the automatic rollback.

### Command Syntax

| <div style="width:250px">Syntax  |  Description  |
| ----------   | ------------  |
| `<revision>` | The configuration revision you want to apply instead of the current pending configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config apply --y
```

- - -

## nv config save

Overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config save
```
- - -

## nv config replace \<cue-file\>

Replaces the pending configuration with the specified YAML configuration file.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<cue-file>` | The NVUE YAML file you want to use to replace the pending configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config replace myconfig.yaml
```

- - -

## nv config detach

Detaches the configuration from the current pending configuration. Cumulus Linux names the detached configuration `pending` and includes a timestamp with extra characters. For example: `pending_20210128_212626_4WSY`

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config detach
```

- - -

## nv config diff

Shows differences between configurations, such as the pending configuration and the applied configuration or the detached configuration and the pending configuration.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<revision>` | The configuration revisions you want to compare. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config diff pending_20210128_212626_4WSY pending_20210222_212625_3VRX
```

- - -

## nv config show

Shows the currently applied configuration in YAML format.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config show
```

- - -

## nv config patch \<cue-file\>

Updates the pending configuration with an NVUE configuration file in YAML format.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<cue-file>` | The NVUE YAML file you want to use to update the pending configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config patch myconfig.yaml
```

- - -

## nv config history

Shows the `apply` history for the current revision or for a specific revision.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<revision>` | The revision whose `apply` history you want to show.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@leaf01:mgmt:~$ nv config history
cumulus@leaf01:mgmt:~$ nv config history 5
```
