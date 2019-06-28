---
title: Monitoring and Troubleshooting
author: Cumulus Networks
weight: 25
aliases:
 - /display/CL36/Monitoring+and+Troubleshooting
 - /pages/viewpage.action?pageId=8362087
pageID: 8362087
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
This chapter introduces monitoring and troubleshooting Cumulus Linux.

## <span>Using the Serial Console</span>

The serial console can be a useful tool for debugging issues, especially
when you find yourself rebooting the switch often or if you don’t have a
reliable network connection.

The default serial console baud rate is 115200, which is the baud rate
[ONIE](http://opencomputeproject.github.io/onie/) uses.

### <span>Configuring the Serial Console on ARM Switches</span>

On ARM switches, the U-Boot environment variable `baudrate` identifies
the baud rate of the serial console. To change the `baudrate` variable,
use the `fw_setenv` command:

    cumulus@switch:~$ sudo fw_setenv baudrate 9600
    Updating environment variable: `baudrate'
    Proceed with update [N/y]? y

You must reboot the switch for the `baudrate` change to take effect.

The valid values for `baudrate` are:

  - 300

  - 600

  - 1200

  - 2400

  - 4800

  - 9600

  - 19200

  - 38400

  - 115200

### <span>Configuring the Serial Console on x86 Switches</span>

On x86 switches, you configure serial console baud rate by editing
`grub`.

{{%notice warning%}}

Incorrect configuration settings in `grub` can cause the switch to be
inaccessible via the console. Grub changes should be carefully reviewed
before implementation.

{{%/notice%}}

The valid values for the baud rate are:

  - 300

  - 600

  - 1200

  - 2400

  - 4800

  - 9600

  - 19200

  - 38400

  - 115200

To change the serial console baud rate:

1.  Edit `/etc/default/grub`. The two relevant lines in
    `/etc/default/grub` are as follows; replace the *115200* value with
    a valid value specified above in the `--speed` variable in the first
    line and in the `console` variable in the second line:
    
        GRUB_SERIAL_COMMAND="serial --port=0x2f8 --speed=115200 --word=8 --parity=no --stop=1"              
        GRUB_CMDLINE_LINUX="console=ttyS1,115200n8 cl_platform=accton_as5712_54x"

2.  After you save your changes to the grub configuration, type the
    following at the command prompt:
    
        cumulus@switch:~$ update-grub

3.  If you plan on accessing your switch's BIOS over the serial console,
    you need to update the baud rate in the switch BIOS. For more
    information, see [this knowledge base
    article](https://support.cumulusnetworks.com/hc/en-us/articles/203884473).

4.  Reboot the switch.

## <span>Getting General System Information</span>

Two commands are helpful for getting general information about the
switch and the version of Cumulus Linux you are running. These are
helpful with system diagnostics and if you need to submit a support
request to Cumulus Networks.

For information about the version of Cumulus Linux running on the
switch, run `net show version`, which displays the contents of
`/etc/lsb-release`:

    cumulus@switch:~$ net show version
    NCLU_VERSION=1.0
    DISTRIB_ID="Cumulus Linux"
    DISTRIB_RELEASE=3.4.0
    DISTRIB_DESCRIPTION="Cumulus Linux 3.4.0"

For general information about the switch, run `net show system`, which
gathers information about the switch from a number of files in the
system:

    cumulus@switch:~$ net show system
     
    Penguin Arctica 4806XP
    Cumulus Version 3.4.0
    Build: Cumulus Linux 3.4.0
     
    Chipset: Broadcom Trident2 BCM56854
     
    Port Config: 48 x 10G-SFP+ & 6 x 40G-QSFP+
     
    CPU: (x86_64) Intel Atom C2558 2.40GHz
     
    Uptime: 4 days, 20:53:49

## <span>Diagnostics Using cl-support</span>

You can use `cl-support` to generate a single export file that contains
various details and the configuration from a switch. This is useful for
remote debugging and troubleshooting. For more information about
`cl-support`, read [Understanding the cl-support Output
File](/version/cumulus-linux-36/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/).

You should run `cl-support` before you submit a support request to
Cumulus Networks as this file helps in the investigation of issues.

    cumulus@switch:~$ sudo cl-support -h
    Usage: cl-support [-h] [-s] [-t] [-v] [reason]...
     
    Args:
    [reason]: Optional reason to give for invoking cl-support.
             Saved into tarball's cmdline.args file.
    Options:
    -h: Print this usage statement
    -s: Security sensitive collection
    -t: User filename tag
    -v: Verbose
    -e MODULES: Enable modules. Comma separated module list (run with -e help for module names)
    -d MODULES: Disable modules. Comma separated module list (run with -d help for module names)

## <span id="src-8362087_MonitoringandTroubleshooting-syslog_server" class="confluence-anchor-link"></span><span>Sending Log Files to a syslog Server</span>

### <span>Using NCLU</span>

The remote syslog server can be configured on the switch using the
following configuration:

    cumulus@switch:~$ net add syslog host ipv4 192.168.0.254 port udp 514

This creates a file called `/etc/rsyslog.d/11-remotesyslog.conf` in the
`rsyslog` directory. The file has the following content:

    cumulus@switch:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
    # This file was automatically generated by NCLU.
    *.*   @192.168.0.254:514   # UDP

{{%notice note%}}

NCLU cannot configure a remote syslog if management VRF is enabled on
the switch. To do so, please refer to the section [Writing to syslog
with Management VRF
Enabled](#src-8362087_MonitoringandTroubleshooting-mgmtvrf) below.

{{%/notice%}}

### <span>Logging Technical Details</span>

Logging on Cumulus Linux is done with
[rsyslog](http://www.rsyslog.com/). `rsyslog` provides both local
logging to the `syslog` file as well as the ability to export logs to an
external `syslog` server. High precision timestamps are enabled for all
`rsyslog` log files; here's an example:

    2015-08-14T18:21:43.337804+00:00 cumulus switchd[3629]: switchd.c:1409 switchd version 1.0-cl2.5+5

There are applications in Cumulus Linux that could write directly to a
log file without going through `rsyslog`. These files are typically
located in `/var/log/`.

{{%notice note%}}

All Cumulus Linux rules are stored in separate files in
`/etc/rsyslog.d/`, which are called at the end of the `GLOBAL
DIRECTIVES` section of `/etc/rsyslog.conf`. As a result, the `RULES`
section at the end of `rsyslog.conf` is ignored because the messages
have to be processed by the rules in `/etc/rsyslog.d` and then dropped
by the last line in `/etc/rsyslog.d/99-syslog.conf`.

{{%/notice%}}

### <span>Local Logging</span>

Most logs within Cumulus Linux are sent through `rsyslog`, which then
writes them to files in the `/var/log` directory. There are default
rules in the `/etc/rsyslog.d/` directory that define where the logs are
written:

| Rule              | Purpose                                                                                                                                                                  |
| ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 10-rules.conf     | Sets defaults for log messages, include log format and log rate limits.                                                                                                  |
| 15-crit.conf      | Logs crit, alert or emerg log messages to `/var/log/crit.log` to ensure they are not rotated away rapidly.                                                               |
| 20-clagd.conf     | Logs `clagd` messages to `/var/log/clagd.log` for [MLAG](/version/cumulus-linux-36/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG).                                       |
| 22-linkstate.conf | Logs link state changes for all physical and logical network links to `/var/log/linkstate`                                                                               |
| 25-switchd.conf   | Logs `switchd` messages to `/var/log/switchd.log`.                                                                                                                       |
| 30-ptmd.conf      | Logs `ptmd` messages to `/var/log/ptmd.log` for [Prescription Topology Manager](/version/cumulus-linux-36/Layer_1_and_Switch_Ports/Prescriptive_Topology_Manager_-_PTM). |
| 35-rdnbrd.conf    | Logs `rdnbrd` messages to `/var/log/rdnbrd.log` for [redistribute neighbor](/version/cumulus-linux-36/Layer_3/Redistribute_Neighbor).                                    |
| 40-netd.conf      | Logs `netd` messages to `/var/log/netd.log` for [NCLU](/version/cumulus-linux-36/System_Configuration/Network_Command_Line_Utility_-_NCLU/).                             |
| 45-frr.conf       | Logs routing protocol messages to /var/log/frr/frr.log. This includes BGP and OSPF log messages.                                                                         |
| 99-syslog.conf    | All remaining processes that use `rsyslog` are sent to `/var/log/syslog`.                                                                                                |

Log files that are rotated are compressed into an archive. Processes
that do not use `rsyslog` write to their own log files within the
`/var/log` directory. For more information on specific log files, see
[Troubleshooting Log
Files](/version/cumulus-linux-36/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_Log_Files).

### <span>Enabling Remote syslog</span>

If you need to send other log files — such as `switchd` logs — to a
`syslog` server, do the following:

1.  Create a file in `/etc/rsyslog.d/`. Make sure it starts with a
    number lower than 99 so that it executes before log messages are
    dropped in, such as `20-clagd.conf` or `25-switchd.conf`. Our
    example file is called `/etc/rsyslog.d/11-remotesyslog.conf`. Add
    content similar to the following:
    
        ## Logging switchd messages to remote syslog server
         
        @192.168.1.2:514
    
    This configuration sends log messages to a remote `syslog` server
    for the following processes: `clagd`, `switchd`, `ptmd`, `rdnbrd`,
    `netd` and `syslog`. It follows the same syntax as the
    `/var/log/syslog` file, where *@* indicates UDP, *192.168.1.2* is
    the IP address of the `syslog` server, and *514* is the UDP port.
    
    {{%notice note%}}
    
    For TCP-based syslog, use two @@ before the IP address:
    *@@192.168.1.2:514*.
    
    Running `syslog` over TCP places a burden on the switch to queue
    packets in the `syslog` buffer. This may cause detrimental effects
    if the remote `syslog` server becomes unavailable.
    
    {{%/notice%}}
    
    {{%notice note%}}
    
    The numbering of the files in `/etc/rsyslog.d/` dictates how the
    rules are installed into `rsyslog.d`. If you want to remotely log
    only the messages in `/var/syslog`, and not those in
    `/var/log/clagd.log` or `/var/log/switchd.log`, for instance, then
    name the file `98-remotesyslog.conf`, since it's lower than the
    `/var/syslog` file `99-syslog.conf` only.
    
    {{%/notice%}}
    
    {{%notice note%}}
    
    Do not use the `imfile` module with any file written by `rsyslogd`.
    
    {{%/notice%}}

2.  Restart `rsyslog`.
    
        cumulus@switch:~$ sudo systemctl restart rsyslog.service

### <span id="src-8362087_MonitoringandTroubleshooting-mgmtvrf" class="confluence-anchor-link"></span><span>Writing to syslog with Management VRF Enabled</span>

You can write to syslog with [management
VRF](/version/cumulus-linux-36/Layer_3/Management_VRF) enabled by
applying the following configuration; this configuration is commented
out in the `/etc/rsyslog.d/11-remotesyslog.conf` file:

    cumulus@switch:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
    ## Copy all messages to the remote syslog server at 192.168.0.254 port 514
    action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp")

For each syslog server, configure a unique ` action  `line. For example,
to configure two syslog servers at 192.168.0.254 and 10.0.0.1:

    cumulus@switch:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
    ## Copy all messages to the remote syslog servers at 192.168.0.254 and 10.0.0.1 port 514
    action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp")
    action(type="omfwd" Target="10.0.0.1" Device="mgmt" Port="514" Protocol="udp")

### <span>Rate-limiting syslog Messages</span>

If you want to limit the number of `syslog` messages that can be written
to the `syslog` file from individual processes, add the following
configuration to `/etc/rsyslog.conf`. Adjust the interval and burst
values to rate-limit messages to the appropriate levels required by your
environment. For more information, read the [rsyslog
documentation](http://www.rsyslog.com/doc/v8-stable/configuration/modules/imuxsock.html).

    module(load="imuxsock"
          SysSock.RateLimit.Interval="2" SysSock.RateLimit.Burst="50")

The following test script shows an example of rate-limit output in
Cumulus Linux ...

    root@leaf1:mgmt-vrf:/home/cumulus# cat ./syslog.py 
    #!/usr/bin/python
    import syslog
    message_count=100
    print "Sending %s Messages..."%(message_count)
    for i in range(0,message_count):
    syslog.syslog("Message Number:%s"%(i))
    print "DONE."
     
    root@leaf1:mgmt-vrf:/home/cumulus# ./syslog.py 
    Sending 100 Messages...
    DONE.
     
    root@leaf1:mgmt-vrf:/home/cumulus# tail -n 60 /var/log/syslog
    2017-02-22T19:59:50.043342+00:00 leaf1 syslog.py[22830]: Message Number:0
    2017-02-22T19:59:50.043723+00:00 leaf1 syslog.py[22830]: Message Number:1
    2017-02-22T19:59:50.043941+00:00 leaf1 syslog.py[22830]: Message Number:2
    2017-02-22T19:59:50.044565+00:00 leaf1 syslog.py[22830]: Message Number:3
    2017-02-22T19:59:50.044830+00:00 leaf1 syslog.py[22830]: Message Number:4
    2017-02-22T19:59:50.045680+00:00 leaf1 syslog.py[22830]: Message Number:5
    <...snip...>
    2017-02-22T19:59:50.056727+00:00 leaf1 syslog.py[22830]: Message Number:45
    2017-02-22T19:59:50.057599+00:00 leaf1 syslog.py[22830]: Message Number:46
    2017-02-22T19:59:50.057741+00:00 leaf1 syslog.py[22830]: Message Number:47
    2017-02-22T19:59:50.057936+00:00 leaf1 syslog.py[22830]: Message Number:48
    2017-02-22T19:59:50.058125+00:00 leaf1 syslog.py[22830]: Message Number:49
    2017-02-22T19:59:50.058324+00:00 leaf1 rsyslogd-2177: imuxsock[pid 22830]: begin to drop messages due to rate-limiting

### <span>Harmless syslog Error: Failed to reset devices.list</span>

The following message gets logged to `/var/log/syslog` when you run
`systemctl daemon-reload` and during system boot:

    systemd[1]: Failed to reset devices.list on /system.slice: Invalid argument

This message is harmless, and can be ignored. It is logged when
`systemd` attempts to change cgroup attributes that are read only. The
upstream version of systemd has been modified to not log this message by
default.

The `systemctl daemon-reload` command is often issued when Debian
packages are installed, so the message may be seen multiple times when
upgrading packages.

### <span>Syslog Troubleshooting Tips</span>

You can use the following commands to troubleshoot `syslog` issues.

#### <span>Verifying that rsyslog is Running</span>

To verify that the `rsyslog` service is running, use the `sudo systemctl
status rsyslog.service` command:

     cumulus@leaf01:mgmt-vrf:~$ sudo systemctl status rsyslog.service
     rsyslog.service - System Logging Service
       Loaded: loaded (/lib/systemd/system/rsyslog.service; enabled)
       Active: active (running) since Sat 2017-12-09 00:48:58 UTC; 7min ago
         Docs: man:rsyslogd(8)
               http://www.rsyslog.com/doc/
     Main PID: 11751 (rsyslogd)
       CGroup: /system.slice/rsyslog.service
               └─11751 /usr/sbin/rsyslogd -n
     
    Dec 09 00:48:58 leaf01 systemd[1]: Started System Logging Service.

#### <span>Verifying your rsyslog Configuration.</span>

After making manual changes to any files in the `/etc/rsyslog.d`
directory, use the `sudo rsyslogd -N1` command to identify any errors in
the configuration files that might prevent the `rsyslog` service from
starting.

In the following example, a closing parenthesis is missing in the
`11-remotesyslog.conf` file, which is used to configure `syslog` for
management VRF:

    cumulus@leaf01:mgmt-vrf:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
    action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp"
     
    cumulus@leaf01:mgmt-vrf:~$ sudo rsyslogd -N1
    rsyslogd: version 8.4.2, config validation run (level 1), master config /etc/rsyslog.conf
    rsyslogd: error during parsing file /etc/rsyslog.d/15-crit.conf, on or before line 3: invalid character '$' in object definition - is there an invalid escape sequence somewhere? [try http://www.rsyslog.com/e/2207 ]
    rsyslogd: error during parsing file /etc/rsyslog.d/15-crit.conf, on or before line 3: syntax error on token 'crit_log' [try http://www.rsyslog.com/e/2207 ]

After correcting the invalid syntax, issuing the ` sudo  ``rsyslogd -N1`
command produces the following output.

    cumulus@leaf01:mgmt-vrf:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
    action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp")
    cumulus@leaf01:mgmt-vrf:~$ sudo rsyslogd -N1
    rsyslogd: version 8.4.2, config validation run (level 1), master config /etc/rsyslog.conf
    rsyslogd: End of config validation run. Bye.

#### <span>Using tcpdump</span>

If a syslog server is not accessible to validate that `syslog` messages
are being exported, you can use `tcpdump`.

In the following example, a syslog server has been configured at
192.168.0.254 for UDP syslogs on port 514:

    cumulus@leaf01:mgmt-vrf:~$ sudo tcpdump -i eth0 host 192.168.0.254 and udp port 514

A simple way to generate `syslog` messages is to use `sudo` in another
session, such as `sudo date`. Using `sudo` generates an `authpriv` log.

    cumulus@leaf01:mgmt-vrf:~$ sudo tcpdump -i eth0 host 192.168.0.254 and udp port 514
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
    00:57:15.356836 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.notice, length: 105
    00:57:15.364346 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.info, length: 103
    00:57:15.369476 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.info, length: 85

To see the contents of the `syslog` file, use the `tcpdump -X` option:

    cumulus@leaf01:mgmt-vrf:~$ sudo tcpdump -i eth0 host 192.168.0.254 and udp port 514 -X -c 3
    tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
    listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
    00:59:15.980048 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.notice, length: 105
    0x0000: 4500 0085 33ee 4000 4011 8420 c0a8 000b E...3.@.@.......
    0x0010: c0a8 00fe 8453 0202 0071 9d18 3c38 353e .....S...q..<85>
    0x0020: 4465 6320 2039 2030 303a 3539 3a31 3520 Dec..9.00:59:15.
    0x0030: 6c65 6166 3031 2073 7564 6f3a 2020 6375 leaf01.sudo:..cu
    0x0040: 6d75 6c75 7320 3a20 5454 593d 7074 732f mulus.:.TTY=pts/
    0x0050: 3120 3b20 5057 443d 2f68 6f6d 652f 6375 1.;.PWD=/home/cu
    0x0060: 6d75 6c75 7320 3b20 5553 4552 3d72 6f6f mulus.;.USER=roo
    0x0070: 7420 3b20 434f 4d4d 414e 443d 2f62 696e t.;.COMMAND=/bin
    0x0080: 2f64 6174 65 /date

## <span>Next Steps</span>

The links below discuss more specific monitoring topics.
