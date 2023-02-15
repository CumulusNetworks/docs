---
title: PTM Commands
author: Cumulus Networks
weight: 237
product: Cumulus Linux
type: nojsscroll
---
## nv show router ptm

Shows if PTM check link state is enabled. When enabled, PTM perfoms additional checks to ensure that routing adjacencies form only on links that have connectivity and that conform to the specification that `ptmd` defines.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@leaf04:mgmt:~$ nv show router ptm
```
