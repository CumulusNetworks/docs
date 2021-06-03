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



## NVIDIA Cumulus In The Cloud

This demo is built on top of the Nvidia networking reference topology. 

The Cumulus Networks reference topology provides a common and consistent preconfigured spine and leaf base network topology, which serves as the basis for all supported Cumulus Networks demos and golden standards. This reference topology is intended to be a blank slate with minimal configuration to prepare the simulation to receive additional deployment and provisioning that demonstrates a feature or represents a fully operational production network.

The Cumulus Networks reference topology provides a complete two-tier spine and leaf topology. It also includes a complete out-of-band management. The devices include:

- Four Cumulus Linux 3.7 spines
- Four Cumulus Linux 3.7 leafs
- Eight Ubuntu 18.04 servers
- Two Cumulus Linux 3.7 border leafs
- Two Cumulus Linux 3.7 *fw* devices that provide a placeholder for *policy* devices
- One Ubuntu 18.04 out-of-band management server (oob-mgmt-server)
- One Cumulus Linux 3.7 out-of-band management switch (oob-mgmt-switch)
- One Cumulus NetQ Cloud virtual appliance (netq-ts)

{{<img src="/images/guides/nvidia-air/1CumulusInTheCloud.png" >}}

