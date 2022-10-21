---
title: Configuring switchd
author: NVIDIA
weight: 240
toc: 3
---
The `switchd` service enables the switch to communicate with Cumulus Linux and all the applications running on Cumulus Linux.

## Configure switchd Parameters

You can control certain options associated with the `switchd` process. For example, you can set polling intervals, optimize ACL hardware resources for better utilization, configure log message levels, set the internal VLAN range, and configure VXLAN encapsulation and decapsulation.

To configure `switchd` options, you either run NVUE commands or manually edit the `/etc/cumulus/switchd.conf` file.

{{%notice note%}}
NVUE currently only supports a subset of the `switchd` configuration available in the `/etc/cumulus/switchd.conf` file.
{{%/notice%}}

{{< tabs "TabID115 ">}}
{{< tab "NVUE Commands ">}}

You can run NVUE commands to set the following `switchd` options:
- The statistic polling interval for physical interfaces. You can specify a value between 1 and 10. The default setting is 2 seconds.
- The statistic polling interval for logical interfaces. You can specify a value between 1 and 10. The default setting is 2 seconds.
- The log level to debug the data plane programming related code. You can specify debug, info, notice, warning, or error. The default setting is info. NVIDIA recommends that you do not set the log level to debug in a production environment.
- The DSCP action and value for encapsulation. You can specify copy, set, or derive for the DSCP action. The default action is derive.
- The DSCP action for decapsulation in VXLAN outer headers. You can specify copy, preserve, or derive. The default action is derive.
- The route or neighbour preference. You can specify route, neighbor, or route and neighbour. The default setting is route.
- The ACL mode (atomic or non-atomic). The default setting is atomic mode.

The following command example sets the statistic polling interval for physical interfaces to 5 seconds:

```
cumulus@switch:~$ nv set system counter polling-interval physical-interface 5
cumulus@switch:~$ nv config apply
```

The following command example sets the statistic polling interval for logical interfaces to 5 seconds:

```
cumulus@switch:~$ nv set system counter polling-interval logical-interface 5
cumulus@switch:~$ nv config apply
```

The following command example sets the log level for debugging the data plane programming related code to warning:

```
cumulus@switch:~$ nv set system forwarding programming log-level warning
cumulus@switch:~$ nv config apply
```

The following command example sets the DSCP action for encapsulation in VXLAN outer headers to copy:

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp action copy
cumulus@switch:~$ nv config apply
```

The following command example sets the DSCP value for encapsulation in VXLAN outer headers to af12:

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp value af12
cumulus@switch:~$ nv config apply
```

The following command example sets the DSCP action for decapsulation in VXLAN outer headers to preserve:

```
cumulus@switch:~$ nv set nve vxlan decapsulation dscp action preserve
cumulus@switch:~$ nv config apply
```

The following command example sets the route or neighbour preference to route and neighbour:

```
cumulus@switch:~$ nv set system forwarding host-route-preference route-and-neighbour
cumulus@switch:~$ nv config apply
```

The following command example sets the ACL mode to non-atomic:

```
cumulus@switch:~$ nv set system acl mode non-atomic 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To configure the `switchd` parameters, edit the `/etc/cumulus/switchd.conf` file. Change the setting and uncomment the line if needed.

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
...
```

When you update the following settings in the `/etc/cumulus/switchd.conf` file, you must restart `switchd` with the `sudo systemctl restart switchd.service` command for the changes to take effect.

{{%notice warning%}}
Restarting the `switchd` service causes all network ports to reset in addition to resetting the switch hardware configuration.
{{%/notice%}}

- `vxlan.def_encap_dscp_action`
- `vxlan.def_encap_dscp_value`
- `vxlan.def_decap_dscp_action`
- `acl.optimize_hw`
- `ignore_non_swps`
- `route.delete_dead_routes`
- `ipmulticast.unknown_ipmc_to_cpu`
- `ipmulticast. svi_l3mc_disable`
- `evpn.multihoming.enable`
- `evpn.multihoming.shared_l2_groups`
- `evpn.multihoming.shared_l3_groups`
- `evpn.multihoming.fast_local_protect`
- `ptp.timestamping`
- `vxlan.default_ttl`
- `netlink.buf_size`
- `netlink.nl_logger`
- `bridge.broadcast_frame_to_cpu`
- `bridge.unreg_mcast_init`
- `bridge.unreg_v4_mcast_prune`
- `bridge.unreg_v6_mcast_prune`
- `vrf_route_leak_enable_dynamic`
- `sync_queue_depth_val`
- `disable_internal_parity_restart`
- `link_flap_window`
- `link_flap_threshold`
- `res_warn_msg_int`
- `res_usage_warn_threshold`

When you update the following settings in the `/etc/cumulus/switchd.conf` file, you must reload `switchd` with the `sudo systemctl reload switchd.service` command for the changes to take effect. The reload does **not** interrupt network services.

- `route.route_preferred_over_neigh`
- `acl.non_atomic_update_mode`
- `interface.swp1.storm_control.broadcast`
- `interface.swp1.storm_control.multicast`
- `interface.swp1.storm_control.unknown_unicast`

{{< /tab >}}
{{< /tabs >}}
