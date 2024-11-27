---
title: Buffer and Queue Management
author: NVIDIA
weight: 320
toc: 3
---
Hardware datapath configuration manages packet buffering, queueing and scheduling in hardware.

{{%notice note%}}

The `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/[bcm|mlx]/datapath.conf` assigns buffer space and egress queues. The default thresholds defined in the `datapath.conf` file are intended for data center environments, but certain workloads may require additional tuning. It is best to make small, incremental changes to validate the changes with your application performance. Be sure to back up the original file before making changes.

{{%/notice%}}

Each packet is assigned to an ASIC Class of Service (CoS) value based on the priority value of the packet stored in the 802.1p (Class of Service) or DSCP (Differentiated Services Code Point) header field. The choice to schedule packets based on COS or DSCP is a configurable option in the `/etc/cumulus/datapath/traffic.conf` file.

Priority groups include:

- *Control*: Highest priority traffic
- *Service*: Second-highest priority traffic
- *Bulk*: All remaining traffic

The scheduler is configured to use a hybrid scheduling algorithm. It applies strict priority to control traffic queues and a weighted round robin selection from the remaining queues. Unicast packets and multicast packets with the same priority value are assigned to separate queues, which are assigned equal scheduling weights.

{{%notice note%}}

You can configure Quality of Service (QoS) for switches on the following platforms only:

- Broadcom Tomahawk, Trident II, Trident II+, and Trident3
- Mellanox Spectrum, Spectrum-2, and Spectrum-3

{{%/notice%}}

## Traffic Marking

You can mark traffic for egress packets through `iptables` or `ip6tables` rule classifications. To enable these rules, you do one of the following:

- Mark DSCP values in egress packets.
- Mark 802.1p CoS values in egress packets.

To enable traffic marking, use `cl-acltool`. Add the `-p` option to specify the location of the policy file. By default, if you do not include the `-p` option, `cl-acltool` looks for the policy file in `/etc/cumulus/acl/policy.d/`.

The `iptables`-/`ip6tables`-based marking is supported with the following action extension:

```
-j SETQOS --set-dscp 10 --set-cos 5
```

For `ebtables`, the setqos keyword must be in lowercase, as in:

```
[ebtables]
-A FORWARD -o swp5 -j setqos --set-cos 5
```

You can specify one of the following targets for SETQOS/setqos:

| Option<img width=400/>| Description<img width=400/>|
|----------------|---------------|
| `--set-cos INT` | Sets the datapath resource/queuing class value. Values are defined in {{<exlink url="http://en.wikipedia.org/wiki/IEEE_P802.1p" text="IEEE P802.1p">}}.|
| `--set-dscp value`| Sets the DSCP field in packet header to a value, which can be either a decimal or hex value.|
| `--set-dscp-class class`| Sets the DSCP field in the packet header to the value represented by the DiffServ class value. This class can be EF, BE or any of the CSxx or AFxx classes.|

{{%notice note%}}

You can specify either `--set-dscp` or `--set-dscp-class`, but not both.

{{%/notice%}}

Here are two example rules:

```
[iptables]
-t mangle -A FORWARD --in-interface swp+ -p tcp --dport bgp -j SETQOS --set-dscp 10 --set-cos 5

[ip6tables]
-t mangle -A FORWARD --in-interface swp+ -j SETQOS --set-dscp 10
```

You can put the rule in either the *mangle* table or the default *filter* table; the mangle table and filter table are put into separate TCAM slices in the hardware.

To put the rule in the mangle table, include `-t mangle`; to put the rule in the filter table, omit `-t mangle`.

## Priority Flow Control

*Priority flow control*, as defined in the {{<exlink url="http://www.ieee802.org/1/pages/802.1bb.html" text="IEEE 802.1Qbb standard">}}, provides a link-level flow control mechanism that can be controlled independently for each Class of Service (CoS) with the intention to ensure no data frames are lost when congestion occurs in a bridged network.

{{%notice note%}}

PFC is not supported on switches with the Helix4 ASIC.

{{%/notice%}}

PFC is a layer 2 mechanism that prevents congestion by throttling packet transmission. When PFC is enabled for received packets on a set of switch ports, the switch detects congestion in the ingress buffer of the receiving port and signals the upstream switch to stop sending traffic. If the upstream switch has PFC enabled for packet transmission on the designated priorities, it responds to the downstream switch and stops sending those packets for a period of time.

PFC operates between two adjacent neighbor switches; it does not provide end-to-end flow control. However, when an upstream neighbor throttles packet transmission, it could build up packet congestion and propagate PFC frames further upstream: eventually the sending server could receive PFC frames and stop sending traffic for a time.

The PFC mechanism can be enabled for individual switch priorities on all or specific switch ports for received and/or transmitted traffic. The ingress buffer occupancy of the switch port is used to measure congestion. If congestion is present, the switch transmits flow control frames to the upstream switch. Packets with priority values that do not have PFC configured are not counted during congestion detection and they do not get throttled by the upstream switch when it receives flow control frames.

