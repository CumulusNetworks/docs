---
title: Setting Date and Time
author: Cumulus Networks
weight: 65
aliases:
 - /display/DOCS/Setting+Date+and+Time
 - /pages/viewpage.action?pageId=8362545
pageID: 8362545
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
Setting the time zone, date and time requires root privileges; use
`sudo`.

## <span>Set the Time Zone</span>

You can use one of two methods to set the time zone on the switch:

  - Edit the `/etc/timezone` file.

  - Use the guided wizard.

### <span>Edit the /etc/timezone File</span>

To see the current time zone, list the contents of `/etc/timezone`:

    cumulus@switch:~$ cat /etc/timezone
    US/Eastern

Edit the file to add your desired time zone. A list of valid time zones
can be found at the following
[link](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

Use the following command to apply the new time zone immediately.

    cumulus@switch:~$ sudo dpkg-reconfigure --frontend noninteractive tzdata

### <span>Use the Guided Wizard</span>

To set the time zone using the guided wizard, run `dpkg-reconfigure
tzdata` as root:

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

## <span>Set the Date and Time</span>

The switch contains a battery backed hardware clock that maintains the
time while the switch is powered off and in between reboots. When the
switch is running, the Cumulus Linux operating system maintains its own
software clock.

During boot up, the time from the hardware clock is copied into the
operating system’s software clock. The software clock is then used for
all timekeeping responsibilities. During system shutdown, the software
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

See `man date(1)` for more information.

You can write the current value of the system (software) clock to the
hardware clock using the `hwclock` command:

    cumulus@switch$ sudo hwclock -w

See `man hwclock(8)` for more information.

You can find a good overview of the software and hardware clocks in the
Debian [System Administrator's Manual –
Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html),
specifically the section [Setting and showing hardware
clock](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html#s16.2).

## <span>Set the Time Using NTP and NCLU</span>

The `ntpd` daemon running on the switch implements the NTP protocol. It
synchronizes the system time with time servers listed in
`/etc/ntp.conf`. The `ntpd` daemon is started at boot by default. See
`man ntpd(8)` for `ntpd` details. You can check [this
site](http://nlug.ml1.co.uk/2012/01/ntpq-p-output/831) for an
explanation of the output.

{{%notice note%}}

If you intend to run this service within a
[VRF](/cumulus-linux/Layer_3/Virtual_Routing_and_Forwarding_-_VRF),
including the [management VRF](/cumulus-linux/Layer_3/Management_VRF),
follow [these
steps](Management_VRF.html#src-8362940_ManagementVRF-services) for
configuring the service.

{{%/notice%}}

By default, `/etc/ntp.conf` contains some default time servers. You can
specify the NTP server or servers you want to use with
[NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU);
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
daemon, use `ntpd -q`. This is the same as `ntpdate`, which is to be
retired and no longer available. See `man ntp.conf(5)` for details on
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

To remove one or more NTP servers:

    cumulus@switch:~$ net del time ntp server 0.cumulusnetworks.pool.ntp.org iburst
    cumulus@switch:~$ net del time ntp server 1.cumulusnetworks.pool.ntp.org iburst
    cumulus@switch:~$ net del time ntp server 2.cumulusnetworks.pool.ntp.org iburst
    cumulus@switch:~$ net del time ntp server 3.cumulusnetworks.pool.ntp.org iburst
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

## <span>Specify the NTP Source Interface</span>

You can change the source interface that NTP uses if you want to use an
interface other than eth0, which is the default.

    cumulus@switch:~$ net add time ntp source swp10
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration snippet in the
`ntp.conf` file:

    ...
     
    # Specify interfaces
    interface listen swp10
     
    ...

## <span>NTP Default Configuration</span>

The default NTP configuration comprises the following servers, which are
listed in the `/etc/ntpd.conf` file:

  - server
    [0.cumulusnetworks.pool.ntp.org](http://0.cumulusnetworks.pool.ntp.org)
    iburst

  - server
    [1.cumulusnetworks.pool.ntp.org](http://1.cumulusnetworks.pool.ntp.org)
    iburst

  - server
    [2.cumulusnetworks.pool.ntp.org](http://2.cumulusnetworks.pool.ntp.org)
    iburst

  - server
    [3.cumulusnetworks.pool.ntp.org](http://3.cumulusnetworks.pool.ntp.org)
    iburst

The contents of the `/etc/ntpd.conf` file are listed below.

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

## <span id="src-8362545_SettingDateandTime-PTP" class="confluence-anchor-link"></span><span>Precision Time Protocol (PTP) Boundary Clock</span>

With the growth of low latency and high performance applications,
precision timing has become increasingly important. Precision Time
Protocol (PTP) is used to synchronize clocks in a network and is capable
of sub-microsecond accuracy. The clocks are organized in a master-slave
hierarchy. The slaves are synchronized to their masters, which can be
slaves to their own masters. The hierarchy is created and updated
automatically by the best master clock (BMC) algorithm, which runs on
every clock. The grandmaster clock is the top-level master and is
typically synchronized by using a Global Positioning System (GPS) time
source to provide a high-degree of accuracy.

A boundary clock has multiple ports; one or more master ports and one or
more slave ports. The master ports provide time (the time can originate
from other masters further up the hierarchy) and the slave ports receive
time. The boundary clock absorbs sync messages in the slave port, uses
that port to set its clock, then generates new sync messages from this
clock out of all of its master ports.

Cumulus Linux includes the `linuxptp` package for PTP, which uses the
`phc2sys` daemon to synchronize the PTP clock with the system clock.

{{%notice note%}}

  - Cumulus Linux currently supports PTP on the Mellanox Spectrum ASIC
    only.

  - If you do not perform a full disk image install of Cumulus Linux 3.6
    or later, you need to install the `linuxptp` package with the `sudo
    -E` `apt-get install linuxptp` command.

  - PTP is supported in boundary clock mode only (the switch provides
    timing to downstream servers; it is a slave to a higher-level clock
    and a master to downstream clocks).

  - The switch uses hardware time stamping to capture timestamps from an
    Ethernet frame at the physical layer. This allows PTP to account for
    delays in message transfer and greatly improves the accuracy of time
    synchronization.

  - Only IPv4/UDP PTP packets are supported.

  - Only a single PTP domain per network is supported. A PTP domain is a
    network or a portion of a network within which all the clocks are
    synchronized.

{{%/notice%}}

In the following example, boundary clock 2 receives time from Master 1
(the grandmaster) on a PTP slave port, sets its clock and passes the
time down from the PTP master port to boundary clock 1. Boundary clock 1
receives the time on a PTP slave port, sets its clock and passes the
time down the hierarchy through the PTP master ports to the hosts that
receive the time. <span style="color: #000000;"> </span>

{{% imgOld 0 %}}

  

### <span>Enable the PTP Boundary Clock on the Switch</span>

To enable the PTP boundary clock on the switch:

1.  Open the `/etc/cumulus/switchd.conf` file in a text editor and add
    the following line:
    
        ptp.timestamping = TRUE

2.  Restart `switchd`:
    
        cumulus@switch:~$ sudo systemctl restart switchd.service

### <span>Configure the PTP Boundary Clock</span>

To configure a boundary clock:

1.  Configure the interfaces on the switch that you want to use for PTP.
    Each interface must be configured as a layer 3 routed interface with
    an IP address.
    
    {{%notice note%}}
    
    PTP *is* supported on BGP unnumbered interfaces.
    
    PTP is *not* supported on switched virtual interfaces (SVIs).
    
    {{%/notice%}}
    
        cumulus@switch:~$ net add interface swp13s0 ip address 10.0.0.9/32
        cumulus@switch:~$ net add interface swp13s1 ip address 10.0.0.10/32

2.  Configure PTP options on the switch:
    
      - Set the `gm-capable` option to `no` to configure the switch to
        be a boundary clock.
    
      - Set the priority, which selects the best master clock. You can
        set priority 1 or 2. For each priority, you can use a number
        between 0 and 255. The default priority is 255. For the boundary
        clock, use a number above 128. The lower priority is applied
        first.
    
      - Add the `time-stamping` parameter. The switch automatically
        enables hardware time-stamping to capture timestamps from an
        Ethernet frame at the physical layer. If you are testing PTP in
        a virtual environment, hardware time-stamping is not available;
        however the `time-stamping` parameter is still required.
    
      - Add the PTP master and slave interfaces. You do not specify
        which is a master interface and which is a slave interface; this
        is determined by the PTP packet received.
    
    The following commands provide an example configuration:
    
        cumulus@switch:~$ net add ptp global gm-capable no
        cumulus@switch:~$ net add ptp global priority2 254
        cumulus@switch:~$ net add ptp global priority1 254
        cumulus@switch:~$ net add ptp global time-stamping
        cumulus@switch:~$ net add ptp interface swp13s0
        cumulus@switch:~$ net add ptp interface swp13s1
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit
    
    The `ptp4l` man page describes all the configuration parameters.

3.  Restart the `ptp4l` and `phc2sys` daemons:
    
        cumulus@switch:~$ sudo systemctl restart ptp4l.service phc2sys.service
    
    The configuration is saved in the `/etc/ptp4l.conf` file.

4.  Enable the services to start at boot time:
    
        cumulus@switch:~$ sudo systemctl enable ptp4l.service phc2sys.service

### <span>Example Configuration</span>

In the following example, the boundary clock on the switch receives time
from Master 1 (the grandmaster) on PTP slave port swp3s0, sets its clock
and passes the time down through PTP master ports swp3s1, swp3s2, and
swp3s3 to the hosts that receive the time.

{{% imgOld 1 %}}

<span style="color: #36424a;"> </span>

The configuration for the above example is shown below. The example
assumes that you have already configured the layer 3 routed interfaces
(`swp3s0`, `swp3s1`, `swp3s2`, and `swp3s3`) you want to use for PTP.

    cumulus@switch:~$ net add ptp global gm-capable no
    cumulus@switch:~$ net add ptp global priority2 254
    cumulus@switch:~$ net add ptp global priority1 254
    cumulus@switch:~$ net add ptp global time-stamping
    cumulus@switch:~$ net add ptp interface swp3s0
    cumulus@switch:~$ net add ptp interface swp3s1
    cumulus@switch:~$ net add ptp interface swp3s2
    cumulus@switch:~$ net add ptp interface swp3s3
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

### <span>Verify PTP Boundary Clock Configuration</span>

To view a summary of the PTP configuration on the switch, run the `net
show configuration ptp` command:

    cumulus@switch:~$ net show configuration ptp
      
    ptp
      global
     
        slaveOnly
          0
        
        priority1
          255
        
        priority2
          255
        
        domainNumber
          0
        
        logging_level
          5
        
        path_trace_enabled
          0
        
        use_syslog
          1
        
        verbose
          0
        
        summary_interval
          0
        
        time_stamping
          hardware
        
        gmCapable
          0
      swp15s0
      swp15s1
    ...

### <span>View PTP Status Information</span>

To view PTP status information, run the `net show ptp parent_data_set`
command:

    cumulus@switch:~$ net show ptp parent_data_set
    parent_data_set
    ===============
    parentPortIdentity                    000200.fffe.000001-1
    parentStats                           0
    observedParentOffsetScaledLogVariance 0xffff
    observedParentClockPhaseChangeRate    0x7fffffff
    grandmasterPriority1                  127
    gm.ClockClass                         248
    gm.ClockAccuracy                      0xfe
    gm.OffsetScaledLogVariance            0xffff
    grandmasterPriority2                  127
    grandmasterIdentity                   000200.fffe.000001

To view the additional PTP status information, including the delta in
nanoseconds from the master clock, run the `sudo pmc -u -b 0 'GET
TIME_STATUS_NP'` command:

    cumulus@switch:~$ sudo pmc -u -b 0 'GET TIME_STATUS_NP'
    sending: GET TIME_STATUS_NP
        7cfe90.fffe.f56dfc-0 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
            master_offset              12610
            ingress_time               1525717806521177336
            cumulativeScaledRateOffset +0.000000000
            scaledLastGmPhaseChange    0
            gmTimeBaseIndicator        0
            lastGmPhaseChange          0x0000'0000000000000000.0000
            gmPresent                  true
            gmIdentity                 000200.fffe.000005
        000200.fffe.000005-1 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
            master_offset              0
            ingress_time               0
            cumulativeScaledRateOffset +0.000000000
            scaledLastGmPhaseChange    0
            gmTimeBaseIndicator        0
            lastGmPhaseChange          0x0000'0000000000000000.0000
            gmPresent                  false
            gmIdentity                 000200.fffe.000005
        000200.fffe.000006-1 seq 0 RESPONSE MANAGEMENT TIME_STATUS_NP
            master_offset              5544033534
            ingress_time               1525717812106811842
            cumulativeScaledRateOffset +0.000000000
            scaledLastGmPhaseChange    0
            gmTimeBaseIndicator        0
            lastGmPhaseChange          0x0000'0000000000000000.0000
            gmPresent                  true
            gmIdentity                 000200.fffe.000005

### <span>Delete PTP Boundary Clock Configuration</span>

To delete PTP configuration, delete the PTP master and slave interfaces.
The following example commands delete the PTP interfaces `swp3s0`,
`swp3s1`, and `swp3s2`.

    cumulus@switch:~$ net del ptp interface swp3s0
    cumulus@switch:~$ net del ptp interface swp3s1
    cumulus@switch:~$ net del ptp interface swp3s2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

## <span>Use NTP in a DHCP Environment</span>

If you use DHCP and want to specify your NTP servers, you must specify
an alternate configuration file for NTP.

Before you create the file, ensure that the DHCP-generated configuration
file exists. In Cumulus Linux 3.6.1 and later (which uses NTP 1:4.2.8),
the DHCP-generated file is named `/run/ntp.conf.dhcp` while in Cumulus
Linux 3.6.0 and earlier (which uses NTP 1:4.2.6) the file is named
`/var/lib/ntp/ntp.conf.dhcp`. This file is generated by the
`/etc/dhcp/dhclient-exit-hooks.d/ntp` script and is a copy of the
default `/etc/ntp.conf` with a modified server list from the DHCP
server. If this file does not exist and you plan on using DHCP in the
future, you can copy your current `/etc/ntp.conf` file to the location
of the DHCP file.

To use an alternate configuration file that persists across upgrades of
Cumulus Linux, create a `systemd` unit override file called
`/etc/systemd/system/ntp.service.d/config.conf` and add the following
content:

    cumulus@switch:~$ sudo echo '
    [Service]
    ExecStart=
    ExecStart=/usr/sbin/ntpd -n -u ntp:ntp -g -c /run/ntp.conf.dhcp
    '  > ~/over
    sudo mkdir -p /etc/systemd/system/ntp.service.d
    sudo mv ~/over /etc/systemd/system/ntp.service.d/dhcp.conf
    sudo chown root:root /etc/systemd/system/ntp.service.d/dhcp.conf

To validate that your configuration, run these commands:

    cumulus@switch:~$ sudo systemctl daemon-reload
    cumulus@switch:~$ sudo systemctl restart ntp
    cumulus@switch:~$ sudo systemctl status -n0 ntp.service

If the state is not *Active*, or the alternate configuration file does
not appear in the `ntp` command line — for example:

    cumulus@switch:~$ /usr/sbin/ntpd -n -u ntp:ntp -g -c /run/ntp.conf.dhcp

— then it is likely that a mistake was made. In this case, correct the
mistake and rerun the three commands above to verify.

{{%notice note%}}

With this unit file override present, changing NTP settings using NCLU
do not take effect until the DHCP script regenerates the alternate NTP
configuration file.

{{%/notice%}}

## <span>System Clock and NCLU Commands</span>

If you provision a new switch without setting the system clock (manually
or with NTP or PTP), the NCLU `net commit` command fails when the system
clock is earlier than the modification date of configuration files. Make
sure to set the system clock on the switch.

## <span>Related Information</span>

  - [Debian System Administrator’s Manual –
    Time](http://www.debian.org/doc/manuals/system-administrator/ch-sysadmin-time.html)

  - [www.ntp.org](http://www.ntp.org)

  - [en.wikipedia.org/wiki/Network\_Time\_Protocol](http://en.wikipedia.org/wiki/Network_Time_Protocol)

  - [wiki.debian.org/NTP](http://wiki.debian.org/NTP)
