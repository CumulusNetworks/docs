---
title: Monitoring and Troubleshooting
author: NVIDIA
weight: 1010
toc: 2
---
This chapter introduces the basics for monitoring and troubleshooting Cumulus Linux.

## Serial Console

Use the serial console to debug issues if you reboot the switch often or if you do not have a reliable network connection.

The default serial console baud rate is 115200, which is the baud rate {{<exlink url="http://opencomputeproject.github.io/onie" text="ONIE">}} uses.

### Configure the Serial Console

On x86 switches, you configure serial console baud rate by editing `grub`.

{{%notice warning%}}
Incorrect configuration settings in `grub` cause the switch to be inaccessible through the console. Review `grub` changes before you implement them.
{{%/notice%}}

The valid values for the baud rate are:

- 300
- 600
- 1200
- 2400
- 4800
- 9600
- 19200
- 38400
- 115200

To change the serial console baud rate:

1. Edit the `/etc/default/grub` file and provide a valid value for the `--speed` and `console` variables:

   ```
   GRUB_SERIAL_COMMAND="serial --port=0x2f8 --speed=115200 --word=8 --parity=no --stop=1"
   GRUB_CMDLINE_LINUX="console=ttyS1,115200n8 cl_platform=accton_as5712_54x"
   ```

2. After you save your changes to the grub configuration, type the following at the command prompt:

   ```
   cumulus@switch:~$ update-grub
   ```

