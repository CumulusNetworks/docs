---
title: Platform
author: Cumulus Networks
weight: 270

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform</h>

Shows a list of all the software and hardware components on the switch.

In Cumulus Linux 5.9 and later, the `nv show platform` command shows only platform hardware information on the switch, such as the model and manufacturer, memory, Cumulus Linux release, serial number and system MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

In Cumulus Linux 5.8 and earlier:

```
cumulus@switch:~$ nv show platform
               operational                            applied  pending
-------------  -------------------------------------  -------  -------
software                                                              
  [installed]  acpi                                                   
  [installed]  acpi-support-base                                      
  [installed]  acpid                                                  
  [installed]  adduser                                                
  [installed]  apt                                                    
  [installed]  arping                                                 
  [installed]  arptables                                              
  [installed]  atftp                                                  
  [installed]  atftpd                                                 
  [installed]  audisp-tacplus                                         
  [installed]  auditd                                                 
  [installed]  babeltrace                                             
  [installed]  base-files                                             
  [installed]  base-passwd                                            
  [installed]  bash                                                   
  [installed]  bash-completion                                        
  [installed]  bind9-host                                             
  [installed]  binutils                                               
  [installed]  binutils-common                                        
  [installed]  binutils-x86-64-linux-gnu                              
  [installed]  bridge-utils                                           
  [installed]  bsdmainutils                                           
  [installed]  bsdutils                                               
  [installed]  busybox                                                
  [installed]  bwm-ng                                                 
  [installed]  bzip2
...
```

In Cumulus Linux 5.9 and later:

```
cumulus@switch:~$ nv show platform
               operational                            
-------------  ---------------------------------------
system-mac     44:38:39:22:01:b1                      
manufacturer   Cumulus                                
product-name   VX                                     
cpu            x86_64 QEMU Virtual CPU version 2.5+ x1
memory         1751856 kB                             
disk-size      n/a                                    
port-layout    n/a                                    
part-number    5.9.0                                  
serial-number  44:38:39:22:01:7a                      
asic-model     n/a                                    
system-uuid    b41196dc-78f1-4048-8079-f3c0fbeef739 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform asic resource

Shows both global and ACL ASIC resources.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform asic resource
Global 
========= 
    Resource Name             Count         Max        Percentage 
    ------------------                      -----      ---------
    IPv4-host-entries             4         32768      0% 
    IPv6-host-entries             4         8192       0% 
    IPv4-neighbors                4                    0% 
    IPv6-neighbors                4                    0% 
    IPv4-route-entries            22        65536      0% 
    IPv6-route-entries            21        45056      0% 
        IPv4-Routes               22                   0% 
    IPv6-Routes                   13                   0% 
    MAC-entries                   36        40960      0% 
    Total-Mcast-Routes             0        1000       0% 
    Ingress-ACL-entries            0                   0% 
    Egress-ACL-entries             0                   0% 
      Total-Routes                 43       110592     0% 
    ACL-Regions                    2        400        0% 
    ACL-18B-Rules-Key              2        3792       0% 
    ACL-36B-Rules-Key              0        1536       0% 
    ACL-54B-Rules-Key              0        1024       0% 
    ECMP-entries                   5                   0% 
    ECMP-nexthops                  8        7808       0% 
    Flow-Counters                  10       16196      0% 
       RIF-Basic-Counters          36       1000       3% 
    RIF-Enhanced-Counters          0        964        0% 
    Downstream-VNI-FID-count       0                   0% 
    Total-FID-count                3        6143       0% 
    Vport-FID-count                3                   0%
Acl 
====== 
    Resource Name                         18B Rule     36B Rule     54B Rule      Rule Count 
    ----------------------------          ----------   -----------  ----------     ------ 
    Egress-ACL-ipv4-filter-table           0           0               0            0 
    Egress-ACL-mac-filter-table            0           0               0            0 
    Ingress-ACL-mac-filter-table           0           0               0            0 
    Ingress-ACL-ipv4-filter-table          0           0               0            0 
    Ingress-ACL-ipv6-filter-table          0           0               0            0 
    Ingress-ACL-ipv4-mangle-table          1           0               0            1 
    Ingress-ACL-ipv6-mangle-table          0           0               0            0 
    Egress ACL-ipv4-mangle-table           1           0               0            1 
    Egress-ACL-ipv6-mangle-table           0           0               0            0 
    Ingress-PBR-ipv4-filter-table          0           0               0            0 
    Ingress-PBR-ipv6-filter-tabl           0           0               0            0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform asic resource acl

Shows global and ASIC resources.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform asic resource acl
Resource Name                        18B Rule     36B Rule     54B Rule    Rule Count 
    ----------------------------     ----------   ----------   ----------  -------- 
    Egress-ACL-ipv4-filter-table       0          0             0          0 
    Egress-ACL-mac-filter-table        0          0             0          0 
    Ingress-ACL-mac-filter-table       0          0             0          0 
    Ingress-ACL-ipv4-filter-table      0          0             0          0 
    Ingress-ACL-ipv6-filter-table      0          0             0          0 
    Ingress-ACL-ipv4-mangle-table      1          0             0          1 
    Ingress-ACL-ipv6-mangle-table      0          0             0          0 
    Egress ACL-ipv4-mangle-table      1           0             0          1 
    Egress-ACL-ipv6-mangle-table      0           0             0          0 
    Ingress-PBR-ipv4-filter-table     0           0             0          0 
    Ingress-PBR-ipv6-filter-tabl      0           0             0          0 
    Egress-ACL-ipv6-filter-table      0           0             0          0 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform asic resource global

Shows ACL ASIC resources.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform asic resource global
Resource Name                     Count   Max      Percentage 
    ------------------            -----   ----      ---------- 
    IPv4-host-entries             4       32768     0%
    IPv6-host-entries             4       8192      0% 
    IPv4-neighbors                4                 0% 
    IPv6-neighbors                4                 0% 
    IPv4-route-entries            22      65536     0% 
    IPv6-route-entries            21      45056     0% 
    IPv4-Routes                   22                0% 
    IPv6-Routes                   13                0% 
    MAC-entries                   36      40960     0% 
    Total-Mcast-Routes            0       1000      0% 
    Ingress-ACL-entries           0                 0% 
    Egress-ACL-entries            0                 0% 
    Total-Routes                  43      110592    0% 
    ACL-Regions                   2       400       0% 
    ACL-18B-Rules-Key             2       3792      0% 
    ACL-36B-Rules-Key             0       1536      0% 
    ACL-54B-Rules-Key             0       1024      0% 
    ECMP-entries                  5                 0% 
    ECMP-nexthops                 8       7808      0% 
    Flow-Counters                 10      16196     0% 
    Ingress-ACL-entries           0                 0% 
    RIF-Basic-Counters            36      1000      3% 
    RIF-Enhanced-Counters         0       964       0% 
    Downstream-VNI-FID-count      0                 0% 
    Total-FID-count               3       6143      0% 
    Vport-FID-count               3                 0%
    Dynamic-Config-DNAT-entries   0       64        0.0% 
    Dynamic-Config -SNAT-entries  0       64        0.0% 
    Dynamic-DNAT-entries          0       1024      0.0% 
    Dynamic-SNAT-entries          0       1024      0.0% 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform capabilities</h>

Shows the platform capabilities of the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform capabilities
                     operational  applied  pending
-------------------  -----------  -------  -------
single-vxlan-device  on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment</h>

Shows a list of sensors, fans, LEDs, and PSUs on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

In Cumulus Linux 5.6 and later, the command output shows the state of each item.

### Example

```
cumulus@switch:~$ nv show platform environment
[TYPE] Name         State
------------------  -----
[FAN] FAN1          ok   
[FAN] FAN2          ok   
[FAN] FAN3          ok   
[FAN] FAN4          ok   
[FAN] FAN5          ok   
[FAN] FAN6          ok   
[FAN] PSU1FAN1      ok   
[FAN] PSU2FAN1      ok   
[LED] FAN           ok   
[LED] POWER         ok   
[LED] SYSTEM        ok   
[PSU] PSU1          ok   
[PSU] PSU2          ok   
[SENSOR] PSU1TEMP1  ok   
[SENSOR] PSU2TEMP1  ok   
[SENSOR] TEMP1      ok   
[SENSOR] TEMP2      ok   
[SENSOR] TEMP3      ok   
[SENSOR] TEMP4      ok   
[SENSOR] TEMP5      ok   
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment fan</h>

