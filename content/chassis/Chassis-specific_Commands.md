---
title: Chassis-specific Commands
author: Cumulus Networks
weight: 19
aliases:
 - /display/CHASSIS/Chassis-specific+Commands
 - /pages/viewpage.action?pageId=7766308
pageID: 7766308
product: Cumulus Chassis
version: '1.0'
imgData: chassis
siteSlug: chassis
---
In general, you use the same Cumulus Linux or Debian Linux commands on
the chassis that you would use on any other Cumulus Linux switch.
However, there is a new suite of commands called `cl-chassis`. In
addition, SSH works a little differently within a chassis.

## <span>cl-chassis Commands</span>

Cumulus Linux has a number of chassis-specific commands that can execute
against one or all cards in the chassis. The cl-chassis command provides
options for:

  - Installing Cumulus Linux licenses

  - Installing a network operating system

  - Interacting with daemons

  - Restarting services

  - Rebooting the fabric and line cards

  - Generating the cl-support script when you need technical support

The `cl-chassis` commands use a REST API on the back end.

    cumulus@chassis:~$ sudo cl-chassis --help
     
     
    Usage:
        cl-chassis [<ipv6>|all] license-install path <text>
        cl-chassis [<ipv6>|all] reboot
        cl-chassis [<ipv6>|all] nos-install path <text>
        cl-chassis [<ipv6>|all] daemon restart <text>
        cl-chassis [<ipv6>|all] cl-support
     
     
    Options:
        <ipv6> : Link local IPv6 address of an endpoint
        all : All endpoints within a chassis
        license-install : Install license for Cumulus Linux
        path : Path on the local system or a URL
        reboot : Reboot endpoint in a CLOS
        nos-install : Install a new Cumulus Linux binary image (Destructive!!!! Please backup important files)
        daemon: Cumulus Linux Daemon related operations
        restart : Systemd restart of a service
     
     
    The following commands contain keyword(s) 'run'
     
     
        net run [<ipv6>|all] cl-support
        net run [<ipv6>|all] daemon restart <text>
        net run [<ipv6>|all] license-install path <text>
        net run [<ipv6>|all] nos-install path <text>
        net run [<ipv6>|all] reboot

## <span>Using SSH within the Chassis</span>

Once you are logged into any fabric or line card in the chassis, you can
use `ssh` and `scp` to connect to any other card without a password. SSH
is managed by the `cumulus-chassis-ssh` service, which runs on port 722
and detects host names listed in `/etc/hosts`.

On a Backpack chassis, to SSH from a line card to a CMM directly when
the management VRF is enabled, use `sudo vrf exec default` before the
`ssh` command. For example:

    cumulus@backpack-lc401:mgmt-vrf:~$ sudo vrf exec default ssh root@fe80::c1:1%eth0.4088
