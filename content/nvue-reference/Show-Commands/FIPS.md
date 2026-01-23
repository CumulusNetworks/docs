---
title: FIPS
author: Cumulus Networks
weight: 175

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system security fips</h>

Shows if FIPS mode is enabled. The default mode is `disabled`.

### Version History

Introduced in Cumulus Linux 5.16.0

### Example

```
cumulus@switch:~$ nv show system security fips
                           operational  applied
-------------------------  -----------  -------
mode                       enabled      enabled
```