Shows information about the fans on the switch, such as the minimum, maximum and current speed, the fan state.

{{%notice note%}}
In Cumulus 5.6, the `nv show platform environment fan` command also shows the fan direction. If the airflow for all fans is not in the same direction (front to back or back to front), cooling is suboptimal for the switch, rack, and even the entire data center.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

Cumulus Linux 5.5 and earlier:

```
cumulus@switch:~$ nv show platform environment fan
Name      Limit variance  Max Speed  Min Speed  Current Speed (RPM)  Fan State
--------  --------------  ---------  ---------  -------------------  ---------
Fan1                      29000      2500       6000                 ok       
Fan2                      29000      2500       6000                 ok       
Fan3                      29000      2500       6000                 ok       
Fan4                      29000      2500       6000                 ok       
Fan5                      29000      2500       6000                 ok       
Fan6                      29000      2500       6000                 ok       
PSU1Fan1                  29000      2500       6000                 ok       
PSU2Fan1                  29000      2500       6000                 ok
```

Cumulus Linux 5.6 and later (includes the fan direction):

```
cumulus@switch:~$ nv show platform environment fan
Name      Fan Direction  Limit variance  Max Speed  Min Speed  Current Speed (RPM)  Fan State
--------  -------------  --------------  ---------  ---------  -------------------  ---------
Fan1      F2B            15              29000      2500       6000                 ok       
Fan2      F2B            15              29000      2500       6000                 ok       
Fan3      F2B            15              29000      2500       6000                 ok       
Fan4      F2B            15              29000      2500       6000                 ok       
Fan5      F2B            15              29000      2500       6000                 ok       
Fan6      F2B            15              29000      2500       6000                 ok       
PSU1Fan1  F2B            15              29000      2500       6000                 ok       
PSU2Fan1  F2B            15              29000      2500       6000                 ok    
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment fan \<fan-id\></h>

Shows information about the specified fan on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<fan-id>` |   The physical fan identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment fan Fan2
           operational  applied  pending
---------  -----------  -------  -------
max-speed  29000                        
min-speed  2500                         
speed      6000                         
state      ok
```

In Cumulus Linux 5.6 and later, the command output also shows the limit variance.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment led</h>

Shows information about the LEDs on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment led
LED Name  LED Color
--------  ---------
Fan       green    
Power     green    
System    green
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment led \<led-id\></h>

Shows information about the specified LED.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<led-id>` |  The physical LED identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment led Fan
       operational  applied
-----  -----------  -------
color  green
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment psu</h>

Shows information about the PSUs on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment psu
Name  PSU State
----  ---------
PSU1  ok       
PSU2  ok
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment psu \<psu-id\></h>

