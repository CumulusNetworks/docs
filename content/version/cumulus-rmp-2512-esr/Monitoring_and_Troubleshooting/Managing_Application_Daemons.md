---
title: Managing Application Daemons
author: Cumulus Networks
weight: 97
aliases:
 - /display/RMP25ESR/Managing+Application+Daemons
 - /pages/viewpage.action?pageId=5116328
pageID: 5116328
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
You manage application daemons in Cumulus RMP in the following ways:

  - Identifying active listener ports

  - Identifying daemons currently active or stopped

  - Identifying boot time state of a specific daemon

  - Disabling or enabling a specific daemon

## <span>Identifying Active Listener Ports for IPv4 and IPv6</span>

You can identify the active listener ports under both IPv4 and IPv6
using the `lsof` command:

    cumulus@switch:~$ sudo lsof -Pnl +M -i4
    COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
    ntpd 1882 104 16u IPv4 3954 0t0 UDP *:123
    ntpd 1882 104 18u IPv4 3963 0t0 UDP 127.0.0.1:123
    ntpd 1882 104 19u IPv4 3964 0t0 UDP 192.168.8.37:123
    snmpd 1987 105 8u IPv4 5423 0t0 UDP *:161
    zebra 1993 103 10u IPv4 5151 0t0 TCP 127.0.0.1:2601 (LISTEN)
    sshd 2496 0 3u IPv4 5809 0t0 TCP *:22 (LISTEN)
    jdoo 2622 0 6u IPv4 6132 0t0 TCP 127.0.0.1:2812 (LISTEN)
    sshd 31700 0 3r IPv4 187630 0t0 TCP 192.168.8.37:22->192.168.8.3:50386 (ESTABLISHED)
    
    cumulus@switch:~$ sudo lsof -Pnl +M -i6
    COMMAND PID USER FD TYPE DEVICE SIZE/OFF NODE NAME
    ntpd 1882 104 17u IPv6 3955 0t0 UDP *:123
    ntpd 1882 104 20u IPv6 3965 0t0 UDP [::1]:123
    ntpd 1882 104 21u IPv6 3966 0t0 UDP [fe80::7272:cfff:fe96:6639]:123
    sshd 2496 0 4u IPv6 5811 0t0 TCP *:22 (LISTEN)

## <span>Identifying Daemons Currently Active or Stopped</span>

To determine which daemons are currently active or stopped, use the
`service` --`status-all` command, then pipe the results to `grep`, using
the - or + operators:

    cumulus@switch:~$ sudo service --status-all | grep +
     [ ? ] aclinit
     [ + ] arp_refresh
     [ + ] auditd
     ...
    
    cumulus@switch:~$ sudo service --status-all | grep -
     [ - ] isc-dhcp-server
     [ - ] openvswitch-vtep
     [ - ] ptmd
     ...

## <span>Identifying Boot Time State of a Specific Daemon</span>

The `ls` command can provide the boot time state of a daemon. A file
link with a name starting with **S** identifies a boot-time-enabled
daemon. A file link with a name starting with **K** identifies a
disabled daemon.

> [cumulus@switch](mailto:cumulus%40switch):\~/etc$ sudo ls -l rc\*.d |
> grep \<daemon name\>

For example:

    cumulus@switch:~/etc$ sudo ls -l rc*.d | grep snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd

## <span>Disabling or Enabling a Specific Daemon</span>

To enable or disable a specific daemon, run:

    cumulus@switch:~$ update-rc.d <daemon> disable | enable

For example:

    cumulus@switch:~/etc$ sudo update-rc.d snmpd disable
    update-rc.d: using dependency based boot sequencing
    insserv: warning: current start runlevel(s) (empty) of script `snmpd' overrides LSB defaults (2 3 4 5).
    insserv: warning: current stop runlevel(s) (0 1 2 3 4 5 6) of script `snmpd' overrides LSB defaults (0 1 6).
    insserv: warning: current start runlevel(s) (empty) of script `snmpd' overrides LSB defaults (2 3 4 5).
    insserv: warning: current stop runlevel(s) (0 1 2 3 4 5 6) of script `snmpd' overrides LSB defaults (0 1 6).
    
    
    cumulus@switch:~/etc$ sudo ls -l rc*.d | grep snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    
    
    cumulus@switch:~/etc$ sudo update-rc.d snmpd enable
    update-rc.d: using dependency based boot sequencing
    
    
    cumulus@switch:~/etc$ sudo ls -l rc*.d | grep snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Feb 13 17:35 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
