---
title: Monitoring Best Practices
author: Cumulus Networks
weight: 117
aliases:
 - /display/RMP321/Monitoring+Best+Practices
 - /pages/viewpage.action?pageId=5127589
pageID: 5127589
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
The following monitoring processes are considered best practices for
reviewing and troubleshooting potential issues with Cumulus RMP
environments. In addition, several of the more common issues have been
listed, with potential solutions included.

## <span>Overview</span>

This document aims to provide two sets of outputs:

1.  Metrics that can be polled from Cumulus RMP and used in trend
    analysis

2.  Critical log messages that can be monitored for triggered alerts

### <span>Trend Analysis via Metrics</span>

A metric is a quantifiable measure that is used to track and assess the
status of a specific infrastructure component. It is a check collected
over time. Examples of metrics include bytes on an interface, CPU
utilization and total number of routes.

Metrics are more valuable when used for trend analysis.

### <span>Alerting via Triggered Logging</span>

Triggered issues are normally sent to syslog, but could go to another
log file depending on the feature. On Cumulus RMP, `rsyslog` handles all
logging including local and remote logging. Logs are the best method to
use for generating alerts when the system transitions from a stable
steady state.

Sending logs to a centralized collector, then creating an alerts based
on critical logs is optimal solution for alerting.

## <span>Hardware</span>

The `smond` process provides monitoring functionality for various switch
hardware elements. Mininmum/maximum values are output, depending on the
flags applied to the basic command. The hardware elements and applicable
commands/flags are listed in the table below:

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
<td><p>600 seconds</p></td>
</tr>
<tr class="even">
<td><p>Fan</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s FAN[X]</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
<tr class="odd">
<td><p>PSU</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s PSU[X]</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
<tr class="even">
<td><p>PSU Fan</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s PSU[X]Fan[X]</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
<tr class="odd">
<td><p>PSU Temperature</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s PSU[X]Temp[X]</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
<tr class="even">
<td><p>Voltage</p></td>
<td><pre><code>cumulus@switch:~$ smonctl -j
cumulus@switch:~$ smonctl -j -s Volt[X]</code></pre></td>
<td><p>600 seconds</p></td>
</tr>
<tr class="odd">
<td><p>Front Panel LED</p></td>
<td><pre><code>cumulus@switch:~$ ledmgrd -d
cumulus@switch:~$ ledmgrd -j</code></pre></td>
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
<th><p>Hardware Logs</p></th>
<th><p>Log Location</p></th>
<th><p>Log Entries</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>High temperature</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>/usr/sbin/smond : : Temp2(Near the CPU (Right)): Temperature(51 C) is HIGH for last 71240 secs
/usr/sbin/smond : : Temp3(Top right corner): Temperature(43 C) is HIGH for last 71240 secs
/usr/sbin/smond : : Temp4:  Avg state is CRITICAL for last 60 secs. Last 10 values: [85.0, 85.5, 86.125, 86.625, 87.0, 87.625, 88.0, 88.625, 88.875, 89.25]. Generating cl-support and shutting down system...</code></pre></td>
</tr>
<tr class="even">
<td><p>Fan speed issues</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>/usr/sbin/smond : : Fan5(Fan Tray 3): state changed from OK to HIGH
/usr/sbin/smond : : Fan5(Fan Tray 3): Fan speed 28912 RPM greater than 19000 RPM
/usr/sbin/smond : : Fan5(Fan Tray 3): state changed from HIGH to OK
...
/usr/sbin/smond : : Fan1: state changed from OK to ABSENT
/usr/sbin/smond : : Fan1:  Fan speed is at 0 RPM (not working or absent)</code></pre></td>
</tr>
<tr class="odd">
<td><p>PSU failure</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre><code>/usr/sbin/smond : : PSU1: state changed from UNKNOWN to BAD</code></pre></td>
</tr>
</tbody>
</table>

## <span>System Data</span>

Cumulus RMP includes a number of ways to monitor various aspects of
system data. In addition, alerts are issued in high risk situations.

### <span>CPU Idle Time</span>

When a CPU reports five high CPU alerts within a span of 5 minutes, an
alert is logged.

{{%notice warning%}}

**Short High CPU Bursts**

Short bursts of high CPU can occur during switchd churn or routing
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
<td><pre class="p1"><code>sysmonitor: High CPU use: 91%
sysmonitor: CPU use no longer high: 58%</code></pre>
<pre><code>sysmonitor: Critically high load average: 1.31 (1.31)
sysmonitor: High load average: 1.24 (1.24)
sysmonitor: Load Average no longer high: 0.88 (0.88)</code></pre></td>
</tr>
</tbody>
</table>

