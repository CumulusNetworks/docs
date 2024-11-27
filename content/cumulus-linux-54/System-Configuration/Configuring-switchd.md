---
title: Configuring switchd
author: NVIDIA
weight: 240
toc: 3
---
The `switchd` service enables the switch to communicate with Cumulus Linux and all the applications running on Cumulus Linux.

## Configure switchd Settings

You can control certain options associated with the `switchd` process. For example, you can set polling intervals, optimize ACL hardware resources for better utilization, configure log message levels, set the internal VLAN range, and configure VXLAN encapsulation and decapsulation.

To configure `switchd` options, you either run NVUE commands or manually edit the `/etc/cumulus/switchd.conf` file.

{{%notice note%}}
NVUE currently only supports a subset of the `switchd` configuration available in the `/etc/cumulus/switchd.conf` file.
{{%/notice%}}

{{< tabs "TabID115 ">}}
{{< tab "NVUE Commands ">}}

You can run NVUE commands to set the following `switchd` options:
- The statistic polling interval for physical interfaces and for logical interfaces. 
  - For physical interfaces, you can specify a value between 1 and 10. The default setting is 2 seconds
  - For logical interfaces, you can specify a value between 1 and 30. The default setting is 5 seconds.
  
   {{%notice note%}}
A low setting, such as 1, might affect system performance.
{{%/notice%}}

- The log level to debug the data plane programming related code. You can specify `debug`, `info`, `notice`, `warning`, or `error`. The default setting is `info`. NVIDIA recommends that you do not set the log level to debug in a production environment.
- The DSCP action and value for encapsulation. You can set the DSCP action to `copy` (to copy the value from the IP header of the packet), `set` (to specify a specific value), or `derive` (to obtain the value from the switch priority). The default action is `derive`. Only specify a value if the action is `set`.
- The DSCP action for decapsulation in VXLAN outer headers. You can specify `copy` (to copy the value from the IP header of the packet), `preserve` (to keep the inner DSCP value), or `derive` (to obtain the value from the switch priority). The default action is `derive`.
- The preference between a route and neighbor with the same IP address and mask. You can specify `route`, `neighbor`, or `route-and-neighbour`. The default setting is `route`.
- The ACL mode (atomic or non-atomic). The default setting is `atomic`.
- The reserved VLAN range. The default setting is 3725-3999.

{{%notice warning%}}
Certain `switchd` settings require a `switchd` restart or reload. Before applying the settings, NVUE indicates if it requires a `switchd` restart or reload and prompts you for confirmation.  
- When the `switchd` service restarts, in addition to resetting the switch hardware configuration, all network ports reset.
- When the `switchd` service reloads, there is **no** interruption to network services.
{{%/notice%}}

The following command example sets both the statistic polling interval for logical interfaces and physical interfaces to 6 seconds:

```
cumulus@switch:~$ nv set system counter polling-interval logical-interface 6
cumulus@switch:~$ nv set system counter polling-interval physical-interface 6
cumulus@switch:~$ nv config apply
```

The following command example sets the log level for debugging the data plane programming related code to `warning`:

```
cumulus@switch:~$ nv set system forwarding programming log-level warning
cumulus@switch:~$ nv config apply
```

