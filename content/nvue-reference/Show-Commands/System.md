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

## <h>nv show maintenance</h>

Show the current maintenance state of the switch.

{{%notice note%}}
Cumulus Linux 5.12 and earlier does not provide this command; run the `nv show system maintenance` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show maintenance 
Maintenance Info 
============== 
Unit                                 State 
-----------------------              --------------- 
all-protocols                        maintenance 
all-interfaces                       maintenance 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show maintenance unit all-protocols</h>

Shows the current maintenance state of the protocols.

{{%notice note%}}
Cumulus Linux 5.12 and earlier does not provide this command; run the `nv show system maintenance unit all-protocols` command instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.13.0

### Example

```
cumulus@switch:~$ nv show maintenance unit all-protocols
              operational      applied 
----------    -----------      ----------- 
state         maintenance       maintenance 
interfaces
protocols             all 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system</h>

Shows information about the switch, such as the hostname, version information, the switch uptime, time zone, memory, and health status.

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv show system
uptime             1 day, 1:52:24                                                 
hostname           leaf01 
product-name       Cumulus Linux                                                  
platform           N/A                                                            
system-memory      1.31 GB used / 363.36 MB free / 1.67 GB total                  
swap-memory        0 Bytes used / 0 Bytes free / 0 Bytes total                    
health-status      Not OK                                                         
date-time          2025-04-18 12:48:46                                            
status             N/A                                                            
timezone           Etc/UTC                                                        
version                                                                           
  onie             N/A                                                            
  kernel           6.1.0-cl-1-amd64                                               
  base-os          Debian GNU/Linux 12.10                                         
```

Cumulus Linux 5.12 and earlier also shows build and product-release fields. NVUE removed these fields in Cumulus Linux 5.13.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system cli</h>

Shows the current CLI settings. CLI settings include timeout and pager configuration.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show system cli
                  applied
----------------  -------
inactive-timeout  300  
pagination               
  state           enabled
  pager           more
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system cli pagination</h>

Shows if the pager is enabled and the configured pager settings (`more`, `less`, or `vim`.)

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show system cli pagination
       applied
-----  -------
state  enabled
pager  more
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system counter</h>

Shows the polling interval for the switch counters for both the logical and physical interfaces.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv show system counter
                      applied
--------------------  -------
polling-interval             
  logical-interface   0:00:05
  physical-interface  0:00:02
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system counter rates</h>

Shows the load interval for the switch counters for both the logical and physical interfaces.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system counter rates 
               applied
-------------  -------
load-interval  6
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

{{%notice note%}}
In Cumulus Linux 5.14 and earlier, this command is `nv show system time`.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.15.0

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

## <h>nv show system disk usage </h>

Shows disk utilization.

### Version History

Introduced in Cumulus Linux 5.12.0

### Example

```
cumulus@switch:~$ nv show system disk usage 
Mount Point  Filesystem  Size  Used  Avail  Use%
-----------  ----------  ----  ----  -----  ----
/            /dev/vda5   5.4G  2.5G  2.7G   49% 
/dev         udev        847M  0     847M   0%  
/dev/shm     tmpfs       856M  31M   825M   4%  
/run         tmpfs       172M  1.4M  170M   1%  
/run/lock    tmpfs       5.0M  0     5.0M   0%  
/tmp         tmpfs       856M  8.0K  856M   1% 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker</h>

Shows Docker information on the switch.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker
       operational  applied
-----  -----------  -------
vrf    mgmt         mgmt   
state  enabled      enabled

Docker Containers
====================
    Container Name      Image                            Container ID  Status               Ports  Summary
    ------------------  -------------------------------  ------------  -------------------  -----  -------
    repo                cumulus-linux-apt-mirror:5.15.0  a941e1e51c3e  Up 6 days (healthy)                
    what-just-happened  docker-wjh:latest                f834edf7fd3c  Up 7 days 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker image</h>

Shows Docker images present on the switch.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker image
Image Id      Image Name                Tag     Size    Date                           Summary
------------  ------------------------  ------  ------  -----------------------------  -------
283e2bf92e80  docker-wjh                latest  716MB   2025-10-29 21:47:09 -0400 EDT         
d839322a5483  cumulus-linux-apt-mirror  5.15.0  3.47GB  2025-10-30 02:35:30 -0400 EDT 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker container</h>

Shows all containers and their status, including stopped containers.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker container
Container Name      Image                            Container ID  Status               Ports  Summary
------------------  -------------------------------  ------------  -------------------  -----  -------
repo                cumulus-linux-apt-mirror:5.15.0  a941e1e51c3e  Up 6 days (healthy)                
what-just-happened  docker-wjh:latest                f834edf7fd3c  Up 7 days
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker container stats</h>

Shows all container statistics.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker container stats
Container Name      CPU%   MEM USAGE  MEM LIMIT  MEM%   NET I/O  BLOCK I/O       PIDS
------------------  -----  ---------  ---------  -----  -------  --------------  ----
repo                0.00%  8.102MiB   15.02GiB   0.05%  0B / 0B  160kB / 41kB    9   
what-just-happened  0.05%  81.96MiB   15.02GiB   0.53%  0B / 0B  496kB / 16.4kB  9
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system docker engine</h>

Shows Docker engine configuration.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system docker engine
                operational                                                                                    
--------------  -----------------------------------------------------------------------------------------------
client                                                                                                         
  name          Docker Engine - Community                                                                      
  version       28.5.1                                                                                         
  context       default                                                                                        
server                                                                                                         
  containers    2                                                                                              
  running       2                                                                                              
  paused        0                                                                                              
  stopped       0                                                                                              
plugins                                                                                                        
  volume        ['local']                                                                                      
  network       ['bridge', 'host', 'ipvlan', 'macvlan', 'null', 'overlay']                                     
  log           ['awslogs', 'fluentd', 'gcplogs', 'gelf', 'journald', 'json-file', 'local', 'splunk', 'syslog']
images          2                                                                                              
server-version  28.5.1                                                                                         
id              ae4be5b9-6806-435d-80cb-5e4548a9c11a                                                           
init-binary     docker-init                                                                                    
data-root       /docker                                                                                        
debug-mode      False                                                                                          
log-level       json-file
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

## <h>nv show system global </h>

Shows if the `svi-force-up` option is set to `on` for all SVIs on the switch.

The first time you configure a switch, all southbound bridge ports are down; therefore, by default, all SVIs are also down. You can force all SVIs to always be UP with the `nv set system global svi-force-up enable on` option, which is beneficial if you want to perform connectivity testing.

### Version History

Introduced in Cumulus Linux 5.8.0

### Example

```
nv show system global svi-force-up
       operational  applied
