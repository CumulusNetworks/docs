---
title: Managing Application Daemons
author: Cumulus Networks
weight: 39
aliases:
 - /display/RMP31/Managing+Application+Daemons
 - /pages/viewpage.action?pageId=5122748
pageID: 5122748
product: Cumulus RMP
version: 3.1.2
imgData: cumulus-rmp-312
siteSlug: cumulus-rmp-312
---
You manage application daemons in Cumulus RMP in the following ways:

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
    also get restarted. For example, running `systemctl restart zebra`
    restarts any of the routing protocol daemons that are enabled and
    running, such as `bgpd` or `ospfd`.

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

    cumulus@switch:~/etc:~$ sudo ls -l rc*.d | grep <daemon name>

For example:

    cumulus@switch:~/etc$ sudo ls -l rc*.d | grep snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 S01snmpd -> ../init.d/snmpd
    lrwxrwxrwx 1 root root 15 Apr 4 2014 K02snmpd -> ../init.d/snmpd
