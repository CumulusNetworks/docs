---
title: Troubleshooting Log Files
author: Cumulus Networks
weight: 175
aliases:
 - /display/RMP30/Troubleshooting+Log+Files
 - /pages/viewpage.action?pageId=5118697
pageID: 5118697
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
The only real unique entity for logging on Cumulus RMP compared to any
other Linux distribution is `switchd.log`, which logs the HAL (hardware
abstraction layer) from hardware like the Broadcom ASIC.

[This guide on
NixCraft](http://www.cyberciti.biz/faq/linux-log-files-location-and-how-do-i-view-logs-files/)
is amazing for understanding how `/var/log` works. The green highlighted
rows below are the most important logs and usually looked at first when
debugging.

<table>
<thead>
<tr class="header">
<th><p>Log</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>/var/log/alternatives.log <span style="color: #111111;"> </span></p></td>
<td><p><span style="color: #111111;"> Information from the update-alternatives are logged into this log file. </span></p></td>
</tr>
<tr class="even">
<td><p>/var/log/apt</p></td>
<td><p>Information the <code>apt</code> utility can send logs here; for example, from <code>apt-get install</code> and <code>apt-get remove</code>.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/audit/</p></td>
<td><p><span style="color: #111111;"> Contains log information stored by the Linux audit daemon, <code>auditd</code>. </span></p></td>
</tr>
<tr class="even">
<td><p>/var/log/auth.log</p></td>
<td><p>Authentication logs.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/boot.log</p></td>
<td><p><span style="color: #111111;"> Contains information that is logged when the system boots. </span></p></td>
</tr>
<tr class="even">
<td><p>/var/log/btmp</p></td>
<td><p><span style="color: #111111;"> This file contains information about failed login attempts. Use the <code>last</code> command to view the <code>btmp</code> file. For example: </span></p>
<pre><code>    
last -f /var/log/btmp | more    </code></pre></td>
</tr>
<tr class="odd">
<td><p>/var/log/daemon.log</p></td>
<td><p><span style="color: #111111;"> Contains information logged by the various background daemons that run on the system. </span></p></td>
</tr>
<tr class="even">
<td><p>/var/log/dmesg</p></td>
<td><p>Contains kernel ring buffer information. When the system boots up, it prints number of messages on the screen that display information about the hardware devices that the kernel detects during boot process. These messages are available in the kernel ring buffer and whenever a new message arrives, the old message gets overwritten. You can also view the content of this file using the <code>dmesg</code> command.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/dpkg.log</p></td>
<td><p>Contains information that is logged when a package is installed or removed using the <code>dpkg</code> command.</p></td>
</tr>
<tr class="even">
<td><p>/var/log/faillog</p></td>
<td><p><span style="color: #111111;"> Contains failed user login attempts. Use the <code>faillog</code> command to display the contents of this file. </span></p></td>
</tr>
<tr class="odd">
<td><p>/var/log/fsck/*</p></td>
<td><p>The <code>fsck</code> utility <span style="color: #000000;"> is used to check and optionally repair one or more Linux filesystems. </span></p></td>
</tr>
<tr class="even">
<td><p>/var/log/mail.log</p></td>
<td><p>Mail server logs.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/messages</p></td>
<td><p>General messages and system related information.</p></td>
</tr>
<tr class="even">
<td><p>/var/log/monit.log</p></td>
<td><p><code>monit</code> is a utility for managing and monitoring processes, files, directories and filesystems on a Unix system.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/news/*</p></td>
<td><p>The <code>news</code> command keeps you informed of news concerning the system.</p></td>
</tr>
<tr class="even">
<td><p>/var/log/ntpstats</p></td>
<td><p>Logs for network configuration protocol.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/kern.log</p></td>
<td><p>Kernel logs.</p></td>
</tr>
<tr class="even">
<td><p>/var/log/switchd.log/</p></td>
<td><p>The HAL log for Cumulus RMP.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/syslog</p></td>
<td><p>The main system log, which logs everything except auth-related messages.</p></td>
</tr>
<tr class="even">
<td><p>/var/log/wtmp</p></td>
<td><p>Login records file.</p></td>
</tr>
<tr class="odd">
<td><p>/var/log/yum.log</p></td>
<td><p><code>apt</code> command log file.</p></td>
</tr>
</tbody>
</table>
