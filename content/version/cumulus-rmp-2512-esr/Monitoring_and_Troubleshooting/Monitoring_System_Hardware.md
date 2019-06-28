---
title: Monitoring System Hardware
author: Cumulus Networks
weight: 91
aliases:
 - /display/RMP25ESR/Monitoring+System+Hardware
 - /pages/viewpage.action?pageId=5116326
pageID: 5116326
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
You monitor system hardware in these ways, using:

  - decode-syseeprom

  - sensors

  - smond

  - Net-SNMP

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

    cumulus@switch:~# decode-syseeprom
    TlvInfo Header:
       Id String:    TlvInfo
       Version:      1
       Total Length: 159
    TLV Name             Code Len Value
    -------------------- ---- --- -----
    Product Name         0x21   6 Pebble
    Part Number          0x22  14 R0854-G0008-02
    Serial Number        0x23  19 D2070023918PE000012
    Manufacture Date     0x25  19 01/15/2015 14:30:00
    Device Version       0x26   1 2
    Label Revision       0x27   6 Pebble
    Platform Name        0x28   6 Pebble
    MAC Addresses        0x2A   2 73
    Manufacturer         0x2B   9 CELESTICA
    Manufacture Country  0x2C   3 CHN
    Vendor Name          0x2D   9 CELESTICA
    Diag Version         0x2E   5 1.0.0
    Service Tag          0x2F   2 LB
    Vendor Extension     0xFD   1 0x62 
    Base MAC Address     0x24   6 44:38:39:00:89:DD
    ONIE Version         0x29  13 2014.11.0.0.2
    CRC-32               0xFE   4 0x19AFD83A
    (checksum valid)

### <span>Command Options</span>

Usage: `/usr/cumulus/bin/decode-syseeprom [-a][-r][-s [args]][-t]`

| Option        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-h, –help    | Displays the help message and exits.                                                                                                                                                                                                                                                                                                                                                                                                                |
| \-a           | Prints the base MAC address for switch interfaces.                                                                                                                                                                                                                                                                                                                                                                                                  |
| \-r           | Prints the number of MACs allocated for switch interfaces.                                                                                                                                                                                                                                                                                                                                                                                          |
| \-s           | Sets the EEPROM content if the EEPROM is writable. `args` can be supplied in command line in a comma separated list of the form `'<field>=<value>, ...'. ','` and `'='` are illegal characters in field names and values. Fields that are not specified will default to their current values. If `args` are supplied in the command line, they will be written without confirmation. If `args` is empty, the values will be prompted interactively. |
| \-t TARGET    | Selects the target EEPROM (`board`, `psu2`, `psu1`) for the read or write operation; default is `board`.                                                                                                                                                                                                                                                                                                                                            |
| \-e, --serial | Prints the device serial number.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \-m           | Prints the base MAC address for management interfaces.                                                                                                                                                                                                                                                                                                                                                                                              |

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
    coretemp-isa-0000
    Adapter: ISA adapter
    Core 0:       +32.0 C  (high = +110.0 C, crit = +110.0 C)
    Core 2:       +35.0 C  (high = +110.0 C, crit = +110.0 C)
    
    lm75-i2c-0-4a
    Adapter: SMBus I801 adapter at e000
    temp1:        +27.0 C  (high = +60.0 C, hyst = +25.0 C)

### <span>Command Options</span>

Usage: `sensors [OPTION]... [CHIP]...`

| Option            | Description                                                                                                                                                 |
| ----------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-c, –config-file | Specify a config file; use - after `-c` to read the config file from `stdin`; by default, `sensors` references the configuration file in `/etc/sensors.d/`. |
| \-s, –set         | Executes set statements in the config file (root only); `sensors -s` is run once at boot time and applies all the settings to the boot drivers.             |
| \-f, –fahrenheit  | Show temperatures in degrees Fahrenheit.                                                                                                                    |
| \-A, –no-adapter  | Do not show the adapter for each chip.                                                                                                                      |
| –bus-list         | Generate bus statements for `sensors.conf`.                                                                                                                 |

If `[CHIP]` is not specified in the command, all chip info will be
printed. Example chip names include:

  - lm78-i2c-0-2d \*-i2c-0-2d

  - lm78-i2c-0-\* \*-i2c-0-\*

  - lm78-i2c-\*-2d \*-i2c-\*-2d

  - lm78-i2c-\*-\* \*-i2c-\*-\*

  - lm78-isa-0290 \*-isa-0290

  - lm78-isa-\* \*-isa-\*

  - lm78-\*

<span id="src-5116326_MonitoringSystemHardware-snmp"></span>

## <span>Monitoring Switch Hardware Using SNMP</span>

Cumulus RMP ships with Net-SNMP v5.4.3. However, it is disabled by
default. To enable Net-SNMP, use `jdoo`, which is the fork of `monit`
version 5.2.5.

{{%notice warning%}}

`jdoo` and `monit` are mutually exclusive, so the `monit` package is not
installed on Cumulus RMP. If you would prefer to use `monit`, it will
uninstall `jdoo` from Cumulus RMP. However, Cumulus Networks will not
provide support for issues with `monit`.

