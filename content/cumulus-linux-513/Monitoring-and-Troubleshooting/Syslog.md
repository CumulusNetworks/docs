---
title: Syslog
author: NVIDIA
weight: 147
toc: 3
---
Cumulus Linux uses `rsyslog` to collect, filter, store, and forward system logs from various services, applications, and network components. `rsyslog` enables efficient troubleshooting, centralized log management, and compliance enforcement with custom rules for log processing.  

You can configure logging based on severity, program name, and facility while specifying transport settings such as VRF, protocol (UDP or TCP), and port. Cumulus Linux also provides advanced filtering using match conditions and actions so that you can capture and forward only relevant logs. Additionally, you can configure rate limiting to ensure controlled log forwarding and prevent overwhelming the system.

## Log Details

`rsyslog` provides both local logging to the `syslog` file and the ability to export logs to an external `syslog` server. All `rsyslog` log files use high precision timestamps:

```
2015-08-14T18:21:43.337804+00:00 cumulus switchd[3629]: switchd.c:1409 switchd version 1.0-cl2.5+5
```

## Local Logging

Cumulus Linux sends logs through `rsyslog`, which writes them to files in the `/var/log` directory. There are default rules in the `/etc/rsyslog.d/` directory that define where the logs write:

| Rule | Purpose  |
| ------- | ------ |
| 10-rules.conf | Sets defaults for log messages, include log format and log rate limits. |
| 15-crit.conf | Logs `crit`, `alert` or `emerg` log messages to `/var/log/crit.log` to ensure they do not rotate away.|
 20-clagd.conf | Logs `clagd` messages to `/var/log/clagd.log` for {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}.|
| 22-linkstate.conf | Logs link state changes for all physical and logical network links to `/var/log/linkstate`. |
| 25-switchd.conf | Logs `switchd` messages to `/var/log/switchd.log`. | 
| 30-ptmd.conf  | Logs `ptmd` messages to `/var/log/ptmd.log` for {{<link url="Prescriptive-Topology-Manager-PTM" text="Prescription Topology Manager">}}. |
| 35-rdnbrd.conf | Logs `rdnbrd` messages to `/var/log/rdnbrd.log` for {{<link url="Redistribute-Neighbor">}}. |
| 42-nvued.conf | Logs `nvued` messages to `/var/log/nvued.log` for NVUE. |
| 45-frr.conf  | Logs routing protocol messages to `/var/log/frr/frr.log`. This includes BGP and OSPF log messages.  |
| 50-netq-agent.conf|  Logs NetQ agent messages to `/var/log/netq-agent.log`.|
| 50-netqd.conf| Logs `netqd` messages to `/var/log/netqd.log`.|
| 55-dhcpsnoop.conf| Logs DHCP snooping messages to `/var/log/dhcpsnoop.log`.|
| 66-ptp4l.conf | Logs PTP messages to `/var/log/ptp4l.log`.|
| 99-syslog.conf | Sends all remaining processes that use `rsyslog` to `/var/log/syslog`. |

Cumulus Linux rotates and compresses log files into an archive. Processes that do not use `rsyslog` write to their own log files within the `/var/log` directory. For more information on specific log files, see {{<link url="Troubleshooting-Log-Files">}}.

## Configure syslog Servers

You can configure Cumulus Linux to send log files to one or more remote syslog servers. By default, Cumulus Linux uses port 514, the UDP protocol, and the `default` VRF for logging transport settings.

{{< tabs "TabID48 ">}}
{{< tab "NVUE Commands ">}}

The following example configures Cumulus Linux to send log files to the remote syslog server with the 192.168.0.254 IP address on the default port using the default protocol.

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254
cumulus@switch:~$ nv config apply
```

The following example configures Cumulus Linux to send log files to the remote syslog server with the 192.168.0.254 IP address on port 601 using the TCP protocol.

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 port 601
cumulus@switch:~$ nv set system syslog server 192.168.0.254 protocol tcp
cumulus@switch:~$ nv config apply
```

