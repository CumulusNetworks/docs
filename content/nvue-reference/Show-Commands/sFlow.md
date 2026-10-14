---
title: sFlow
author: Cumulus Networks
weight: 355

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow</h>

Shows all sFlow configuration on the switch.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow
                operational  applied    
-------------  -----------  -----------
poll-interval               20         
state                       enabled    
[collector]                 192.0.2.100
[collector]                 192.0.2.200
sampling-rate                          
  default                   400        
  speed-100m                100        
  speed-1g                  1000       
  speed-10g                 10000      
  speed-25g                 25000      
  speed-40g                 40000      
  speed-50g                 50000      
  speed-100g                100000     
  speed-200g                200000     
  speed-400g                400000     
  speed-800g                800000     
agent                                  
  ip                        10.0.0.0/8 
  interface                 eth0       
policer                                
  rate                      8000       
  burst                     9000       
[dropmon]                   sw
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow collector</h>

Shows sFlow collector configuration.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow collector
Ip                    Port 
--------------------------------- 
192.0.2.100           6343 
192.0.2.200           6344
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow collector \<collector-ip\></h>

Shows configuration settings for a specific sFlow collector.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<collector-ip>`    |  The IP address of the sFlow collector. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow collector 192.0.2.100
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow sampling-rate</h>

Shows the sFlow sampling rate configuration.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow sampling-rate
            applied
----------  -------
default     400    
speed-100m  100    
speed-1g    1000   
speed-10g   10000  
speed-25g   25000  
speed-40g   40000  
speed-50g   50000  
speed-100g  100000 
speed-200g  200000 
speed-400g  400000 
speed-800g  800000 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow agent</h>

Shows sFlow agent configuration.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow agent
           operational  applied   
---------  -----------  ----------
ip                      10.0.0.0/8
interface               eth0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow policer</h>

Shows the number of sFlow samples per second and the sample burst size per second that the switch can send.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow policer
---------------------- 
       applied
-----  -------
rate   8000   
burst  9000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system sflow dropmon hw</h>

Shows information for dropped packets in hardware.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show system sflow dropmon hw
```
