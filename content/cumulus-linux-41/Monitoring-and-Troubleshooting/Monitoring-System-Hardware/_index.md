---
title: Monitoring System Hardware
author: NVIDIA
weight: 940
toc: 3
---
You monitor system hardware using the following commands and utilities:

- `decode-syseeprom`
- `smond`
- `sensors`
- {{<link url="Simple-Network-Management-Protocol-SNMP" text="Net-SNMP">}}
- watchdog

## Retrieve Hardware Information Using decode-syseeprom

The `decode-syseeprom` command enables you to retrieve information about the switch's EEPROM. If the EEPROM is writable, you can set values on the EEPROM.

The following is an example. The command output is different on different switches:

```
cumulus@switch:~$ decode-syseeprom
TlvInfo Header:
    Id String:    TlvInfo
    Version:      1
    Total Length: 114
TLV Name             Code Len Value
-------------------- ---- --- -----
Product Name         0x21   4 4804
Part Number          0x22  14 R0596-F0009-00
Device Version       0x26   1 2
Serial Number        0x23  19 D1012023918PE000012
Manufacture Date     0x25  19 10/09/2013 20:39:02
Base MAC Address     0x24   6 00:E0:EC:25:7B:D0
MAC Addresses        0x2A   2 53
Vendor Name          0x2D  17 Penguin Computing
Label Revision       0x27   4 4804
Manufacture Country  0x2C   2 CN
CRC-32               0xFE   4 0x96543BC5
(checksum valid)
```

### Command Options

Usage: `/usr/cumulus/bin/decode-syseeprom [-a][-r][-s [args]][-t <target>][-e][-m]`

| Option<img width="200" />| Description |
|---------------------- |--------------------------- |
| `-h`, `-help` | Displays the help message and exits. |
| `-a` | Prints the base MAC address for switch interfaces. |
| `-r` | Prints the number of MACs allocated for switch interfaces. |
| `-s` | Sets the EEPROM content if the EEPROM is writable. args can be supplied in the command line in a comma separated list of the form `<field>=<value>`. `.` `,` and `=` are illegal characters in field names and values. Fields that are not specified default to their current values. If args are supplied in the command line, they will be written without confirmation. If args is empty, the values will be prompted interactively.<br>NVIDIA Spectrum switches do not support this option. |
| `-j`, `--json` | Displays JSON output. |
| `-t <target>` | Prints the target EEPROM (board, psu2, psu1) information.<br><br>**Note**: Some systems that use a BMC to manage sensors (such as the Dell Z9264 and EdgeCore Minipack AS8000) do not provide the PSU EEPROM contents. This is because the BMC connects to the PSUs via I2C and the main CPU of the switch has no direct access. |
| `--serial`, `-e` | Prints the device serial number. |
| `-m` | Prints the base MAC address for management interfaces. |
| `--init` | Clears and initializes the board EEPROM cache |

### Related Commands

You can also use the `dmidecode` command to retrieve hardware configuration information that is populated in the BIOS.

You can use `apt-get` to install the `lshw` program on the switch, which also retrieves hardware configuration information.

## Monitor System Units Using smond

The `smond` daemon monitors system units like power supply and fan, updates their corresponding LEDs, and logs the change in the state. Changes in system unit state are detected via the `cpld` registers. `smond` utilizes these registers to read all sources, which impacts the health of the system unit, determines the unit's health, and updates the system LEDs.

Use `smonctl` to display sensor information for the various system units:

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

{{%notice note%}}

On the Dell S4148 switch, `smonctl` shows PSU1 and PSU2; however in the sensors output, both PSUs are listed as PSU1.

{{%/notice%}}

{{%notice note%}}

Some switch models lack the sensor for reading voltage information, so this data is not output from the `smonctl` command.

For example, the Dell S4048 series has this sensor and displays power and voltage information:

```
cumulus@dell-s4048-ON:~$ sudo smonctl -v -s PSU2
PSU2:  OK
power:8.5 W   (voltages = ['11.98', '11.87'] V currents = ['0.72'] A)
```