By default, the syslog server runs in the default VRF. To set a different server VRF, run the `nv set system syslog server <server-id> vrf <vrf-id>` command. The following example sets the syslog server to run in the management VRF:

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 vrf mgmt
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Create a file in the `/etc/rsyslog.d/` directory and add the server IP address, port and protocol. Make sure the filename starts with a number lower than 99 so that it executes before log messages go in.

   ```
   cumulus@switch:~$ sudo nano /etc/rsyslog.d/11-remotesyslog-default.conf
   ...
   action(type="omfwd" Target="@@192.168.0.254" Port="601" Protocol="tcp")
   ```

  - For TCP-based syslog, use two @@ before the IP address *@@192.168.1.2:514*.
  - The file numbering in `/etc/rsyslog.d/` dictates how the rules install into `rsyslog.d`. Lower numbered rules process first and `rsyslog` processing *terminates* with the `stop` keyword. For example, the `rsyslog` configuration for FRR is in the `45-frr.conf` file with an explicit `stop` at the bottom of the file. FRR messages log to the `/var/log/frr/frr.log` file on the local disk only (these messages do not go to a remote server using the default configuration). To log FRR messages remotely in addition to writing FRR messages to the local disk, rename the `99-syslog.conf` file to `11-remotesyslog.conf`. The `11-remotesyslog.conf` rule (transmit to remote server) processes FRR messages first, then the `45-frr.conf` file continues to process the messages (write to local disk in the `/var/log/frr/frr.log` file).

2. Restart `rsyslog`.

   ```
   cumulus@switch:~$ sudo systemctl restart rsyslog.service
   ```

By default, the syslog server runs in the default VRF. You can write to syslog with {{<link url="Management-VRF" text="management VRF">}} enabled by applying the following configuration:

```
cumulus@switch:~$ sudo nano /etc/rsyslog.d/11-remotesyslog.conf
...
action(type="omfwd" Target="192.168.0.254" Port="514" Protocol="tcp" Device="mgmt")
```

For each syslog server, configure a unique `action` line. For example, to configure two syslog servers at 192.168.0.254 and 10.0.0.1:

```
cumulus@switch:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
...
action(type="omfwd" Target="192.168.0.254" Port="514" Protocol="tcp" Device="mgmt" )
action(type="omfwd" Target="10.0.0.1" Port="514" Protocol="tcp" Device="mgmt" )
```

{{%notice warning%}}
If you configure remote logging to use the TCP protocol, local logging might stop when the remote syslog server is unreachable. Also, if you configure remote logging to use the UDP protocol, local logging might stop if the UDP servers are unreachable because there are no routes available for the destination IP addresses. To avoid this issue, configure a disk queue size and maximum retry count in your `rsyslog` configuration:

For TCP:

```
action(type="omfwd" Target="172.28.240.15" Device="mgmt" Port="1720" Protocol="tcp" action.resumeRetryCount="100" queue.type="linkedList" queue.size="10000")
```

For UDP:

```
action(type="omfwd" Target="172.28.240.15" Device="mgmt" Port="540" Protocol="udp" action.resumeRetryCount="100" queue.type="linkedList" queue.size="10000")
```

