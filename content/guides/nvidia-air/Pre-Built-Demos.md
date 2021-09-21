---
title: Pre-built Demos
author: NVIDIA
weight: 30
version: "1.0"
product: NVIDIA Air
---

Three demos are available in the Air simulation:

1. Cumulus in the Cloud
2. Cumulus and SONiC in the Cloud
3. SONiC in the Cloud

All three demos utilize the NVIDIA Cumulus Linux [reference topology](https://gitlab.com/cumulus-consulting/goldenturtle/cldemo2).

The reference topology provides a common and consistent pre-configured spine and leaf-based network topology, which serves as the basis for all supported NVIDIA demos and golden standards. The reference topology is a blank slate with minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

The reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out-of-band management network. The devices include:

- Four Cumulus Linux spines
- Four Cumulus Linux leafs
- Eight Ubuntu servers
- Two Cumulus Linux border leafs
- Two Cumulus Linux *fw* devices that provide a placeholder for *policy* devices
- One Ubuntu out-of-band management server (*oob-server*)
- One Cumulus Linux out-of-band management switch (*oob-switch*)
- One NVIDIA NetQ Cloud virtual appliance (*netq-ts*)

{{<img src="/images/guides/cldemo2-diagram.png" >}}

When you start the reference topology simulation environment, all interfaces (except for the out-of-band management network) are not configured and are administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that you can apply to this simulation topology.

## Cumulus In The Cloud

In the NVIDIA Cumulus in the Cloud demo, all nodes in the reference topology use Cumulus Linux as the network OS.

{{<img src="/images/guides/nvidia-air/1CumulusInTheCloud.png">}}

## Cumulus and SONiC In The Cloud

In the Cumulus and SONiC In The Cloud demo, two spines in the reference topology use SONiC as the network OS while all the remaining nodes use Cumulus Linux.

{{<img src="/images/guides/nvidia-air/2SonicSpines.png" >}}

## SONiC In The Cloud

In the SONiC In The Cloud demo, all nodes in the reference topology use SONiC as the network OS.

{{<img src="/images/guides/nvidia-air/3SonicDemo.png" >}}

## Guided Tour

Every demo has a Guided Tour. The guided tour provides step-by-step instructions on how to run the demo infrastructure through user interaction with the console session.

{{<img src="/images/guides/nvidia-air/GuidedTour.png" width="800px">}}
