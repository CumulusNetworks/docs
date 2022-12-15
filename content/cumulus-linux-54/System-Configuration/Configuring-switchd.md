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
- `resv_vlan_range`

When you update the following settings in the `/etc/cumulus/switchd.conf` file, you must reload `switchd` with the `sudo systemctl reload switchd.service` command for the changes to take effect. The reload does **not** interrupt network services.

- `route.route_preferred_over_neigh`
- `acl.non_atomic_update_mode`
- `interface.swp1.storm_control.broadcast`
- `interface.swp1.storm_control.multicast`
- `interface.swp1.storm_control.unknown_unicast`

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
