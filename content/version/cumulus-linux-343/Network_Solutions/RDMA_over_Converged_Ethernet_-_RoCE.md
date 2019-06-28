---
title: RDMA over Converged Ethernet - RoCE
author: Cumulus Networks
weight: 251
aliases:
 - /display/CL34/RDMA+over+Converged+Ethernet+-+RoCE
 - /pages/viewpage.action?pageId=7112741
pageID: 7112741
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
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
    network. Therefore, it requires the link layer [priority flow
    control](Buffer_and_Queue_Management.html#src-7112623_BufferandQueueManagement-pfc)
    (PFC) to be enabled.

  - RoCEv2, which runs over layer 3. Since it's a routed solution,
    Cumulus Networks recommends you use [explicit congestion
    notification](Buffer_and_Queue_Management.html#src-7112623_BufferandQueueManagement-ecn)
    (ECN) with RoCEv2 since ECN bits are communicated end-to-end across
    a routed network.

## <span>Enabling RDMA over Converged Ethernet with PFC</span>

RoCEv1 uses the Infiniband (IB) Protocol over converged Ethernet. The IB
global route header rides directly on top of the Ethernet header. The
lossless Ethernet layer handles congestion hop by hop.

To learn the Cumulus Linux settings you need to configure to support
RoCEv1, see the example configuration in the
[PFC](Buffer_and_Queue_Management.html#src-7112623_BufferandQueueManagement-pfc)
section of the [Buffer and Queue
Management](/version/cumulus-linux-343/Interface_Configuration_and_Management/Buffer_and_Queue_Management/)
chapter.

{{%notice note%}}

While [link
pause](Buffer_and_Queue_Management.html#src-7112623_BufferandQueueManagement-pause)
is another way to provide lossless ethernet, PFC is the preferred
method. PFC allows more granular control by pausing the traffic flow for
a given CoS group, rather than the entire link.

{{%/notice%}}

## <span>Enabling RDMA over Converged Ethernet with ECN</span>

RoCEv2 requires flow control for lossless Ethernet. RoCEv2 uses the
Infiniband (IB) Transport Protocol over UDP. The IB transport protocol
includes an end-to-end reliable delivery mechanism, and has its own
sender notification mechanism.

RoCEv2 congestion management uses RFC 3168 to signal congestion
experienced to the receiver. The receiver generates an RoCEv2 congestion
notification packet directed to the source of the packet.

To learn the Cumulus Linux settings you need to configure to support
RoCEv2, see the example configuration in the
[ECN](Buffer_and_Queue_Management.html#src-7112623_BufferandQueueManagement-ecn)
section of the [Buffer and Queue
Management](/version/cumulus-linux-343/Interface_Configuration_and_Management/Buffer_and_Queue_Management/)
chapter.

## <span>Related Information</span>

  - [RoCE
    introduction](http://www.roceinitiative.org/roce-introduction/) —
    roceinitiative.org

  - [RoCEv2 congestion
    management](https://community.mellanox.com/docs/DOC-2321) —
    community.mellanox.com

  - [Configuring RoCE over a DSCP-based lossless
    network](https://community.mellanox.com/docs/DOC-2884) with a
    Mellanox Spectrum switch