PFC congestion detection is implemented on the switch using xoff and xon threshold values for the specific ingress buffer used by the targeted switch priorities. When a packet enters the buffer and the buffer occupancy is above the xoff threshold, the switch transmits an Ethernet PFC frame to the upstream switch to signal packet transmission must stop. When the buffer occupancy drops below the xon threshold, the switch sends another PFC frame upstream to signal that packet transmission can resume. (PFC frames contain a quanta value to indicate a timeout value for the upstream switch: packet transmission can resume after the timer has expired or when a PFC frame with quanta == 0 is received from the downstream switch.)

After the downstream switch sends a PFC frame upstream, it continues to receive packets until the upstream switch receives and responds to the PFC frame. The downstream ingress buffer must be large enough to store those additional packets after the xoff threshold is reached.

Priority flow control is fully supported on both {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Broadcom">}} (including the Edgecore Minipack-AS8000/Trident3) and {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Mellanox">}} switches.

PFC is disabled by default in Cumulus Linux. To configure PFC, update and uncomment the settings in the `priority flow control` section of the `/etc/cumulus/datapath/traffic.conf` file.

```
# to configure priority flow control on a group of ports:
# -- assign cos value(s) to the cos list
# -- add or replace port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a PFC buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers PFC frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers PFC frames transmit to stop)
#    -- enable PFC frame transmit and/or PFC frame receive

# priority flow control
pfc.port_group_list = [pfc_port_group]
pfc.pfc_port_group.cos_list = []
pfc.pfc_port_group.port_set = swp1-swp4,swp6
pfc.pfc_port_group.port_buffer_bytes = 25000
pfc.pfc_port_group.xoff_size = 10000
pfc.pfc_port_group.xon_delta = 2000
pfc.pfc_port_group.tx_enable = true
pfc.pfc_port_group.rx_enable = true
#
# Specify cable length in mts
pfc.pfc_port_group.cable_length = 10
```

| PFC Setting | Description |
| ---- | ----- |
| `pfc.port_group_list` | The name of the port group in brackets. |
| `pfc.pfc_port_group.cos_list` | The CoS value to the ports. |
| `pfc.pfc_port_group.port_set` | The ports in the port group. |
| `pfc.pfc_port_group.port_buffer_bytes` | The PFC buffer size. This is the maximum number of bytes allocated for storing bursts of packets, guaranteed at the ingress port. The default is *25000* bytes.<br>This setting is optional. If not provided, the value is derived from the port speed, port MTU, or port cable length. |
| `pfc.pfc_port_group.xoff_size` | The xoff byte limit. This is a threshold for the PFC buffer; when this limit is reached, an xoff transition is initiated, signaling the upstream port to stop sending traffic, during which time packets continue to arrive due to the latency of the communication. The default is *10000* bytes.<br>This setting is optional. If not provided, the value is derived from the port speed, port MTU, or port cable length.|
| `pfc.pfc_port_group.xon_delta` | The xon delta limit. This is the number of bytes to subtract from the xoff limit, which results in a second threshold at which the egress port resumes sending traffic. After the xoff limit is reached and the upstream port stops sending traffic, the buffer begins to drain. When the buffer reaches 8000 bytes (assuming default xoff and xon settings), the egress port signals that it can start receiving traffic again. The default is *2000* bytes.<br>This setting is optional. If not provided, the value is derived from the port speed, port MTU, or port cable length. |
| `pfc.pfc_port_group.tx_enable` | Enables the egress port to signal the upstream port to stop sending traffic. The default is *true*. |
| `pfc.pfc_port_group.rx_enable` | Enables the egress port to receive notifications and act on them. The default is *true*. |
| `pfc.pfc_port_group.cable_length` | The length of the port group cable. |

On Broadcom switches, after you modify the settings in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

{{<cl/restart-switchd>}}

On NVIDIA Spectrum switches, changes to the settings in the `/etc/cumulus/datapath/traffic.conf` file do *not* require you to restart `switchd`. However, you must run the `echo 1 > /cumulus/switchd/config/traffic/reload` command to apply the settings.

```
cumulus@switch:~$ echo 1 > /cumulus/switchd/config/traffic/reload
```

Always run the {{<link url="#syntax-checker" text="syntax checker">}} syntax checker before applying the configuration changes.

## Port Groups

A *port group* refers to one or more sequences of contiguous ports. You can define multiple port groups by adding:

- A comma-separated list of port group names to the `port_group_list`.
- The `port_set`, `rx_enable`, and `tx_enable` configuration lines for each port group.

You can specify the set of ports in a port group in comma-separate sequences of contiguous ports; you can see which ports are contiguous in the `/var/lib/cumulus/porttab` file. The syntax supports:

- A single port (swp1s0 or swp5).
- A sequence of regular swp ports (swp2-swp5).
- A sequence within a breakout swp port (swp6s0-swp6s3).
- A sequence of regular and breakout ports, provided they are all in a contiguous range. For example:

```
...
swp2
swp3
swp4
swp5
swp6s0
swp6s1
swp6s2
swp6s3
swp7
...
```

## Link Pause

The PAUSE frame is a flow control mechanism that halts the transmission of the transmitter for a specified period of time, which might be needed if a server or other network node within the data center receives traffic faster than it can handle. In Cumulus Linux, you can configure individual ports to execute link pause by:

- Transmitting pause frames when the ingress buffers become congested (TX pause enable).
- Responding to received pause frames (RX pause enable).

Link pause is disabled by default. To enable link pause, you must configure settings in the `/etc/cumulus/datapath traffic.conf` file.

{{< expand "What's the difference between link pause and priority flow control?" >}}

- Priority flow control is applied to an individual priority group for a specific ingress port.
- Link pause (also known as port pause or global pause) is applied to all the traffic for a specific ingress port.

{{< /expand >}}

Here is an example configuration that enables TX pause and RX pause for swp1 through swp4 and swp6:

``` 
# to configure pause on a group of ports:
# -- add or replace port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a pause buffer size in bytes for each port
#    -- set the xoff byte limit (buffer limit that triggers pause frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers pause frames transmit to stop)
#    -- enable pause frame transmit and/or pause frame receive

 link pause
 link_pause.port_group_list = [pause_port_group]
 link_pause.pause_port_group.port_set = swp1-swp4,swp6
 link_pause.pause_port_group.port_buffer_bytes = 25000
 link_pause.pause_port_group.xoff_size = 10000
 link_pause.pause_port_group.xon_delta = 2000
 link_pause.pause_port_group.rx_enable = true
 link_pause.pause_port_group.tx_enable = true

# Specify cable length in mts
 link_pause.pause_port_group.cable_length = 10
```

{{%notice note%}}
This `link_pause.pause_port_group.port_buffer_bytes`, `link_pause.pause_port_group.xoff_size`, and `link_pause.pause_port_group.xon_delta` settings are optional. If not provided, the values are derived from the port speed, port MTU, or port cable length.
{{%/notice%}}

On Broadcom switches, after you modify the settings in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

{{<cl/restart-switchd>}}

On NVIDIA Spectrum switches, changes to the settings in the `/etc/cumulus/datapath/traffic.conf` file do *not* require you to restart `switchd`. However, you must run the `echo 1 > /cumulus/switchd/config/traffic/reload` command to apply the settings.

```
cumulus@switch:~$ echo 1 > /cumulus/switchd/config/traffic/reload
```

Always run the {{<link url="#syntax-checker" text="syntax checker">}} syntax checker before applying the configuration changes.

## Cut-through Mode and Store and Forward Switching

Cut-through mode is disabled in Cumulus Linux by default on switches with Broadcom ASICs. On NVIDIA Spectrum switches, you cannot disable cut-through mode.

```
# Cut-through is disabled by default on all chips with the exception of
# Spectrum.  On Spectrum cut-through cannot be disabled.
#cut_through_enable = false
```

If cut-though mode is enabled and link pause is asserted, Cumulus Linux generates a TOVR and TUFL ERROR; certain error counters increment on a given physical port.

```
cumulus@switch:~$ sudo ethtool -S swp49 | grep Error
HwIfInDot3LengthErrors: 0
HwIfInErrors: 0
HwIfInDot3FrameErrors: 0
SoftInErrors: 0
SoftInFrameErrors: 0
HwIfOutErrors: 35495749
SoftOutErrors: 0

cumulus@switch:~$ sudo ethtool -S swp50 | grep Error
HwIfInDot3LengthErrors: 3038098
HwIfInErrors: 297595762
HwIfInDot3FrameErrors: 293710518
```

To work around this issue, disable link pause by commenting out the `link_pause*` section in the `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
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
```

To enable store and forward switching, set `cut_through_enable` to *false* in the `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
cut_through_enable = false
```

On Broadcom switches, after you modify the settings in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command. Always run the {{<link url="#syntax-checker" text="syntax checker">}} syntax checker before applying the configuration changes.

{{<cl/restart-switchd>}}

{{%notice note%}}

On switches using Broadcom Tomahawk, Trident II, Trident II+, and Trident3 ASICs, Cumulus Linux supports store and forward switching but does **not** support cut-through mode.

On switches with the Mellanox Spectrum ASIC, Cumulus Linux supports cut-through mode but does **not** support store and forward switching.

{{%/notice%}}

## Congestion Notification

