---
title: Setting Date and Time
author: Cumulus Networks
weight: 37
aliases:
 - /display/RMP321/Setting+Date+and+Time
 - /pages/viewpage.action?pageId=5127537
pageID: 5127537
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
Setting the time zone, date and time requires root privileges; use
`sudo`.

## <span>Setting the Time Zone</span>

To see the current time zone, list the contents of `/etc/timezone`:

    cumulus@switch:~$ cat /etc/timezone
    US/Eastern

Edit the file to add your desired time zone. A list of valid time zones
can be found at the following
[link](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

Use the following command to apply the new time zone immediately.

    cumulus@switch:~$ sudo dpkg-reconfigure --frontend noninteractive tzdata

### <span>Alternative: Use the Guided Wizard to Find and Apply a Time Zone</span>

To set the time zone, run `dpkg-reconfigure tzdata` as root:

    cumulus@switch:~$ sudo dpkg-reconfigure tzdata

Then navigate the menus to enable the time zone you want. The following
example selects the *US/Pacific* time zone:

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
command. First, determine your current time zone:

    cumulus@switch$ date +%Z

{{%notice note%}}

If you need to reconfigure the current time zone, refer to the
instructions above.

{{%/notice%}}

Then, to set the system clock according to the time zone configured:

    cumulus@switch$ sudo date -s "Tue Jan 12 00:37:13 2016"

See `man date(1)` for if you need more information.

You can write the current value of the system (software) clock to the
hardware clock using the `hwclock` command:

    cumulus@switch$ sudo hwclock -w

See `man hwclock(8)` if you need more information.

You can find a good overview of the software and hardware clocks in the
Debian [System Administrator's Manual –
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
ntp.conf(5)` for details on configuring `ntpd` using `ntp.conf`.

To set the initial date and time via NTP before starting the `ntpd`
daemon, use `ntpd -q` (This is same as `ntpdate`, which is to be retired
and not available).

{{%notice note%}}

`ntpd -q` can hang if the time servers are not reachable.

{{%/notice%}}

To verify that `ntpd` is running on the system:

    cumulus@switch:~$ ps -ef | grep ntp
    ntp       4074     1  0 Jun20 ?        00:00:33 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 101:102

To check the NTP peer status:

    cumulus@switch:~$ ntpq -p
     
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    *level1f.cs.unc. .PPS.            1 u  225 1024  377   92.505   -1.296   1.139
    +ip.tcp.lv       193.11.166.8     2 u   29 1024  377  192.701    2.424   1.227
    -host-86.3.217.2 131.107.13.100   2 u 1024 1024  367  240.622   11.250   7.785
    +li290-38.member 128.138.141.172  2 u  553 1024  377   38.944   -0.810   1.139

## <span>Specifying the NTP Source Interface</span>

You can change the source interface that NTP uses if you want to use
something other than the default of eth0. Edit `ntp.conf` and edit the
entry under the **\# Specify interfaces** comment:

    cumulus@switch:~$ sudo nano /etc/ntp.conf
    ...
     
    # Specify interfaces
    interface listen bridge10

## <span>Related Information</span>

  - [Debian System Administrator’s Manual –
    Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

  - [www.ntp.org](http://www.ntp.org)

  - [en.wikipedia.org/wiki/Network\_Time\_Protocol](http://en.wikipedia.org/wiki/Network_Time_Protocol)

  - [wiki.debian.org/NTP](http://wiki.debian.org/NTP)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
