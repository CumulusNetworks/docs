---
title: Monitoring Best Practices
author: NVIDIA
weight: 1240
toc: 3
---
The following monitoring processes are best practices for reviewing and troubleshooting potential issues with Cumulus Linux environments.

This document describes:

- Metrics that you can poll from Cumulus Linux and use in trend analysis
- Critical log messages that you can monitor for triggered alerts

## Trend Analysis Using Metrics

A metric is a quantifiable measure that tracks and assesses the status of a specific infrastructure component. Examples of metrics include bytes on an interface, CPU utilization, and total number of routes.

Metrics are more valuable when you use them for trend analysis.

## Generate Alerts with Triggered Logging

Cumulus Linux typically sends triggered issues to `syslog`, but can send issues to another log file depending on the feature. `rsyslog` handles all logging, including local and remote logging. Logs are the best method to use for generating alerts when the system transitions from a stable steady state.

Sending logs to a centralized collector, then creating alerts that you base on critical logs is an optimal solution.

## Log Formatting

Most log files in Cumulus Linux use a standard presentation format. For example:

```
2017-03-08T06:26:43.569681+00:00 leaf01 sysmonitor: Critically high CPU use: 99%
```

- *2017-03-08T06:26:43.569681+00:00* is the timestamp.
- *leaf01* is the hostname.
- *sysmonitor* is the process that is the source of the message.
- *Critically high CPU use: 99%* is the message.

For brevity and legibility, this section omits the timestamp and hostname from examples.

## Hardware

The `smond` process provides monitoring for various switch hardware elements. Minimum or maximum values depend on the flags you apply to the basic command. The table below lists the hardware elements and applicable commands and flags.

| Hardware Element | Monitoring Commands | Interval Poll |
|----------------- |-------------------- |-------------- |
| Temperature | `smonctl -j`<br>`smonctl -j -s TEMP[X]` | 10 seconds |
| Fan | `smonctl -j`<br>`smonctl -j -s FAN[X]` | 10 seconds |
| PSU | `smonctl -j`<br>`smonctl -j -s PSU[X]` | 10 seconds |
| PSU Fan | `smonctl -j`<br>`smonctl -j -s PSU[X]Fan[X]` |10 seconds |
| PSU Temperature | `smonctl -j`<br>`smonctl -j -s PSU[X]Temp[X]` |10 seconds |
| Voltage|`smonctl -j`<br>`smonctl -j -s Volt[X]` | 10 seconds |
| Front Panel LED | `ledmgrd -d`<br>`ledmgrd -j` |5 seconds |

{{%notice note%}}
Not all switch models include a sensor for monitoring power consumption and voltage. See {{<link url="Monitoring-System-Hardware#smond-daemon" text="this note">}} for details.
{{%/notice%}}

| Hardware Logs| Log Location| Log Entries|
|------------- |------------ |----------- |
| High temperature | <pre>/var/log/syslog</pre> | <pre>/usr/sbin/smond : : Temp1(Board Sensor near CPU): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Temp2(Board Sensor Near Virtual Switch): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Temp3(Board Sensor at Front Left Corner): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Temp4(Board Sensor at Front Right Corner): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Temp5(Board Sensor near Fan): state changed from UNKNOWN to OK</pre> |
| Fan speed issues | <pre>/var/log/syslog</pre> | <pre>/usr/sbin/smond : : Fan1(Fan Tray 1, Fan 1): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Fan2(Fan Tray 1, Fan 2): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Fan3(Fan Tray 2, Fan 1): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Fan4(Fan Tray 2, Fan 2): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Fan5(Fan Tray 3, Fan 1): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : Fan6(Fan Tray 3, Fan 2): state changed from UNKNOWN to OK</pre> |
| Fan direction issue |<pre>/var/log/syslog</pre> |<pre>/usr/sbin/smond : : Fan direction mismatch: 12 fans B2F; 1 fans F2B!</pre> |
| PSU failure | <pre>/var/log/syslog</pre> | <pre>/usr/sbin/smond : : PSU1Fan1(PSU1 Fan): state changed from UNKNOWN to OK<br>/usr/sbin/smond : : PSU2Fan1(PSU2 Fan): state changed from UNKNOWN to BAD</pre> |

## System Data

Cumulus Linux includes several ways to monitor system data. In addition, you can receive alerts in high risk situations.

