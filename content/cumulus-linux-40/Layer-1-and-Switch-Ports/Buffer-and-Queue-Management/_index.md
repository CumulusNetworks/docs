---
title: Buffer and Queue Management
author: NVIDIA
weight: 320
toc: 3
---
Hardware datapath configuration manages packet buffering, queueing and scheduling in hardware. To configure priority groups, and assign the scheduling alogorithm and weights, you edit the `/etc/cumulus/datapath/traffic.conf`.

{{%notice note%}}

The `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/[bcm|mlx]/datapath.conf` assigns buffer space and egress queues. The default thresholds defined in the `datapath.conf` file are intended for data center environments, but certain workloads may require additional tuning. It is best to make small, incremental changes to validate the changes with your application performance. Be sure to backup the original file before making changes.

{{%/notice%}}

Each packet is assigned to an ASIC Class of Service (CoS) value based on the priority value of the packet stored in the 802.1p (Class of Service) or DSCP (Differentiated Services Code Point) header field. The choice to schedule packets based on COS or DSCP is a configurable option in the `/etc/cumulus/datapath/traffic.conf` file.

Priority groups include:

- *Control*: Highest priority traffic
- *Service*: Second-highest priority traffic
- *Bulk*: All remaining traffic

The scheduler is configured to use a hybrid scheduling algorithm. It applies strict priority to control traffic queues and a weighted round robin selection from the remaining queues. Unicast packets and multicast packets with the same priority value are assigned to separate queues, which are assigned equal scheduling weights.

{{%notice note%}}

You can configure Quality of Service (QoS) for switches on the following platforms only:

- Broadcom Tomahawk, Trident II, Trident II+ and Trident3
- Mellanox Spectrum and Spectrum-2

{{%/notice%}}

## Example Configuration File

The following example `/etc/cumulus/datapath/traffic.conf` datapath configuration file applies to 10G, 40G, and 100G switches on Broadcom Tomahawk, Trident II, Trident II+, or Trident3 and Mellanox Spectrum platforms only.

- For the default source packet fields and mapping, each selected packet field must have a block of mapped values. Any packet field value that is not specified in the configuration is assigned to a default internal switch priority. The configuration applies to every forwarding port unless a custom remark configuration is defined for that port (see below).
- For the default remark packet fields and mapping, each selected packet field should have a block of mapped values. Any internal switch priority value that is not specified in the configuration is assigned to a default packet field value. The configuration applies to every forwarding port unless a custom remark configuration is defined for that port (see below).
- Per-port source packet fields and mapping apply to the designated set of ports.
- Per-port remark packet fields and mapping apply to the designated set of ports.

{{< expand "click to see traffic.conf file"  >}}

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
#
# /etc/cumulus/datapath/traffic.conf
#

# packet header field used to determine the packet priority level
# fields include {802.1p, dscp}
traffic.packet_priority_source_set = [802.1p,dscp]

# remark packet priority value
# fields include {802.1p, none}
# remark packet priority value
# fields include {802.1p, dscp}
traffic.packet_priority_remark_set = [802.1p,dscp]

# packet priority remark values assigned from each internal cos value
# internal cos values {cos_0..cos_7}
# (internal cos 3 has been reserved for CPU-generated traffic)
#
# 802.1p values = {0..7}

traffic.cos_0.priority_remark.8021p = [1]
traffic.cos_1.priority_remark.8021p = [0]
traffic.cos_2.priority_remark.8021p = [3]
traffic.cos_3.priority_remark.8021p = [2]
traffic.cos_4.priority_remark.8021p = [4]
traffic.cos_5.priority_remark.8021p = [5]
traffic.cos_6.priority_remark.8021p = [7]
traffic.cos_7.priority_remark.8021p = [6]

# dscp values = {0..63}
traffic.cos_0.priority_remark.dscp = [1]
traffic.cos_1.priority_remark.dscp = [9]
traffic.cos_2.priority_remark.dscp = [17]
traffic.cos_3.priority_remark.dscp = [25]
traffic.cos_4.priority_remark.dscp = [33]
traffic.cos_5.priority_remark.dscp = [41]
traffic.cos_6.priority_remark.dscp = [49]
traffic.cos_7.priority_remark.dscp = [57]

