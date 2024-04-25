---
title: Cumulus Networks Services Demos
author: NVIDIA
weight: 1150
toc: 3
---
The Services team demos provide a virtual environment built with either VirtualBox or `libvirt` using Vagrant to manage the VMs. This environment utilizes the reference topology shown below. Vagrant and Cumulus VX can be used together to build virtual simulations of production networks to validate configurations, develop automation code and simulate failure scenarios.

## Reference Topology

The *reference topology* includes cabling (in DOT format for dual use with {{<link url="Prescriptive-Topology-Manager-PTM" text="PTM">}}), MAC addressing, IP addressing, switches and servers. This topology is blessed by the Professional Services Team to fit a majority of designs seen in the field.

{{< img src = "/images/cumulus-linux/network-solutions-ref-topology.png" >}}

### IP and MAC Addressing

| Hostname | eth0 IP | eth0 MAC | Interface Count |
| -------- | ------- | ---------| ----------------|
| oob-mgmt-server | 192.168.0.254 | any |  |
| oob-mgmt-switch | 192.168.0.1   | any |  |
| leaf01 | 192.168.0.11  | A0:00:00:00:00:11 | 48x10g w/ 6x40g uplink |
| leaf02 | 192.168.0.12  | A0:00:00:00:00:12 | 48x10g w/ 6x40g uplink |
| leaf03 | 192.168.0.13  | A0:00:00:00:00:13 | 48x10g w/ 6x40g uplink |
| leaf04 | 192.168.0.14  | A0:00:00:00:00:14 | 48x10g w/ 6x40g uplink |
| spine01 | 192.168.0.21  | A0:00:00:00:00:21 | 32x40g |
| spine02 | 192.168.0.22  | A0:00:00:00:00:22 | 32x40g |
| server01 | 192.168.0.31  | A0:00:00:00:00:31 | 10g NICs |
| server02 | 192.168.0.32  | A0:00:00:00:00:32 | 10g NICs |
| server03 | 192.168.0.33  | A0:00:00:00:00:33 | 10g NICs |
| server04 | 192.168.0.34  | A0:00:00:00:00:34 | 10g NICs |
| exit01 | 192.168.0.41  | A0:00:00:00:00:41 | 48x10g w/ 6x40g uplink (exit leaf) |
| exit02  | 192.168.0.42  | A0:00:00:00:00:42 | 48x10g w/ 6x40g uplink (exit leaf) |
| edge01  | 192.168.0.51  | A0:00:00:00:00:51 | 10g NICs (customer edge device, firewall, load balancer, etc.) |
| internet | 192.168.0.253 | any  | (represents internet provider edge device) |

### Build the Topology

#### Virtual Appliance

You can build out the reference topology in hardware or using Cumulus VX. The {{<exlink url="https://github.com/CumulusNetworks/cldemo-vagrant" text="Cumulus Reference Topology using Vagrant">}} is
essentially the reference topology built out inside Vagrant with VirtualBox or KVM. The installation and setup instructions for bringing up the entire reference topology on a laptop or server are on the {{<exlink url="https://github.com/CumulusNetworks/cldemo-vagrant" text="cldemo-vagrant GitHub repo">}}.

### Demos

You can find an up to date list of all the demos in the {{<exlink url="https://github.com/CumulusNetworks/cldemo-vagrant#available-demos" text="cldemo-vagrant GitHub repository">}}, which is available to anyone free of charge.
