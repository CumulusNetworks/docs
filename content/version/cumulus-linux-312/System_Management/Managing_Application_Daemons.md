---
title: Managing Application Daemons
author: Cumulus Networks
weight: 63
aliases:
 - /display/CL31/Managing+Application+Daemons
 - /pages/viewpage.action?pageId=5121946
pageID: 5121946
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
You manage application daemons (services) in Cumulus Linux in the
following ways:

  - Identifying active listener ports

  - Identifying daemons currently active or stopped

  - Identifying boot time state of a specific daemon

  - Disabling or enabling a specific daemon

## <span>Using systemd and the systemctl Command</span>

In general, you manage services using `systemd` via the `systemctl`
command. You use it with any service on the switch to
start/stop/restart/reload/enable/disable/reenable or get the status of
the service.

    systemctl start | stop | restart | status | reload | enable | disable | reenable SERVICENAME.service

For example to restart networking, run the command:

    systemctl restart networking.service

{{%notice note%}}

Unlike the `service` command in Debian Wheezy, the service name is
written **after** the systemctl subcommand, not before it.

{{%/notice%}}

### <span>Understanding the systemctl Subcommands</span>

`systemctl` has a number of subcommands that perform a specific
operation on a given daemon.

  - **status**: Returns the status of the specified daemon.

  - **start**: Starts the daemon.

  - **stop**: Stops the daemon.

  - **restart**: Stops, then starts the daemon, all the while
    maintaining state. So if there are dependent services or services
    that mark the restarted service as *Required*, the other services
    also get restarted. For example, running `systemctl restart
    quagga.service` restarts any of the routing protocol daemons that
    are enabled and running, such as `bgpd` or `ospfd`.

  - **reload**: Reloads a daemon's configuration.

  - **enable**: Enables the daemon to start when the system boots, but
    does not start it unless you use the `systemctl start
    SERVICENAME.service` command or reboot the switch.

  - **disable**: Disables the daemon, but does not stop it unless you
    use the `systemctl stop SERVICENAME.service` command or reboot the
    switch. A disabled daemon can still be started or stopped.

  - **reenable**: Disables, then enables a daemon. You might need to do
    this so that any new *Wants* or *WantedBy* lines create the symlinks
    necessary for ordering. This has no side effects on other daemons.

### <span>Ensuring a Service Starts after Multiple Restarts</span>

By default, `systemd` is configured to try to restart a particular
service only a certain number of times within a given interval before
the service fails to start at all. The settings for this are stored in
the service script. The settings are *StartLimitInterval* (which
defaults to 10 seconds) and *StartBurstLimit* (which defaults to 5
attempts), but many services override these defaults, sometimes with
much longer times. `switchd.service`, for example, sets
*StartLimitInterval=10m* and *StartBurstLimit=3*, which means if you
restart switchd more than 3 times in 10 minutes, it will not start.

When the restart fails for this reason, a message similar to the
following appears:

    Job for switchd.service failed. See 'systemctl status switchd.service' and 'journalctl -xn' for details.

And `systemctl status switchd.service` shows output similar to:

    Active: failed (Result: start-limit) since Thu 2016-04-07 21:55:14 UTC; 15s ago

To clear this error, run `systemctl reset-failed switchd.service`. If
you know you are going to restart frequently (multiple times within the
StartLimitInterval), you can run the same command before you issue the
restart request. This also applies to stop followed by start.

### <span>Keeping systemd Services from Hanging after Starting</span>

If you start, restart or reload any `systemd` service that could be
started from another `systemd` service, you must use the `--no-block`
option with `systemctl`. Otherwise, that service or even the switch
itself may hang after starting or restarting.

## <span>Identifying Active Listener Ports for IPv4 and IPv6</span>

You can identify the active listener ports under both IPv4 and IPv6
using the `netstat` command:

    cumulus@switch:~$ sudo netstat -nlp --inet --inet6
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

## <span>Identifying Daemons Currently Active or Stopped</span>

To determine which daemons are currently active or stopped, run
`cl-service-summary`:

    cumulus@switch:~$ sudo cl-service-summary
    Service cron         enabled    active 
    Service ssh          enabled    active 
    Service syslog       enabled    active     
    Service arp_refresh  enabled    active   
    Service clagd        enabled    active   
    Service lldpd        enabled    active   
    Service mstpd        enabled    active   
    Service poed                    inactive 
    Service portwd                  inactive 
    Service ptmd         enabled    active   
    Service pwmd         enabled    active   
    Service smond        enabled    active   
    Service switchd      enabled    active   
    Service vxrd         disabled   inactive 
    Service vxsnd        disabled   inactive 
    Service bgpd         disabled   inactive 
    Service isisd        disabled   inactive 
    Service ospf6d       disabled   inactive 
    Service ospfd        disabled   inactive 
    Service rdnbrd       disabled   inactive 
    Service ripd         disabled   inactive 
    Service ripngd       disabled   inactive 
    Service zebra        disabled   inactive 

Another way to get this information is to use the `systemctl status`
command, then pipe the results to `grep`, using the - or + operators:

    cumulus@switch:~$ sudo systemctl status | grep +
     [ ? ] aclinit
     [ + ] arp_refresh
     [ + ] auditd
     ...
     
    cumulus@switch:~$ sudo systemctl status | grep -
     [ - ] isc-dhcp-server
     [ - ] openvswitch-vtep
     [ - ] ptmd
     ...

## <span>Identifying Boot Time State of a Specific Daemon</span>

The `ls` command can provide the boot time state of a daemon. A file
link with a name starting with **S** identifies a boot-time-enabled
daemon. A file link with a name starting with **K** identifies a
disabled daemon.

    cumulus@switch:~/etc$ sudo ls -l rc*.d | grep <daemon name>

For example:

    cumulus@switch:~/etc$ sudo ls -l rc*.d | grep snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
