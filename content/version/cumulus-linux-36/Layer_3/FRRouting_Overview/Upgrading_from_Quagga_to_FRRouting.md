---
title: Upgrading from Quagga to FRRouting
author: Cumulus Networks
weight: 425
aliases:
 - /display/CL36/Upgrading+from+Quagga+to+FRRouting
 - /pages/viewpage.action?pageId=8362388
pageID: 8362388
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
Cumulus Linux 3.4 and later releases replace Quagga with FRRouting. This
section outlines the upgrade process for users currently using Quagga.

{{%notice note%}}

These instructions only apply to upgrading to Cumulus Linux 3.4 or later
from releases earlier than 3.4. New image installations contain `frr`
instead of `quagga` or `quagga-compat`. If you are using any automation
tools to configure your network and are installing a new Cumulus Linux
image, make sure your automation tools refer to FRR and not to Quagga.

If you are upgrading Cumulus Linux using `apt-get upgrade`, existing
automation that references Quagga continues to work until you upgrade to
FRR. Once you perform the following upgrade steps, your automation
**must** reference FRR instead of Quagga.

{{%/notice%}}

{{%notice warning%}}

Upgrading to Cumulus Linux 3.4 or later results in both `quagga.service`
and `frr.service` being present on the system, until `quagga.service` is
removed. These services have been configured to conflict with each
other; starting one service automatically stops the other, as they
cannot run concurrently.

{{%/notice%}}

1.  Run the following commands to begin the upgrade process:
    
        cumulus@switch:~$ sudo -E apt-get update
        cumulus@switch:~$ sudo -E apt-get upgrade
    
    {{%notice note%}}
    
    At the end of the `apt-get upgrade` process, the output shows
    details of the upgrade process, regarding the Quagga to FRR
    switchover.
    
        Unpacking quagga-compat (1.0.0+cl3u15-1) ...                                                                                                                                                                                                                                                                                                                                                                                    [476/476]
        Selecting previously unselected package frr.
        Preparing to unpack .../frr_3.1+cl3u1_amd64.deb ...
        Unpacking frr (3.1+cl3u1) ...
        Processing triggers for man-db (2.7.0.2-5) ...
        Setting up frr (3.1+cl3u1) ...
        Setting up quagga-compat (1.0.0+cl3u15-1) ...
        +-----------------------------------------------------------------------------+
        | Your system has been upgraded to use Cumulus Linux's new routing protocol   |
        | suite, FRRouting. The 'quagga' package is now a dummy transitional package  |
        | and may be removed.                                                         |
        |                                                                             |
        | As part of this upgrade, please take note of the following information:     |
        |                                                                             |
        |  - The location of your configuration files has changed to /etc/frr.        |
        |    In order to enable a seamless transition, FRRouting will continue to     |
        |    read all configuration files from /etc/quagga until the transition is    |
        |    completed.                                                               |
        |                                                                             |
        |  - In the interest of stability, action is required on your part to         |
        |    complete the transition to FRRouting. For instructions on how to do      |
        |    this, please refer to the Cumulus Linux documentation.                   |
        +-----------------------------------------------------------------------------+
        Setting up quagga (1.0.0+cl3u14-1) ...
        Processing triggers for libc-bin (2.19-18+deb8u10) ...
        Creating post-apt snapshot... 245 done.
        root@dell-s6000-16:/etc#
    
    {{%/notice%}}

Once the upgrade process is completed, the switch is in the following
state:

    cumulus@switch:~$ sudo systemctl list-unit-files | grep "quagga\|frr"
    frr.service                            enabled
    quagga.service                         enabled
    cumulus@switch:~$ sudo systemctl status frr
    ● frr.service - Cumulus Linux FRR
       Loaded: loaded (/etc/systemd/system/frr.service; enabled)
       Active: inactive (dead) since Fri 2017-07-28 18:54:59 UTC; 3 days ago
    cumulus@switch:~$ sudo systemctl status quagga
    ● quagga.service - Quagga (Transitional)
       Loaded: loaded (/lib/systemd/system/quagga.service; enabled)
       Active: active (running) since Fri 2017-07-28 18:55:49 UTC; 3 days ago
      Process: 29436 ExecStop=/usr/lib/frr/quagga stop (code=exited, status=0/SUCCESS)
      Process: 29772 ExecStart=/usr/lib/frr/quagga start (code=exited, status=0/SUCCESS)
       CGroup: /system.slice/quagga.service
               ├─29791 /usr/lib/frr/zebra -s 90000000 --daemon -A 127.0.0.1 -q
               ├─29798 /usr/lib/frr/bgpd --daemon -A 127.0.0.1 -q
               ├─29805 /usr/lib/frr/ripd --daemon -A 127.0.0.1 -q
               ├─29812 /usr/lib/frr/ospfd --daemon -A 127.0.0.1 -q
               ├─29819 /usr/lib/frr/ospf6d --daemon -A ::1 -q
               └─29825 /usr/lib/frr/watchfrr -q -adz -r /usr/sbin/servicebBquaggabBrestartbB%s -s /usr/sbin/servicebBquaggabBstartbB%s -k /usr/sbin/servicebBquaggabBstopbB%s -b bB -t 90 zebra bgpd ripd ospfd ospf6d

