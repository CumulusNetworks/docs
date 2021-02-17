---
title: VXLAN Routing
author: NVIDIA
weight: 610
toc: 3
---
VXLAN routing, sometimes referred to as *inter-VXLAN routing*, provides IP routing between VXLAN VNIs in overlay networks. The routing of traffic is based on the inner header or the overlay tenant IP address.

Because VXLAN routing is fundamentally routing, it is most commonly deployed with a control plane, such as Ethernet Virtual Private Network ({{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}). You can also set up static routing for MAC distribution and BUM handling.

For a detailed description of different VXLAN routing models and configuration examples, refer to {{<link url="Ethernet-Virtual-Private-Network-EVPN" text="EVPN">}}.

VXLAN routing supports full layer 3 multi-tenancy; all routing occurs in the context of a {{<link url="Virtual-Routing-and-Forwarding-VRF" text="VRF">}}. Also, VXLAN routing is supported for dual-attached hosts where the associated VTEPs function in {{<link url="VXLAN-Active-active-Mode" text="active-active mode">}}.