### CPU Idle Time

When a CPU reports five high CPU alerts within a span of five minutes, the switch logs an alert.

{{%notice warning%}}
Short bursts of high CPU can occur during `switchd` churn or routing protocol startup. Do not set alerts for these short bursts.
{{%/notice%}}

| System Element | Monitoring Commands | Interval Poll |
|--------------- |-------------------- |-------------- |
|CPU utilization | `sudo cat /proc/stat`<br>`top -b -n 1` | 30 seconds |

| CPU Logs | Log Location | Log Entries |
|--------- |------------- |------------ |
| High CPU | <pre>/var/log/syslog</pre> | <pre>sysmonitor: Critically high CPU use: 99%<br>systemd[1]: Starting Monitor system resources (cpu, memory, disk)...<br>systemd[1]: Started Monitor system resources (cpu, memory, disk).<br>sysmonitor: High CPU use: 89%<br>systemd[1]: Starting Monitor system resources (cpu, memory, disk)...<br>systemd[1]: Started Monitor system resources (cpu, memory, disk).<br>sysmonitor: CPU use no longer high: 77% |

Cumulus Linux monitors CPU, memory, and disk space with `sysmonitor`. The configurations for the thresholds are in `/etc/cumulus/sysmonitor.conf`. For more information, see `man sysmonitor`.

| CPU measure  | Thresholds            |
| ------------ | --------------------- |
| Use          | Alert: 90% Crit: 95%  |
| Process Load | Alarm: 95% Crit: 125% |
<!--
{{%notice note%}}
The Spectrum 1 CPUs can become overloaded at a moderate to high network scale. If your Spectrum 1 switch is not able to process CPU-destined traffic or is running continually at high CPU, either reduce the scale of the network in which you deploy the Spectrum 1 switches or upgrade your switch.
{{%/notice%}}
-->
### Disk Usage

When monitoring disk utilization, you can exclude `tmpfs` from monitoring.

| System Element | Monitoring Commands | Interval Poll |
|--------------- |-------------------- |-------------- |
| Disk utilization | `/bin/df -x tmpfs` | 300 seconds |

## Process Restart

In Cumulus Linux, `systemd` monitors and restarts processes.

| Process Element | Monitoring Commands |
|---------------- |-------------------- |
| View processes that `systemd` monitors | `systemctl status` |

## Layer 1 Protocols and Interfaces

Link and port state interface transitions log to `/var/log/syslog` and `/var/log/switchd.log`.

| Interface Element | Monitoring Commands |
|------------------ |-------------------- |
| Link state | `sudo cat /sys/class/net/[iface]/operstate`<br>`nv show interface --view=brief` |
| Link speed | `sudo cat /sys/class/net/[iface]/speed`<br>`nv show interface --view=brief` |
| Port state | `ip link show`<br>`nv show interface --view=brief` |
| Bond state | `sudo cat /proc/net/bonding/[bond]`<br>`nv show interface --view=brief` |

You obtain interface counters from either querying the hardware or the Linux kernel. The Linux kernel aggregates the output from the hardware.

| Interface Counter Element | Monitoring Commands | Interval Poll|
|-------------------------- |-------------------- |------------- |
| Interface counters | `cat /sys/class/net/[iface]/statistics/[stat_name]`<br>`cl-netstat -j`<br>`ethtool -S [ iface]` | 10 seconds |

