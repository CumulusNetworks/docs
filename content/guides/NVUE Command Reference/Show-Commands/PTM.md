---
title: PTM
author: Cumulus Networks
weight: 300
product: Cumulus Linux
type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
## <h>nv show router ptm</h>

Shows if PTM check link state is enabled. When enabled, PTM performs additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that `ptmd` defines.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show router ptm
```