# Per-port remark packet fields and mapping: applies to the designated set of ports.
remark.port_group_list = [remark_port_group]
remark.remark_port_group.packet_priority_remark_set = [802.1p,dscp]
remark.remark_port_group.port_set = swp1-swp4,swp6
remark.remark_port_group.cos_0.priority_remark.dscp = [2]
remark.remark_port_group.cos_1.priority_remark.dscp = [10]
remark.remark_port_group.cos_2.priority_remark.dscp = [18]
remark.remark_port_group.cos_3.priority_remark.dscp = [26]
remark.remark_port_group.cos_4.priority_remark.dscp = [34]
remark.remark_port_group.cos_5.priority_remark.dscp = [42]
remark.remark_port_group.cos_6.priority_remark.dscp = [50]
remark.remark_port_group.cos_7.priority_remark.dscp = [58]

# packet priority values assigned to each internal cos value
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
traffic.cos_0.priority_source.dscp = [0,1,2,3,4,5,6,7]
traffic.cos_1.priority_source.dscp = [8,9,10,11,12,13,14,15]
traffic.cos_2.priority_source.dscp = []
traffic.cos_3.priority_source.dscp = []
traffic.cos_4.priority_source.dscp = []
traffic.cos_5.priority_source.dscp = []
traffic.cos_6.priority_source.dscp = []
traffic.cos_7.priority_source.dscp = [56,57,58,59,60,61,62,63]

# Per-port source packet fields and mapping: applies to the designated set of ports.
source.port_group_list = [source_port_group]
source.source_port_group.packet_priority_source_set = [802.1p,dscp]
source.source_port_group.port_set = swp1-swp4,swp6
source.source_port_group.cos_0.priority_source.8021p = [7]
source.source_port_group.cos_1.priority_source.8021p = [6]
source.source_port_group.cos_2.priority_source.8021p = [5]
source.source_port_group.cos_3.priority_source.8021p = [4]
source.source_port_group.cos_4.priority_source.8021p = [3]
source.source_port_group.cos_5.priority_source.8021p = [2]
source.source_port_group.cos_6.priority_source.8021p = [1]
source.source_port_group.cos_7.priority_source.8021p = [0]

# priority groups
traffic.priority_group_list = [control, service, bulk]

# internal cos values assigned to each priority group
# each cos value should be assigned exactly once
# internal cos values {0..7}
priority_group.control.cos_list = [7]
priority_group.service.cos_list = [2]
priority_group.bulk.cos_list = [0,1,3,4,5,6]

# to configure priority flow control on a group of ports:
# -- assign cos value(s) to the cos list
# -- add or replace a port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a PFC buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers PFC frame transmit to start)
#    -- set the xon byte delta (buffer limit that triggers PFC frame transmit to stop)
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

# to configure pause on a group of ports:
# -- add or replace port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a pause buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers pause frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers pause frames transmit to stop)

# link pause
# link_pause.port_group_list = [pause_port_group]
# link_pause.pause_port_group.port_set = swp1-swp4,swp6
# link_pause.pause_port_group.port_buffer_bytes = 25000
# link_pause.pause_port_group.xoff_size = 10000
# link_pause.pause_port_group.xon_delta = 2000
# link_pause.pause_port_group.rx_enable = true
# link_pause.pause_port_group.tx_enable = true

# scheduling algorithm: algorithm values = {dwrr}
scheduling.algorithm = dwrr

# traffic group scheduling weight
# weight values = {0..127}
# '0' indicates strict priority
priority_group.control.weight = 0
priority_group.service.weight = 32
priority_group.bulk.weight = 16

# To turn on/off Denial of service (DOS) prevention checks
dos_enable = false

# Cut-through is disabled by default on all chips with the exception of
# Spectrum. On Spectrum cut-through cannot be disabled.
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
# Default value 0
# Value Rang: {0..4294967295}
#ecmp_hash_seed = 42

