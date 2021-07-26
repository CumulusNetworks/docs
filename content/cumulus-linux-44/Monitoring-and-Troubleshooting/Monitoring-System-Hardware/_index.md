---
title: Monitoring System Hardware
author: NVIDIA
weight: 1020
toc: 3
---
You can monitor system hardware with the following commands and utilities:

- `decode-syseeprom`
- `smond`
- `sensors`
- watchdog
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
| `-s` | Sets the EEPROM content (if the EEPROM is writable). You can provide arguments in the command line in a comma separated list in the form `<field>=<value>`. <ul><li>`.` `,` and `=` are not allowed in field names and values.</li><li>Any field not specified defaults to the current value.</li></ul> |
| `-j`, `--json` | Displays JSON output. |
| `-t <target>` | Prints the target EEPROM information (board, psu2, psu1). |
| `--serial`, `-e` | Prints the device serial number. |
| `-m` | Prints the base MAC address for the management interfaces. |
| `--init` | Clears and initializes the board EEPROM cache. |

Run the `dmidecode` command to retrieve hardware configuration information populated in the BIOS.

Run `apt-get` to install the `lshw` program on the switch, which also retrieves hardware configuration information.

## smond Daemon

The `smond` daemon monitors system units like power supply and fan, updates the corresponding LEDs, and logs the change in state. Changes in system unit state are detected by the `cpld` registers. `smond` utilizes these registers to read all sources, which determines the health of the unit and updates the system LEDs.

Run the  `sudo smonctl` command to display sensor information for the various system units:

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

For more information, read `man smond` and `man smonctl`.

<!--You can also run these NCLU commands to show sensor information: `net show system sensors`, `net show system sensors detail`, and `net show system sensors json`.-->

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
- If only one PSU is plugged in, the fan is at maximum speed.
{{%/notice%}}

The following table shows the `sensors` command options.

| Option<img width="200" /> | Description |
| ----------- | ----------- |
| `-c`, `--config-file` | Specify a configuration file; use `-` after `-c` to read the configuration file from `stdin`; by default, `sensors` references the configuration file in `/etc/sensors.d/`. |
| `-s`, `--set` | Execute set statements in the configuration file (root only); `sensors -s` runs one time at boot and applies all the settings to the boot drivers. |
| `-f`, `--fahrenheit`  | Show temperatures in degrees Fahrenheit. |
| `-A`, `--no-adapter`  | Do not show the adapter for each chip.|
| `--bus-list`| Generate bus statements for `sensors.conf`. |

## Hardware Watchdog

Cumulus Linux includes a simplified version of the `wd_keepalive(8)` daemon than the one provided in the standard `watchdog` Debian package. `wd_keepalive` writes to a file called `/dev/watchdog` periodically (at least one time per minute) to prevent the switch from resetting. Each write delays the reboot time by another minute. After one minute of inactivity, where `wd_keepalive` does not write to `/dev/watchdog`, the switch resets itself.

The watchdog is enabled by default on all supported switches and starts when you boot the switch (before `switchd` starts).

To disable the watchdog, disable and stop the `wd_keepalive` service:

```
cumulus@switch:~$ sudo systemctl disable wd_keepalive ; systemctl stop wd_keepalive 
```

You can modify the settings for the watchdog, such as the timeout and the scheduler priority, in the `/etc/watchdog.conf` configuration file.

## Related Information

- {{<exlink url="http://packages.debian.org/search?keywords=lshw" text="packages.debian.org/search?keywords=lshw">}}
- {{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors.org">}}
- {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tutorials" text="Net-SNMP tutorials">}}
