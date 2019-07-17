---
title: Understanding the cl-support Output File
author: Cumulus Networks
weight: 2259
aliases:
 - /display/CL3740/Understanding-the-cl-support-Output-File
 - /pages/viewpage.action?pageId=83626006321
pageID: 83626006321
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
The `cl-support` script generates a compressed archive file of useful
information for troubleshooting. The system either creates the archive
file automatically or you can create the archive file manually.

The system creates the `cl-support` archive file automatically for the
following reasons:

  - When there is a [core file dump](http://linux.die.net/man/5/core) of
    any application (not specific to Cumulus Linux, but something all
    Linux distributions support), located in `/var/support/core`.

  - After the first failure of one of several monitored services since
    the switch was rebooted or power cycled.

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
    Directory](/version/cumulus-linux-37740/Monitoring-and-Troubleshooting/Understanding-the-cl-support-Output-File/Troubleshooting-the-etc-Directory)
    — In terms of the sheer number of files, `/etc` contains the largest
    number of files to send to Cumulus Networks. However, log files
    might be significantly larger in file size.

  - [Troubleshooting Log
    Files](/version/cumulus-linux-37740/Monitoring-and-Troubleshooting/Understanding-the-cl-support-Output-File/Troubleshooting-Log-Files)
    — This guide highlights the most important log files to inspect.
    Keep in mind, `cl-support` includes all of the log files.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTMyMDE1MDI0OF19
-->