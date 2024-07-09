---
title: Configuring switchd
author: NVIDIA
weight: 240
toc: 3
---
The `switchd` service enables the switch to communicate with Cumulus Linux and all the applications running on Cumulus Linux.

## Configure switchd Parameters

You can control certain options associated with the `switchd` process. For example, you can set polling intervals, optimize ACL hardware resources for better utilization, configure log message levels, set the internal VLAN range, and configure VXLAN encapsulation and decapsulation.

To configure the `switchd` parameters, edit the `/etc/cumulus/switchd.conf` file. Change the setting and uncomment the line if needed. The `switchd.conf` file contains comments with a description for each setting.

The following example shows the first few lines of the `/etc/cumulus/switchd.conf` file.

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

The following table describes the `/etc/cumulus/switchd.conf` file parameters and indicates if you need to restart `switchd` with the `sudo systemctl restart switchd.service` command or reload `switchd` with the `sudo systemctl reload switchd.service` command for changes to take effect when you update the setting.

{{%notice warning%}}
Restarting the `switchd` service causes all network ports to reset in addition to resetting the switch hardware configuration.
{{%/notice%}}

| Parameter| Description | switchd reload or restart |
| -------|  --------- | --------- |
| `stats.poll_interval` | The statistics polling interval in milliseconds.</br>The default setting is 2000. | restart |
| `buf_util.poll_interval` | The buffer utilization polling interval in milliseconds. 0 disables buffer utilization polling.</br>The default setting is 0. | restart |
| `buf_util.measure_interval` | The buffer utilization measurement interval in minutes.</br>The default setting is 0. | restart |
| `acl.optimize_hw` | Optimizes ACL hardware resources for better utilization.</br>The default setting is FALSE. | restart |
| `acl.flow_based_mirroring` | Enables flow-based mirroring.</br>The default setting is TRUE. | restart |
| `acl.non_atomic_update_mode`  | Enables non atomic ACL updates</br>The default setting is FALSE. | reload |
| `arp.next_hops` | Sends ARPs for next hops.</br>The default setting is TRUE. | restart |
| `route.table` | The kernel routing table ID. The range is between 1 and 2^31.</br> The default is 254. | restart |
| `route.host_max_percent` | The maximum neighbor table occupancy in hardware (a percentage of the hardware table size).</br>The default setting is 100. | restart |
| `coalescing.reducer` | The coalescing reduction factor for accumulating changes to reduce CPU load.</br>The default setting is 1. | restart |
| `coalescing.timeout` | The coalescing time limit in seconds.</br>The default setting is 10. | restart |
| `ignore_non_swps` | Ignore routes that point to non-swp interfaces.</br>The default setting is TRUE. | restart |
| `disable_internal_parity_restart` | Disables restart after a parity error.</br>The default setting is TRUE. | restart |
| `disable_internal_hw_err_restart` | Disables restart after an unrecoverable hardware error.</br>The default setting is FALSE. | restart |
| `nat.static_enable` | Enables static NAT.<br>The default setting is TRUE. | restart |
| `nat.dynamic_enable` | Enables dynamic NAT.<br>The default setting is TRUE. | restart |
| `nat.age_poll_interval` | The NAT age polling interval in minutes. The minimum is 1 minute and the maximum is 24 hours. You can configure this setting only when `nat.dynamic_enable` is set to TRUE.<br>The default setting is 5. | restart |
| `nat.table_size` | The NAT table size limit in number of entries. You can configure this setting only when `nat.dynamic_enable` is set to TRUE.<br>The default setting is 1024. | restart |
| `nat.config_table_size` | The NAT configuration table size limit in number of entries. You can configure this setting only when `nat.dynamic_enable` is set to TRUE.<br>The default setting is 64. | restart |
| `logging` | Configures logging in the format BACKEND=LEVEL. Separate multiple BACKEND=LEVEL pairs with a space. The BACKEND value can be `stderr`, `file:filename`, `syslog`, `program:executable`. The LEVEL value can be `CRIT`, `ERR`, `WARN`, `INFO`, `DEBUG`.</br>The default value is `syslog=INFO`| restart |
| `interface.swp1.storm_control.broadcast` | Enables broadcast storm control and sets the number of packets per second (pps).</br>The default setting is 400. | reload |
| `interface.swp1.storm_control.multicast` | Enables multicast storm control and sets the number of packets per second (pps).</br>The default setting is 3000. | reload |
| `interface.swp1.storm_control.unknown_unicast` | Enables unicast storm control and sets the number of packets per second (pps).</br>The default setting is 2000. | reload |
| `stats.vlan.aggregate` | Enables hardware statistics for VLANs and specifies the type of statistics needed. You can specify NONE, BRIEF, or DETAIL.</br>The default setting is BRIEF. | restart |
| `stats.vxlan.aggregate` | Enables hardware statistics for VXLANs and specifies the type of statistics needed. You can specify NONE, BRIEF, or DETAIL.</br> The default setting is DETAIL. | restart |
| `stats.vxlan.member` | Enables hardware statistics for VXLAN members and specifies the type of statistics needed. You can specify NONE, BRIEF, or DETAIL.</br>The default setting is BRIEF. | restart |
| `stats.vlan.show_internal_vlans` | Show internal VLANs.</br>The default setting is FALSE. | restart |
| `stats.vdev_hw_poll_interval` | The polling interval in seconds for virtual device hardware statisitcs.</br>The default setting is 5. | restart |
| `resv_vlan_range` | The internal VLAN range.</br>The default setting is 3725-3999. | restart |
| `netlink.buf_size` | The netlink socket buffer size in MB.</br>The default setting is 136314880. | restart |
| `route.delete_dead_routes` | Delete routes on interfaces when the carrier is down.</br>The default setting is TRUE. | restart |
| `vxlan.default_ttl` | The default TTL to use in VXLAN headers.</br>The default setting is 64. | restart |
| `bridge.broadcast_frame_to_cpu` | Enables bridge broadcast frames to the CPU even if the SVI is not enabled.</br>The default setting is FALSE. | restart |
| `bridge.unreg_mcast_init` | Initialize the prune module for IGMP snooping unregistered layer 2 multicast flood control.</br>The default setting is FALSE. | restart |
| `bridge.unreg_v4_mcast_prune` | Enables unregistered layer 2 multicast prune to mrouter ports (IPv4).</br>The default setting is FALSE (flood unregistered layer 2 multicast traffic). | restart |
| `bridge.unreg_v6_mcast_prune` | Enables unregistered layer 2 multicast prune to mrouter ports (IPv6).</br>The default setting is FALSE (flood unregistered layer 2 multicast traffic). | restart |
| `netlink libnl logger` | The default setting is [0-5]. | restart |
| `netlink.nl_logger` | The default setting is 0. | restart |
| `vxlan.def_encap_dscp_action` | Sets the default VXLAN router DSCP action during encapsulation. You can specify `copy` if the inner packet is IP, `set` to set a specific value, or `derive` to derive the value from the switch priority.</br>The default setting is `derive`. | restart |
| `vxlan.def_encap_dscp_value` | Sets the default VXLAN encapsulation DSCP value if the action is `set`.</br> | restart |
| `vxlan.def_decap_dscp_action` | Sets the default VXLAN router DSCP action during decapsulation. You can specify `copy` if the inner packet is IP, `preserve` to preserve the inner DSCP value, or `derive` to derive the value from the switch priority.</br>The default setting is `derive`. | restart |
| `ipmulticast.unknown_ipmc_to_cpu` | Enables sending unknown IPMC to the CPU.</br>The default setting is FALSE. | restart |
| `ptp.timestamping` | Enables PTP time stamping.</br>The default setting is TRUE. | restart|
| `vrf_route_leak_enable_dynamic` | Enables dynamic VRF route leaking.</br>The default setting is FALSE. | restart |
| `sync_queue_depth_val` | The event queue depth.</br>The default setting is 50000. | restart |
| `route.route_preferred_over_neigh` | Sets the preference between a route and neighbor with the same IP address and mask. You can specify `TRUE` to prefer the route over the neighbor, `FALSE` to prefer the neighbor over the route, or `BOTH` to install both the route and neighbor.</br>The default setting is TRUE. | restart |
| `evpn.multihoming.enable` | Enables EVPN multihoming.</br>The default setting is TRUE. | restart |
| `evpn.multihoming.shared_l2_groups` | Enables sharing for layer 2 next hop groups.</br>The default setting is FALSE. | restart |
| `evpn.multihoming.shared_l3_groups` | Enables sharing for layer 3 next hop groups.</br>The default setting is FALSE. | restart |
| `evpn.multihoming.fast_local_protect` | Enables fast reroute for egress link protection. The default setting is FALSE. | restart |
| `link_flap_window` | The duration in seconds during which a link must flap the number of times set in the `link_flap_threshold` before Cumulus Linux sets the link to protodown and specifies `linkflap` as the reason.</br>The default setting is 10. A value of 0 disables link flap protection.| restart |
| `link_flap_threshold` | The number of times the link must flap within the link flap window before Cumulus Linux sets the link to protodown and specifies `linkflap` as the reason.</br>The default setting is 5. A value of 0 disables link flap protection. | restart |
| `res_usage_warn_threshold` | Sets the percentage over which forwarding resources (routes, hosts, MAC addresses) must go before Cumulus Linux generates a warning. You can set a value between 50 and 95.</br>The default setting is 90. | restart |
| `res_warn_msg_int` | The time interval in seconds between resource warning messages. Warning messages generate only one time in the specified interval per resource type even if the threshold falls below or goes over the value set in `res_usage_warn_threshold` multiple times during this interval. You can set a value between 60 and 3600.</br>The default setting is 300. | restart |

{{%notice note%}}
In addition to restarting `switchd` when you change certain `/etc/cumulus/switchd.conf` file parameters, you also need to restart `switchd` whenever you modify a `switchd` hardware configuration file (any `*.conf` file that requires making a change to the switching hardware, such as `/etc/cumulus/datapath/traffic.conf`). You do not have to restart the `switchd` service when you update a network interface configuration (for example, when you edit the `/etc/network/interfaces` file).
{{%/notice%}}