The output below shows the FRR / Quagga package status:

    cumulus@switch:~$ dpkg -l quagga\* frr\*
    interacting with quagga
    rc  quagga                            1.0.0+cl3u14-1                               amd64        transitional package
    ii  quagga-compat                     1.0.0+cl3u15-1                               all          Quagga compatibility for FRRouting
    ii  frr                               3.1+cl3u1                                    amd64        BGP/OSPF/RIP routing daemon

{{%notice note%}}

Cumulus 3.4 and later releases do not support or implement
`python-clcmd`. While the package remains, the related commands have
been removed.

{{%/notice%}}

To complete the transition to FRR:

1.  Migrate all `/etc/quagga/*` files to `/etc/frr/*`.
    
    {{%notice warning%}}
    
    The `vtysh.conf` file should not be moved, as it is unlikely any
    configuration is in the file. However, if there is necessary
    configuration in place, copy the contents into
    `/etc/frr/vtysh.conf`.
    
    {{%/notice%}}

2.  Merge the current `Quagga.conf` file with the new `frr.conf` file.
    Keep the default configuration for `frr.conf` in place, and add the
    additional configuration sections from `Quagga.conf`.

3.  Enable the daemons needed for your installation in
    `/etc/frr/daemons`.

4.  Manually update the log file locations to `/var/log/frr` or
    `syslog`.

5.  Remove the compatibility package:
    
    {{%notice warning%}}
    
    This step stops the Quagga compatibility mode, causing routing to go
    down.
    
    {{%/notice%}}
    
        cumulus@switch:~$ sudo -E apt-get remove quagga quagga-compat quagga-doc
    
    {{%notice note%}}
    
    Removing the `quagga-compat` package also removes `quagga.service`.
    
    However, the `/etc/quagga` directory is not removed in this step, as
    it is left in place for reference.
    
    {{%/notice%}}

6.  Purge the Quagga packages:
    
        cumulus@switch:~$ sudo dpkg -P quagga quagga-compat
    
    {{%notice warning%}}
    
    This step deletes all Quagga configuration files. Please ensure you
    back up your configuration.
    
    {{%/notice%}}
    
    {{%notice warning%}}
    
    Cumulus Networks does not recommend reinstalling the `quagga` and
    `quagga-compat` packages once they have been removed. While they can
    be reinstalled to continue migration iterations, limited testing has
    taken place, and configuration issues may occur.
    
    {{%/notice%}}

7.  Start FRR without Quagga compatibility mode:
    
        cumulus@switch:~$ sudo systemctl start frr.service
        cumulus@switch:~$ sudo systemctl -l status frr.service

## <span>Troubleshooting</span>

If the `systemctl -l status frr` output shows an issue, edit the
configuration files to correct it, and repeat the process. If issues
persist, you can return to Quagga compatibility mode for further
testing:

    cumulus@switch:~$ sudo -E apt-get install quagga-compat
    cumulus@switch:~$ sudo systemctl stop frr.service
    cumulus@switch:~$ sudo systemctl disable frr.service

{{%notice note%}}

Several configuration migration iterations may be necessary to ensure
the configuration is behaving the same in both Quagga and FRR.

{{%/notice%}}

Once further testing is complete, run the following commands to reset
the FRR installation, and then repeat the steps from the beginning of
this section to upgrade to FRR:

    cumulus@switch:~$ sudo systemctl reset-failed frr.service
    cumulus@switch:~$ sudo systemctl enable frr.service
