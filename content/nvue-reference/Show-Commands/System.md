---
title: System
author: Cumulus Networks
weight: 385

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system</h>

Shows information about the switch, such as the hostname, Cumulus Linux version, the switch uptime, and the time zone.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system
          operational          applied
--------  -------------------  -------
hostname  leaf01               leaf01 
build     Cumulus Linux 5.5.0         
uptime    3 days, 18:40:31            
timezone  Etc/UTC
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system counter polling-interval</h>

Shows the polling interval for the switch counters for both the logical and physical interfaces.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system counter polling-interval
                   applied
------------------  -------
logical-interface   0:00:05
physical-interface  0:00:02
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system cpu</h>

Shows information about the switch CPU, such as the core-count, the model, and the utilization percentage.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system cpu
             operational                    applied
-----------  -----------------------------  -------
core-count   1                                     
model        QEMU Virtual CPU version 2.5+         
utilization  100.0%
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system date-time</h>

Shows the current date and time on the switch software clock.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system date-time
                           operational                  
-------------------------  -----------------------------
local-time                 Wed 2023-11-22 11:22:54 EST  
universal-time             Wed 2023-11-22 16:22:54 UTC  
rtc-time                   Wed 2023-11-22 16:22:54      
time-zone                  America/New_York (EST, -0500)
system-clock-synchronized  no                           
ntp-service                inactive                     
rtc-in-local-tz            no                           
unix-time                  1700670174.4371066
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system forwarding profile-option</h>

Shows forwarding profile information.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system forwarding profile-option
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global</h>

Shows global system configuration, such as the anycast ID, anycast MAC address, fabric ID, fabric MAC address, system MAC address, routing table, VLAN, and VNI information.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system global
                 operational        applied          
---------------  -----------------  -----------------
anycast-id       none               none             
anycast-mac      44:38:39:BE:EF:AA  44:38:39:BE:EF:AA
fabric-id        1                  1                
fabric-mac       none               none             
system-mac       44:38:39:22:01:7a  44:38:39:22:01:7a
l3svd                                                
  enable         off                off              
reserved                                             
  routing-table                                      
    pbr                                              
      begin      10000              10000            
      end        4294966272         4294966272       
  vlan                                               
    internal                                         
      range      3725-3999          3725-3999        
    l3-vni-vlan                                      
      begin      4000               4000             
      end        4064               4064
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global reserved</h>

Shows global reserved configuration information, such as the VLAN internal range.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system global reserved
               operational  applied   
-------------  -----------  ----------
routing-table                         
  pbr                                 
    begin      10000        10000     
    end        4294966272   4294966272
vlan                                  
  internal                            
    range      3725-3999    3725-3999 
  l3-vni-vlan                         
    begin      4000         4000      
    end        4064         4064
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global reserved routing-table</h>

Shows global reserved routing table information.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system global reserved routing-table
         operational  applied   
-------  -----------  ----------
pbr                             
  begin  10000        10000     
  end    4294966272   4294966272
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global reserved vlan</h>

Shows the reserved VLAN configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system global reserved vlan
             operational  applied  
-----------  -----------  ---------
internal                           
  range      3725-3999    3725-3999
l3-vni-vlan                        
  begin      4000         4000     
  end        4064         4064
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global reserved vlan internal</h>

Shows the reserved internal VLAN configuration settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system global reserved vlan internal
       operational  applied  
-----  -----------  ---------
range  3725-3999    3725-3999
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system global reserved vlan l3-vni-vlan</h>

Shows the reserved VLAN layer 3 VNI to VLAN mapping settings.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system global reserved vlan l3-vni-vlan
       operational  applied
-----  -----------  -------
begin  4000         4000   
end    4064         4064
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system maintenance</h>

Show the current system maintenance mode.

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show system maintenance 
       operational
-----  ----------- 
mode   disabled            
ports  enabled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system memory</h>

Shows information about the switch memory, such as the total amount of memory, the amount of free and used memory, and the percent of memory utilized.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system memory
Type      Buffers   Cache      Free       Total    Used       Utilization
--------  --------  ---------  ---------  -------  ---------  -----------
Physical  36.32 MB  521.31 MB  236.07 MB  1.69 GB  935.82 MB  86.4%      
Swap                           0 Bytes    0 Bytes  0 Bytes    0.0%
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system message</h>

Shows pre- and post-login messages.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system message
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system reboot</h>

Shows system reboot information, such as the time when the switch rebooted, the reason for the reboot, and the restart mode (fast, warm, cold).

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system reboot
          operational                       applied
---------  --------------------------------  -------
reason                                              
  gentime  2023-04-26T15:47:34.033663+00:00         
  reason   Unknown                                  
  user     system/root                              
mode       cold                              cold
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system reboot history</h>

Shows the system reboot history.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system reboot history
    gentime                           reason   user       
--  --------------------------------  -------  -----------
1   2023-04-26T15:47:34.033663+00:00  Unknown  system/root
2   2023-04-26T15:38:12.317900+00:00  Unknown  system/root
3   2023-04-26T15:38:09.769047+00:00  Unknown  system/root
4   2023-04-26T15:38:02.208193+00:00  Unknown  system/root
5   2023-04-25T01:30:36.145781+00:00  Unknown  system/root
6   2023-04-25T01:30:32.430332+00:00  Unknown  system/root
7   2023-04-25T01:30:22.843263+00:00  Unknown  system/root
8   2023-04-25T01:26:10.124076+00:00  Unknown  system/root
9   2023-04-25T01:26:06.517457+00:00  Unknown  system/root
10  2023-04-25T01:25:53.811710+00:00  Unknown  system/root
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system reboot reason</h>

Shows the reason why the switch rebooted.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show system reboot reason
        operational                       applied
-------  --------------------------------  -------
gentime  2023-04-26T15:47:34.033663+00:00         
reason   Unknown                                  
user     system/root
```
