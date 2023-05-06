---
title: PTM
author: Cumulus Networks
weight: 670
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set router ptm

Provides commands to configure Prescriptive Topology Manager (PTM).

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set router ptm enable</h>

Turns PTM on or off. When on, PTM performs additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that `ptmd` defines.

The default setting is `off`.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf01:mgmt:~$ nv set router ptm enable on
```
