---
title: Managing Application Daemons
author: Cumulus Networks
weight: 71
aliases:
 - /display/CL332/Managing+Application+Daemons
 - /pages/viewpage.action?pageId=5868898
pageID: 5868898
product: Cumulus Linux
version: 3.3.2
imgData: cumulus-linux-332
siteSlug: cumulus-linux-332
---
<details>

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

    cumulus@switch:~$ sudo systemctl start | stop | restart | status | reload | enable | disable | reenable SERVICENAME.service

For example to restart networking, run the command:

    cumulus@switch:~$ sudo systemctl restart networking.service

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

    cumulus@switch:~$ cl-service-summary
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

You can also run `systemctl list-unit-files --type service` to list all
services on the switch and see which ones are enabled:

<summary>Click here to see output of this command ... </summary>

    cumulus@switch:~$ systemctl list-unit-files --type service
    UNIT FILE                              STATE   
    aclinit.service                        enabled 
    acltool.service                        enabled 
    acpid.service                          disabled
    arp_refresh.service                    enabled 
    auditd.service                         enabled 
    autovt@.service                        disabled
    bootlog.service                        enabled 
    bootlogd.service                       masked  
    bootlogs.service                       masked  
    bootmisc.service                       masked  
    checkfs.service                        masked  
    checkroot-bootclean.service            masked  
    checkroot.service                      masked  
    clagd.service                          enabled 
    clcmd.service                          enabled 
    console-getty.service                  disabled
    console-shell.service                  disabled
    container-getty@.service               static  
    cron.service                           enabled 
    cryptdisks-early.service               masked  
    cryptdisks.service                     masked  
    cumulus-aclcheck.service               static  
    cumulus-core.service                   static  
    cumulus-fastfailover.service           enabled 
    cumulus-firstboot.service              disabled
    cumulus-platform.service               enabled 
    cumulus-support.service                static  
    dbus-org.freedesktop.hostname1.service static  
    dbus-org.freedesktop.locale1.service   static  
    dbus-org.freedesktop.login1.service    static  
    dbus-org.freedesktop.machine1.service  static  
    dbus-org.freedesktop.timedate1.service static  
    dbus.service                           static  
    debian-fixup.service                   static  
    debug-shell.service                    disabled
    decode-syseeprom.service               static  
    dhcpd.service                          disabled
    dhcpd6.service                         disabled
    dhcpd6@.service                        disabled
    dhcpd@.service                         disabled
    dhcrelay.service                       enabled 
    dhcrelay6.service                      disabled
    dhcrelay6@.service                     disabled
    dhcrelay@.service                      disabled
    dm-event.service                       disabled
    dns-watcher.service                    disabled
    dnsmasq.service                        enabled 
    emergency.service                      static  
    fuse.service                           masked  
    getty-static.service                   static  
    getty@.service                         enabled 
    halt-local.service                     static  
    halt.service                           masked  
    heartbeat-failed@.service              static  
    hostname.service                       masked  
    hsflowd.service                        enabled 
    hsflowd@.service                       enabled 
    hwclock-save.service                   enabled 
    hwclock.service                        masked  
    hwclockfirst.service                   masked  
    ifup@.service                          static  
    initrd-cleanup.service                 static  
    initrd-parse-etc.service               static  
    initrd-switch-root.service             static  
    initrd-udevadm-cleanup-db.service      static  
    killprocs.service                      masked  
    kmod-static-nodes.service              static  
    kmod.service                           static  
    ledmgrd.service                        enabled 
    lldpd.service                          enabled 
    lm-sensors.service                     enabled 
    lvm2-activation-early.service          enabled 
    lvm2-activation.service                enabled 
    lvm2-lvmetad.service                   static  
    lvm2-monitor.service                   enabled 
    lvm2-pvscan@.service                   static  
    lvm2.service                           disabled
    module-init-tools.service              static  
    motd.service                           masked  
    mountall-bootclean.service             masked  
    mountall.service                       masked  
    mountdevsubfs.service                  masked  
    mountkernfs.service                    masked  
    mountnfs-bootclean.service             masked  
    mountnfs.service                       masked  
    mstpd.service                          enabled 
    netd.service                           enabled 
    netq-agent.service                     disabled
    networking.service                     enabled 
    ntp.service                            enabled 
    ntp@.service                           disabled
    openvswitch-vtep.service               disabled
    phy-ucode-update.service               enabled 
    portwd.service                         enabled 
    procps.service                         static  
    ptmd.service                           enabled 
    pwmd.service                           enabled 
    quagga.service                         enabled 
    quotaon.service                        static  
    rc-local.service                       static  
    rc.local.service                       static  
    rdnbrd.service                         disabled
    reboot.service                         masked  
    rescue.service                         static  
    rmnologin.service                      masked  
    rsyslog.service                        enabled 
    screen-cleanup.service                 masked  
    sendsigs.service                       masked  
    serial-getty@.service                  disabled
    single.service                         masked  
    smond.service                          enabled 
    snmpd.service                          disabled
    snmpd@.service                         disabled
    snmptrapd.service                      disabled
    snmptrapd@.service                     disabled
    ssh.service                            enabled 
    ssh@.service                           disabled
    sshd.service                           enabled 
    stop-bootlogd-single.service           masked  
    stop-bootlogd.service                  masked  
    stopssh.service                        enabled 
    sudo.service                           disabled
    switchd-diag.service                   static  
    switchd.service                        enabled 
    syslog.service                         enabled 
    sysmonitor.service                     static  
    systemd-ask-password-console.service   static  
    systemd-ask-password-wall.service      static  
    systemd-backlight@.service             static  
    systemd-binfmt.service                 static  
    systemd-fsck-root.service              static  
    systemd-fsck@.service                  static  
    systemd-halt.service                   static  
    systemd-hibernate.service              static  
    systemd-hostnamed.service              static  
    systemd-hybrid-sleep.service           static  
    systemd-initctl.service                static  
    systemd-journal-flush.service          static  
    systemd-journald.service               static  
    systemd-kexec.service                  static  
    systemd-localed.service                static  
    systemd-logind.service                 static  
    systemd-machined.service               static  
    systemd-modules-load.service           static  
    systemd-networkd-wait-online.service   disabled
    systemd-networkd.service               disabled
    systemd-nspawn@.service                disabled
    systemd-poweroff.service               static  
    systemd-quotacheck.service             static  
    systemd-random-seed.service            static  
    systemd-readahead-collect.service      disabled
    systemd-readahead-done.service         static  
    systemd-readahead-drop.service         disabled
    systemd-readahead-replay.service       disabled
    systemd-reboot.service                 static  
    systemd-remount-fs.service             static  
    systemd-resolved.service               disabled
    systemd-rfkill@.service                static  
    systemd-setup-dgram-qlen.service       static  
    systemd-shutdownd.service              static  
    systemd-suspend.service                static  
    systemd-sysctl.service                 static  
    systemd-timedated.service              static  
    systemd-timesyncd.service              disabled
    systemd-tmpfiles-clean.service         static  
    systemd-tmpfiles-setup-dev.service     static  
    systemd-tmpfiles-setup.service         static  
    systemd-udev-settle.service            static  
    systemd-udev-trigger.service           static  
    systemd-udevd.service                  static  
    systemd-update-utmp-runlevel.service   static  
    systemd-update-utmp.service            static  
    systemd-user-sessions.service          static  
    udev-finish.service                    static  
    udev.service                           static  
    umountfs.service                       masked  
    umountnfs.service                      masked  
    umountroot.service                     masked  
    update-ports.service                   enabled 
    urandom.service                        static  
    user@.service                          static  
    uuidd.service                          static  
    vboxadd-service.service                enabled 
    vboxadd-x11.service                    enabled 
    vboxadd.service                        enabled 
    vxrd.service                           disabled
    vxsnd.service                          disabled
    wd_keepalive.service                   enabled 
    x11-common.service                     masked  
    ztp-init.service                       enabled 
    ztp.service                            disabled
    191 unit files listed.
    lines 147-194/194 (END)

## <span>Identifying Essential Services</span>

If you need to know which services are required to run when the switch
boots, run:

    cumulus@switch:~$ sudo systemctl list-dependencies --before basic.target

To see which services are needed for networking, run:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>cumulus@switch:~$ sudo systemctl list-dependencies --after network.target
network.target</code></pre>
<p><span style="color: #5cdd49;"> <strong>●</strong> </span> <code>├─networking.service</code><br />
<span style="color: #5cdd49;"> <strong>●</strong> </span> <code>├─switchd.service</code><br />
<span style="color: #5cdd49;"> <strong>●</strong> </span> <code>├─wd_keepalive.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>└─network-pre.target</code></p></td>
</tr>
</tbody>
</table>

To identify the services needed for a multi-user environment, run:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>cumulus@leaf01:~$ sudo systemctl list-dependencies --before multi-user.target
multi-user.target</code></pre>
<p><span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─bootlog.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─systemd-readahead-done.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─systemd-readahead-done.timer</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─systemd-update-utmp-runlevel.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>└─graphical.target</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>└─systemd-update-utmp-runlevel.service</code></p></td>
</tr>
</tbody>
</table>

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
