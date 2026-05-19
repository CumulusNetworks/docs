---
title: cl-support File
author: Cumulus Networks
weight: 535

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system tech-support auto-generation burst-duration</h>

Configures the number of seconds during which failures are counted before automatic `cl-support` file generation deactivates.

`cl-support` files can generate in quick succession due to a chain of faults, which burdens system resources and causes system instability. When this occurs, the switch deactivates automatic `cl-support` file generation and preserves the first `cl-support` file (which contains relevant diagnostic information) for troubleshooting.

You can reactivate automatic `cl-support` file generation with the `nv action activate system tech-support auto-generation` command.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system tech-support auto-generation burst-duration 120
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system tech-support auto-generation burst-size</h>

Configures the maximum number of failures allowed during the burst duration time before automatic `cl-support` file generation deactivates.

`cl-support` files can generate in quick succession due to a chain of faults, which burdens system resources and causes system instability. When this occurs, the switch deactivates automatic `cl-support` file generation and preserves the first `cl-support` file (which contains relevant diagnostic information) for troubleshooting.

You can reactivate automatic `cl-support` file generation with the `nv action activate system tech-support auto-generation` command.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system tech-support auto-generation burst-size 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system tech-support auto-generation state</h>

Enables and disables automatic `cl-support` file generation.

The switch generates the `cl-support` file automatically:
- When there is a core dump file in the `/var/support/core` directory for any application that Linux distributions support.
- When one of the monitored services fails for the first time after you reboot or power cycle the switch.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv set system tech-support auto-generation state disabled
```
