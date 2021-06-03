---
title: Pre Built Demos
weight: 30
version: "1.0"
draft: true
---

There are three demos available on the Air simulation:
1. NVIDIA Cumulus In The Cloud
2. SONiC Spines
3. SONiC Demo

All three demos are built on top of the reference topology.

The reference topology provides a common and consistent preconfigured spine and leaf base network topology, which serves as the basis for all supported NVIDIA demos and golden standards. This reference topology is intended to be a blank slate with minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

The reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out-of-band management network. The devices include:

- Four Cumulus Linux spines
- Four Cumulus Linux leafs
- Eight Ubuntu servers
- Two Cumulus Linux border leafs
- Two Cumulus Linux *fw* devices that provide a placeholder for *policy* devices
- One Ubuntu out-of-band management server (oob-mgmt-server)
- One Cumulus Linux out-of-band management switch (oob-mgmt-switch)
- One NVIDIA NetQ Cloud virtual appliance (netq-ts)

{{<img src="/images/guides/cldemo2-diagram.png" >}}

When you start the reference topology simulation environment, all interfaces (except for the out-of-band management network) are unconfigured and administratively down. The golden standard configurations and demos provide interface and routing protocol configurations that are applied to this simulation topology.

## NVIDIA Cumulus In The Cloud

The NVIDIA Cumulus In The Cloud demo has all nodes in the reference topology set to use Cumulus Linux.

{{<img src="/images/guides/nvidia-air/1CumulusInTheCloud.png" >}}

## SONiC Spines

The SONiC Spines demo has two spines in the reference topology set to use SONiC while all the remaining nodes are Cumulus Linux.

{{<img src="/images/guides/nvidia-air/2SonicSpines.png" >}}

## SONiC Demo

The SONiC demo has all nodes in the reference topology set to use SONiC.

{{<img src="/images/guides/nvidia-air/3SonicDemo.png" >}}

## Guided Tour

Every demo has a Guided Tour. The guided tour provides step by step instructions on how to run the demo infrastructure through user interaction with the console session.

{{<img src="/images/guides/nvidia-air/GuidedTour.png" >}}

