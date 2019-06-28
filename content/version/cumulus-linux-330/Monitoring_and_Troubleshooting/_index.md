---
title: Monitoring and Troubleshooting
author: Cumulus Networks
weight: 25
aliases:
 - /display/CL330/Monitoring+and+Troubleshooting
 - /pages/viewpage.action?pageId=5866129
pageID: 5866129
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
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
    DISTRIB_RELEASE=3.3.0~1493169975.9482755
    DISTRIB_DESCRIPTION="Cumulus Linux 3.3.0~1493169975.9482755"

For general information about the switch, run `net show system`, which
gathers information about the switch from a number of files in the
system:

    cumulus@switch:~$ net show system
     
    Penguin Arctica 4806XP
    Cumulus Version 3.3.0~1493169975.9482755
    Build: Cumulus Linux 3.3.0~1493169975.9482755
     
     
    Chipset: Broadcom Trident2 BCM56854
     
     
    Port Config: 48 x 10G-SFP+ & 6 x 40G-QSFP+
     
     
    CPU: (x86_64) Intel Atom C2558 2.40GHz
     
     
    Uptime: 4 days, 20:53:49

## <span>Diagnostics Using cl-support</span>

You can use `cl-support` to generate a single export file that contains
various details and the configuration from a switch. This is useful for
remote debugging and troubleshooting. For more information about
`cl-support`, read [Understanding the cl-support Output
File](/version/cumulus-linux-330/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/).

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

## <span id="src-5866129_MonitoringandTroubleshooting-syslog_server" class="confluence-anchor-link"></span><span>Sending Log Files to a syslog Server</span>

Logging on Cumulus Linux is done with
[rsyslog](http://www.rsyslog.com/). `rsyslog` provides both local
logging to the `syslog` file as well as the ability to export logs to an
external `syslog` server. High precision timestamps are enabled for all
`rsyslog` log files; here's an example:

    2015-08-14T18:21:43.337804+00:00 cumulus switchd[3629]: switchd.c:1409 switchd version 1.0-cl2.5+5

There are applications in Cumulus Linux that write directly to a log
file without going through `rsyslog`. These files are typically located
in `/var/log/`.

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

| Rule            | Purpose                                                                                                                                                            |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| 10-rules.conf   | Sets defaults for log messages, include log format and log rate limits.                                                                                            |
| 15-crit.conf    | Logs crit, alert or emerg log messages to `/var/log/crit.log` to ensure they are not rotated away rapidly.                                                         |
| 20-clagd.conf   | Logs `clagd` messages to `/var/log/clagd.log` for [MLAG](/version/cumulus-linux-330/Layer_One_and_Two/Multi-Chassis_Link_Aggregation_-_MLAG).                      |
| 25-switchd.conf | Logs `switchd` messages to `/var/log/switchd.log`.                                                                                                                 |
| 30-ptmd.conf    | Logs `ptmd` messages to `/var/log/ptmd.log` for [Prescription Topology Manager](/version/cumulus-linux-330/Layer_One_and_Two/Prescriptive_Topology_Manager_-_PTM). |
| 35-rdnbrd.conf  | Logs `rdnbrd` messages to `/var/log/rdnbrd.log` for [redistribute neighbor](/version/cumulus-linux-330/Layer_Three/Redistribute_Neighbor).                         |
| 40-netd.conf    | Logs `netd` messages to `/var/log/netd.log` for [NCLU](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility).                              |
| 99-syslog.conf  | All remaining processes that use `rsyslog` are sent to `/var/log/syslog`.                                                                                          |

Log files that are rotated are compressed into an archive. Processes
that do not use `rsyslog` write to their own log files within the
`/var/log` directory. For more information on specific log files, see
[Troubleshooting Log
Files](/version/cumulus-linux-330/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_Log_Files).

### <span>Enabling Remote syslog</span>

If you need to send other log files — such as `switchd` logs — to a
`syslog` server, do the following:

1.  Create a file in `/etc/rsyslog.d/`. Make sure it starts with a
    number lower than 99 so that it executes before log messages are
    dropped in, such as `20-clagd.conf` or `25-switchd.conf`. Our
    example file is called `/etc/rsyslog.d/11-remotesyslog.conf`. Add
    content similar to the following:
    
        ## Logging switchd messages to remote syslog server
         
         
        if $programname == 'switchd' then @192.168.1.2:514
    
    This configuration sends log messages to a remote `syslog` server
    for the following processes: `clagd`, `switchd`, `ptmd`, `rdnbrd`,
    `netd` and `syslog`. The `if $programname` line sends the log files
    to the `syslog` server. It follows the same syntax as the
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

2.  Restart `rsyslog`.
    
        cumulus@switch:~$ sudo systemctl restart rsyslog.service

### <span>Writing to syslog with Management VRF Enabled</span>

You can write to syslog with [management
VRF](/version/cumulus-linux-330/Layer_Three/Management_VRF) enabled by
applying the following configuration; this configuration is commented
out in the `/etc/rsyslog.d/99-syslog.conf` file:

    ## Copy all messages to the remote syslog server at 192.168.1.2 port 514
    action(type="omfwd" Target="192.168.1.2" Device="mgmt" Port="514" Protocol="udp")

### <span>Advanced Logging</span>

All Cumulus applications included in Cumulus Linux log via `rsyslog`.
There are some third party applications bypass `rsyslog` and log to a
file directly. This section demonstrates how you can configure Cumulus
Linux to read in from a flat log file and pass it through the `rsyslog`
filter engine by using the `imfile` module.

{{%notice warning%}}

Never use the `imfile` module to read files that are written by
`rsyslog`, as it can cause loops when reading and writing to the same
log file.

{{%/notice%}}

Configuring advanced logging ...

Create a file and add content similar to the following:

    module(load="imfile")
     
    input(type="imfile"
          stateFile="quagga-state"
          File="/var/log/EXAMPLE.log"
          Severity="Warning"
          Tag="EXAMPLE-log:"
          Facility="local7")
     
    if $syslogtag contains "EXAMPLE-log" then action(type="omfwd" Target="192.168.1.2" Port="514" Protocol="udp")

{{%notice tip%}}

You can find more information in the [rsyslog
documentation](http://www.rsyslog.com/doc/v8-stable/configuration/modules/imfile.html).

{{%/notice%}}

Then restart `syslog`:

    cumulus@switch:~$ sudo systemctl restart rsyslog.service

In the above configuration, each setting is defined as follows:

| Setting   | Description                                                                                                                                               |
| --------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| load      | Loads the `rsyslog` module to watch file contents.                                                                                                        |
| File      | The file to be sent through the `rsyslog` rules engine. In the above example, any changes made are sent to `/var/log/switchd.log` to the `syslog` server. |
| stateFile | `rsyslog` uses this to track the state of the file being monitored. This must be unique for each file being monitored.                                    |
| Tag       | Defines the `syslog` tag that precedes the `syslog` messages. In this example, all logs are prefaced with *quagga-log*.                                   |
| Severity  | Defines the logging severity level sent to the `syslog` server.                                                                                           |
| Facility  | Defines the logging format. *local7* is common.                                                                                                           |

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

## <span>Next Steps</span>

The links below discuss more specific monitoring topics.