{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Configure Log Format

You can set the log format to:
- Standard (the default syslog format with a standard template).
- WELF (WebTrends Enhanced Log Format), which enables you to provide an optional firewall name. The WELF format structures logs as key-value pairs. Each log entry consists of a key that identifies the data field and a corresponding value. This format is easy to parse and often used for web traffic analysis and security logs.

The following example sets the log format to WELF and sets the firewall name to `nvidia`:

{{< tabs "TabID141 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system syslog format welf firewall-name nvidia
cumulus@switch:~$ nv config apply
```

To set the log format back to the default setting (standard), run the `nv unset syslog format` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the file `/etc/rsyslog.d/11-remotesyslog.conf` to add the following content:

```
cumulus@switch:~$ sudo cat /etc/rsyslog.d/11-remotesyslog.conf
...
template(name="WelfRemoteFormat" type="string" string="%TIMESTAMP% id=firewall time=\"%timereported:::date-year%-%timereported:::date-month%-%timereported:::date-day% %timereported:::date-hour%-%timereported:::date-minute%-%timereported:::date-second%\" fw=\"nvidia\" severity=\"%syslogseverity-text%\" facility=\"%syslogfacility-text%\" program=\"%programname%\" msg=\"%syslogtag%%msg:::sp-if-no-1st-sp%%msg:::drop-last-lf%\"\n")

action(type="omfwd" Target="192.168.0.254" Port="514" Protocol="tcp" Device="mgmt" Template="WelfRemoteFormat")
```

{{< /tab >}}
{{< /tabs >}}

## Configure Filters

Filtering rules let you control which logs to capture using selectors. A selector enables you to choose options such as facility, program name, severity, filters (with match conditions and actions for log selection), and rate limit, for precise and targeted log management.

The following table describes the severity levels you can use in a selector:

| Level | Description                                                                          |
| ----- | ------------------------------------------------------------------------------------ |
| 0     | Emergency messages (the system is about to crash or is unstable).                    |
| 1     | Serious conditions (alerts); you must take action immediately.                                |
| 2     | Critical conditions (serious hardware or software failures).                         |
| 3     | Error conditions (often used by drivers to indicate difficulties with the hardware). |
| 4     | Warning messages (nothing serious but might indicate problems).                      |
| 5     | Notifications for many conditions, including security events.                |
| 6     | Informational messages.                                                              |
| 7     | Debug messages.                                                                      |

If you set the severity to warning(4), the forwarding process does not include logs with severity levels debug (7), info (6), and notice (5). The forwarding process only forwards logs with severity level warning (4) or higher (Err (3), crit (2), alert (1), and emerg (0)).

You can configure the syslog rate limit in a selector to ensure that a specific resource is not flooded with messages. You can set the rate limit to burst, interval, or both.

The following example defines the selector called SELECTOR1 and groups logs based on the source `cron`:

```
cumulus@switch:~$ nv set system syslog selector SELECTOR1 facility cron
cumulus@switch:~$ nv config apply
```

The following example defines the selector named SELECTOR2, which filters logs generated by `switchd` with severity levels up to and including `debug` (all logs with severity levels `debug`, `info`, `notice`, `warning`, and higher). The filtering process includes all logs that match the regular expression `issu_start=true.+$` and logs that match `cs_mgr.+$`.

```
nv set system syslog selector SELECTOR2 program-name switchd
nv set system syslog selector SELECTOR2 severity debug
nv set system syslog selector SELECTOR2 filter 10 match issu_start=true.+$
nv set system syslog selector SELECTOR2 filter 10 action include
nv set system syslog selector SELECTOR2 filter 15 match cs_mgr.+$
nv set system syslog selector SELECTOR2 filter 15 action include
nv config apply
```

You can also specify a rate-limiting rule with an interval (between 1 and 65535) and a burst limit (between 1 and 65535) to control log message processing or forwarding within a defined time period. The interval defines the time window within which log messages are limited after reaching the burst threshold. The burst limit specifies the maximum number of log messages that can be processed instantly before rate limiting takes effect.

The following example sets a rate limiting rule with an interval of 20 and a burst limit of 200:

```
cumulus@switch:~$ nv set system syslog selector SELECTOR1 rate-limit interval 20
cumulus@switch:~$ nv set system syslog selector SELECTOR1 rate-limit burst 200
cumulus@switch:~$ nv config apply
```

If you configure more than one selector, you can associate a priority level with each selector. The following example configures SELECTOR1 with priority 1 and SELECTOR2 with priority 2.

```
cumulus@switch:~$ nv set system syslog server 192.168.0.254 selector 1 selector-id SELECTOR1
cumulus@switch:~$ nv set system syslog server 192.168.0.254 selector 2 selector-id SELECTOR2
cumulus@switch:~$ nv config apply
```

## Verify syslog Configuration

To check syslog configuration:

{{< tabs "TabID213 ">}}
{{< tab "NVUE Commands ">}}

To show all syslog configuration settings, run the `nv show system syslog` command:

```
cumulus@switch:~$  nv show system syslog
nv show system syslog
        operational  applied
------  -----------  --------
format  standard     standard

server
=========
    Servers        Vrf   Protocol  Port  Priority  Selector-Id
    -------------  ----  --------  ----  --------  -----------
    192.168.0.254  mgmt  tcp       601   1         SELECTOR1
                                         2         SELECTOR2
selector
===========
    Selectors  Severity  Program-Name  Facility  Burst  Interval  Filter  Match                Action
    ---------  --------  ------------  --------  -----  --------  ------  -------------------  -------
    SELECTOR1  notice                  cron      200    20
    SELECTOR2  debug     switchd       daemon                     10      issu_start=false.+$  exclude
```

To show the syslog format, run the `nv show system syslog format` command:

```
cumulus@switch:~$ nv show system syslog format
                 operational       applied                 
---------------  ----------------  ----------------  
welf                                                               
  firewall-name  security-gateway  security-gateway 
```

To show the configured syslog servers, run the `nv show system syslog server` command:

```
cumulus@switch:~$ nv show system syslog server
Servers        Vrf   Protocol  Port  Priority  Selector-Id
-------------  ----  --------  ----  --------  -----------
192.168.0.254  mgmt  tcp       601   1         SELECTOR1
                                     2         SELECTOR2
```

To show information for a specific syslog server, run the `nv show system syslog server <server-id>` command:

```
cumulus@switch:~$ nv show system syslog server 192.168.0.254
          operational  applied
--------  -----------  -------
port      601          601
protocol  tcp          tcp
vrf       mgmt         mgmt

selector
===========
    Priority  Selector-Id
    --------  -----------
    1         SELECTOR1
    2         SELECTOR2
```

To show filtering information for a selector, run the `nv show system syslog selector <selector-id>` command:

```
cumulus@switch:~$ nv show system syslog selector SELECTOR2
              operational  applied
------------  -----------  -------
facility      daemon       daemon 
program-name  switchd      switchd
severity      debug        debug  

filter
=========
    Priority  Action   Match              
    --------  -------  -------------------
    10        exclude  issu_start=false.+$
```

To show all filters for a specific selector, run the `nv show system syslog selector <selector-id> filter` command:

```
cumulus@switch:~$ nv show system syslog selector SELECTOR2 filter
Priority  Action   Match              
--------  -------  -------------------
10        exclude  issu_start=false.+$
```

To show information about a specific filter for a selector, run the `nv show system syslog selector <selector-id> filter <filter-id>` command:

```
cumulus@switch:~$ nv show system syslog selector SELECTOR2 filter 10
        operational          applied            
------  -------------------  -------------------
match   issu_start=false.+$  issu_start=false.+$
action  exclude              exclude
```

To show the rate limit configuration for a selector, run the `nv show system syslog selector <selector-id> rate-limit` command:

```
cumulus@switch:~$ nv show system syslog selector SELECTOR1 rate-limit
          operational  applied
--------  -----------  -------
burst     200          200    
interval  20           20
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

After making manual changes to any files in the `/etc/rsyslog.d` directory, use the `sudo rsyslogd -N1` command to identify any errors in the configuration files that prevent the `rsyslog` service from starting.

In the following example, a closing parenthesis is missing in the `11-remotesyslog.conf` file, which configures `syslog` for management VRF:

```
cumulus@leaf01:mgmt-vrf:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp"

cumulus@leaf01:mgmt-vrf:~$ sudo rsyslogd -N1
rsyslogd: version 8.4.2, config validation run (level 1), master config /etc/rsyslog.conf
syslogd: error during parsing file /etc/rsyslog.d/15-crit.conf, on or before line 3: invalid character '$' in object definition - is there an invalid escape sequence somewhere? [try http: /www.rsyslog.com/e/2207 ]
rsyslogd: error during parsing file /etc/rsyslog.d/15-crit.conf, on or before line 3: syntax error on token 'crit_log' [try http://www.rsyslog.com/e/2207 ]
```

After correcting the invalid syntax, issuing the `sudo rsyslogd -N1` command produces the following output.

```
cumulus@leaf01:mgmt-vrf:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp")
cumulus@leaf01:mgmt-vrf:~$ sudo rsyslogd -N1
rsyslogd: version 8.4.2, config validation run (level 1), master config /etc/rsyslog.conf
rsyslogd: End of config validation run. Bye.
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

You can use the following Linux commands to troubleshoot `syslog` issues.

### Verifying that rsyslog is Running

To verify that the `rsyslog` service is running, use the `sudo systemctl status rsyslog.service` command:

```
cumulus@leaf01:mgmt-vrf:~$ sudo systemctl status rsyslog.service
rsyslog.service - System Logging Service
  Loaded: loaded (/lib/systemd/system/rsyslog.service; enabled)
  Active: active (running) since Sat 2017-12-09 00:48:58 UTC; 7min ago
    Docs: man:rsyslogd(8)
          http://www.rsyslog.com/doc/
Main PID: 11751 (rsyslogd)
   Tasks: 4 (limit: 2032)
     Memory: 1.1M
        CPU: 20ms
     CGroup: /system.slice/rsyslog.service
             └─8587 /usr/sbin/rsyslogd -n -iNONE

Dec 09 00:48:58 leaf01 systemd[1]: Started System Logging Service.
```

### tcpdump

If a syslog server is not accessible to validate that `syslog` messages are exporting, you can use `tcpdump`.

In the following example, a syslog server uses 192.168.0.254 for UDP syslog messages on port 514:

```
cumulus@leaf01:mgmt-vrf:~$ sudo tcpdump -i eth0 host 192.168.0.254 and udp port 514
```

To generate `syslog` messages, use `sudo` in another session such as `sudo date`. Using `sudo` generates an `authpriv` log.

```
cumulus@leaf01:mgmt-vrf:~$ sudo tcpdump -i eth0 host 192.168.0.254 and udp port 514
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
00:57:15.356836 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.notice, length: 105
00:57:15.364346 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.info, length: 103
00:57:15.369476 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.info, length: 85
```

To see the contents of the `syslog` file, use the `tcpdump -X` option:

```
cumulus@leaf01:mgmt-vrf:~$ sudo tcpdump -i eth0 host 192.168.0.254 and udp port 514 -X -c 3
tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
listening on eth0, link-type EN10MB (Ethernet), capture size 262144 bytes
00:59:15.980048 IP leaf01.lab.local.33875 > 192.168.0.254.syslog: SYSLOG authpriv.notice, length: 105
0x0000: 4500 0085 33ee 4000 4011 8420 c0a8 000b E...3.@.@.......
0x0010: c0a8 00fe 8453 0202 0071 9d18 3c38 353e .....S...q..<85>
0x0020: 4465 6320 2039 2030 303a 3539 3a31 3520 Dec..9.00:59:15.
0x0030: 6c65 6166 3031 2073 7564 6f3a 2020 6375 leaf01.sudo:..cu
0x0040: 6d75 6c75 7320 3a20 5454 593d 7074 732f mulus.:.TTY=pts/
0x0050: 3120 3b20 5057 443d 2f68 6f6d 652f 6375 1.;.PWD=/home/cu
0x0060: 6d75 6c75 7320 3b20 5553 4552 3d72 6f6f mulus.;.USER=roo
0x0070: 7420 3b20 434f 4d4d 414e 443d 2f62 696e t.;.COMMAND=/bin
0x0080: 2f64 6174 65 /date
```
