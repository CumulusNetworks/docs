---
title: Services and Daemons in Cumulus Linux
author: Cumulus Networks
weight: 71
aliases:
 - /display/DOCS/Services+and+Daemons+in+Cumulus+Linux
 - /pages/viewpage.action?pageId=8362578
pageID: 8362578
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
*Services* (also known as *daemons*) and *processes* are at the heart of
how a Linux system functions. Most of the time a service takes care of
itself; you just enable and start it, then let it run. However, because
a Cumulus Linux switch is a Linux system, you have the ability to dig
deeper if you like. Services may start multiple processes as they run.
Services tend to be the most important things to monitor on a Cumulus
Linux switch.

You manage services in Cumulus Linux in the following ways:

  - Identify currently active or stopped services

  - Identify boot time state of a specific service

  - Disable or enable a specific service

  - Identify active listener ports

## <span>systemd and the systemctl Command</span>

In general, you manage services using `systemd` via the `systemctl`
command. You use it with any service on the switch to start, stop,
restart, reload, enable, disable, reenable, or get the status of the
service.

    cumulus@switch:~$ sudo systemctl start | stop | restart | status | reload | enable | disable | reenable SERVICENAME.service

For example to restart networking, run the command:

    cumulus@switch:~$ sudo systemctl restart networking.service

{{%notice note%}}

Unlike the `service` command in Debian Wheezy, the service name is
written **after** the `systemctl` subcommand, not before it.

{{%/notice%}}

To see all the currently running services, run:

    cumulus@switch:~$ sudo systemctl status
    ● switch
        State: running
         Jobs: 0 queued
       Failed: 0 units
        Since: Thu 2019-01-10 00:19:34 UTC; 23h ago
       CGroup: /
               ├─1 /sbin/init
               └─system.slice
                 ├─dbus.service
                 │ └─403 /usr/bin/dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation
                 ├─uuidd.service
                 │ └─669 /usr/sbin/uuidd --socket-activation
                 ├─cron.service
                 │ └─381 /usr/sbin/cron -f -L 38
                 ├─smond.service
                 │ └─606 /usr/bin/python /usr/sbin/smond
                 ├─switchd.service
                 │ └─587 /usr/sbin/switchd -vx
                 ├─ledmgrd.service
                 │ └─613 /usr/bin/python /usr/sbin/ledmgrd
                 ├─wd_keepalive.service
                 │ └─433 /usr/sbin/wd_keepalive 
                 ├─netq-agent.service
                 │ └─915 /usr/bin/python /usr/sbin/netq-agent
                 ├─ptmd.service
                 │ └─914 /usr/sbin/ptmd -l INFO
                 ├─networking.service
                 │ ├─729 /sbin/dhclient -pf /run/dhclient.vagrant.pid -lf /var/lib/dhcp/dhclient.vagrant.leases vagrant
                 │ └─828 /sbin/dhclient -pf /run/dhclient.eth0.pid -lf /var/lib/dhcp/dhclient.eth0.leases eth0
                 ├─nginx.service
                 │ ├─449 nginx: master process /usr/sbin/nginx -g daemon on; master_process on
                 │ ├─450 nginx: worker process                           
                 │ ├─451 nginx: worker process                           
                 │ ├─452 nginx: worker process                           
                 │ └─453 nginx: worker process                           
                 ├─sysmonitor.service
                 │ ├─ 847 /bin/bash /usr/lib/cumulus/sysmonitor
                 │ └─7717 sleep 60
                 ├─system-serial\x2dgetty.slice
                 │ └─serial-getty@ttyS0.service
                 │   └─920 /sbin/agetty --keep-baud 115200 38400 9600 ttyS0 vt102
                 ├─neighmgrd.service
                 │ └─844 /usr/bin/python /usr/bin/neighmgrd
                 ├─systemd-journald.service
                 │ └─252 /lib/systemd/systemd-journald
                 ├─netqd.service
                 │ └─846 /usr/bin/python /usr/sbin/netqd --daemon
                 ├─auditd.service
                 │ └─337 /sbin/auditd -n
                 ├─pwmd.service
                 │ └─614 /usr/bin/python /usr/sbin/pwmd
                 ├─netd.service
                 │ └─845 /usr/bin/python -O /usr/sbin/netd -d
                 ├─ssh.service
                 │ ├─ 937 /usr/sbin/sshd -D
                 │ ├─6893 sshd: cumulus [priv]
                 │ ├─6911 sshd: cumulus@pts/0 
                 │ ├─6912 -bash
                 │ ├─7747 sudo systemctl status
                 │ ├─7752 systemctl status
                 │ └─7753 pager
                 ├─systemd-logind.service
                 │ └─405 /lib/systemd/systemd-logind
                 ├─system-getty.slice
                 │ └─getty@tty1.service
                 │   └─435 /sbin/agetty --noclear tty1 linux
                 ├─systemd-udevd.service
                 │ └─254 /lib/systemd/systemd-udevd
                 ├─mcelog.service
                 │ └─438 /usr/sbin/mcelog --ignorenodev --daemon --foreground
                 ├─portwd.service
                 │ └─603 /usr/bin/python /usr/sbin/portwd
                 ├─lldpd.service
                 │ ├─911 lldpd: monitor.        
                 │ └─936 lldpd: connected to oob-mgmt-switch
                 ├─rsyslog.service
                 │ └─392 /usr/sbin/rsyslogd -n
                 ├─ntp.service
                 │ └─912 /usr/sbin/ntpd -n -u ntp:ntp -g
                 ├─acpid.service
                 │ └─390 /usr/sbin/acpid
                 └─mstpd.service
                   └─436 /sbin/mstpd -d -v2

