---
title: Monitoring System Hardware
author: NVIDIA
weight: 219
pageID: 8362594
---
You monitor system hardware in these ways, using:

- `decode-syseeprom`
- `smond`
- `sensors`
- {{<link url="Simple-Network-Management-Protocol-SNMP" text="Net-SNMP">}}
- `watchdog`

## Retrieve Hardware Information Using decode-syseeprom

The `decode-syseeprom` command enables you to retrieve information about
the switch's EEPROM. If the EEPROM is writable, you can set values on
the EEPROM.

For example:

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

{{%notice info%}}

Edgecore AS5712-54X, AS5812-54T, AS5812-54X, AS6712-32X and AS6812-32X switches support a second source power supply. This second source device presents at a different I2C address than the primary. As a result, whenever `decode-syseeprom` attempts to read the EEPROM on the PSUs in these systems, both addresses are checked. When the driver reads the location that is not populated, a warning message like the following is logged:

    Oct 18 09:54:41 lfc-1ao15 decode-syseeprom: Unable to find eeprom at /sys/bus/i2c/devices/11-0050/eeprom for psu2

This is expected behavior on these platforms.

{{%/notice%}}

### decode-syseeprom Command Options

Usage: `/usr/cumulus/bin/decode-syseeprom [-a][-r][-s [args]][-t]`

|Option|Description|
|--- |--- |
|-h|Displays the help message and exits.|
|-a|Prints the base MAC address for switch interfaces.|
|-r|Prints the number of MACs allocated for switch interfaces.|
|-s|Sets the EEPROM content if the EEPROM is writable. args can be supplied in command line in a comma separated list of the form \<field>=\<value>, .... Illegal characters in field names and values include the comma (,) and equals sign (=). Fields that are not specified default to their current values. If args are supplied in the command line, they will be written without confirmation. If args is empty, the values will be prompted interactively.<br>NVIDIA Spectrum switches do not support this option. |
|-j, --json|Displays JSON output.|
|-t TARGET|Prints the target EEPROM (board, psu2, psu1) information.{{%notice note%}}Some systems that use a BMC to manage sensors (such as the Dell Z9264, Facebook Voyager, and Facebook Wedge-100) do not provide the PSU EEPROM contents. This is because the BMC connects to the PSUs via I2C and the main CPU of the switch has no direct access.{{%/notice%}}|
|--serial|Prints the device serial number.|
|-m|Prints the base MAC address for management interfaces.|
|--init|Clears and initializes the board EEPROM cache|

### Related Commands

You can also use the `dmidecode` command to retrieve hardware
configuration information that's been populated in the BIOS.

You can use `apt-get` to install the `lshw` program on the switch, which
also retrieves hardware configuration information.

## Monitor System Units Using smond

The `smond` daemon monitors system units like power supply and fan,
updates their corresponding LEDs, and logs the change in the state.
Changes in system unit state are detected via the `cpld` registers.
`smond` utilizes these registers to read all sources, which impacts the
health of the system unit, determines the unit's health, and updates the
system LEDs.

Use `smonctl` to display sensor information for the various system
units:

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

{{%notice note%}}

When the switch is not powered on, `smonctl` shows the PSU status as
*BAD* instead of *POWERED OFF* or *NOT DETECTED*. This is a known
limitation.

{{%/notice%}}

{{%notice note%}}

On the Dell S4148 switch, `smonctl` shows PSU1 and PSU2; however in the
sensors output, both PSUs are listed as PSU1.

{{%/notice%}}

{{%notice note%}}

Some switch models lack the sensor for reading voltage information, so
this data is not output from the `smonctl` command.

For example, the Dell S4048 series has this sensor and displays power
and voltage information:

    cumulus@dell-s4048-ON:~$ sudo smonctl -v -s PSU2
    PSU2:  OK
    power:8.5 W   (voltages = ['11.98', '11.87'] V currents = ['0.72'] A)

Whereas the Penguin Arctica 3200c does not:

    cumulus@cel-sea:~/tmp$ sudo smonctl -v -s PSU1
    PSU1:  OK

{{%/notice%}}

The following table shows the `smonctl` command options.

Usage: `smonctl [OPTION]... [CHIP]...`

