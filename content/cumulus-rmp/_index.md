---
title: Cumulus RMP
author: Cumulus Networks
weight: -37
product: Cumulus RMP
version: "3.7"
subsection: true
---

## Introducing Cumulus RMP

Cumulus RMP is a network operating system in a ready-to-deploy solution
that enables out-of-band management for web-scale networks. It provides
an open platform for customers and system integrators to use as is or on
which to build rack management applications.

Cumulus RMP shares the same architecture, foundation, and user
experience with Cumulus Linux. However, the feature set is customized to
the needs of out-of-band management. For a comparison of the features
supported in Cumulus RMP, [see below](#cumulus-rmp-features).

<img src="/images/old_doc_images/RMP.png" />

## What's New in Cumulus RMP

{{%notice note%}}

Starting with Cumulus Linux 4.0.0, the Cumulus RMP uses the same binary image as Cumulus Linux.

{{%/notice%}}

Cumulus RMP 3.7.0 contains several bug fixes and the following new
features:

- {{<kb_link text="RADIUS Change of Authorization (CoA) requests" url="cumulus-linux-37/Layer-1-and-Switch-Ports/802.1X-Interfaces/#radius-change-of-authorization-and-disconnect-requests" >}}
- {{<kb_link text="RADIUS AAA local fallback authentication" url="cumulus-linux-37/System-Configuration/Authentication,-Authorization-and-Accounting/RADIUS-AAA/#local-fallback-authentication" >}}
- {{<kb_link text="TACACS+ local fallback authentication" url="cumulus-linux-37/System-Configuration/Authentication,-Authorization-and-Accounting/TACACS-Plus/#local-fallback-authentication" >}}
- New NCLU commands:
  - {{<kb_link text="Show the version of a package" url="cumulus-linux-37/Installation-Management/Adding-and-Updating-Packages/#display-the-version-of-a-package" >}}
  - {{<kb_link text="Show the interface description (alias)" url="cumulus-linux-37/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#add-descriptions-to-interfaces" >}}
    for all interfaces on the switch
  - {{<kb_link text="Change bond mode to IEEE 802.3ad" url="cumulus-linux-37/Layer-2/Bonding-Link-Aggregation/" >}} link
    aggregation mode

### What's New in Cumulus RMP 3.6.2

Cumulus RMP 3.6.2 contains several bug fixes and the following new
feature:

- NCLU commands available for {{<kb_link text="configuring traditional mode bridges" url="cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/" >}}

### What's New in Cumulus RMP 3.6.0

Cumulus RMP 3.6.0 contains several bug fixes and the following new
feature:

- Support for a combination of `local-as` and `allowas-in` commands

## Cumulus RMP Features

Cumulus RMP shares much of the same functionality as Cumulus Linux and
comes preinstalled on your choice of
[1G switches](https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/).
For more information about each feature, follow the links below to the
{{<kb_link text="Cumulus Linux user guide" url="cumulus-linux-37">}}:

| **Layer 2 Support**                                                                              | **Cumulus RMP** | **Cumulus Linux** |
| ------------------------------------------------------------------------------------------------ | --------------- | ----------------- |
| {{<kb_link text="LLDP" url="cumulus-linux-37/Layer-2/Link-Layer-Discovery-Protocol/" >}}                                 | ✓               | ✓                 |
| {{<kb_link text="PTM" url="cumulus-linux-37/Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM/" >}}             | ✓               | ✓                 |
| {{<kb_link text="Ethernet bridging" url="cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs/" >}}                          | ✓               | ✓                 |
| {{<kb_link text="Bonds/link aggregation" url="cumulus-linux-37/Layer-2/Bonding-Link-Aggregation/" >}}                    | ✓               | ✓                 |
| {{<kb_link text="MLAG" url="cumulus-linux-37/Layer-2/Multi-Chassis-Link-Aggregation-MLAG/" >}}                                                                                             |                 | ✓                 |
| LACP                                                                                             | ✓               | ✓                 |
| {{<kb_link text="LACP bypass" url="cumulus-linux-37/Layer-2/LACP-Bypass/"  >}}                                                                                    |                 | ✓                 |
| {{<kb_link text="Spanning tree protocol/RST" url="cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/" >}}   | ✓               | ✓                 |
| {{<kb_link text="802.1Q VLAN tagging" url="cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs/VLAN-Tagging/" >}}           | ✓               | ✓                 |
| {{<kb_link text="VLAN-aware bridging" url="cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode" >}} | ✓               | ✓                 |
| {{<kb_link text="BPDU guard" url="cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}}                   | ✓               | ✓                 |
| {{<kb_link text="Bridge assurance" url="cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}}             | ✓               | ✓                 |
| {{<kb_link text="BPDU filter" url="cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/" >}}                  | ✓               | ✓                 |
| {{<kb_link text="VRR" url="cumulus-linux-37/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP/" >}}                                                                                              |                 | ✓                 |
| {{<kb_link text="IGMP and MLD snooping" url="cumulus-linux-37/Layer-2/IGMP-and-MLD-Snooping/" >}}                                                                            |                 | ✓                 |
| {{<kb_link text="Unicast/broadcast storm control" url="cumulus-linux-37/Layer-2/Storm-Control/" >}}                                                                  |                 | ✓                 |
| CDP                                                                                              |                 | ✓                 |

&nbsp;

| **Layer 3 Support**                                         | **Cumulus RMP** | **Cumulus Linux** |
| ----------------------------------------------------------- | --------------- | ----------------- |
| [Static routing](/cumulus-linux-37/Layer-3/Routing/)        | ✓               | ✓                 |
| ECMP                                                        |                 | ✓                 |
| ECMP resilient hashing                                      |                 | ✓                 |
| OSPF                                                        |                 | ✓                 |
| BGP                                                         |                 | ✓                 |
| FRRouting                                                   |                 | ✓                 |
| BFD                                                         |                 | ✓                 |
| IPv6                                                        |                 | ✓                 |
| [Management VRF](/cumulus-linux-37/Layer-3/Management-VRF/) | ✓               | ✓                 |
| Virtual routing and forwarding (VRF)                        |                 | ✓                 |

&nbsp;

| **Additional Functionality**                                                                                                     | **Cumulus RMP** | **Cumulus Linux** |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| {{<kb_link text="Network command line utility" url="cumulus-linux-37/System-Configuration/Network-Command-Line-Utility-NCLU/" >}}                        | ✓               | ✓                 |
| {{<kb_link text="Interface configuration & management" url="cumulus-linux-37/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/" >}}       | ✓               | ✓                 |
| {{<kb_link text="802.1X interfaces" url="cumulus-linux-37/Layer-1-and-Switch-Ports/802.1X-Interfaces/" >}}                                               |                 | ✓                 |
| {{<kb_link text="Zero-touch OS install & upgrade" url="cumulus-linux-37/Installation-Management/Zero-Touch-Provisioning-ZTP/" >}}                        | ✓               | ✓                 |
| {{<kb_link text="Installation and package management" url="cumulus-linux-37/Installation-Management/" >}}                                                | ✓               | ✓                 |
| Full Linux extensibility                                                                                                         | ✓               | ✓                 |
| Network virtualization (VXLAN, EVPN, etc.)                                                                                       |                 | ✓                 |
| {{<kb_link text="Monitoring & troubleshooting" url="cumulus-linux-37/Monitoring-and-Troubleshooting/" >}}                                                | ✓               | ✓                 |
| {{<kb_link text="AAA" url="cumulus-linux-37/System-Configuration/Authentication,-Authorization-and-Accounting/LDAP-Authentication-and-Authorization/" >}} | ✓               | ✓                 |
| {{<kb_link text="ACLs / Netfilter" url="cumulus-linux-37/System-Configuration/Netfilter-ACLs/" >}}                                                       | ✓               | ✓                 |
| QoS                                                                                                                              |                 | ✓                 |


## Setting up a Cumulus RMP Switch

The {{<link text="quick start guide" url="Quick-Start-Guide" >}} walks you
through the steps necessary for getting your Cumulus RMP switch up and
running after you remove it from the box.

## Considerations

### Dynamic MAC Address Learning Delays

On Cumulus RMP switches, during an STP topology change or an interface flap, the following symptoms could be observed:

- A dynamic MAC address learned on the switch can take a long time to get
  populated back into the kernel, even though the MAC address has already been
  updated in hardware.
- The update of MAC learning can take a much longer time than expected, causing
  the MAC address to point to the wrong interface in hardware and not show up in
  the kernel, which leads to traffic disruption.

These symptoms have only been observed on Cumulus RMP switches; Cumulus RMP is meant to be used for out-of-band management purposes. Other platforms do not
exhibit this issue.
