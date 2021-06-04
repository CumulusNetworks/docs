---
title: Buffer and Queue Management
author: NVIDIA
weight: 320
right_toc_levels: 2
---

{{< notice note >}}
This chapter will refer to "frames" for all internal QoS functionality, but the actions are independent of layer 2 frames or layer 3 packets, unless explicitly stated.
{{< /notice >}}
## Overview
traffic.conf is now qos_features.conf
datapath.conf is now qos_infra.conf
 For Ingress/Egress descriptor buffers, no configuration knob to be provided for users. Refer to the Buffer Configuration section describing the “Descriptor Pool Configurations” 

    CL provides only ONE LOSSLESS PG configured per port and that is internal to CL implementation with PFC/LinkPause enabled on the port. 

    Split ports buffers allocation is same as non-split ports 

dynamic buffer pools by default.
### Buffers

### Queuing
## Classification
When a frame or packet arrives on the switch it is mapped to an "internal COS" value. This value is never written to the frame or packet but is used to internally classify and prioritize traffic through the switch.

By default 802.1p COS markings are trusted. Frames or packets without 802.1p markings will be set to `0`.

You can define what values are trusted in `qos_features.conf` by editing the line  
`traffic.packet_priority_source_set`

| traffic.packet_priority_source_set setting | Result |
| ------------------------------------------ | ------ | 
| 802.1p | Accept incoming 802.1p COS marking |
| dscp | Accept incoming DSCP IP header marking | 
| port | Ignore any existing markings and use `traffic.port_default_priority` setting | 

The `traffic.port_default_priority` accepts a value between 0 and 7 and defines what internal COS marking should be used when the `port` value is used in `traffic.port_default_priority`.

If the `traffic.packet_priority_source_set` is set to `cos` or `dscp` the ingress values can then be mapped to an internal COS value.

### Trust COS
In order to trust ingress COS markings set `traffic.packet_priority_source_set = [802.1p]` (the default).

When COS is trusted then the following lines are used to classify ingress COS values to internal COS values
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

The `traffic.cos_` number is the internal COS value, for example `traffic.cos_0` defines the mapping for internal COS 0. To map ingress COS 0 to internal COS 4, the configuration `traffic.cos_4.priority_source.8021p = [0]` is used.

Multiple ingress COS values can be mapped to the same internal value. For example, to map ingress COS values 0, 1 and 2 to internal COS 0,
```
traffic.cos_0.priority_source.8021p = [0, 1, 2]
```

You can also choose not to use an internal COS value. In this example we do not use internal COS values 3 or 4.
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

### Trust DSCP
To trust ingress DSCP markings configure `traffic.packet_priority_source_set = [dscp]`.

If DSCP is trusted then the following lines are used to classify ingress DSCP values to internal COS values
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
The `#` in the configuration file is a comment. By default the `traffic.cos_*.priority_source.dscp` lines are commented out.  
You must uncomment them for them to take effect.  
The existing `traffic_cos*.priority_source.8021p` **must** be commented out.
{{% /notice %}}

The `traffic.cos_` number is the internal COS value, for example `traffic.cos_0` defines the mapping for internal COS 0. To map ingress DSCP 22 to internal COS 4, the configuration `traffic.cos_4.priority_source.dscp = [22]` is used.

Multiple ingress DSCP values can be mapped to the same internal COS value. For example, to map ingress DSCP values 10, 21 and 36 to internal COS 0

```
traffic.cos_0.priority_source.dscp = [10,21,36]
```

You can also choose not to use an internal COS value. In this example we do not use internal COS values 3 or 4.
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

### Trust Port
To assign all traffic to an internal COS queue, regardless of the ingress marking configure `traffic.packet_priority_source_set = [port]`.

All traffic will be assigned to COS value defined by `traffic.port_default_priority`

Additional settings may be configured using {{<link text="Port Groups" url="#port-groups" >}}

## Traffic Marking and Remarking

Traffic can be marked or remarked in two different ways:

 * Using {{<link url="#using-iptables-for-marking" text="iptables" >}} to match packet settings and setting COS or DSCP values.
 * Using ingress COS or DSCP to remark an existing COS or DSCP value to a new value.

### Using iptables for marking
Cumulus supports the use of ACLs through `ebtables`, `iptables` or `ip6tables` for _egress_ packet marking.

`ebtables` is used to mark layer-2, 802.1p COS values.
`iptables` isused to match IPv4 traffic for DSCP marking while `ip6tables` is to match IPv6 traffic for DSCP marking.

{{% notice info %}}
More information on how to configure and apply ACLs please reference the {{<link title="Netfilter - ACLs" text="Netfilter - ACLs" >}} chapter.
{{% /notice %}}

#### Marking Layer-2 COS

You must use `ebtables` in order to match and mark layer-2 bridged traffic.

Traffic can be matched with any supported ebtables rule.  
When traffic is matched, to set the new COS value, use `-A FORWARD -o <interface> -j setqos --set-cos <value>`

{{% notice info %}}
COS can only be set on a _per-egress interface_ basis. `ebtables` based matching is not supported on ingress.
{{% /notice %}}

The configured action always has the following conditions:
* the rule is always configured as part of the `FORWARD` chain
* the interface (`<interface>`) is a physical swp port
* the "jump" action is always `setqos`, in lowercase
* the `--set-cos` value is a COS value between 0 and 7 (inclusive)

For example, to set traffic leaving interface `swp5` to COS value `4`, the following rule would be used  
`-A FORWARD -o swp5 -j setqos --set-cos 4`

#### Marking Layer-3 DSCP

You must use `iptables` (for IPv4 traffic) or `ip6tables` (for IPv6 traffic) to match and mark layer 3 traffic.

