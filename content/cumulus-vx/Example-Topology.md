---
title: 'Example Topology'
author: Cumulus Networks
weight: 8
product: Cumulus VX
version: '3.7'
---
The Cumulus VX documentation uses the following two leaf and one spine tolopolgy to configure Cumulus VX. This topology is intended to be a blank slate with minimal configuration that you can build on, if desired.

{{< img src = "/images/cumulus-vx/VX-Topology.png" >}}

In this topology:

- Server01 and Server02 are connected to Leaf01 and Leaf02, which are the access layer switches on the network
- Leaf01 and Leaf02 are MLAG peer switches that appear as a single device (this provides greater redundancy and greater system throughput)
- Leaf01 and Leaf02 connect to Spine01, which is the aggregation layer switch on the network

The steps provided to configure each VM on your platform of choice uses this topology.