Shows information about the specified PSU on the switch.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<psu-id>` |  The physical PSU identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment psu PSU1
       operational  applied
-----  -----------  -------
state  ok
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment sensor</h>

Shows information about the physical sensors on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment sensor
Sensor Name                         Critical Temp  Max Temp  Min Temp  Sensor State  Current Temp (°C)
----------------------------------  -------------  --------  --------  ------------  ----------------
Board Sensor Near Virtual Switch    85.0           80.0      5         ok            25.0                    
Board Sensor at Front Left Corner   85.0           80.0      5         ok            25.0                    
Board Sensor at Front Right Corner  85.0           80.0      5         ok            25.0                    
Board Sensor near CPU               85.0           80.0      5         ok            25.0                    
Board Sensor near Fan               85.0           80.0      5         ok            25.0                    
PSU1 Temp Sensor                    85.0           80.0      5         ok            25.0                    
PSU2 Temp Sensor                    85.0           80.0      5         ok            25.0
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment sensor \<sensor-id\></h>

Shows information about the specified physical sensor on the switch.

{{%notice note%}}
This command is not available in Cumulus Linux 5.9 and later.
{{%/notice%}}

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<sensor-id>` |  The physical sensor identifier. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform environment sensor Temp
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment temperature</h>

Shows the physical temperature sensors on the switch.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform environment temperature
Name                                Cur Temp (°C)  Crit Temp  Max Temp  Min Temp  State
----------------------------------  -------------  ---------  --------  --------  -----
Board-Sensor-Near-Virtual-Switch    25.0           85         80        5         ok   
Board-Sensor-at-Front-Left-Corner   25.0           85         80        5         ok   
Board-Sensor-at-Front-Right-Corner  25.0           85         80        5         ok   
Board-Sensor-near-CPU               25.0           85         80        5         ok   
Board-Sensor-near-Fan               25.0           85         80        5         ok   
PSU1-Temp-Sensor                    25.0           85         80        5         ok   
PSU2-Temp-Sensor                    25.0           85         80        5         ok
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment temperature \<sensor-id\></h>

Shows the current, critical, maximum, and minimum temperature for the specified sensor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<sensor-id>`  |  The sensor ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform environment temperature PSU1-Temp-Sensor
         operational
-------  -----------
state    ok         
current  25.0       
min      5          
max      80         
crit     85
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment voltage</h>

Shows the voltage sensors on the switch.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform environment voltage
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform environment voltage \<sensor-id\></h>

Shows the details for the specified voltage sensor.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<sensor-id>`  |  The sensor ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform environment voltage <sensor>
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform firmware</h>

Shows information about the switch firmware.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform firmware
Name  Actual FW                     Part Number  FW Source
----  ----------------------------  -----------  ---------
BIOS  1.13.0-1ubuntu1.1_04/01/2014  SeaBIOS      default
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform firmware \<component-id\></h>

Shows information about the specified firmware component.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  The component name. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform firmware BIOS
                operational                 
---------------  ----------------------------
part-number      SeaBIOS                     
actual-firmware  1.13.0-1ubuntu1.1_04/01/2014
fw-source        default 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform hardware</h>

Shows platform hardware information on the switch, such as the base MAC address, model and manufacturer, memory, Cumulus Linux release, serial number and system MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform hardware
               operational        applied  pending
-------------  -----------------  -------  -------
base-mac       44:38:39:22:01:7A                  
manufacturer   Cumulus                            
memory         1.69 GB                            
model          VX                                 
part-number    5.5.0                              
product-name   VX                                 
serial-number  44:38:39:22:01:7a                  
system-mac     44:38:39:22:01:b1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform hardware component</h>

Shows the hardware components on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform hardware component
        Model  Serial  State  Type  
------  -----  ------  -----  ------
device  vx                    switch
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform hardware component \<component-id\></h>

Shows information about the specified platform component.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<component-id>`  |  The component name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform hardware component device
       operational  applied  pending
-----  -----------  -------  -------
model  vx                           
type   switch
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform inventory</h>

Shows the switch inventory, which includes fan and PSU hardware version, model, serial number, state, and type.

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform inventory
          Hw version  Model  Serial             State  Type  
--------  ----------  -----  -----------------  -----  ------
FAN1/1    N/A         N/A    N/A                ok     fan   
FAN1/2    N/A         N/A    N/A                ok     fan   
FAN2/1    N/A         N/A    N/A                ok     fan   
FAN2/2    N/A         N/A    N/A                ok     fan   
FAN3/1    N/A         N/A    N/A                ok     fan   
FAN3/2    N/A         N/A    N/A                ok     fan   
PSU1      N/A         N/A    N/A                ok     psu   
PSU1/FAN  N/A         N/A    N/A                ok     fan   
PSU2      N/A         N/A    N/A                ok     psu   
PSU2/FAN  N/A         N/A    N/A                ok     fan   
SWITCH    3           5.9.0  44:38:39:22:01:7a  ok     switch
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform inventory \<inventory-id\></h>

Shows information about the specified inventory type.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<inventory-id>`  |  The inventory ID. |

