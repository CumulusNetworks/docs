---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 1340
toc: 3
---
RDMA over Converged Ethernet ({{<exlink url="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet" text="RoCE">}}) enables you to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on congestion control and lossless Ethernet to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments.

{{%notice note%}}
While Cumulus Linux can support RoCE environments, the hosts send and receive the RoCE packets.
{{%/notice%}}

RoCE helps you obtain a *converged network*, where all services run over the Ethernet infrastructure, including Infiniband apps.

There are two versions of RoCE, which run at separate layers of the stack:

- RoCEv1 runs at the link layer and allows communication between any two hosts in the same Ethernet broadcast domain.
- RoCEv2 is an internet layer protocol and runs over layer 3.

## Enable RDMA over Converged Ethernet lossless (with PFC and ECN)

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB global route header rides directly on top of the Ethernet header. The lossless Ethernet layer handles congestion hop by hop.

To configure RoCE with PFC and ECN:

```
cumulus@switch:~$ cl set qos roce mode lossless
cumulus@switch:~$ cl config apply
```

{{%notice note%}}
{{<link url="Buffer-and-Queue-Management#link-pause" text="Link pause">}} is another way to provide lossless ethernet; however, PFC is the preferred method. PFC allows more granular control by pausing the traffic flow for a given CoS group instead of the entire link.
{{%/notice%}}

## Enable RDMA over Converged Ethernet lossy (with ECN)

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the Infiniband (IB) Transport Protocol over UDP. The IB transport protocol includes an end-to-end reliable delivery mechanism and has its own sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion experienced to the receiver. The receiver generates an RoCEv2 congestion notification packet directed to the source of the packet.

To configure RoCE with ECN:

```
cumulus@switch:~$ cl set qos roce mode lossy
cumulus@switch:~$ cl config apply
```

## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
- {{<exlink url="https://community.mellanox.com/s/article/understanding-rocev2-congestion-management" text="RoCEv2 congestion management">}} - community.mellanox.com
- {{<exlink url="https://community.mellanox.com/s/article/lossless-roce-configuration-for-spectrum-based-cumulus-switches-in-dscp-based-qos-mode" text="Configuring RoCE over a DSCP-based lossless network">}} on a switch with the NVIDIA Spectrum ASIC