# Specify the forwarding table resource allocation profile, applicable
# only on platforms that support universal forwarding resources.
#
# /usr/cumulus/sbin/cl-rsource-query reports the allocated table sizes
# based on the profile setting.
#
#   Values: one of {'default', 'l2-heavy', 'v4-lpm-heavy', 'v6-lpm-heavy'}
#   Default value: 'default'
#   Note: some devices may support more modes, please consult user
#         guide for more details
#
#forwarding_table.profile = default
```

{{< /expand >}}

{{%notice note%}}

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, you must enable packet priority remark on the **ingress** port. A packet received on a remark-enabled port is remarked according to the priority mapping configured on the **egress** port. If you configure packet priority remark the same way on every port, the default configuration example above is correct. However, per-port customized configurations require two port groups: one for the ingress ports and one for the egress ports, as below:

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

On Broadcom switches, if you modify the configuration in the `/etc/cumulus/datapath/traffic.conf` file, you *must* restart `switchd` for the changes to take effect; run the `cumulus@switch:~$ sudo systemctl restart switchd.service` command.

On Mellanox switches with the Spectrum ASIC, the following options in the `/etc/cumulus/datapath/traffic.conf` file do *not* require you to restart `switchd`. However, you must run the `echo 1 > /cumulus/switchd/config/traffic/reload` command after you change the options.

- DSCP/802.1p to COS remark assignments (`traffic.*`)
- Explicit congestion notification (ECN) settings (`ecn_red.*`)
- Priority flow control (PFC) settings (`pfc.*`)
- Link Pause settings (`link_pause.*`)
- Queue weight settings (`priority_group.*.weight`)

## Configure Traffic Marking through ACL Rules

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

The PFC mechanism can be enabled for individual switch priorities on specific switch ports for RX and/or TX traffic. The switch port's ingress buffer occupancy is used to measure congestion. If congestion is present, the switch transmits flow control frames to the upstream switch. Packets with priority values that do not have PFC configured are not counted during congestion detection; neither do they get throttled by the upstream switch when it receives flow control frames.

PFC congestion detection is implemented on the switch using xoff and xon threshold values for the specific ingress buffer which is used by the targeted switch priorities. When a packet enters the buffer and the buffer occupancy is above the xoff threshold, the switch transmits an Ethernet PFC frame to the upstream switch to signal packet transmission should stop. When the buffer occupancy drops below the xon threshold, the switch sends another PFC frame upstream to signal that packet transmission can resume. (PFC frames contain a quanta value to indicate a timeout value for the upstream switch: packet transmission can resume after the timer has expired, or when a PFC frame with quanta == 0 is received from the downstream switch.)

After the downstream switch has sent a PFC frame upstream, it continues to receive packets until the upstream switch receives and responds to the PFC frame. The downstream ingress buffer must be large enough to store those additional packets after the xoff threshold has been reached.

Priority flow control is fully supported on both {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Broadcom">}} and {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Mellanox">}} switches.

PFC is disabled by default in Cumulus Linux. To enable priority flow control (PFC), you must configure the following settings in the `/etc/cumulus/datapath/traffic.conf` file on the switch:

- Specify the name of the port group in `pfc.port_group_list` in brackets; for example, *pfc.port\_group\_list = \[pfc\_port\_group\]*.
- Assign a CoS value to the port group in `pfc.pfc_port_group.cos_list` setting. *pfc\_port\_group* is the name of a port group you specified above and is used throughout the following settings.
- Populate the port group with its member ports in `pfc.pfc_port_group.port_set`.
- Set a PFC buffer size in `pfc.pfc_port_group.port_buffer_bytes`. This is the maximum number of bytes allocated for storing bursts of packets, guaranteed at the ingress port. The default is *25000* bytes.
- Set the xoff byte limit in `pfc.pfc_port_group.xoff_size`. This is a threshold for the PFC buffer; when this limit is reached, an xoff transition is initiated, signaling the upstream port to stop sending traffic, during which time packets continue to arrive due to the latency of the communication. The default is *10000* bytes.
- Set the xon delta limit in `pfc.pfc_port_group.xon_delta`. This is the number of bytes to subtract from the xoff limit, which results in a second threshold at which the egress port resumes sending traffic. After the xoff limit is reached and the upstream port stops sending traffic, the buffer begins to drain. When the buffer reaches 8000 bytes (assuming default xoff and xon settings), the egress port signals that it can start receiving traffic again. The default is *2000* bytes.
- Enable the egress port to signal the upstream port to stop sending traffic (`pfc.pfc_port_group.tx_enable`). The default is *true*.
- Enable the egress port to receive notifications and act on them (`pfc.pfc_port_group.rx_enable`). The default is *true*.
- The switch priority value(s) are mapped to the specific ingress buffer for each targeted switch port. Cumulus Linux looks at either the 802.1p bits or the IP layer DSCP bits depending on which is configured in the `traffic.conf` file to map packets to internal switch priority values.

The following configuration example shows PFC configured for ports swp1 through swp4 and swp6:

```
# to configure priority flow control on a group of ports:
# -- assign cos value(s) to the cos list
# -- add or replace a port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a PFC buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers PFC frame transmit to start)
#    -- set the xon byte delta (buffer limit that triggers PFC frame transmit to stop)
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
```

## Port Groups

A *port group* refers to one or more sequences of contiguous ports. You can define multiple port groups by adding:

- A comma-separated list of port group names to the port\_group\_list.
- The port\_set, rx\_enable, and tx\_enable configuration lines for each port group.

You can specify the set of ports in a port group in comma-separate sequences of contiguous ports; you can see which ports are contiguous in the `/var/lib/cumulus/porttab` file. The syntax supports:

- A single port (swp1s0 or swp5)
- A sequence of regular swp ports (swp2-swp5)
- A sequence within a breakout swp port (swp6s0-swp6s3)
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

On a Broadcom switch, restart `switchd` with the `sudo systemctl restart switchd.service` command to allow the PFC configuration changes to take effect. On a Mellanox switch with the Spectrum ASIC, restarting `switchd` is not necessary.

## Link Pause

The PAUSE frame is a flow control mechanism that halts the transmission of the transmitter for a specified period of time. A server or other network node within the data center may be receiving traffic faster than it can handle it, thus the PAUSE frame. In Cumulus Linux, you can configure individual ports to execute link pause by:

- Transmitting pause frames when its ingress buffers become congested (TX pause enable)
- Responding to received pause frames (RX pause enable).

Link pause is disabled by default. To enabling link pause, you must configure settings in the `/etc/cumulus/datapath traffic.conf` file.

{{%notice tip%}}

What's the difference between link pause and priority flow control?

- Priority flow control is applied to an individual priority group for a specific ingress port.
- Link pause (also known as port pause or global pause) is applied to all the traffic for a specific ingress port.

{{%/notice%}}

Here is an example configuration that enables both types of link pause for swp1 through swp4 and swp6:

``` 
# to configure pause on a group of ports:
# -- add or replace port group names in the port group list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
#    -- set a pause buffer size in bytes for each port in the group
#    -- set the xoff byte limit (buffer limit that triggers pause frames transmit to start)
#    -- set the xon byte delta (buffer limit that triggers pause frames transmit to stop)

