---
title: Monitoring and Troubleshooting
author: Cumulus Networks
weight: 21
aliases:
 - /display/RMP25ESR/Monitoring+and+Troubleshooting
 - /pages/viewpage.action?pageId=5116323
pageID: 5116323
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
This chapter introduces monitoring and troubleshooting Cumulus RMP.

## <span>Commands</span>

  - cl-support

  - fw\_setenv

## <span>Using the Serial Console</span>

The serial console can be a useful tool for debugging issues, especially
when you find yourself rebooting the switch often or if you don’t have a
reliable network connection.

The default serial console baud rate is 115200, which is the baud rate
[ONIE](http://opencomputeproject.github.io/onie/) uses.

### <span>Configuring the Serial Console on PowerPC Switches</span>

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
`grub`. The valid values for the baud rate are:

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
    line and in the console variable in the second line:
    
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
| core      | Contains the core files generated from Cumulus RMP HAL process, `switchd.`                                                                                                                                                                                                                                                                         |
| etc       | Is a replica of the switch’s `/etc` directory. `/etc` contains all the general Linux configuration files, as well as configurations for the system’s network interfaces, `jdoo`, and other packages.                                                                                                                                               |
| log       | Is a replica of the switch’s `/var/log` directory. Most Cumulus RMP log files are located in this directory. Notable log files include `switchd.log` and `daemon.log` log files, and `syslog`. For more information, read this [knowledge base article](https://support.cumulusnetworks.com/entries/24125147-Relevant-Log-Files-in-Cumulus-Linux). |
| proc      | Is a replica of the switch’s `/proc` directory. In Linux, `/proc` contains runtime system information (like system memory, devices mounted, and hardware configuration). These files are not actual files but the current state of the system.                                                                                                     |
| support   | Is a set of files containing further system information, which is obtained by `cl-support` running commands such as `ps -aux`, `netstat -i`, and so forth — even the routing tables.                                                                                                                                                               |

`cl-support`, when untarred, contains a `reason.txt` file. This file
indicates what reason triggered it. When contacting Cumulus Networks
technical support, please attach the `cl-support` file if possible. For
more information about `cl-support`, please read [Understanding and
Decoding the cl-support Output
File](/version/cumulus-rmp-2512-esr/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/)
.

## <span>Configuration Files</span>

  - /etc/cumulus/switchd.conf

## <span>Next Steps</span>

The links listed under Child Pages below discuss more specific
monitoring topics.