*Explicit Congestion Notification* (ECN) is defined by {{<exlink url="https://tools.ietf.org/html/rfc3168" text="RFC 3168">}}. ECN enables the Cumulus Linux switch to mark a packet to signal impending congestion instead of dropping the packet, which is how TCP typically behaves when ECN is not enabled.

ECN is a layer 3 end-to-end congestion notification mechanism only. Packets can be marked as *ECN-capable transport* (ECT) by the sending server. If congestion is observed by any switch while the packet is getting forwarded, the ECT-enabled packet can be marked by the switch to indicate the congestion. The end receiver can respond to the ECN-marked packets by signaling the sending server to slow down transmission. The sending server marks a packet *ECT* by setting the least two significant bits in an IP header `DiffServ` (ToS) field to *01* or *10*. A packet that has the least teo significant bits set to *00* indicates a non-ECT-enabled packet.

The ECN mechanism on a switch only marks packets to notify the end receiver. It does not take any other action or change packet handling in any way, nor does it respond to packets that have already been marked ECN by an upstream switch.

{{%notice note%}}

**On Trident II switches only**, if ECN is enabled on a specific queue, the ASIC also enables RED on the same queue. If the packet is ECT marked (the ECN bits are 01 or 10), the ECN mechanism executes as described above. However, if it is entering an ECN-enabled queue but is not ECT marked (the ECN bits are 00), then the RED mechanism uses the same threshold and probability values to decide whether to drop the packet. Packets entering a non-ECN-enabled queue do not get marked or dropped due to ECN or RED in any case.

{{%/notice%}}

ECN is implemented on the switch using minimum and maximum threshold values for the egress queue length. When a packet enters the queue and the average queue length is between the minimum and maximum threshold values, a configurable probability value will determine whether the packet is marked. If the average queue length is above the maximum threshold value, the packet is always marked.

The downstream switches with ECN enabled perform the same actions as the traffic is received. If the ECN bits are set, they remain set. The only way to overwrite ECN bits is to set the ECN bits to *11*.

ECN is supported on Broadcom Tomahawk, Tomahawk2, Trident II, Trident II+ and Trident3, and Mellanox Spectrum ASICs.

ECN is disabled by default in Cumulus Linux. You can enable ECN for individual switch priorities on specific switch ports in the `/etc/cumulus/datapath/traffic.conf` file:

- Specify the name of the port group in `ecn.port_group_list` in brackets; for example, `ecn.port_group_list = [ecn_port_group]`.
- Assign a CoS value to the port group in `ecn.ecn_port_group.cos_list`. If the CoS value of a packet matches the value of this setting, ECN is applied.
- Populate the port group with its member ports (`ecn.ecn_port_group.port_set`). Congestion is measured on the egress port queue for the ports listed here, using the average queue length: if congestion is present, a packet entering the queue can be marked to indicate that congestion was observed. Marking a packet involves setting the least 2 significant bits in the IP header DiffServ (ToS) field to *11*.
- The switch priority value(s) are mapped to specific egress queues for the target switch ports.
- The `ecn.ecn_port_group.probability` value indicates the probability of a packet being marked if congestion is experienced.

The following configuration example shows ECN configured for ports swp1 through swp4 and swp6:

```
# Explicit Congestion Notification
# to configure ECN and RED on a group of ports:
# -- add or replace port group names in the port group list
# -- assign cos value(s) to the cos list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
# -- to enable RED requires the latest traffic.conf
ecn_red.port_group_list = [ecn_red_port_group]
ecn_red.ecn_red_port_group.cos_list = [3]
ecn_red.ecn_red_port_group.port_set = swp1-swp4,swp6
ecn_red.ecn_red_port_group.ecn_enable = true
ecn_red.ecn_red_port_group.red_enable = false
ecn_red.ecn_red_port_group.min_threshold_bytes = 40000
ecn_red.ecn_red_port_group.max_threshold_bytes = 200000
ecn_red.ecn_red_port_group.probability = 100
```

On Broadcom switches, after you modify the settings in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

{{<cl/restart-switchd>}}

On NVIDIA Spectrum switches, changes to the settings in the `/etc/cumulus/datapath/traffic.conf` file do *not* require you to restart `switchd`. However, you must run the `echo 1 > /cumulus/switchd/config/traffic/reload` command to apply the settings.

```
cumulus@switch:~$ echo 1 > /cumulus/switchd/config/traffic/reload
```

Always run the {{<link url="#syntax-checker" text="syntax checker">}} syntax checker before applying the configuration changes.

## Scheduling Weights Per Egress Queue

On NVIDIA Spectrum switches, you can set the scheduling weight per egress queue, which determines the amount of bandwidth assigned to the queue. Cumulus Linux supports eight queues per port. You can either use a default profile that each port inherits​ or create separate profiles that map a different set of ports. Each profile, including the default profile, has weights configured for each egress queue (0-7)​​.

