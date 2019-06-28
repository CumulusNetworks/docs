---
title: Setting Date and Time
author: Cumulus Networks
weight: 35
aliases:
 - /display/RMP25ESR/Setting+Date+and+Time
 - /pages/viewpage.action?pageId=5116309
pageID: 5116309
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
Setting the time zone, date and time requires root privileges; use
`sudo`.

## <span>Commands</span>

  - date

  - dpkg-reconfigure tzdata

  - hwclock

  - ntpd (daemon)

  - ntpq

## <span>Setting the Time Zone</span>

To see the current time zone, list the contents of `/etc/timezone`:

    cumulus@switch:~$ cat /etc/timezone
    US/Eastern

To set the time zone, run `dpkg-reconfigure tzdata` as root:

    cumulus@switch:~$ sudo dpkg-reconfigure tzdata

Then navigate the menus to enable the time zone you want. The following
example selects the US/Pacific time zone:

    cumulus@switch:~$ sudo dpkg-reconfigure tzdata
    
    Configuring tzdata
    ------------------
    
    Please select the geographic area in which you live. Subsequent configuration
    questions will narrow this down by presenting a list of cities, representing
    the time zones in which they are located.
    
      1. Africa      4. Australia  7. Atlantic  10. Pacific  13. Etc
      2. America     5. Arctic     8. Europe    11. SystemV
      3. Antarctica  6. Asia       9. Indian    12. US
    Geographic area: 12
    
    Please select the city or region corresponding to your time zone.
    
      1. Alaska    4. Central  7. Indiana-Starke  10. Pacific
      2. Aleutian  5. Eastern  8. Michigan        11. Pacific-New
      3. Arizona   6. Hawaii   9. Mountain        12. Samoa
    Time zone: 10
    
    Current default time zone: 'US/Pacific'
    Local time is now:      Mon Jun 17 09:27:45 PDT 2013.
    Universal Time is now:  Mon Jun 17 16:27:45 UTC 2013.

For more info see the Debian [System Administrator’s Manual –
Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html).

## <span>Setting the Date and Time</span>

The switch contains a battery backed hardware clock that maintains the
time while the switch is powered off and in between reboots. When the
switch is running, the Cumulus RMP operating system maintains its own
software clock.

During boot up, the time from the hardware clock is copied into the
operating system’s software clock. The software clock is then used for
all timekeeping responsibilities. During system shutdown the software
clock is copied back to the battery backed hardware clock.

You can set the date and time on the software clock using the `date`
command. See `man date(1)` for details.

You can set the date and time on the hardware clock using the `hwclock`
command. See man `hwclock(8)` for details.

A good overview of the software and hardware clocks can be found in the
Debian [System Administrator’s Manual –
Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html),
specifically the section [Setting and showing hardware
clock](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.2).

## <span>Setting Time Using NTP</span>

The `ntpd` daemon running on the switch implements the NTP protocol. It
synchronizes the system time with time servers listed in
`/etc/ntp.conf`. It is started at boot by default. See `man ntpd(8)` for
`ntpd` details.

By default, `/etc/ntp.conf` contains some default time servers. Edit
`/etc/ntp.conf` to add or update time server information. See `man
ntp.conf(5)` for details on configuring `ntpd` using `ntp.conf.`

To set the initial date and time via NTP before starting the `ntpd`
daemon, use `ntpd` -`q` (This is same as `ntpdate`, which is to be
retired and not available).

{{%notice note%}}

`ntpd -q` can hang if the time servers are not reachable.

{{%/notice%}}

To verify that `ntpd` is running on the system:

    cumulus@switch:~$ ps -ef | grep ntp
    ntp       4074     1  0 Jun20 ?        00:00:33 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 101:102

## <span>Configuration Files</span>

  - /etc/default/ntp — `ntpd init.d` configuration variables

  - /etc/ntp.conf — default NTP configuration file

  - /etc/init.d/ntp — `ntpd init` script

## <span>Useful Links</span>

  - [Debian System Administrator’s Manual –
    Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

  - <http://www.ntp.org>

  - <http://en.wikipedia.org/wiki/Network_Time_Protocol>

  - <http://wiki.debian.org/NTP>
