---
title: Understanding and Decoding the cl-support Output File
author: Cumulus Networks
weight: 109
aliases:
 - /display/RMP321/Understanding+and+Decoding+the+cl-support+Output+File
 - /pages/viewpage.action?pageId=5127566
pageID: 5127566
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
The `cl-support` command generates a tar archive of useful information
for troubleshooting that can be auto-generated or manually created. To
manually create it, run the `cl-support` command. The `cl-support` file
is automatically generated when:

  - There is a [core file dump](http://linux.die.net/man/5/core) of any
    application (not specific to Cumulus RMP, but something all Linux
    distributions support)

  - Memory usage surpasses 90% of the total system memory (memory usage
    \> 90% for 1 cycle)

  - The [loadavg](http://linux.die.net/man/5/proc) over 15 minutes has
    on average greater than 2 (loadavg (15min) \> 2)

The Cumulus Networks support team may request you submit the output from
`cl-support` to help with the investigation of issues you might
experience with Cumulus RMP.

    cumulus@switch:~$ sudo cl-support -h
    Usage: cl-support [-h] [reason]...
    Args:
    [reason]: Optional reason to give for invoking cl-support.
             Saved into tarball's reason.txt file.
    Options:
    -h: Print this usage statement
     
    Example output:
    cumulus@switch:~$ ls /var/support
    cl_support__switch_20141204_203833

This chapter covers ...

## <span>Understanding the File Naming Scheme </span>

The `cl-support` command generates a file under `/var/support` with the
following naming scheme. The following example describes the file called
`cl_support__switch_20141204_203833.tar.xz`.

| cl\_support                                      | switch                                                              | 20141204                                                          | 203833                                                                                                   |
| ------------------------------------------------ | ------------------------------------------------------------------- | ----------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- |
| This is always prepended to the `tar.gz` output. | This is the hostname of the switch where `cl-support` was executed. | The date in year, month, day; so 20141204 is December, 4th, 2014. | The time in hours, minutes, seconds; so 203833 is 20, 38, 33 (20:38:33) or the equivalent to 8:38:33 PM. |

## <span>Decoding the Output</span>

Decoding a `cl_support` file is a simple process performed using the
`tar` **command. The following example illustrates extracting the
`cl_support` file:

    $ tar -xf cl_support__switch_20141204_203834.tar.xz

The `-xf` options are defined here:

| Option | Description                                |
| ------ | ------------------------------------------ |
| \-x    | Extracts to disk from the archive.         |
| \-f    | Reads the archive from the specified file. |

    cumulus@switch:~$ ls -l cl_support__switch_20141204_203834/
     
    -rwxr-xr-x  1 root root 7724 Jul 29 14:00 cl-support
    -rw-r--r--  1 root root   52 Jul 29 14:00 cmdline.args
    drwxr-xr-x  2 root root 4096 Jul 29 14:00 core
    drwxr-xr-x 64 root root 4096 Jul 29 13:51 etc
    drwxr-xr-x  4 root root 4096 Jul 29 14:00 proc
    drwxr-xr-x  2 root root 4096 Jul 29 14:01 support
    drwxr-xr-x  3 root root 4096 Jul 29 14:00 sys
    drwxr-xr-x  3 root root 4096 Aug  8 15:22 var

The `cl_support` file, when untarred, contains a `reason.txt` file. This
file indicates what reason triggered the event. When contacting Cumulus
Networks technical support, please attach the `cl-support` file if
possible.

The directory contains the following elements:

| Directory  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ---------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cl-support | This is a copy of the `cl-support` script that generated the `cl_support` file. It is copied so Cumulus Networks knows exactly which files were included and which weren't. This helps to fix future `cl-support` requests in the future.                                                                                                                                                                                                                                                                                                                                                                                               |
| core       | Contains the core files generated from the Cumulus RMP HAL (hardware abstraction layer) process, `switchd`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| etc        | `etc` is the core system configuration directory. `cl-support` replicates the switch’s `/etc` directory. `/etc` contains all the general Linux configuration files, as well as configurations for the system’s network interfaces, `quagga`, `monit`, and other packages.                                                                                                                                                                                                                                                                                                                                                               |
| var/log    | `/var` is the "variable" subdirectory, where programs record runtime information. System logging, user tracking, caches and other files that system programs create and monitor go into `/var`. `cl-support` includes only the `log` subdirectory of the `var` system-level directory and replicates the switch’s `/var/log` directory. Most Cumulus RMP log files are located in this directory. Notable log files include `switchd.log` and `daemon.log` log files, and `syslog`. For more information, read this [knowledge base article](https://support.cumulusnetworks.com/entries/24125147-Relevant-Log-Files-in-Cumulus-Linux). |
| proc       | `proc` (short for processes) provides system statistics through a directory-and-file interface. In Linux, `/proc` contains runtime system information (like system memory, devices mounted, and hardware configuration). `cl-support` simply replicates the switch’s `/proc` directory to determine the current state of the system.                                                                                                                                                                                                                                                                                                    |
| support    | `support` is **not** a replica of the Linux file system like the other folders listed above. Instead, it is a set of files containing the output of commands from the command line. Examples include the output of `ps -aux`, `netstat -i`, and so forth — even the routing tables are included.                                                                                                                                                                                                                                                                                                                                        |

Here is more information on the file structure:

  - [Troubleshooting the etc
    Directory](/version/cumulus-rmp-321/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/Troubleshooting_the_etc_Directory)
    — In terms of sheer numbers of files, `/etc` contains the largest
    number of files to send to Cumulus Networks by far. However, log
    files could be significantly larger in file size.

  - [Troubleshooting Log
    Files](/version/cumulus-rmp-321/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/Troubleshooting_Log_Files)
    — This guide highlights the most important log files to look at.
    Keep in mind, `cl-support` includes all of the log files.

  - [Troubleshooting the support
    Directory](/version/cumulus-rmp-321/Monitoring_and_Troubleshooting/Understanding_and_Decoding_the_cl-support_Output_File/Troubleshooting_the_support_Directory)
    — This is an explanation of the `support` directory included in the
    `cl-support` output.
