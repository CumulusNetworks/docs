---
title: Configuring switchd
author: NVIDIA
weight: 240
toc: 3
---
`switchd` is the daemon at the heart of Cumulus Linux. It communicates between the switch and Cumulus Linux, and all the applications running on Cumulus Linux.

The `switchd` configuration is stored in `/etc/cumulus/switchd.conf`.

## The switchd File System

`switchd` also exports a file system, mounted on `/cumulus/switchd`, that presents all the `switchd` configuration options as a series of files arranged in a tree structure. To show the contents, run the `tree /cumulus/switchd` command. The following example shows output for a switch with one switch port configured:

```
cumulus@switch:~$ sudo tree /cumulus/switchd/
/cumulus/switchd/
├── clear
│   └── stats
│       ├── vlan
│       └── vxlan
├── config
│   ├── acl
│   │   ├── flow_based_mirroring
│   │   ├── non_atomic_update_mode
│   │   ├── optimize_hw
│   │   └── vxlan_tnl_arp_punt_disable
│   ├── arp
│   │   ├── drop_during_failed_state
│   │   └── next_hops
│   ├── bridge
│   │   ├── broadcast_frame_to_cpu
│   │   └── optimized_mcast_flood
│   ├── buf_util
│   │   ├── measure_interval
│   │   └── poll_interval
│   ├── coalesce
│   │   ├── offset
│   │   ├── reducer
│   │   └── timeout
│   ├── disable_internal_hw_err_restart
│   ├── disable_internal_parity_restart
│   ├── hal
│   │   └── bcm
│   │       ├── l3
│   │       │   └── per_vlan_router_mac_lookup_for_vrrp
│   │       ├── linkscan_interval
│   │       ├── logging
│   │       │   └── l3mc
│   │       ├── per_vlan_router_mac_lookup
│   │       └── vxlan_support
│   ├── ignore_non_swps
│   ├── interface
│   │   ├── swp1
│   │   │   ├── ethtool_mode
│   │   │   ├── interface_mode
│   │   │   ├── port_security
│   │   │   │   ├── enable
│   │   │   │   ├── mac_limit
│   │   │   │   ├── static_mac
│   │   │   │   ├── sticky_aging
│   │   │   │   ├── sticky_mac
│   │   │   │   ├── sticky_timeout
│   │   │   │   ├── violation_mode
│   │   │   │   └── violation_timeout
│   │   │   └── storm_control
│   │   │       ├── broadcast
│   │   │       ├── multicast
│   │   │       └── unknown_unicast
...
```

## Configure switchd Parameters

To configure the `switchd` parameters, edit the `/etc/cumulus/switchd.conf` file. An example is provided below.

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.conf
#
# /etc/cumulus/switchd.conf - switchd configuration file
#

# Statistic poll interval (in msec)
#stats.poll_interval = 2000

# Buffer utilization poll interval (in msec), 0 means disable
#buf_util.poll_interval = 0

# Buffer utilization measurement interval (in mins)
#buf_util.measure_interval = 0

# Optimize ACL HW resources for better utilization
#acl.optimize_hw = FALSE

# Enable Flow based mirroring.
#acl.flow_based_mirroring = TRUE

# Enable non atomic acl update
acl.non_atomic_update_mode = FALSE

# Send ARPs for next hops
#arp.next_hops = TRUE

# Kernel routing table ID, range 1 - 2^31, default 254
#route.table = 254
...
```

When you update the `/etc/cumulus/switchd.conf` file, you must restart `switchd` for the changes to take effect. See {{<link url="#restart-switchd" text="Restart switchd">}}, below.

## Restart switchd

Whenever you modify a `switchd` hardware configuration file (for example, you update any `*.conf` file that requires making a change to the switching hardware, like `/etc/cumulus/datapath/traffic.conf`), you must restart the `switchd` service for the change to take effect:

```
cumulus@switch:~$ sudo systemctl restart switchd.service
```

You do not have to restart the `switchd` service when you update a network interface configuration (for example, when you edit the `/etc/network/interfaces` file).

{{%notice warning%}}

Restarting the `switchd` service causes all network ports to reset in addition to resetting the switch hardware configuration. NVIDIA recommends that you reboot the switch instead of restarting the `switchd` service to minimize traffic impact when redundant switches are present with MLAG.

{{%/notice%}}
