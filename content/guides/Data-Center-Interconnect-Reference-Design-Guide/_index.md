---
title: Data Center Interconnect Reference Design Guide
author: Cumulus Networks
weight: 10
product: Cumulus Networks Guides
imgData: guides
---

## Introduction

Data centers of all sizes host significant amounts of business-critical data---data that grows by the day, hour, and millisecond. Maintaining this data creates multiple challenges for a network architect, who must consider data resiliency, traffic, and storage. To mitigate network issues, data is split into pieces or replicated and then dispersed across an area, country, or even around the world. Traditional applications that generate traffic in and out of the data center (north-south traffic) are now a thing of the past, having ceded their position to modern successors that move traffic horizontally (east-west) within the data center.  

Creating workloads independent of location become feasible with the introduction of network virtualization and multi-tenancy, powered by {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/guides/EVPN-Network-Reference/" text="EVPN with VXLAN encapsulation">}}. Although EVPN supports encapsulation methods other than VXLAN&mdash;such as NVGRE, MPLSoGRE, and recently, GENEVE&mdash;this article focuses on VXLAN-based EVPN due to its popularity and widespread deployment.

But how does a network architect interconnect data centers that are resilient and scalable while also preserving KPIs? This article aims to clarify data center interconnect (DCI) from NVIDIA’s perspective and offer applied solutions to networking challenges. 

## Reference DCI Topology

The following reference DCI topology consists of two pods interconnected via two DCI connections between the border leaf nodes of each pod. This topology is referenced throughout the document.

{{<img src= "/images/guides/dci-reference-topology.png">}}

## NVIDIA Air

NVIDIA Air helps customers and partners to simulate any network topology supported by NVIDIA to be created as a Digital TWIN. You can find blogs , documentation and API guide of this platform in the corresponding links. 

The topologies (for each use case) in this document have been created using NVIDIA AIR Infrastructure Simulation Platform and could be ported/moved onto real NVIDIA switches when required hardware and software (Cumulus Linux 5.4.0 and above) installed. 
