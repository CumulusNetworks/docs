---
title: Data Center Interconnect Reference Design Guide
author: NVIDIA
weight: 10
product: Technical Guides
imgData: guides
---
Data centers of all sizes host significant amounts of business-critical data---data that grows by the day, hour, and millisecond. Maintaining this data creates multiple challenges for a network architect, who must consider data resiliency, traffic, and storage. To mitigate network issues, data is split into pieces or replicated and then dispersed across an area, country, or even around the world. Traditional applications that generate traffic in and out of the data center (north-south traffic) are now a thing of the past, having given up their position to modern successors that move traffic horizontally (east-west) within the data center.  

Creating workloads independent of location became feasible with the introduction of network virtualization and multi-tenancy, powered by {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/" text="EVPN with VXLAN encapsulation">}}. Although EVPN supports encapsulation methods other than VXLAN&mdash;such as NVGRE, MPLSoGRE, and recently, GENEVE&mdash;this document focuses on VXLAN-based EVPN due to its popularity and widespread deployment.

So how does a network architect interconnect data centers that are resilient and scalable? This document tries to clarify data center interconnect (DCI) and offer applied solutions to networking challenges.

## Reference DCI Topology

This document uses the following reference DCI topology that consists of two pods interconnected with two DCI connections between the border leaf switches of each pod.

{{<img src="/images/guides/dci-reference-topology.png">}}

## NVIDIA Air

{{<exlink url="https://air.nvidia.com/" text="NVIDIA Air">}} is a cloud-hosted, network simulation platform that behaves exactly like a real world production environment. The topologies in this document were created with NVIDIA Air running Cumulus Linux 5.4.0.

NVIDIA AIR provides {{<exlink url="https://air.nvidia.com/marketplace?demo_id=77b72253-0a82-4148-b34d-a07dbef8f242" text="EVPN VXLAN based DCI labs">}}, which are pre-built demos. You can use the DCI labs along with this guide to better understand the configurations.
