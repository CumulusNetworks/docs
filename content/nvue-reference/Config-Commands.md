---
title: Config Commands
author: Cumulus Networks
weight: 50

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config apply </h>

In Cumulus Linux 5.8 and earlier, the `nv config apply` command applies the current pending configuration. This command does not save the configuration; the configuration does not persist after a reboot. To save the startup configuration automatically when you run `nv config apply` without having to run the `nv config save` command, run the `nv set system config auto-save enable on` command.

In Cumulus Linux 5.9 and later, auto save is `on` by default; the `nv config apply` command automatically saves the configuration and the configuration persists after a reboot.

You can specify the following options with the `nv config apply` command:

- `--y` or `--assume-yes` automatically replies yes to all prompts.
- `--assume-no` automatically replies no to all prompts.
- `--confirm` applies the configuration change, but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the `apply --confirm <time>` command. For example, `nv config apply --confirm 60` requires you to confirm within one hour.
- `--confirm-status` shows the amount of time left before the automatic rollback.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config apply --y
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config apply \<revision\></h>

Applies a specific configuration revision. This command does not save the configuration; the configuration does not persist after a reboot. You can specify the following options with this command:

- `--y` or `--assume-yes` automatically replies yes to all prompts.
- `--assume-no` automatically replies no to all prompts.
- `--confirm` applies the configuration change, but you must confirm the applied configuration. If you do not confirm within ten minutes, the configuration rolls back automatically. You can change the default time with the `apply --confirm <time>` command. For example, `nv config apply --confirm 60` requires you to confirm within one hour.
- `--confirm-status` shows the amount of time left before the automatic rollback.

### Command Syntax

| <div style="width:250px">Syntax  |  Description  |
| ----------   | ------------  |
| `<revision>` | The configuration revision you want to apply instead of the current pending configuration. You can specify `applied`, `startup`, `empty`, or a revision number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config apply 5 --y
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config detach</h>

Detaches the configuration from the current pending configuration. When you run this command, NVUE discards all configuration changes between the last `nv config apply` command and the `nv config detach` command.”

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config detach
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config diff \<revision-base\> \<revision-target\></h>

Shows differences between configurations, such as the startup configuration and the applied configuration, or the applied configuration and a specific configuration revision.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<revision-base>` | The base configuration revision you want to compare against. You can specify applied, startup, or a specific configuration revision number. |
| `<revision-target>` | The target configuration revision you want to compare against. You can specify applied, startup, or a specific configuration revision number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config diff 1 2
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config find</h>

Finds a portion of the applied configuration according to the search string you provide.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config find stp
- set:
    bridge:
      domain:
        br_default:
          stp:
            mode: pvrst
            vlan:
              '10':
                bridge-priority: 4096
                forward-delay: 4
                hello-time: 4
                max-age: 6
              '20':
                bridge-priority: 61440
                forward-delay: 4
                hello-time: 4
                max-age: 6
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

##  <h>nv config history</h>

Shows the `apply` history for the current configuration revision.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config history
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config history \<revision\></h>

Shows the `apply` history for a specific configuration revision.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<revision>` | The revision whose `apply` history you want to show.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config history 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config patch \<nvue-file\></h>

Updates the pending configuration with an NVUE configuration file in YAML format.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<cue-file>` | The NVUE YAML file you want to use to update the pending configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config patch myconfig.yaml
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config replace \<nvue-file\></h>

Replaces the pending configuration with the specified YAML configuration file.

### Command Syntax

| <div style="width:250px">Syntax   |  Description  |
| ----------   | ------------  |
| `<nvue-file>` | The NVUE YAML file you want to use to replace the pending configuration. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config replace myconfig.yaml
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config revision</h>

Shows the configuration revisions on the switch.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv config revision
Rev ID                State              Apply ID                          Apply Date           Type      User     Reason         Message                        
--------------------  -----------------  --------------------------------  -------------------  --------  -------  -------------  -------------------------------
1                     applied_and_saved  rev_1_apply_1                     2024-04-26 11:24:50  CLI       root     Config update  Password sync for user: cumulus
2                     applied_and_saved  rev_2_apply_2                     2024-04-26 16:06:14  CLI       cumulus  Config update  Config update by cumulus       
3                     applied_and_saved  rev_3_apply_1                     2024-04-26 16:17:21  CLI       cumulus  Config update  Config update by cumulus       
4                     applied_and_saved  rev_4_apply_1                     2024-04-26 16:34:04  CLI       cumulus  Config update  Config update by cumulus
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config save</h>

Overwrites the startup configuration with the applied configuration by writing to the `/etc/nvue.d/startup.yaml` file. The configuration persists after a reboot.

In Cumulus Linux 5.9 and later, auto save is `on` by default; NVUE saves the configuration to the `/etc/nvue.d/startup.yaml` file automatically. Run this command to save the applied configuration if NVUE auto save if `off`.

In Cumulus Linux 5.8 and earlier, auto save is `off` by default.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config save
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv config show</h>

Shows the currently applied configuration in YAML format.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv config show
 header:
    model: VX
    nvue-api-version: nvue_v1
    rev-id: 1.0
    version: Cumulus Linux 5.7.0
- set:
    bridge:
      domain:
        br_default:
          vlan:
            '10':
              vni:
                '10': {}
            '20':
              vni:
                '20': {}
            '30':
              vni:
                '30': {}
    evpn:
      enable: on
    interface:
      bond1:
        bond:
          member:
            swp1: {}
          mlag:
            id: 1
        bridge:
          domain:
            br_default:
              access: 10
      bond1-3:
        bond:
          lacp-bypass: on
          mlag:
            enable: on
        link:
          mtu: 9000
        type: bond
...
```
