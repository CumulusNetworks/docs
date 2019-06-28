---
title: Understanding the cl-support Output File
author: Cumulus Networks
weight: 199
aliases:
 - /display/CL321/Understanding+the+cl-support+Output+File
 - /pages/viewpage.action?pageId=5126784
pageID: 5126784
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
The `cl-support` command generates an archive of useful information for
troubleshooting that can be auto-generated or manually created. To
manually create it, run the `cl-support` command. The `cl-support` file
is automatically generated when:

  - There is a [core file dump](http://linux.die.net/man/5/core) of any
    application (not specific to Cumulus Linux, but something all Linux
    distributions support), located in `/var/support/core`

  - After the first failure of one of the following monitored services
    since the switch was rebooted or power cycled:
    
      - clagd
    
      - openvswitch-vtep
    
      - portwd
    
      - ptmd
    
      - quagga
    
      - rdnbrd
    
      - switchd
    
      - vxrd
    
      - vxsnd

The Cumulus Networks support team may request you submit the output from
`cl-support` to help with the investigation of issues you might
experience with Cumulus Linux.

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

You can find information on the directories included in the `cl-support`
file:

  - [Troubleshooting the etc
    Directory](/version/cumulus-linux-321/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_the_etc_Directory)
    — In terms of sheer numbers of files, `/etc` contains the largest
    number of files to send to Cumulus Networks by far. However, log
    files could be significantly larger in file size.

  - [Troubleshooting Log
    Files](/version/cumulus-linux-321/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_Log_Files)
    — This guide highlights the most important log files to look at.
    Keep in mind, `cl-support` includes all of the log files.