| Layer 1 Logs |Log Location | Log Entries |
|------------- |------------- |------------ |
| Link failure/Link flap | <pre>/var/log/switchd.log</pre> | <pre>switchd[5692]: nic.c:213 nic_set_carrier: swp17: setting kernel carrier: down<br>switchd[5692]: netlink.c:291 libnl: swp1, family 0, ifi 20, oper down<br>switchd[5692]: nic.c:213 nic_set_carrier: swp1: setting kernel carrier: up<br>switchd[5692]: netlink.c:291 libnl: swp17, family 0, ifi 20, oper up</pre> |
| Unidirectional link | <pre>/var/log/switchd.log<br>/var/log/ptm.log</pre>|<pre>ptmd[7146]: ptm_bfd.c:2471 Created new session 0x1 with peer 10.255.255.11 port swp1<br>ptmd[7146]: ptm_bfd.c:2471 Created new session 0x2 with peer fe80::4638:39ff:fe00:5b port swp1<br>ptmd[7146]: ptm_bfd.c:2471 Session 0x1 down to peer 10.255.255.11, Reason 8<br>ptmd[7146]: ptm_bfd.c:2471 Detect timeout on session 0x1 with peer 10.255.255.11, in state 1</pre> |
| Bond Negotiation Working | <pre>/var/log/syslog</pre>|<pre>kernel: [85412.763193] bonding: bond0 is being created...<br>kernel: [85412.770014] bond0: Enslaving swp2 as a backup interface with an up link<br>kernel: [85412.775216] bond0: Enslaving swp1 as a backup interface with an up link<br>kernel: [85412.797393] IPv6: ADDRCONF(NETDEV_UP): bond0: link is not ready<br>kernel: [85412.799425] IPv6: ADDRCONF(NETDEV_CHANGE): bond0: link becomes ready</pre> |
| Bond Negotiation Failing | <pre>/var/log/syslog</pre>|<pre>kernel: [85412.763193] bonding: bond0 is being created...<br>kernel: [85412.770014] bond0: Enslaving swp2 as a backup interface with an up link<br>kernel: [85412.775216] bond0: Enslaving swp1 as a backup interface with an up link<br>kernel: [85412.797393] IPv6: ADDRCONF(NETDEV_UP): bond0: link is not ready</pre> |
| MLAG peerlink negotiation Working | <pre>/var/log/syslog</pre>|<pre>lldpd[998]: error while receiving frame on swp50: Network is down<br>lldpd[998]: error while receiving frame on swp49: Network is down<br>kernel: [76174.262893] peerlink: Setting ad_actor_system to 44:38:39:00:00:11<br>kernel: [76174.264205] 8021q: adding VLAN 0 to HW filter on device peerlink<br>mstpd: one_clag_cmd: setting (1) peer link: peerlink<br>mstpd: one_clag_cmd: setting (1) clag state: up<br>mstpd: one_clag_cmd: setting system-mac 44:38:39:ff:40:94<br>mstpd: one_clag_cmd: setting clag-role secondary</pre> |
| | <pre>/var/log/clagd.log</pre>|<pre>clagd[14003]: Cleanup is executing.<br>clagd[14003]: Cannot open file "/tmp/pre-clagd.q7XiO<br>clagd[14003]: Cleanup is finished<br>clagd[14003]: Beginning execution of clagd version 1<br>clagd[14003]: Invoked with: /usr/sbin/clagd --daemon<br>clagd[14003]: Role is now secondary<br>clagd[14003]: HealthCheck: role via backup is second<br>clagd[14003]: HealthCheck: backup active<br>clagd[14003]: Initial config loaded<br>clagd[14003]: The peer switch is active.<br>clagd[14003]: Initial data sync from peer done.<br>clagd[14003]: Initial handshake done.<br>clagd[14003]: Initial data sync to peer done.</pre> |
| MLAG peerlink negotiation Failing | <pre>/var/log/syslog</pre>|<pre>lldpd[998]: error while receiving frame on swp50: Network is down<br>lldpd[998]: error while receiving frame on swp49: Network is down<br>kernel: [76174.262893] peerlink: Setting ad_actor_system to 44:38:39:00:00:11<br>kernel: [76174.264205] 8021q: adding VLAN 0 to HW filter on device peerlink<br>mstpd: one_clag_cmd: setting (1) peer link: peerlink<br>mstpd: one_clag_cmd: setting (1) clag state: down<br>mstpd: one_clag_cmd: setting system-mac 44:38:39:ff:40:94<br>mstpd: one_clag_cmd: setting clag-role secondary</pre> |
| | <pre>/var/log/clagd.log</pre> | <pre>clagd[26916]: Cleanup is executing.<br>clagd[26916]: Cannot open file "/tmp/pre-clagd.6M527vvGX0/brbatch" for reading: No such file or directory<br>clagd[26916]: Cleanup is finished<br>clagd[26916]: Beginning execution of clagd version 1.3.0<br>clagd[26916]: Invoked with: /usr/sbin/clagd --daemon 169.254.1.2 peerlink.4094 44:38:39:FF:01:01 --priority 1000 --backupIp 10.0.0.2<br>clagd[26916]: Role is now secondary<br>clagd[26916]: Initial config loaded</pre> |
| MLAG port negotiation Working | <pre>/var/log/syslog</pre> | <pre>kernel: [77419.112195] bonding: server01 is being created...<br>lldpd[998]: error while receiving frame on swp1: Network is down<br>kernel: [77419.122707] 8021q: adding VLAN 0 to HW filter on device swp1<br>kernel: [77419.126408] server01: Enslaving swp1 as a backup interface with a down link<br>kernel: [77419.177175] server01: Setting ad_actor_system to 44:38:39:ff:40:94<br>kernel: [77419.190874] server01: Warning: No 802.3ad response from the link partner for any adapters in the bond<br>kernel: [77419.191448] IPv6: ADDRCONF(NETDEV_UP): server01: link is not ready<br>kernel: [77419.191452] 8021q: adding VLAN 0 to HW filter on device server01<br>kernel: [77419.192060] server01: link status definitely up for interface swp1, 1000 Mbps full duplex<br>kernel: [77419.192065] server01: now running without any active interface!<br>kernel: [77421.491811] IPv6: ADDRCONF(NETDEV_CHANGE): server01: link becomes ready<br>mstpd: one_clag_cmd: setting (1) mac 44:38:39:00:00:17 <server01, None></pre>|
| | <pre>/var/log/clagd.log</pre> | <pre>clagd[14003]: server01 is now dual connected.</pre> |
| MLAG port negotiation Failing | <pre>/var/log/syslog</pre> | <pre>kernel: [79290.290999] bonding: server01 is being created...<br>kernel: [79290.299645] 8021q: adding VLAN 0 to HW filter on device swp1<br>kernel: [79290.301790] server01: Enslaving swp1 as a backup interface with a down link<br>kernel: [79290.358294] server01: Setting ad_actor_system to 44:38:39:ff:40:94<br>kernel: [79290.373590] server01: Warning: No 802.3ad response from the link partner for any adapters in the bond<br>kernel: [79290.374024] IPv6: ADDRCONF(NETDEV_UP): server01: link is not ready<br>kernel: [79290.374028] 8021q: adding VLAN 0 to HW filter on device server01<br>kernel: [79290.375033] server01: link status definitely up for interface swp1, 1000 Mbps full duplex<br>kernel: [79290.375037] server01: now running without any active interface!</pre> |
| | <pre>/var/log/clagd.log</pre> | <pre>clagd[14291]: Conflict (server01): matching clag-id (1) not configured on peer...<br>clagd[14291]: Conflict cleared (server01): matching clag-id (1) detected on peer</pre> |
| MLAG port negotiation Flapping | <pre>/var/log/syslog</pre>|<pre>mstpd: one_clag_cmd: setting (0) mac 00:00:00:00:00:00 <server01, None><br>mstpd: one_clag_cmd: setting (1) mac 44:38:39:00:00:03 <server01, None></pre> |
| | <pre>/var/log/clagd.log</pre> | <pre>clagd[14291]: server01 is no longer dual connected<br>clagd[14291]: server01 is now dual connected.</pre> |

