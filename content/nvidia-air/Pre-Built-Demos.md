---
title: Pre-built Demos
author: NVIDIA
weight: 30
product: NVIDIA Air
---

NVIDIA Air provides three pre-built demos:
- Cumulus in the Cloud
- Cumulus and SONiC in the Cloud
- SONiC in the Cloud

All three demos use the NVIDIA Cumulus Linux [reference topology](https://gitlab.com/cumulus-consulting/goldenturtle/cldemo2-air-builder/), which provides a common and consistent pre-configured spine and leaf-based network topology and serves as the basis for all supported NVIDIA demos and golden standards. The reference topology is a blank slate with minimal configuration, and prepares the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

The reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out-of-band management network. The devices include:
- Four Cumulus Linux spines
- Four Cumulus Linux leafs
- Eight Ubuntu servers
- Two Cumulus Linux border leafs
- Two Cumulus Linux *fw* devices that provide a placeholder for *policy* devices
- One Ubuntu out-of-band management server (*oob-server*)
- One Cumulus Linux out-of-band management switch (*oob-switch*)
- One NVIDIA NetQ Cloud virtual appliance (*netq-ts*)

<!--{{<img src="/images/guides/cldemo2-diagram.png" >}}-->
When you start the reference topology simulation environment, none of the interfaces are configured (except for the out-of-band management network) and all interfaces are administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that you can apply to this simulation topology.

## Cumulus In The Cloud

In the NVIDIA Cumulus in the Cloud demo, all nodes in the reference topology use Cumulus Linux as the network operating system.

{{<img src="/images/guides/nvidia-air/1CumulusInTheCloud.png">}}

## Cumulus and SONiC In The Cloud

In the Cumulus and SONiC In The Cloud demo, two spines in the reference topology use SONiC as the network operating system and all the remaining nodes use Cumulus Linux.

{{<img src="/images/guides/nvidia-air/2SonicSpines.png" >}}

## SONiC In The Cloud

In the SONiC In The Cloud demo, all nodes in the reference topology use SONiC as the network operating system.

{{<img src="/images/guides/nvidia-air/3SonicDemo.png" >}}

## Guided Tour

Every demo has a Guided Tour that provides step-by-step instructions on how to run the demo infrastructure in a console session.

{{<img src="/images/guides/nvidia-air/GuidedTour.png" width="800px">}}