### Version History

Introduced in Cumulus Linux 5.9.0

### Example

```
cumulus@switch:~$ nv show platform inventory FAN3/2
                  operational
----------------  -----------
state             ok         
hardware-version  N/A        
model             N/A        
serial            N/A        
type              fan
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform software</h>

Shows the software installed on the switch.

{{%notice note%}}
Cumulus Linux 5.13 no longer provides this command; run `nv show system version packages` instead.
{{%/notice%}}

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform software
Installed Software
=====================
    Installed software          description                 package                      version                     
    -------------------------…  -------------------------   --------------------------    -----------------------
    acpi                        displays information on     acpi                         1.7-1.1                     
                                ACPI devices                                                                         
    acpi-support-base           scripts for handling base   acpi-support-base            0.142-8                     
                                ACPI events such as the                                                              
                                power button                                                                         
    acpid                       Advanced Configuration and  acpid                        1:2.0.31-1                  
                                Power Interface event                                                                
                                daemon                                                                               
    adduser                     add and remove users and    adduser                      3.118                       
                                groups                                                                               
    apt                         commandline package         apt                          1.8.2.3                     
                                manager                                                                              
    arping                      sends IP and/or ARP pings   arping                       2.19-6                      
                                (to the MAC address)                                                                 
    arptables                   ARP table administration    arptables                    0.0.4+snapshot20181021-4    
    atftp                       advanced TFTP client        atftp                        0.7.git20120829-3.2~deb10u3 
    atftpd                      advanced TFTP server        atftpd                       0.7.git20120829-3.2~deb
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform software installed</h>

Shows a list of the installed software packages on the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform software installed
Installed software          description                 package                      version                     
-------------------------…  -------------------------…  --------------------------…  ---------------------------…
acpi                        displays information on     acpi                         1.7-1.1                     
                            ACPI devices                                                                         
acpi-support-base           scripts for handling base   acpi-support-base            0.142-8                     
                            ACPI events such as the                                                              
                            power button                                                                         
acpid                       Advanced Configuration and  acpid                        1:2.0.31-1                  
                            Power Interface event                                                                
                            daemon                                                                               
adduser                     add and remove users and    adduser                      3.118                       
                            groups                                                                               
apt                         commandline package         apt                          1.8.2.3                     
                            manager                                                                              
arping                      sends IP and/or ARP pings   arping                       2.19-6  
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform software installed \<installed-id\></h>

Shows information about the specified installed package, such as the package description and version number.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<installed-id>` |  The package name. |

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv show platform software installed what-just-happened
            operational                                                      applied  pending
-----------  ---------------------------------------------------------------  -------  -------
description  Package containing what-just-happened feature for Cumulus Linux                  
package      what-just-happened                                                               
version      2.3.0-cl5.6.0u3
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform transceiver</h>

Shows the identifier, vendor name, part number, serial number, and revision for all SFP or QSFP modules

