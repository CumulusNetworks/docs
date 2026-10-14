---
title: System Maintenance
author: Cumulus Networks
weight: 771

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set maintenance unit all-interfaces mode</h>

Puts all ports in maintenance mode. When you put all ports in maintenance mode, all the ports go into the link down state.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set maintenance unit all-interfaces mode enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set maintenance unit all-interfaces mode disabled</h>

Takes all ports out of maintenance and put them in production.

When you take all ports out of maintenance and put them in production, all the ports move out of the link down state.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set maintenance unit all-interfaces mode disabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set maintenance unit all-protocols mode enabled</h>

Puts all protocols in maintenance mode.

When you put all protocols in maintenance mode:
- All the protocols that support graceful shutdown perform graceful shutdown with all their neighbors.
- The switch goes through a warmboot when rebooted if the switch is in warm mode or when you do a warmboot to upgrade software to the next release.

If the protocols have done a graceful shutdown while going into maintenance, but some of the neighbors do not have alternate paths, those neighbors continue to send traffic through this switch. That traffic continues to flow through this switch through the warmboot operation. All protocols continue to remain in maintenance mode through the warmboot operation.

All the protocols that support graceful shutdown re-advertise the routes with a lower weight or preference.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set maintenance unit all-protocols mode enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set maintenance unit all-protocols mode disabled</h>

Takes all protocols out of maintenance and put them back into production. All the protocols that support graceful shutdown re-advertise the routes with the original weight or preference.

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv set maintenance unit all-protocols mode disabled
```
