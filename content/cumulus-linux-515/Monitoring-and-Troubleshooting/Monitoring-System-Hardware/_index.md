---
title: Monitoring System Hardware
author: NVIDIA
weight: 1020
toc: 3
---
You can monitor system hardware with the following commands and utilities:

- NVUE
- `decode-syseeprom`
- `smond`
- `sensors`
- watchdog

## NVUE Commands

You can run NVUE commands to monitor your system hardware.

| Command | Description |
| ----------- | ----------- |
| `nv show system health`| Shows information about the health of the switch including the status of the ASIC, hardware, and process and describes any issues. Run this command to check real-time health metrics and view historical health data.<ul><li>To show system health information for a specific configuration revision, run the `nv show system health --rev <revision-id>` command.</li><li>To show system health information in `json` format, run the `nv show system health -o json` command.</li></ul>|
| `nv show platform`| Shows platform hardware information on the switch, such as the model and manufacturer, memory, serial number and system MAC address. |
|`nv show platform environment fan` | Shows information about the fans on the switch, such as the minimum, maximum and current speed, the fan state, and the fan direction.|
| `nv show platform environment led` | Shows information about the LEDs on the switch, such as the LED name and color.|
| `nv show platform environment psu` | Shows information about the PSUs on the switch, such as the PSU name and state.|
| `nv show platform environment temperature` | Shows information about the sensors on the switch, such as the critical, maximum, minimum and current temperature and the current state of the sensor.|
| `nv show platform environment voltage` | Shows the list of voltage sensors on the switch. Note: On the SN3700 and SN3700c switch, the `nv show platform environment voltage` command output shows a failed state for the PSU-n-12V-RAIL-OUT sensors. This is a known hardware limitation that cannot be corrected by the PSU vendor.|
| `nv show platform inventory` | Shows the switch inventory, which includes fan and PSU hardware version, model, serial number, state, and type. For information about a specific fan or PSU, run the `nv show platform inventory <inventory-name>` command.|

The following example shows the `nv show health` command output when the health of the switch is not good:

```
cumulus@switch:~$ nv show system health
            operational  applied
----------  -----------  -------
status      Not OK          
status-led  amber

Health issues
================
    Component           Status information                                           
    ------------------  -------------------------------------------------------------
    forwarding          active (running) since Tue 2025-09-30 14:36:55 UTC; 1 day 21h ago
    hw-management       inactive                                                         
    hw-management-sync  inactive                                                         
    hw-management-tc    inactive                                                         
    mft                 inactive                                                         
    process             Not OK  
```

The following example shows the `nv show platform` command output:

```
cumulus@switch:~$ nv show platform
               operational      
-------------  -----------------
system-mac     44:38:39:22:01:b1                               
manufacturer   Cumulus                                         
cpu            x86_64 QEMU Virtual CPU version 2.5+ x1         
memory         1.67 GB                                         
disk-size      n/a                                             
port-layout    n/a                                             
part-number    5.15.0                                          
serial-number  44:38:39:22:01:7a                               
asic-model     n/a                                             
system-uuid    51c411e8-43d2-4e60-a7e7-e068aa04b7f9            
system-type    VX
```

The following example shows the `nv show platform environment fan` command output. The airflow direction must be the same for all fans. If Cumulus Linux detects that the fan airflow direction is not uniform, it logs a message in the `var/log/syslog` file.

```
cumulus@switch:~$ nv show platform environment fan
Name      Fan State  Current Speed (RPM)  Max Speed  Min Speed  Fan Direction
--------  ---------  -------------------  ---------  ---------  -------------
FAN1/1    ok         6000                 29000      2500       F2B         
FAN1/2    ok         6000                 29000      2500       F2B         
FAN2/1    ok         6000                 29000      2500       F2B         
FAN2/2    ok         6000                 29000      2500       F2B         
FAN3/1    ok         6000                 29000      2500       F2B         
FAN3/2    ok         6000                 29000      2500       F2B         
PSU1/FAN  ok         6000                 29000      2500       F2B         
PSU2/FAN  ok         6000                 29000      2500       F2B   
```

{{%notice note%}}
- If the airflow direction for all fans is not in the same (front to back or back to front), cooling is suboptimal for the switch, rack, and even the entire data center.
- During thermal overload or if you physically remove a fan tray while the switch is powered on, the switch reboots and none of the interfaces come up until you power cycle the switch with the fan tray reinserted or when the environmental temperature corrects. You can detect this condition with the following log message:

```
switch determine-reset[8801]: determine-reset-reason INFO: Platform api indicates reboot cause Thermal Overload: ASIC
```
{{%/notice%}}