Cumulus RMP 3.0 and later monitors CPU, memory and disk space via
`sysmonitor`. The configurations for the thresholds are stored in
`/etc/cumulus/sysmonitor.conf`. More information is available via `man
sysmonitor`.

| CPU measure  | Thresholds            |
| ------------ | --------------------- |
| Use          | Alert: 90% Crit: 95%  |
| Process Load | Alarm: 95% Crit: 125% |

Click here to see differences between Cumulus RMP 2.5 ESR and 3.0 and
later...

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
<td><pre><code>jdoo[2803]: &#39;localhost&#39; cpu system usage of 41.1% matches resource limit [cpu system usage&gt;30.0%]</code></pre>
<pre><code>jdoo[4727]: &#39;localhost&#39; sysloadavg(15min) of 111.0 matches resource limit [sysloadavg(15min)&gt;110.0]</code></pre></td>
</tr>
</tbody>
</table>

In Cumulus RMP 2.5, CPU logs are created with each unique threshold:

| CPU measure | \< 2.5 Threshold |
| ----------- | ---------------- |
| User        | 70%              |
| System      | 30%              |
| Wait        | 20%              |

Cumulus RMP 2.5, CPU and Memory warnings are generated via jdoo. The
configuration for the thresholds are stored in
**/etc/jdoo/jdoorc.d/cl-utilities.rc**.

### <span>Memory Usage</span>

When the memory utilization exceeds 90% a warning is logged and a
cl-support is generated.

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
<td><p>Memory utilization</p></td>
<td><pre><code>cumulus@switch:~$ cat     
/proc/meminfo     
cumulus@switch:~$ cat     
/usr/bin/free    </code></pre></td>
<td><p>30 seconds</p></td>
</tr>
</tbody>
</table>

### <span>Disk Usage</span>

<span style="color: #000000;"> When monitoring disk utilization
**tmpfs** can be excluded from monitoring. </span>

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

## <span>Process Restart </span>

In Cumulus RMP 3.0 and later, systemd is responsible for monitoring and
restarting processes.

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
<td><p>View processes monitored by systemd</p></td>
<td><pre><code>cumulus@switch:~$     
systemctl status    </code></pre></td>
</tr>
</tbody>
</table>

Click here to changes from Cumulus Linux 2.5 ESR to 3.0 and later...

Cumulus RMP 2.5.4 through 2.5 ESR uses a forked version of monit called
jdoo to monitor processes. If the process ever fails, jdoo then invokes
init.d to restart the process.

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

## <span>Layer 1 Protocols and Interfaces</span>

<span style="color: #000000;"> Link and port state interface transitions
are logged to **/var/log/syslog** and **/var/log/switchd.log**. </span>

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
<td><pre><code>    
cumulus@switch:~$ cat /sys/class/net/[iface]/operstate     

cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
<tr class="even">
<td><p>Link speed</p></td>
<td><pre><code>    
cumulus@switch:~$ cat /sys/class/net/[iface]/speed     

cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
<tr class="odd">
<td><p>Port state</p></td>
<td><pre><code>cumulus@switch:~$     
ip link show
    
cumulus@switch:~$ net show interface all json</code></pre></td>
</tr>
<tr class="even">
<td><p>Bond state</p></td>
<td><pre><code>cumulus@switch:~$     
cat /proc/net/bonding/[bond]
    
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
<td><pre><code>    
cumulus@switch:~$ cat /sys/class/net/[iface]/statistics/[stat_name]    

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
...
switchd[5692]: nic.c:213 nic_set_carrier: swp1: setting kernel carrier: up
switchd[5692]: netlink.c:291 libnl: swp17, family 0, ifi 20, oper up</code></pre></td>
</tr>
<tr class="even">
<td><p>Unidirectional link</p></td>
<td><pre><code>/var/log/switchd.log
/var/log/ptm.log</code></pre></td>
<td><pre><code>ptmd[7146]: ptm_bfd.c:2471 Created new session 0x1 with peer 10.255.255.11 port swp1
ptmd[7146]: ptm_bfd.c:2471 Created new session 0x2 with peer fe80::4638:39ff:fe00:5b port swp1
...
ptmd[7146]: ptm_bfd.c:2471 Session 0x1 down to peer 10.255.255.11, Reason 8
ptmd[7146]: ptm_bfd.c:2471 Detect timeout on session 0x1 with peer 10.255.255.11, in state 1</code></pre></td>
</tr>
<tr class="odd">
<td><p>Bond Negotiation</p>
<ul>
<li><p>Working</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre class="p1"><code>kernel: [73946.052292] bonding: Bond1 is being created...
kernel: [73946.062957] Bond1: Enslaving swp49 as a backup interface with an up link
kernel: [73946.081609] Bond1: Enslaving swp50 as a backup interface with an up link
kernel: [73946.090636] IPv6: ADDRCONF(NETDEV_UP): Bond1: link is not ready
kernel: [74590.925353] IPv6: ADDRCONF(NETDEV_CHANGE): Bond1: link becomes ready</code></pre></td>
</tr>
<tr class="even">
<td><p>Bond Negotiation</p>
<ul>
<li><p>Failing</p></li>
</ul></td>
<td><pre><code>/var/log/syslog</code></pre></td>
<td><pre class="p1"><code>kernel: [73946.052292] bonding: Bond1 is being created...
kernel: [73946.062957] Bond1: Enslaving swp49 as a backup interface with an up link
kernel: [73946.081609] Bond1: Enslaving swp50 as a backup interface with an up link
kernel: [73946.090636] IPv6: ADDRCONF(NETDEV_UP): Bond1: link is not ready </code></pre></td>
</tr>
</tbody>
</table>

