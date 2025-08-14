---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 259
pageID: 8363018
---
*RDMA over Converged Ethernet* ({{<exlink url="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet" text="RoCE">}})
provides the ability to write to compute or storage elements using
remote direct memory access (RDMA) over an Ethernet network instead of
using host CPUs. RoCE relies on congestion control and lossless Ethernet
to operate. Cumulus Linux supports features that can enable lossless
Ethernet for RoCE environments. Note that while Cumulus Linux can
support RoCE environments, the hosts send and receive the RoCE packets.

RoCE helps you obtain a *converged network*, where all services run over
the Ethernet infrastructure, including Infiniband apps.

There are two versions of RoCE, which run at separate layers of the
stack:

- RoCEv1, which runs at the link layer and cannot be run over a routed network. Therefore, it requires the link layer {{<link url="Buffer-and-Queue-Management/#configure-priority-flow-control" text="priority flow control">}} (PFC) to be enabled.
- RoCEv2, which runs over layer 3. Since it's a routed solution, consider using {{<link url="Buffer-and-Queue-Management/#configure-explicit-congestion-notification" text="explicit congestion notification">}} (ECN) with RoCEv2 since ECN bits are communicated end-to-end across a routed network.

## Enable RDMA over Converged Ethernet with PFC

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB
global route header rides directly on top of the Ethernet header. The
lossless Ethernet layer handles congestion hop by hop.

To learn the Cumulus Linux settings you need to configure to support
RoCEv1, see the example configuration in the
{{<link url="Buffer-and-Queue-Management/#configure-priority-flow-control" text="PFC">}}
section of the {{<link url="Buffer-and-Queue-Management">}} chapter.

{{%notice tip%}}

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}},
you can alternately use NCLU to configure RoCE with PFC:

    cumulus@switch:~$ net add interface swp1 storage-optimized pfc
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the `/etc/cumulus/datapath/traffic.conf`
and  `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` files.
The most notable changes involve configuring both PFC and ECN on cos 3 in
`/etc/cumulus/datapath/traffic.conf` file. They also add a flow control buffer pool for 
lossless traffic and change the buffer limits in the
`/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file.

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
...
# packet header field used to determine the packet priority level
# fields include {802.1p, dscp}
traffic.packet_priority_source_set = [dscp]

# dscp values = {0..63}
traffic.cos_0.priority_source.dscp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
traffic.cos_1.priority_source.dscp = []
traffic.cos_2.priority_source.dscp = [48]
traffic.cos_3.priority_source.dscp = [26]
traffic.cos_4.priority_source.dscp = []
traffic.cos_5.priority_source.dscp = []
traffic.cos_6.priority_source.dscp = []
traffic.cos_7.priority_source.dscp = []

...

# internal cos values assigned to each priority group
# each cos value should be assigned exactly once
# internal cos values {0..7}
priority_group.control.cos_list = [2]
priority_group.service.cos_list = [3]
priority_group.bulk.cos_list = [0,1,4,5,6,7]

...

# priority flow control
pfc.port_group_list = [ROCE_PFC]
pfc.pfc_port_group.cos_list = [3]
pfc.pfc_port_group.port_set = swp1
pfc.pfc_port_group.port_buffer_bytes = 70000
pfc.pfc_port_group.xoff_size = 18000
pfc.pfc_port_group.xon_delta = 0
pfc.pfc_port_group.tx_enable = true
pfc.pfc_port_group.rx_enable = true

...

# Explicit Congestion Notification
# to configure ECN and RED on a group of ports:
# -- add or replace port group names in the port group list
# -- assign cos value(s) to the cos list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
# -- to enable RED requires the latest traffic.conf
ecn_red.port_group_list = [ROCE_ECN]
ecn_red.ecn_red_port_group.cos_list = [3]
ecn_red.ecn_red_port_group.port_set = swp1
ecn_red.ecn_red_port_group.ecn_enable = true
ecn_red.ecn_red_port_group.red_enable = false
ecn_red.ecn_red_port_group.min_threshold_bytes = 153600
ecn_red.ecn_red_port_group.max_threshold_bytes = 1536000
ecn_red.ecn_red_port_group.probability = 100

# scheduling algorithm: algorithm values = {dwrr}
scheduling.algorithm = dwrr

# traffic group scheduling weight
# weight values = {0..127}
# '0' indicates strict priority
priority_group.control.weight = 0
priority_group.service.weight = 16
priority_group.bulk.weight = 16

...
```

```
cumulus@mlnx:~$ sudo cat /usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf

...

# ingress service pool buffer allocation: percent of total buffer
# If a service pool has no priority groups, the buffer is added
# to the shared buffer space.
ingress_service_pool.0.percent = 50.0  # all priority groups

...

# Service pool buffer allocation: percent of total
# buffer size.
egress_service_pool.0.percent = 50.0   # all priority groups, UC and MC

...

# Resilient hash timers: in milliseconds
# resilient_hash_active_timer = 120000
# resilient_hash_max_unbalanced_timer = 4294967295
priority_group.control.id = 0
priority_group.service.id = 0
priority_group.bulk.id = 0
priority_group.control.service_pool = 0
priority_group.service.service_pool = 0
priority_group.bulk.service_pool = 0
ingress_service_pool.0.mode = 1
egress_service_pool.0.mode = 1
flow_control.service_pool = 1
ingress_service_pool.1.percent = 50.0
ingress_service_pool.1.mode = 1
egress_service_pool.1.percent = 100.0
egress_service_pool.1.mode = 1
priority_group.control.ingress_buffer.dynamic_quota = 11
priority_group.service.ingress_buffer.dynamic_quota = 11
priority_group.bulk.ingress_buffer.dynamic_quota = 11
flow_control.ingress_buffer.dynamic_quota = 9
priority_group.bulk.egress_buffer.uc.sp_dynamic_quota = 11
priority_group.service.egress_buffer.uc.sp_dynamic_quota = 11
priority_group.control.egress_buffer.uc.sp_dynamic_quota = 11
priority_group.bulk.egress_buffer.mc.sp_dynamic_quota = 9
priority_group.service.egress_buffer.mc.sp_dynamic_quota = 9
priority_group.control.egress_buffer.mc.sp_dynamic_quota = 9
```