<!-- vale off -->
## decode-syseeprom Command
<!-- vale on -->
Use the `decode-syseeprom` command to retrieve information about the switch EEPROM. If the EEPROM is writable, you can set values on the EEPROM.

The following is example `decode-syseeprom` command output. The output is different on different switches:

```
cumulus@switch:~$ decode-syseeprom
TlvInfo Header:
   Id String:    TlvInfo
   Version:      1
   Total Length: 69
TLV Name             Code Len Value
-------------------- ---- --- -----
Vendor Name          0x2D  16 Cumulus Networks
Product Name         0x21   2 VX
Device Version       0x26   1 3
Part Number          0x22   5 5.15
MAC Addresses        0x2A   2 55
Base MAC Address     0x24   6 44:38:39:22:01:7A
Serial Number        0x23  17 44:38:39:22:01:7a
CRC-32               0xFE   4 0xF305A73F
(checksum valid)
```

The `decode-syseeprom` command includes the following options:

| Option<img width="200" />| Description |
|---------------------- |--------------------------- |
| `-h`, `-help` | Displays the help message and exits. |
| `-a` | Prints the base MAC address for switch interfaces. |
| `-r` | Prints the number of MAC addresses allocated for the switch interfaces. |
| `-s` | Sets the EEPROM content (if the EEPROM is writable). You can provide arguments in the command line in a comma separated list in the form `<field>=<value>`. <ul><li>`.` `,` and `=` are not allowed in field names and values.</li><li>Any field not specified defaults to the current value.</li></ul> <br>NVIDIA Spectrum switches do not support this option.|
| `-j`, `--json` | Displays JSON output. |
| `-t <target>` | Prints the target EEPROM information (board, psu2, psu1). |
| `--serial`, `-e` | Prints the device serial number. |
| `-m` | Prints the base MAC address for the management interfaces. |
| `--init` | Clears and initializes the board EEPROM cache. |

Run the `sudo dmidecode` command to retrieve hardware configuration information populated in the BIOS.

## smond

The `smond` service monitors system units like power supply and fan, updates the corresponding LEDs, and logs the change in state. The `cpld` registers detect changes in system unit state. `smond` utilizes these registers to read all sources, which determines the health of the unit and updates the system LEDs.

Run the `sudo smonctl` command to display sensor information for the various system units:

```
cumulus@switch:~$ sudo smonctl
Fan1      (Fan Tray 1, Fan 1                     ):  OK
Fan2      (Fan Tray 1, Fan 2                     ):  OK
Fan3      (Fan Tray 2, Fan 1                     ):  OK
Fan4      (Fan Tray 2, Fan 2                     ):  OK
Fan5      (Fan Tray 3, Fan 1                     ):  OK
Fan6      (Fan Tray 3, Fan 2                     ):  OK
PSU1                                              :  OK
PSU2                                              :  OK
PSU1Fan1  (PSU1 Fan                              ):  OK
PSU1Temp1 (PSU1 Temp Sensor                      ):  OK
PSU2Fan1  (PSU2 Fan                              ):  OK
PSU2Temp1 (PSU2 Temp Sensor                      ):  OK
Temp1     (Board Sensor near CPU                 ):  OK
Temp2     (Board Sensor Near Virtual Switch      ):  OK
Temp3     (Board Sensor at Front Left Corner     ):  OK
Temp4     (Board Sensor at Front Right Corner    ):  OK
Temp5     (Board Sensor near Fan                 ):  OK
```

{{%notice note%}}
When the switch is not powered on, `smonctl` shows the PSU status as *BAD* instead of *POWERED OFF* or *NOT DETECTED*. This is a known limitation.
{{%/notice%}}

The `smonctl` command includes the following options:

| Option <img width="200" /> | Description |
| --------| ----------- |
| `-s <sensor>`, `--sensor <sensor>` | Displays data for the specified sensor. |
| `-v`, `--verbose` | Displays detailed hardware sensors data. |

The following command example shows information about FAN6 on the switch:

```
cumulus@switch:~$ smonctl -s FAN6 -v
Fan6      (Fan Tray 3, Fan 2                     ):  OK
```

For more information, read `man smond` and `man smonctl`.

## sensors Command

Run the `sensors` command to monitor the health of your switch hardware, such as power, temperature and fan speeds. This command executes `{{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors">}}`.

{{%notice note%}}
Even though you can use the `sensors` command to monitor the health of your switch hardware, NVIDIA recommends you use the `smond` daemon to monitor hardware health. See {{<link url="#smond-daemon" text="smond Daemon">}}
above.
{{%/notice%}}

