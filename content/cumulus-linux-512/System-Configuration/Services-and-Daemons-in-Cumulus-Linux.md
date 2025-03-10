---
title: Services and Daemons in Cumulus Linux
author: NVIDIA
weight: 230
toc: 3
---
*Services* (also known as *daemons*) and *processes* are at the heart of how a Linux system functions. Most of the time, a service takes care of itself; you just enable and start it, then let it run. However, because a Cumulus Linux switch is a Linux system, you can dig deeper if you like. Services can start multiple processes as they run. Services are important to monitor on a Cumulus Linux switch.

You manage services in Cumulus Linux to identify all active or stopped services and the boot time state of a specific service, disable or enable a specific service, and identify active listener ports.

## systemd and the systemctl Command

You manage services that use `systemd` with the `systemctl` command.

| Command Options | Description|
| --------| -----------|
|`status` | Returns the status of the specified service. |
|`start` | Starts the service. |
|`stop`| Stops the service. |
|`restart` | Stops, then starts the service, all the while maintaining state. If there are dependent services or services that mark the restarted service as *Required*, the other services also restart. For example, running `systemctl restart frr.service` restarts any of the routing protocol services that you enable and that are running, such as `bgpd` or `ospfd`.|
| `reload` | Reloads the configuration for the service. |
| `enable` | Enables the service to start when the system boots, but does not start it unless you use the `systemctl start SERVICENAME.service` command or reboot the switch. |
| `disable` | Disables the service, but does not stop it unless you use the `systemctl stop SERVICENAME.service` command or reboot the switch. You can start or stop a disabled service.|
| `reenable` | Disables, then enables a service. Run this command so that any new *Wants* or *WantedBy* lines create the symlinks necessary for ordering. This does not affect on other services.|

You do not need to interact with the services directly using these commands. If a critical service crashes or encounters an error, `systemd` restarts it automatically. `systemd` is the caretaker of services in modern Linux systems and responsible for starting all the necessary services at boot time.

The following example restarts the networking service:

```
cumulus@switch:~$ sudo systemctl restart networking.service
```

The following example shows all running services:

```
cumulus@switch:~$ sudo systemctl status
● switch
    State: running
      Jobs: 0 queued
    Failed: 0 units
    Since: Thu 2019-01-10 00:19:34 UTC; 23h ago
    CGroup: /
            ├─init.scope
            │ └─1 /sbin/init
            └─system.slice
              ├─haveged.service
              │ └─234 /usr/sbin/haveged --Foreground --verbose=1 -w 1024
              ├─sysmonitor.service
              │ ├─  658 /bin/bash /usr/lib/cumulus/sysmonitor
              │ └─26543 sleep 60
              ├─systemd-udevd.service
              │ └─218 /lib/systemd/systemd-udevd
              ├─system-ntp.slice
              │ └─ntp@mgmt.service
              │   └─vrf
              │     └─mgmt
              │       └─12108 /usr/sbin/ntpd -n -u ntp:ntp -g
              ├─cron.service
              │ └─274 /usr/sbin/cron -f -L 38
              ├─system-serial\x2dgetty.slice
              │ └─serial-getty@ttyS0.service
              │   └─745 /sbin/agetty -o -p -- \u --keep-baud 115200,38400,9600 ttyS0 vt220
              ├─nginx.service
              │ ├─332 nginx: master process /usr/sbin/nginx -g daemon on; master_process on;
              │ └─333 nginx: worker process
              ├─auditd.service
              │ └─235 /sbin/auditd
              ├─rasdaemon.service
              │ └─275 /usr/sbin/rasdaemon -f -r
              ├─clagd.service
              │ └─11443 /usr/bin/python /usr/sbin/clagd --daemon 169.254.1.2 peerlink.4094 44:39:39:ff:40:9
              --priority 100 --vxlanAnycas
              ├─switchd.service
              │ └─430 /usr/sbin/switchd -vx
              ...
```

{{%notice note%}}
Add the service name **after** the `systemctl` argument.
{{%/notice%}}

### Ensure a Service Starts after Multiple Restarts

By default, `systemd` tries to restart a particular service only a certain number of times within a given interval before the service fails to start. The settings *StartLimitInterval* (which defaults to 10 seconds) and *StartBurstLimit* (which defaults to 5 attempts) are in the service script; however, certain services override these defaults, sometimes with much longer times. For example, `switchd.service` sets *StartLimitInterval=10m* and *StartBurstLimit=3;* therefore, if you restart `switchd` more than three times in ten minutes, it does not start.

When the restart fails for this reason, you see a message similar to the following:

```
Job for switchd.service failed. See 'systemctl status switchd.service' and 'journalctl -xn' for details.
```

`systemctl status switchd.service` shows output similar to:

```
Active: failed (Result: start-limit) since Thu 2016-04-07 21:55:14 UTC; 15s ago
```

To clear this error, run `systemctl reset-failed switchd.service`. If you know you are going to restart frequently (multiple times within the StartLimitInterval), you can run the same command before you issue the restart request. This also applies to stop followed by start.

### Keep systemd Services from Hanging after Starting

If you start, restart, or reload a `systemd` service that you can start from another `systemd` service, you must use the `--no-block` option with `systemctl`.

## Identify Active Listener Ports for IPv4 and IPv6

You can identify the active listener ports under both IPv4 and IPv6 using the `netstat` command:

```
cumulus@switch:~$ netstat -nlp --inet --inet6
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:53              0.0.0.0:*               LISTEN      444/dnsmasq
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      874/sshd
tcp6       0      0 :::53                   :::*                    LISTEN      444/dnsmasq
tcp6       0      0 :::22                   :::*                    LISTEN      874/sshd
udp        0      0 0.0.0.0:28450           0.0.0.0:*                           839/dhclient
udp        0      0 0.0.0.0:53              0.0.0.0:*                           444/dnsmasq
udp        0      0 0.0.0.0:68              0.0.0.0:*                           839/dhclient
udp        0      0 192.168.0.42:123        0.0.0.0:*                           907/ntpd
udp        0      0 127.0.0.1:123           0.0.0.0:*                           907/ntpd
udp        0      0 0.0.0.0:123             0.0.0.0:*                           907/ntpd
udp        0      0 0.0.0.0:4784            0.0.0.0:*                           909/ptmd
udp        0      0 0.0.0.0:3784            0.0.0.0:*                           909/ptmd
udp        0      0 0.0.0.0:3785            0.0.0.0:*                           909/ptmd
udp6       0      0 :::58352                :::*                                839/dhclient
udp6       0      0 :::53                   :::*                                444/dnsmasq
udp6       0      0 fe80::a200:ff:fe00::123 :::*                                907/ntpd
udp6       0      0 ::1:123                 :::*                                907/ntpd
udp6       0      0 :::123                  :::*                                907/ntpd
udp6       0      0 :::4784                 :::*                                909/ptmd
udp6       0      0 :::3784                 :::*                                909/ptmd
```

## Identify Active or Stopped Services

To see active or stopped services, run the `cl-service-summary` command:

```
cumulus@switch:~$ cl-service-summary
Service cron               enabled    active   
Service ssh                enabled    active   
Service rsyslog            enabled    active   
Service asic-monitor       enabled    inactive 
Service clagd              disabled   active   
Service cumulus-poe                   inactive 
Service lldpd              enabled    active   
Service mstpd              enabled    active   
Service neighmgrd          enabled    active   
Service netd               enabled    active   
Service netq-agent         disabled   inactive 
Service ntp                disabled   inactive 
Service portwd             enabled    inactive 
Service ptmd               enabled    active   
Service pwmd               enabled    active   
Service smond              enabled    active   
Service switchd            enabled    active   
Service sysmonitor         enabled    active   
Service vxrd                          inactive 
Service vxsnd                         inactive 
Service rdnbrd             disabled   inactive 
Service frr                enabled    active   
Service ntp@mgmt           disabled   inactive 
Service ntp@ntp            disabled   inactive
...
```

You can also run the `systemctl list-unit-files --type service` command to list all services on the switch and to see their status:

```
cumulus@switch:~$ systemctl list-unit-files --type service
UNIT FILE                                  STATE           VENDOR PRESET
aclinit.service                            enabled         enabled      
acltool.service                            enabled         enabled      
acpid.service                              disabled        enabled      
air-agent@.service                         indirect        enabled      
apt-daily-upgrade.service                  static          -            
apt-daily.service                          static          -            
asic-monitor.service                       enabled         enabled      
atftpd.service                             generated       -            
auditd.service                             enabled         enabled      
autovt@.service                            alias           -            
blk-availability.service                   enabled         enabled      
bmcd.service                               disabled        enabled      
bootlog.service                            enabled         enabled      
cl-system-services.service                 enabled         enabled      
clagd.service                              disabled        enabled      
clagd_rebootNotifier.service               disabled        enabled      
console-getty.service                      disabled        disabled     
console-setup.service                      enabled         enabled      
container-getty@.service                   static          -            
containerd.service                         disabled        enabled      
cron.service                               enabled         enabled      
cryptdisks-early.service                   masked          enabled      
cryptdisks.service                         masked          enabled      
csmgrd.service                             enabled         enabled      
cumulus-aclcheck.service                   static          -            
cumulus-cleanup-health_check.service       static          -            
cumulus-cleanup-lttng_traces.service       static          -            
cumulus-core.service                       static          -
...
```

## Identify Essential Services

