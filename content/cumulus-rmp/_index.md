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

## What's New in Cumulus RMP

Cumulus RMP 3.7.0 contains several bug fixes and the following new
features:

- [RADIUS Change of Authorization (CoA) requests]({{<ref "/cumulus-linux-37/Layer-1-and-Switch-Ports/802.1X-Interfaces.md#radius-change-of-authorization-and-disconnect-requests" >}})
- [RADIUS AAA local fallback authentication]({{<ref "/cumulus-linux-37/System-Configuration/Authentication-Authorization-and-Accounting/RADIUS-AAA#local-fallback-authentication" >}})
- [TACACS+ local fallback authentication]({{<ref "/cumulus-linux-37/System-Configuration/Authentication-Authorization-and-Accounting/TACACS-Plus#local-fallback-authentication" >}})
- New NCLU commands:
  - [Show the version of a package]({{<ref "/cumulus-linux-37/Installation-Management/Adding-and-Updating-Packages#display-the-version-of-a-package" >}})
  - [Show the interface description (alias)]({{<ref "/cumulus-linux-37/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management#add-descriptions-to-interfaces" >}})
    for all interfaces on the switch
  - [Change bond mode to IEEE 802.3ad]({{<ref "/cumulus-linux-37/Layer-2/Bonding-Link-Aggregation" >}}) link
    aggregation mode

### What's New in Cumulus RMP 3.6.2

Cumulus RMP 3.6.2 contains several bug fixes and the following new
feature:

- NCLU commands available for [configuring traditional mode bridges]({{<ref "/cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode" >}})

### What's New in Cumulus RMP 3.6.0

Cumulus RMP 3.6.0 contains several bug fixes and the following new
feature:

- Support for a combination of `local-as` and `allowas-in` commands

## Cumulus RMP Features

Cumulus RMP shares much of the same functionality as Cumulus Linux and
comes preinstalled on your choice of 1G switches. For more information about each feature, follow the links below to the [Cumulus Linux user guide]({{<ref "/cumulus-linux-37">}}):

| **Layer 2 Support**                                                                              | **Cumulus RMP** | **Cumulus Linux** |
| ------------------------------------------------------------------------------------------------ | --------------- | ----------------- |
| [LLDP]({{<ref "/cumulus-linux-37/Layer-2/Link-Layer-Discovery-Protocol" >}})                                 | ✓               | ✓                 |
| [PTM]({{<ref "/cumulus-linux-37/Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM" >}})             | ✓               | ✓                 |
| [Ethernet bridging]({{<ref "/cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs" >}})                          | ✓               | ✓                 |
| [Bonds/link aggregation]({{<ref "/cumulus-linux-37/Layer-2/Bonding-Link-Aggregation" >}})                    | ✓               | ✓                 |
| [MLAG]({{<ref "/cumulus-linux-37/Layer-2/Multi-Chassis-Link-Aggregation-MLAG" >}})                                                                                             |                 | ✓                 |
| LACP                                                                                             | ✓               | ✓                 |
| [LACP bypass]({{<ref "/cumulus-linux-37/Layer-2/LACP-Bypass">}})                                                                                    |                 | ✓                 |
| [Spanning tree protocol/RST]({{<ref "/cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}})   | ✓               | ✓                 |
| [802.1Q VLAN tagging]({{<ref "/cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs/VLAN-Tagging" >}})           | ✓               | ✓                 |
| [VLAN-aware bridging]({{<ref "/cumulus-linux-37/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode" >}}) | ✓               | ✓                 |
| [BPDU guard]({{<ref "/cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}})                   | ✓               | ✓                 |
| [Bridge assurance]({{<ref "/cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}})             | ✓               | ✓                 |
| [BPDU filter]({{<ref "/cumulus-linux-37/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree" >}})                  | ✓               | ✓                 |
| [VRR]({{<ref "/cumulus-linux-37/Layer-2/Virtual-Router-Redundancy-VRR-and-VRRP" >}})                                                                                              |                 | ✓                 |
| [IGMP and MLD snooping]({{<ref "/cumulus-linux-37/Layer-2/IGMP-and-MLD-Snooping" >}})                                                                            |                 | ✓                 |
| [Unicast/broadcast storm control]({{<ref "/cumulus-linux-37/Layer-2/Storm-Control" >}})                                                                  |                 | ✓                 |
| CDP                                                                                              |                 | ✓                 |

&nbsp;

| **Layer 3 Support**                                         | **Cumulus RMP** | **Cumulus Linux** |
| ----------------------------------------------------------- | --------------- | ----------------- |
| {{<kb_link text="Static routing" url="content/cumulus-linux-37/Layer-3/Routing.md" >}}        | ✓               | ✓                 |
| ECMP                                                        |                 | ✓                 |
| ECMP resilient hashing                                      |                 | ✓                 |
| OSPF                                                        |                 | ✓                 |
| BGP                                                         |                 | ✓                 |
| FRRouting                                                   |                 | ✓                 |
| BFD                                                         |                 | ✓                 |
| IPv6                                                        |                 | ✓                 |
| {{<kb_link text="Management VRF" url="content/cumulus-linux-37/Layer-3/Management-VRF.md" >}} | ✓               | ✓                 |
| Virtual routing and forwarding (VRF)                        |                 | ✓                 |

&nbsp;

| **Additional Functionality**                                                                                                     | **Cumulus RMP** | **Cumulus Linux** |
| -------------------------------------------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| [Network command line utility]({{<ref "/cumulus-linux-37/System-Configuration/Network-Command-Line-Utility-NCLU" >}})                        | ✓               | ✓                 |
| [Interface configuration & management]({{<ref "/cumulus-linux-37/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management" >}})       | ✓               | ✓                 |
| [802.1X interfaces]({{<ref "/cumulus-linux-37/Layer-1-and-Switch-Ports/802.1X-Interfaces.md" >}})                                               |                 | ✓                 |
| [Zero-touch OS install & upgrade]({{<ref "/cumulus-linux-37/Installation-Management/Zero-Touch-Provisioning-ZTP" >}})                        | ✓               | ✓                 |
| [Installation and package management]({{<ref "/cumulus-linux-37/Installation-Management" >}})                                                | ✓               | ✓                 |
| Full Linux extensibility                                                                                                         | ✓               | ✓                 |
| Network virtualization (VXLAN, EVPN, etc.)                                                                                       |                 | ✓                 |
| [Monitoring & troubleshooting]({{<ref "/cumulus-linux-37/Monitoring-and-Troubleshooting" >}})                                                | ✓               | ✓                 |
| [AAA]({{<ref "/cumulus-linux-37/System-Configuration/Authentication-Authorization-and-Accounting/LDAP-Authentication-and-Authorization" >}}) | ✓               | ✓                 |
| [ACLs / Netfilter]({{<ref "/cumulus-linux-37/System-Configuration/Netfilter-ACLs" >}})                                                       | ✓               | ✓                 |
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
