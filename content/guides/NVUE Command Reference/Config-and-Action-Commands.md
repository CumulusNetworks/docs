---
title: Config and Action Commands
author: Cumulus Networks
weight: 50
product: Cumulus Linux
---
## nv config apply

Applies the current pending configuration or a specific revision. This command does not save the configuration; the configuration does not persist after a reboot.

| Option   |  Description  |
| ----------   | ------------  |
|`--y` or `--assume-yes` | Automatically reply yes to all prompts. |
| `--assume-no`  | Automatically reply no to all prompts. |
| `--confirm` | Applies the configuration change but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the apply `--confirm <time>` command. For example, `nv config apply --confirm 60` requires you to confirm within one hour. |
| `--confirm-status` | Shows the amount of time left before the automatic rollback.|

**Default Setting**

The current pending configuration.

**Identifiers**

| Identifier   |  Description  |
| ----------   | ------------  |
| `<revision>` | The configuration revision you want to apply instead of the current pending configuration. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config apply --y
```

## nv config save

Overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot.

**Usage**

`nv config save [options]`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config save
```

## nv config replace \<cue-file\>

Replaces the pending configuration with the specified YAML configuration file.

**Usage**

`nv config replace [options] <cue-file>`

**Default Setting**

N/A

**Identifiers**

| Identifier   |  Description  |
| ----------   | ------------  |
| `<cue-file>` | The NVUE YAML file you want to use to replace the pending configuration. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config replace myconfig.yaml
```

## nv config detach

Detaches the configuration from the current pending configuration. Cumulus Linux names the detached configuration `pending` and includes a timestamp with extra characters. For example: `pending_20210128_212626_4WSY`

**Usage**

`nv config detach [options]`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config detach
```

## nv config diff

Shows differences between configurations, such as the pending configuration and the applied configuration or the detached configuration and the pending configuration.

**Usage**

`nv config diff [options] [<revision>] [<revision>]`

**Default Setting**

N/A

| Identifier   |  Description  |
| ----------   | ------------  |
| `<revision>` | The configuration revision you want to compare. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config diff pending_20210128_212626_4WSY pending_20210222_212625_3VRX
```

## nv config show

Shows the currently applied configuration in YAML format.

**Usage**

`nv config show [options]`

**Default Setting**

N/A

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config show
```

## nv config patch <cue-file>

Updates the pending configuration with an NVUE configuration file in YAML format.

**Usage**

`nv config patch [options] <cue-file>`

**Default Setting**

N/A

| Identifier   |  Description  |
| ----------   | ------------  |
| `<cue-file>` | The NVUE YAML file you want to use to replace the pending configuration. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config patch myconfig.yaml
```

## nv config history \<revision\>

Shows the `apply` history for a revision.

**Usage**

`nv config history [options] [<revision>]`

**Default Setting**

The current revision.

**Identifiers**

| Identifier   |  Description  |
| ----------   | ------------  |
| `<revision>` | The revision whose `apply` history you want to show. |

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv config history myfile
```

## nv action

Applies action configuration attributes.

**Usage**

`nv action [options]`

**Version History**

Introduced in Cumulus Linux 5.0.0

**Example**

```
cumulus@leaf01:mgmt:~$ nv action 
```
