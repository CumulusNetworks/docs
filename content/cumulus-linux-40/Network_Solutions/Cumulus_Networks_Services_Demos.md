---
title: Cumulus Networks Services Demos
author: Cumulus Networks
weight: 251
aliases:
 - /display/DOCS/Cumulus+Networks+Services+Demos
 - /pages/viewpage.action?pageId=8362987
pageID: 8362987
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The Cumulus Networks Services team demos provide a virtual environment
built using either VirtualBox or `libvirt` using Vagrant to manage the
VMs. This environment utilizes the reference topology shown below.
Vagrant and Cumulus VX can be used together to build virtual simulations
of production networks to validate configurations, develop automation
code and simulate failure scenarios.

## <span>Reference Topology</span>

The Cumulus Networks *reference topology* includes cabling (in DOT
format for dual use with
[PTM](/cumulus-linux/Layer_1_and_Switch_Ports/Prescriptive_Topology_Manager_-_PTM)),
MAC addressing, IP addressing, switches and servers. This topology is
blessed by the Professional Services Team at Cumulus Networks to fit a
majority of designs seen in the field.

{{% imgOld 0 %}}

### <span>IP and MAC Addressing</span>

| Hostname        | eth0 IP       | eth0 MAC          | Interface Count                                                  |
| --------------- | ------------- | ----------------- | ---------------------------------------------------------------- |
| oob-mgmt-server | 192.168.0.254 | any               |                                                                  |
| oob-mgmt-switch | 192.168.0.1   | any               | [Cumulus RMP](https://cumulusnetworks.com/cumulus-rmp/overview/) |
| leaf01          | 192.168.0.11  | A0:00:00:00:00:11 | 48x10g w/ 6x40g uplink                                           |
| leaf02          | 192.168.0.12  | A0:00:00:00:00:12 | 48x10g w/ 6x40g uplink                                           |
| leaf03          | 192.168.0.13  | A0:00:00:00:00:13 | 48x10g w/ 6x40g uplink                                           |
| leaf04          | 192.168.0.14  | A0:00:00:00:00:14 | 48x10g w/ 6x40g uplink                                           |
| spine01         | 192.168.0.21  | A0:00:00:00:00:21 | 32x40g                                                           |
| spine02         | 192.168.0.22  | A0:00:00:00:00:22 | 32x40g                                                           |
| server01        | 192.168.0.31  | A0:00:00:00:00:31 | 10g NICs                                                         |
| server02        | 192.168.0.32  | A0:00:00:00:00:32 | 10g NICs                                                         |
| server03        | 192.168.0.33  | A0:00:00:00:00:33 | 10g NICs                                                         |
| server04        | 192.168.0.34  | A0:00:00:00:00:34 | 10g NICs                                                         |
| exit01          | 192.168.0.41  | A0:00:00:00:00:41 | 48x10g w/ 6x40g uplink (exit leaf)                               |
| exit02          | 192.168.0.42  | A0:00:00:00:00:42 | 48x10g w/ 6x40g uplink (exit leaf)                               |
| edge01          | 192.168.0.51  | A0:00:00:00:00:51 | 10g NICs (customer edge device, firewall, load balancer, etc.)   |
| internet        | 192.168.0.253 | any               | (represents internet provider edge device)                       |

### <span>Build the Topology</span>

#### <span>Virtual Appliance</span>

You can build out the reference topology in hardware or using Cumulus VX
(the free Cumulus Networks virtual appliance). The [Cumulus Reference
Topology using
Vagrant](https://github.com/CumulusNetworks/cldemo-vagrant) is
essentially the reference topology built out inside Vagrant with
VirtualBox or KVM. The installation and setup instructions for bringing
up the entire reference topology on a laptop or server are on the
[cldemo-vagrant GitHub
repo](https://github.com/CumulusNetworks/cldemo-vagrant).

#### <span>Hardware</span>

Any switch from the [hardware compatibility
list](https://cumulusnetworks.com/support/linux-hardware-compatibility-list/)
is compatible with the topology as long as you follow the interface
count from the table above. Of course, in your own production
environment, you don't have to use exactly the same devices and cabling
as outlined above.

### <span>Demos</span>

You can find an up to date list of all the demos in the [cldemo-vagrant
GitHub
repository](https://github.com/CumulusNetworks/cldemo-vagrant#available-demos),
which is available to anyone free of charge.
