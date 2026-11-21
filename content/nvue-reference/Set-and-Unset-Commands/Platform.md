---
title: Platform
author: Cumulus Networks
weight: 830

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>

{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform firmware \<platform-component-id\></h>

Configures the firmware settings for the specified platform component.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<platform-component-id>` |  The platform component. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set platform firmware BIOS
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set platform firmware \<platform-component-id\> auto-update</h>

Enables and disables automatic firmware updates for the specified platform component. You can set a value of `enabled`, or `disabled`.

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

## <h>nv set platform firmware \<platform-component-id\> fw-source</h>

Configures the firmware source for the specified platform component. You can set a value of `default`, or `custom`.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<platform-component-id>` |  The platform component. |

### Version History

Introduced in Cumulus Linux 5.19.0

### Example

```
cumulus@switch:~$ nv set platform firmware BIOS fw-source custom
```
