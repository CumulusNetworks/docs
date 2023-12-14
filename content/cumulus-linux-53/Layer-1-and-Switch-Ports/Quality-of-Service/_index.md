---
title: Quality of Service
author: NVIDIA
weight: 320
right_toc_levels: 2
---

This section refers to frames for all internal QoS functionality. Unless explicitly stated, the actions are independent of layer 2 frames or layer 3 packets.

Cumulus Linux supports several different <span class="a-tooltip">[QoS](## "Quality of Service")</span> features and standards including:
- <span class="a-tooltip">[COS](## "Class of Service")</span> and <span class="a-tooltip">[DSCP](## "Differentiated Services Code Point")</span> marking and remarking
- Shaping and policing
- Egress traffic scheduling (802.1Qaz, Enhanced Transmission Selection (ETS))
- Flow control with IEEE Pause Frames, <span class="a-tooltip">[PFC](## "Priority Flow Control")</span>, and <span class="a-tooltip">[ECN](## "Explicit Congestion Notification")</span>
- {{<link title="RDMA over Converged Ethernet - RoCE" text="Lossless and lossy RoCE ">}}

Cumulus Linux uses two configuration files for QoS:
- `/etc/cumulus/datapath/qos/qos_features.conf` includes all standard QoS configuration, such as marking, shaping and flow control.
- `/etc/mlx/datapath/qos/qos_infra.conf` includes all platform specific configurations, such as buffer allocations and [Alpha values](https://enterprise-support.nvidia.com/s/article/understanding-the-alpha-parameter-in-the-buffer-configuration-of-mellanox-spectrum-switches).

{{% notice note %}}
Cumulus Linux 5.0 and later does not use the `traffic.conf` and `datapath.conf` files but uses the `qos_features.conf` and `qos_infra.conf` files instead. Before upgrading Cumulus Linux, review your existing QoS configuration to determine the changes you need to make.
{{% /notice %}}

## switchd and QoS

When you run **Linux commands** to configure QoS, you must apply QoS changes to the ASIC with the following command:

```
cumulus@switch:~$ sudo systemctl reload switchd.service
```

Unlike the `restart` command, the `reload switchd.service` command does not impact traffic forwarding except when the `qos_infra.conf` file changes, or when the switch [pauses frames](#pause-frames) or controls [priority flow](#priority-flow-control-pfc), which require modifications to the ASIC buffer and might result in momentary packet loss.

NVUE reloads the `switchd` service automatically. You do **not** have to run the `reload switchd.service` command to apply changes when configuring QoS with NVUE commands.

## Classification

When a frame or packet arrives on the switch, Cumulus Linux maps it to an internal COS (switch priority) value. This value never writes to the frame or packet but classifies and schedules traffic internally through the switch.

You can define which values are `trusted`: 802.1p, DSCP, or both.

The following table describes the default classifications for various frame and switch priority configurations:

| Setting | VLAN Tagged? | IP or Non-IP | Result |
| ------------------------------------------ | ------ | ---- | ---- |
| PCP (802.1p) | Yes | IP | Accept incoming 802.1p marking. |
| PCP (802.1p)| Yes | Non-IP | Accept incoming 802.1p  marking. |
| PCP (802.1p)| No | IP | Use the default priority setting. |
| PCP (802.1p)| No | Non-IP | Use the default priority setting. |
| DSCP | Yes | IP | Accept incoming DSCP IP header marking. |
| DSCP | Yes | Non-IP | Use the default priority setting. |
| DSCP | No | IP | Accept incoming DSCP IP header marking. |
| DSCP | No | Non-IP | Use the default priority setting. |
| PCP (802.1p) and DSCP | Yes | IP | Accept incoming DSCP IP header marking. |
| PCP (802.1p) and DSCP | Yes | Non-IP | Accept incoming 802.1p marking. |
| PCP (802.1p) and DSCP | No | IP | Accept incoming DSCP IP header marking. |
| PCP (802.1p) and DSCP | No | Non-IP | Use the default priority setting. |
| port | Either | Either | Ignore any existing markings and use the default priority setting. |

- If you use NVUE to configure QoS, you define which values are `trusted` with the `nv set qos mapping <profile> trust l2` command (802.1p) or the `nv set qos mapping <profile> trust l3` command (DSCP) .
- If you use Linux commands to configure QoS, you define which values are `trusted` in the `/etc/cumulus/datapath/qos/qos_features.conf` file by configuring the `traffic.packet_priority_source_set` setting to `802.1p` or `dscp`.
<!-- vale off -->
### Trust 802.1p Marking
<!-- vale on -->
To trust 802.1p marking:

{{< tabs "TabID97 ">}}
{{< tab "NVUE Commands ">}}

When 802.1p (`l2`) is `trusted`, Cumulus Linux classifies these ingress 802.1p values to switch priority values:

|Switch Priority |802.1p (PCP) |
| ----------- | ---------- |
|0 |0|
|1 |1|
|2 |2|
|3 |3|
|4 |4|
|5 |5|
|6 |6|
|7 |7|

The PCP number is the incoming 802.1p marking; for example PCP 0 maps to switch priority 0.

To change the default profile to map PCP 0 to switch priority 4:

```
cumulus@switch:~$ nv set qos mapping default-global trust l2
cumulus@switch:~$ nv set qos mapping default-global pcp 0 switch-priority 4 
cumulus@switch:~$ nv config apply
```

You can map multiple PCP values to the same switch priority value. For example, to map PCP values 2, 3, and 4 to switch priority 0:

```
cumulus@switch:~$ nv set qos mapping default-global trust l2 
cumulus@switch:~$ nv set qos mapping default-global pcp 2,3,4 switch-priority 0
cumulus@switch:~$ nv config apply
```

If you configure the trust to be `l2` but do not specify any PCP to switch priority mappings, Cumulus Linux uses the default values.

To show the ingress 802.1p mapping for the default profile, run the `nv show qos mapping default-global pcp` command. To show the PCP mapping for a specific switch priority in the default profile, run the `nv show qos mapping default-global pcp <value>` command. The following example shows that PCP 0 maps to switch priority 4:

```
cumulus@switch:~$ nv show qos mapping default-global pcp 0
                 operational  applied  description
---------------  -----------  -------  ------------------------
switch-priority  4            4        Internal Switch Priority
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/cumulus/datapath/qos/qos_features.conf` file, set `traffic.packet_priority_source_set = [802.1p]`.

When 802.1p marking is `trusted`, the following lines classify ingress 802.1p values to switch priority (internal COS) values:

```
traffic.cos_0.priority_source.8021p = [0]
traffic.cos_1.priority_source.8021p = [1]
traffic.cos_2.priority_source.8021p = [2]
traffic.cos_3.priority_source.8021p = [3]
traffic.cos_4.priority_source.8021p = [4]
traffic.cos_5.priority_source.8021p = [5]
traffic.cos_6.priority_source.8021p = [6]
traffic.cos_7.priority_source.8021p = [7]
```

The `traffic.cos_` number is the switch priority value; for example 802.1p 0 maps to switch priority 0.

To map 802.1p 4 to switch priority 0, configure the `traffic.cos_0.priority_source.8021p` setting to 4.

```
traffic.cos_0.priority_source.8021p = [4]
```

You can map multiple values to the same switch priority value. For example, to map 802.1p values 0, 1, and 2 to switch priority 0:

```
traffic.cos_0.priority_source.8021p = [0, 1, 2]
```

You can also choose not to use a switch priority value. This example does not use switch priority values 3 and 4.

```
traffic.cos_0.priority_source.8021p = [0]
traffic.cos_1.priority_source.8021p = [1]
traffic.cos_2.priority_source.8021p = [2,3,4]
traffic.cos_3.priority_source.8021p = []
traffic.cos_4.priority_source.8021p = []
traffic.cos_5.priority_source.8021p = [5]
traffic.cos_6.priority_source.8021p = [6]
traffic.cos_7.priority_source.8021p = [7]
```

{{< /tab >}}
{{< /tabs >}}

To apply a custom profile to specific interfaces, see [Port Groups](#port-groups).

### Trust DSCP

To trust ingress DSCP markings:

{{< tabs "TabID138 ">}}
{{< tab "NVUE Commands ">}}

If DSCP (`l3`) is `trusted`, Cumulus Linux classifies these ingress DSCP values to switch priority values:

| Switch Priority | Ingress DSCP |
|------------- | ------------ |
| 0 | [0,1,2,3,4,5,6,7]|
| 1 | [8,9,10,11,12,13,14,15]|
| 2 | [16,17,18,19,20,21,22,23]|
| 3 | [24,25,26,27,28,29,30,31]|
| 4 | [32,33,34,35,36,37,38,39]|
| 5 | [40,41,42,43,44,45,46,47]|
| 6 | [48,49,50,51,52,53,54,55]|
| 7 | [56,57,58,59,60,61,62,63]|

The DSCP number is the ingress DSCP value; for example DSCP 0 through 7 maps to switch priority 0.

To change the default profile to map ingress DSCP 22 to switch priority 4:

```
cumulus@switch:~$ nv set qos mapping default-global trust l3 
cumulus@switch:~$ nv set qos mapping default-global dscp 22 switch-priority 4 
cumulus@switch:~$ nv config apply
```

You can map multiple ingress DSCP values to the same switch priority value. For example, to change the default profile to map ingress DSCP values 10, 21, and 36 to switch priority 0:

```
cumulus@switch:~$ nv set qos mapping default-global trust l3 
cumulus@switch:~$ nv set qos mapping default-global dscp 10,21,36 switch-priority 0
cumulus@switch:~$ nv config apply
```

If you configure the trust to be `l3` but do not specify any DSCP to switch priority mappings, Cumulus Linux uses the default values.

To show the DSCP mapping in the default profile, run the `nv show qos mapping default-global dscp` command. To show the DSCP mapping for a specific switch priority in the default profile, run the `nv show qos mapping default-global dscp <value>` command. The following example shows that DSCP 22 maps to switch priority 4:

```
cumulus@switch:~$ nv show qos mapping default-global dscp 22
                 operational  applied  description
---------------  -----------  -------  ------------------------
switch-priority  4            4        Internal Switch Priority
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/cumulus/datapath/qos/qos_features.conf` file, configure `traffic.packet_priority_source_set = [dscp]`.

If DSCP is `trusted`, the following lines classify ingress DSCP values to switch priority (internal COS) values:

```
traffic.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]
traffic.cos_1.priority_source.dscp = [8,9,10,11,12,13,14,15]
traffic.cos_2.priority_source.dscp = [16,17,18,19,20,21,22,23]
traffic.cos_3.priority_source.dscp = [24,25,26,27,28,29,30,31]
traffic.cos_4.priority_source.dscp = [32,33,34,35,36,37,38,39]
traffic.cos_5.priority_source.dscp = [40,41,42,43,44,45,46,47]
traffic.cos_6.priority_source.dscp = [48,49,50,51,52,53,54,55]
traffic.cos_7.priority_source.dscp = [56,57,58,59,60,61,62,63]
```

{{% notice note %}}
The `#` in the configuration file is a comment. By default, the file comments out the `traffic.cos_*.priority_source.dscp` lines.  
You must uncomment them for them to take effect.  
{{% /notice %}}

The `traffic.cos_` number is the switch priority value; for example DSCP values 0 through 7 map to switch priority 0. To map ingress DSCP 22 to switch priority 4, configure the `traffic.cos_4.priority_source.dscp` setting.

```
traffic.cos_4.priority_source.dscp = [22]
```

You can map multiple ingress DSCP values to the same switch priority value. For example, to map ingress DSCP values 10, 21, and 36 to switch priority 0:

```
traffic.cos_0.priority_source.dscp = [10,21,36]
```

You can also choose not to use an switch priority value. This example does not use switch priority values 3 and 4:

```
traffic.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]
traffic.cos_1.priority_source.dscp = [8,9,10,11,12,13,14,15]
traffic.cos_2.priority_source.dscp = [16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
traffic.cos_3.priority_source.dscp = []
traffic.cos_4.priority_source.dscp = []
traffic.cos_5.priority_source.dscp = [40,41,42,43,44,45,46,47,32,33,34,35,36,37,38,39]
traffic.cos_6.priority_source.dscp = [48,49,50,51,52,53,54,55]
traffic.cos_7.priority_source.dscp = [56,57,58,59,60,61,62,63]
```

{{< /tab >}}
{{< /tabs >}}

To apply a custom DSCP profile to specific interfaces, see [Port Groups](#port-groups).

### Trust Port

You can assign all traffic to a switch priority regardless of the ingress marking.

{{< tabs "TabID183 ">}}
{{< tab "NVUE Commands ">}}

The following commands assign all traffic to switch priority 3 regardless of the ingress marking.

```
cumulus@switch:~$ nv set qos mapping default-global trust port 
cumulus@switch:~$ nv set qos mapping default-global port-default-sp 3 
cumulus@switch:~$ nv config apply
```

To show the switch priority setting in the default profile for all traffic regardless of the ingress marking, run the `nv show qos mapping default-global` command:

```
cumulus@switch:~$ nv show qos mapping default-global
                 operational  applied  description
---------------  -----------  -------  ----------------------------
port-default-sp  3            3        Port Default Switch Priority
trust            port         port     Port Trust configuration
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/cumulus/datapath/qos/qos_features.conf` file, configure `traffic.packet_priority_source_set = [port]`.

The `traffic.port_default_priority` setting defines the switch priority that all traffic uses.

{{< /tab >}}
{{< /tabs >}}

To apply a custom profile to specific interfaces, see [Port Groups](#port-groups).

## Mark and Remark Traffic

{{%notice note%}}
NVUE does not currently provide commands to mark or remark traffic.
{{%/notice%}}

You can mark or remark traffic in two ways:

 * Use [iptables](#iptables) to match packets and set 802.1p COS or DSCP values.
 * Use ingress COS or DSCP to remark an existing 802.1p COS or DSCP value to a new value.

### iptables

Cumulus Linux supports ACLs through `ebtables`, `iptables` or `ip6tables` for _egress_ packet marking and remarking.

Cumulus Linux uses `ebtables` to mark layer 2, 802.1p COS values.
Cumulus Linux uses `iptables` to match IPv4 traffic and `ip6tables` to match IPv6 traffic for DSCP marking.

{{% notice info %}}
For more information on configuring and applying ACLs, refer to {{<link title="Netfilter - ACLs" text="Netfilter - ACLs" >}}.
{{% /notice %}}

#### Mark Layer 2 COS

You must use `ebtables` to match and mark layer 2 bridged traffic. You can match traffic with any supported ebtables rule.  

To set the new 802.1p COS value when traffic matches, use `-A FORWARD -o <interface> -j setqos --set-cos <value>`.

{{% notice info %}}
You can only set COS on a *per-egress interface* basis. Cumulus Linux does not support `ebtables` based matching on ingress.
{{% /notice %}}

The configured action always has the following conditions:
- The rule is always part of the `FORWARD` chain.
- The interface (`<interface>`) is a physical swp port.
- The *jump* action is always `setqos` (lowercase).
- The `--set-cos` value is a 802.1p COS value between 0 and 7.

For example, to set traffic leaving interface `swp5` to 802.1p COS value `4`:

```
-A FORWARD -o swp5 -j setqos --set-cos 4
```

#### Mark Layer 3 DSCP

You must use `iptables` (for IPv4 traffic) or `ip6tables` (for IPv6 traffic) to match and mark layer 3 traffic.

You can match traffic with any supported iptable or ip6tables rule.
To set the new COS or DSCP value when traffic matches, use `-A FORWARD -o <interface> -j SETQOS [--set-dscp <value> | --set-cos <value> | --set-dscp-class <name>]`.

The configured action always has the following conditions:
- The rule is always configured as part of the `FORWARD` chain.
- The interface (`<interface>`) is a physical swp port.
- The *jump* action is always `SETQOS` (uppercase).

You can configure COS markings with `--set-cos` and a value between 0 and 7 (inclusive).

You can use only one of `--set-dscp` or `--set-dscp-class`.  
`--set-dscp` supports decimal or hex DSCP values between 0 and 77.
`--set-dscp-class` supports standard DSCP naming, described in [RFC3260](https://datatracker.ietf.org/doc/html/rfc3260), including `ef`, `be`, CS and AF classes.

{{%notice note%}}
You can specify either `--set-dscp` or `--set-dscp-class`, but not both.
{{%/notice%}}

For example, to set traffic leaving interface swp5 to DSCP value `32`:

```
-A FORWARD -o swp5 -j SETQOS --set-dscp 32
```

To set traffic leaving interface swp11 to DSCP class value `CS6`:

```
-A FORWARD -o swp11 -j SETQOS --set-dscp-class cs6
```
<!-- vale off -->
### 802.1p or DSCP for Marking
<!-- vale on -->
To enable global remarking of 802.1p, DSCP or both 802.1p and DSCP values, modify the `traffic.packet_priority_remark_set` value to `[802.1p]`, `[dscp]` or `[802.1p,dscp]` in the `/etc/cumulus/datapath/qos/qos_features.conf` file. For example, to enable the remarking of only 802.1p values:

```
traffic.packet_priority_remark_set = [802.1p]
```

You remark 802.1p or DSCP with the `priority_remark.8021p` or `priority_remark.dscp` setting. The switch priority (internal `cos_`) value determines the egress 802.1p or DSCP remarking. For example, to remark switch priority 0 to egress 802.1p 4:

```
traffic.cos_0.priority_remark.8021p = [4]
```

To remark switch priority 0 to egress DSCP 22:

```
traffic.cos_0.priority_remark.dscp = [22]
```

{{% notice note %}}
The `#` in the configuration file is a comment. The file comments out the `traffic.cos_*.priority_remark.8021p` and the `traffic.cos_*.priority_remark.dscp` lines by default. You must uncomment them to set the configuration.
{{% /notice %}}

You can remap multiple switch priority values to the same external 802.1p or DSCP value. For example, to map switch priority 1 and 2 to 802.1p 3:

```
traffic.cos_1.priority_remark.8021p = [3]
traffic.cos_2.priority_remark.8021p = [3]
```

To map switch priority 1 and 2 to DSCP 40:

```
traffic.cos_1.priority_remark.dscp = [40]
traffic.cos_2.priority_remark.dscp = [40]
```

To apply a custom profile to specific interfaces, see [Port Groups](#remarking).

## Flow Control

Congestion control prevents traffic loss during times of congestion and helps identify which traffic to keep if you need to drop packets.

Cumulus Linux supports the following congestion control mechanisms:

- Pause Frames (IEEE 802.3x), sends specialized ethernet frames to an adjacent layer 2 switch to stop or *pause* **all** traffic on the link during times of congestion.
- Priority Flow Control (PFC), which is an upgrade of Pause Frames that IEEE 802.1bb defines, extends the pause frame concept to act on a per-COS value basis instead of an entire link. A PFC pause frame indicates to the peer which specific COS value to pause, while other COS values or queues continue transmitting.
- Explicit Congestion Notification (ECN). Unlike Pause Frames and PFC that operate only at layer 2, ECN is an end-to-end layer 3 congestion control protocol. Defined by RFC 3168, ECN relies on bits in the IPv4 header Traffic Class to signal congestion conditions. ECN requires one or both server endpoints to support ECN to be effective.

### Flow Control Buffers

Before configuring pause frames or PFC, configure the buffer pool memory allocated for lossless and lossy flows. The following example sets each to fifty percent:

{{< tabs "TabID445 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set qos traffic-pool default-lossless memory-percent 50
cumulus@switch:~$ nv set qos traffic-pool default-lossy memory-percent 50
cumulus@switch:~$ nv config apply
```

{{%notice note%}}
Cumulus Linux allocates 100% of the buffer memory to the default-lossy traffic pool by default. The total memory allocation across pools must not exceed 100%.
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the following lines in the `/etc/mlx/datapath/qos/qos_infra.conf` file:

1. Modify the existing `ingress_service_pool.0.percent` and `egress_service_pool.0.percent` buffer allocation. Change the existing ingress setting to `ingress_service_pool.0.percent = 50`. Change the existing egress setting to `egress_service_pool.0.percent = 50`.

2. Add the following lines to create a new `service_pool`, set `flow_control` to the service pool, and define buffer reservations:

```
ingress_service_pool.1.percent = 50.0
ingress_service_pool.1.mode = 1
egress_service_pool.1.percent = 50.0
egress_service_pool.1.mode = 1
egress_service_pool.1.infinite_flag = TRUE
#
flow_control.ingress_service_pool = 1
flow_control.egress_service_pool = 1
#
port.service_pool.1.ingress_buffer.reserved = 0
port.service_pool.1.ingress_buffer.dynamic_quota = ALPHA_1
port.service_pool.1.egress_buffer.uc.reserved = 0
port.service_pool.1.egress_buffer.uc.dynamic_quota = ALPHA_INFINITY
#
flow_control.ingress_buffer.dynamic_quota = ALPHA_1
flow_control.egress_buffer.reserved = 0
flow_control.egress_buffer.dynamic_quota = ALPHA_INFINITY
```

{{< /tab >}}
{{< /tabs >}}

### Pause Frames

{{%notice note%}}
NVUE does not currently provide commands to configure pause frames.
{{%/notice%}}

Pause frames are an older congestion control mechanism that causes all traffic on a link between two devices (two switches or a host and switch) to stop transmitting during times of congestion. Pause frames start and stop depending on how congested the buffer is. The value that determines when pause frames start is the `xoff` value (transmit off). When the buffer congestion reaches the `xoff` point, the switch sends a pause frame to one or more neighbors. When congestion drops below the `xon` point (transmit on), the switch sends an updated pause frame so that the neighbor resumes sending traffic.

{{% notice note %}}
NVIDIA recommends that you use Priority Flow Control (PFC) instead of pause frames.
{{% /notice  %}}

{{% notice note %}}
Before configuring pause frames, you must first modify the switch buffer allocation. Refer to {{<link title="#Flow Control Buffers" text="Flow Control Buffers">}}.
{{% /notice %}}

You configure pause frames on a per-direction, per-interface basis under the `link_pause` section of the `qos_features.conf` file.  
Setting `link_pause.pause_port_group.rx_enable = true` receives pause frames to stop the switch from transmitting when requested.
Setting `link_pause.pause_port_group.tx_enable = true` sends pause frames to request neighboring devices to stop transmitting.
You can use pause frames for either receive (`rx`), transmit (`tx`), or both.

{{% notice note %}}
Cumulus Linux automatically enables or derives the following settings when link pause is on an interface with `link_pause.port_group_list`:

- `link_pause.pause_port_group.rx_enable`
- `link_pause.pause_port_group.tx_enable`
- `link_pause.pause_port_group.port_buffer_bytes`
- `link_pause.pause_port_group.xoff_size`
- `link_pause.pause_port_group.xon_delta`

To process pause frames, you must enable link pause on the specific interfaces.
{{% /notice %}}

The following is an example `link_pause` configuration.

```
link_pause.port_group_list = [my_pause_ports]
link_pause.my_pause_ports.port_set = swp1-swp4,swp6
```

{{% notice warning %}}
Pause frame buffer calculation is a complex topic that IEEE 802.1Q-2012 defines. This attempts to incorporate the delay between signaling congestion and the reception of the signal by the neighboring device. This calculation includes the delay that the PHY and MAC layers (interface delay) introduce as well as the distance between end points (cable length).

Incorrect cable length settings can cause wasted buffer space (triggering congestion too early) or packet drops (congestion occurs before flow control activates).
{{% /notice %}}

<details>
<summary>All Link Pause configuration options</summary>

|Configuration |Description |
|------------- |----------- |
|`link_pause.port_group_list` |The port group (label) to use with pause frame settings.<br>In the following example, the group is `my_pause_ports`:<br>`link_pause.port_group_list = [my_pause_ports]`  |
|`link_pause.my_pause_ports.port_set` | The set of interfaces on which to apply pause frame configuration.<br>In the following example, swp1, swp2, swp3, swp4 and swp6 have pause frame on:<br>`link_pause.my_pause_ports.port_set = swp1-swp4,swp6` |
|`link_pause.my_pause_ports.port_buffer_bytes`|The amount of reserved buffer space for the set of ports in the port group list (reserved from the global shared buffer).<br>The following example sets the amount of reserved buffer space to 25000 bytes:<br>`link_pause.my_pause_ports.port_buffer_bytes = 25000` |
|`link_pause.my_pause_ports.xoff_size`  | The amount of reserved buffer to consume before the switch sends a pause frame out of the set of interfaces in the port group list.<br>In the following example, after you consume 10000 bytes of reserved buffer, the switch sends pause frames:<br>`link_pause.my_pause_ports.xoff_size = 10000` |
|`link_pause.my_pause_ports.xon_delta` |The number of bytes below the `xoff` threshold that the buffer consumption must drop below before sending pause frame stops.<br>In the following example, the buffer congestion must reduce by 2000 bytes (to 8000 bytes) before pause frame stops:<br>`link_pause.my_pause_ports.xon_delta = 2000` |
|`link_pause.my_pause_ports.rx_enable` |Enables (`true`) or disables (`false`) sending pause frames. The default value is `true`.<br>In the following example, sending pause frames is on:<br>`link_pause.my_pause_ports.tx_enable = true`  |
|`link_pause.my_pause_ports.tx_enable`  |Enables (`true`) or disables (`false`) the switch to receive pause frames. The default value is `true`.<br>In the following example, the receiving pause frames is on:<br>`link_pause.my_pause_ports.rx_enable = true` |
|`link_pause.my_pause_ports.cable_length` | The length, in meters, of the cable that attaches to the port in the port group list. Cumulus Linux uses this value internally to determine the latency between generating a pause frame and receiving the pause frame. The default is `100` meters.<br>In the following example, the attached cable is `5` meters:<br>`link_pause.pause_port_group.cable_length = 5`|
</details>

### Priority Flow Control (PFC)

Priority flow control extends the capabilities of pause frames by the frames for a specific 802.1p value instead of stopping all traffic on a link. If a switch supports PFC and receives a PFC pause frame for a given 802.1p value, the switch stops transmitting frames from that queue, but continues transmitting frames for other queues.

You use PFC with {{<link title="RDMA over Converged Ethernet - RoCE" text="RDMA over Converged Ethernet - RoCE">}}. The RoCE section provides information to specifically deploy PFC and ECN for RoCE environments.

{{% notice note %}}
Before configuring PFC, first modify the switch buffer allocation according to {{<link title="#Flow Control Buffers" text="Flow Control Buffers">}}.
{{% /notice %}}

{{% notice warning %}}
PFC buffer calculation is a complex topic defined in IEEE 802.1Q-2012, which attempts to incorporate the delay between signaling congestion and receiving the signal by the neighboring device. This calculation includes the delay that the PHY and MAC layers (called the interface delay) introduce as well as the distance between end points (cable length).  
Incorrect cable length settings cause wasted buffer space (triggering congestion too early) or packet drops (congestion occurs before flow control activates).
{{% /notice %}}

To apply PFC settings on all ports, modify the default PFC profile (`default-global`).

The following example modifies the default profile and configures:
- PFC on egress queue 0.
- The buffer limit that triggers PFC frame transmission to stop to 1500 bytes and to start to 1000 bytes.
- The amount of reserved buffer space to 2000 bytes.
- The cable length to 50 meters.

{{< tabs "TabID535 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set qos pfc default-global switch-priority 0 
cumulus@switch:~$ nv set qos pfc default-global xoff-threshold 1500 
cumulus@switch:~$ nv set qos pfc default-global xon-threshold 1000 
cumulus@switch:~$ nv set qos pfc default-global tx enable 
cumulus@switch:~$ nv set qos pfc default-global rx disable 
cumulus@switch:~$ nv set qos pfc default-global port-buffer 2000 
cumulus@switch:~$ nv set qos pfc default-global cable-length 50
cumulus@switch:~$ nv config apply
```

To show the PFC settings for the default profile, run the `nv show qos pfc default-global` command:

```
cumulus@switch:~$ nv show qos pfc default-global
                   operational  applied  description
-----------------  -----------  -------  --------------------------------
cable-length       50           50       Cable Length (in meters)
port-buffer        2000 B       2000 B   Port Buffer (in bytes)
rx                 disable      disable  PFC Rx State
tx                 enable       enable   PFC Tx State
xoff-threshold     1500 B       1500 B   Xoff Threshold (in bytes)
xon-threshold      1000 B       1000 B   Xon Threshold (in bytes)
[switch-priority]  0            0        Collection of switch priorities.
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `priority flow control` section of the `/etc/cumulus/datapath/qos/qos_features.conf` file.

```
pfc.port_group_list = [default-global]
pfc.default-global.port_set = allports
pfc.default-global.cos_list = [0]
pfc.default-global.port_buffer_bytes = 2000
pfc.default-global.xoff_size = 1500
pfc.default-global.xon_delta = 500
pfc.default-global.tx_enable = true
pfc.default-global.rx_enable = false
pfc.default-global.cable_length = 50
```

{{< /tab >}}
{{< /tabs >}}

To apply a custom profile to specific interfaces, see [Port Groups](#pfc).

### Explicit Congestion Notification (ECN)

Unlike pause frames or PFC, ECN is an end-to-end flow control technology. Instead of telling adjacent devices to stop transmitting during times of buffer congestion, ECN sets the ECN bits of the transit IPv4 or IPv6 header to indicate to end hosts that congestion might occur. As a result, the sending hosts reduce their sending rate until the transit switch no longer sets ECN bits.

You use ECN with {{<link title="RDMA over Converged Ethernet - RoCE" text="RDMA over Converged Ethernet - RoCE">}}. The RoCE section describes how to deploy PFC and ECN for RoCE environments.

ECN operates by having a transit switch that marks packets between two end hosts.
1. The transmitting host indicates it is ECN-capable by setting the ECN bits in the outgoing IP header to `01` or `10`
2. If the buffer of a transit switch is greater than the configured minimum threshold of the buffer, the switch remarks the ECN bits to `11` indicating *Congestion Encountered* or *CE*.
3. The receiving host marks any reply packets, like a TCP-ACK, as CE (`11`).
4. The original transmitting host reduces its transmission rate.
5. When the switch buffer congestion falls below the configured minimum threshold of the buffer, the switch stops remarking ECN bits, setting them back to `01` or `10`.
6. A receiving host reflects this new ECN marking in the next reply so that the transmitting host resumes sending at normal speeds.

The default profile (`default-global`) enables ECN by default on egress queue 0 for all ports with the following settings:
- A minimum buffer threshold of 150000 bytes. Random ECN marking starts when buffer congestion crosses this threshold. The probability determines if ECN marking occurs.
- A maximum buffer threshold of 1500000 bytes. Cumulus Linux marks all ECN-capable packets when buffer congestion crosses this threshold.
- A probability of 100 percent that Cumulus Linux marks an ECN-capable packet when buffer congestion is between the minimum threshold and the maximum threshold.
- Random Early Detection (RED) disabled. ECN prevents packet drops in the network due to congestion by signaling hosts to transmit less. However, if congestion continues after ECN marking, packets drop after the switch buffer is full. By default, Cumulus Linux tail-drops packets when the buffer is full. You can enable RED to drop packets that are in the queue randomly instead of always dropping the last arriving packet. This might improve overall performance of TCP based flows.

The following example commands change the default ECN profile that applies to all ports. The commands enable ECN on egress queue 4, 5, and 7, set the minimum buffer threshold to 40000 and the maximum buffer threshold to 200000, and enable RED.

{{< tabs "TabID480 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 min-threshold 40000
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 max-threshold 200000 
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 4,5,7 red enable
cumulus@switch:~$ nv config apply
```

The following example disables ECN bit marking in the default profile for all ports.

```
cumulus@switch:~$ nv set qos congestion-control default-global traffic-class 0 ecn disable
cumulus@switch:~$ nv config apply
```

To show the ECN settings for the default profile, run the `nv show qos congestion-control default-global` command:

```
cumulus@switch:~$ nv show qos congestion-control default-global
    operational  applied  description
--  -----------  -------  -----------

ECN Configurations
=====================
    traffic-class  ECN     RED     Min Th   Max Th    Probability
    -------------  ------  ------  -------  --------  -----------
    4              enable  enable  40000 B  200000 B  100
    5              enable  enable  40000 B  200000 B  100
    7              enable  enable  40000 B  200000 B  100
```

To show the ECN settings in the default profile for a specific egress queue, run the `nv show qos congestion-control default-global traffic-class <value>` command:

```
cumulus@switch:~$ nv show qos congestion-control default-global traffic-class 4 
               operational  applied   description
-------------  -----------  --------  -----------------------------------
ecn            enable       enable    Early Congestion Notification State
max-threshold  200000 B     200000 B  Maximum Threshold (in bytes)
min-threshold  40000 B      40000 B   Minimum Threshold (in bytes)
probability    100          100       Probability
red            enable       enable    Random Early Detection State
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Explicit Congestion Notification` section of the `/etc/cumulus/datapath/qos/qos_features.conf` file.

```
default_ecn_red_conf.egress_queue_list = [4,5,7]
default_ecn_red_conf.ecn_enable = true
default_ecn_red_conf.red_enable = true
default_ecn_red_conf.min_threshold_bytes = 40000
default_ecn_red_conf.max_threshold_bytes = 200000
default_ecn_red_conf.probability = 100
```

To disable ECN bit marking, set `ecn_enable` to false. The following example disables ECN bit marking in the default profile for all ports.

```
...
default_ecn_red_conf.ecn_enable = false 
...
```

{{< /tab >}}
{{< /tabs >}}

To apply a custom ECN profile to specific interfaces, see [Port Groups](#ecn).

## Egress Queues

Cumulus Linux supports eight egress queues to provide different classes of service. By default switch priority values map directly to the matching egress queue. For example, switch priority value 0 maps to egress queue 0.

You can remap queues by changing the switch priority value to the corresponding queue value. You can map multiple switch priority values to a single egress queue.

{{% notice note %}}
You do not have to assign all egress queues.
{{% /notice %}}

The following command examples assign switch priority 2 to egress queue 7:

{{< tabs "TabID580 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set qos egress-queue-mapping default-global switch-priority 2 traffic-class 7
cumulus@switch:~$ nv config apply
```

NVUE only supports the `default-global` profile.

To show the egress queue mapping configuration for the default profile, run the `nv show qos egress-queue-mapping default-global` command:

```
cumulus@switch:~$ nv show qos egress-queue-mapping default-global
    operational  applied  description
--  -----------  -------  -----------

SP->TC mapping configuration
===============================
    switch-priority  traffic-class
    ---------------  -------------
    0                0
    1                1
    2                7
    3                3
    4                4
    5                5
    6                6
    7                7
```

To show the egress queue mapping for a specific switch priority in the default profile, run the `nv show qos egress-queue-mapping default-global switch-priority <value>` command. The following example command shows that switch priority 2 maps to egress queue 7.

```
cumulus@switch:~$ nv show qos egress-queue-mapping default-global switch-priority 2
               operational  applied  description
-------------  -----------  -------  -------------
traffic-class  7            7        Traffic Class
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You configure egress queues in the `qos_infra.conf` file.

```
cos_egr_queue.cos_0.uc  = 0
cos_egr_queue.cos_1.uc  = 1
cos_egr_queue.cos_2.uc  = 7
cos_egr_queue.cos_3.uc  = 3
cos_egr_queue.cos_4.uc  = 4
cos_egr_queue.cos_5.uc  = 5
cos_egr_queue.cos_6.uc  = 6
cos_egr_queue.cos_7.uc  = 7
```

{{< /tab >}}
{{< /tabs >}}

## Egress Scheduler

Cumulus Linux supports 802.1Qaz, Enhanced Transmission Selection, which allows the switch to assign bandwidth to egress queues and then schedule the transmission of traffic from each queue. 802.1Qaz supports Priority Queuing.

Cumulus Linux provides a default egress scheduler that applies to all ports, where the bandwidth allocated to egress queues 0,2,4,6 is 12 percent and the bandwidth allocated to egress queues 1,3,5,7 is 13 percent. You can also apply a custom egress scheduler for specific ports; see [Port Groups](#egress-scheduling).

The following example modifies the default profile. The commands change the bandwidth allocation for egress queues 0, 1, 5, and 7 to strict, bandwidth allocation for egress queues 2 and 6 to 30 percent and bandwidth allocation for egress queues 3 and 4 to 20 percent.

{{< tabs "TabID546 ">}}
{{< tab "NVUE Commands ">}}

- The `traffic-class` value defines the [egress queue](#egress-queues) where you want to assign bandwidth. For example, `traffic-class 2` defines the bandwidth allocation for egress queue 2.
- For each egress queue, you can either define the mode as `dwrr` or `strict`. In `dwrr` mode, you must define a bandwidth percent value between 1 and 100. If you do not specify a value for an egress queue, Cumulus Linux uses a DWRR value of 0 (no egress scheduling). The combined total of values you assign to `bw_percent` must be less than or equal to 100.

```
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 2,6 mode dwrr 
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 2,6 bw-percent 30 
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 3,4 mode dwrr
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 3,4 bw-percent 20 
cumulus@switch:~$ nv set qos egress-scheduler default-global traffic-class 0,1,5,7 mode strict
cumulus@switch:~$ nv config apply
```

To show the egress scheduling policy for the default profile, run the `nv show qos egress-scheduler default-global` command:

```
cumulus@switch:~$ nv show qos egress-scheduler default-global
    operational  applied  description
--  -----------  -------  -----------

TC->DWRR weight configuration
================================
    traffic-class  mode    bw-percent
    -------------  ------  ----------
    0              strict
    1              strict
    2              dwrr    30
    3              dwrr    20
    4              dwrr    20
    5              strict
    6              dwrr    30
    7              strict
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You configure the egress scheduling policy in the `egress scheduling` section of the `/etc/cumulus/datapath/qos/qos_features.conf` file.
- The `egr_queue_` value defines the [egress queue](#egress-queues) where you want to assign bandwidth. For example, `egr_queue_0` defines the bandwidth allocation for egress queue 0.
- The `bw_percent` value defines the bandwidth allocation you want to assign to an egress queue. If you do not specify a value for an egress queue, there is no egress scheduling. If you specify a value of 0 for an egress queue, Cumulus Linux assigns `strict` priority mode to the egress queue and always processes it ahead of other queues. The combined total of values you assign to `bw_percent` must be less than or equal to 100.

```
default_egress_sched.egr_queue_0.bw_percent = 0
default_egress_sched.egr_queue_1.bw_percent = 0
default_egress_sched.egr_queue_2.bw_percent = 30
default_egress_sched.egr_queue_3.bw_percent = 20
default_egress_sched.egr_queue_4.bw_percent = 20
default_egress_sched.egr_queue_5.bw_percent = 0
default_egress_sched.egr_queue_6.bw_percent = 30
default_egress_sched.egr_queue_7.bw_percent = 0
```

{{< /tab >}}
{{< /tabs >}}

{{% notice note %}}
`strict` mode does not define a maximum bandwidth allocation. This can lead to starvation of other queues.
{{% /notice %}}

To apply a custom egress scheduler for specific ports, see [Port Groups](#egress-scheduling).

## Policing and Shaping

{{%notice note%}}
NVUE does not currently provide commands to configure traffic shaping and policing.
{{%/notice%}}

Traffic shaping and policing control the rate at which the switch sends or receives traffic on a network to prevent congestion.

{{% notice note %}}
Traffic shaping typically occurs at egress and traffic policing at ingress.
{{% /notice %}}

### Shaping

Traffic shaping allows a switch to send traffic at an average bitrate lower than the physical interface. Traffic shaping prevents a receiving device from dropping bursty traffic if the device is either not capable of that rate of traffic or has a policer that limits what it accepts; for example, an ISP.

Traffic shaping works by holding packets in the buffer and releasing them at time intervals called the `tc`.

Cumulus Linux supports two levels of hierarchical traffic shaping: one at the egress queue level and one at the port level. This allows for minimum and maximum bandwidth guarantees for each egress-queue and a defined interface traffic shaping rate.

You configure traffic shaping in the `shaping` section of the `qos_features.conf` file. Traffic shaping configuration supports [Port Groups](#using-port-groups) so that you can apply different shaping profiles to different ports.

Cumulus Linux bases the `egr_queue` value on the configured [egress queue](#egress-queues).

This is an example traffic shaping configuration:

```
shaping.port_group_list = [shaper_port_group]
shaping.shaper_port_group.port_set = swp1-swp3,swp5
shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]
shaping.shaper_port_group.port.shaper = 900000
```

<details>
<summary>All Shaping configuration options</summary>

|Configuration  |Description|
|-------------  |---------- |
|`shaping.port_group_list`  | The port group (label) to use with traffic shaping settings.<br>In the following example, the group is `shaper_port_group`:<br>`shaping.port_group_list = [shaper_port_group]` |
|`shaping.shaper_port_group.port_set` | The set of interfaces on which you want to apply traffic shaping.<br>The following example applies traffic shaping on swp1, swp2, swp3, and swp5:<br>`shaping.shaper_port_group.port_set = swp1-swp3,swp5` |
|`shaping.shaper_port_group.egr_queue_0.shaper`| The minimum and maximum bandwidth value in kbps for switch priority group 0.<br>In the following example, switch priority 0 always has at least `50000` kbps of bandwidth with a maximum of `100000` kbps:<br>`shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]` |
|`shaping.shaper_port_group.port.shaper` | The maximum packet shaper rate at the interface level.<br>In the following example, swp1, swp2, swp3, and swp5 do not transmit greater than `900000` kbps:<br>`shaping.shaper_port_group.port.shaper = 900000`|
</details>

If you define a queue minimum shaping value of `0`, there is no bandwidth guarantee for this queue. The maximum queue shaping value must not exceed the interface shaping value defined by `port.shaper`. The `port.shaper` value must not exceed the physical interface speed.

<!--### PTP Shaping

To improve performance on the NVIDIA Spectrum 1 switch for PTP-enabled ports with speeds lower than 100G, you can configure traffic shaping.

{{%notice note%}}
PTP shaping is not supported on Spectrum-2 and later.
{{%/notice%}}

{{< tabs "TabID1387 ">}}
{{< tab "NVUE Commands ">}}

For each PTP-enabled port, run the `nv set interface <swp> qos egress-shaper ptp-shaper profile <profile-name>` command.

```
cumulus@switch:~$ nv set interface swp1 qos egress-shaper ptp-shaper profile ptp-profile
cumulus@switch:~$ nv set interface swp2 qos egress-shaper ptp-shaper profile ptp-profile
cumulus@switch:~$ nv set interface swp3 qos egress-shaper ptp-shaper profile ptp-profile
cumulus@switch:~$ nv set interface swp5 qos egress-shaper ptp-shaper profile ptp-profile
cumulus@switch:~$ nv config apply
```

The NVUE command adds the PTP shaping configuration for the specified ports to the `qos_features.conf` file. To see the profile settings, run the `nv show qos egress-shaper ptp-shaper profile <profile-name>` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `shaping` section of the `qos_features.conf` file, add the following:
- A port group to use with traffic shaping settings.
- The set of interfaces to which you want apply traffic shaping.
- The minimum and maximum bandwidth value in kbps for internal COS group 0.
- The maximum packet shaper rate at the interface level.

```
ptp_shaping.port_group_list = [ptp_shaper_port_group_speed_1G]
ptp_shaping.shaper_port_group.port_set = swp1-swp3,swp5
ptp_shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]
ptp_shaping.shaper_port_group.port.shaper = 900000
```

{{< /tab >}}
{{< /tabs >}}
-->
### Policing

Traffic policing prevents an interface from receiving more traffic than intended. You use policing to enforce a maximum transmission rate on an interface. The switch drops any traffic above the policing level.

Cumulus Linux supports both a single-rate policer and a dual-rate policer (*tricolor policer*).

You configure traffic policing using ebtables, iptables, or ip6table rules.

{{% notice info %}}
For more information on configuring and applying ACLs, refer to {{<link title="Netfilter - ACLs" text="Netfilter - ACLs" >}}.
{{% /notice %}}
<!-- vale off -->
#### Single-rate Policer
<!-- vale on -->
To configure a single-rate policer, use iptables `JUMP` action `-j POLICE`.

Cumulus Linux supports the following iptable flags with a single-rate policer.

| iptables Flag | Description |
| ---  | --- |
| `--set-mode [pkt \| KB]` | Define the policer to count packets or kilobytes. |
| `--set-rate [<kbytes> \| <packets>]` | The maximum rate of traffic in kilobytes or packets per second. |
| `--set-burst <kilobytes>` | The allowed burst size in kilobytes. |

For example, to create a policer to allow 400 packets per second with 100 packet burst:  
`-j POLICE --set-mode pkt --set-rate 400 --set-burst 100`
<!-- vale off -->
#### Dual-rate Policer
<!-- vale on -->
To configure a dual-rate policer, use the iptables `JUMP` action `-j TRICOLORPOLICE`.

Cumulus Linux supports the following iptable flags with a dual-rate policer.

| iptables Flag | Description |
| ---  | --- |
| `--set-color-mode [blind \| aware]` |The policing mode: single-rate (`blind`) or dual-rate (`aware`). The default is `aware`. |
| `--set-cir <kbps>` | The committed information rate (CIR) in kilobits per second. |
| `--set-cbs <kbytes>` | The committed burst size (CBS) in kilobytes. |
| `--set-pir <kbps>` |  The peak information rate (PIR) in kilobits per second. |
| `--set-ebs <kbytes>` | The excess burst size (EBS) in kilobytes. |
| `--set-conform-action-dscp <dscp value>` | The numerical DSCP value to mark for traffic that conforms to the policer rate. |
| `--set-exceed-action-dscp <dscp value>` | The numerical DSCP value to mark for traffic that exceeds the policer rate. |
| `--set-violate-action-dscp <dscp value>` | The numerical DSCP value to mark for traffic that violates the policer rate. |
| `--set-violate-action [accept \| drop]` | Cumulus Linux either accepts and remarks, or drops packets that violate the policer rate. |

For example, to configure a dual-rate, three-color policer, with a 3 Mbps CIR, 500 KB CBS, 10 Mbps PIR, and 1 MB EBS and drops packets that violate the policer:

`-j TRICOLORPOLICE --set-color-mode blind --set-cir 3000 --set-cbs 500 --set-pir 10000 --set-ebs 1000 --set-violate-action drop`

## Port Groups

Cumulus Linux supports profiles (port groups) for all features including [ECN](#explicit-congestion-notification-ecn) and [RED](#random-early-detection-red). Profiles apply similar QoS configurations to a set of ports.

{{% notice note %}}
- Configurations with a profile override the global settings for the ingress ports in the port group.
- Ports not in a profile use the global settings.
- To apply a profile to all ports, use the global profile.
{{% /notice %}}

### Trust and Marking

You can use port groups to assign different profiles to different ports. A profile is a label for a group of configuration settings.

{{< tabs "TabID975 ">}}
{{< tab "NVUE Commands ">}}

The following example configures two profiles. `customer1` applies to swp1, swp4, and swp6. `customer2` applies to swp5 and swp7.

```
cumulus@switch:~$ nv set qos mapping customer1 trust l3 
cumulus@switch:~$ nv set qos mapping customer1 dscp 0 switch-priority 1-7
cumulus@switch:~$ nv set interface swp1,swp4,swp6 qos mapping profile customer1
cumulus@switch:~$ nv set qos mapping customer2 trust l2
cumulus@switch:~$ nv set qos mapping customer2 pcp 1 switch-priority 4 
cumulus@switch:~$ nv set interface swp5,swp7 qos mapping profile customer2
cumulus@switch:~$ nv config apply
```

The following example configures the profile `customports`, which assigns traffic on swp1, swp2, and swp3 to switch priority 4 regardless of the ingress marking.

```
cumulus@switch:~$ nv set qos mapping customports trust port 
cumulus@switch:~$ nv set qos mapping customports port-default-sp 4
cumulus@switch:~$ nv set interface swp1,swp2,swp3 qos mapping profile customports
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You define profiles with the `source.port_group_list` configuration in the `qos_features.conf` file. A `source.port_group_list` is one or more names used for a group of settings.

The following example configures two profiles. `customer1` applies to swp1, swp4, and swp6. `customer2` applies to swp5 and swp7.

```
source.port_group_list = [customer1,customer2]
source.customer1.packet_priority_source_set = [dscp]
source.customer1.port_set = swp1-swp4,swp6
source.customer1.port_default_priority = 0
source.customer1.cos_0.priority_source.dscp = [0-7]
source.customer2.packet_priority_source_set = [802.1p]
source.customer2.port_set = swp5,swp7
source.customer2.port_default_priority = 0
source.customer2.cos_1.priority_source.8021p = [4]
```

| Configuration | Description  |
| ------------- | -----------  |
| `source.port_group_list` | The names of the port groups (profiles) you want to use.<br>The following example defines `customer1` and `customer2`:<br>`source.port_group_list = [customer1,customer2]`  |
| `source.customer1.packet_priority_source_set` | The ingress marking trust.<br>In the following example, ingress DSCP values are for group `customer1`:<br>`source.customer1.packet_priority_source_set = [dscp]` |
| `source.customer1.port_set` | The set of ports on which to apply the ingress marking trust policy.<br>In the following example, ports swp1, swp2, swp3, swp4, and swp6 are for `customer1`:<br>`source.customer1.port_set = swp1-swp4,swp6` |
| `source.customer1.port_default_priority` | The default switch priority marking for unmarked or untrusted traffic.<br>In the following example, Cumulus Linux marks unmarked traffic or layer 2 traffic for `customer1` ports with switch priority 0:<br>`source.customer1.port_default_priority = 0` |
| `source.customer1.cos_0.priority_source`  | The ingress DSCP values to a switch priority value mapping for `customer1`.<br>In the following example, the set of DSCP values from 0 through 7 map to switch priority 0:<br>`source.customer1.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]` |
| `source.customer2.packet_priority_source_set` | The ingress marking trust for `customer2`.<br>In the following example, 802.1p is `trusted`:<br>`source.packet_priority_source_set = [802.1p]`  |
| `source.customer2.port_set` | The set of ports on which to apply the ingress marking trust policy.<br>In the following example, swp5 and swp7 apply for `customer2`:<br>`source.customer2.port_set = swp5,swp7` |
| `source.customer2.port_default_priority` | The default switch priority marking for unmarked or untrusted traffic.<br>In the following example, Cumulus Linux marks unmarked tagged layer 2 traffic or unmarked VLAN tagged traffic for `customer1` ports with switch priority 0:<br>`source.customer2.port_default_priority = 0` |
| `source.customer2.cos_0.priority_source` | The switch priority value to an ingress 802.1p value mapping for `customer2`.<br>The following example maps ingress 802.1p value 4 to switch priority 1:<br>`source.customer2.cos_1.priority_source.8021p = [4]` |

The following example configures the profile `customports`, which assigns traffic on swp1, swp2, and swp3 to switch priority 4 regardless of the ingress marking.

```
source.port_group_list = [customports]
source.customports.packet_priority_source_set = [port]
source.customports.port_default_priority = 4
source.customports.port_set = swp1,swp2,swp3
```

{{< /tab >}}
{{< /tabs >}}

### Remarking

You can use profiles to remark 802.1p or DSCP on egress according to the switch priority (internal COS) value. You define these profiles with `remark.port_group_list` in the `/etc/cumulus/datapath/qos/qos_features.conf` file. The name is a label for configuration settings.

To change the marked value on a packet, the switch ASIC reads the enable or disable rewrite flag on the ingress port and refers to the mapping configuration on the egress port to change the marked value. To remark 802.1p or DSCP values, you have to enable the rewrite on the ingress port and configure the mapping on the egress port.

In the following example configuration, only packets that *ingress* on swp1 and *egress* on swp2 change the marked value of the packet. Packets that ingress on other ports and egress on swp2 do **not** change the marked value of the packet. The commands map switch priority 0 and 1 to egress DSCP 37.

```
remark.port_group_list = [remark_port_group1,remark_port_group2]
remark.remark_port_group1.packet_priority_remark_set = [dscp]
remark.remark_port_group1.port_set = swp1
remark.remark_port_group2.packet_priority_remark_set = []
remark.remark_port_group2.port_set = swp2
remark.remark_port_group2.cos_0.priority_remark.dscp = [37]
remark.remark_port_group2.cos_1.priority_remark.dscp = [37]
```

### Egress Scheduling

You can use port groups with egress scheduling weights to assign different profiles to different egress ports.

In the following example, the profile `list2` applies to swp1, swp3, and swp18. `list2` only assigns weights to queues 2, 5, and 6, and schedules the other queues on a best-effort basis when there is no congestion in queues 2, 5, or 6. `list1` applies to swp2 and assigns weights to all queues.

{{< tabs "TabID884 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set qos egress-scheduler list2 traffic-class 2,5,6 mode dwrr 
cumulus@switch:~$ nv set qos egress-scheduler list2 traffic-class 2,5 bw-percent 50 
cumulus@switch:~$ nv set qos egress-scheduler list2 traffic-class 6 mode strict
cumulus@switch:~$ nv set interface swp1,swp3,swp18 qos egress-scheduler profile list2
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 0,3,4,5,6 mode dwrr 
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 0,3,4,5,6 bw-percent 10 
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 1 mode dwrr
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 1 bw-percent 20 
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 2 mode dwrr
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 2 bw-percent 30 
cumulus@switch:~$ nv set qos egress-scheduler list1 traffic-class 7 mode strict
cumulus@switch:~$ nv set interface swp2 qos egress-scheduler profile list1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

You define port groups with `egress_sched.port_group_list` in the `/etc/cumulus/datapath/qos/qos_features.conf` file. An `egress_sched.port_group_list` includes the names for the group settings. The name is a label (profile) for the configuration settings.

```
egress_sched.port_group_list = [list1,list2]
egress_sched.list1.port_set = swp2
egress_sched.list1.egr_queue_0.bw_percent = 10
egress_sched.list1.egr_queue_1.bw_percent = 20
egress_sched.list1.egr_queue_2.bw_percent = 30
egress_sched.list1.egr_queue_3.bw_percent = 10
egress_sched.list1.egr_queue_4.bw_percent = 10
egress_sched.list1.egr_queue_5.bw_percent = 10
egress_sched.list1.egr_queue_6.bw_percent = 10
egress_sched.list1.egr_queue_7.bw_percent = 0
#
egress_sched.list2.port_set = [swp1,swp3,swp18]
egress_sched.list2.egr_queue_2.bw_percent = 50
egress_sched.list2.egr_queue_5.bw_percent = 50
egress_sched.list2.egr_queue_6.bw_percent = 0
```

|Configuration |Description |
|-------------  |----------- |
| `egress_sched.port_group_list` |  The names of the port groups (labels) to use.<br>The following example defines port groups list1 snd list2:<br>`egress_sched.port_group_list = [list1,list2]` |
| `egress_sched.list1.port_set` |The interfaces on which you want to apply the port group.<br>`egress_sched.list1.port_set = swp2`  |
| `egress_sched.list1.egr_queue_0.bw_percent` | The percentage of bandwidth for egress queue 0.<br>`egress_sched.list1.egr_queue_0.bw_percent = 10` |
| `egress_sched.list1.egr_queue_1.bw_percent`  | The percentage of bandwidth for egress queue 1.<br>`egress_sched.list1.egr_queue_1.bw_percent = 20`  |
| `egress_sched.list1.egr_queue_2.bw_percent` | The percentage of bandwidth for egress queue 2.<br>`egress_sched.list1.egr_queue_2.bw_percent = 30`|
| `egress_sched.list1.egr_queue_3.bw_percent` | The percentage of bandwidth for egress queue 3.<br>`egress_sched.list1.egr_queue_3.bw_percent = 10`     |
| `egress_sched.list1.egr_queue_4.bw_percent` | The percentage of bandwidth for egress queue 4.<br>`egress_sched.list1.egr_queue_4.bw_percent = 10`|
| `egress_sched.list1.egr_queue_5.bw_percent` | The percentage of bandwidth for egress queue 5.<br><br>`egress_sched.list1.egr_queue_5.bw_percent = 10` |
| `egress_sched.list1.egr_queue_6.bw_percent` | The percentage of bandwidth for egress queue 6.<br>`egress_sched.list1.egr_queue_6.bw_percent = 10` |
| `egress_sched.list1.egr_queue_7.bw_percent` |  The percentage of bandwidth for egress queue 7.<br>`0` indicates a strict priority queue:<br>`egress_sched.list1.egr_queue_7.bw_percent = 0`|
| `egress_sched.list2.port_set` | The interfaces you want to apply to the port group.<br>The following example applies `swp1`, `swp3` and `swp18` to port group `list2`:<br>`egress_sched.list2.port_set = [swp1,swp3,swp18]`  |
| `egress_sched.list2.egr_queue_2.bw_percent` | The percentage of bandwidth for egress queue 2.<br>`egress_sched.list2.egr_queue_2.bw_percent = 50`  |
| `egress_sched.list2.egr_queue_5.bw_percent`  | The percentage of bandwidth for egress queue 5.<br>`egress_sched.list2.egr_queue_5.bw_percent = 50` |
| `egress_sched.list2.egr_queue_6.bw_percent`  | The percentage of bandwidth for egress queue 6.<br>`0` indicates a strict priority queue:<br>`egress_sched.list2.egr_queue_6.bw_percent = 0` |

{{< /tab >}}
{{< /tabs >}}

### PFC

To set priority flow control on a group of ports, you create a profile to define the egress queues that support sending PFC pause frames and define the set of interfaces to which you want to apply PFC pause frame configuration. Cumulus Linux automatically enables PFC frame transmit and PFC frame receive, and derives all other PFC settings, such as the buffer limits that trigger PFC frames transmit to start and stop, the amount of reserved buffer space, and the cable length.

{{< tabs "TabID1050 ">}}
{{< tab "NVUE Commands ">}}

The following example applies a PFC profile called `my_pfc_ports` for egress queue 3 and 5 on swp1, swp2, swp3, swp4, and swp6.

```
cumulus@switch:~$ nv set qos pfc my_pfc_ports switch-priority 3,5
cumulus@switch:~$ nv set interface swp1-4,swp6 qos pfc profile my_pfc_ports
cumulus@switch:~$ nv config apply
```

The following example applies a PFC profile called `my_pfc_ports2` for egress queue 0 on swp1. The commands disable PFC frame receive, and set the buffer limit that triggers PFC frame transmission to stop to 1500 bytes and to start to 1000 bytes. The commands also set the amount of reserved buffer space to 2000 bytes, and the cable length to 50 meters:

```
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 switch-priority 0 
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 xoff-threshold 1500 
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 xon-threshold 1000 
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 tx enable 
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 rx disable 
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 port-buffer 2000 
cumulus@switch:~$ nv set qos pfc my_pfc_ports2 cable-length 50
cumulus@switch:~$ nv set interface swp1 qos pfc profile my_pfc_ports2
cumulus@switch:~$ nv config apply
```

<details>
<summary>All PFC commands</summary>

| <div style="width:450px">Command | Description |
| ------------- | ----------- |
| `nv set qos pfc <profile> port-buffer <value>` | The amount of reserved buffer space (from the global shared buffer) for the interfaces defined in the port group list .<br>The following example sets the amount of reserved buffer space to 25000 bytes:<br>`nv set qos pfc my_pfc_ports port-buffer 25000` |
| `nv set qos pfc <profile> xoff-threshold <value>` | The amount of reserved buffer that the switch must consume before sending a PFC pause frame out of the set of interfaces in the port group list.<br>The following example sends PFC pause frames after consuming 20000 bytes of reserved buffer:<br>`nv set qos pfc my_pfc_ports xoff-threshold 20000` |
| `nv set qos pfc <profile> xon-threshold <value>` | The number of bytes below the `xoff` threshold that the buffer consumption must drop below before sending PFC pause frames stops.<br>In the following example, the buffer congestion must reduce by 1000 bytes (to 8000 bytes) before PFC pause frames stop:<br>`nv set qos pfc my_pfc_ports xon-threshold 1000`|
| `nv set qos pfc <profile> rx enable`<br>`nv set qos pfc <profile> rx disable` | Enables or disables sending PFC pause frames. The default value is enable.<br>The following example disables sending PFC pause frames:<br>`nv set qos pfc my_pfc_ports rx disable`  |
| `nv set qos pfc <profile> tx enable`<br>`nv set qos pfc <profile> tx disable` | Enables or disables receiving PFC pause frames. You do not need to define the COS values for `rx enable`. The switch receives any COS value. The default value is enable.<br>The following example disables receiving PFC pause frames:<br>`nv set qos pfc my_pfc_ports tx disable` |
| `nv set qos pfc <profile> cable-length <value>` | The length, in meters, of the cable that attaches to the ports. Cumulus Linux uses this value internally to determine the latency between generating a PFC pause frame and receiving the PFC pause frame. The default is `10` meters.<br>The following example sets the cable length to `5` meters:<br>`nv set qos pfc my_pfc_ports cable-length 5`|
</details>

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `priority flow control` section of the `/etc/cumulus/datapath/qos/qos_features.conf` file.

The following example applies a PFC profile called `my_pfc_ports` for egress queue 3 and 5 on swp1, swp2, swp3, swp4, and swp6.

```
pfc.port_group_list = [my_pfc_ports2]
pfc.my_pfc_ports2.cos_list = [0]
pfc.my_pfc_ports2.port_set = swp1
```

The following example applies a PFC profile called `my_pfc_ports2` for egress queue 0 on swp1. The commands also disable PFC frame receive, and set the xoff-size to 1500 bytes, the xon-size to 1000 bytes, the headroom to 2000 bytes, and the cable length to 10 meters:

```
pfc.port_group_list = [my_pfc_ports2]
pfc.my_pfc_ports2.cos_list = [0]
pfc.my_pfc_ports2.port_set = swp1
pfc.my_pfc_ports2.port_buffer_bytes = 2000
pfc.my_pfc_ports2.xoff_size = 1500
pfc.my_pfc_ports2.xon_delta = 1000
pfc.my_pfc_ports2.tx_enable = true
pfc.my_pfc_ports2.rx_enable = false
pfc.my_pfc_ports2.cable_length = 10
```

<details>
<summary>All PFC configuration options</summary>

| Configuration | Description |
| ------------- | ------- |
| `pfc.my_pfc_ports.port_buffer_bytes` | The amount of reserved buffer space (from the global shared buffer) for the interfaces defined in the port group list.<br>The following example sets the amount of reserved buffer space to 25000 bytes:<br>`pfc.my_pfc_ports.port_buffer_bytes = 25000`  |
| `pfc.my_pfc_ports.xoff_size` | The amount of reserved buffer that the switch must consume before sending a PFC pause frame out the set of interfaces in the port group list.<br>The following example sends PFC pause frames after consuming 10000 bytes of reserved buffer:<br>`pfc.my_pfc_ports.xoff_size = 10000`|
| `pfc.my_pfc_ports.xon_delta` | The number of bytes below the `xoff` threshold that the buffer consumption must drop below before sending PFC pause frames stops.<br>The following example the buffer congestion must reduce by 2000 bytes (to 8000 bytes) before PFC pause frames stop:<br>`pfc.my_pfc_ports.xon_delta = 2000`|
| `pfc.my_pfc_ports.rx_enable` | Enables (`true`) or disables (`false`) sending PFC pause frames. The default value is `true`.<br>The following example enables sending PFC pause frames:<br>`pfc.my_pfc_ports.tx_enable = true` |
| `pfc.my_pfc_ports.tx_enable` | Enables (`true`) or disables (`false`) receiving PFC pause frames. You do not need to define the COS values for `rx_enable`. The switch receives any COS value. The default value is `true`.<br>The following example enables receiving PFC pause frames:<br> `pfc.my_pfc_ports.rx_enable = true` |
| `pfc.my_pfc_ports.cable_length` | The length, in meters, of the cable that attaches to the port in the port group list. Cumulus Linux uses this value internally to determine the latency between generating a PFC pause frame and receiving the PFC pause frame. The default is `10` meters<br>In this example, the cable is `5` meters:<br> `pfc.my_pfc_ports.cable_length = 5`|
</details>

{{< /tab >}}
{{< /tabs >}}

### ECN

You can create ECN profiles and assign them to different ports.

{{< tabs "TabID1114 ">}}
{{< tab "NVUE Commands ">}}

The following example creates a custom ECN profile called `my-red-profile` for egress queue (`traffic-class`) 1 and 2. The commands set the minimum buffer threshold to 40000 bytes, maximum buffer threshold to 200000 bytes, and the probability to 10. The commands also enable RED and apply the ECN profile to swp1 and swp2.

```
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 min-threshold-bytes 40000 
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 max-threshold-bytes 200000 
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 probability 10
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 red enable
cumulus@switch:~$ nv set interface swp1,swp2 qos congestion-control my-red-profile
cumulus@switch:~$ nv config apply
```

You can configure different thresholds and probability values for different traffic classes in a custom profile:

```
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 min-threshold-bytes 40000 
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 max-threshold-bytes 200000 
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 probability 10
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1,2 red enable
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 4 min-threshold-bytes 30000 
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 4 max-threshold-bytes 150000 
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 4 probability 80
cumulus@switch:~$ nv set interface swp1,swp2 qos congestion-control my-red-profile
cumulus@switch:~$ nv config apply
```

You can disable ECN bit marking for an ECN profile. The following example disables ECN bit marking in the `my-red-profile` profile:

```
cumulus@switch:~$ nv set qos congestion-control my-red-profile traffic-class 1 ecn disable
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `Explicit Congestion Notification` section of the `/etc/cumulus/datapath/qos/qos_features.conf` file.

The following example creates a custom ECN profile called `my-red-profile` for egress queue 1 and 2, with a minimum buffer threshold of 40000 bytes, maximum buffer threshold of 200000 bytes, and a probability of 10. The commands also enable RED and apply the ECN profile to swp1 and swp2.

```
ecn_red.port_group_list = [my-red-profile] 
my-red-profile.egress_queue_list = [1,2]
my-red-profile.port_set = swp1,swp2
my-red-profile.ecn_enable = true
my-red-profile.red_enable = true
my-red-profile.min_threshold_bytes = 40000
my-red-profile.max_threshold_bytes = 200000
my-red-profile.probability = 10
```

To disable ECN bit marking, set `ecn_enable` to false. The following example disables ECN bit marking in the `my-red-profile`.

```
...
my-red-profile.ecn_enable = false 
...
```

{{< /tab >}}
{{< /tabs >}}

## Traffic Pools

Cumulus Linux supports adjusting the following traffic pools:

|Traffic Pool |Description |
|------------- |----------- |
| `default-lossy` | The default traffic pool for all switch priorities. |
| `default-lossless` | The traffic pool for lossless traffic when you enable {{<link title="#Flow Control Buffers" text="flow control">}}. |
| `mc-lossy` | The traffic pool for multicast traffic. |
| `roce-lossy` | The traffic pool for {{<link title="RDMA over Converged Ethernet - RoCE" text="RoCE">}} lossy mode. |
| `roce-lossless` | The traffic pool for {{<link title="RDMA over Converged Ethernet - RoCE" text="RoCE">}} lossless mode. |

You configure a traffic pool by associating switch priorities and defining the buffer memory percentages allocated to the pools. The following example associates switch priority 2 and allocates a memory percentage of 30 for the `mc-lossy` pool:

{{< tabs "TabID1166 ">}}
{{< tab "NVUE Commands">}}

```
cumulus@switch:~$ nv set qos traffic-pool default-lossy switch-priority 0,1,3,4,5,6,7
cumulus@switch:~$ nv set qos traffic-pool default-lossy memory-percent 70
cumulus@switch:~$ nv set qos traffic-pool mc-lossy switch-priority 2
cumulus@switch:~$ nv set qos traffic-pool mc-lossy memory-percent 30
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Configure the following settings in the `/etc/mlx/datapath/qos/qos_infra.conf` file:

```
traffic.priority_group_list = [service2,bulk]

priority_group.service2.cos_list = [2]
priority_group.bulk.cos_list = [0,1,3,4,5,6,7]

priority_group.service2.id = 2

priority_group.service2.service_pool = 2

ingress_service_pool.2.percent = 30
ingress_service_pool.0.percent = 70

port.service_pool.2.ingress_buffer.reserved = 10240

ingress_service_pool.2.mode = 1

port.service_pool.2.ingress_buffer.dynamic_quota = ALPHA_8

priority_group.service2.ingress_buffer.dynamic_quota = ALPHA_8

egress_buffer.egr_queue_2.uc.service_pool = 2

egress_service_pool.2.percent = 30
egress_service_pool.0.percent = 70

port.service_pool.2.egress_buffer.uc.reserved = 0

egress_buffer.cos_2.mc.service_pool = 2

egress_buffer.egr_queue_2.uc.reserved = 1024

port.egress_buffer.mc.reserved = 10240
port.egress_buffer.mc.shared_size = 2097152
egress_service_pool.2.mode = 1

port.service_pool.2.egress_buffer.uc.dynamic_quota = ALPHA_8

egress_buffer.egr_queue_2.uc.dynamic_quota = ALPHA_8

egress_buffer.cos_2.mc.dynamic_quota = ALPHA_8
```

{{< /tab >}}
{{< /tabs >}}

For additional `default-lossless` and RoCE pool examples, see {{<link title="#Flow Control Buffers" text="Flow Control Buffers">}} and {{<link title="RDMA over Converged Ethernet - RoCE" text="RoCE">}}.

## Syntax Checker

Cumulus Linux provides a syntax checker for the `qos_features.conf` and `qos_infra.conf` files to check for errors, such missing parameters or invalid parameter labels and values.

The syntax checker runs automatically with every `switchd reload`.

You can run the syntax checker manually from the command line with the `cl-consistency-check --datapath-syntax-check` command. If errors exist, they write to `stderr` by default. If you run the command with `-q`, errors write to the `/var/log/switchd.log` file.

The `cl-consistency-check --datapath-syntax-check` command takes the following options:

| <div style="width:120px">Option | Description |
| ------------------------------- | ----------- |
| `-h` | Displays this list of command options. |
| `-q` | Runs the command in quiet mode. Errors write to the `/var/log/switchd.log` file instead of `stderr`. |
| `-qi` | Runs the syntax checker against a specified `qos_infra.conf` file. |
| `-qf` | Runs the syntax checker against a specified `qos_features.conf` file. |

By default the syntax checker assumes:
- `qos_infra.conf` is in `/etc/mlx/datapath/qos/qos_infra.conf`
- `qos_features.conf` is in `/etc/cumulus/datapath/qos/qos_features.conf`

You can run the syntax checker when `switchd` is either running or stopped.

<!--
**Example Commands**

The following example command runs the syntax checker on the default `/etc/cumulus/datapath/traffic.conf` file and shows that there are no errors:

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check
No errors detected in traffic config file /etc/cumulus/datapath/traffic.conf
```

The following example command runs the syntax checker on the default `/etc/cumulus/datapath/traffic.conf` file in quiet mode. If errors exist, they write to the `/var/log/switchd.log` file.

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check -q
```

The following example command runs the syntax checker on the `/mypath/test-traffic.conf` file and shows that there are errors:

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check -t /path/test-traffic.conf
Traffic source 8021p: missing mapping for priority value '7'
Errors detected while checking traffic config file /mypath/test-traffic.conf
```

The following example command runs the syntax checker on the `/mypath/test-traffic.conf` file in quiet mode. If errors exist, they write to the `/var/log/switchd.log` file.

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check -t /path/test-traffic.conf -q
```
-->

## Default Configuration Files

<details>
<summary>qos_features.conf</summary>

```
# /etc/cumulus/datapath/qos/qos_features.conf
#
# Copyright © 2021 NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# This software product is a proprietary product of Nvidia Corporation and its affiliates
# (the "Company") and all right, title, and interest in and to the software
# product, including all associated intellectual property rights, are and
# shall remain exclusively with the Company.
#
# This software product is governed by the End User License Agreement
# provided with the software product. 

# packet header field used to determine the packet priority level
# fields include {802.1p, dscp, port}
traffic.packet_priority_source_set = [802.1p]
traffic.port_default_priority      = 0

# packet priority source values assigned to each internal cos value
# internal cos values {cos_0..cos_7}
# (internal cos 3 has been reserved for CPU-generated traffic)
# 802.1p values = {0..7}
traffic.cos_0.priority_source.8021p = [0]
traffic.cos_1.priority_source.8021p = [1]
traffic.cos_2.priority_source.8021p = [2]
traffic.cos_3.priority_source.8021p = [3]
traffic.cos_4.priority_source.8021p = [4]
traffic.cos_5.priority_source.8021p = [5]
traffic.cos_6.priority_source.8021p = [6]
traffic.cos_7.priority_source.8021p = [7]

# dscp values = {0..63}
#traffic.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]
#traffic.cos_1.priority_source.dscp = [8,9,10,11,12,13,14,15]
#traffic.cos_2.priority_source.dscp = [16,17,18,19,20,21,22,23]
#traffic.cos_3.priority_source.dscp = [24,25,26,27,28,29,30,31]
#traffic.cos_4.priority_source.dscp = [32,33,34,35,36,37,38,39]
#traffic.cos_5.priority_source.dscp = [40,41,42,43,44,45,46,47]
#traffic.cos_6.priority_source.dscp = [48,49,50,51,52,53,54,55]
#traffic.cos_7.priority_source.dscp = [56,57,58,59,60,61,62,63]
# remark packet priority value
# fields include {802.1p, dscp}
traffic.packet_priority_remark_set = []

# packet priority remark values assigned from each internal cos value
# internal cos values {cos_0..cos_7}
# (internal cos 3 has been reserved for CPU-generated traffic)
# 802.1p values = {0..7}
#traffic.cos_0.priority_remark.8021p = [0]
#traffic.cos_1.priority_remark.8021p = [1]
#traffic.cos_2.priority_remark.8021p = [2]
#traffic.cos_3.priority_remark.8021p = [3]
#traffic.cos_4.priority_remark.8021p = [4]
#traffic.cos_5.priority_remark.8021p = [5]
#traffic.cos_6.priority_remark.8021p = [6]
#traffic.cos_7.priority_remark.8021p = [7]

# dscp values = {0..63}
#traffic.cos_0.priority_remark.dscp = [0]
#traffic.cos_1.priority_remark.dscp = [8]
#traffic.cos_2.priority_remark.dscp = [16]
#traffic.cos_3.priority_remark.dscp = [24]
#traffic.cos_4.priority_remark.dscp = [32]
#traffic.cos_5.priority_remark.dscp = [40]
#traffic.cos_6.priority_remark.dscp = [48]
#traffic.cos_7.priority_remark.dscp = [56]

# source.port_group_list = [source_port_group]
# source.source_port_group.packet_priority_source_set = [dscp]
# source.source_port_group.port_set = swp1-swp4,swp6
# source.source_port_group.port_default_priority = 0
# source.source_port_group.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]
# source.source_port_group.cos_1.priority_source.dscp = [8,9,10,11,12,13,14,15]
# source.source_port_group.cos_2.priority_source.dscp = [16,17,18,19,20,21,22,23]
# source.source_port_group.cos_3.priority_source.dscp = [24,25,26,27,28,29,30,31]
# source.source_port_group.cos_4.priority_source.dscp = [32,33,34,35,36,37,38,39]
# source.source_port_group.cos_5.priority_source.dscp = [40,41,42,43,44,45,46,47]
# source.source_port_group.cos_6.priority_source.dscp = [48,49,50,51,52,53,54,55]
# source.source_port_group.cos_7.priority_source.dscp = [56,57,58,59,60,61,62,63]

# remark.port_group_list = [remark_port_group]
# remark.remark_port_group.packet_priority_remark_set = [dscp]
# remark.remark_port_group.port_set = swp1-swp4,swp6
# remark.remark_port_group.cos_0.priority_remark.dscp = [0]
# remark.remark_port_group.cos_1.priority_remark.dscp = [8]
# remark.remark_port_group.cos_2.priority_remark.dscp = [16]
# remark.remark_port_group.cos_3.priority_remark.dscp = [24]
# remark.remark_port_group.cos_4.priority_remark.dscp = [32]
# remark.remark_port_group.cos_5.priority_remark.dscp = [40]
# remark.remark_port_group.cos_6.priority_remark.dscp = [48]
# remark.remark_port_group.cos_7.priority_remark.dscp = [56]

# to configure priority flow control on a group of ports:
# -- assign cos value(s) to the cos list
# -- add or replace a port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a PFC buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers PFC frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers PFC frames transmit to stop)
#    -- enable PFC frame transmit and/or PFC frame receive

# priority flow control
#pfc.port_group_list = [pfc_port_group]
#pfc.pfc_port_group.cos_list = []
#pfc.pfc_port_group.port_set = swp1-swp4,swp6
#pfc.pfc_port_group.port_buffer_bytes = 25000
#pfc.pfc_port_group.xoff_size = 10000
#pfc.pfc_port_group.xon_delta = 2000
#pfc.pfc_port_group.tx_enable = true
#pfc.pfc_port_group.rx_enable = true
#Specify cable length in mts
#pfc.pfc_port_group.cable_length = 10

# to configure pause on a group of ports:
# -- add or replace port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a pause buffer size in bytes for each port
#    -- set the xoff byte limit (buffer limit that triggers pause frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers pause frames transmit to stop)
#    -- enable pause frame transmit and/or pause frame receive

# link pause
# link_pause.port_group_list = [pause_port_group]
# link_pause.pause_port_group.port_set = swp1-swp4,swp6
# link_pause.pause_port_group.port_buffer_bytes = 25000
# link_pause.pause_port_group.xoff_size = 10000
# link_pause.pause_port_group.xon_delta = 2000
# link_pause.pause_port_group.rx_enable = true
# link_pause.pause_port_group.tx_enable = true
# Specify cable length in mts
# link_pause.pause_port_group.cable_length = 10

# Explicit Congestion Notification
# to configure ECN and RED on a group of ports:
# -- add or replace port group names in the port group list
# -- assign cos value(s) to the cos list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
# -- to enable RED requires the latest traffic.conf
#Default ECN configuration on TC0
default_ecn_red_conf.egress_queue_list = [0]
default_ecn_red_conf.ecn_enable = true
default_ecn_red_conf.red_enable = false
default_ecn_red_conf.min_threshold_bytes = 150000
default_ecn_red_conf.max_threshold_bytes = 1500000
default_ecn_red_conf.probability = 100

#ecn_red.port_group_list = [ecn_red_port_group]
#ecn_red.ecn_red_port_group.egress_queue_list = [1]
#ecn_red.ecn_red_port_group.port_set = allports
#ecn_red.ecn_red_port_group.ecn_enable = true
#ecn_red.ecn_red_port_group.red_enable = false
#ecn_red.ecn_red_port_group.min_threshold_bytes = 40000
#ecn_red.ecn_red_port_group.max_threshold_bytes = 200000
#ecn_red.ecn_red_port_group.probability = 100

# Hierarchical traffic shaping
# to configure shaping at 2 levels:
#     - per egress queue egr_queue_0 - egr_queue_7
#     - port level aggregate
# -- add or replace a port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set min and max rates in kbps for each egr_queue [min, max]
#    -- set max rate in kbps at port level
# shaping.port_group_list = [shaper_port_group]
# shaping.shaper_port_group.port_set = swp1-swp3,swp5,swp7s0-swp7s3
# shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]
# shaping.shaper_port_group.egr_queue_1.shaper = [51000, 150000]
# shaping.shaper_port_group.egr_queue_2.shaper = [52000, 200000]
# shaping.shaper_port_group.egr_queue_3.shaper = [53000, 250000]
# shaping.shaper_port_group.egr_queue_4.shaper = [54000, 300000]
# shaping.shaper_port_group.egr_queue_5.shaper = [55000, 350000]
# shaping.shaper_port_group.egr_queue_6.shaper = [56000, 400000]
# shaping.shaper_port_group.egr_queue_7.shaper = [57000, 450000]
# shaping.shaper_port_group.port.shaper = 900000

# default egress scheduling weight per egress queue
# To be applied to all the ports if port_group profile not configured
# If you do not specify any bw_percent of egress_queues, those egress queues
# will assume DWRR weight 0 - no egress scheduling for those queues
# '0' indicates strict priority

default_egress_sched.egr_queue_0.bw_percent = 12
default_egress_sched.egr_queue_1.bw_percent = 13
default_egress_sched.egr_queue_2.bw_percent = 12
default_egress_sched.egr_queue_3.bw_percent = 13
default_egress_sched.egr_queue_4.bw_percent = 12
default_egress_sched.egr_queue_5.bw_percent = 13
default_egress_sched.egr_queue_6.bw_percent = 12
default_egress_sched.egr_queue_7.bw_percent = 13

# port_group profile for egress scheduling weight per egress queue
# If you do not specify any bw_percent of egress_queues, those egress queues
# will assume DWRR weight 0 - no egress scheduling for those queues
# '0' indicates strict priority
#egress_sched.port_group_list = [sched_port_group1]
#egress_sched.sched_port_group1.port_set = swp2
#egress_sched.sched_port_group1.egr_queue_0.bw_percent = 10
#egress_sched.sched_port_group1.egr_queue_1.bw_percent = 20
#egress_sched.sched_port_group1.egr_queue_2.bw_percent = 30
#egress_sched.sched_port_group1.egr_queue_3.bw_percent = 10
#egress_sched.sched_port_group1.egr_queue_4.bw_percent = 10
#egress_sched.sched_port_group1.egr_queue_5.bw_percent = 10
#egress_sched.sched_port_group1.egr_queue_6.bw_percent = 10
#egress_sched.sched_port_group1.egr_queue_7.bw_percent = 0

# Cut-through is disabled by default on all chips with the exception of
# Spectrum.  On Spectrum cut-through cannot be disabled.
#cut_through_enable = false
```
</details>

<details>
<summary>qos_infra.conf</summary>

```
#
# Default qos-infra configuration for Mellanox Spectrum chip
#
# Copyright © 2021 NVIDIA CORPORATION & AFFILIATES. ALL RIGHTS RESERVED.
#
# This software product is a proprietary product of Nvidia Corporation and its affiliates
# (the "Company") and all right, title, and interest in and to the software
# product, including all associated intellectual property rights, are and
# shall remain exclusively with the Company.
#
# This software product is governed by the End User License Agreement
# provided with the software product. 

# scheduling algorithm: algorithm values = {dwrr}
scheduling.algorithm = dwrr

# priority groups
# supported group names are control, bulk, service1-6
traffic.priority_group_list = [bulk]

# internal cos values assigned to each priority group
# each cos value should be assigned exactly once
# internal cos values {0..7}
priority_group.bulk.cos_list = [0,1,2,3,4,5,6,7]

# Alias Name defined for each priority group
# Valid string between 0-255 chars
# Sample alias support for naming priority groups
#priority_group.bulk.alias = "Bulk"

# priority group ID assigned to each priority group
#priority_group.control.id = 7
#priority_group.service2.id = 2
priority_group.bulk.id = 0

# all priority groups share a service pool on Spectrum
# service pools assigned to each priority group
priority_group.bulk.service_pool = 0

# service pool assigned for lossless PGs
#flow_control.ingress_service_pool = 0

# --- ingress buffer space allocations ---
# total buffer
#  - ingress minimum buffer allocations
#  - ingress service pool buffer allocations
#  - priority group ingress headroom allocations
#  - ingress global headroom allocations
#  = total ingress shared buffer size

# ingress service pool buffer allocation: percent of total buffer
# If a service pool has no priority groups, the buffer is added
# to the shared buffer space.
ingress_service_pool.0.percent = 100

# Ingress buffer port.pool buffer : size in bytes
#port.service_pool.0.ingress_buffer.reserved = 10240
#port.service_pool.0.ingress_buffer.shared_size = 9000
#port.management.ingress_buffer.reserved = 0


# priority group minimum buffer allocation: size in bytes
# priority group shared buffer allocation: shared buffer size in bytes
# if a priority group has no packet priority values assigned to it, the buffers will not be allocated

#priority_group.bulk.ingress_buffer.reserved           = 0
#priority_group.bulk.ingress_buffer.shared_size        = 15

# ---- ingress dynamic buffering settings
# To enable ingress static pool, set the mode to 0
ingress_service_pool.0.mode = 1

# The ALPHA defines the max% of buffers (quota) available on a
# per ingress port OR ipool, Ingress PG, Egress TC, Egress port OR epool.
# ALPHA value equates to the following buffer limit calculated as:
# alpha%(alpha+1) = Max Buffer percentage

# https://community.mellanox.com/s/article/understanding-the-alpha-parameter-in-the-buffer-configuration-of-mellanox-spectrum-switches
# Each shared buffer pool can use a maximum of [total_buffer * (alpha / (alpha+1))]
# Configure quota values mapped to the following alpha values:
# Configuration value = alpha level:
# Both ALPHA_*(string representation) as well as integer values (old representation) will be supported for alpha
# 0/ALPHA_0  = alpha 0
# 1/ALPHA_1_128  = alpha 1/128
# 2/ALPHA_1_64  = alpha 1/64
# 3/ALPHA_1_32  = alpha 1/32
# 4/ALPHA_1_16  = alpha 1/16
# 5/ALPHA_1_8  = alpha 1/8
# 6/ALPHA_1_4  = alpha 1/4
# 7/ALPHA_1_2  = alpha 1/2
# 8/ALPHA_1  = alpha  1
# 9/ALPHA_2  = alpha  2
# 10/ALPHA_4 = alpha  4
# 11/ALPHA_8 = alpha  8
# 12/ALPHA_16 = alpha 16
# 13/ALPHA_32 = alpha 32
# 14/ALPHA_64 = alpha 64
# 15/ALPHA_INFINITY = alpha Infinity

# Ingress buffer per-port dynamic buffering alpha (Default: ALPHA_8)
#port.service_pool.0.ingress_buffer.dynamic_quota = ALPHA_8
#port.management.ingress_buffer.dynamic_quota = ALPHA_8


# Ingress buffer dynamic buffering alpha for lossless PGs (if any; Default: ALPHA_1)
#flow_control.ingress_buffer.dynamic_quota = ALPHA_1

# Ingress buffer per-PG dynamic buffering alpha (Default: ALPHA_8)
#priority_group.bulk.ingress_buffer.dynamic_quota = ALPHA_8

# --- egress buffer space allocations ---
# total egress buffer
#  - minimum buffer allocations
#  = total service pool buffer size
# service pool assigned for lossless PGs
#flow_control.egress_service_pool = 0

# service pool assigned for egress queues
egress_buffer.egr_queue_0.uc.service_pool = 0
egress_buffer.egr_queue_1.uc.service_pool = 0
egress_buffer.egr_queue_2.uc.service_pool = 0
egress_buffer.egr_queue_3.uc.service_pool = 0
egress_buffer.egr_queue_4.uc.service_pool = 0
egress_buffer.egr_queue_5.uc.service_pool = 0
egress_buffer.egr_queue_6.uc.service_pool = 0
egress_buffer.egr_queue_7.uc.service_pool = 0

# Service pool buffer allocation: percent of total
# buffer size.
egress_service_pool.0.percent = 100

# Egress buffer port.pool buffer : size in bytes
#port.service_pool.0.egress_buffer.uc.reserved = 10240
#port.service_pool.0.egress_buffer.uc.shared_size = 9000
#port.management.egress_buffer.reserved = 0

# Front panel port egress buffer limits enforced for each
# priority group.
# Unlimited egress buffers not supported on Spectrum.
#priority_group.bulk.unlimited_egress_buffer     = false

# if a priority group has no cos values assigned to it, the buffers will not be allocated

# Service pool mapping for MC.SP region
egress_buffer.cos_0.mc.service_pool = 0
egress_buffer.cos_1.mc.service_pool = 0
egress_buffer.cos_2.mc.service_pool = 0
egress_buffer.cos_3.mc.service_pool = 0
egress_buffer.cos_4.mc.service_pool = 0
egress_buffer.cos_5.mc.service_pool = 0
egress_buffer.cos_6.mc.service_pool = 0
egress_buffer.cos_7.mc.service_pool = 0
# Reserved and static shared buffer allocation for MC.SP region: size in bytes
#egress_buffer.cos_0.mc.reserved = 10240
#egress_buffer.cos_1.mc.reserved = 10240
#egress_buffer.cos_2.mc.reserved = 10240
#egress_buffer.cos_3.mc.reserved = 10240
#egress_buffer.cos_4.mc.reserved = 10240
#egress_buffer.cos_5.mc.reserved = 10240
#egress_buffer.cos_6.mc.reserved = 10240
#egress_buffer.cos_7.mc.reserved = 10240
#egress_buffer.cos_0.mc.shared_size = 40
#egress_buffer.cos_1.mc.shared_size = 40
#egress_buffer.cos_2.mc.shared_size =  5
#egress_buffer.cos_3.mc.shared_size = 40
#egress_buffer.cos_4.mc.shared_size = 40
#egress_buffer.cos_5.mc.shared_size = 40
#egress_buffer.cos_6.mc.shared_size = 40
#egress_buffer.cos_7.mc.shared_size = 30

# Shared buffer allocation for ePort.TC region : size in bytes.
#egress_buffer.egr_queue_0.uc.shared_size   = 40
#egress_buffer.egr_queue_1.uc.shared_size   = 40
#egress_buffer.egr_queue_2.uc.shared_size   =  5
#egress_buffer.egr_queue_3.uc.shared_size   = 40
#egress_buffer.egr_queue_4.uc.shared_size   = 40
#egress_buffer.egr_queue_5.uc.shared_size   = 40
#egress_buffer.egr_queue_6.uc.shared_size   = 40
#egress_buffer.egr_queue_7.uc.shared_size   = 30

# Minimum buffer allocation for ePort.TC region: size in bytes
#egress_buffer.egr_queue_0.uc.reserved = 1024
#egress_buffer.egr_queue_1.uc.reserved = 1024
#egress_buffer.egr_queue_2.uc.reserved = 1024
#egress_buffer.egr_queue_3.uc.reserved = 1024
#egress_buffer.egr_queue_4.uc.reserved = 1024
#egress_buffer.egr_queue_5.uc.reserved = 1024
#egress_buffer.egr_queue_6.uc.reserved = 1024
#egress_buffer.egr_queue_7.uc.reserved = 1024

# Reserved Egress buffer for TCs mapped to lossless SPs
#flow_control.egress_buffer.reserved = 0

# Egress buffer ePort.MC buffer : size in bytes
# the per-port limit on multicast packets (applies to all switch priorities)
#port.egress_buffer.mc.reserved = 10240
#port.egress_buffer.mc.shared_size = 92160

# To enable egress static pool, set the mode to 0
egress_service_pool.0.mode = 1

# Egress dynamic buffer pool configuration
# Replace the shared_size parameter with the dynamic_quota=n/ALPHA_x,
# where ‘n’ should be the configuration value for alpha.
# 		‘ALPHA_x’ should be string representation for alpha.
# Pls note : Same alpha configuration values can be used as mentioned in Ingress Dynamic Buffering section above
# Egress buffer per-port dynamic buffering quota (alpha ; Default: ALPHA_16)
#port.service_pool.0.egress_buffer.uc.dynamic_quota = ALPHA_16
#port.management.egress_buffer.dynamic_quota = ALPHA_8


# Egress buffer per-egress-queue dynamic buffering quota (alpha) for lossless egress queues (Default: ALPHA_INFINITY)
#flow_control.egress_buffer.dynamic_quota = ALPHA_1

# Egress buffer per-egress-queue dynamic buffering quota (alpha) for unicast (Default: ALPHA_8)
#egress_buffer.egr_queue_0.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_1.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_2.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_3.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_4.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_5.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_6.uc.dynamic_quota = ALPHA_8
#egress_buffer.egr_queue_7.uc.dynamic_quota = ALPHA_8

# Egress buffer per-egress-queue dynamic buffering quota (alpha) for multicast (Default: ALPHA_INFINITY)
#egress_buffer.egr_queue_0.mc.dynamic_quota    = ALPHA_2
#egress_buffer.egr_queue_1.mc.dynamic_quota = ALPHA_4
#egress_buffer.egr_queue_2.mc.dynamic_quota = ALPHA_1
#egress_buffer.egr_queue_3.mc.dynamic_quota = ALPHA_1_2
#egress_buffer.egr_queue_4.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.egr_queue_5.mc.dynamic_quota = ALPHA_1_8
#egress_buffer.egr_queue_6.mc.dynamic_quota = ALPHA_1_16
#egress_buffer.egr_queue_7.mc.dynamic_quota = ALPHA_INFINITY

# These parameters can be assigned to the virtual Multicast port as well (Default: ALPHA_1_4)
#egress_buffer.cos_0.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_1.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_2.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_3.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_4.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_5.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_6.mc.dynamic_quota = ALPHA_1_4
#egress_buffer.cos_7.mc.dynamic_quota = ALPHA_1_4

# internal cos values mapped to egress queues
# multicast queue: same as unicast queue
cos_egr_queue.cos_0.uc  = 0
cos_egr_queue.cos_0.cpu = 0

cos_egr_queue.cos_1.uc  = 1
cos_egr_queue.cos_1.cpu = 1

cos_egr_queue.cos_2.uc  = 2
cos_egr_queue.cos_2.cpu = 2

cos_egr_queue.cos_3.uc  = 3
cos_egr_queue.cos_3.cpu = 3

cos_egr_queue.cos_4.uc  = 4
cos_egr_queue.cos_4.cpu = 4

cos_egr_queue.cos_5.uc  = 5
cos_egr_queue.cos_5.cpu = 5

cos_egr_queue.cos_6.uc  = 6
cos_egr_queue.cos_6.cpu = 6

cos_egr_queue.cos_7.uc  = 7
cos_egr_queue.cos_7.cpu = 7
```
</details>

## Caveats

### Configure QoS and Breakout Ports Simultaneously

If you configure both breakout ports by modifying `ports.conf` and QoS settings by modifying `qos_features.conf`, then apply the settings with `reload switchd`, errors might occur.

You must apply breakout port configuration before QoS configuration on the breakout ports. Modify `ports.conf` first, `reload switchd`, then modify `qos_features.conf` and `reload switchd` a second time.

### QoS Settings on Bond Member Interfaces

If you use Linux commands to apply QoS settings on bond member interfaces instead of the logical bond interface, the members must share identical QoS configuration. If the configuration is not identical between bond interfaces, the bond inherits the `_last_ interface` you apply to the bond.

If QoS settings do not match, `switchd reload` fails; however, `switchd restart` does not fail.

NVUE rejects QoS configurations on bond member interfaces and shows an error when you try to apply the configurations; you must apply all QoS configuration on logical bond interfaces.

<!-- vale off -->
### Cut-through Switching
<!-- vale on -->
You cannot disable cut-through switching on Spectrum ASICs. Cumulus Linux ignores the `cut_through_enable = false` setting in the `qos_features.conf` file.
