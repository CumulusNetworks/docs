---
title: RADIUS
author: Cumulus Networks
weight: 325

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa radius</h>

Shows the RADIUS configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system aaa radius
                 operational    applied      
---------------  -------------  -------------
enable           on             on           
vrf              mgmt           mgmt         
debug            enabled        enabled      
privilege-level  10             10           
retransmit       8              8            
port                            1812         
timeout                         10           
source-ipv4                     192.168.1.10 
[server]         192.168.0.254  192.168.0.254 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa radius server</h>

Shows a list of the RADIUS servers configured on the switch and their configuration settings.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system aaa radius server
Hostname       Port  Priority  Password  source-ip     Timeout
-------------  ----  --------  --------  ------------  -------
192.168.0.254  42    1         *         192.168.1.10  10
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system aaa radius server \<hostname-id\></h>

Shows configuration settings for a specific RADIUS server.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<hostname-id>` | The IP address or hostname of the RADIUS server. |

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system aaa radius server 192.168.0.254
           operational   applied     
---------  ------------  ------------
port       42            42          
timeout    10            10          
secret     *             *           
priority   1             10          
source-ip  192.168.1.10  192.168.1.10
```
