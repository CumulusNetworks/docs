---
title: Understanding the cl-support Output File
author: Cumulus Networks
weight: 213
aliases:
 - /display/CL35/Understanding+the+cl-support+Output+File
 - /pages/viewpage.action?pageId=8357382
pageID: 8357382
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
The `cl-support` script generates a compressed archive file of useful
information for troubleshooting. The system either creates the archive
file automatically or you can create the archive file manually.

The system creates the `cl-support` archive file automatically for the
following reasons:

  - When there is a [core file dump](http://linux.die.net/man/5/core) of
    any application (not specific to Cumulus Linux, but something all
    Linux distributions support), located in `/var/support/core`

  - After the first failure of one of the following monitored services
    since the switch was rebooted or power cycled:
    
      - clagd
    
      - frr
    
      - openvswitch-vtep
    
      - portwd
    
      - ptmd
    
      - rdnbrd
    
      - switchd
    
      - vxrd
    
      - vxsnd

When the system creates the `cl-support` archive automatically due to a
failure, the archive contains a file called `Control` that provides the
reason why the script was executed. For example:

    Reason: switchd first heartbeat miss

To create the `cl-support` archive file manually, run the `cl-support`
command:

    cumulus@switch:~$ sudo cl-support

If the Cumulus Networks support team requests that you submit the output
from `cl-support` to help with the investigation of issues you might
experience with Cumulus Linux and you need to include security-sensitive
information, such as the `sudoers` file, use the `-s` option:

    cumulus@switch:~$ sudo cl-support -s

For information on the directories included in the `cl-support` archive,
see:

  - [Troubleshooting the etc
    Directory](/version/cumulus-linux-35/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_the_etc_Directory)
    — In terms of the sheer number of files, `/etc` contains the largest
    number of files to send to Cumulus Networks. However, log files
    might be significantly larger in file size.

  - [Troubleshooting Log
    Files](/version/cumulus-linux-35/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_Log_Files)
    — This guide highlights the most important log files to inspect.
    Keep in mind, `cl-support` includes all of the log files.