Use the `nv show platform transceiver brief` command to see condensed information or the `nv show platform transceiver detail` command to see detailed information.

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform transceiver 
Transceiver  Identifier  Vendor name  Vendor PN         Vendor SN      Vendor revision
-----------  ----------  -----------  ----------------  -------------  --------------- 
swp1         QSFP28      Mellanox     MCP1600-C001E30N  MT2039VB01185  A3 
swp10        QSFP28      Mellanox     MCP1600-C001E30N  MT2211VS01792  A3 
swp11        QSFP28      Mellanox     MCP1600-C001E30N  MT2211VS01792  A3 
swp12        QSFP28      Mellanox     MCP1650-V00AE30   MT2122VB02220  A2 
swp13        QSFP28      Mellanox     MCP1650-V00AE30   MT2122VB02220  A2 
swp14        QSFP-DD     Mellanox     MCP1660-W00AE30   MT2121VS01645  A3 
swp15        QSFP-DD     Mellanox     MCP1660-W00AE30   MT2121VS01645  A3 
swp18        QSFP28      Mellanox     MCP1600-C001E30N  MT2211VS01967  A3 
swp20        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp21        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02204  B2 
swp22        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02194  B2 
swp23        QSFP28      Mellanox     MFA1A00-C003      MT2108FT02194  B2 
swp31        QSFP28      Mellanox     MCP1600-C001E30N  MT2039VB01191  A3 
... 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform transceiver \<interface\></h>

Shows hardware capabilities and measurement information on the SFP or QSFP module in a particular port.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface with the SFP or QSFP module. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform transceiver swp2
cable-type             : Active cable 
cable-length           : 3m 
supported-cable-length : 0m om1, 0m om2, 0m om3, 3m om4, 0m om5 
diagnostics-status     : Diagnostic Data Available 
status                 : plugged_enabled 
error-status           : N/A 
vendor-date-code       : 210215__ 
identifier             : QSFP28 
vendor-rev             : B2 
vendor-name            : Mellanox 
vendor-pn              : MFA1A00-C003 
vendor-sn              : MT2108FT02204 
temperature: 
  temperature           : 42.56 C 
  high-alarm-threshold  : 80.00 C 
  low-alarm-threshold   : -10.00 C 
  high-warning-threshold: 70.00 C 
  low-warning-threshold : 0.00 C 
  alarm                 : Off 
voltage: 
  voltage               : 3.2862 V 
  high-alarm-threshold  : 3.5000 V 
  low-alarm-threshold   : 3.1000 V 
  high-warning-threshold: 3.4650 V 
  low-warning-threshold : 3.1350 V 
  alarm                 : Off 
channel: 
  channel-1: 
    rx-power: 
        power                 : 0.8625 mW / -0.64 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -13.31 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -10.30 dBm 
        alarm                 : Off 
    tx-power: 
        power                 : 0.8988 mW / -0.46 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -11.40 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -8.40 dBm 
        alarm                 : Off 
    tx-bias-current: 
        current               : 6.750 mA 
        high-alarm-threshold  : 8.500 mA 
        low-alarm-threshold   : 5.492 mA 
        high-warning-threshold: 8.000 mA 
        low-warning-threshold : 6.000 mA 
        alarm                 : Off
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform transceiver \<interface\> channel</h>

Shows channel information for the SFP or QSFP module in a particular port.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface with the SFP or QSFP module. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform transceiver swp25 channel 
channel: 
  channel-1: 
    rx-power: 
        power                 : 0.8625 mW / -0.64 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -13.31 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -10.30 dBm 
        alarm                 : Off 
    tx-power: 
        power                 : 0.8988 mW / -0.46 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -11.40 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -8.40 dBm 
        alarm                 : Off 
    tx-bias-current: 
        current               : 6.750 mA 
        high-alarm-threshold  : 8.500 mA 
        low-alarm-threshold   : 5.492 mA 
        high-warning-threshold: 8.000 mA 
        low-warning-threshold : 6.000 mA 
        alarm                 : Off 
  channel-2: 
    rx-power: 
        power                 : 0.8385 mW / -0.76 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -13.31 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -10.30 dBm 
        alarm                 : Off 
    tx-power: 
        power                 : 0.9154 mW / -0.38 dBm 
        high-alarm-threshold  : 5.40 dBm 
        low-alarm-threshold   : -11.40 dBm 
        high-warning-threshold: 2.40 dBm 
        low-warning-threshold : -8.40 dBm 
        alarm                 : Off
