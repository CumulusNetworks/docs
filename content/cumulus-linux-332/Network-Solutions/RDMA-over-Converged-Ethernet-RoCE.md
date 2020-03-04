---
title: RDMA over Converged Ethernet - RoCE
author: Cumulus Networks
weight: 245
aliases:
 - /display/CL332/RDMA+over+Converged+Ethernet+++RoCE
 - /display/CL332/RDMA+over+Converged+Ethernet+-+RoCE
 - /display/CL332/RDMA+over+Converged+Ethernet+RoCE
 - /pages/viewpage.action?pageId=5869292
pageID: 5869292
---
*RDMA over Converged Ethernet*
([RoCE](https://en.wikipedia.org/wiki/RDMA_over_Converged_Ethernet))
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

  - RoCEv1, which runs at the link layer and cannot be run over a routed
    network. Therefore, it requires the link layer 
    [priority flow control](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/#configuring-priority-flow-control)
    (PFC) to be enabled.
  - RoCEv2, which runs over layer 3. Since it's a routed solution,
    Cumulus Networks recommends you use 
    [explicit congestion notification](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/#configuring-explicit-congestion-notification)
    (ECN) with RoCEv2 since ECN bits are communicated end-to-end across
    a routed network.

## Enabling RDMA over Converged Ethernet with PFC

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB
global route header rides directly on top of the Ethernet header. The
lossless Ethernet layer handles congestion hop by hop.

To learn the Cumulus Linux settings you need to configure to support
RoCEv1, see the example configuration in the
[PFC](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/#configuring-priority-flow-control)
section of the [Buffer and Queue
Management](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/)
chapter.

{{%notice note%}}

While [link pause](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/#configuring-link-pause)
is another way to provide lossless ethernet, PFC is the preferred
method. PFC allows more granular control by pausing the traffic flow for
a given CoS group, rather than the entire link.

{{%/notice%}}

## Enabling RDMA over Converged Ethernet with ECN

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the
Infiniband (IB) Transport Protocol over UDP. The IB transport protocol
includes an end-to-end reliable delivery mechanism, and has its own
sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion
experienced to the receiver. The receiver generates an RoCEv2 congestion
notification packet directed to the source of the packet.

To learn the Cumulus Linux settings you need to configure to support
RoCEv2, see the example configuration in the
[ECN](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/#configuring-explicit-congestion-notification)
section of the [Buffer and Queue
Management](/cumulus-linux-332/Interface-Configuration-and-Management/Buffer-and-Queue-Management/)
chapter.

## Related Information

  - [RoCE introduction](http://www.roceinitiative.org/roce-introduction/) -
    roceinitiative.org
  - [RoCEv2 congestion management](https://community.mellanox.com/docs/DOC-2321) -
    community.mellanox.com
  - [Configuring RoCE over a DSCP-based lossless network](https://community.mellanox.com/docs/DOC-2884) with a
    Mellanox Spectrum switch
