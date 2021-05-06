---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 1200
toc: 3
---
*RDMA over Converged Ethernet* ({{<exlink url="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet" text="RoCE">}}) provides the ability to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on congestion control and lossless Ethernet to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments. 

{{%notice note%}}

While Cumulus Linux can support RoCE environments, the hosts send and receive the RoCE packets.

{{%/notice%}}

RoCE helps you obtain a *converged network*, where all services run over the Ethernet infrastructure, including Infiniband apps.

There are two versions of RoCE, which run at separate layers of the stack:

- RoCEv1, which runs at the link layer and cannot be run over a routed network. Therefore, it requires the link layer {{<link url="Buffer-and-Queue-Management#priority-flow-control" text="priority flow control">}} (PFC) to be enabled.
- RoCEv2, which runs over layer 3. Use {{<link url="Buffer-and-Queue-Management#congestion-notification" text="explicit congestion notification">}} (ECN) with RoCEv2 as ECN bits are communicated end-to-end across a routed network.

## Enable RDMA over Converged Ethernet with PFC

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB global route header rides directly on top of the Ethernet header. The lossless Ethernet layer handles congestion hop by hop.

To learn the Cumulus Linux settings, you need to configure support for RoCEv1, see the example configuration in the {{<link url="Buffer-and-Queue-Management#priority-flow-control" text="PFC">}} section of the {{<link url="Buffer-and-Queue-Management">}} chapter.

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, you can use NCLU to configure RoCE with PFC:

```
cumulus@switch:~$ net add interface swp1 storage-optimized pfc
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/cumulus/datapath/traffic.conf` file. They configure PFC on cos 1, ECN on cos 0 and 1 in `/etc/cumulus/datapath/traffic.conf` file. They also add a flow control buffer pool for lossless traffic and change the buffer limits in the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file.

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
...
ecn_red.port_group_list = [ROCE_ECN]
pfc.ROCE_PFC.port_set = swp1
pfc.ROCE_PFC.cos_list = [1]
pfc.ROCE_PFC.xoff_size = 18000
pfc.ROCE_PFC.xon_delta = 18000
pfc.ROCE_PFC.tx_enable = true
pfc.ROCE_PFC.rx_enable = true
pfc.ROCE_PFC.port_buffer_bytes = 70000
ecn_red.ROCE_ECN.port_set = swp1
ecn_red.ROCE_ECN.cos_list = [0,1]
ecn_red.ROCE_ECN.min_threshold_bytes = 150000
ecn_red.ROCE_ECN.max_threshold_bytes = 1500000
ecn_red.ROCE_ECN.ecn_enable = true
ecn_red.ROCE_ECN.red_enable = true
ecn_red.ROCE_ECN.probability = 100

...
```

{{%notice note%}}

- While {{<link url="Buffer-and-Queue-Management#link-pause" text="link pause">}} is another way to provide lossless ethernet, PFC is the preferred method. PFC allows more granular control by pausing the traffic flow for a given CoS group, rather than the entire link.
- RoCEv1 depends on 802.1p fields for traffic classification; therefore it is not supported with access ports. Use trunk ports with RoCEv1.

{{%/notice%}}

## Enable RDMA over Converged Ethernet with ECN

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the Infiniband (IB) Transport Protocol over UDP. The IB transport protocol includes an end-to-end reliable delivery mechanism and has its own sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion experienced to the receiver. The receiver generates an RoCEv2 congestion notification packet directed to the source of the packet.

To learn the Cumulus Linux settings you need to configure support for RoCEv2, see the example configuration in the {{<link url="Buffer-and-Queue-Management#congestion-notification" text="ECN">}} section of the {{<link url="Buffer-and-Queue-Management">}} chapter.

On switches with {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Spectrum ASICs">}}, you can use NCLU to configure RoCE with ECN:

```
cumulus@switch:~$ net add interface swp1 storage-optimized
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/cumulus/datapath/traffic.conf` file:

```
cumulus@switch:~$ sudo cat /etc/cumulus/datapath/traffic.conf
...
ecn_red.port_group_list = [ROCE_ECN]
ecn_red.ROCE_ECN.port_set = swp1
ecn_red.ROCE_ECN.cos_list = [0,1]
ecn_red.ROCE_ECN.min_threshold_bytes = 150000
ecn_red.ROCE_ECN.max_threshold_bytes = 1500000
ecn_red.ROCE_ECN.ecn_enable = true
ecn_red.ROCE_ECN.red_enable = true
ecn_red.ROCE_ECN.probability = 100
...
```

The `storage-optimized` command changes the buffer limits in the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file.

The  `storage-optimized` command also enables drop behaviors and Random Early Detection (RED). RED identifies packets that have been added to a long egress queue. The ECN action marks the packet and forwards it, requiring the packet to be ECT-capable. However, the drop action drops the packet, requiring the packet to **not** be ECT-capable.

## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
- {{<exlink url="https://community.mellanox.com/s/article/understanding-rocev2-congestion-management" text="RoCEv2 congestion management">}} - community.mellanox.com
- {{<exlink url="https://community.mellanox.com/s/article/lossless-roce-configuration-for-spectrum-based-cumulus-switches-in-dscp-based-qos-mode" text="Configuring RoCE over a DSCP-based lossless network">}} on a switch with a Mellanox Spectrum ASIC