### <span>systemctl Subcommands</span>

`systemctl` has a number of subcommands that perform a specific
operation on a given service.

  - **status**: Returns the status of the specified service.

  - **start**: Starts the service.

  - **stop**: Stops the service.

  - **restart**: Stops, then starts the service, all the while
    maintaining state. So if there are dependent services or services
    that mark the restarted service as *Required*, the other services
    also get restarted. For example, running `systemctl restart
    frr.service` restarts any of the routing protocol services that are
    enabled and running, such as `bgpd` or `ospfd`.

  - **reload**: Reloads a service's configuration.

  - **enable**: Enables the service to start when the system boots, but
    does not start it unless you use the `systemctl start
    SERVICENAME.service` command or reboot the switch.

  - **disable**: Disables the service, but does not stop it unless you
    use the `systemctl stop SERVICENAME.service` command or reboot the
    switch. A disabled service can still be started or stopped.

  - **reenable**: Disables, then enables a service. You might need to do
    this so that any new *Wants* or *WantedBy* lines create the symlinks
    necessary for ordering. This has no side effects on other services.

There is often little reason to interact with the services directly
using these commands. If a critical service should happen to crash or
hit an error it will be automatically respawned by systemd. Systemd is
effectively the caretaker of services in modern Linux systems and is
responsible for starting all the necessary services at boot time.

### <span>Ensure a Service Starts after Multiple Restarts</span>

By default, `systemd` is configured to try to restart a particular
service only a certain number of times within a given interval before
the service fails to start at all. The settings for this are stored in
the service script. The settings are *StartLimitInterval* (which
defaults to 10 seconds) and *StartBurstLimit* (which defaults to 5
attempts), but many services override these defaults, sometimes with
much longer times. `switchd.service`, for example, sets
*StartLimitInterval=10m* and *StartBurstLimit=3*, which means if you
restart switchd more than 3 times in 10 minutes, it does not start.

When the restart fails for this reason, a message similar to the
following appears:

    Job for switchd.service failed. See 'systemctl status switchd.service' and 'journalctl -xn' for details.

And `systemctl status switchd.service` shows output similar to:

    Active: failed (Result: start-limit) since Thu 2016-04-07 21:55:14 UTC; 15s ago

To clear this error, run `systemctl reset-failed switchd.service`. If
you know you are going to restart frequently (multiple times within the
StartLimitInterval), you can run the same command before you issue the
restart request. This also applies to stop followed by start.

### <span>Keep systemd Services from Hanging after Starting</span>

If you start, restart, or reload any `systemd` service that can be
started from another `systemd` service, you must use the `--no-block`
option with `systemctl`. Otherwise, that service or even the switch
itself might hang after starting or restarting.

## <span>Identify Active Listener Ports for IPv4 and IPv6</span>

You can identify the active listener ports under both IPv4 and IPv6
using the `netstat` command:

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

## <span>Identify Services Currently Active or Stopped</span>

