---
title: Monitoring Best Practices
author: Cumulus Networks
weight: 233
aliases:
 - /display/DOCS/Monitoring+Best+Practices
 - /pages/viewpage.action?pageId=8362625
pageID: 8362625
product: Cumulus Linux
version: 3.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The following monitoring processes are considered best practices for
reviewing and troubleshooting potential issues with Cumulus Linux
environments. In addition, several of the more common issues have been
listed, with potential solutions included.

## Overview

This document describes:

  - Metrics that you can poll from Cumulus Linux and use in trend
    analysis

  - Critical log messages that you can monitor for triggered alerts

### Trend Analysis Using Metrics

A metric is a quantifiable measure that is used to track and assess the
status of a specific infrastructure component. It is a check collected
over time. Examples of metrics include bytes on an interface, CPU
utilization, and total number of routes.

Metrics are more valuable when used for trend analysis.

### Generate Alerts with Triggered Logging

Triggered issues are normally sent to `syslog`, but can go to another
log file depending on the feature. In Cumulus Linux, `rsyslog` handles
all logging, including local and remote logging. Logs are the best
method to use for generating alerts when the system transitions from a
stable steady state.

Sending logs to a centralized collector, then creating alerts based on
critical logs is an optimal solution for alerting.

### Log Formatting

Most log files in Cumulus Linux use a standard presentation format. For
example, consider this `syslog` entry:

    2017-03-08T06:26:43.569681+00:00 leaf01 sysmonitor: Critically high CPU use: 99%

  - *2017-03-08T06:26:43.569681+00:00* is the timestamp.

  - *leaf01* is the hostname.

  - *sysmonitor* is the process that is the source of the message.

  - *Critically high CPU use: 99%* is the message.

For brevity and legibility, the timestamp and hostname have been omitted
from the examples in this chapter.

## Hardware

The `smond` process provides monitoring functionality for various switch
hardware elements. Minimum or maximum values are output depending on the
flags applied to the basic command. The hardware elements and applicable
commands and flags are listed in the table below.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Hardware Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Temperature</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s TEMP[X]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
<tr class="even">
<td><p>Fan</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s FAN[X]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
<tr class="odd">
<td><p>PSU</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s PSU[X]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
<tr class="even">
<td><p>PSU Fan</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s PSU[X]Fan[X]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
<tr class="odd">
<td><p>PSU Temperature</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s PSU[X]Temp[X]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
<tr class="even">
<td><p>Voltage</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s Volt[X]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
<tr class="odd">
<td><p>Front Panel LED</p></td>
<td><pre><code>cumulus@switch:~$ ledmgrd -d
cumulus@switch:~$ ledmgrd -j</code></pre></td>
<td><p>5 seconds</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

