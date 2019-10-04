---
title: Configuring switchd
author: Cumulus Networks
weight: 61
aliases:
 - /display/CL25ESR/Configuring+switchd
 - /pages/viewpage.action?pageId=5115907
pageID: 5115907
product: Cumulus Linux
version: 2.5 ESR
imgData: cumulus-linux-25esr
siteSlug: cumulus-linux-25esr
---
`switchd` is the daemon at the heart of Cumulus Linux. It communicates
between the switch and Cumulus Linux, and all the applications running
on Cumulus Linux.

The `switchd` configuration is stored in `/etc/cumulus/switchd.conf`.

{{%notice note%}}

Versions of Cumulus Linux prior to 2.1 stored the `switchd`
configuration at `/etc/default/switchd.`

{{%/notice%}}

## The switchd File System

`switchd` also exports a file system, mounted on `/cumulus/switchd`,
that presents all the `switchd` configuration options as a series of
files arranged in a tree structure. You can see the contents by parsing
the `switchd` tree; run `tree /cumulus/switchd`. The output below is for
a switch with one switch port configured:

    cumulus@cumulus:~# sudo tree /cumulus/switchd/
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
    |   |   |-- max_routes
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

## Configuring switchd Parameters

You can use `cl-cfg` to configure many `switchd` parameters at runtime
(like ACLs, interfaces, and route table utilization), which minimizes
disruption to your running switch. However, some options are read only
and cannot be configured at runtime.

For example, to see data related to routes, run:

    cumulus@cumulus:~$ sudo cl-cfg -a switchd | grep route
    route.table = 254
    route.max_routes = 32768
    route.host_max_percent = 50
    cumulus@cumulus:~$

To modify the configuration, run `cl-cfg -w`. For example, to set the
buffer utilization measurement interval to 1 minute, run:

    cumulus@cumulus:~$ sudo cl-cfg -w switchd buf_util.measure_interval=1

To verify that the value changed, use `grep`:

    cumulus@cumulus:~# cl-cfg -a switchd | grep buf
    buf_util.poll_interval = 0
    buf_util.measure_interval = 1

{{%notice note%}}

You can get some of this information by running `cl-resource-query`;
though you cannot update the switchd configuration with it.

{{%/notice%}}

## Restarting switchd

Whenever you modify any `switchd` hardware configuration file (typically
changing any `*.conf` file that requires making a change to the
switching hardware, like `/etc/cumulus/datapath/traffic.conf`), you must
restart `switchd` for the change to take effect:

    cumulus@switch:~$ sudo service switchd restart

{{%notice note%}}

You do not have to restart the `switchd` service when you update a
network interface configuration (that is, edit
`/etc/network/interfaces`).

{{%/notice%}}

{{%notice warning%}}

Restarting `switchd` causes all network ports to reset in addition to
resetting the switch hardware configuration.

{{%/notice%}}

## Commands

  - cl-cfg

## Configuration Files

  - /etc/cumulus/switchd.conf