To determine which services are currently active or stopped, run the
`cl-service-summary` command:

    cumulus@switch:~$ cl-service-summary
    Service cron               enabled    active   
    Service ssh                enabled    active   
    Service syslog             enabled    active   
    Service asic-monitor       enabled    inactive 
    Service clagd              enabled    inactive 
    Service cumulus-poe                   inactive 
    Service lldpd              enabled    active   
    Service mstpd              enabled    active   
    Service neighmgrd          enabled    active   
    Service netd               enabled    active   
    Service netq-agent         enabled    active   
    Service ntp                enabled    active   
    Service portwd             enabled    active   
    Service ptmd               enabled    active   
    Service pwmd               enabled    active   
    Service smond              enabled    active   
    Service switchd            enabled    active   
    Service sysmonitor         enabled    active   
    Service vxrd               disabled   inactive 
    Service vxsnd              disabled   inactive 
    Service rdnbrd             disabled   inactive 
    Service frr                enabled    inactive 
    Service bgpd               disabled   inactive 
    Service eigrpd             disabled   inactive 
    Service isisd              disabled   inactive 
    Service ldpd               disabled   inactive 
    Service nhrpd              disabled   inactive 
    Service ospf6d             disabled   inactive 
    Service ospfd              disabled   inactive 
    Service pbrd               disabled   inactive 
    Service pimd               disabled   inactive 
    Service ripd               disabled   inactive 
    Service ripngd             disabled   inactive 
    Service zebra              disabled   inactive 

You can also run the `systemctl list-unit-files --type service` command
to list all services on the switch and see which ones are enabled:

Click here to see output of this command ...

    cumulus@switch:~$ systemctl list-unit-files --type service
    UNIT FILE                              STATE   
    aclinit.service                        enabled 
    acltool.service                        enabled 
    acpid.service                          disabled
    asic-monitor.service                   enabled 
    auditd.service                         enabled 
    autovt@.service                        disabled
    bmcd.service                           disabled
    bootlog.service                        enabled 
    bootlogd.service                       masked  
    bootlogs.service                       masked  
    bootmisc.service                       masked  
    checkfs.service                        masked  
    checkroot-bootclean.service            masked  
    checkroot.service                      masked  
    clagd.service                          enabled 
    console-getty.service                  disabled
    console-shell.service                  disabled
    container-getty@.service               static  
    cron.service                           enabled 
    cryptdisks-early.service               masked  
    cryptdisks.service                     masked  
    cumulus-aclcheck.service               static  
    cumulus-chassis-ssh.service            disabled
    cumulus-chassisd.service               disabled
    cumulus-core.service                   static  
    cumulus-fastfailover.service           enabled 
    cumulus-firstboot.service              disabled
    cumulus-hyperconverged.service         disabled
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
    dhcrelay.service                       disabled
    dhcrelay6.service                      disabled
    dhcrelay6@.service                     disabled
    dhcrelay@.service                      disabled
    dm-event.service                       disabled
    dns-watcher.service                    disabled
    dnsmasq.service                        disabled
    emergency.service                      static  
    frr.service                            enabled 
    fuse.service                           masked  
    getty-static.service                   static  
    getty@.service                         enabled 
    halt-local.service                     static  
    halt.service                           masked  
    heartbeat-failed@.service              static  
    hostapd.service                        disabled
    hostname.service                       masked  
    hsflowd.service                        disabled
    hsflowd@.service                       disabled
    hwclock-save.service                   enabled 
    hwclock.service                        masked  
    hwclockfirst.service                   masked  
    ifup@.service                          static  
    initrd-cleanup.service                 static  
    initrd-parse-etc.service               static  
    initrd-switch-root.service             static  
    initrd-udevadm-cleanup-db.service      static  
    ipmievd.service                        disabled
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
    mcelog.service                         enabled 
    module-init-tools.service              static  
    motd.service                           masked  
    mountall-bootclean.service             masked  
    mountall.service                       masked  
    mountdevsubfs.service                  masked  
    mountkernfs.service                    masked  
    mountnfs-bootclean.service             masked  
    mountnfs.service                       masked  
    mstp_bridge.service                    enabled 
    mstpd.service                          enabled 
    neighmgrd.service                      enabled 
    netd.service                           enabled 
    netq-agent.service                     enabled 
    netq-agent@.service                    disabled
    netq-notifier.service                  disabled
    netq-notifier@.service                 disabled
    netqd.service                          enabled 
    netqd@.service                         disabled
    networking.service                     enabled 
    nginx.service                          enabled 
    ntp.service                            enabled 
    ntp@.service                           disabled
    open-vm-tools.service                  enabled 
    openvswitch-vtep.service               disabled
    phc2sys.service                        disabled
    phy-ucode-update.service               enabled 
    portwd.service                         enabled 
    procps.service                         static  
    ptmd.service                           enabled 
    ptp4l.service                          disabled
    pwmd.service                           enabled 
    quotaon.service                        static  
    rc-local.service                       static  
    rc.local.service                       static  
    rdnbrd.service                         disabled
    reboot.service                         masked  
    rescue.service                         static  
    restserver.service                     disabled
    rmnologin.service                      masked  
    rsyslog.service                        enabled 
    screen-cleanup.service                 masked  
    sendsigs.service                       masked  
    serial-getty@.service                  disabled
    single.service                         masked  
    smartd.service                         masked  
    smartmontools.service                  disabled
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
    sysmonitor.service                     enabled 
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
    ztp.service                            disabled
    210 unit files listed.
    lines 165-213/213 (END)