You set the weights per egress queue as a percentage. The total weight percentages for all egress queues cannot be greater than 100. If you do not define a weight for an egress queue, no scheduling is done for packets on this queue if congestion occurs. If you want to configure strict scheduling on an egress queue (always send every single packet in the queue) set the value to 0.

You can configure per queue egress scheduling with NCLU commands or manually by editing the `/etc/cumulus/datapath/traffic.conf` file.

Cumulus Linux provides a default profile. You can either enable the default profile or configure a non-default profile.

{{< tabs "TabID432 ">}}

{{< tab "NCLU Commands ">}}

The following example commands enable the default profile:

```
cumulus@switch:~$ net add qos egress-sched default_profile
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

In the default profile, the egress queue weights are set as follows. You cannot modify these values with NCLU.

```
...
default_egress_sched.egr_queue_0.bw_percent = 12
default_egress_sched.egr_queue_1.bw_percent = 12
default_egress_sched.egr_queue_2.bw_percent = 24
default_egress_sched.egr_queue_3.bw_percent = 12
default_egress_sched.egr_queue_4.bw_percent = 12
default_egress_sched.egr_queue_5.bw_percent = 12
default_egress_sched.egr_queue_6.bw_percent = 12
default_egress_sched.egr_queue_7.bw_percent = 0
```

The following commands create a non-default profile for port group `port_group1` for swp2 and swp3, set the weight to 30 percent on egress queue 2 and strict scheduling on egress queue 3:

```
cumulus@switch:~$ net add qos egress-sched profile port_set swp2-swp3
cumulus@switch:~$ net add qos egress_sched profile sched_port_group1 queue 2 dwrr bw_percent 30​
cumulus@switch:~$ net add qos egress_sched profile sched_port_group1 queue 3 strict
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The NCLU commands save the configuration in the `/etc/cumulus/datapath/traffic.conf` file. For example:

```
...
egress_sched.port_group_list = [sched_port_group1]
egress_sched.sched_port_group1.port_set = swp2-swp3
egress_sched.sched_port_group1.egr_queue_2.bw_percent = 30
egress_sched.sched_port_group1.egr_queue_3.bw_percent = 0
...
```

{{%notice note%}}
- To configure a non-default profile with NCLU, you must configure the port set for the profile before you configure the bandwidth percent for the egress queues.
- The total bandwidth percent for all egress queues cannot be greater than 100.
- If you delete the port set for a non-default profile, the bandwidth percent for all the queues in that profile are deleted.
{{%/notice%}}

{{< /tab >}}

{{< tab "Edit the traffic.conf File ">}}

To configure per queue egress scheduling manually in the `/etc/cumulus/datapath/traffic.conf` file, update and uncomment the settings in the `default egress scheduling weight per egress queue` section of the `/etc/cumulus/datapath/traffic.conf` file.

The following example enables the default profile, and sets the weight to 30 percent for egress queue 2 and 10 percent for the remaining egress queues. The settings are applied to all ports.

```
# default egress scheduling weight per egress queue 
# To be applied to all the ports if port_group profile not configured
# If you do not specify any bw_percent of egress_queues, those egress queues 
# will assume DWRR weight 0 - no egress scheduling for those queues
# '0' indicates strict priority
default_egress_sched.egr_queue_0.bw_percent = 10
default_egress_sched.egr_queue_1.bw_percent = 10
default_egress_sched.egr_queue_2.bw_percent = 30
default_egress_sched.egr_queue_3.bw_percent = 10
default_egress_sched.egr_queue_4.bw_percent = 10
default_egress_sched.egr_queue_5.bw_percent = 10
default_egress_sched.egr_queue_6.bw_percent = 10
default_egress_sched.egr_queue_7.bw_percent = 10
```

The following example creates a non-default profile for port group `port_group1`, sets the weight to 30 percent for egress queue 1 and 2, to 0 for egress queue 6 and 7 (always send every single packet from egress queue 6 and 7 before any other queue), and 10 percent for the remaining egress queues:

```
...
egress_sched.port_group_list = [sched_port_group1]
egress_sched.sched_port_group1.port_set = swp2
egress_sched.sched_port_group1.egr_queue_0.bw_percent = 10
egress_sched.sched_port_group1.egr_queue_1.bw_percent = 30
egress_sched.sched_port_group1.egr_queue_2.bw_percent = 30
egress_sched.sched_port_group1.egr_queue_3.bw_percent = 10
egress_sched.sched_port_group1.egr_queue_4.bw_percent = 10
egress_sched.sched_port_group1.egr_queue_5.bw_percent = 10
egress_sched.sched_port_group1.egr_queue_6.bw_percent = 0
egress_sched.sched_port_group1.egr_queue_7.bw_percent = 0
```

On Broadcom switches, after you modify the settings in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

{{<cl/restart-switchd>}}

