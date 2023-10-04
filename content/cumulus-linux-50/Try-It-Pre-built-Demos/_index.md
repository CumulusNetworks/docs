---
title: Try It Pre-built Demos
author: NVIDIA
weight: 1500
toc: 2
---
This documentation includes pre-built **Try It** demos for certain Cumulus Linux features. The Try It demos run a simulation in NVIDIA Air; a cloud hosted platform that works exactly like a real world production deployment. All the Try It demos use the NVIDIA Cumulus Linux reference topology.

The following Try It demos are available:
- {{<link url="Configuration-Example" text="BGP">}}
- {{<link url="OSPF-Configuration-Example" text="OSPF">}}
- {{<link url="Protocol-Independent-Multicast-PIM/#configuration-example" text="PIM">}}
- {{<link url="Inter-subnet-Routing/#configure-route-targets" text="EVPN downstream VNI">}}
- {{<link url="EVPN-Multihoming/#configuration-example" text="EVPN multihoming">}}
- {{<link url="Configuration-Examples/#evpn-symmetric-routing" text="EVPN symmetric routing">}}
- {{<link url="Multi-Chassis-Link-Aggregation-MLAG/#configuration-example" text="MLAG">}}
- {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#configuration-example" text="VRR">}}
- {{<link url="Static-VXLAN-Tunnels/#single-vxlan-device" text="Single VXLAN device">}}
- {{<link url="VXLAN-Active-active-Mode/#configuration-example" text="VXLAN Active-active Mode">}}

## Access a Try It Demo

To access a demo, click the **Try It** tab in a Configuration Example section of the documentation. Acknowledge the captcha and select the Launch Simulation button:

{{< img src = "/images/cumulus-linux/try-it.png" >}}

NVIDIA Air starts building the simulation and boots the nodes:

{{< img src = "/images/cumulus-linux/try-it-boot.png" >}}

{{%notice note%}}
The simulation can take a few minutes to build and might display a grey screen before loading.
{{%/notice%}}

## Run Commands

When the simulation is ready, you can log into the leaf and spine switches. The switches are pre-configured with the configuration shown in the documentation. You can run any Cumulus Linux commands to learn more about the feature and configure additional settings.

{{< img src = "/images/cumulus-linux/try-it-launch.png" >}}

## Launch in AIR
<!-- vale off -->
If you want to save the simulation or extend the run time, click **LAUNCH IN AIR** to access the network simulation platform. From this platform, you can run additional pre-built demos and even build your own simulations. Refer to the [NVIDIA Air User Guide]({{<ref "/nvidia-air" >}}).
<!-- vale on -->
