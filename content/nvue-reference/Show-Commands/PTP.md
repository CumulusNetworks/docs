---
title: PTP
author: Cumulus Networks
weight: 310

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show bridge domain \<domain-id\> vlan \<vid\> ptp</h>

Shows PTP configuration and counters for a specific VLAN interface on the specified bridge domain.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<domain-id>`   |  The bridge domain. |
| `<vid-id>`   |  The VLAN name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show bridge domain br_default vlan 10 ptp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> counters ptp</h>

Shows PTP statistics for the specified interface.

{{%notice note%}}
In Cumulus Linux 5.4 and earlier, this command is `nv show interface <interface-id> ptp counters`
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show interface swp1 counters ptp
       operational  applied
------  -----------  -------
enable  on           on     
cumulus@leaf03:mgmt:~$ nv show interface swp1 counters ptp
Packet Type          Received  Transmitted
-------------------  --------  -----------
Announce             0         663        
Delay Request        0         0          
Delay Response       0         0          
Follow-up            0         1325       
Management           0         0          
Peer Delay Request   0         0          
Peer Delay Response  0         0          
Signaling            0         0          
Sync                 0         1325
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ptp</h>

Shows PTP configuration and counters for the specified interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ptp
                          operational  applied  pending   
------------------------  -----------  -------  ----------
enable                                          on        
acceptable-master                               off       
delay-mechanism                                 end-to-end
forced-master                                   off       
instance                                        1         
mixed-multicast-unicast                         off       
ttl                                             1         
unicast-request-duration                        300       
shaper                                                    
  enable                                        off       
timers                                                    
  announce-interval                             1         
  announce-timeout                              3         
  delay-req-interval                            0         
  sync-interval                                 0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ptp shaper</h>

Shows if PTP shaper is ON or OFF on the specified PTP interface.

{{%notice note%}}
This command is available for the NVIDIA Spectrum 1 switch only for PTP-enabled ports with speeds lower than 100G.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ptp shaper
        operational  applied  pending
------  -----------  -------  -------
enable                        off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> ptp timers</h>

Shows PTP timer settings for the specified PTP interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>`   |  The interface name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show interface swp1 ptp timers
                    operational  applied  pending
------------------  -----------  -------  -------
announce-interval                         1      
announce-timeout                          3      
delay-req-interval                        0      
sync-interval                             0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp</h>

Shows global PTP configuration.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp
id  Clock-id                 Enabled  Domain  Priority1  Priority2
--  -----------------------  -------  ------  ---------  ---------
1   48:b0:2d:ff:fe:0a:67:46  on       28      128        128
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\></h>

Shows configuration for the specified PTP instance. PTP commands require an instance number for management purposes.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1
cumulus@switch:~$ nv show service ptp 1
                             operational  applied
---------------------------  -----------  ------------------
enable                       on           on
current-profile                           default-itu-8275-2
domain                                    0
ip-dscp                                   46
logging-level                             info
priority1                                 128
priority2                                 128
[acceptable-master]
monitor
  max-offset-threshold                    50
  max-timestamp-entries                   100
  max-violation-log-entries               4
  max-violation-log-sets                  2
  min-offset-threshold                     -50
  path-delay-threshold                    200
  violation-log-interval                  1
[profile]                                 abc
[profile]                                 default-1588
[profile]                                 default-itu-8275-1
[profile]                                 default-itu-8275-2
[unicast-master]                          1
[unicast-master]                          2
[unicast-master]                          3
[unicast-master]                          4
[unicast-master]
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> acceptable-master</h>

Shows the acceptable master clocks for the specified PTP instance.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 acceptable-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> acceptable-master \<clock-id\></h>

