---
title: Try It Pre-built Demos
author: NVIDIA
weight: 1500
toc: 2
---
This documentation includes pre-built **Try It** demos for certain Cumulus Linux features. The Try It demos run a simulation in NVIDIA Air; a cloud hosted platform that works exactly like a real world production deployment. All the Try It demos use the NVIDIA Cumulus Linux reference topology.

The following Try It demos are available:
- {{<link url="Configuration-Example/#nvue-commands" text="BGP">}}
- {{<link url="Inter-subnet-Routing/#configure-route-targets" text="EVPN downstream VNI">}}
- {{<link url="EVPN-Multihoming/#evpn-mh-with-head-end-replication" text="EVPN multihoming">}}
- {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#nvue-commands" text="MLAG">}}
- {{<link url="Protocol-Independent-Multicast-PIM/#example-pim-configuration" text="PIM">}}
- {{<link url="Static-VXLAN-Tunnels/#single-vxlan-device" text="Single VXLAN device">}}

## Access a Try It Demo

To access a demo, click the **Try It** tab in a Configuration Example section of the documentation:

{{< img src = "/images/cumulus-linux/try-it.png" >}}

NVIDIA Air starts building the simulation and boots the nodes:

{{< img src = "/images/cumulus-linux/try-it-boot.png" >}}

## Run Commands

When the simulation is ready, you can log into the leaf and spine switches. The switches are pre-configured with the configuration shown in the documentation. You can run any Cumulus Linux commands to learn more about the feature and configure additional settings.

{{< img src = "/images/cumulus-linux/try-it-launch.png" >}}

## Launch in AIR
<!-- vale off -->
If you want to save the simulation or extend the run time, click **LAUNCH IN AIR** to access the network simulation platform. From this platform, you can run additional pre-built demos and even build your own simulations. Refer to the [NVIDIA Air User Guide]({{<ref "/guides/nvidia-air" >}}).
<!-- vale on -->
