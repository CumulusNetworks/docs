---
title: RDMA over Converged Ethernet - RoCE
author: NVIDIA
weight: 322
toc: 3
---
RDMA over Converged Ethernet ({{<exlink url="https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet" text="RoCE">}}) enables you to write to compute or storage elements using remote direct memory access (RDMA) over an Ethernet network instead of using host CPUs. RoCE relies on explicit congestion notification (ECN) and priority flow control (PFC) to operate. Cumulus Linux supports features that can enable lossless Ethernet for RoCE environments.

{{%notice note%}}
While Cumulus Linux can support RoCE environments, the end hosts must support the RoCE protocol.
{{%/notice%}}

RoCE helps you obtain a *converged network*, where all services run over the Ethernet infrastructure, including Infiniband apps.

## Enable RDMA over Converged Ethernet lossless (with PFC and ECN)

RoCE uses the Infiniband (IB) Protocol over converged Ethernet. The IB global route header rides directly on top of the Ethernet header. The lossless Ethernet layer handles congestion hop by hop.

To configure RoCE with PFC and ECN:

{{< tabs "roce lossless commands">}}
{{< tab "NCLU Commands">}}
```
cumulus@switch:~$ net add roce mode lossless
cumulus@switch:~$ net commit
```
{{< /tab >}}
{{< tab "NVUE Commands">}}
```
cumulus@switch:~$ nv set qos roce mode lossless
cumulus@switch:~$ nv config apply
```
{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
{{<link url="Quality-of-Service#link-pause" text="Link pause">}} is another way to provide lossless ethernet; however, PFC is the preferred method. PFC allows more granular control by pausing the traffic flow for a given CoS group instead of the entire link.
{{%/notice%}}

## Enable RDMA over Converged Ethernet lossy (with ECN)

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the Infiniband (IB) Transport Protocol over UDP. The IB transport protocol includes an end-to-end reliable delivery mechanism and has its own sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion experienced to the receiver. The receiver generates an RoCEv2 congestion notification packet directed to the source of the packet.

To configure RoCE with ECN:

{{< tabs "roce commands">}}
{{< tab "NCLU Commands">}}
```
cumulus@switch:~$ net add roce lossless
cumulus@switch:~$ net commit
```
{{< /tab >}}
{{< tab "NVUE Commands">}}
```
cumulus@switch:~$ nv set qos roce lossy
cumulus@switch:~$ nv config apply
```
{{< /tab >}}
{{< /tabs >}}

## Remove RoCE Configuration
To remove RoCE configurations:

{{< tabs "remove roce commands">}}
{{< tab "NCLU Commands">}}
```
cumulus@switch:~$ net del roce
cumulus@switch:~$ net commit
```
{{< /tab >}}
{{< tab "NVUE Commands">}}
```
cumulus@switch:~$ nv unset qos roce
cumulus@switch:~$ nv config apply
```
{{< /tab >}}
{{< /tabs >}}
## Related Information

- {{<exlink url="http://www.roceinitiative.org/roce-introduction/" text="RoCE introduction">}} - roceinitiative.org
- {{<exlink url="https://community.mellanox.com/s/article/understanding-rocev2-congestion-management" text="RoCEv2 congestion management">}} - community.mellanox.com