For example:

```
cumulus@switch:~$ sensors
cumulus_vx_cpld-isa-0000
Adapter: ISA adapter
fan1:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan2:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan3:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan4:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan5:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan6:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan7:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
fan8:        6000 RPM  (min = 2500 RPM, max = 29000 RPM)
temp1:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
temp2:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
temp3:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
temp4:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
temp5:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
temp6:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
temp7:        +25.0°C  (low  =  +5.0°C, high = +80.0°C)
                       (crit low =  +0.0°C, crit = +85.0°C)
```

{{%notice note%}}
- Output from the `sensors` command varies depending upon the switch.
- If you only plug in one PSU, the fan is at maximum speed.
{{%/notice%}}

The following table shows the `sensors` command options.

| Option<img width="200" /> | Description |
| ----------- | ----------- |
| `-c --config-file` | Specify a configuration file; use `-` after `-c` to read the configuration file from `stdin`; by default, `sensors` references the configuration file in `/etc/sensors.d/`. |
| `-s --set` | Execute set statements in the configuration file (root only); `sensors -s` runs one time at boot and applies all the settings to the boot drivers. |
| `-f --fahrenheit`  | Show temperatures in degrees Fahrenheit. |
| `-A --no-adapter`<br>`-A --bus-list` | Do not show the adapter for each chip.<br>Generate bus statements for `sensors.conf`. |
| `-u`| Generate raw output. |
| `-j`| Generate json output. |
| `-v`| Show the program version. |

## Hardware Watchdog

Cumulus Linux includes a simplified version of the `wd_keepalive(8)` daemon instead of the one in the standard `watchdog` Debian package. `wd_keepalive` writes to a file called `/dev/watchdog` periodically (at least one time per minute) to prevent the switch from resetting. Each write delays the reboot time by another minute. After one minute of inactivity, where `wd_keepalive` does not write to `/dev/watchdog`, the switch resets itself.

Cumulus Linux enables the watchdog by default, which starts when you boot the switch (before `switchd` starts).

To disable the watchdog, disable and stop the `wd_keepalive` service:

```
cumulus@switch:~$ sudo systemctl disable wd_keepalive ; systemctl stop wd_keepalive 
```

You can modify the settings for the watchdog, such as the timeout and the scheduler priority, in the `/etc/watchdog.conf` configuration file.

```
cumulus@switch:~$ sudo nano /etc/watchdog.conf
watchdog-device	= /dev/watchdog
# Set the hardware watchdog timeout in seconds
watchdog-timeout = 30
# Kick the hardware watchdog every 'interval' seconds
interval = 5
# Log a status message every (interval * logtick) seconds.  Requires
# --verbose option to enable.
logtick = 240
# Run the daemon using default scheduler SCHED_OTHER with slightly
# elevated process priority.  See man setpriority(2).
realtime = no
priority = -2
```

## Health Monitoring Reference

The following table summarizes the events that Cumulus Linux monitors for system health:

| Event Category      | Component Name        | Severity   | Event Description                        | Threshold/Condition                          | States            |
|---------------------|----------------------|------------|------------------------------------------|----------------------------------------------|-------------------|
| Temperature Sensor  | Temp1-Temp8          | WARNING    | Temperature sensor state is HIGH         | temp ≥ max_hyst but < max                    | HIGH              |
| Temperature Sensor  | Temp1-Temp8          | WARNING    | Temperature sensor state is LOW          | temp ≤ min but > lcrit                       | LOW               |
| Temperature Sensor  | Temp1-Temp8          | CRITICAL   | Temperature sensor state is CRITICAL     | temp ≥ max                                   | CRITICAL          |
| Temperature Sensor  | Temp1-Temp8          | CRITICAL   | Temperature sensor state is LCRITICAL    | temp ≤ lcrit                                 | LCRITICAL         |
| Temperature Sensor  | Temp1-Temp8          | ERROR      | Temperature sensor state is BAD          | Sensor data outside limits or read failure    | BAD               |
| Temperature Sensor  | Temp1-Temp8          | INFO       | Temperature sensor state is ABSENT       | Sensor not present in system                  | ABSENT            |
| Temperature Sensor  | Temp1-Temp8          | INFO       | Temperature sensor state is OK           | temp within normal range                      | OK                |
| ASIC Temperature    | ASIC1                | WARNING    | ASIC temperature is too hot              | Temperature exceeds threshold                 | Not OK            |
| Fan Status          | Fan1-FanN            | WARNING    | Fan speed is out of range                | Speed not within min-max range                | BAD               |
| Fan Status          | Fan1-FanN            | WARNING    | Fan is not working                       | Fan status check failed                       | BAD               |
| Fan Status          | Fan1-FanN            | ERROR      | Failed to get fan speed data             | Unable to read fan metrics                    | BAD               |
| Fan Status          | Fan1-FanN            | INFO       | Fan is missing                           | Fan hardware not detected                     | ABSENT            |
| Fan Status          | Fan1-FanN            | CRITICAL   | Fan direction mismatch                   | Mix of B2F and F2B fans                      | BAD               |
| Fan Status          | Fan1-FanN            | INFO       | Fan state is OK                          | Fan operating normally                        | OK                |
| Power Supply        | PSU1, PSU2           | ERROR      | PSU state is BAD                         | PSU failure or malfunction                    | BAD               |
| Power Supply        | PSU1, PSU2           | INFO       | PSU is ABSENT                            | PSU not installed or detected                 | ABSENT            |
| Power Supply        | PSU1, PSU2           | INFO       | PSU state is OK                          | PSU operating normally                        | OK                |
| PSU Fan             | PSU1Fan1, PSU2Fan1   | WARNING    | PSU fan failure                          | Fan in PSU module failed                      | BAD               |
| PSU Temperature     | PSU1Temp1, PSU2Temp1 | WARNING    | PSU temperature out of range             | Temperature sensor in PSU reporting issues    | HIGH/CRITICAL     |
| CPU Utilization     | CpuStatus            | ALERT      | High CPU use                             | 80% ≤ CPU < 95%                              | Alert             |
| CPU Utilization     | CpuStatus            | CRITICAL   | Critically high CPU use                  | CPU ≥ 95%                                    | Critical          |
| CPU Utilization     | CpuStatus            | INFO       | CPU use no longer high                   | CPU < 80% (recovered)                        | OK                |
| CPU Status          | cpu                  | WARNING    | CPU status is Not OK                     | Critically high CPU in last 5 min             | Not OK            |
| Memory Usage        | MemoryStatus         | ALERT      | Low free memory                          | 90% ≤ Memory < 95%                           | Alert             |
| Memory Usage        | MemoryStatus         | CRITICAL   | Critically low free memory               | Memory ≥ 95%                                 | Critical          |
| Memory Usage        | MemoryStatus         | INFO       | Free memory no longer low                | Memory < 90% (recovered)                     | OK                |
| Root Filesystem     | disk                 | ALERT      | Filesystem nearly full                   | 90% ≤ Disk < 95%                             | Alert             |
| Root Filesystem     | disk                 | CRITICAL   | Filesystem critically full               | Disk ≥ 95%                                   | Critical          |
| /var/log Partition  | var-log              | ALERT      | /var/log partition nearly full           | /var/log usage ≥ 90%                         | Alert             |
| System Load         | LoadAverage          | ALERT      | High load average                        | 95% ≤ Load < 125% (5-min avg per core)       | Alert             |
| System Load         | LoadAverage          | CRITICAL   | Critically high load average             | Load ≥ 125% (5-min avg per core)             | Critical          |
| ASIC Status         | ASIC                 | ERROR      | ASIC state is Not OK                     | ASIC not detected via lspci                   | Not OK            |
| ASIC Status         | ASIC                 | CRITICAL   | ASIC thermal reset detected              | System rebooted due to ASIC thermal shutdown  | Not OK (Thermal Reset) |
| ASIC Status         | ASIC                 | INFO       | ASIC state is OK                         | ASIC detected and functioning                 | OK                |
| Service Status      | switchd              | ERROR      | switchd service not active               | switchd is inactive or failed                 | inactive/failed   |
| Service Status      | frr                  | ERROR      | FRR routing service not active           | frr service is inactive                       | inactive          |
| Service Status      | nvued                | ERROR      | NVUE daemon not active                   | nvued is inactive or failed                   | inactive/failed   |
| Service Status      | lldpd, smond, etc.   | WARNING    | Service not active                       | Service is inactive                           | inactive          |
| Transceiver Temp    | swp1-swpN            | WARNING    | Transceiver temperature high alarm       | Module temp high alarm/warning ON             | Not OK            |
| Transceiver Temp    | swp1-swpN            | WARNING    | Transceiver temperature low alarm        | Module temp low alarm/warning ON              | Not OK            |
| Transceiver Status  | transceiver          | INFO       | Transceiver status is OK                 | All transceivers operating normally           | OK                |


## Related Information

- {{<exlink url="http://packages.debian.org/search?keywords=lshw" text="packages.debian.org/search?keywords=lshw">}}
- {{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors.org">}}
- {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tutorials" text="Net-SNMP tutorials">}}