PTM uses LLDP information to compare against a `topology.dot` file that describes the network. It has built in alerting capabilities. Use PTM on the switch instead of polling LLDP information regularly. You can install PTM from the Cumulus Linux {{<exlink url="https://github.com/CumulusNetworks/ptm" text="GitHub repository">}}.

{{%notice note%}}
Consider tracking peering information through PTM. For more information, refer to the {{<link url="Prescriptive-Topology-Manager-PTM" text="Prescriptive Topology Manager documentation">}}.
{{%/notice%}}

| Neighbor Element | Monitoring Commands | Interval Poll |
|----------------- |-------------------- |-------------- |
| LLDP Neighbor | `lldpctl -f json` | 300 seconds |
| Prescriptive Topology Manager | `ptmctl -j [-d]` | Triggered |

## Layer 2 Protocols

Spanning tree is a protocol that prevents loops in a layer 2 infrastructure. In a stable state, the spanning tree protocol converges. Monitor the Topology Change Notifications (TCN) in STP to identify when new BPDUs arrive.

| Interface Counter Element | Monitoring Commands | Interval Poll |
|-------------------------- |-------------------- |-------------- |
| STP TCN Transitions | `mstpctl showbridge json`<br>`mstpctl showport json` | 60 seconds |
| MLAG peer state | `clagctl status`<br>`clagd -j`<br>`sudo cat /var/log/clagd.log` | 60 seconds |
| MLAG peer MACs | `clagctl dumppeermacs`<br>`clagctl dumpourmacs` |300 seconds |