Not all switch models include a sensor for monitoring power consumption
and voltage. See
[this note](../Monitoring-System-Hardware/#monitor-system-units-using-smond)
for details.

{{%/notice%}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Hardware Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>High temperature</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>/usr/sbin/smond : : Temp1(Board Sensor near CPU): state changed from UNKNOWN to OK
/usr/sbin/smond : : Temp2(Board Sensor Near Virtual Switch): state changed from UNKNOWN to OK
/usr/sbin/smond : : Temp3(Board Sensor at Front Left Corner): state changed from UNKNOWN to OK
/usr/sbin/smond : : Temp4(Board Sensor at Front Right Corner): state changed from UNKNOWN to OK
/usr/sbin/smond : : Temp5(Board Sensor near Fan): state changed from UNKNOWN to OK</code></pre></td>
</tr>
<tr class="even">
<td><p>Fan speed issues</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>/usr/sbin/smond : : Fan1(Fan Tray 1, Fan 1): state changed from UNKNOWN to OK
/usr/sbin/smond : : Fan2(Fan Tray 1, Fan 2): state changed from UNKNOWN to OK
/usr/sbin/smond : : Fan3(Fan Tray 2, Fan 1): state changed from UNKNOWN to OK
/usr/sbin/smond : : Fan4(Fan Tray 2, Fan 2): state changed from UNKNOWN to OK
/usr/sbin/smond : : Fan5(Fan Tray 3, Fan 1): state changed from UNKNOWN to OK
/usr/sbin/smond : : Fan6(Fan Tray 3, Fan 2): state changed from UNKNOWN to OK</code></pre></td>
</tr>
<tr class="odd">
<td><p>PSU failure</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>/usr/sbin/smond : : PSU1Fan1(PSU1 Fan): state changed from UNKNOWN to OK
/usr/sbin/smond : : PSU2Fan1(PSU2 Fan): state changed from UNKNOWN to BAD</code></pre></td>
</tr>
</tbody>
</table>

## System Data

Cumulus Linux includes a number of ways to monitor various aspects of
system data. In addition, alerts are issued in high risk situations.

### CPU Idle Time

When a CPU reports five high CPU alerts within a span of five minutes,
an alert is logged.

{{%notice warning%}}

**Short High CPU Bursts**

Short bursts of high CPU can occur during `switchd` churn or routing
protocol startup. Do not set alerts for these short bursts.

{{%/notice%}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>System Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>CPU utilization</p></td>
<td><pre><code>cumulus@switch:~$ cat /proc/stat
cumulus@switch:~$ top -b -n 1</code></pre></td>
<td><p>30 seconds</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CPU Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>High CPU</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>sysmonitor: Critically high CPU use: 99%
systemd[1]: Starting Monitor system resources (cpu, memory, disk)...
systemd[1]: Started Monitor system resources (cpu, memory, disk).
sysmonitor: High CPU use: 89%
systemd[1]: Starting Monitor system resources (cpu, memory, disk)...
systemd[1]: Started Monitor system resources (cpu, memory, disk).
sysmonitor: CPU use no longer high: 77%</code></pre></td>
</tr>
</tbody>
</table>

Cumulus Linux 3.0 and later monitors CPU, memory, and disk space via
`sysmonitor`. The configurations for the thresholds are stored in
`/etc/cumulus/sysmonitor.conf`. More information is available with `man
sysmonitor`.

| CPU measure  | Thresholds            |
| ------------ | --------------------- |
| Use          | Alert: 90% Crit: 95%  |
| Process Load | Alarm: 95% Crit: 125% |
<details>
<summary>Click here to see differences between Cumulus Linux 2.5 ESR and
3.0 and later... </summary>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>CPU Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>High CPU</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>jdoo[2803]: &#39;localhost&#39; cpu system usage of 41.1% matches resource limit [cpu system usage&gt;30.0%]
jdoo[4727]: &#39;localhost&#39; sysloadavg(15min) of 111.0 matches resource limit [sysloadavg(15min)&gt;110.0]</code></pre></td>
</tr>
</tbody>
</table>
</details>
In Cumulus Linux 2.5, CPU logs are created with each unique threshold:

| CPU measure | \< 2.5 Threshold |
| ----------- | ---------------- |
| User        | 70%              |
| System      | 30%              |
| Wait        | 20%              |

In Cumulus Linux 2.5, CPU and memory warnings are generated with `jdoo`.
The configuration for the thresholds is stored in
`/etc/jdoo/jdoorc.d/cl-utilities.rc`.

### Disk Usage

When monitoring disk utilization, you can exclude `tmpfs` from
monitoring.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>System Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Disk utilization</p></td>
<td><pre><code>cumulus@switch:~$ /bin/df -x tmpfs</code></pre></td>
<td><p>300 seconds</p></td>
</tr>
</tbody>
</table>

## Process Restart

In Cumulus Linux 3.0 and later, `systemd` is responsible for monitoring
and restarting processes.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Process Element</p></th>
<th><p>Monitoring Command/s</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>View processes monitored by <code>systemd</code></p></td>
<td><pre><code>cumulus@switch:~$ systemctl status</code></pre></td>
</tr>
</tbody>
</table>
<details>
<summary>Click here to changes from Cumulus Linux 2.5 ESR to 3.0 and
later... </summary>

Cumulus Linux 2.5.2 through 2.5 ESR uses a forked version of `monit`
called `jdoo` to monitor processes. If the process fails, `jdoo` invokes
`init.d` to restart the process.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Process Element</p></th>
<th><p>Monitoring Command/s</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>View processes monitored by jdoo</p></td>
<td><pre><code>cumulus@switch:~$ jdoo summary</code></pre></td>
</tr>
<tr class="even">
<td><p>View process restarts</p></td>
<td><pre><code>cumulus@switch:~$ sudo cat /var/log/syslog</code></pre></td>
</tr>
<tr class="odd">
<td><p>View current process state</p></td>
<td><pre><code>cumulus@switch:~$ ps -aux</code></pre></td>
</tr>
</tbody>
</table>
</details>
## Layer 1 Protocols and Interfaces

Link and port state interface transitions are logged to
`/var/log/syslog` and `/var/log/switchd.log`.

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Interface Element</p></th>
<th><p>Monitoring Command/s</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Link state</p></td>
<td><pre><code>cumulus@switch:~$ cat /sys/class/net/[iface]/operstate          
cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
<tr class="even">
<td><p>Link speed</p></td>
<td><pre><code>cumulus@switch:~$ cat /sys/class/net/[iface]/speed           
cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
<tr class="odd">
<td><p>Port state</p></td>
<td><pre><code>cumulus@switch:~$ ip link show
cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
<tr class="even">
<td><p>Bond state</p></td>
<td><pre><code>cumulus@switch:~$ cat /proc/net/bonding/[bond]
cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
</tbody>
</table>

Interface counters are obtained from either querying the hardware or the
Linux kernel. The two outputs should align, but the Linux kernel
aggregates the output from the hardware.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Interface Counter Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Interface counters</p></td>
<td><pre><code>cumulus@switch:~$ cat /sys/class/net/[iface]/statistics/[stat_name]
cumulus@switch:~$ net show counters json
cumulus@switch:~$ cl-netstat -j
cumulus@switch:~$ ethtool -S [iface]</code></pre></td>
<td><p>10 seconds</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Layer 1 Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Link failure/Link flap</p></td>
<td><pre><code>/var/log/switchd.log</code></pre></td>
<td><pre><code>switchd[5692]: nic.c:213 nic_set_carrier: swp17: setting kernel carrier: down
switchd[5692]: netlink.c:291 libnl: swp1, family 0, ifi 20, oper down
switchd[5692]: nic.c:213 nic_set_carrier: swp1: setting kernel carrier: up
switchd[5692]: netlink.c:291 libnl: swp17, family 0, ifi 20, oper up</code></pre></td>
</tr>
<tr class="even">
<td><p>Unidirectional link</p></td>
<td><pre><code>/var/log/switchd.log
/var/log/ptm.log</code></pre></td>
<td><pre><code>ptmd[7146]: ptm_bfd.c:2471 Created new session 0x1 with peer 10.255.255.11 port swp1
ptmd[7146]: ptm_bfd.c:2471 Created new session 0x2 with peer fe80::4638:39ff:fe00:5b port swp1
ptmd[7146]: ptm_bfd.c:2471 Session 0x1 down to peer 10.255.255.11, Reason 8
ptmd[7146]: ptm_bfd.c:2471 Detect timeout on session 0x1 with peer 10.255.255.11, in state 1</code></pre></td>
</tr>
<tr class="odd">
<td><p>Bond Negotiation</p>
<ul>
<li><p>Working</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>kernel: [85412.763193] bonding: bond0 is being created...
kernel: [85412.770014] bond0: Enslaving swp2 as a backup interface with an up link
kernel: [85412.775216] bond0: Enslaving swp1 as a backup interface with an up link
kernel: [85412.797393] IPv6: ADDRCONF(NETDEV_UP): bond0: link is not ready
kernel: [85412.799425] IPv6: ADDRCONF(NETDEV_CHANGE): bond0: link becomes ready</code></pre></td>
</tr>
<tr class="even">
<td><p>Bond Negotiation</p>
<ul>
<li><p>Failing</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>kernel: [85412.763193] bonding: bond0 is being created...
kernel: [85412.770014] bond0: Enslaving swp2 as a backup interface with an up link
kernel: [85412.775216] bond0: Enslaving swp1 as a backup interface with an up link
kernel: [85412.797393] IPv6: ADDRCONF(NETDEV_UP): bond0: link is not ready</code></pre></td>
</tr>
<tr class="odd">
<td><p>MLAG peerlink negotiation</p>
<ul>
<li><p>Working</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>lldpd[998]: error while receiving frame on swp50: Network is down
lldpd[998]: error while receiving frame on swp49: Network is down
kernel: [76174.262893] peerlink: Setting ad_actor_system to 44:38:39:00:00:11
kernel: [76174.264205] 8021q: adding VLAN 0 to HW filter on device peerlink
mstpd: one_clag_cmd: setting (1) peer link: peerlink
mstpd: one_clag_cmd: setting (1) clag state: up
mstpd: one_clag_cmd: setting system-mac 44:38:39:ff:40:94
mstpd: one_clag_cmd: setting clag-role secondary</code></pre></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><pre><code>/var/log/clagd.log</code></pre></td>
<td><pre><code>clagd[14003]: Cleanup is executing.
clagd[14003]: Cannot open file &quot;/tmp/pre-clagd.q7XiO
clagd[14003]: Cleanup is finished
clagd[14003]: Beginning execution of clagd version 1
clagd[14003]: Invoked with: /usr/sbin/clagd --daemon
clagd[14003]: Role is now secondary
clagd[14003]: HealthCheck: role via backup is second
clagd[14003]: HealthCheck: backup active
clagd[14003]: Initial config loaded
clagd[14003]: The peer switch is active.
clagd[14003]: Initial data sync from peer done.
clagd[14003]: Initial handshake done.
clagd[14003]: Initial data sync to peer done.</code></pre></td>
</tr>
<tr class="odd">
<td><p>MLAG peerlink negotiation</p>
<ul>
<li><p>Failing</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>lldpd[998]: error while receiving frame on swp50: Network is down
lldpd[998]: error while receiving frame on swp49: Network is down
kernel: [76174.262893] peerlink: Setting ad_actor_system to 44:38:39:00:00:11
kernel: [76174.264205] 8021q: adding VLAN 0 to HW filter on device peerlink
mstpd: one_clag_cmd: setting (1) peer link: peerlink
mstpd: one_clag_cmd: setting (1) clag state: down
mstpd: one_clag_cmd: setting system-mac 44:38:39:ff:40:94
mstpd: one_clag_cmd: setting clag-role secondary</code></pre></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><pre><code>/var/log/clagd.log</code></pre></td>
<td><pre><code>clagd[26916]: Cleanup is executing.
clagd[26916]: Cannot open file &quot;/tmp/pre-clagd.6M527vvGX0/brbatch&quot; for reading: No such file or directory
clagd[26916]: Cleanup is finished
clagd[26916]: Beginning execution of clagd version 1.3.0
clagd[26916]: Invoked with: /usr/sbin/clagd --daemon 169.254.1.2 peerlink.4094 44:38:39:FF:01:01 --priority 1000 --backupIp 10.0.0.2
clagd[26916]: Role is now secondary
clagd[26916]: Initial config loaded</code></pre></td>
</tr>
<tr class="odd">
<td><p>MLAG port negotiation</p>
<ul>
<li><p>Working</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>kernel: [77419.112195] bonding: server01 is being created...
lldpd[998]: error while receiving frame on swp1: Network is down
kernel: [77419.122707] 8021q: adding VLAN 0 to HW filter on device swp1
kernel: [77419.126408] server01: Enslaving swp1 as a backup interface with a down link
kernel: [77419.177175] server01: Setting ad_actor_system to 44:38:39:ff:40:94
kernel: [77419.190874] server01: Warning: No 802.3ad response from the link partner for any adapters in the bond
kernel: [77419.191448] IPv6: ADDRCONF(NETDEV_UP): server01: link is not ready
kernel: [77419.191452] 8021q: adding VLAN 0 to HW filter on device server01
kernel: [77419.192060] server01: link status definitely up for interface swp1, 1000 Mbps full duplex
kernel: [77419.192065] server01: now running without any active interface!
kernel: [77421.491811] IPv6: ADDRCONF(NETDEV_CHANGE): server01: link becomes ready
mstpd: one_clag_cmd: setting (1) mac 44:38:39:00:00:17 &lt;server01, None&gt;</code></pre></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><pre><code>/var/log/clagd.log</code></pre></td>
<td><pre><code>clagd[14003]: server01 is now dual connected.</code></pre></td>
</tr>
<tr class="odd">
<td><p>MLAG port negotiation</p>
<ul>
<li><p>Failing</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>kernel: [79290.290999] bonding: server01 is being created...
kernel: [79290.299645] 8021q: adding VLAN 0 to HW filter on device swp1
kernel: [79290.301790] server01: Enslaving swp1 as a backup interface with a down link
kernel: [79290.358294] server01: Setting ad_actor_system to 44:38:39:ff:40:94
kernel: [79290.373590] server01: Warning: No 802.3ad response from the link partner for any adapters in the bond
kernel: [79290.374024] IPv6: ADDRCONF(NETDEV_UP): server01: link is not ready
kernel: [79290.374028] 8021q: adding VLAN 0 to HW filter on device server01
kernel: [79290.375033] server01: link status definitely up for interface swp1, 1000 Mbps full duplex
kernel: [79290.375037] server01: now running without any active interface!</code></pre></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><pre><code>/var/log/clagd.log</code></pre></td>
<td><pre><code>clagd[14291]: Conflict (server01): matching clag-id (1) not configured on peer
...
clagd[14291]: Conflict cleared (server01): matching clag-id (1) detected on peer </code></pre></td>
</tr>
<tr class="odd">
<td><p>MLAG port negotiation</p>
<ul>
<li><p>Flapping</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>mstpd: one_clag_cmd: setting (0) mac 00:00:00:00:00:00 &lt;server01, None&gt;
mstpd: one_clag_cmd: setting (1) mac 44:38:39:00:00:03 &lt;server01, None&gt;</code></pre></td>
</tr>
<tr class="even">
<td><p> </p></td>
<td><pre><code>/var/log/clagd.log</code></pre></td>
<td><pre><code>clagd[14291]: server01 is no longer dual connected
clagd[14291]: server01 is now dual connected.</code></pre></td>
</tr>
</tbody>
</table>

Prescriptive Topology Manager (PTM) uses LLDP information to compare
against a `topology.dot` file that describes the network. It has built
in alerting capabilities, so it is preferable to use PTM on box rather
than polling LLDP information regularly. The PTM code is available on
the Cumulus Networks [GitHub
repository](https://github.com/CumulusNetworks/ptm). Additional PTM,
BFD, and associated logs are documented in the code.

{{%notice note%}}

Cumulus Networks recommends that you track peering information through
PTM. For more information, refer to the [Prescriptive Topology Manager
documentation](../../Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM).

{{%/notice%}}

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Neighbor Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>LLDP Neighbor</p></td>
<td><pre><code>cumulus@switch:~$ lldpctl -f json</code></pre></td>
<td><p>300 seconds</p></td>
</tr>
<tr class="even">
<td><p>Prescriptive Topology Manager</p></td>
<td><pre><code>cumulus@switch:~$ ptmctl -j [-d]</code></pre></td>
<td><p>Triggered</p></td>
</tr>
</tbody>
</table>

## Layer 2 Protocols

Spanning tree is a protocol that prevents loops in a layer 2
infrastructure. In a stable state, the spanning tree protocol should
stably converge. Monitoring the Topology Change Notifications (TCN) in
STP helps identify when new BPDUs are received.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Interface Counter Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>STP TCN Transitions</p></td>
<td><pre><code>cumulus@switch:~$ mstpctl showbridge json
cumulus@switch:~$ mstpctl showport json</code></pre></td>
<td><p>60 seconds</p></td>
</tr>
<tr class="even">
<td><p>MLAG peer state</p></td>
<td><pre><code>cumulus@switch:~$ clagctl status
cumulus@switch:~$ clagd -j
cumulus@switch:~$ cat /var/log/clagd.log</code></pre></td>
<td><p>60 seconds</p></td>
</tr>
<tr class="odd">
<td><p>MLAG peer MACs</p></td>
<td><pre><code>cumulus@switch:~$ clagctl dumppeermacs
cumulus@switch:~$ clagctl dumpourmacs </code></pre></td>
<td><p>300 seconds</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Layer 2 Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Spanning Tree Working</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>kernel: [1653877.190724] device swp1 entered promiscuous mode
kernel: [1653877.190796] device swp2 entered promiscuous mode
mstpd: create_br: Add bridge bridge
mstpd: clag_set_sys_mac_br: set bridge mac 00:00:00:00:00:00
mstpd: create_if: Add iface swp1 as port#2 to bridge bridge
mstpd: set_if_up: Port swp1 : up
mstpd: create_if: Add iface swp2 as port#1 to bridge bridge
mstpd: set_if_up: Port swp2 : up
mstpd: set_br_up: Set bridge bridge up
mstpd: MSTP_OUT_set_state: bridge:swp1:0 entering blocking state(Disabled)
mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering blocking state(Disabled)
mstpd: MSTP_OUT_flush_all_fids: bridge:swp1:0 Flushing forwarding database
mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database
mstpd: MSTP_OUT_set_state: bridge:swp1:0 entering learning state(Designated)
mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering learning state(Designated)
sudo: pam_unix(sudo:session): session closed for user root
mstpd: MSTP_OUT_set_state: bridge:swp1:0 entering forwarding state(Designated)
mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering forwarding state(Designated)
mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database
mstpd: MSTP_OUT_flush_all_fids: bridge:swp1:0 Flushing forwarding database</code></pre></td>
</tr>
<tr class="even">
<td><p>Spanning Tree Blocking</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering blocking state(Designated)
mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering learning state(Designated)
mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering forwarding state(Designated)
mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database
mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database
mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering blocking state(Alternate)
mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database</code></pre></td>
</tr>
</tbody>
</table>

## Layer 3 Protocols

When FRRouting boots up for the first time, there is a different log
file for each daemon that is activated. If the log file is ever edited
(for example, through `vtysh` or `frr.conf`), the integrated
configuration sends all logs to the same file.

To send FRRouting logs to syslog, apply the configuration `log syslog`
in `vtysh`.

### BGP

When monitoring BGP, check if BGP peers are operational. There is not
much value in alerting on the current operational state of the peer;
monitoring the transition is more valuable, which you can do by
monitoring `syslog`.

Monitoring the routing table provides trending on the size of the
infrastructure. This is especially useful when integrated with
host-based solutions (such as Routing on the Host) when the routes track
with the number of applications available.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>BGP Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BGP peer failure</p></td>
<td><pre><code>cumulus@switch:~$ vtysh -c &quot;show ip bgp summary json&quot;
cumulus@switch:~$ cl-bgp summary show json</code></pre></td>
<td><p>60 seconds</p></td>
</tr>
<tr class="even">
<td><p>BGP route table</p></td>
<td><pre><code>cumulus@switch:~$ vtysh -c &quot;show ip bgp json&quot;
cumulus@switch:~$ cl-bgp route show</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>BGP Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>BGP peer down</p></td>
<td><pre><code>/var/log/syslog
/var/log/frr/*.log </code></pre></td>
<td><pre><code>bgpd[3000]: %NOTIFICATION: sent to neighbor swp1 4/0 (Hold Timer Expired) 0 bytes
bgpd[3000]: %ADJCHANGE: neighbor swp1 Down BGP Notification send</code></pre></td>
</tr>
</tbody>
</table>

### OSPF

When monitoring OSPF, check if OSPF peers are operational. There is not
much value in alerting on the current operational state of the peer;
monitoring the transition is more valuable, which you can do by
monitoring `syslog`.

Monitoring the routing table provides trending on the size of the
infrastructure. This is especially useful when integrated with
host-based solutions (such as Routing on the Host) when the routes track
with the number of applications available.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OSPF Element</p></th>
<th><p>Monitoring Command(s)</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>OSPF protocol peer failure</p></td>
<td><pre><code>cumulus@switch:~$ vtysh -c &quot;show ip ospf neighbor all json&quot;
cumulus@switch:~$ cl-ospf summary show json</code></pre></td>
<td><p>60 seconds</p></td>
</tr>
<tr class="even">
<td><p>OSPF link state database</p></td>
<td><pre><code>cumulus@switch:~$ vtysh - c &quot;show ip ospf database&quot;</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
</tbody>
</table>

### Route and Host Entries

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Route Element</p></th>
<th><p>Monitoring Command(s)</p></th>
<th><p>Interval Poll</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Host Entries</p></td>
<td><pre><code>cumulus@switch:~$ cl-resource-query
cumulus@switch:~$ cl-resource-query -k</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
<tr class="even">
<td><p>Route Entries</p></td>
<td><pre><code>cumulus@switch:~$ cl-resource-query
cumulus@switch:~$ cl-resource-query -k</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
</tbody>
</table>

### Routing Logs

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Layer 3 Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Routing protocol process crash</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>frrouting[1824]: Starting FRRouting daemons (prio:10):. zebra. bgpd.
bgpd[1847]: BGPd 1.0.0+cl3u7 starting: vty@2605, bgp@&lt;all&gt;:179
zebra[1840]: client 12 says hello and bids fair to announce only bgp routes
watchfrr[1853]: watchfrr 1.0.0+cl3u7 watching [zebra bgpd], mode [phased zebra restart]
watchfrr[1853]: bgpd state -&gt; up : connect succeeded
watchfrr[1853]: bgpd state -&gt; down : read returned EOF
cumulus-core: Running cl-support for core files bgpd.3030.1470341944.core.core_helper
core_check.sh[4992]: Please send /var/support/cl_support__spine01_20160804_201905.tar.xz to Cumulus support
watchfrr[1853]: Forked background command [pid 6665]: /usr/sbin/service frr restart bgpd
watchfrr[1853]: watchfrr 0.99.24+cl3u2 watching [zebra bgpd ospfd], mode [phased zebra restart]
watchfrr[1853]: zebra state -&gt; up : connect succeeded
watchfrr[1853]: bgpd state -&gt; up : connect succeeded
watchfrr[1853]: watchfrr: Notifying Systemd we are up and running</code></pre></td>
</tr>
</tbody>
</table>

## Logging

The table below describes the various log files.

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Logging Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Log Location</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>syslog</p></td>
<td><p>Catch all log file. Identifies memory leaks and CPU spikes.</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
</tr>
<tr class="even">
<td><p>switchd functionality</p></td>
<td><p>Hardware Abstraction Layer (HAL).</p></td>
<td><pre><code>/var/log/switchd.log</code></pre></td>
</tr>
<tr class="odd">
<td><p>Routing daemons</p></td>
<td><p>FRRouting zebra daemon details.</p></td>
<td><pre><code>/var/log/daemon.log</code></pre></td>
</tr>
<tr class="even">
<td><p>Routing protocol</p></td>
<td><p>The log file is configurable in FRRouting. When FRRouting first boots, it uses the non-integrated configuration so each routing protocol has its own log file. After booting up, FRRouting switches over to using the integrated configuration, so that all logs go to a single place.</p>
<p>To edit the location of the log files, use the <code>log file &lt;location&gt; </code>command. By default, FRRouting logs are not sent to <code>syslog</code>. Use the <code>log syslog &lt;level&gt;</code> command to send logs through <code>rsyslog</code> and into <code>/var/log/syslog</code>.</p>
<p>{{%notice note%}}</p>
<p>To write syslog debug messages to the log file, you must run the <code>log syslog debug</code> command to configure FRR with syslog severity 7 (debug); otherwise, when you issue a debug command such as, <code>debug bgp neighbor-events</code>, no output is sent to <code>/var/log/frr/frr.log</code>.<br />
However, when you manually define a log target with the <code>log file /var/log/frr/debug.log</code> command, FRR automatically defaults to severity 7 (debug) logging and the output is logged to <code>/var/log/frr/frr.log</code>.</p>
<p>{{%/notice%}}</p></td>
<td><pre><code>/var/log/frr/zebra.log
/var/log/frr/{protocol}.log
/var/log/frr/frr.log</code></pre></td>
</tr>
</tbody>
</table>

## Protocols and Services

Run the following command to confirm that the NTP process is working
correctly and that the switch clock is in sync with NTP:

    cumulus@switch:~$ /usr/bin/ntpq -p

## Device Management

### Device Access Logs

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Access Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>User Authentication and Remote Login</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>sshd[31830]: Accepted publickey for cumulus from 192.168.0.254 port 45582 ssh2: RSA 38:e6:3b:cc:04:ac:41:5e:c9:e3:93:9d:cc:9e:48:25
sshd[31830]: pam_unix(sshd:session): session opened for user cumulus by (uid=0)</code></pre></td>
</tr>
</tbody>
</table>

### Device Super User Command Logs

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Super User Command Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Executing commands using sudo</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>sudo:  cumulus : TTY=unknown ; PWD=/home/cumulus ; USER=root ; COMMAND=/tmp/script_9938.sh -v
sudo: pam_unix(sudo:session): session opened for user root by (uid=0)
sudo: pam_unix(sudo:session): session closed for user root</code></pre></td>
</tr>
</tbody>
</table>
