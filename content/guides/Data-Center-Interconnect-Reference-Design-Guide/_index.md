---
title: Data Center Interconnect Reference Design Guide
author: Cumulus Networks
weight: 10
product: Cumulus Networks Guides
imgData: guides
---

## Introduction


Data centers of all sizes host significant amounts of business-critical data---data that grows by the day, hour, and millisecond. Maintaining this data creates multiple challenges for a network architect, who must consider data resiliency, traffic, and storage. To address these challenges, data is split into pieces or replicated and then dispersed across an area, country, or even around the world. Traditional applications that generate traffic in and out of the data center (north-south traffic) are now a thing of the past, having ceded their position to modern successors that move traffic horizontally (east-west) within the data center.  

<!--Network Virtualization and Multitenancy, powered by the modern encapsulation VXLAN and the signaling over EVPN.--> Both are mature and well-defined technologies that are common in data centers, no matter their size. Although EVPN supports encapsulation methods other than VXLAN&mdash;such as NVGRE, MPLSoGRE, and recently, GENEVE&mdash;this article focuses on VXLAN-based EVPN because of its popularity and widespread deployment.

<br>
<br>
Creating workloads independent from a particular location become easier with the introduction of EVPN/VXLAN-based overlays. But exactly how does a network architect interconnect data centers that are resilient and scalable while also preserving KPIs? This article aims to clarify data center interconnect (DCI) from NVIDIA’s perspective and offers solutions to real-life challenges. 

For detailed information about VXLAN and EVPN, refer to the {{link to Cumulus Linux VXLAN and EVPN Network Reference Design Guide}}. 

## Reference DCI Topology

The reference DCI topology displayed in Figure 1 consists of two pods interconnected via two DCI connections between border leaf nodes of each pod.  We will use this topology throughout this article to explain the principles of DCI configuration.