Shows the configuration settings for the specified acceptable master clock.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<clock-id>`  |  The clock ID. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 acceptable-master 24:8a:07:ff:fe:f4:16:06
              operational  applied
------------  -----------  -------
alt-priority  255          255
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> counters</h>

Shows all PTP counters, such as the number of received and transmitted announce, sync, followup, and delay request and response packets.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.6.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 counters
Packet Type              Received       Transmitted    
---------------------    ------------   ------------   
Port swp4
  Announce                 0              10370            
  Sync                     0              20731             
  Follow-up                0              20731            
  Delay Request            0              0              
  Delay Response           0              0              
  Peer Delay Request       0              0              
  Peer Delay Response      0              0              
  Management               0              0              
  Signaling                0              0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> current</h>

Shows the local states learned from the exchange of PTP messages for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 current
                    operational  applied
------------------  -----------  -------
mean-path-delay     0                   
offset-from-master  0                   
steps-removed       0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> clock-quality</h>

Shows the clock quality status, such as accuracy, class and the offset scaled log variance, for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 clock-quality
                            operational  applied
--------------------------  -----------  -------
clock-accuracy              254                 
clock-class                 248                 
offset-scaled-log-variance  65535
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> force-version</h>

Shows the PTP version. Cumulus Linux uses a `linuxptp` package that is PTP v2.1 compliant, and sets the major PTP version to 2 and the minor PTP version to 1 by default in the configuration. If your PTP configuration does not work correctly when the minor version is set, you can change the minor version to 0.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 force-version
               applied
-------------  -------
force-version  2.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor</h>

Shows the PTP monitor configuration for the specified PTP instance, such as:
- The minimum and maximum difference allowed between the master and slave time.
- The mean time that PTP packets take to travel between the master and slave.
- The maximum number of timestamp entries allowed.
- The maximum number of violation log sets allowed.
- The maximum number of violation log entries allowed for each set.
- The violation log interval.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor
                           operational  applied
-------------------------  -----------  -------
max-offset-threshold       50           50     
max-timestamp-entries      100          100    
max-violation-log-entries  4            4      
max-violation-log-sets     2            2      
min-offset-threshold       -50          -50    
path-delay-threshold       200          200    
violation-log-interval     1            1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor timestamp-log</h>

Shows the monitor timestamp log for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor timestamp-log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations</h>

Shows the PTP violations for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations
 cumulus@switch:~$ nv show service ptp 1 monitor violations
                  operational                  applied
----------------  ---------------------------  -------
last-max-offset
last-min-offset   2023-04-24T15:22:01.312295Z
last-path-delay
max-offset-count  0
min-offset-count  2
path-delay-count  0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log</h>

Shows all the PTP violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations log
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log acceptable-master</h>

Shows the acceptable master violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations log acceptable-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log forced-master</h>

Shows the forced master violation logs for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations log forced-master
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log max-offset</h>

Shows violation logs for the maximum difference allowed between the master and slave time for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations log max-offset
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log min-offset</h>

Shows violation logs for the minimum difference allowed between the master and slave time for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations log min-offset
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> monitor violations log path-delay</h>

Shows violation logs for the mean time that PTP packets take to travel between the master and slave for the specified PTP instance.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 monitor violations log path-delay
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> parent</h>

Shows global PTP parent information.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 parent
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> parent grandmaster-clock-quality</h>

Shows the grandmaster clock quality for the PTP parent.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 parent grandmaster-clock-quality
                            operational  applied
--------------------------  -----------  -------
clock-accuracy              254                 
clock-class                 248                 
offset-scaled-log-variance  65535
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> profile</h>

Shows the predefined and custom PTP profiles configured for the specified PTP instance. Predefined profiles are a standardized set of configurations and rules intended to meet the requirements of a specific application. You base a custom profile off a predefined profile. Profiles define required, allowed, and restricted PTP options, network restrictions, and performance requirements.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 profile
Profile Name        Type          Domain  Transport  Delay Mechanism
------------------  ------------  ------  ---------  ---------------
default-1588        ieee-1588     0       ipv4       end-to-end     
default-itu-8275-1  itu-g-8275-1  24      802.3      end-to-end     
default-itu-8275-2  itu-g-8275-2  44      ipv4       end-to-end 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> profile \<profile-id\></h>

Shows configuration settings for a specific PTP profile.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 profile CUSTOM1
                    operational   applied     
------------------  ------------  ------------
announce-interval   -3            -3          
announce-timeout    3             3           
delay-mechanism     end-to-end    end-to-end  
delay-req-interval  -4            -4          
domain              28            28          
local-priority      128           128         
priority1           128           128         
priority2           128           128         
profile-type        itu-g-8275-1  itu-g-8275-1
sync-interval       -4            -4          
transport           802.3         802.3
```
<!--
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> servo</h>

Shows the Noise Transfer Servo configuration settings.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.7.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 servo
       operational  applied
-----  -----------  --------------
servo               noise-transfer
```
-->
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> status</h>

Shows PTP status.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | The PTP instance number. |

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 status
Port   Mode   State    Ustate                           Server
-----  -----  -------  -------------------------------  -------
swp9   Ucast  SLAVE    Sync and Delay Granted (H_SYDY)  9.9.9.2
swp10  Ucast  PASSIVE  Initial State (WAIT)
swp11  Ucast  PASSIVE  Initial State (WAIT)
swp12  Ucast  PASSIVE  Initial State (WAIT)
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> time-properties</h>

Shows time properties for the specified PTP instance, such as the current UTC offset and the PTP time scale.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>` | The PTP instance number. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 time-properties
                          operational  applied
------------------------  -----------  -------
current-utc-offset        37                  
current-utc-offset-valid  off                 
freq-traceable            off                 
leap59                    off                 
leap61                    off                 
ptp-time-scale            off                 
time-traceable            off
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master</h>

Shows the PTP unicast master table configuration on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master
Table-id  Address     Peer-address  Query-interval
--------  ----------  ------------  --------------
1         10.10.10.1                4
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master \<table-id\></h>

Shows information about a specific PTP unicast master table on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<table-id>`  | The unicast master table ID.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1
                operational  applied   
--------------  -----------  ----------
query-interval  4            4         
[address]       10.10.10.1   10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master \<table-id\> address</h>

Shows the IP addresses of the specified PTP unicast master table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<table-id>`  | The unicast master table ID.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1 address
IP or MAC Address
-----------------
10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show service ptp \<instance-id\> unicast-master \<table-id\> address \<ip-mac-address-id\></h>

Shows information about a specific IP or MAC address for the specified PTP unicast master table.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<instance-id>`  | The PTP instance number.|
| `<table-id>`  | The unicast master table ID.|
| `<ip-mac-address-id>`  | The IP or MAC address.|

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show service ptp 1 unicast-master 1 address 10.10.10.1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show vrf \<vrf-id\> ptp</h>

Shows PTP configuration for the specified VRF.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<vrf-id>` | The VRF name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show vrf default ptp
        operational  applied
------  -----------  -------
enable  on           on
```