Prescriptive Topology Manager (PTM) uses LLDP information to compare
against a topology.dot file that describes the network. It has built in
alerting capabilities, so it is preferable to use PTM on box rather than
polling LLDP information regularly. The PTM code is available on the
Cumulus Networks [github
repository](https://github.com/CumulusNetworks/ptm). Additional PTM, BFD
and associated logs are documented in the code.

{{%notice note%}}

Peering information should be tracked through PTM. For more information,
refer to the <span style="color: #000000;"> [Prescriptive Topology
Manager
documentation](/display/RMP321/Prescriptive+Topology+Manager+-+PTM).
</span>

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

## <span>Layer 2 Protocols</span>

Spanning tree is a protocol that prevents loops in a layer 2
infrastructure. In a stable state, the spanning tree protocol should
stably converge. Monitoring the Topology Change Notifications (TCN) in
STP helps identify when new BPDUs were received.

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

## <span>Layer 3 Protocols</span>

Routing Logs

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
<td><pre><code>watchquagga[3044]: bgpd state -&gt; down : read returned EOF
cumulus-core: Running cl-support for core files bgpd.3030.1470341944.core.core_helper
core_check.sh[4992]: Please send /var/support/cl_support__spine01_20160804_201905.tar.xz to Cumulus support.
watchquagga[5241]: Forked background command [pid 6665]: /usr/sbin/service quagga restart bgpd
watchquagga[7719]: watchquagga 0.99.24+cl3u2 watching [zebra bgpd ospfd], mode [phased zebra restart]
watchquagga[7719]: zebra state -&gt; up : connect succeeded
watchquagga[7719]: bgpd state -&gt; up : connect succeeded
watchquagga[7719]: ospfd state -&gt; up : connect succeeded</code></pre></td>
</tr>
</tbody>
</table>

## <span>Logging</span>

The table below covers the various log files, and what they should be
used for:

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th><p>OSPF Element</p></th>
<th><p>Monitoring Command/s</p></th>
<th><p>Log Location</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Syslog</p></td>
<td><p>Catch all log file. Identifies memory leaks and CPU spikes.</p></td>
<td><pre><code>/var/log/syslog</code></pre></td>
</tr>
<tr class="even">
<td><p>Switchd functionality</p></td>
<td><p>Hardware Abstraction Layer (HAL).</p></td>
<td><pre><code>/var/log/switchd.log</code></pre></td>
</tr>
</tbody>
</table>

## <span>Protocols and Services</span>

### <span>NTP</span>

Run the following command to confirm the NTP process is working
correctly, and that the switch clock is synced with NTP:

    cumulus@switch:~$ /usr/bin/ntpq -p

## <span>Device Management</span>

### <span>Device Access Logs</span>

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
<td><pre class="p1"><code>sshd[31830]: Accepted publickey for cumulus from 192.168.0.254 port 45582 ssh2: RSA 38:e6:3b:cc:04:ac:41:5e:c9:e3:93:9d:cc:9e:48:25
sshd[31830]: pam_unix(sshd:session): session opened for user cumulus by (uid=0)</code></pre></td>
</tr>
</tbody>
</table>

### <span>Device Super User Command Logs</span>

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
<td><pre class="p1"><code>sudo:  cumulus : TTY=pts/2 ; PWD=/home/cumulus ; USER=root ; COMMAND=/bin/uname -a
sudo: pam_unix(sudo:session): session opened for user root by cumulus(uid=0)
sudo: pam_unix(sudo:session): session closed for user root</code></pre></td>
</tr>
</tbody>
</table>

<span style="color: #000000;">  
</span>
