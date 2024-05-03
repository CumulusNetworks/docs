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
