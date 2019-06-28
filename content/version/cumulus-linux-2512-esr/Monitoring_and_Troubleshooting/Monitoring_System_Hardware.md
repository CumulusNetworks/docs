---
title: Monitoring System Hardware
author: Cumulus Networks
weight: 161
aliases:
 - /display/CL25ESR/Monitoring+System+Hardware
 - /pages/viewpage.action?pageId=5115965
pageID: 5115965
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
You monitor system hardware in these ways, using:

  - decode-syseeprom

  - sensors

  - smond

  - [Net-SNMP](/version/cumulus-linux-2512-esr/Monitoring_and_Troubleshooting/SNMP_Monitoring)

  - watchdog

## <span>Commands</span>

  - decode-syseeprom

  - dmidecode

  - lshw

  - sensors

  - smond

## <span>Monitoring Hardware Using decode-syseeprom</span>

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

### <span>Command Options</span>

Usage: `/usr/cumulus/bin/decode-syseeprom [-a][-r][-s [args]][-t]`

| Option       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-h, –help   | Displays the help message and exits.                                                                                                                                                                                                                                                                                                                                                                                                                |
| \-a          | Prints the base MAC address for switch interfaces.                                                                                                                                                                                                                                                                                                                                                                                                  |
| \-r          | Prints the number of MACs allocated for switch interfaces.                                                                                                                                                                                                                                                                                                                                                                                          |
| \-s          | Sets the EEPROM content if the EEPROM is writable. `args` can be supplied in command line in a comma separated list of the form `'<field>=<value>, ...'. ','` and `'='` are illegal characters in field names and values. Fields that are not specified will default to their current values. If `args` are supplied in the command line, they will be written without confirmation. If `args` is empty, the values will be prompted interactively. |
| \-t TARGET   | Selects the target EEPROM (`board`, `psu2`, `psu1`) for the read or write operation; default is `board`.                                                                                                                                                                                                                                                                                                                                            |
| \-e, –serial | Prints the device serial number.                                                                                                                                                                                                                                                                                                                                                                                                                    |

### <span>Related Commands</span>

You can also use the `dmidecode` command to retrieve hardware
configuration information that’s been populated in the BIOS.

You can use `apt-get` to install the `lshw` program on the switch, which
also retrieves hardware configuration information.

## <span>Monitoring Hardware Using sensors</span>

The `sensors` command provides a method for monitoring the health of
your switch hardware, such as power, temperature and fan speeds. This
command executes [lm-sensors](http://lm-sensors.org).

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

Output from the `sensors` command varies depending upon the switch
hardware you use, as each platform ships with a different type and
number of sensors.

{{%/notice%}}

### <span>Command Options</span>

Usage: `sensors [OPTION]... [CHIP]...`

| Option             | Description                                                                                                                                                 |
| ------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-c, --config-file | Specify a config file; use - after `-c` to read the config file from `stdin`; by default, `sensors` references the configuration file in `/etc/sensors.d/`. |
| \-s, --set         | Executes set statements in the config file (root only); `sensors -s` is run once at boot time and applies all the settings to the boot drivers.             |
| \-f, --fahrenheit  | Show temperatures in degrees Fahrenheit.                                                                                                                    |
| \-A, --no-adapter  | Do not show the adapter for each chip.                                                                                                                      |
| \--bus-list        | Generate bus statements for `sensors.conf`.                                                                                                                 |

If `[CHIP]` is not specified in the command, all chip info will be
printed. Example chip names include:

  - lm78-i2c-0-2d \*-i2c-0-2d

  - lm78-i2c-0-\* \*-i2c-0-\*

  - lm78-i2c-\*-2d \*-i2c-\*-2d

  - lm78-i2c-\*-\* \*-i2c-\*-\*

  - lm78-isa-0290 \*-isa-0290

  - lm78-isa-\* \*-isa-\*

  - lm78-\*

<span id="src-5115965_MonitoringSystemHardware-snmp"></span>

## <span>Monitoring Switch Hardware Using SNMP</span>

The Net-SNMP documentation has been moved to a new chapter, [available
here](/version/cumulus-linux-2512-esr/Monitoring_and_Troubleshooting/SNMP_Monitoring).

## <span>Monitoring System Units Using smond</span>

The `smond` daemon monitors system units like power supply and fan,
updates their corresponding LEDs, and logs the change in the state.
Changes in system unit state are detected via the `cpld` registers.
`smond` utilizes these registers to read all sources, which impacts the
health of the system unit, determines the unit's health, and updates the
system LEDs.

Use ` smonctl  `to display sensor information for the various system
units:

    cumulus@switch:~$ smonctl
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

### <span>Command Options</span>

Usage: `smonctl [OPTION]... [CHIP]...`

| Option                      | Description                              |
| --------------------------- | ---------------------------------------- |
| \-s SENSOR, --sensor SENSOR | Displays data for the specified sensor.  |
| \-v, --verbose              | Displays detailed hardware sensors data. |

For more information, read `man smond` and `man smonctl`.

<span id="src-5115965_MonitoringSystemHardware-watchdog"></span>

## <span>Keeping the Switch Alive Using the Hardware Watchdog</span>

Cumulus Linux includes a simplified version of the ` wd_keepalive(8)
 `daemon from the standard Debian package ` watchdog  `. `wd_keepalive`
writes to a file called `/dev/watchdog` periodically to keep the switch
from resetting, at least once per minute. Each write delays the reboot
time by another minute. After one minute of inactivity where
`wd_keepalive` doesn't write to `/dev/watchdog`, the switch resets
itself.

The watchdog is enabled by default on QuantaMesh BMS T1048-LB9 switches
only; you must enable the watchdog on all other switch platforms. When
enabled, it starts when you boot the switch, before `switchd` starts.

To enable the hardware watchdog, edit the
`/etc/watchdog.d/<your_platform>` file and set `run_watchdog` to *1*:

    run_watchdog=1

To disable the watchdog, edit the `/etc/watchdog.d/<your_platform>` file
and set `run_watchdog` to *0*:

    run_watchdog=0

Then stop the daemon:

    cumulus@switch:~$ sudo service wd_keepalive stop

You can modify the settings for the watchdog — like the timeout setting
and scheduler priority — in its configuration file,
`/etc/watchdog.conf`.

## <span>Configuration Files</span>

  - /etc/cumulus/switchd.conf

  - /etc/cumulus/sysledcontrol.conf

  - /etc/sensors.d/\<switch\>.conf - sensor configuration file (do
    **not** edit it\!)

  - /etc/watchdog.conf

## <span>Useful Links</span>

  - <http://packages.debian.org/search?keywords=lshw>

  - <http://lm-sensors.org>

  - [Net-SNMP
    tutorials](http://net-snmp.sourceforge.net/wiki/index.php/Tutorials)
