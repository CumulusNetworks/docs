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
| `nv show platform hardware`| Shows platform hardware information on the switch, such as the base MAC address, model and manufacturer, memory, Cumulus Linux release, serial number and system MAC address. |
| `nv show system cpu` | Shows information about the switch CPU, such as the core-count, the model, and the utilization percentage.|
| `nv show platform environment` | Shows a list of sensors, fans, LEDs, and PSUs on the switch.|
|`nv show platform environment fan` | Shows information about the fans on the switch, such as the minimum, maximum and current speed, the fan state, and the fan direction.|
| `nv show platform environment led` | Shows information about the LEDs on the switch, such as the LED name and color.|
| `nv show platform environment psu` | Shows information about the PSUs on the switch, such as the PSU name and state.|
| `nv show platform environment sensor` | Shows information about the sensors on the switch, such as the critical, maximum, minimum and current temperature and the current state of the sensor.|

The following example shows the `nv show platform hardware` command output:

```
cumulus@switch:~$ nv show platform hardware
               operational      
-------------  -----------------
base-mac       44:38:39:22:01:7A
cpu            n/a              
disk-size      n/a              
manufacturer   Cumulus          
memory         1758728 kB       
model          VX               
part-number    5.6.0            
port-layout    n/a              
product-name   VX               
serial-number  44:38:39:22:01:7a
system-mac     44:38:39:22:01:b1
asic-model     n/a              
asic-vendor    n/a
```

The following example shows the `nv show platform environment fan` command output. The fan direction must be the same for all fans. If Cumulus Linux detects that the fan air flow direction is not uniform, it logs a message in the `var/log/syslog` file.

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

{{%notice note%}}
If the airflow for all fans is not in the same direction (front to back or back to front), cooling is suboptimal for the switch, rack, and even the entire data center.
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
   Total Length: 629
TLV Name             Code Len Value
-------------------- ---- --- -----
Product Name         0x21  64 MSN3700C
Part Number          0x22  20 MSN3700-CSBFO
Serial Number        0x23  24 MT2043X05294
Base MAC Address     0x24   6 1C:34:DA:24:C9:00
Manufacture Date     0x25  19 10/21/2020 20:57:29
Device Version       0x26   1 1
MAC Addresses        0x2A   2 254
Manufacturer         0x2B   8 Mellanox
Vendor Extension     0xFD  52 0x00 0x00 0x81 0x19 0x00 0x2E 0x00 0x02 0x07 0x98 0x00 0x00 0x31 0x00 0x20 0x00 0x00 0x00 0x00 0x00 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 0x07 
Platform Name        0x28  64 x86_64-mlnx_msn3700C-r0
ONIE Version         0x29  23 2019.11-5.2.0020-115200
CRC-32               0xFE   4 0x11D0954D
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

Run the `dmidecode` command to retrieve hardware configuration information populated in the BIOS.

Run `apt-get` to install the `lshw` program on the switch, which also retrieves hardware configuration information.

## smond

The `smond` service monitors system units like power supply and fan, updates the corresponding LEDs, and logs the change in state. The `cpld` registers detect changes in system unit state. `smond` utilizes these registers to read all sources, which determines the health of the unit and updates the system LEDs.

Run the `sudo smonctl` command to display sensor information for the various system units:

```
cumulus@switch:~$ sudo smonctl
Board                                             :  OK
Fan                                               :  OK
PSU1                                              :  OK
PSU2                                              :  BAD
Temp1     (Networking ASIC Die Temp Sensor       ):  OK
Temp10    (Right side of the board               ):  OK
Temp2     (Near the CPU (Right)                  ):  OK
Temp3     (Top right corner                      ):  OK
Temp4     (Right side of Networking ASIC         ):  OK
Temp5     (Middle of the board                   ):  OK
Temp6     (P2020 CPU die sensor                  ):  OK
Temp7     (Left side of the board                ):  OK
Temp8     (Left side of the board                ):  OK
Temp9     (Right side of the board               ):  OK
```

{{%notice note%}}
When the switch is not powered on, `smonctl` shows the PSU status as *BAD* instead of *POWERED OFF* or *NOT DETECTED*. This is a known limitation.
{{%/notice%}}

The `smonctl` command includes the following options:

| Option <img width="200" /> | Description |
| --------| ----------- |
| `-s <sensor>`, `--sensor <sensor>` | Displays data for the specified sensor. |
| `-v`, `--verbose` | Displays detailed hardware sensors data. |

The following command example shows detailed information about FAN6 on the switch. The information includes the fan state, the current, minimum, and maximum speed, the limit variance, and the fan direction.

```
cumulus@switch:~$ smonctl -s FAN6 -v
Fan6(Fan Tray 3 Rear):  OK 
fan:8282 RPM   (max = 25000 RPM, min = 4500 RPM, limit_variance = 15 direction = F2B)
```

For more information, read `man smond` and `man smonctl`.

## sensors Command

Run the `sensors` command to monitor the health of your switch hardware, such as power, temperature and fan speeds. This command executes `{{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors">}}`.

{{%notice note%}}
Even though you can use the `sensors` command to monitor the health of your switch hardware, the `smond` daemon is the recommended method for monitoring hardware health. See {{<link url="#smond-daemon" text="smond Daemon">}}
above.
{{%/notice%}}

For example:

```
cumulus@switch:~$ sensors
tmp75-i2c-6-48
Adapter: i2c-1-mux (chan_id 0)
temp1:        +39.0 C  (high = +75.0 C, hyst = +25.0 C)

tmp75-i2c-6-49
Adapter: i2c-1-mux (chan_id 0)
temp1:        +35.5 C  (high = +75.0 C, hyst = +25.0 C)

ltc4215-i2c-7-40
Adapter: i2c-1-mux (chan_id 1)
in1:         +11.87 V
in2:         +11.98 V
power1:       12.98 W
curr1:        +1.09 A

max6651-i2c-8-48
Adapter: i2c-1-mux (chan_id 2)
fan1:        13320 RPM  (div = 1)
fan2:        13560 RPM
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

## Related Information

- {{<exlink url="http://packages.debian.org/search?keywords=lshw" text="packages.debian.org/search?keywords=lshw">}}
- {{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors.org">}}
- {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tutorials" text="Net-SNMP tutorials">}}