{{%/notice%}}

1.  Edit `/etc/default/snmpd` and verify that `SNMPDRUN=yes`.

2.  In order to use `jdoo` on SNMPD, you need to add a configuration
    like the following to your `/etc/jdoo/jdoorc` file:
    
        check process snmpd with pidfile /var/run/snmpd.pid
            every 6 cycles
            group networking
            start program = "/etc/init.d/snmpd start"
            stop program = "/etc/init.d/snmpd stop"

3.  Then reload `jdoo`:
    
        # sudo jdoo reload

4.  Start `snmp`:
    
        # sudo jdoo start snmpd

5.  Optionally, if you don't want to monitor SNMPD, you can just start
    it natively:
    
        # service snmpd start

Once enabled, you can use SNMP to manage various components on the
switch. The supported MIBs include many publicly used MIBs as well as
some MIBs developed by Cumulus Networks for Cumulus RMP:

  - [SNMP-FRAMEWORK](http://net-snmp.sourceforge.net/docs/mibs/snmpFrameworkMIB.html)

  - [SNMP-MPD](http://net-snmp.sourceforge.net/docs/mibs/snmpMPDMIB.html)

  - [SNMP-USER-BASED-SM](http://net-snmp.sourceforge.net/docs/mibs/snmpUsmMIB.html)

  - [SNMP-VIEW-BASED-ACM](http://net-snmp.sourceforge.net/docs/mibs/snmpVacmMIB.html)

  - [SNMPv2](http://net-snmp.sourceforge.net/docs/mibs/snmpMIB.html)

  - [IP (includes
    ICMP)](http://net-snmp.sourceforge.net/docs/mibs/ip.html)

  - [TCP](http://net-snmp.sourceforge.net/docs/mibs/tcp.html)

  - [UDP](http://net-snmp.sourceforge.net/docs/mibs/udp.html)

  - [UCD-SNMP](http://www.net-snmp.org/docs/mibs/UCD-SNMP-MIB.txt) (For
    information on exposing CPU and memory information via SNMP, see
    this [knowledge base
    article](https://support.cumulusnetworks.com/hc/en-us/articles/203922988).)

  - [IF-MIB](http://net-snmp.sourceforge.net/docs/mibs/interfaces.html)

  - [LLDP](http://www.mibdepot.com/cgi-bin/getmib3.cgi?i=1&n=LLDP-MIB&r=cisco&f=LLDP-MIB-V1SMI.my&v=v1&t=tree)

  - [LM-SENSORS
    MIB](http://support.ipmonitor.com/mibs_byoidtree.aspx?oid=.1.3.6.1.4.1.2021.13.16)

  - [NET-SNMP-EXTEND-MIB](http://net-snmp.sourceforge.net/docs/mibs/netSnmpExtendMIB.html)
    (See also [this knowledge base
    article](https://support.cumulusnetworks.com/hc/en-us/articles/204507848)
    on extending NET-SNMP in Cumulus RMP to include data from power
    supplies, fans and temperature sensors.)

  - Resource utilization: Cumulus RMP includes its own resource
    utilization MIB, which is similar to using ` cl-resource-query  `.
    It monitors L3 entries by host, route, nexthops, and L2 MAC/BDPU
    entries. The MIB is defined in
    `/usr/share/snmp/Cumulus-Resource-Query-MIB.txt`.

  - Discard counters: Cumulus RMP also includes its own counters MIB,
    defined in `/usr/share/snmp/Cumulus-Counters-MIB.txt`.

  - The overall Cumulus RMP MIB is defined in
    `/usr/share/snmp/Cumulus-Snmp-MIB.txt`.

### <span>Public Community Disabled</span>

Public community is disabled by default in Cumulus RMP. While it is
disabled, `/etc/snmp/snmpd.conf` will have its public community entry
commented out, like this:

    #rocommunity public default -V systemonly

If the comment is removed, an agent can query the switch with this:

    rocommunity public default -V systemonly

After you make any change to `snmpd.conf`, you must restart `snmpd`
using `service snmpd restart` for the new configuration to take effect.

To define the desired community configuration, use:

    rocommunity <any community> default -V systemonly

## <span>Monitoring System Units Using smond</span>

The `smond` daemon monitors these system units: power, board, temp, fan
and volt. It updates their corresponding LEDs, and logs the change in
the state. Changes in system unit state are detected via the `cpld`
registers. `smond` utilizes these registers to read all sources, which
impacts the health of the system unit, determines the unit's health, and
updates the system LEDs.

Use `smonctl` to display sensor information for the various system
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
| \-j, --json                 | Generates JSON output.                   |
| \-s SENSOR, --sensor SENSOR | Displays data for the specified sensor.  |
| \-v, --verbose              | Displays detailed hardware sensors data. |

For more information, read `man smond` and `man smonctl`.

## <span>Keeping the Switch Alive Using the Hardware Watchdog</span>

Cumulus RMP includes a simplified version of the`  wd_keepalive(8)
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