On NVIDIA Spectrum switches, changes to the settings in the `/etc/cumulus/datapath/traffic.conf` file do *not* require you to restart `switchd`. However, you must run the `echo 1 > /cumulus/switchd/config/traffic/reload` command to apply the settings.

```
cumulus@switch:~$ echo 1 > /cumulus/switchd/config/traffic/reload
```

Always run the {{<link url="#syntax-checker" text="syntax checker">}} syntax checker before applying the configuration changes.

{{< /tab >}}

{{< /tabs >}}

## Traffic Shaping

Configure traffic shaping to regulate network traffic by using a lower bitrate than the physical interface is capable of. Traffic shaping prevents packets from being dropped or lost due to bandwidth limits or congestion.

To configure traffic shaping, update and uncomment the settings in the `Hierarchical traffic shaping` section of the the `/etc/cumulus/datapath/traffic.conf` file. You can configure traffic shaping per egress queue or aggregated at the port level.

The egress shaping rate configured in the `/etc/cumulus/datapath/traffic.conf` is always the layer 1 rate. The calculated shaping rate considers overheads in the Ethernet frame like the interframe gap, preamble, cyclic redundancy check (CRC) and so on. The egress layer 3 throughput measured is always less than the maximum shaper rate configured.

The following example shows the `Hierarchical traffic shaping` section of the `/etc/cumulus/datapath/traffic.conf` file.

```
...
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
shaping.port_group_list = [shaper_port_group]
shaping.shaper_port_group.port_set = swp1-swp3
shaping.shaper_port_group.egr_queue_0.shaper = [50000, 100000]
shaping.shaper_port_group.egr_queue_1.shaper = [51000, 150000]
shaping.shaper_port_group.egr_queue_2.shaper = [52000, 200000]
shaping.shaper_port_group.egr_queue_3.shaper = [53000, 250000]
shaping.shaper_port_group.egr_queue_4.shaper = [54000, 300000]
shaping.shaper_port_group.egr_queue_5.shaper = [55000, 350000]
shaping.shaper_port_group.egr_queue_6.shaper = [56000, 400000]
shaping.shaper_port_group.egr_queue_7.shaper = [57000, 450000]
# shaping.shaper_port_group.port.shaper = 900000
```

The settings are described below:

| Traffic Shaping Setting | Description|
| ------------------------| ---------- |
| `shaping.port_group_list` | The name of the port group. You must enclose the name in square brackets; for example, `shaping.port_group_list = [shaper_port_group1]`. |
| `shaping.shaper_port_group.port_set` | The list of ports in the port group. |
| `shaping.shaper_port_group.egr_queue_0.shaper` | The minimum and maximum rates in kbps for egress queue 0. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_1.shaper` | The minimum and maximum rates in kbps for egress queue 1. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_2.shaper` | The minimum and maximum rates in kbps for egress queue 2. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_3.shaper` | The minimum and maximum rates in kbps for egress queue 3. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_4.shaper` | The minimum and maximum rates in kbps for egress queue 4. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_5.shaper` | The minimum and maximum rates in kbps for egress queue 5. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_6.shaper` | The minimum and maximum rates in kbps for egress queue 6. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.egr_queue_7.shaper` | The minimum and maximum rates in kbps for egress queue 7. You must enclose the values in square brackets. |
| `shaping.shaper_port_group.port.shaper` |  The maximum rate in kbps at the port level.<br>At the port level, only the maximum shaper rate is supported. |
| `scheduling.algorithm` | Cumulus Linux supports the Deficit Weighted Round Robin (DWRR) scheduling algorithm only. |

{{%notice note%}}
In Cumulus Linux, the burst size is set to twice the maximum rate internally; the setting is not configurable.
{{%/notice%}}

On Broadcom switches, when you modify the configuration in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

{{<cl/restart-switchd>}}

On Broadcom switches, after you modify the settings in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

{{<cl/restart-switchd>}}

On NVIDIA Spectrum switches, changes to the settings in the `/etc/cumulus/datapath/traffic.conf` file do *not* require you to restart `switchd`. However, you must run the `echo 1 > /cumulus/switchd/config/traffic/reload` command to apply the settings.

```
cumulus@switch:~$ echo 1 > /cumulus/switchd/config/traffic/reload
```

Always run the {{<link url="#syntax-checker" text="syntax checker">}} syntax checker before applying the configuration changes.

## Interface Buffer Status

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="ASICs">}}, you can collect a fine-grained history of queue lengths using histograms maintained by the ASIC; see the {{<link title="ASIC Monitoring">}} for details.

## Example Configuration File

The following example `/etc/cumulus/datapath/traffic.conf` datapath configuration file applies to 10G, 40G, and 100G switches on Broadcom Tomahawk, Trident II, Trident II+, or Trident3 and Mellanox Spectrum platforms only.

- For the default source packet fields and mapping, each selected packet field must have a block of mapped values. Any packet field value that is not specified in the configuration is assigned to a default internal switch priority. The configuration applies to every forwarding port unless a custom remark configuration is defined for that port (see below).
- For the default remark packet fields and mapping, each selected packet field should have a block of mapped values. Any internal switch priority value that is not specified in the configuration is assigned to a default packet field value. The configuration applies to every forwarding port unless a custom remark configuration is defined for that port (see below).
- Per-port source packet fields and mapping apply to the designated set of ports.
- Per-port remark packet fields and mapping apply to the designated set of ports.

{{< expand "Click to see the traffic.conf file"  >}}

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
#
# /etc/cumulus/datapath/traffic.conf
# Copyright 2014, 2015, 2016, 2017, 2020 Cumulus Networks, Inc.  All rights reserved.
#

# packet header field used to determine the packet priority level
# fields include {802.1p, dscp}
traffic.packet_priority_source_set = [802.1p]

# packet priority source values assigned to each internal cos value
# internal cos values {cos_0..cos_7}
# (internal cos 3 has been reserved for CPU-generated traffic)
#
# 802.1p values = {0..7}
traffic.cos_0.priority_source.8021p = [0]
traffic.cos_1.priority_source.8021p = [1]
traffic.cos_2.priority_source.8021p = [2]
traffic.cos_3.priority_source.8021p = []
traffic.cos_4.priority_source.8021p = [3,4]
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

# priority groups
traffic.priority_group_list = [control, service, bulk]

# internal cos values assigned to each priority group
# each cos value should be assigned exactly once
# internal cos values {0..7}
priority_group.control.cos_list = [7]
priority_group.service.cos_list = [2]
priority_group.bulk.cos_list = [0,1,3,4,5,6]

# Alias Name defined for each priority group
# Valid string between 0-255 chars
# Sample alias support for naming priority groups
#priority_group.control.alias = "Control"
#priority_group.service.alias = "Service"
#priority_group.bulk.alias = "Bulk"

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
# pfc.port_group_list = [pfc_port_group]
# pfc.pfc_port_group.cos_list = []
# pfc.pfc_port_group.port_set = swp1-swp4,swp6
# pfc.pfc_port_group.port_buffer_bytes = 25000
# pfc.pfc_port_group.xoff_size = 10000
# pfc.pfc_port_group.xon_delta = 2000
# pfc.pfc_port_group.tx_enable = true
# pfc.pfc_port_group.rx_enable = true
#
# Specify cable length in mts
# pfc.pfc_port_group.cable_length = 10

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
# -- to enable RED requires the latest traffic.conf
# ecn_red.port_group_list = [ecn_red_port_group]
# ecn_red.ecn_red_port_group.cos_list = []
# ecn_red.ecn_red_port_group.port_set = swp1-swp4,swp6
# ecn_red.ecn_red_port_group.ecn_enable = true
# ecn_red.ecn_red_port_group.red_enable = false
# ecn_red.ecn_red_port_group.min_threshold_bytes = 40000
# ecn_red.ecn_red_port_group.max_threshold_bytes = 200000
# ecn_red.ecn_red_port_group.probability = 100

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

# scheduling algorithm: algorithm values = {dwrr}
scheduling.algorithm = dwrr

# traffic group scheduling weight
# weight values = {0..127}
# '0' indicates strict priority
priority_group.control.weight = 0
priority_group.service.weight = 32
priority_group.bulk.weight = 16

# default egress scheduling weight per egress queue 
# To be applied to all the ports if port_group profile not configured
# If you do not specify any bw_percent of egress_queues, those egress queues 
# will assume DWRR weight 0 - no egress scheduling for those queues
# '0' indicates strict priority
#default_egress_sched.egr_queue_0.bw_percent = 12
#default_egress_sched.egr_queue_1.bw_percent = 12
#default_egress_sched.egr_queue_2.bw_percent = 24
#default_egress_sched.egr_queue_3.bw_percent = 12
#default_egress_sched.egr_queue_4.bw_percent = 12
#default_egress_sched.egr_queue_5.bw_percent = 12
#default_egress_sched.egr_queue_6.bw_percent = 12
#default_egress_sched.egr_queue_7.bw_percent = 0

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

# To turn on/off Denial of service (DOS) prevention checks
dos_enable = false

# Cut-through is disabled by default on all chips with the exception of
# Spectrum.  On Spectrum cut-through cannot be disabled.
#cut_through_enable = false

# Enable resilient hashing
#resilient_hash_enable = FALSE

# Resilient hashing flowset entries per ECMP group
# Valid values - 64, 128, 256, 512, 1024
#resilient_hash_entries_ecmp = 128

# Enable symmetric hashing
#symmetric_hash_enable = TRUE

# Set sflow/sample ingress cpu packet rate and burst in packets/sec
# Values: {0..16384}
#sflow.rate = 16384
#sflow.burst = 16384

#Specify the maximum number of paths per route entry.
#  Maximum paths supported is 200.
#  Default value 0 takes the number of physical ports as the max path size.
#ecmp_max_paths = 0

#Specify the hash seed for Equal cost multipath entries
# and for cutom ecmp and lag hash
# Default value : random
# Value Rang: {0..4294967295}
#ecmp_hash_seed = 42

# HASH config for  ECMP to enable custom fields
# Fields will be applicable for ECMP hash
# calculation
#Note : Currently supported only for MLX platform
# Uncomment to enable custom fields configured below
#hash_config.enable = true

#hash Fields available ( assign true to enable)
#ip protocol
hash_config.ip_prot = true
#source ip
hash_config.sip = true
#destination ip
hash_config.dip = true
#source port
hash_config.sport = true
#destination port
hash_config.dport = true
#ipv6 flow label
hash_config.ip6_label = true
#ingress interface
hash_config.ing_intf = false

#inner fields for  IPv4-over-IPv6 and IPv6-over-IPv6
hash_config.inner_ip_prot = false
hash_config.inner_sip = false
hash_config.inner_dip = false
hash_config.inner_sport = false
hash_config.inner_dport = false
hash_config.inner_ip6_label = false
# Hash config end #


#LAG HASH config
#HASH config for LACP to enable custom fields
#Fields will be applicable for LAG hash
#calculation
#Uncomment to enable custom fields configured below
#lag_hash_config.enable = true

lag_hash_config.smac = true
lag_hash_config.dmac = true
lag_hash_config.sip  = true
lag_hash_config.dip  = true
lag_hash_config.ether_type = true
lag_hash_config.vlan_id = true
lag_hash_config.sport = true
lag_hash_config.dport = true
lag_hash_config.ip_prot = true

# Specify the forwarding table resource allocation profile, applicable
# only on platforms that support universal forwarding resources.
#
# /usr/cumulus/sbin/cl-resource-query reports the allocated table sizes
# based on the profile setting.
#
#   Values: one of { *** Common ***
#                   'default', 'l2-heavy', 'v4-lpm-heavy', 'v6-lpm-heavy',
#                   'ipmc-heavy',
#
#                   *** Mellanox only platforms ***
#                   'l2-heavy-1', 'l2-heavy-2', 'v4-lpm-heavy-1',
#                   'rash-v4-lpm-heavy', 'rash-custom-profile1',
#                   'rash-custom-profile2', 'lpm-balanced',
#
#                   *** Broadcom[XGS] only platforms ***
#                   'mode-0', 'mode-1', 'mode-2', 'mode-3', 'mode-4',
#                   'mode-5', 'mode-6', 'mode-7', 'mode-8'
#                   }
#
#   Default value: 'default'
#   Notes: some devices may support more modes, please consult user
#          guide for more details
#
forwarding_table.profile = default
```

