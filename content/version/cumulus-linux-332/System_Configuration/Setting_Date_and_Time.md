---
title: Setting Date and Time
author: Cumulus Networks
weight: 65
aliases:
 - /display/CL332/Setting+Date+and+Time
 - /pages/viewpage.action?pageId=5868873
pageID: 5868873
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
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
switch is running, the Cumulus Linux operating system maintains its own
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

## <span>Setting Time Using NTP and NCLU</span>

The `ntpd` daemon running on the switch implements the NTP protocol. It
synchronizes the system time with time servers listed in
`/etc/ntp.conf`. It is started at boot by default. See `man ntpd(8)` for
`ntpd` details.

By default, `/etc/ntp.conf` contains some default time servers. You can
specify the NTP server or servers you want to use with
[NCLU](/version/cumulus-linux-332/System_Configuration/Network_Command_Line_Utility);
include the `iburst` option to increase the sync speed.

    cumulus@switch:~$ net add time ntp server 4.cumulusnetworks.pool.ntp.org iburst
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands add the NTP server to the list of servers in
`/etc/ntp.conf`:

    # pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
    # pick a different set every time it starts up.  Please consider joining the
    # pool: <http://www.pool.ntp.org/join.html>
    server 0.cumulusnetworks.pool.ntp.org iburst
    server 1.cumulusnetworks.pool.ntp.org iburst
    server 2.cumulusnetworks.pool.ntp.org iburst
    server 3.cumulusnetworks.pool.ntp.org iburst
    server 4.cumulusnetworks.pool.ntp.org iburst

To set the initial date and time via NTP before starting the `ntpd`
daemon, use `ntpd -q`. This is same as `ntpdate`, which is to be retired
and no longer available. See `man ntp.conf(5)` for details on
configuring `ntpd` using `ntp.conf`.

{{%notice note%}}

`ntpd -q` can hang if the time servers are not reachable.

{{%/notice%}}

To verify that `ntpd` is running on the system:

    cumulus@switch:~$ ps -ef | grep ntp
    ntp       4074     1  0 Jun20 ?        00:00:33 /usr/sbin/ntpd -p /var/run/ntpd.pid -g -u 101:102

To check the NTP peer status:

    cumulus@switch:~$ net show time ntp servers 
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
    +minime.fdf.net  58.180.158.150   3 u  140 1024  377   55.659    0.339   1.464
    +69.195.159.158  128.138.140.44   2 u  259 1024  377   41.587    1.011   1.677
    *chl.la          216.218.192.202  2 u  210 1024  377    4.008    1.277   1.628
    +vps3.drown.org  17.253.2.125     2 u  743 1024  377   39.319   -0.316   1.384

## <span>Specifying the NTP Source Interface</span>

You can change the source interface that NTP uses if you want to use an
interface other than eth0, the default.

    cumulus@switch:~$ net add time ntp source swp10
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`ntp.conf` file:

    ...
     
    # Specify interfaces
    interface listen swp10
     
    ...

## <span>Forcing NTP Syncronization</span>

NTP is a notoriously slow protocol that takes significant time to
converge. It is possible to jumpstart the process by just accepting the
upstream values instantly. In the past the ntpdate application would
have been used for this task but that application has become deprecated
and is not included by default in Cumulus Linux. The technique below can
be especially useful when the Local and Upstream time servers have a
significant drift between them. Start by stopping the existing NTP
service. Force the NTP daemon to use the configured servers to quickly
accept the upstream time values without question. Then restart the
normal operation of the NTP service.

    cumulus@switch:~$ sudo systemctl stop ntp
    cumulus@switch:~$ sudo ntpd -gq
    ntpd: time slew +0.001789s
    cumulus@switch:~$ sudo systemctl start ntp

{{%notice note%}}

If NTP is running in the MGMT VRF substitute ntp@mgmt for the service
name above

{{%/notice%}}

## <span>NTP Default Configuration</span>

The default NTP configuration comprises the following servers, which are
listed in the `/etc/ntpd.conf` file:

  - server 0.cumulusnetworks.pool.ntp.org iburst

  - server 1.cumulusnetworks.pool.ntp.org iburst

  - server 2.cumulusnetworks.pool.ntp.org iburst

  - server 3.cumulusnetworks.pool.ntp.org iburst

If you need to restore the default NTP configuration, its contents are
listed below.

Default ntpd.conf file ...

    # /etc/ntp.conf, configuration for ntpd; see ntp.conf(5) for help
     
    driftfile /var/lib/ntp/ntp.drift
     
     
    # Enable this if you want statistics to be logged.
    #statsdir /var/log/ntpstats/
     
    statistics loopstats peerstats clockstats
    filegen loopstats file loopstats type day enable
    filegen peerstats file peerstats type day enable
    filegen clockstats file clockstats type day enable
     
     
    # You do need to talk to an NTP server or two (or three).
    #server ntp.your-provider.example
     
    # pool.ntp.org maps to about 1000 low-stratum NTP servers.  Your server will
    # pick a different set every time it starts up.  Please consider joining the
    # pool: <http://www.pool.ntp.org/join.html>
    server 0.cumulusnetworks.pool.ntp.org iburst
    server 1.cumulusnetworks.pool.ntp.org iburst
    server 2.cumulusnetworks.pool.ntp.org iburst
    server 3.cumulusnetworks.pool.ntp.org iburst
     
     
    # Access control configuration; see /usr/share/doc/ntp-doc/html/accopt.html for
    # details.  The web page <http://support.ntp.org/bin/view/Support/AccessRestrictions>
    # might also be helpful.
    #
    # Note that "restrict" applies to both servers and clients, so a configuration
    # that might be intended to block requests from certain clients could also end
    # up blocking replies from your own upstream servers.
     
    # By default, exchange time with everybody, but don't allow configuration.
    restrict -4 default kod notrap nomodify nopeer noquery
    restrict -6 default kod notrap nomodify nopeer noquery
     
    # Local users may interrogate the ntp server more closely.
    restrict 127.0.0.1
    restrict ::1
     
    # Clients from this (example!) subnet have unlimited access, but only if
    # cryptographically authenticated.
    #restrict 192.168.123.0 mask 255.255.255.0 notrust
     
     
    # If you want to provide time to your local subnet, change the next line.
    # (Again, the address is an example only.)
    #broadcast 192.168.123.255
     
    # If you want to listen to time broadcasts on your local subnet, de-comment the
    # next lines.  Please do this only if you trust everybody on the network!
    #disable auth
    #broadcastclient
     
    # Specify interfaces, don't listen on switch ports
    interface listen eth0

## <span>Related Information</span>

  - [Debian System Administrator’s Manual –
    Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

  - [www.ntp.org](http://www.ntp.org)

  - [en.wikipedia.org/wiki/Network\_Time\_Protocol](http://en.wikipedia.org/wiki/Network_Time_Protocol)

  - [wiki.debian.org/NTP](http://wiki.debian.org/NTP)