| Option                      | Description                              |
| --------------------------- | ---------------------------------------- |
| \-s SENSOR, --sensor SENSOR | Displays data for the specified sensor.  |
| \-v, --verbose              | Displays detailed hardware sensors data. |

For more information, read `man smond` and `man smonctl`.

{{%notice note%}}

In Cumulus Linux 3.7.11 and later, you can run these NCLU commands to show sensor information: `net show system sensors`, `net show system sensors detail`, and `net show system sensors json`.

{{%/notice%}}

## Monitor Hardware Health Using sensors

The `sensors` command provides a method for monitoring the health of
your switch hardware, such as power, temperature and fan speeds. This
command executes `{{<exlink url="https://en.wikipedia.org/wiki/Lm_sensors" text="lm-sensors">}}`.

{{%notice note%}}

Even though you can use the `sensors` command to monitor the health of
your switch hardware, the `smond` daemon is the recommended method for
monitoring hardware health. See
{{<link url="#monitor-system-units-using-smond" text="Monitor System Units Using smond">}} above.

{{%/notice%}}

For example:

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

{{%notice note%}}

- Output from the `sensors` command varies depending upon the switch hardware you use, as each platform ships with a different type and number of sensors.
- On a Mellanox switch with the Spectrum ASIC, if both power supply units (PSUs) are energized, the `sensors` command does not flag any ALARM. If only one PSU cable is energized and the other PSU cable is just plugged in without being energized, `lm-sensors` might enumerate this device and flag an ALARM as the VIN field reports zero voltage.
- On a Mellanox switch, if only one PSU is plugged in, the fan is at maximum speed.

{{%/notice%}}

The following table shows the `sensors` command options.

Usage: `sensors [OPTION]... [CHIP]...`

| Option      | Description  |
| ----------- | ------------ |
| \-c, --config-file | Specify a config file; use `-` after `-c` to read the config file from `stdin`; by default, `sensors` references the configuration file in `/etc/sensors.d/`. |
| \-s, --set         | Executes set statements in the config file (root only); `sensors -s` is run once at boot time and applies all the settings to the boot drivers.   |
| \-f, --fahrenheit  | Show temperatures in degrees Fahrenheit.  |
| \-A, --no-adapter  | Do not show the adapter for each chip.    |
| \--bus-list        | Generate bus statements for `sensors.conf`.|

If `[CHIP]` is not specified in the command, all chip info will be printed.
Example chip names include:

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

Cumulus Linux includes a simplified version of the `wd_keepalive(8)`
daemon from the standard `watchdog` Debian package. `wd_keepalive`
writes to a file called `/dev/watchdog` periodically to keep the switch
from resetting, at least once per minute. Each write delays the reboot
time by another minute. After one minute of inactivity where `wd_keepalive`
doesn't write to `/dev/watchdog`, the switch resets itself.

The watchdog is enabled by default on all supported switches,
and starts when you boot the switch, before `switchd` starts.

To disable the watchdog, disable and stop the `wd_keepalive` service:

    cumulus@switch:~$ sudo systemctl disable wd_keepalive; systemctl stop wd_keepalive 

You can modify the settings for the watchdog &mdash; like the timeout setting
and scheduler priority &mdash; in the configuration file, `/etc/watchdog.conf`. Here
is the default configuration file:

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

## Known Limitations

### Facebook Backpack PSU Monitoring Occasionally Replies with N/A Values or FAULT ALARM instead of Integers

On Facebook Backpack switches, you sometimes see unparsible sensor value
`"FAULT ALARM"` and/or `state changed from OK to ABSENT` in the
`/var/log/syslog` file. This is a known issue with the platform.

### No PSU sensors/smonctl support for Edgecore OMP-800

On the Edgecore OMP-800, there is no power supply information from the sensor or from `smonctl`.

The platform driver has support for the PSUs but this was not added to the sensors infrastructure.

This is a known limitation on the OMP-800 platform.

## Related Information

- {{<exlink url="https://packages.debian.org/jessie/lshw" text="lshw package for Debian Jessie">}}
- {{<exlink url="https://github.com/lm-sensors/lm-sensors" text="lm-sensors on GitHub">}}
- {{<exlink url="http://net-snmp.sourceforge.net/wiki/index.php/Tutorials" text="Net-SNMP tutorials">}}