3. If you plan on accessing the switch BIOS over the serial console, you need to update the baud rate in the switch BIOS. For more information, see [this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Accessing-the-BIOS-on-an-x86-Switch" >}}).

4. Reboot the switch.

### Change the Console Log Level

By default, the console prints all log messages except debug messages. To tune console logging to be less verbose so that certain levels of messages do not print, run the `dmesg -n <level>` command, where the log levels are:

| Level | Description                                                                          |
| ----- | ------------------------------------------------------------------------------------ |
| 0     | Emergency messages (the system is about to crash or is unstable).                    |
| 1     | Serious conditions; you must take action immediately.                                |
| 2     | Critical conditions (serious hardware or software failures).                         |
| 3     | Error conditions (often used by drivers to indicate difficulties with the hardware). |
| 4     | Warning messages (nothing serious but might indicate problems).                      |
| 5     | Message notifications for many conditions, including security events.                |
| 6     | Informational messages.                                                              |
| 7     | Debug messages.                                                                      |

Only messages with a value lower than the level specified print to the console. For example, if you specify level **3**, only level 2 (critical conditions), level 1 (serious conditions), and level 0 (emergency messages) print to the console:

```
cumulus@switch:~$ sudo dmesg -n 3
```

You can also run `dmesg --console-level <level>` command, where the log levels are `emerg`, `alert`, `crit`, `err`, `warn`, `notice`, `info`, or `debug`. For example, to print critical conditions, run the following command:

```
cumulus@switch:~$ sudo dmesg --console-level crit
```

The `dmesg` command applies until the next reboot.

For more details about the `dmesg` command, run `man dmesg`.

## Show System Information

Cumulus Linux provides commands to obtain system information and to show the version of Cumulus Linux you are running. Use these commands when performing system diagnostics, troubleshooting performance, or submitting a support request.

To show information about the version of Cumulus Linux running on the switch, run the `nv show system` command:

```
cumulus@switch:~$ nv show system
            operational          applied
-----------  -------------------  -------
hostname     leaf01                
build        Cumulus Linux 5.10        
uptime       0:02:50                     
timezone     Etc/UTC                     
maintenance                              
  mode       disabled                    
  ports      enabled
```

To show system memory information in bytes, run the `nv show system memory` command:

```
cumulus@switch:~$ nv show system memory
Type      Buffers     Cache        Free         Total         Used         Utilization
--------  ----------  -----------  -----------  ------------  -----------  -----------
Physical  81661952 B  571834368 B  373276672 B  1813528576 B  786755584 B  79.4%
Swap                               0 B          0 B           0 B          0.0%
```

To show system CPU information, run the `nv show system cpu` command:

```
cumulus@switch:~$ nv show system cpu
             operational                  
-----------  -----------------------------
model        QEMU Virtual CPU version 2.5+
core-count   1                            
utilization  0.3%
```

To show general information about the switch, run the `nv show platform` command:

```
cumulus@switch:~$ nv show platform
              operational                            
------------  ---------------------------------------
system-mac    44:38:39:22:01:b1                      
manufacturer  Accton                                 
cpu           x86_64 QEMU Virtual CPU version 2.5+ x1
memory        1751856 kB                             
disk-size     n/a                                    
port-layout   n/a                                    
asic-model    n/a                                    
system-uuid   a6bfbd6d-70ac-426f-b46d-3743e16e1f4b
```
<!-- vale off -->
## Diagnostics Using cl-support
<!-- vale on -->
You can use `cl-support` to generate a single export file that contains various details about switch configuration, and is useful for remote debugging and troubleshooting. For more information about `cl-support`, read {{<link url="Understanding-the-cl-support-Output-File">}}.

Run `cl-support` to investigate issues before you submit a support request.

```
cumulus@switch:~$ sudo cl-support -h
Usage: [-h (help)] [-cDjlMsv] [-d m1,m2,...] [-e m1,m2,...]
  [-p prefix] [-r reason] [-S dir] [-T Timeout_seconds] [-t tag]
  -h: Display this help message
  -c: Run only modules matching any core files, if no -e modules
  -D: Display debugging information
  -d: Disable (do not run) modules in this comma separated list
  -e: Enable (only run) modules in this comma separated list; "-e all" runs
      all modules and sub-modules, including all optional modules
...
```

## Send Log Files to a syslog Server

You can configure Cumulus Linux to send log files to one or more remote syslog servers.

The following example configures Cumulus Linux to send log files to the remote syslog server with the 192.168.0.254 address in the default VRF on port 514 using UDP.

{{%notice note%}}
You must specify a VRF in the command.
{{%/notice%}}

```
cumulus@switch:~$ nv set service syslog default server 192.168.0.254 port 514
cumulus@switch:~$ nv set service syslog default server 192.168.0.254 protocol udp
cumulus@switch:~$ nv config apply
```

The configuration creates the `/etc/rsyslog.d/11-remotesyslog-default.conf` file. The file has the following content:

```
cumulus@switch:~$ sudo cat /etc/rsyslog.d/11-remotesyslog-default.conf
# Auto-generated by NVUE!
# Any local modifications will prevent NVUE from re-generating this file.
# md5sum: c8e094c868c7f9be4cfa6ccec752b44b
#
# Remote syslog servers configured through CUE
#
action(type="omfwd" Target="192.168.0.254" Port="514" Protocol="udp")
```

### Log Technical Details

{{<exlink url="http://www.rsyslog.com/" text="rsyslog">}} performs logging on Cumulus Linux. `rsyslog` provides both local logging to the `syslog` file and the ability to export logs to an external `syslog` server. All `rsyslog` log files use high precision timestamps:

```
2015-08-14T18:21:43.337804+00:00 cumulus switchd[3629]: switchd.c:1409 switchd version 1.0-cl2.5+5
```

Cumulus Linux includes applications in the `/var/log/` directory that write directly to a log file without going through `rsyslog`.

{{%notice note%}}
All Cumulus Linux rules are in separate files in `/etc/rsyslog.d/`, which `rsyslog` calls at the end of the `GLOBAL DIRECTIVES` section of the `/etc/rsyslog.conf` file. `rsyslog` ignores the `RULES` section at the end of the `rsyslog.conf` file; the rules in the `/etc/rsyslog.d` file must process the messages, which the last line in the `/etc/rsyslog.d/99-syslog.conf` file drops.
{{%/notice%}}

### Local Logging

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

### Enable Remote syslog

Cumulus Linux does not send all log messages to a remote server. To send other log files (such as `switchd` logs) to a `syslog` server, follow these steps:

1. Create a file in `/etc/rsyslog.d/`. Make sure the filename starts with a number lower than 99 so that it executes before log messages go in, such as `20-clagd.conf` or `25-switchd.conf`. The name of the example file below is `/etc/rsyslog.d/11-remotesyslog.conf`. Add content similar to the following:

   ```
   ## Logging switchd messages to remote syslog server

   @192.168.1.2:514
   ```

   This configuration sends log messages to a remote `syslog` server for the following processes: `clagd`, `switchd`, `ptmd`, `rdnbrd`, `nvued` and `syslog`. It follows the same syntax as the `/var/log/syslog` file, where *@* indicates UDP, *192.168.12* is the IP address of the `syslog` server, and *514* is the UDP port.

   {{%notice note%}}
- For TCP-based syslog, use two @@ before the IP address *@@192.168.1.2:514*.
- The file numbering in `/etc/rsyslog.d/` dictates how the rules install into `rsyslog.d`. Lower numbered rules process first and `rsyslog` processing *terminates* with the `stop` keyword. For example, the `rsyslog` configuration for FRR is in the `45-frr.conf` file with an explicit `stop` at the bottom of the file. FRR messages log to the `/var/log/frr/frr.log` file on the local disk only (these messages do not go to a remote server using the default configuration). To log FRR messages remotely in addition to writing FRR messages to the local disk, rename the `99-syslog.conf` file to `11-remotesyslog.conf`. The `11-remotesyslog.conf` rule (transmit to remote server) processes FRR messages first, then the `45-frr.conf` file continues to process the messages (write to local disk in the `/var/log/frr/frr.log` file).
- Do not use the `imfile` module with any file written by `rsyslogd`.
{{%/notice%}}

2. Restart `rsyslog`.

   ```
   cumulus@switch:~$ sudo systemctl restart rsyslog.service
   ```

### Write to syslog with Management VRF Enabled

You can write to syslog with {{<link url="Management-VRF" text="management VRF">}} enabled by applying the following configuration; the `/etc/rsyslog.d/11-remotesyslog.conf` file comments out this configuration.

```
cumulus@switch:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
## Copy all messages to the remote syslog server at 192.168.0.254 port 514
action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp")
```

For each syslog server, configure a unique `action` line. For example, to configure two syslog servers at 192.168.0.254 and 10.0.0.1:

```
cumulus@switch:~$ cat /etc/rsyslog.d/11-remotesyslog.conf
## Copy all messages to the remote syslog servers at 192.168.0.254 and 10.0.0.1 port 514
action(type="omfwd" Target="192.168.0.254" Device="mgmt" Port="514" Protocol="udp")
action(type="omfwd" Target="10.0.0.1" Device="mgmt" Port="514" Protocol="udp")
```

{{%notice warning%}}
If you configure remote logging to use the TCP protocol, local logging might stop when the remote syslog server is unreachable. Also, if you configure remote logging to use the UDP protocol, local logging might stop if the UDP servers are unreachable because there are no routes available for the destination IP addresses.

To avoid this behavior, configure a disk queue size and maximum retry count in your `rsyslog` configuration:

{{< tabs "TabID35 ">}}
{{< tab "TCP Configuration ">}}

```
action(type="omfwd" Target="172.28.240.15" Device="mgmt" Port="1720" Protocol="tcp" action.resumeRetryCount="100" queue.type="linkedList" queue.size="10000")
```

{{< /tab >}}
{{< tab "UDP Configuration ">}}

```
action(type="omfwd" Target="172.28.240.15" Device="mgmt" Port="540" Protocol="udp" action.resumeRetryCount="100" queue.type="linkedList" queue.size="10000")
```

{{< /tab >}}
{{< /tabs >}}

{{%/notice%}}

<!-- vale off -->
### Rate-limit syslog Messages
<!-- vale on -->
If you want to limit the number of `syslog` messages that write to the `syslog` file from individual processes, add the following configuration to the `/etc/rsyslog.conf` file. Adjust the interval and burst values to rate-limit messages to the appropriate levels required by your environment. For more information, read the {{<exlink url="http://www.rsyslog.com/doc/v8-stable/configuration/modules/imuxsock.html" text="rsyslog documentation">}}.

```
module(load="imuxsock"
      SysSock.RateLimit.Interval="2" SysSock.RateLimit.Burst="50")
```

The following test script shows an example of rate-limit output.

{{< expand "Example test script" >}}

```
root@leaf1:mgmt-vrf:/home/cumulus# cat ./syslog.py 
#!/usr/bin/python
import syslog
message_count=100
print "Sending %s Messages..."%(message_count)
for i in range(0,message_count):
syslog.syslog("Message Number:%s"%(i))
print "DONE."

root@leaf1:mgmt-vrf:/home/cumulus# ./syslog.py
Sending 100 Messages...
DONE.

root@leaf1:mgmt-vrf:/home/cumulus# tail -n 60 /var/log/syslog
2017-02-22T19:59:50.043342+00:00 leaf1 syslog.py[22830]: Message Number:0
2017-02-22T19:59:50.043723+00:00 leaf1 syslog.py[22830]: Message Number:1
2017-02-22T19:59:50.043941+00:00 leaf1 syslog.py[22830]: Message Number:2
2017-02-22T19:59:50.044565+00:00 leaf1 syslog.py[22830]: Message Number:3
2017-02-22T19:59:50.044830+00:00 leaf1 syslog.py[22830]: Message Number:4
2017-02-22T19:59:50.045680+00:00 leaf1 syslog.py[22830]: Message Number:5
<...snip...>
2017-02-22T19:59:50.056727+00:00 leaf1 syslog.py[22830]: Message Number:45
2017-02-22T19:59:50.057599+00:00 leaf1 syslog.py[22830]: Message Number:46
2017-02-22T19:59:50.057741+00:00 leaf1 syslog.py[22830]: Message Number:47
2017-02-22T19:59:50.057936+00:00 leaf1 syslog.py[22830]: Message Number:48
2017-02-22T19:59:50.058125+00:00 leaf1 syslog.py[22830]: Message Number:49
2017-02-22T19:59:50.058324+00:00 leaf1 rsyslogd-2177: imuxsock[pid 22830]: begin to drop messages due to rate-limiting
```

{{< /expand >}}
<!-- vale off -->
### Harmless syslog Error: Failed to reset devices.list
<!-- vale on -->
The following message logs to `/var/log/syslog` when you run `systemctl daemon-reload` and during system boot:

```
systemd[1]: Failed to reset devices.list on /system.slice: Invalid argument
```

This message is harmless, you can ignore it. It logs when `systemd` attempts to change read-only group attributes. Cumulus Linux modifies the upstream version of `systemd` to not log this message by default.

The `systemctl daemon-reload` command runs when you install Debian packages. You see the message multiple times when upgrading packages.

### Troubleshoot syslog

You can use the following commands to troubleshoot `syslog` issues.

#### Verifying that rsyslog is Running

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

#### Verify your rsyslog Configuration

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

#### tcpdump

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
