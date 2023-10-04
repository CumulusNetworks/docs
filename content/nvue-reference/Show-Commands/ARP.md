---
title: ARP
author: Cumulus Networks
weight: 127

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global arp</h>

Shows ARP settings, such as the neighbor base reachable timer and garbage collection settings.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system global arp
                              operational  applied
----------------------------  -----------  -------
base-reachable-time           50           50   
garbage-collection-threshold                      
  effective                   35840               
  maximum                     40960               
  minimum                     128            
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global arp garbage-collection-threshold</h>

Shows the ARP garbage collection threshold settings.

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show system global arp garbage-collection-threshold
           operational  applied
---------  -----------  -------
effective  35840               
maximum    40960               
minimum    128           
```
