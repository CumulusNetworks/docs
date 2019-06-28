---
title: Understanding the cl-support Output File
author: Cumulus Networks
weight: 215
aliases:
 - /display/CL332/Understanding+the+cl-support+Output+File
 - /pages/viewpage.action?pageId=5868918
pageID: 5868918
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
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
experience with Cumulus Linux. If you need to includes
security-sensitive information, such as the `sudoers` file, use the `-s`
option:

    cumulus@switch:~$ sudo cl-support -s

You can find information on the directories included in the `cl-support`
file:

  - [Troubleshooting the etc
    Directory](/version/cumulus-linux-332/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_the_etc_Directory)
    — In terms of sheer numbers of files, `/etc` contains the largest
    number of files to send to Cumulus Networks by far. However, log
    files could be significantly larger in file size.

  - [Troubleshooting Log
    Files](/version/cumulus-linux-332/Monitoring_and_Troubleshooting/Understanding_the_cl-support_Output_File/Troubleshooting_Log_Files)
    — This guide highlights the most important log files to look at.
    Keep in mind, `cl-support` includes all of the log files.
