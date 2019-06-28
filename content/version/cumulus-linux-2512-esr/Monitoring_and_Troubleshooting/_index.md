---
title: Monitoring and Troubleshooting
author: Cumulus Networks
weight: 23
aliases:
 - /display/CL25ESR/Monitoring+and+Troubleshooting
 - /pages/viewpage.action?pageId=5115962
pageID: 5115962
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
This chapter introduces monitoring and troubleshooting Cumulus Linux.

## <span>Commands</span>

  - cl-support

  - fw\_setenv

## <span>Using the Serial Console</span>

The serial console can be a useful tool for debugging issues, especially
when you find yourself rebooting the switch often or if you don’t have a
reliable network connection.

The default serial console baud rate is 115200, which is the baud rate
[ONIE](http://opencomputeproject.github.io/onie/) uses.

### <span>Configuring the Serial Console on PowerPC or ARM Switches</span>

On PowerPC switches, the U-Boot environment variable `baudrate`
identifies the baud rate of the serial console. To change the `baudrate`
variable, use the `fw_setenv` command:

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

## <span>Diagnostics Using cl-support</span>

You can use `cl-support` to generate a single export file that contains
various details and the configuration from a switch. This is useful for
remote debugging and troubleshooting.

You should run `cl-support` before you submit a support request to
Cumulus Networks as this file helps in the investigation of issues:

    cumulus@switch:~$ sudo cl-support -h
    Usage: cl-support [-h] [reason]...
    Args:
    [reason]: Optional reason to give for invoking cl-support.
             Saved into tarball's reason.txt file.
    Options:
    -h: Print this usage statement

Example output:

    cumulus@switch:~$ ls /var/support
    cl_support_20130806_032720.tar.xz

The directory structure is compressed using LZMA2 compression and can be
extracted using the `unxz` command:

    cumulus@switch:~$ cd /var/support
    cumulus@switch:~$ sudo unxz cl_support_20130729_140040.tar.xz
    cumulus@switch:~$ sudo tar xf cl_support_20130729_140040.tar
    cumulus@switch:~$ ls -l cl_support_20130729_140040/
    
    -rwxr-xr-x  1 root root 7724 Jul 29 14:00 cl-support
    -rw-r--r--  1 root root   52 Jul 29 14:00 cmdline.args
    drwxr-xr-x  2 root root 4096 Jul 29 14:00 core
    drwxr-xr-x 64 root root 4096 Jul 29 13:51 etc
    drwxr-xr-x  4 root root 4096 Jul 29 14:00 proc
    drwxr-xr-x  2 root root 4096 Jul 29 14:01 support
    drwxr-xr-x  3 root root 4096 Jul 29 14:00 sys
    drwxr-xr-x  3 root root 4096 Aug  8 15:22 var

The directory contains the following elements:

| Directory | Description                                                                                                                                                                                                                                                                                                                                                 |
| --------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| core      | Contains the core files generated from Cumulus Linux HAL process, `switchd`.                                                                                                                                                                                                                                                                                |
| etc       | Is a replica of the switch’s `/etc` directory. `/etc` contains all the general Linux configuration files, as well as configurations for the system’s network interfaces, `quagga`, `jdoo`, and other packages.                                                                                                                                              |
| log       | Is a replica of the switch's `/var/log` directory. Most Cumulus Linux log files are located in this directory. Notable log files include `switchd.log`, `daemon.log`, `quagga` log files, and `syslog`. For more information, read this [knowledge base article](https://support.cumulusnetworks.com/entries/24125147-Relevant-Log-Files-in-Cumulus-Linux). |
| proc      | Is a replica of the switch’s `/proc` directory. In Linux, `/proc` contains runtime system information (like system memory, devices mounted, and hardware configuration). These files are not actual files but the current state of the system.                                                                                                              |
| support   | Is a set of files containing further system information, which is obtained by `cl-support` running commands such as `ps -aux`, `netstat -i`, and so forth — even the routing tables.                                                                                                                                                                        |

`cl-support`, when untarred, contains a `reason.txt` file. This file
indicates what reason triggered it. When contacting Cumulus Networks
technical support, please attach the `cl-support` file if possible. For
more information about `cl-support`, read [Understanding and Decoding
the cl-support Output
File](/version/cumulus-linux-2512-esr/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/).

<span id="src-5115962_MonitoringandTroubleshooting-syslog_server"></span>

## <span>Sending Log Files to a syslog Server</span>

All logging on Cumulus Linux is done with
[rsyslog](http://www.rsyslog.com/). `rsyslog` provides both local
logging to the `syslog` file as well as the ability to export logs to an
external `syslog` server. High precision timestamps are enabled for all
`rsyslog` log files; here's an example:

    2015-08-14T18:21:43.337804+00:00 cumulus switchd[3629]: switchd.c:1409 switchd version 1.0-cl2.5+5

There are applications in Cumulus Linux that write directly to a log
file without going through `rsyslog`. These files are typically located
in `/var/log/`.

{{%notice note%}}

Starting with Cumulus Linux 2.5.4, all Cumulus Linux rules have been
moved from `/etc/rsyslog.conf` into separate files in `/etc/rsyslog.d/`,
which are called at the end of the `GLOBAL DIRECTIVES` section of
`/etc/rsyslog.conf`. As a result, the `RULES` section at the end of
`rsyslog.conf` is ignored because the messages have to be processed by
the rules in `/etc/rsyslog.d` and then dropped by the last line in
`/etc/rsyslog.d/99-syslog.conf`.

{{%/notice%}}

### <span>Local Logging</span>

Most logs within Cumulus Linux are sent through `rsyslog`, which then
writes them to files in the `/var/log` directory. There are default
rules in the `/etc/rsyslog.d/` directory that define where the logs are
written:

| Rule            | Purpose                                                                                                                                                                            |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 10-rules.conf   | Sets defaults for log messages, include log format and log rate limits.                                                                                                            |
| 15-crit.conf    | Logs crit, alert or emerg log messages to `/var/log/crit.log` to ensure they are not rotated away rapidly.                                                                         |
| 20-clagd.conf   | Logs `clagd` messages to `/var/log/clagd.log` for [MLAG](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Multi-Chassis_Link_Aggregation_-_MLAG).                      |
| 25-switchd.conf | Logs `switchd` messages to `/var/log/switchd.log`.                                                                                                                                 |
| 30-ptmd.conf    | Logs `ptmd` messages to `/var/log/ptmd.log` for [Prescription Topology Manager](/version/cumulus-linux-2512-esr/Layer_1_and_Layer_2_Features/Prescriptive_Topology_Manager_-_PTM). |
| 99-syslog.conf  | All remaining processes that use `rsyslog` are sent to `/var/log/syslog`.                                                                                                          |

Log files that are rotated are compressed into an archive. Processes
that do not use `rsyslog` write to their own log files within the
`/var/log` directory. For more information on specific log files, see
[Troubleshooting Log
Files](/version/cumulus-linux-2512-esr/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/Troubleshooting_Log_Files).

### <span>Enabling Remote syslog</span>

If you need to send other log files — such as `switchd` logs — to a
`syslog` server, do the following:

1.  Create a file in `/etc/rsyslog.d/`. Make sure it starts with a
    number lower than 99 so that it executes before log messages are
    dropped in, such as `20-clagd.conf` or `25-switchd.conf`. Our
    example file is called `/etc/rsyslog.d/11-remotesyslog.conf`. Add
    content similar to the following:
    
        ## Logging switchd messages to remote syslog server
        $ModLoad imfile
        $InputFileName /var/log/switchd.log
        $InputFileStateFile logfile-log
        $InputFileTag switchd:
        $InputFileSeverity info
        $InputFileFacility local7
        $InputFilePollInterval 5
        $InputRunFileMonitor
         
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
    
        cumulus@switch:~$ sudo rsyslog restart

In the above configuration, each setting is defined as follows:

| Setting                | Description                                                                                                                                                      |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| $ModLoad *imfile*      | Enables the `rsyslog` module to watch file contents.                                                                                                             |
| $InputFileName         | The file to be sent to the `syslog` server. In this example, you are going to send changes made to `/var/log/switchd.log` to the `syslog` server.                |
| $InputFileStateFile    | This is used by `rsyslog` to track state of the file being monitored. This must be unique for each file being monitored.                                         |
| $InputFileTag          | Defines the `syslog` tag that will precede the `syslog` messages. In this example, all logs are prefaced with *switchd*.                                         |
| $InputFileSeverity     | Defines the logging severity level sent to the `syslog` server.                                                                                                  |
| $InputFileFacility     | Defines the logging format. *local7* is common.                                                                                                                  |
| $InputFilePollInterval | Defines how frequently in seconds `rsyslog` looks for new information in the file. Lower values provide faster updates but create slightly more load on the CPU. |
| $InputRunFileMonitor   | Enables the file monitor module with the configured settings.                                                                                                    |

In most cases, the settings to customize include:

| Setting             | Description                                |
| ------------------- | ------------------------------------------ |
| $InputFileName      | The file to stream to the `syslog` server. |
| $InputFileStateFile | A unique name for each file being watched. |
| $InputFileTag       | A prefix to the log message on the server. |

## <span>Next Steps</span>

The links below discuss more specific monitoring topics.