| Layer 2 Logs | Log Location | Log Entries |
|------------- |------------- |------------ |
| Spanning Tree Working | <pre>/var/log/syslog</pre> | <pre>kernel: [1653877.190724] device swp1 entered promiscuous mode<br>kernel: [1653877.190796] device swp2 entered promiscuous mode<br>mstpd: create_br: Add bridge bridge<br>mstpd: clag_set_sys_mac_br: set bridge mac 00:00:00:00:00:00<br>mstpd: create_if: Add iface swp1 as port#2 to bridge bridge<br>mstpd: set_if_up: Port swp1 : up<br>mstpd: create_if: Add iface swp2 as port#1 to bridge bridge<br>mstpd: set_if_up: Port swp2 : up<br>mstpd: set_br_up: Set bridge bridge up<br>mstpd: MSTP_OUT_set_state: bridge:swp1:0 entering blocking state(Disabled)<br>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering blocking state(Disabled)<br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp1:0 Flushing forwarding database<br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database<br>mstpd: MSTP_OUT_set_state: bridge:swp1:0 entering learning state(Designated)<br>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering learning state(Designated)<br>sudo: pam_unix(sudo:session): session closed for user root<br>mstpd: MSTP_OUT_set_state: bridge:swp1:0 entering forwarding state(Designated)<br>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering forwarding state(Designated)<br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database<br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp1:0 Flushing forwarding database</pre> |
| Spanning Tree Blocking | <pre>/var/log/syslog</pre> | <pre>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering blocking state(Designated)<br>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering learning state(Designated)</br>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering forwarding state(Designated)</br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database</br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database</br>mstpd: MSTP_OUT_set_state: bridge:swp2:0 entering blocking state(Alternate)<br>mstpd: MSTP_OUT_flush_all_fids: bridge:swp2:0 Flushing forwarding database</pre> |

## Layer 3 Protocols

When FRR boots up for the first time, there is a different log file for each activated daemon. If you edit the log file (for example, through vtysh or `frr.conf`), the integrated configuration sends all logs to the same file.

To send FRR logs to syslog, apply the configuration `log syslog` in vtysh.

### BGP

When monitoring BGP, check if BGP peers are operational. There is not much value in alerting on the current operational state of the peer; monitoring the transition is more valuable, which you can do by monitoring `syslog`.

Monitoring the routing table provides trending on the size of the infrastructure. This is useful when you integrate with host-based solutions (such as Routing on the Host) when the routes track with the number of applications available.

| BGP Element | Monitoring Commands | Interval Poll |
|------------ |-------------------- |-------------- |
| BGP peer failure | `sudo vtysh -c "show ip bgp summary json"` | 60 seconds |
| BGP route table | `sudo vtysh -c "show ip bgp json"` | 600 seconds |

