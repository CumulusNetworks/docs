---
title: PTM
author: Cumulus Networks
weight: 300

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show router ptm</h>

Shows if PTM check link state is on or off. When on, PTM performs additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that `ptmd` defines.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show router ptm
        applied  pending
------  -------  -------
enable  off      off
```