...
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform transceiver \<interface\> channel \<channel-id\></h>

Shows specific channel information for the SFP or QSFP module in a particular port.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface with the SFP or QSFP module. |
| `<channel-id>` |  The channel ID. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show platform transceiver swp25 channel 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface\> transceiver</h>

Shows transceiver data for an interface in a condensed format.

### Command Syntax

| Syntax | Description |
| --------- | -------------- |
| `<interface-id>` | The interface name. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show interface swp1 transceiver
cable-type             : Active cable 
cable-length           : 3m 
supported-cable-length : 0m om1, 0m om2, 0m om3, 3m om4, 0m om5 
diagnostics-status     : Diagnostic Data Available 
status                 : plugged_enabled 
error-status           : N/A 
revision-compliance    : SFF-8636 Rev 2.5/2.6/2.7 
vendor-date-code       : 210215__ 
identifier             : QSFP28 
vendor-rev             : B2 
vendor-oui             : 00:02:c9 
vendor-name            : Mellanox 
vendor-pn              : MFA1A00-C003 
vendor-sn              : MT2108FT02204 
temperature            : 42.56 degrees C / 108.61 degrees F 
voltage                : 3.2888 V 
ch-1-rx-power          : 0.8625 mW / -0.64 dBm 
ch-1-tx-power          : 0.8988 mW / -0.46 dBm 
ch-1-tx-bias-current   : 6.750 mA 
ch-2-rx-power          : 0.8385 mW / -0.76 dBm 
ch-2-tx-power          : 0.9154 mW / -0.38 dBm 
ch-2-tx-bias-current   : 6.750 mA 
ch-3-rx-power          : 0.8556 mW / -0.68 dBm 
ch-3-tx-power          : 0.9537 mW / -0.21 dBm 
ch-3-tx-bias-current   : 6.750 mA 
ch-4-rx-power          : 0.8576 mW / -0.67 dBm 
ch-4-tx-power          : 0.9695 mW / -0.13 dBm 
ch-4-tx-bias-current   : 6.750 mA
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show platform transceiver \<interface\> temperature</h>

Shows the temperature threshold configuration for a port.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface with the SFP or QSFP module. |

### Version History

Introduced in Cumulus Linux 5.14.0

### Example

```
cumulus@switch:~$ nv show platform transceiver swp1 temperature 
          operational  applied 
--------  -----------  ------- 
setpoint  60           60 
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv show interface \<interface-id\> transceiver thresholds</h>

Shows the thresholds for the SFP or QSFP module for a specific interface.

### Command Syntax

| Syntax |  Description   |
| --------- | -------------- |
| `<interface-id>` |  The interface with the SFP or QSFP module. |

### Version History

Introduced in Cumulus Linux 5.11.0

### Example

```
cumulus@switch:~$ nv show interface swp3 transceiver thresholds
                     Ch    Value          High Alarm       High Warn        Low Warn       Low Alarm       Alt Value 
                                          Threshold        Threshold       Threshold       Threshold 
------------------------------------------------------------------------------------------------------------------------ 
temperature          -     42.74 C         80.00 C         70.00 C         0.00 C          -10.00 C        108.94F 
voltage              -     3.2862 V        3.5000 V        3.4650 V        3.1350 V        3.1000 V 
rx-power             1     -0.64 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8625 mW 
                     2     -0.70 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8514 mW 
                     3     -0.68 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8556 mW 
                     4     -0.60 dBm       5.40 dBm        2.40 dBm        -10.30 dBm      -13.31 dBm      0.8704 mW 
tx-power             1     -0.48 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.8963 mW 
                     2     -0.38 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.9154 mW 
                     3     -0.19 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.9562 mW 
                     4     -0.13 dBm       5.40 dBm        2.40 dBm        -8.40 dBm       -11.40 dBm      0.9695 mW 
tx-bias-current      1     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
                     2     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
                     3     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA 
                     4     6.750 mA        8.500 mA        8.000 mA        6.000 mA        5.492 mA
```