| BGP Logs | Log Location | Log Entries |
|--------- |------------- |------------ |
| BGP peer down | <pre>/var/log/syslog<br>/var/log/frr/*.log</pre> | <pre>bgpd[3000]: %NOTIFICATION: sent to neighbor swp1 4/0 (Hold Timer Expired) 0 bytes<br>bgpd[3000]: %ADJCHANGE: neighbor swp1 Down BGP Notification send</pre> |

### OSPF

When monitoring OSPF, check if OSPF peers are operational. There is not much value in alerting on the current operational state of the peer; monitoring the transition is more valuable, which you can do by monitoring `syslog`.

Monitoring the routing table provides trending on the size of the infrastructure. This is useful when you integrate with host-based solutions (such as Routing on the Host) when the routes track with the number of applications available.

| OSPF Element |Monitoring Commands |Interval Poll |
|------------- |------------------- |------------- |
|OSPF protocol peer failure | `sudo vtysh -c "show ip ospf neighbor all json"`<br>`cl-ospf summary show json`|60 seconds |
| OSPF link state database | `sudo vtysh - c "show ip ospf database"` | 600 seconds |

### Route and Host Entries

| Route Element | Monitoring Commands | Interval Poll |
|-------------- |-------------------- |-------------- |
| Host Entries | `cl-resource-query`<br>`cl-resource-query -k` | 600 seconds |
| Route Entries | `cl-resource-query`<br>`cl-resource-query -k` | 600 seconds |

### Routing Logs

| Layer 3 Logs | Log Location | Log Entries |
|------------- |------------- |------------ |
| Routing protocol process crash | <pre>/var/log/syslog</pre> | <pre>frrouting[1824]: Starting FRRouting daemons (prio:10):. zebra. bgpd.<br>bgpd[1847]: BGPd 1.0.0+cl3u7 starting: vty@2605, bgp@<all>:179<br>zebra[1840]: client 12 says hello and bids fair to announce only bgp routes<br>watchfrr[1853]: watchfrr 1.0.0+cl3u7 watching [zebra bgpd], mode [phased zebra restart]<br>watchfrr[1853]: bgpd state -> up : connect succeeded<br>watchfrr[1853]: bgpd state -> down : read returned EOF<br>cumulus-core: Running cl-support for core files bgpd.3030.1470341944.core.core_helper<br>core_check.sh[4992]: Please send /var/support/cl_support__spine01_20160804_201905.tar.xz to Cumulus support<br>watchfrr[1853]: Forked background command [pid 6665]: /usr/sbin/service frr restart bgpd<br>watchfrr[1853]: watchfrr 0.99.24+cl3u2 watching [zebra bgpd ospfd], mode [phased zebra restart]<br>watchfrr[1853]: zebra state -> up : connect succeeded<br>watchfrr[1853]: bgpd state -> up : connect succeeded<br>watchfrr[1853]: watchfrr: Notifying Systemd we are up and running</pre> |

## Logging

The table below describes the various log files.

| Logging Element | Monitoring Commands | Log Location |
|---------------- |-------------------- |------------- |
| syslog | Catch all log file. Identifies memory leaks and CPU spikes. | <pre>/var/log/syslog</pre> |
| switchd functionality | Hardware Abstraction Layer (HAL). | <pre>/var/log/switchd.log</pre> |
| Routing daemons | FRR zebra daemon details. | <pre>/var/log/daemon.log</pre> |
| Routing protocol | The log file is configurable in FRR. When FRR first boots, it uses the non-integrated configuration so each routing protocol has its own log file. After booting up, FRR switches over to using the integrated configuration, so that all logs go to a single place.<br><br>To edit the location of the log files, use the log file <location> command. By default, Cumulus Linux does not send FRR logs to syslog. Use the log syslog <level> command to send logs through `rsyslog` and into `/var/log/syslog`.<br><br>**Note**: To write syslog debug messages to the log file, you must run the log syslog debug command to configure FRR with syslog severity 7 (debug); otherwise, when you issue a debug command such as `debug bgp neighbor-events`, no output logs to `/var/log/frr/frr.log`.<br><br>However, when you manually define a log target with the log file `/var/log/frr/debug.log` command, FRR automatically defaults to severity 7 (debug) logging and the output logs to `/var/log/frr/frr.log`.|<pre>/var/log/frr/zebra.log<br>/var/log/frr/{protocol}.log<br>/var/log/frr/frr.log</pre> |

## Protocols and Services

Run the following command to confirm that the NTP process is working correctly and that the switch clock is in sync with NTP:

```
cumulus@switch:~$ /usr/bin/ntpq -p
```

## Device Management

### Device Access Logs

| Access Logs | Log Location | Log Entries |
|------------ |------------- |------------ |
| User Authentication and Remote Login | <pre>/var/log/syslog</pre> | <pre>sshd[31830]: Accepted publickey for cumulus from 192.168.0.254 port 45582 ssh2: RSA 38:e6:3b:cc:04:ac:41:5e:c9:e3:93:9d:cc:9e:48:25<br>sshd[31830]: pam_unix(sshd:session): session opened for user cumulus by (uid=0)</pre> |

### Device Super User Command Logs

| Super User Command Logs | Log Location | Log Entries |
|------------------------ |------------- |------------ |
| Executing commands using sudo | <pre>/var/log/syslog</pre> | <pre>sudo: cumulus: TTY=unknown ; PWD=/home/cumulus ; USER=root ; COMMAND=/tmp/script_9938.sh -v<br>sudo: pam_unix(sudo:session): session opened for user root by (uid=0)<br>sudo: pam_unix(sudo:session): session closed for user root</pre> |