{{%/notice%}}

{{%notice note%}}

While {{<link url="Buffer-and-Queue-Management/#configure-link-pause" text="link pause">}}
is another way to provide lossless ethernet, PFC is the preferred
method. PFC allows more granular control by pausing the traffic flow for
a given CoS group, rather than the entire link.

{{%/notice%}}

## Enable RDMA over Converged Ethernet with ECN

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the
Infiniband (IB) Transport Protocol over UDP. The IB transport protocol
includes an end-to-end reliable delivery mechanism, and has its own
sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion
experienced to the receiver. The receiver generates an RoCEv2 congestion
notification packet directed to the source of the packet.

To learn the Cumulus Linux settings you need to configure to support
RoCEv2, see the example configuration in the
{{<link url="Buffer-and-Queue-Management/#configure-explicit-congestion-notification" text="ECN">}}
section of the {{<link url="Buffer-and-Queue-Management">}} chapter.

{{%notice tip%}}

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, you can alternately use NCLU to configure RoCE with ECN:

    cumulus@switch:~$ net add interface swp1 storage-optimized
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
...

# packet header field used to determine the packet priority level
# fields include {802.1p, dscp}
traffic.packet_priority_source_set = [dscp]

...

# dscp values = {0..63}
traffic.cos_0.priority_source.dscp = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
traffic.cos_1.priority_source.dscp = []
traffic.cos_2.priority_source.dscp = [48]
traffic.cos_3.priority_source.dscp = [26]
traffic.cos_4.priority_source.dscp = []
traffic.cos_5.priority_source.dscp = []
traffic.cos_6.priority_source.dscp = []
traffic.cos_7.priority_source.dscp = []

...
```

The `storage-optimized` command changes the buffer limits in the
`/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file.

It also enables drop behaviors and Random Early Detection (RED). RED
identifies packets that have been added to a long egress queue. The ECN
action marks the packet and forwards it, requiring the packet to be
ECT-capable. However, the drop action drops the packet, requiring the
packet to **not** be ECT-capable.

```
cumulus@switch:~$ sudo cat /usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf

...

# Resilient hash timers: in milliseconds
# resilient_hash_active_timer = 120000
# resilient_hash_max_unbalanced_timer = 4294967295
priority_group.control.id = 0
priority_group.service.id = 0
priority_group.bulk.id = 0
priority_group.control.service_pool = 0
priority_group.service.service_pool = 0
priority_group.bulk.service_pool = 0
ingress_service_pool.0.mode = 1
egress_service_pool.0.mode = 1
priority_group.control.ingress_buffer.dynamic_quota = 11
priority_group.service.ingress_buffer.dynamic_quota = 11
priority_group.bulk.ingress_buffer.dynamic_quota = 11
priority_group.bulk.egress_buffer.uc.sp_dynamic_quota = 11
priority_group.service.egress_buffer.uc.sp_dynamic_quota = 11
priority_group.control.egress_buffer.uc.sp_dynamic_quota = 11
priority_group.bulk.egress_buffer.mc.sp_dynamic_quota = 9
priority_group.service.egress_buffer.mc.sp_dynamic_quota = 9
priority_group.control.egress_buffer.mc.sp_dynamic_quota = 9

...

# internal cos values assigned to each priority group
# each cos value should be assigned exactly once
# internal cos values {0..7}
priority_group.control.cos_list = [2]
priority_group.service.cos_list = [3]
priority_group.bulk.cos_list = [0,1,4,5,6,7]

...

# Explicit Congestion Notification
# to configure ECN and RED on a group of ports:
# -- add or replace port group names in the port group list
# -- assign cos value(s) to the cos list
# -- for each port group in the list
#    -- populate the port set, e.g.
#       swp1-swp4,swp8,swp50s0-swp50s3
# -- to enable RED requires the latest traffic.conf
ecn_red.port_group_list = [ROCE_ECN]
ecn_red.ecn_red_port_group.cos_list = [3]
ecn_red.ecn_red_port_group.port_set = swp1
ecn_red.ecn_red_port_group.ecn_enable = true
ecn_red.ecn_red_port_group.red_enable = false
ecn_red.ecn_red_port_group.min_threshold_bytes = 153600
ecn_red.ecn_red_port_group.max_threshold_bytes = 1536000
ecn_red.ecn_red_port_group.probability = 100

...

# traffic group scheduling weight
# weight values = {0..127}
# '0' indicates strict priority
priority_group.control.weight = 0
priority_group.service.weight = 16

...

```

{{%/notice%}}

## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
- {{<exlink url="https://community.mellanox.com/s/article/understanding-rocev2-congestion-management" text="RoCEv2 congestion management">}} - community.mellanox.com
- {{<exlink url="https://community.mellanox.com/s/article/lossless-roce-configuration-for-spectrum-based-cumulus-switches-in-dscp-based-qos-mode" text="Configuring RoCE over a DSCP-based lossless network">}} with a Mellanox Spectrum switch