To identify which services must run when the switch boots:

```
cumulus@switch:~$ systemctl list-dependencies --before basic.target
```

To identify which services you need for networking:

<pre style="line-height: 1rem;">cumulus@switch:~$ systemctl list-dependencies --after network.target
<span style="color: #5cdd49;"> <strong>●</strong> </span> ├─switchd.service
<span style="color: #6a0900;"> <strong>●</strong> </span> └─network-pre.target</pre>

To identify the services needed for a multi-user environment, run:

<pre style="line-height: 1rem;">cumulus@switch:~$ systemctl list-dependencies --before multi-user.target

 ●  ├─bootlog.service
<span style="color: #6a0900;"> <strong>●</strong> </span> ├─systemd-readahead-done.service
<span style="color: #6a0900;"> <strong>●</strong> </span> ├─systemd-readahead-done.timer
<span style="color: #6a0900;"> <strong>●</strong> </span> ├─systemd-update-utmp-runlevel.service
<span style="color: #6a0900;"> <strong>●</strong> </span> └─graphical.target
<span style="color: #6a0900;"> <strong>●</strong> </span> └─systemd-update-utmp-runlevel.service</pre>

### Important Services

The following table lists the most important services in Cumulus Linux.
<!-- vale off -->
|Service Name|Description|Affects Forwarding?|
|------------ |-----------|-------------------|
|`switchd`|Hardware abstraction daemon. Synchronizes the kernel with the ASIC.|YES|
|`sx_sdk`|Interfaces with the Spectrum ASIC. Only on Spectrum switches.|YES|
|`frr`|{{<link url="FRRouting" text="FRR">}}. Handles routing protocols. There are separate processes for each routing protocol, such as `bgpd` and `ospfd`.|YES if routing|
|`clagd`|Cumulus link aggregation daemon. Handles {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG">}}.|YES if using MLAG|
|`neighmgrd`|Keeps neighbor entries refreshed, snoops on ARP and ND packets if ARP suppression is on, and refreshes VRR MAC addresses.|YES|
|`mstpd`|{{<link url="Spanning-Tree-and-Rapid-Spanning-Tree-STP" text="Spanning tree protocol">}} daemon.|YES if using layer 2|
|`ptmd`|{{<link url="Prescriptive-Topology-Manager-PTM" text="Prescriptive Topology Manager">}}. Verifies cabling based on {{<link url="Link-Layer-Discovery-Protocol" text="LLDP">}} output. Also sets up {{<link url="Bidirectional-Forwarding-Detection-BFD" text="BFD">}} sessions.|YES if using BFD|
|`nvued`| Handles the NVUE object model.|NO|
|`rsyslog`|Handles logging of syslog messages.|NO|
|`ntp`|{{<link url="Network-Time-Protocol-NTP" text="Network time protocol">}}.|NO|
|`ledmgrd`|{{<link url="Network-Switch-Port-LED-and-Status-LED-Guidelines" text="LED manager">}}. Reads the state of system LEDs.|NO|
|`sysmonitor`|Watches and logs critical system load (free memory, disk, CPU).|NO|
|`lldpd`|Handles Tx/Rx of {{<link url="Link-Layer-Discovery-Protocol" text="LLDP">}} information.|NO|
|`smond`|Reads {{<link url="Monitoring-System-Hardware" text="platform sensors and fan information">}} from pwmd.|NO|
|`pwmd`|Reads and sets fan speeds.|NO|

## Limit Resources for Services

You can configure a limit on memory and CPU usage for the following services to divide hardware resources up among applications and users, increasing overall efficiency.
- SNMP
- DHCP Server
- DHCP relay
- NTP
- syslog

To configure a limit on CPU usage, run the `nv set service control <service-name-id> resource-limit cpu <percent>` command.

The following example configures the syslog service to limit CPU usage to 60 percent:

```
cumulus@switch:~$ nv set service control rsyslog resource-limit cpu 60
cumulus@switch:~$ nv config apply
```

To configure a limit on memory usage, run the `nv set service control <service-name-id> resource-limit memory <size>` command.

The following example configures the DHCP service to limit memory usage to 6700M:

```
cumulus@switch:~$ nv set service control dhcpd resource-limit memory 6700M
cumulus@switch:~$ nv config apply
```

A value of 100 configures no limit on CPU usage for the service.

To show the current CPU and memory usage for all services, run the `nv show service control` command:

```
cumulus@switch:~$ nv show service control
```

To show the current CPU and memory usage for a specific service, run the `nv show service control <service>` command:

```
cumulus@switch:~$ nv show service control rsyslog
```

To show the configured resource limits for a specific service, run the `nv show service control <service-name-id> resource-limit` command:

```
cumulus@switch:~$ nv show service control rsyslog resource-limit
```

<!-- vale on -->