{{< /expand >}}

{{%notice note%}}

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, you must enable packet priority remark on the **ingress** port. A packet received on a remark-enabled port is remarked according to the priority mapping configured on the **egress** port. If you configure packet priority remark the same way on every port, the default configuration example above is correct. However, per-port customized configurations require two port groups, one for the ingress ports and one for the egress ports, as below:

```
remark.port_group_list = [ingress_remark_group, egress_remark_group]
remark.ingress_remark_group.packet_priority_remark_set = [dscp]
remark.remark_port_group.port_set = swp1-swp4,swp6
remark.egress_remark_group.port_set = swp10-swp20
remark.egress_remark_group.cos_0.priority_remark.dscp = [2]
remark.egress_remark_group.cos_1.priority_remark.dscp = [10]
remark.egress_remark_group.cos_2.priority_remark.dscp = [18]
remark.egress_remark_group.cos_3.priority_remark.dscp = [26]
remark.egress_remark_group.cos_4.priority_remark.dscp = [34]
remark.egress_remark_group.cos_5.priority_remark.dscp = [42]
remark.egress_remark_group.cos_6.priority_remark.dscp = [50]
remark.egress_remark_group.cos_7.priority_remark.dscp = [58]
```

{{%/notice%}}

## Syntax Checker

Cumulus Linux provides a syntax checker for the `/etc/cumulus/datapath/traffic.conf` file to check for errors, such missing parameters, or invalid parameter labels and values.

On Broadcom switches, the syntax checker runs automatically during `switchd` initialization and reports syntax errors to the `/var/log/switchd.log` file.

On both Broadcom and NVIDIA switches, you can run the syntax checker manually from the command line by issuing the `cl-consistency-check --datapath-syntax-check` command. If errors exist, they are written to `stderr` by default. If you run the command with `-q`, errors are written to the `/var/log/switchd.log` file.

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

## Related Information

- {{<exlink url="http://ipset.netfilter.org/iptables-extensions.man.html" text="iptables-extensions man page">}}
