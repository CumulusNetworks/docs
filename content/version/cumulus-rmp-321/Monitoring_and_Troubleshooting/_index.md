---
title: Monitoring and Troubleshooting
author: Cumulus Networks
weight: 21
aliases:
 - /display/RMP321/Monitoring+and+Troubleshooting
 - /pages/viewpage.action?pageId=5127557
pageID: 5127557
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
This chapter introduces monitoring and troubleshooting Cumulus RMP.

## <span>Using the Serial Console</span>

The serial console can be a useful tool for debugging issues, especially
when you find yourself rebooting the switch often or if you don’t have a
reliable network connection.

The default serial console baud rate is 115200, which is the baud rate
[ONIE](http://opencomputeproject.github.io/onie/) uses.

### <span>Configuring the Serial Console</span>

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
    DISTRIB_ID="Cumulus Linux"
    DISTRIB_RELEASE=3.2.1
    DISTRIB_DESCRIPTION="Cumulus Linux 3.2.1"

For general information about the switch, run `net show system`:

    cumulus@switch:~$ net show system
    Cumulus Version 3.2.1
    Build: Cumulus Linux 3.2.1
    Uptime: 6 days, 1:00:52

## <span>Diagnostics Using cl-support</span>

You can use `cl-support` to generate a single export file that contains
various details and the configuration from a switch. This is useful for
remote debugging and troubleshooting.

You should run `cl-support` before you submit a support request to
Cumulus Networks as this file helps in the investigation of issues:

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

| Directory | Description                                                                                                                                                                                                                                                                                                                                        |
| --------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| core      | Contains the core files on the switch, including those generated from `switchd`.                                                                                                                                                                                                                                                                   |
| etc       | Is a replica of the switch’s `/etc` directory. `/etc` contains all the general Linux configuration files, as well as configurations for the system’s network interfaces and other packages.                                                                                                                                                        |
| log       | Is a replica of the switch’s `/var/log` directory. Most Cumulus RMP log files are located in this directory. Notable log files include `switchd.log` and `daemon.log` log files, and `syslog`. For more information, read this [knowledge base article](https://support.cumulusnetworks.com/entries/24125147-Relevant-Log-Files-in-Cumulus-Linux). |
| proc      | Is a replica of the switch’s `/proc` directory. In Linux, `/proc` contains runtime system information (like system memory, devices mounted, and hardware configuration). These files are not actual files but the current state of the system.                                                                                                     |
| support   | Is a set of files containing further system information, which is obtained by `cl-support` running commands such as `ps -aux`, `netstat -i`, and so forth — even the routing tables.                                                                                                                                                               |

`cl-support`, when untarred, contains a `cmdline.args` file. This file
indicates what reason triggered it. When contacting Cumulus Networks
technical support, please attach the `cl-support` file if possible. For
more information about `cl-support`, please read [Understanding and
Decoding the cl-support Output
File](/version/cumulus-rmp-321/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/).

{{%notice note%}}

If you have issues extracting the script with the `tar` command, like an
error saying the file does not look like tar archive, try using the
`unxz` command first:

    cumulus@switch:~$ sudo unxz cl_support_20130729_140040.tar.xz

You can save a lot of disk space and perhaps some time if you do not run
`unxz` on the tar file.

{{%/notice%}}

## <span id="src-5127557_MonitoringandTroubleshooting-syslog_server" class="confluence-anchor-link"></span><span>Sending Log Files to a syslog Server</span>

All logging on Cumulus RMP is done with
[rsyslog](http://www.rsyslog.com/). `rsyslog` provides both local
logging to the `syslog` file as well as the ability to export logs to an
external `syslog` server. High precision timestamps are enabled for all
`rsyslog` log files; here's an example:

    2015-08-14T18:21:43.337804+00:00 cumulus switchd[3629]: 
     switchd.c:1409 switchd version 1.0-cl2.5+5

**Local logging:** Most logs within Cumulus RMP are sent to files in the
`/var/log` directory. Most relevant information is placed within the
`/var/log/syslog` file. For more information on specific log files, see
[Troubleshooting Log Files](/display/RMP321/Troubleshooting+Log+Files).

**Export logging:** To send `syslog` files to an external `syslog`
server, add a rule specifying to copy all messages (\*.\*) to the IP
address and switch port of your `syslog` server in the `rsyslog`
configuration files as described below.

In the following example, *192.168.1.2* is the remote `syslog` server
and *514* is the port number. For UDP-based syslog, use a single @
before the IP address: *@192.168.1.2:514*. For TCP-based syslog, use two
@@ before the IP address: *@@192.168.1.2:514*.

1.  Create a file called something like
    `/etc/rsyslog.d/90-remotesyslog.conf`. Make sure it starts with a
    number lower than 99 so that it executes before `99-syslog.conf`.
    Add content like the following:
    
        ## Copy all messages to the remote syslog server at 192.168.1.2 port 514
        *.*                             @192.168.1.2:514

2.  Restart `rsyslog`.
    
        cumulus@switch:~$ sudo systemctl restart rsyslog.service

{{%notice note%}}

All Cumulus RMP rules are stored in separate files in `/etc/rsyslog.d/`,
which are called at the end of the `GLOBAL DIRECTIVES` section of
`/etc/rsyslog.conf`. As a result, the `RULES` section at the end of
`rsyslog.conf` is ignored because the messages have to be processed by
the rules in `/etc/rsyslog.d` and then dropped by the last line in
`/etc/rsyslog.d/99-syslog.conf`.

{{%/notice%}}

{{%notice note%}}

In the case of the `switchd` rules file, the file must be numbered lower
than 25. For example, `13-switchd-remote.conf`.

{{%/notice%}}

If you need to send other log files (e.g. switchd logs) to a `syslog`
server, configure a new file in `/etc/rsyslog.d`, as described above,
and add lines similar to the following lines:

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

Then restart `syslog`:

    cumulus@switch:~$ sudo systemctl restart rsyslog.service

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

Finally, the `if $programname` line is what sends the log files to the
`syslog` server. It follows the same syntax as the `/var/log/syslog`
file, where *@* indicates UDP, *192.168.1.2* is the IP address of the
`syslog` server, and *514* is the UDP port. The value *switchd* must
match the value in `$InputFileTag`.

## <span>Next Steps</span>

The links listed below discuss more specific monitoring topics.
