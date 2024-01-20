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

Shows the system configuration in json format.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config
apply:
  ignore: {}
  overwrite: all
auto-save:
  enable: off
snippet: {}
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system config apply</h>

Shows the system configuration apply settings in `json` format.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system config apply
ignore: {}
overwrite: all
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

By default, when you run the `nv config apply` command to apply a configuration setting, NVUE applies the pending configuration to become the applied configuration but does not update the startup configuration file (`/etc/nvue.d/startup.yaml`). To save the applied configuration to the startup configuration so that the changes persist after the reboot, you must run the `nv config save` command. The auto save option lets you save the pending configuration to the startup configuration automatically when you run `nv config apply` so that you do not have to run the `nv config save` command.

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