Traffic can be matched with any supported iptable or ip6tables rule. 
When traffic is matched, to mark the traffic, to set the new COS or DSCP value, use `-A FORWARD -o <interface> -j setqos [--set-dscp <value> | --set-cos <value> | --set-dscp-class <name>]`

The configured action always has the following conditions:
* the rule is always configured as part of the `FORWARD` chain
* the interface (`<interface>`) is a physical swp port
* the "jump" action is always `setqos`, in lowercase

COS markings may optionally be configured with `--set-cos` with a value between 0 and 7 (inclusive).

Only one of `--set-dscp` or `--set-dscp-class` may be used.  
`--set-dscp` supports decimal or hex DSCP values between 0 and 77.
`--set-dscp-class` supports standard DSCP naming described in [RFC3260](https://datatracker.ietf.org/doc/html/rfc3260) including `ef`, `be`, CS and AF classes. 

{{%notice note%}}
You can specify either `--set-dscp` or `--set-dscp-class`, but not both.
{{%/notice%}}

For example, to set traffic leaving interface `swp5` to DSCP value `32`, the following rule would be used  
`-A FORWARD -o swp5 -j setqos --set-dscp 32`

To set traffic leaving interface `swp11` to DSCP class value `CS6`, the following rule would be used  
`-A FORWARD -o swp11 -j setqos --set-dscp-class cs6`

<!--
You can put the rule in either the *mangle* table or the default *filter* table; the mangle table and filter table are put into separate TCAM slices in the hardware.
To put the rule in the mangle table, include `-t mangle`; to put the rule in the filter table, omit `-t mangle`.
-->

### Using ingress COS or DSCP for remarking
To define if COS or DSCP values should be remarked modify the `traffic.packet_priority_remark_set` value in `qos_features.conf`.

This configuration allows an internal COS value to determine the egress COS or DSCP value.

For example, to enable the remarking of only DSCP values use the following configuration  
`traffic.packet_priority_remark_set = [dscp]`

You can remark both COS and DSCP with  
`traffic.packet_priority_remark_set = [cos,dscp]`

#### Remarking COS
COS is remarked with the `priority_remark.8021p` component of `qos_features.conf`.

The internal `cos_` value determines the egress 802.1p COS remarking. 

For example, to remark internal COS 0 to egress COS 4, the following configuration would be used  
`traffic.cos_0.priority_remark.8021p = [4]`

{{% notice note %}}
The `#` in the configuration file is a comment. By default the `traffic.cos_*.priority_remark.8021p` lines are commented out.  
You must uncomment them for them for the configurations to be applied.
{{% /notice %}}

Multiple internal COS values can be remapped to the same external COS values. For example, to map internal COS 1 and internal COS 2 to external COS 3
```
traffic.cos_1.priority_remark.8021p = [3]
traffic.cos_2.priority_remark.8021p = [3]
```

{{% notice note %}}
If `traffic.packet_priority_remark_set` is configured to remark `cos` then all `traffic.cos_*.priority_remark.8021p` lines must be uncommented.
{{% /notice %}}

#### Remarking DSCP
DSCP is remarked with the `priority_remark.dscp` component of `qos_features.conf`.

The internal `cos_` value determines the egress DSCP remarking.

For example, to remark internal COS 0 to egress DSCP 22 the following configuration would be used
`traffic.cos_0.priority_remark.dscp = [22]`

{{% notice note %}}
The `#` in the configuration file is a comment. By default the `traffic.cos_*.priority_remark.dscp` lines are commented out.  
You must uncomment them for them for the configurations to be applied.
{{% /notice %}}

Multiple internal COS values can be remapped to the same external DSCP values. For example, to map internal COS 1 and internal COS 2 to external DSCP 40
```
traffic.cos_1.priority_remark.dscp = [40]
traffic.cos_2.priority_remark.dscp = [40]
```

{{% notice note %}}
If `traffic.packet_priority_remark_set` is configured to remark `dscp` then all `traffic.cos_*.priority_remark.dscp` lines must be uncommented.
{{% /notice %}}

## Using Port Groups
`qos_features.conf` supports the use of "port groups" to apply similar QoS configurations to a set of ports.

{{% notice note %}}
Any configurations used via port groups will override the global settings for the ingress ports defined in the port group.

Any ports that are not defined in a port group will use the global settings.
{{% /notice %}}

### Port Groups for Trust and Marking
Port groups are defined using the `source.port_group_list` configuration within `qos_features.conf`.

A `source.port_group_list` is one or more names to be used for group settings. The name is used as a label for configuration settings, for example, if a `source.port_group_list` included `test` the folllowing `port_default_priority` would be configured with `source.test.port_default_priority`. 

The following is an explanation of an example `source.port_group_list` configuration.
```
source.port_group_list = [customer1,customer2]
source.customer1.packet_priority_source_set = [dscp]
source.customer1.port_set = swp1-swp4,swp6
source.customer1.port_default_priority = 0
source.customer1.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]
source.customer2.packet_priority_source_set = [cos]
source.customer2.port_set = swp5,swp7
source.customer2.port_default_priority = 0
source.customer2.cos_1.priority_source.8021p = [4]
```

| Configuration                                 | Example                                                           | Explanation                                                                                                                                                                                                         |
| -------------                                 | -------                                                           | -----------                                                                                                                                                                                                         |
| `source.port_group_list`                      | `source.port_group_list = [customer1,customer2]`                  | Defines the names of the port groups to be used. Two groups are created `customer1` and `customer2`                                                                                                                 |
| `source.customer1.packet_priority_source_set` | `source.customer1.packet_priority_source_set = [dscp]`            | Defines the ingress marking trust. In this example ingress DSCP values will be preserved for group `customer1`                                                                                                      |
| `source.customer1.port_set`                   | `source.customer1.port_set = swp1-swp4,swp6`                      | The set of ports to apply the ingress marking trust policy to. In this example, ports swp1, swp2, swp3, swp4 and swp6 will be used for `customer1`                                                                  |
| `source.customer1.port_default_priority`      | `source.customer1.port_default_priority = 0`                      | Define the default internal COS marking for unmarked or untrusted traffic. In this example unmarked traffic or Layer 2 traffic for `customer1` ports will be marked with internal COS 0                             |
| `source.customer1.cos_0.priority_source`      | `source.customer1.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]` | Map the ingress DSCP values to an internal COS value for `customer1`. In this example the set of DSCP values from 0-7 are mapped to internal COS 0                                                                  |
| `source.customer2.packet_priority_source_set` | `source.packet_priority_source_set = [cos]`                       | Defines the ingress marking trust for `customer2`. In this example COS will be trusted                                                                                                                              |
| `source.customer2.port_set`                   | `source.customer2.port_set = swp5,swp7`                           | The set of ports to apply the ingress marking trust policy to. In this example, ports swp5 and swp7 will be used for `customer2`                                                                                    |
| `source.customer2.port_default_priority`      | `source.customer2.port_default_priority = 0`                      | Define the default internal COS marking for unmarked or untrusted traffic. In this example unmarked tagged layer 2 traffic or unmarked VLAN tagged traffic for `customer1` ports will be marked with internal COS 0 |
| `source.customer2.cos_0.priority_source`      | `source.customer2.cos_1.priority_source.8021p = [4]`              | Map the ingress COS values to an internal COS value for `customer2`. In this example ingress COS value 4 is mapped to internal COS 1                                                                                |

### Port Groups for Remarking
Port groups can also be used for remarking COS or DSCP on egress based on the internal COS value that was assigned. These port groups are defined with `remark.port_group_list` in `qos_features.conf`.

A `remark.port_group_list` is one or more names to be used for group settings. The name is used as a label for configuration settings, for example, if a `remark.port_group_list` included `test` the folllowing `remark.port_set` would be configured with `remark.test.port_set`.

The following is an explanation of an example `remark.group_list` configuration.

```
remark.port_group_list = [list1,list2]
remark.list1.port_set = swp1-swp3,swp6
remark.list1.cos_3.priority_remark.dscp = [24]
remark.list2.packet_priority_remark_set = [cos]
remark.list2.port_set = swp9,swp10
remark.list2.cos_3.priority_remark.8021p = [2]
```

|Configuration                             |Example                                           |Explanation                                                                                                                                                                                                                                 |
|-------------                             |-------                                           |-----------                                                                                                                                                                                                                                 |
|`remark.port_group_list`                  |`remark.port_group_list = [list1,list2]`          |Defines the names of the port groups to be used. Two groups are created `list1` and `list2`                                                                                                                                                 |
|`remark.list1.packet_priority_remark_set` |`remark.list1.packet_priority_remark_set = [dscp]`|Defines the egress marking to be applied, `cos` or `dscp`. In this example the egress DSCP marking will be rewritten                                                                                                                        |
|`remark.list1.port_set`                   |`remark.list1.port_set = swp1-swp3,swp6`          |The set of _ingress_ ports that received frames or packets that will have remarking applied, regardless of egress interface. In this example traffic arriving on ports swp1, swp2, swp3 and swp6 will have their egress DSCP values remarked|
|`remark.list1.cos_3.priority_remark.dscp` |`remark.list1.cos_3.priority_remark.dscp = [24]`  |The egress DSCP value to write to the packet based on the internal COS value. In this example, traffic in internal COS 3 will set the egress DSCP to 24                                                                                     |
|`remark.list2.packet_priority_remark_set` |`remark.list2.packet_priority_remark_set = [cos]` |Defines the egress marking to be applied, `cos` or `dscp`. In this example the egress COS marking will be rewritten                                                                                                                         |
|`remark.list2.port_set`                   |`remark.list2.port_set = swp9,swp10`              |The set of _ingress_ ports that received frames or packets that will have remarking applied, regardless of egress interface. In this example traffic arriving on ports swp9 and swp10 will have their egress COS values remarked            |
|`remark.list2.cos_4.priority_remark.8021p`|`remark.list1.cos_3.priority_remark.8021p = [2]`  |The egress COS value to write to the frame based on the internal COS value. In this example, traffic in internal COS 4 will set the egress COS 2                                                                                            |


## Flow Control 
Congestion control is used to help prevent traffic loss during times of congestion or to identify the traffic that should be preserved if packets must be dropped.

By default Cumulus Linux tail-drops packets exceeding the buffer. 

Cumulus supports the following congestion control mechanisms:

* Pause Frames - defined by IEEE 802.3x, uses specalized ethernet frames sent to an adjacent layer 2 switch to stop or "pause" _all_ traffic on the link during times of congestion. Pause frames are generally not recommended due to their scope of their impact.
* Priority Flow Control (PFC) - An upgrade of Pause Frames, defined by IEEE 802.1bb, extends the pause frame concept to act on a per-COS value basis instead of an entire link. A PFC pause frame indicates to the peer which specific COS value needs to pause, while other COS values or queues may continue transmitting.
* Explicit Congestion Notification (ECN) - Unlike Pause Frames and PFC which operate only at layer 2, ECN is an end-to-end layer 3 congestion control protocol. Defined by RFC 3168 ECN relies on bits in the IPv4 header Traffic Class to signal congestion conditions. ECN requires one or both server endpoints to support ECN to be effective.

### Pause Frames
Pause frames are an older congestion control mechnism that causes all traffic on a link between two devices (two switches or a host and switch) to stop transmitting during times of congestion. Pause frames are started and stoped based on how congested the buffer is. The value that determines when pause frames should start is called the `xoff` value (xoff for "transmit off") . When the buffer congestion reaches the `xoff` point the switch sends a pause frame to one or more neighbors.  
When congestion drops below the `xon` point (xon for "trasnmit on") an updated pause frame is sent to indicate that the neighbor should resume sending traffic.

{{% notice note %}}
Pause frames are not recommended due to the corse nature of flow control. Priority Flow Control (PFC) is recommended over the use of pause frames.
{{% /notice  %}}

Pause frames are configured on a per-direction, per-interface basis under the `link_pause` section of `qos_features.conf`.  
Setting `link_pause.pause_port_group.rx_enable = true` supports the reception of pause frames causing the switch to stop transmitting when requested.
Setting `link_pause.pause_port_group.tx_enable = true` supports the sending of pause frame causing the switch to request neighboring devices to stop transmitting.
Pause frames may be supported for either receive (`rx`), transmit (`tx`) or both.

{{% notice note %}}
The `#` in the configuration file is a comment. By default the `link_pause.` lines are commented out.  
You must uncomment them for them for the configurations to be applied.
{{% /notice %}}

By default, if link pause is enabled on one or more ports the following values are automatically derived:

* `link_pause.pause_port_group.port_buffer_bytes`
* `link_pause.pause_port_group.xoff_size`
* `link_pause.pause_port_group.xon_delta`

{{% notice warning %}}
Pause frame buffer calculation is a complex topic defined in IEEE 802.1Q-2012. This attempts to incorporate the delay between signaling congestion and the reception of the signal by the neighboring device. This calculation includes the delay introduced by the PHY and MAC layers (called the "interface delay") as well as the distance between end points (cable length).  
Incorrect cable length settings can cause wasted buffer space (triggering congestion too early) or packet drops (congestion occurs before flow control is activated).

Unless directed by NVIDIA support or engineering, it is not recommended to change these values.
{{% /notice %}}

The following is an explanation of an example `link_pause` configuration.

```
link_pause.port_group_list = [my_pause_ports]
link_pause.my_pause_ports.port_set = swp1-swp4,swp6
link_pause.my_pause_ports.port_buffer_bytes = 25000
link_pause.my_pause_ports.xoff_size = 10000
link_pause.my_pause_ports.xon_delta = 2000
link_pause.my_pause_ports.rx_enable = true
link_pause.my_pause_ports.tx_enable = true
#
link_pause.my_pause_ports.cable_length = 5
```

|Configuration                                |Example                                              |Explanation                                                                                                                                                                                                                                                                                                          |
|-------------                                |-------                                              |-----------                                                                                                                                                                                                                                                                                                          |
|`link_pause.port_group_list`                 |`link_pause.port_group_list = [my_pause_ports]`      |Creates a port_group to be used with pause frame settings. In this example the group is named `my_pause_ports`                                                                                                                                                                                                       |
|`link_pause.my_pause_ports.port_set`         |`link_pause.my_pause_ports.port_set = swp1-swp4,swp6`|Define the set of interfaces that pause frame configuration will be applied to. In this example ports swp1, swp2, swp3, swp4 and swp6 will have pause frame configurations applied                                                                                                                                   |
|`link_pause.my_pause_ports.port_buffer_bytes`|`link_pause.my_pause_ports.port_buffer_bytes = 25000`|The amount of reserved buffer space for the set of ports defined in the port_group_list. This is reserved from the global shared buffer                                                                                                                                                                              |
|`link_pause.my_pause_ports.xoff_size`        |`link_pause.my_pause_ports.xoff_size = 10000`        |Set the amount of reserved buffer that must be consumed before a pause frame will be sent out the set of interfaces defined in the port_group_list, if transmitting pause frames is enabled. In this example after 10000 bytes of reserved buffer is consumed pause frames will be sent.                             |
|`link_pause.my_pause_ports.xon_delta`        |`link_pause.my_pause_ports.xon_delta = 2000`         |The number of bytes below the `xoff` threshold that the buffer consumption must drop below before the sending of pause frame stops, if transmitting pause frames is enabled. In this example the buffer congestion must reduce by 2000 bytes (to 8000 bytes) before pause frame will stop                            |
|`link_pause.my_pause_ports.rx_enable`        |`link_pause.my_pause_ports.tx_enable = true`         |Enable (`true`) or disable (`false`) the sending of pause frames. The default value is `false`. In this example the sending of pause frames is enabled                                                                                                                                                               |
|`link_pause.my_pause_ports.tx_enable`        |`link_pause.my_pause_ports.rx_enable = true`         |Enable (`true`) or disable (`false`) acting to the reception of a pause frame. The default value is `false`. In this example the reception of pause frames is enabled                                                                                                                                                |
|`link_pause.my_pause_ports.cable_length`     |`link_pause.pause_port_group.cable_length = 5`       |The length, in meters, of the cable attached to the port defined in the port_group_list. This value is used internally to determine the latency between generating a pause frame and the reception of the pause frame. The default is `10` meters. In this example the cable attached has been defined as `5` meters.|

### Priority flow control (PFC)

Priority flow control extends the capabilities of pause frames by sending pause frames for a specific COS value instead of stopping all traffic on a link. If a switch supports PFC and receives a PFC pause frame for a given COS value the switch will stop transmitting frames from that queue, but will continue transmitting frames for other queues.

PFC pause frames are configured on a per-direction, per-interface basis under the `pfc` section of `qos_features.conf`.  
Setting `pfc.pfc_port_group.rx_enable = true` supports the reception of PFC pause frames causing the switch to stop transmitting when requested.
Setting `pfc.pfc_port_group.tx_enable = true` supports the sending of PFC pause frames, for the defined COS values, causing the switch to request neighboring devices to stop transmitting.
PFC pause frames may be supported for either receive (`rx`), transmit (`tx`) or both.

{{% notice note %}}
The `#` in the configuration file is a comment. By default the `pfc.` lines are commented out.  
You must uncomment them for them for the configurations to be applied.
{{% /notice %}}

By default, if link pause is enabled on one or more ports the following values are automatically derived:

* `pfc.pause_port_group.port_buffer_bytes`
* `pfc.pause_port_group.xoff_size`
* `pfc.pause_port_group.xon_delta`

{{% notice note %}}
PFC buffer calculation is a complex topic defined in IEEE 802.1Q-2012. This attempts to incorporate the delay between signaling congestion and the reception of the signal by the neighboring device. This calculation includes the delay introduced by the PHY and MAC layers (called the "interface delay") as well as the distance between end points (cable length).  
Incorrect cable length settings can cause wasted buffer space (triggering congestion too early) or packet drops (congestion occurs before flow control is activated).

Unless directed by NVIDIA support or engineering, it is not recommended to change these values.
{{% /notice %}}


{{% notice note %}}
The `#` in the configuration file is a comment. By default the `pfc.` lines are commented out.  
You must uncomment them for them for the configurations to be applied.
{{% /notice %}}


The following is an explanation of an example `pfc` configuration.

```
pfc.port_group_list = [my_pfc_ports]
pfc.my_pfc_ports.cos_list = [3,5]
pfc.my_pfc_ports.port_set = swp1-swp4,swp6
pfc.my_pfc_ports.port_buffer_bytes = 25000
pfc.my_pfc_ports.xoff_size = 10000
pfc.my_pfc_ports.xon_delta = 2000
pfc.my_pfc_ports.tx_enable = true
pfc.my_pfc_ports.rx_enable = true
#
pfc.my_pfc_ports.cable_length = 10
```

| Configuration | Example | Explanation |
| ------------- | ------- | ----------- |
| `pfc.port_group_list` | `pfc.port_group_list = [my_pfc_ports]` | Creates a port_group to be used with PFC pause frame settings. In this example the group is named `my_pfc_ports` |
| `pfc.my_pfc_ports.cos_list` | `pfc.my_pfc_ports.cos_list = [3,5]` | Define the COS values that will support sending PFC pause frames, if enabled. In this example COS values 3 and 5 are enabled to send PFC pause frames.|
| `pfc.my_pfc_ports.port_set` | `pfc.my_pfc_ports.port_set = swp1-swp4,swp6` | Define the set of interfaces that PFC pause frame configuration will be applied to. In this example ports swp1, swp2, swp3, swp4 and swp6 will have pause frame configurations applied |
| `pfc.my_pfc_ports.port_buffer_bytes` | `pfc.my_pfc_ports.port_buffer_bytes = 25000` | The amount of reserved buffer space for the set of ports defined in the port_group_list. This is reserved from the global shared buffer |
| `pfc.my_pfc_ports.xoff_size` | `pfc.my_pfc_ports.xoff_size = 10000` | Set the amount of reserved buffer that must be consumed before a PFC pause frame will be sent out the set of interfaces defined in the port_group_list, if transmitting pause frames is enabled. In this example after 10000 bytes of reserved buffer is consumed PFC pause frames will be sent.|
| `pfc.my_pfc_ports.xon_delta` | `pfc.my_pfc_ports.xon_delta = 2000` | The number of bytes below the `xoff` threshold that the buffer consumption must drop below before the sending of PFC pause frames stops, if transmitting pause frames is enabled. In this example the buffer congestion must reduce by 2000 bytes (to 8000 bytes) before PFC pause frame will stop |
| `pfc.my_pfc_ports.rx_enable` | `pfc.my_pfc_ports.tx_enable = true` | Enable (`true`) or disable (`false`) the sending of PFC pause frames. The default value is `false`. In this example the sending of PFC pause frames is enabled |
| `pfc.my_pfc_ports.tx_enable` | `pfc.my_pfc_ports.rx_enable = true` | Enable (`true`) or disable (`false`) acting to the reception of a PFC pause frame. For `rx_enable` the COS values do not need to be defined. Any COS value a PFC pause is received for will be respected. The default value is `false`. In this example the reception of PFC pause frames is enabled |
| `pfc.my_pfc_ports.cable_length` | `pfc.my_pfc_ports.cable_length = 5` | The length, in meters, of the cable attached to the port defined in the port_group_list. This value is used internally to determine the latency between generating a PFC pause frame and the reception of the PFC pause frame. The default is `10` meters. In this example the cable attached has been defined as `5` meters.|

### Explicit Congestion Notification (ECN)

Unlike Pause Frames or PFC, ECN is an end-to-end flow control technology. Instead of telling adjacent devices to stop transmitting during times of buffer congestion ECN sets the ECN bits of transit IPv4 or IPv6 header to indicate to end-hosts that congestion may occur. As a result the sending hosts will reduce their sending rate until the ECN bits are no longer being set by the transit switch.

ECN operates by having a transit switch mark packets being sent between two end-hosts.
1. Transmitting host indicates it is ECN-capable by setting the ECN bits in the outgoing IP header to `01` or `10`
2. If the buffer of a transit switch is greater than the configured `min_threshold_bytes` the switch will remark the ECN bits to `11` indicating "Congestion Encountered" or "CE".
3. The receiving host will mark any reply packets, like a TCP-ACK, as CE (`11`)
4. The original transmitting host will reduce its transmission rate.
5. When the switch buffer congestion falls below the configured `min_threshold_bytes` the switch will stop remarking ECN bits, setting them back to `01` or `10`.
6. A receiving host reflects this new ECN marking in the next reply, indicating the transmitting host should resume sending at normal speeds.

The following is the default ECN configuration.

```
default_ecn_conf.egress_queue_list = [0]
default_ecn_conf.ecn_enable = true
default_ecn_conf.min_threshold_bytes = 150000
default_ecn_conf.max_threshold_bytes = 1500000
default_ecn_conf.probability = 100
```

|Configuration                       |Example                                       |Explanation|
| ------------- | ------- | ----------- |
|`default_ecn_conf.egress_queue_list`  |`default_ecn_conf.egress_queue_list` = [0]      | The list of ECN enabled queues. By default a single queue exists |
|`default_ecn_conf.ecn_enable`         |`default_ecn_conf.ecn_enable` = true            | Enable (`true`) or disable (`false`) the marking of ECN bits |
|`default_ecn_conf.min_threshold_bytes`|`default_ecn_conf.min_threshold_bytes` = 150000 | The minimum threshold of the buffer in bytes. Random ECN marking starts when buffer congestion crosses this threshold. The probability of ECN marking is based on the `default_ecn_conf.probability` value. | 
|`default_ecn_conf.max_threshold_bytes`|`default_ecn_conf.max_threshold_bytes` = 1500000| The maximum threshold of the buffer in bytes. All ECN-capable packets are marked when buffer congestion crosses this threshold. | 
|`default_ecn_conf.probability`        |`default_ecn_conf.probability` = 100            | The probability, in percent, that an ECN-capable packet will be marked when buffer congestion is between the `default_ecn_conf.min_threshold_bytes` and `default_ecn_conf.max_threshold_bytes`. The default is 100, meaning all ECN-capable packets will be marked. |

### Random Early Detection (RED)
The goal of ECN is to prevent packet drops in the network due to congestion by signaling hosts to transmit less. However, if congestion continues after ECN marking packets will be dropped once the switch buffer is full. By default Cumulus Linux tail-drops packets when the buffer is full.

Optionally, Random Early Detection (RED) can be configured to randomly drop packets that are currently in the queue instead of always dropping the last arriving packet. This may improve overall performance of TCP based flows. 

RED is configured by changing the value of `default_ecn_conf.red_enable` to `true`.

 `default_ecn_conf.red_enable = false`
## Policing and Shaping

Traffic shaping and policing are used to control the rate in which traffic is sent or received on a network to prevent congestion. 

{{% notice note %}}
Traffic shaping is generally used egress while traffic policing is used ingress.
{{% /notice %}}
### Shaping
Traffic shaping allows a switch to send traffic at and average bitrate lower than the physical interface. Traffic shaping prevents bursty traffic from being dropped by a receiving device that is either not capaible of that rate of traffic or may have a policer limiting what will be accepted, for example, an ISP.

Traffic shaping works by holding packets in the buffer and releasing them at time intervals called the `tc`. 

Cumulus Linux supports two-levels of hierarchial traffic shaping: one at the egress-queue level and one at the port level. This allows for minimum and maximum bandwidth guarantees for each egress-queue and a defined interface traffic shaping rate.

Traffic shaping is configured in the `shaping.` section of `qos_features.conf`. 
Traffic shaping configuration supports {{<link text="Port Groups" url="#port-groups" >}} to apply different shaping profiles to different ports. 

Each queue is an internal COS value, for example `egr_queue_3` is for traffic mapped to internal COS value 3.

This is an example traffic shaping configuration.
```
shaping.port_group_list = [shaper_port_group]
shaping.shaper_port_group.port_set = swp1-swp3,swp5
shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]
shaping.shaper_port_group.port.shaper = 900000
```
|Configuration                                 |Example                                                         |Explanation|
|----                                          |----                                                            |---        |
|`shaping.port_group_list`                     |`shaping.port_group_list = [shaper_port_group]`                 | Creates a port_group to be used with traffic shaping settings. In this example the group is named `shaper_port_group`          |
|`shaping.shaper_port_group.port_set  `        |`shaping.shaper_port_group.port_set = swp1-swp3,swp5`           | Define the set of interfaces that traffic shaping configurations will be applied to. In this example ports swp1, swp2, swp3 and swp5 will have traffic shaping applied         |
|`shaping.shaper_port_group.egr_queue_0.shaper`|`shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]`| Applies a minimum and maximum bandwidth value in kbps for interal COS group 0. In this example internal COS 0 will always have at least `50000` kbps of bandwidth with a maximum of `100000` kbps      |
|`shaping.shaper_port_group.port.shaper`       |`shaping.shaper_port_group.port.shaper = 900000`                | Applies the maximum packet shaper rate at the interface level. In this example, interfaces swp1, swp2, swp3 and swp5 will not transmit greater than `900000` kbps.          |

Defining a queue minimum shaping value of `0` means there is no bandwidth guarantee for this queue.
The maximum queue shaping value can not exceed the interface shaping value defined by `port.shaper`.
The `port.shaper` value can not exceed the physical interface speed.

## Troubleshooting
### Syntax Checker
Cumulus Linux provides a syntax checker for the `/etc/cumulus/datapath/traffic.conf` file to check for errors, such missing parameters, or invalid parameter labels and values.

You can run the syntax checker manually from the command line by issuing the `cl-consistency-check --datapath-syntax-check` command. If errors exist, they are written to `stderr` by default. If you run the command with `-q`, errors are written to the `/var/log/switchd.log` file.

The `cl-consistency-check --datapath-syntax-check` command takes the following options:

| <div style="width:120px">Option | Description |
| ------------------------------- | ----------- |
| -h | Displays this list of command options. |
| -q | Runs the command in quiet mode. Errors are written to the `/var/log/switchd.log` file instead of `stderr`. |
| -t `<file-name>` | Runs the syntax check on a non-default `traffic.conf` file; for example, `/mypath/test-traffic.conf`.|

You can run the syntax checker when `switchd` is either running or stopped.

**Example Commands**

The following example command runs the syntax checker on the default `/etc/cumulus/datapath/traffic.conf` file and shows that no errors are detected:

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check
No errors detected in traffic config file /etc/cumulus/datapath/traffic.conf
```

The following example command runs the syntax checker on the default `/etc/cumulus/datapath/traffic.conf` file in quiet mode. If errors exist, they are written to the `/var/log/switchd.log` file.

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check -q
```

The following example command runs the syntax checker on the `/mypath/test-traffic.conf` file and shows that errors are detected:

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check -t /path/test-traffic.conf
Traffic source 8021p: missing mapping for priority value '7'
Errors detected while checking traffic config file /mypath/test-traffic.conf
```

The following example command runs the syntax checker on the `/mypath/test-traffic.conf` file in quiet mode. If errors exist, they are written to the `/var/log/switchd.log` file.

```
cumulus@switch:~$ cl-consistency-check --datapath-syntax-check -t /path/test-traffic.conf -q
```

## Default Configuration Files
### qos_features.conf
<details>
<summary>Default qos_features.conf File</summary>
    #
    # /etc/cumulus/datapath/qos/qos_features.conf
    # Copyright (C) 2021 NVIDIA Corporation. ALL RIGHTS RESERVED.
    #
    
    # packet header field used to determine the packet priority level
    # fields include {802.1p, dscp, port}
    traffic.packet_priority_source_set = [802.1p]
    traffic.port_default_priority      = 0
    
    # packet priority source values assigned to each internal cos value
    # internal cos values {cos_0..cos_7}
    # (internal cos 3 has been reserved for CPU-generated traffic)
    #
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
    #
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
    #
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
    #
    # Specify cable length in mts
    # link_pause.pause_port_group.cable_length = 10
    
    # Explicit Congestion Notification
    # to configure ECN and RED on a group of ports:
    # -- add or replace port group names in the port group list
    # -- assign cos value(s) to the cos list
    # -- for each port group in the list
    #    -- populate the port set, e.g.
    #       swp1-swp4,swp8,swp50s0-swp50s3
    # -- to enable RED requires the latest qos_features.conf
    #ecn_red.port_group_list = [ecn_red_port_group]
    #ecn_red.ecn_red_port_group.egress_queue_list = []
    #ecn_red.ecn_red_port_group.port_set = swp1-swp4,swp6
    #ecn_red.ecn_red_port_group.ecn_enable = true
    #ecn_red.ecn_red_port_group.red_enable = false
    #ecn_red.ecn_red_port_group.min_threshold_bytes = 40000
    #ecn_red.ecn_red_port_group.max_threshold_bytes = 200000
    #ecn_red.ecn_red_port_group.probability = 100
    
    #Default ECN configuration on TC0
    default_ecn_conf.egress_queue_list = [0]
    default_ecn_conf.ecn_enable = true
    default_ecn_conf.red_enable = false
    default_ecn_conf.min_threshold_bytes = 150000
    default_ecn_conf.max_threshold_bytes = 1500000
    default_ecn_conf.probability = 100
    
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
</details>

### qos_infra.conf
<details>
<summary>Default qos_infra.conf File</summary>
    ### qos_infra.conf
    #
    # Default qos_infra configuration for Mellanox Spectrum chip
    # Copyright (C) 2021 NVIDIA Corporation. ALL RIGHTS RESERVED.
    #
    
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
    #
    # total buffer
    #  - ingress minimum buffer allocations
    #  - ingress service pool buffer allocations
    #  - priority group ingress headroom allocations
    #  - ingress global headroom allocations
    #  = total ingress shared buffer size
    
    # ingress service pool buffer allocation: percent of total buffer
    # If a service pool has no priority groups, the buffer is added
    # to the shared buffer space.
    ingress_service_pool.0.percent = 100.0# all priority groups
    
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
    #ingress_service_pool.0.mode = 0
    
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
    #priority_group.bulk.ingress_buffer.dynamic_quota      = ALPHA_8
    
    # --- egress buffer space allocations ---
    #
    # total egress buffer
    #  - minimum buffer allocations
    #  = total service pool buffer size
    #
    # service pool assigned for lossless PGs
    #flow_control.egress_service_pool = 0
    #
    # service pool assigned for egress queues
    egress_buffer.egr_queue_0.uc.service_pool = 0
    egress_buffer.egr_queue_1.uc.service_pool = 0
    egress_buffer.egr_queue_2.uc.service_pool = 0
    egress_buffer.egr_queue_3.uc.service_pool = 0
    egress_buffer.egr_queue_4.uc.service_pool = 0
    egress_buffer.egr_queue_5.uc.service_pool = 0
    egress_buffer.egr_queue_6.uc.service_pool = 0
    egress_buffer.egr_queue_7.uc.service_pool = 0
    #
    # Service pool buffer allocation: percent of total
    # buffer size.
    egress_service_pool.0.percent = 100.0# all priority groups, UC and MC
    
    # Egress buffer port.pool buffer : size in bytes
    #port.service_pool.0.egress_buffer.uc.reserved = 10240
    #port.service_pool.0.egress_buffer.uc.shared_size = 9000
    #port.management.egress_buffer.reserved = 0
    
    # Front panel port egress buffer limits enforced for each
    # priority group.
    # Unlimited egress buffers not supported on Spectrum.
    #priority_group.bulk.unlimited_egress_buffer     = false
    
    #
    # if a priority group has no cos values assigned to it, the buffers will not be allocated
    #
    
    # Service pool mapping for MC.SP region
    egress_buffer.cos_0.mc.service_pool = 0
    egress_buffer.cos_1.mc.service_pool = 0
    egress_buffer.cos_2.mc.service_pool = 0
    egress_buffer.cos_3.mc.service_pool = 0
    egress_buffer.cos_4.mc.service_pool = 0
    egress_buffer.cos_5.mc.service_pool = 0
    egress_buffer.cos_6.mc.service_pool = 0
    egress_buffer.cos_7.mc.service_pool = 0
    #
    # Reserved and static shared buffer allocation for MC.SP region: size in bytes
    #egress_buffer.cos_0.mc.reserved = 10240
    #egress_buffer.cos_1.mc.reserved = 10240
    #egress_buffer.cos_2.mc.reserved = 10240
    #egress_buffer.cos_3.mc.reserved = 10240
    #egress_buffer.cos_4.mc.reserved = 10240
    #egress_buffer.cos_5.mc.reserved = 10240
    #egress_buffer.cos_6.mc.reserved = 10240
    #egress_buffer.cos_7.mc.reserved = 10240
    #
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
    #egress_buffer.egr_queue_0.uc.reserved  = 1024
    #egress_buffer.egr_queue_1.uc.reserved  = 1024
    #egress_buffer.egr_queue_2.uc.reserved  = 1024
    #egress_buffer.egr_queue_3.uc.reserved  = 1024
    #egress_buffer.egr_queue_4.uc.reserved  = 1024
    #egress_buffer.egr_queue_5.uc.reserved  = 1024
    #egress_buffer.egr_queue_6.uc.reserved  = 1024
    #egress_buffer.egr_queue_7.uc.reserved  = 1024
    
    # Reserved Egress buffer for TCs mapped to lossless SPs
    #flow_control.egress_buffer.reserved = 0
    
    # Egress buffer ePort.MC buffer : size in bytes
    # the per-port limit on multicast packets (applies to all switch priorities)
    #port.egress_buffer.mc.reserved = 10240
    #port.egress_buffer.mc.shared_size = 92160
    
    # To enable egress static pool, set the mode to 0
    #egress_service_pool.0.mode = 0
    
    # Egress dynamic buffer pool configuration
    # Replace the shared_size parameter with the dynamic_quota=n/ALPHA_x,
    # where ‘n’ should be the configuration value for alpha.
    # 		‘ALPHA_x’ should be string representation for alpha.
    # Pls note : Same alpha configuration values can be used as mentioned in Ingress Dynamic Buffering section above
    #
    # Egress buffer per-port dynamic buffering quota (alpha ; Default: ALPHA_16)
    #port.service_pool.0.egress_buffer.uc.dynamic_quota = ALPHA_16
    #port.management.egress_buffer.dynamic_quota = ALPHA_8
    
    # Egress buffer per-egress-queue dynamic buffering quota (alpha) for lossless egress queues (Default: ALPHA_INFINITY)
    #flow_control.egress_buffer.dynamic_quota = ALPHA_INFINITY
    
    # Egress buffer per-egress-queue dynamic buffering quota (alpha) for unicast (Default: ALPHA_8)
    #egress_buffer.egr_queue_0.uc.dynamic_quota    = ALPHA_2
    #egress_buffer.egr_queue_1.uc.dynamic_quota = ALPHA_4
    #egress_buffer.egr_queue_2.uc.dynamic_quota = ALPHA_1
    #egress_buffer.egr_queue_3.uc.dynamic_quota = ALPHA_1_2
    #egress_buffer.egr_queue_4.uc.dynamic_quota = ALPHA_1_4
    #egress_buffer.egr_queue_5.uc.dynamic_quota = ALPHA_1_8
    #egress_buffer.egr_queue_6.uc.dynamic_quota = ALPHA_1_16
    #egress_buffer.egr_queue_7.uc.dynamic_quota = ALPHA_1_32
    
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
    #egress_buffer.cos_1.mc.dynamic_quota = ALPHA_8
    #egress_buffer.cos_2.mc.dynamic_quota = ALPHA_4
    #egress_buffer.cos_3.mc.dynamic_quota = ALPHA_2
    #egress_buffer.cos_4.mc.dynamic_quota = ALPHA_1_8
    #egress_buffer.cos_5.mc.dynamic_quota = ALPHA_1
    #egress_buffer.cos_6.mc.dynamic_quota = ALPHA_1_2
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
</details>

## Caveats
### Configuring QoS and Breakout Ports Simultaneously
If both breakout ports are configured by modifying `ports.conf` and QoS settings via `qos_features.conf` and `restart switchd` to apply the settings errors may occur. 

Breakout port configuration must be applied before QoS configuration can be applied on the breakout ports. Modify `ports.conf` first, `restart switchd` then modify `qos_features.conf` and `restart switchd` a second time.

### QoS Settings Applied on a Bond Member Interfaces
If QoS settings are applied on bond member interfaces instead of the logical bond interface, the members must share identical QoS configuration. If the configuration is not identical between bond interfaces the bond will inherit the _last_ interface applied to the bond. 

It is also possible that a restart or reload of `switchd` will fail.

### Cut-Through Switching
Cut-through switching can _not_ be disabled on Spectrum ASICs. Setting `cut_through_enable = false` in `qos_features.conf` will either be ignored or cause a `switchd` restart to fail.