The following command example sets the DSCP action for encapsulation in VXLAN outer headers to `set` and the value to `af12`:

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp action set
cumulus@switch:~$ nv set nve vxlan encapsulation dscp value af12
cumulus@switch:~$ nv config apply
```

The following command example sets the DSCP action for decapsulation in VXLAN outer headers to `preserve`:

```
cumulus@switch:~$ nv set nve vxlan decapsulation dscp action preserve
cumulus@switch:~$ nv config apply
```

The following command example sets the route or neighbour preference to both route and neighbour:

```
cumulus@switch:~$ nv set system forwarding host-route-preference route-and-neighbour
cumulus@switch:~$ nv config apply
```

The following command example sets the ACL mode to non-atomic:

```
cumulus@switch:~$ nv set system acl mode non-atomic 
cumulus@switch:~$ nv config apply
```

The following command example sets the reserved VLAN range between 4064 and 4094:

```
cumulus@switch:~$ nv set system global reserved vlan internal range 4064-4094
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

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
| `vrf_route_leak_enable_dynamic` | Enables dynamic VRF route leaking.</br>The default setting is FALSE. | restart |
| `sync_queue_depth_val` | The event queue depth.</br>The default setting is 50000. | restart |
| `route.route_preferred_over_neigh` | Sets the preference between a route and neighbor with the same IP address and mask. You can specify `TRUE` to prefer the route over the neighbor, `FALSE` to prefer the neighbor over the route, or `BOTH` to install both the route and neighbor.</br>The default setting is TRUE. | restart |
| `evpn.multihoming.enable` | Enables EVPN multihoming.</br>The default setting is TRUE. | restart |
| `evpn.multihoming.shared_l2_groups` | Enables sharing for layer 2 next hop groups.</br>The default setting is FALSE. | restart |
| `evpn.multihoming.shared_l3_groups` | Enables sharing for layer 3 next hop groups.</br>The default setting is FALSE. | restart |
| `evpn.multihoming.fast_local_protect` | Enables fast reroute for egress link protection. The default setting is FALSE. | restart |
| `evpn.multihoming.bum_sph_filter` | Sets split-horizon filtering for EVPN multihoming. You can specify `TRUE` to filter only BUM traffic from the Ethernet segment (ES) peer or `FALSE` to filter all traffic from the ES peer.</br>The default setting is TRUE. | restart |
| `link_flap_window` | The duration in seconds during which a link must flap the number of times set in the `link_flap_threshold` before Cumulus Linux sets the link to protodown and specifies `linkflap` as the reason.</br>The default setting is 10. A value of 0 disables link flap protection.| restart |
| `link_flap_threshold` | The number of times the link must flap within the link flap window before Cumulus Linux sets the link to protodown and specifies `linkflap` as the reason.</br>The default setting is 5. A value of 0 disables link flap protection. | restart |
| `res_usage_warn_threshold` | Sets the percentage over which forwarding resources (routes, hosts, MAC addresses) must go before Cumulus Linux generates a warning. You can set a value between 50 and 95.</br>The default setting is 90. | restart |
| `res_warn_msg_int` | The time interval in seconds between resource warning messages. Warning messages generate only one time in the specified interval per resource type even if the threshold falls below or goes over the value set in `res_usage_warn_threshold` multiple times during this interval. You can set a value between 60 and 3600.</br>The default setting is 300. | restart |

{{< /tab >}}
{{< /tabs >}}

## Show switchd Settings

You can run the following NVUE commands to show the current `switchd` configuration settings.

| <div style="width:350px">Command | Description |
| ------- | ----------- |
|`nv show system counter polling-interval` | Shows the polling interval for physical and logical interface counters in seconds. |
|`nv show system forwarding programming` | Shows the log level for data plane programming logs. |
|`nv show nve vxlan encapsulation dscp` | Shows the DSCP action and value (if the action is `set`) for the outer header in VXLAN encapsulation.|
|`nv show nve vxlan decapsulation dscp` | Shows the DSCP action for the outer header in VXLAN decapsulation.|
|`nv show system acl ` | Shows the ACL mode (atomic or non-atomic). |
|`nv show system global reserved vlan internal` | Shows the reserved VLAN range.|

The following example command shows that the polling interval setting for logical interface counters is 6 seconds:

```
cumulus@switch:~$ nv show system counter polling-interval
                   applied  description
-----------------  -------  -----------------------------------------------------
logical-interface  0:00:06  Config polling-interval for logical interface(in sec)
```

The following example command shows that the log level setting for data plane programming logs is `warning`:

```
cumulus@switch:~$ nv show system forwarding programming
           applied  description
---------  -------  -------------------
log-level  warning  configure Log-level
```

The following example command shows that the DSCP action setting for the outer header in VXLAN encapsulation is `set` and the value is `af12`.

```
cumulus@switch:~$ nv show nve vxlan encapsulation dscp
        operational  applied  description
------  -----------  -------  --------------------------------------------------
action  set          set      DSCP encapsulation action
value   af12         af12     Configured DSCP value to put in outer Vxlan packet
```

The following command example shows that ACL mode is `atomic`:

```
cumulus@switch:~$ nv show system acl
      applied  description
----  -------  -----------------------------------------
mode  atomic   configure Atomic or Non-Atomic ACL update
```

The following command example shows that the reserved VLAN range is between 4064 and 4094:

```
cumulus@switch:~$ nv show system global reserved vlan internal
       operational  applied    description
-----  -----------  ---------  -------------------
range  4064-4094    4064-4094  Reserved Vlan range
```

{{%notice note%}}
In addition to restarting `switchd` when you change certain `/etc/cumulus/switchd.conf` file parameters manually, you also need to restart `switchd` whenever you modify a `switchd` hardware configuration file (any `*.conf` file that requires making a change to the switching hardware, such as `/etc/cumulus/datapath/traffic.conf`). You do not have to restart the `switchd` service when you update a network interface configuration (for example, when you edit the `/etc/network/interfaces` file).
{{%/notice%}}