# link pause
link_pause.port_group_list = [pause_port_group]
link_pause.pause_port_group.port_set = swp1-swp4,swp6
link_pause.pause_port_group.port_buffer_bytes = 25000
link_pause.pause_port_group.xoff_size = 10000
link_pause.pause_port_group.xon_delta = 2000
link_pause.pause_port_group.rx_enable = true
link_pause.pause_port_group.tx_enable = true
```

On a Broadcom switch, restart `switchd` with the `sudo systemctl restart switchd.service` command to allow the PFC configuration changes to take effect. On a Mellanox switch with the Spectrum ASIC, restarting `switchd` is not necessary.

## Cut-through Mode and Store and Forward Switching

Cut-through mode is disabled in Cumulus Linux by default on switches with Broadcom ASICs. With cut-though mode enabled and link pause is asserted, Cumulus Linux generates a TOVR and TUFL ERROR; certain error counters increment on a given physical port.

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

To work around this issue, disable link pause or disable cut-through mode in the `/etc/cumulus/datapath/traffic.conf` file.

To disable link pause, comment out the `link_pause*` section in the `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf 
#link_pause.port_group_list = [port_group_0]
#link_pause.port_group_0.port_set = swp45-swp54
#link_pause.port_group_0.rx_enable = true
#link_pause.port_group_0.tx_enable = true
```

To enable store and forward switching, set `cut_through_enable` to *false* in the `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo nano /etc/cumulus/datapath/traffic.conf
cut_through_enable = false
```

{{%notice note%}}

On switches using Broadcom Tomahawk, Trident II, Trident II+, and Trident3 ASICs, Cumulus Linux supports store and forward switching but does **not** support cut-through mode.

On switches with the Mellanox Spectrum ASIC, Cumulus Linux supports cut-through mode but does **not** support store and forward switching.

{{%/notice%}}

## Congestion Notification

*Explicit Congestion Notification* (ECN) is defined by {{<exlink url="https://tools.ietf.org/html/rfc3168" text="RFC 3168">}}. ECN enables the Cumulus Linux switch to mark a packet to signal impending congestion instead of dropping the packet, which is how TCP typically behaves when ECN is not enabled.

ECN is a layer 3 end-to-end congestion notification mechanism only. Packets can be marked as *ECN-capable transport* (ECT) by the sending server. If congestion is observed by any switch while the packet is getting forwarded, the ECT-enabled packet can be marked by the switch to indicate the congestion. The end receiver can respond to the ECN-marked packets by signaling the sending server to slow down transmission. The sending server marks a packet *ECT* by setting the least 2 significant bits in an IP header `DiffServ` (ToS) field to *01* or *10*. A packet that has the least 2 significant bits set to *00* indicates a non-ECT-enabled packet.

The ECN mechanism on a switch only marks packets to notify the end receiver. It does not take any other action or change packet handling in any way, nor does it respond to packets that have already been marked ECN by an upstream switch.

{{%notice note%}}

**On Trident II switches only**, if ECN is enabled on a specific queue, the ASIC also enables RED on the same queue. If the packet is ECT marked (the ECN bits are 01 or 10), the ECN mechanism executes as described above. However, if it is entering an ECN-enabled queue but is not ECT marked (the ECN bits are 00), then the RED mechanism uses the same threshold and probability values to decide whether to drop the packet. Packets entering a non-ECN-enabled queue do not get marked or dropped due to ECN or RED in any case.

{{%/notice%}}

ECN is implemented on the switch using minimum and maximum threshold values for the egress queue length. When a packet enters the queue and the average queue length is between the minimum and maximum threshold values, a configurable probability value will determine whether the packet will be marked. If the average queue length is above the maximum threshold value, the packet is always marked.

The downstream switches with ECN enabled perform the same actions as the traffic is received. If the ECN bits are set, they remain set. The only way to overwrite ECN bits is to set the ECN bits to *11*.

ECN is supported on Broadcom Tomahawk, Tomahawk2, Trident II, Trident II+ and Trident3, and Mellanox Spectrum ASICs.

{{< expand "Click to learn how to configure ECN "  >}}

ECN is disabled by default in Cumulus Linux. You can enable ECN for individual switch priorities on specific switch ports in the `/etc/cumulus/datapath/traffic.conf` file:

- Specify the name of the port group in `ecn.port_group_list` in brackets; for example, `ecn.port_group_list = [ecn_port_group]`.
- Assign a CoS value to the port group in `ecn.ecn_port_group.cos_list`. If the CoS value of a packet matches the value of this setting, then ECN is applied. Note that *ecn\_port\_group* is the name of a port group you specified above.
- Populate the port group with its member ports (`ecn.ecn_port_group.port_set`), where *ecn\_port\_group* is the name of the port group you specified above. Congestion is measured on the egress port queue for the ports listed here, using the average queue length: if congestion is present, a packet entering the queue may be marked to indicate that congestion was observed. Marking a packet involves setting the least 2 significant bits in the IP header DiffServ (ToS) field to *11*.
- The switch priority value(s) are mapped to specific egress queues for the target switch ports.
- The `ecn.ecn_port_group.probability` value indicates the probability of a packet being marked if congestion is experienced.

The following configuration example shows ECN configured for ports swp1 through swp4 and swp6:

```
# Explicit Congestion Notification
# to configure ECN on a group of ports:
# -- add or replace port group names in the port group list
# -- assign cos value(s) to the cos list  *ECN will only be applied to traffic matching this COS*
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
  ecn.port_group_list = [ecn_port_group]
  ecn.ecn_port_group.cos_list = [0]
  ecn.ecn_port_group.port_set = swp1-swp4,swp6
  ecn.ecn_port_group.min_threshold_bytes = 40000
  ecn.ecn_port_group.max_threshold_bytes = 200000
  ecn.ecn_port_group.probability = 100
```

On a Broadcom switch, restart `switchd` with the `sudo systemctl restart switchd.service` command to allow the PFC configuration changes to take effect. On a Mellanox switch with the Spectrum ASIC, restarting `switchd` is not necessary.

{{< /expand >}}

## Check Interface Buffer Status

- On switches with 
{{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="ASICs">}}, you can collect a fine-grained history of queue lengths using histograms maintained by the ASIC; see the {{<link title="ASIC Monitoring">}} for details.
- On Broadcom switches, the buffer status is not visible currently.

## Related Information

{{<exlink url="http://ipset.netfilter.org/iptables-extensions.man.html" text="iptables-extensions man page">}}