------  -----------  -------
enable  on           on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system health</h>

Shows system health information.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system health 
            operational  applied
----------  -----------  -------
status      OK                  
status-led  green               

Health issues
================
No Data
```

In 5.13 and later the nv show system health command output is:

```
nv show system health 
            operational  applied  
----------  -----------  -------
status      Not OK                       
status-led  amber                        

Health issues
================
    Component           Status information                                         
    ------------------  -----------------------------------------------------------
    ASIC                Not OK                                                     
    forwarding          active (running) since Wed 2025-04-23 17:44:13 UTC; 12h ago
    hw-management       inactive                                                   
    hw-management-sync  inactive                                                   
    hw-management-tc    inactive                                                   
    mft                 inactive                                                   
    process             Not OK
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system health history</h>

Shows system health history. Press q to exit the history.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system health history
[2025-11-01T15:45:49.265284] INFO: Fan1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.291928] INFO: Fan2 initialized to OK: Value: N/A
[2025-11-01T15:45:49.293223] INFO: Fan3 initialized to OK: Value: N/A
[2025-11-01T15:45:49.294401] INFO: Fan4 initialized to OK: Value: N/A
[2025-11-01T15:45:49.295561] INFO: Fan5 initialized to OK: Value: N/A
[2025-11-01T15:45:49.297519] INFO: Fan6 initialized to OK: Value: N/A
[2025-11-01T15:45:49.298587] INFO: PSU1Fan1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.302107] INFO: PSU2Fan1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.303410] INFO: Temp1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.304783] INFO: Temp2 initialized to OK: Value: N/A
[2025-11-01T15:45:49.306142] INFO: Temp3 initialized to OK: Value: N/A
[2025-11-01T15:45:49.307599] INFO: Temp4 initialized to OK: Value: N/A
[2025-11-01T15:45:49.308990] INFO: Temp5 initialized to OK: Value: N/A
[2025-11-01T15:45:49.310387] INFO: PSU1Temp1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.311783] INFO: PSU2Temp1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.313159] INFO: PSU1 initialized to OK: Value: N/A
[2025-11-01T15:45:49.314894] INFO: PSU2 initialized to OK: Value: N/A
[2025-11-01T15:45:49.616534] INFO: ThermalAlarm initialized to OK
[2025-11-01T15:45:49.629542] INFO: CpuStatus initialized to OK
[2025-11-01T15:45:49.636946] INFO: MemoryStatus initialized to OK: Memory usage: 49%
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system health history files</h>

Shows a list of the health history report files on the switch and their location.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system health history files
Health history file report  File path                  Summary
--------------------------  -------------------------  -------
health_history              /var/log/health_history           
health_history.1            /var/log/health_history.1         
health_history.2            /var/log/health_history.2         
health_history.3            /var/log/health_history.3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system health history files \<file-name\></h>

Shows the health history report in the specified file.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<file-name>` | The name of the health report file you want to see.|

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system health history files health_history
[2025-11-01T15:45:49.648197] INFO: ASIC initial state is Not OK: ASIC state: Not OK
[2025-11-01T16:44:51.539021] ERROR: MemoryStatus changed from OK to BAD: Memory usage: 91%
[2025-11-01T16:45:21.830564] Cleared: MemoryStatus changed from BAD to OK: Memory usage: 90%
[2025-11-01T16:47:02.825350] ERROR: MemoryStatus changed from OK to BAD: Memory usage: 91%
[2025-11-01T16:52:05.538832] Cleared: MemoryStatus changed from BAD to OK: Memory usage: 84%
[2025-11-03T15:05:02.640429] ERROR: MemoryStatus changed from OK to BAD: Memory usage: 92%
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system maintenance</h>

Show the current system maintenance mode.

{{%notice note%}}
Cumulus Linux 5.12 and earlier provides this command. For Cumulus Linux 5.13 and later use the `nv show maintenance` command instead.
{{%/notice%}}

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

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system reboot required</h>

Shows if you need to reboot the switch after upgrade.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show system reboot required
yes
```

<HR HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system serial-console</h>

Shows serial console configuration.

### Version History

Introduced in Cumulus Linux 5.15.0

### Example

```
cumulus@switch:~$ nv show system serial-console
                    operational  applied    
------------------  -----------  --------
sysrq-capabilities  disabled     disabled 
```

<HR HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show system version</h>

Shows the version information, such as kernel version and the Cumulus Linux release number.

### Version History

Introduced in Cumulus Linux 5.10.0

### Example

```
cumulus@switch:~$ nv show system version
            operational                 
----------  ----------------------------
kernel      6.1.0-cl-1-amd64            
build-date  Mon Jul 29 04:57:52 UTC 2024
image       5.10.0.0021                 
onie        N/A 
```
