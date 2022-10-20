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
- The statistic polling interval for both physical interfaces and logical interfaces.
- The log level to debug the data plane programming related code.
- The DSCP action and value for encapsulation and the DSCP action for decapsulation in VXLAN outer headers.
- The route or neighbour preference.
- The ACL mode (atomic or non-atomic).

To set the statistic polling interval (in seconds) for physical interfaces:

```
cumulus@switch:~$ nv set system counter polling-interval physical-interface 5
cumulus@switch:~$ nv config apply
```

To set the statistic polling interval (in seconds) for logical interfaces:

```
cumulus@switch:~$ nv set system counter polling-interval logical-interface 5
cumulus@switch:~$ nv config apply
```

To set the log level (debug, info, notice, warning, or err) for debugging the data plane programming related code:

```
cumulus@switch:~$ nv set system forwarding programming log-level warning
cumulus@switch:~$ nv config apply
```

To set the DSCP action (copy, set, or derive) for encapsulation in VXLAN outer headers:

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp action copy
cumulus@switch:~$ nv config apply
```

To set the DSCP value for encapsulation in VXLAN outer headers:

```
cumulus@switch:~$ nv set nve vxlan encapsulation dscp value af12
cumulus@switch:~$ nv config apply
```

To set the DSCP action (copy, preserve, or derive) for decapsulation in VXLAN outer headers:

```
cumulus@switch:~$ nv set nve vxlan decapsulation dscp action preserve
cumulus@switch:~$ nv config apply
```

To set the route or neighbour preference (route, neighbor, or route-and-neighbour):

```
cumulus@switch:~$ nv set system forwarding host-route-preference route-and-neighbour
cumulus@switch:~$ nv config apply
```

To set the ACL mode (atomic or non-atomic):

```
cumulus@switch:~$ nv set system acl mode atomic 
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

# Send ARPs for next hops
#arp.next_hops = TRUE

# Kernel routing table ID, range 1 - 2^31, default 254
#route.table = 254
...
```

When you update the `/etc/cumulus/switchd.conf` file, you must restart `switchd` with the `sudo systemctl restart switchd.service` command for the changes to take effect.

{{< /tab >}}
{{< /tabs >}}

## Restart switchd

When you modify certain settings in the `switchd` hardware configuration files (for example, you update a `*.conf` file that requires making a change to the switching hardware), you must restart the `switchd` service for the change to take effect:

```
cumulus@switch:~$ sudo systemctl restart switchd.service
```

You do not have to restart the `switchd` service when you update a network interface configuration (for example, when you edit the `/etc/network/interfaces` file).

{{%notice warning%}}
Restarting the `switchd` service causes all network ports to reset in addition to resetting the switch hardware configuration. NVIDIA recommends that you reboot the switch instead of restarting the `switchd` service to minimize traffic impact when redundant switches are present with MLAG.
{{%/notice%}}

NVUE commands restart the `switchd` service automatically; you do not need to run the `sudo systemctl restart switchd.service` command when using NVUE commands.
