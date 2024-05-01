---
title: System Config
author: Cumulus Networks
weight: 390

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config</h>

Shows system configuration.

{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the command output is in `json` format.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config
            operational  applied
-----------  -----------  ---------
             apply        apply
             auto-save    auto-save
             snippet      snippet
apply
  overwrite  all          all
auto-save
  enable     off          off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config apply</h>

Shows the system configuration apply settings.

{{%notice note%}}
In Cumulus Linux 5.6 and earlier, the command output is in `json` format.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config apply
          operational  applied
---------  -----------  -------
overwrite  all          all
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config apply ignore</h>

Shows which files NVUE ignores when you run the `nv config apply` command.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config apply ignore 
/etc/ptp4l.conf: {}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config apply ignore \<ignore-id\></h>

Shows information about the specified file you set to ignore when you run the `nv config apply` command.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<ignore-id>` | The ignored file. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config apply ignore /etc/frr/frr.conf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config auto-save</h>

Shows if configuration auto save is on or off.

When auto save is `off`, when you run the `nv config apply` command to apply a configuration setting, NVUE applies the pending configuration to become the applied configuration but does not update the startup configuration file (`/etc/nvue.d/startup.yaml`). To save the applied configuration to the startup configuration so that the changes persist after the reboot, you must run the `nv config save` command.

When auto save is `on` when you run the `nv config apply` command, NVUE saves the configuration to the startup configuration automatically when you run `nv config apply` so that you do not have to run the `nv config save` command.

- In Cumulus Linux 5.9 and later, auto save is `on` by default.
- In Cumulus Linux 5.8 and earlier, auto save is `off` by default.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show system config auto-save
enable: off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config snippet</h>

Shows the file snippets you configure on the system.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config snippet
switchd.conf: |
  link_flap_window = 10
  link_flap_threshold = 5
```