## <span>Identify Essential Services</span>

If you need to know which services are required to run when the switch
boots, run:

    cumulus@switch:~$ systemctl list-dependencies --before basic.target

To see which services are needed for networking, run:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><pre><code>cumulus@switch:~$ systemctl list-dependencies --after network.target</code></pre>
<p><span style="color: #5cdd49;"> <strong>●</strong> </span> <code>├─switchd.service</code><br />
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
<td><pre><code>cumulus@switch:~$ systemctl list-dependencies --before multi-user.target</code></pre>
<p><code>● ├─bootlog.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─systemd-readahead-done.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─systemd-readahead-done.timer</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>├─systemd-update-utmp-runlevel.service</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>└─graphical.target</code><br />
<span style="color: #6a0900;"> <strong>●</strong> </span> <code>└─systemd-update-utmp-runlevel.service</code></p></td>
</tr>
</tbody>
</table>

### <span>Important Services</span>

The following table lists the most important services in Cumulus Linux.

| Service Name | Description                                                                                                                                                                                                                                                                                                 | Affects Forwarding?                          |
| ------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| switchd      | Hardware abstraction daemon, synchronizes the kernel with the ASIC.                                                                                                                                                                                                                                         | YES                                          |
| sx\_sdk      | Only on Mellanox switches, interfaces with the Spectrum ASIC.                                                                                                                                                                                                                                               | YES                                          |
| portwd       | Reads pluggable information over the I2C bus. Identifies and classifies the optics that are inserted into the system. Sets interface speeds and capabilities to match the optics.                                                                                                                           | YES, eventually, if optics are added/removed |
| frr          | [FRRouting](/cumulus-linux/Layer_3/FRRouting_Overview/), handles routing protocols. There are separate processes for each routing protocol, like bgpd and ospfd.                                                                                                                                            | YES if routing                               |
| clag         | Cumulus link aggregation daemon, handles [MLAG](/cumulus-linux/Layer_2/Multi-Chassis_Link_Aggregation_-_MLAG).                                                                                                                                                                                              | YES if using MLAG                            |
| neighmgrd    | Synchronizes MAC address information when MLAG is in use.                                                                                                                                                                                                                                                   | YES if using MLAG                            |
| mstpd        | [Spanning tree protocol](/cumulus-linux/Layer_2/Spanning_Tree_and_Rapid_Spanning_Tree) daemon.                                                                                                                                                                                                              | YES if using layer 2                         |
| ptmd         | [Prescriptive Topology Manager](/cumulus-linux/Layer_1_and_Switch_Ports/Prescriptive_Topology_Manager_-_PTM), verifies cabling based on [LLDP](/cumulus-linux/Layer_2/Link_Layer_Discovery_Protocol/) output, also sets up [BFD](/cumulus-linux/Layer_3/Bidirectional_Forwarding_Detection_-_BFD) sessions. | YES if using BFD                             |
| netd         | [NCLU](/cumulus-linux/System_Configuration/Network_Command_Line_Utility_-_NCLU) back end.                                                                                                                                                                                                                   | NO                                           |
| rsyslog      | Handles logging of syslog messages.                                                                                                                                                                                                                                                                         | NO                                           |
| ntp          | [Network time protocol](/cumulus-linux/System_Configuration/Setting_Date_and_Time).                                                                                                                                                                                                                         | NO                                           |
| ledmgrd      | [LED manager](/cumulus-linux/Monitoring_and_Troubleshooting/Monitoring_System_Hardware/Network_Switch_Port_LED_and_Status_LED_Guidelines), reads the state of system LEDs.                                                                                                                                  | NO                                           |
| sysmonitor   | Watches and logs critical system load (free memory, disk, CPU).                                                                                                                                                                                                                                             | NO                                           |
| lldpd        | Handles Tx/Rx of [LLDP](/cumulus-linux/Layer_2/Link_Layer_Discovery_Protocol/) information.                                                                                                                                                                                                                 | NO                                           |
| smond        | Reads [platform sensors and fan information](/cumulus-linux/Monitoring_and_Troubleshooting/Monitoring_System_Hardware/) from pwmd.                                                                                                                                                                          | NO                                           |
| pwmd         | Reads and sets fan speeds.                                                                                                                                                                                                                                                                                  | NO                                           |
