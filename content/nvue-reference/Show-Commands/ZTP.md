---
title: ZTP
author: Cumulus Networks
weight: 470

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ztp</h>

Shows information about <span class="a-tooltip">[ZTP](## "Zero Touch Provisioning")</span> scripts on the switch, such as location and version, the date the script was run, and if it was a success.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system ztp
            operational                                   applied
----------  --------------------------------------------  -------
script                                                           
  location  /var/lib/cumulus/ztp/ztp_script-202304261538         
status                                                           
  date      2023-04-26T15:38:42Z                                 
  method    ZTP DHCP                                             
  result    success                                              
  state     disabled                                             
  url       http://192.168.200.1/cumulus-ztp                     
  version   1.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ztp script</h>

Shows the location of the ZTP script on the switch.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system ztp script
          operational                                   applied
--------  --------------------------------------------  -------
location  /var/lib/cumulus/ztp/ztp_script-202304261538
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system ztp status</h>

Shows the status of the ZTP script run on the switch.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system ztp status
         operational                       applied
-------  --------------------------------  -------
date     2023-04-26T15:38:42Z                     
method   ZTP DHCP                                 
result   success                                  
state    disabled                                 
url      http://192.168.200.1/cumulus-ztp         
version  1.0
```
