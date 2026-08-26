---
title: Firmware
author: Cumulus Networks
weight: 566

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform firmware /<platform-component-id/> auto-update</h>

Configures whether Cumulus Linux automatically updates the staged files for a platform firmware component, and whether a component uses the default firmware source or a custom one you staged yourself.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<platform-component-id>` |  The platform component. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set platform firmware BIOS auto-update enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform firmware /<platform-component-id/> fw-source</h>

Configures whether a component uses the default firmware source or a custom one.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<platform-component-id>` |  The platform component. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set platform firmware ASIC fw-source custom
```
