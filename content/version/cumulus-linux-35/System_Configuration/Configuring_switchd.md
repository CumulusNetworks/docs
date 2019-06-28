---
title: Configuring switchd
author: Cumulus Networks
weight: 73
aliases:
 - /display/CL35/Configuring+switchd
 - /pages/viewpage.action?pageId=8357343
pageID: 8357343
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
`switchd` is the daemon at the heart of Cumulus Linux. It communicates
between the switch and Cumulus Linux, and all the applications running
on Cumulus Linux.

The `switchd` configuration is stored in `/etc/cumulus/switchd.conf`.

{{%notice note%}}

Versions of Cumulus Linux prior to 2.1 stored the `switchd`
configuration at `/etc/default/switchd`.

{{%/notice%}}

## <span>The switchd File System</span>

`switchd` also exports a file system, mounted on `/cumulus/switchd`,
that presents all the `switchd` configuration options as a series of
files arranged in a tree structure. You can see the contents by parsing
the `switchd` tree; run `tree /cumulus/switchd`. The output below is for
a switch with one switch port configured:

    cumulus@switch:~$ sudo tree /cumulus/switchd/
    /cumulus/switchd/
    |-- config
    |   |-- acl
    |   |   |-- non_atomic_update_mode
    |   |   `-- optimize_hw
    |   |-- arp
    |   |   `-- next_hops
    |   |-- buf_util
    |   |   |-- measure_interval
    |   |   `-- poll_interval
    |   |-- coalesce
    |   |   |-- reducer
    |   |   `-- timeout
    |   |-- disable_internal_restart
    |   |-- ignore_non_swps
    |   |-- interface
    |   |   |-- swp1
    |   |   |   `-- storm_control
    |   |   |       |-- broadcast
    |   |   |       |-- multicast
    |   |   |       `-- unknown_unicast
    |   |-- logging
    |   |-- route
    |   |   |-- host_max_percent
    |   |   `-- table
    |   `-- stats
    |       `-- poll_interval
    |-- ctrl
    |   |-- acl
    |   |-- hal
    |   |   `-- resync
    |   |-- logger
    |   |-- netlink
    |   |   `-- resync
    |   |-- resync
    |   `-- sample
    |       `-- ulog_channel
    |-- run
    |   `-- route_info
    |       |-- ecmp_nh
    |       |   |-- count
    |       |   |-- max
    |       |   `-- max_per_route
    |       |-- host
    |       |   |-- count
    |       |   |-- count_v4
    |       |   |-- count_v6
    |       |   `-- max
    |       |-- mac
    |       |   |-- count
    |       |   `-- max
    |       `-- route
    |           |-- count_0
    |           |-- count_1
    |           |-- count_total
    |           |-- count_v4
    |           |-- count_v6
    |           |-- mask_limit
    |           |-- max_0
    |           |-- max_1
    |           `-- max_total
    `-- version

## <span>Configuring switchd Parameters</span>

You can use `cl-cfg` to configure many `switchd` parameters at runtime
(like ACLs, interfaces, and route table utilization), which minimizes
disruption to your running switch. However, some options are read only
and cannot be configured at runtime.

For example, to see data related to routes, run:

    cumulus@switch:~$ sudo cl-cfg -a switchd | grep route
    route.table = 254
    route.host_max_percent = 50
    cumulus@cumulus:~$

To modify the configuration, run `cl-cfg -w`. For example, to set the
buffer utilization measurement interval to 1 minute, run:

    cumulus@switch:~$ sudo cl-cfg -w switchd buf_util.measure_interval=1

To verify that the value changed, use `grep`:

    cumulus@switch:~$ cl-cfg -a switchd | grep buf
    buf_util.poll_interval = 0
    buf_util.measure_interval = 1

{{%notice note%}}

You can get some of this information by running `cl-resource-query`;
though you cannot update the `switchd` configuration with it.

{{%/notice%}}

## <span id="src-8357343_Configuringswitchd-restartswitchd" class="confluence-anchor-link"></span><span>Restarting switchd</span>

Whenever you modify any `switchd` hardware configuration file (typically
changing any `*.conf` file that requires making a change to the
switching hardware, like `/etc/cumulus/datapath/traffic.conf`), you must
restart `switchd` for the change to take effect:

    cumulus@switch:~$ sudo systemctl restart switchd.service

{{%notice note%}}

You do not have to restart the `switchd` service when you update a
network interface configuration (that is, edit
`/etc/network/interfaces`).

{{%/notice%}}

{{%notice warning%}}

Restarting `switchd` causes all network ports to reset in addition to
resetting the switch hardware configuration.

{{%/notice%}}