The Penguin Arctica 3200c does not have this sensor:

```
cumulus@cel-sea:~/tmp$ sudo smonctl -v -s PSU1
PSU1:  OK
```

{{%/notice%}}

The following table shows the `smonctl` command options.

Usage: `smonctl [OPTION]... [CHIP]...`

| Option <img width="200" /> | Description |
| --------| ----------- |
| `-s <sensor>`, `--sensor <sensor>` | Displays data for the specified sensor. |
| `-v`, `--verbose` | Displays detailed hardware sensors data. |

For more information, read `man smond` and `man smonctl`.

You can also run these NCLU commands to show sensor information: `net show system sensors`, `net show system sensors detail`, and `net show system sensors json`.

## Monitor Hardware Using sensors

Use the `sensors` command to monitor the health of your switch hardware, such as power, temperature and fan speeds. This command executes `{{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors">}}`.

{{%notice note%}}

Even though you can use the `sensors` command to monitor the health of your switch hardware, the `smond` daemon is the recommended method for monitoring hardware health. See {{<link url="#monitor-system-units-using-smond" text="Monitor System Units Using smond">}}
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

Output from the `sensors` command varies depending upon the switch hardware you use, as each platform ships with a different type and number of sensors.

{{%/notice%}}

The following table shows the `sensors` command options.

Usage: `sensors [OPTION]... [CHIP]...`

| Option<img width="200" /> | Description |
| ----------- | ----------- |
| `-c`, `--config-file` | Specify a config file; use `-` after `-c` to read the config file from `stdin`; by default, `sensors` references the configuration file in `/etc/sensors.d/`. |
| `-s`, `--set` | Executes set statements in the config file (root only); `sensors -s` is run once at boot time and applies all the settings to the boot drivers. |
| `-f`, `--fahrenheit`  | Show temperatures in degrees Fahrenheit. |
| `-A`, `--no-adapter`  | Do not show the adapter for each chip.|
| `--bus-list`| Generate bus statements for `sensors.conf`. |

If `[CHIP]` is not specified in the command, all chip information is printed. Example chip names include:

- lm78-i2c-0-2d \*-i2c-0-2d
- lm78-i2c-0-\* \*-i2c-0-\*
- lm78-i2c-\*-2d \*-i2c-\*-2d
- lm78-i2c-\*-\* \*-i2c-\*-\*
- lm78-isa-0290 \*-isa-0290
- lm78-isa-\* \*-isa-\*
- lm78-\*

## Monitor Switch Hardware Using SNMP

The Net-SNMP documentation is discussed {{<link url="Simple-Network-Management-Protocol-SNMP" text="here">}}.

## Keep the Switch Alive Using the Hardware Watchdog

Cumulus Linux includes a simplified version of the `wd_keepalive(8)` daemon from the standard `watchdog` Debian package. `wd_keepalive` writes to a file called `/dev/watchdog` periodically to keep the switch from resetting, at least once per minute. Each write delays the reboot time by another minute. After one minute of inactivity where `wd_keepalive` doesn't write to `/dev/watchdog`, the switch resets itself.

The watchdog is enabled by default on all supported switches, and starts when you boot the switch, before `switchd` starts.

To disable the watchdog, disable and stop the `wd_keepalive` service:

    cumulus@switch:~$ sudo systemctl disable wd_keepalive ; systemctl stop wd_keepalive 

You can modify the settings for the watchdog &mdash; like the timeout setting and scheduler priority &mdash; in the configuration file, `/etc/watchdog.conf`. Here is the default configuration file:

```
cumulus@switch:~$ cat /etc/watchdog.conf

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

## Related Information

- {{<exlink url="http://packages.debian.org/search?keywords=lshw" text="packages.debian.org/search?keywords=lshw">}}
- {{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors.org">}}
- {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tutorials" text="Net-SNMP tutorials">}}
