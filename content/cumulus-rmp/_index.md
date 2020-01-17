---
title: Cumulus RMP
author: Cumulus Networks
weight: -37
aliases:
 - /display/RMP/Cumulus-RMP
 - /display/RMP/Cumulus+RMP
 - /display/RMP/
 - /pages/viewpage.action?pageId=5122807
pageID: 5122807
product: Cumulus RMP
version: '3.7'
siteSlug: cumulus-rmp
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

You can also find more information about Cumulus RMP
[here](https://cumulusnetworks.com/products/cumulus-rack-management-platform/).

{{ <img src="/images/old_doc_images/RMP.png" >}}

## What's New in Cumulus RMP

{{%notice note%}}

Starting with Cumulus Linux 4.0.0, the Cumulus RMP uses the same binary image as Cumulus Linux.

{{%/notice%}}

Cumulus RMP 3.7.0 contains several bug fixes and the following new
features:

- [RADIUS Change of Authorization (CoA) requests](/cumulus-linux/Layer-1-and-Switch-Ports/802.1X-Interfaces/#radius-change-of-authorization-and-disconnect-requests)
- [RADIUS AAA local fallback authentication](/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/RADIUS-AAA/#local-fallback-authentication)
- [TACACS+ local fallback authentication](/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/TACACS+/#local-fallback-authentication)
- New NCLU commands:
  - [Show the version of a package](/cumulus-linux/Installation-Management/Adding-and-Updating-Packages/#display-the-version-of-a-package)
  - [Show the interface description (alias)](/cumulus-linux/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/#add-descriptions-to-interfaces)
        for all interfaces on the switch
  - [Change bond mode to IEEE 802.3ad](/cumulus-linux/Layer-2/Bonding-Link-Aggregation/) link
        aggregation mode

For further information regarding bug fixes and known issues present in
the 3.7 release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360009508373-Cumulus-RMP-3-7-Release-Notes).

### What's New in Cumulus RMP 3.6.2

Cumulus RMP 3.6.2 contains several bug fixes and the following new
feature:

- NCLU commands available for [configuring traditional mode bridges](/cumulus-linux/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode/)

For further information regarding bug fixes and known issues present in
the 3.6.2 release, refer to the 
[product release notes](https://support.cumulusnetworks.com/hc/en-us/articles/360003646974-Cumulus-RMP-3-6-Release-Notes).

### What's New in Cumulus RMP 3.6.0

Cumulus RMP 3.6.0 contains several bug fixes and the following new
feature:

- Support for a combination of `local-as` and `allowas-in` commands

For further information regarding bug fixes and known issues present in
the 3.6.0 release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360003646974-Cumulus-RMP-3-6-Release-Notes).

## Cumulus RMP Features

Cumulus RMP shares much of the same functionality as Cumulus Linux and
comes preinstalled on your choice of
[1G switches](https://cumulusnetworks.com/products/hardware-compatibility-list/?platform_type%5B0%5D=RMP).
For more information about each feature, follow the links below to the
[Cumulus Linux user guide](/cumulus-linux):

| **Layer 2 Support** | **Cumulus RMP**  | **Cumulus Linux**  |
| ------------------- | ---------------- | ------------------ |
| [LLDP](/cumulus-linux/Layer-2/Link-Layer-Discovery-Protocol/) | ✓     | ✓  |
| [PTM](/cumulus-linux/Layer-1-and-Switch-Ports/Prescriptive-Topology-Manager-PTM/)  | ✓  | ✓  |
| [Ethernet bridging](/cumulus-linux/Layer-2/Ethernet-Bridging-VLANs/)       | ✓ | ✓ |
| [Bonds/link aggregation](/cumulus-linux/Layer-2/Bonding-Link-Aggregation/)    | ✓     | ✓ |
| MLAG | | ✓  |
| LACP         | ✓               | ✓                 |
| LACP bypass |                 | ✓                 |
| [Spanning tree protocol/RST](/cumulus-linux/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/)  | ✓  | ✓   |
| [802.1Q VLAN tagging](/cumulus-linux/Layer-2/Ethernet-Bridging-VLANs/VLAN-Tagging/) | ✓  | ✓  |
| [VLAN-aware bridging](/cumulus-linux/Layer-2/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode/)  | ✓     | ✓  |
| [BPDU guard](/cumulus-linux/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/)   | ✓  | ✓  |
| [Bridge assurance](/cumulus-linux/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/)   | ✓  | ✓  |
| [BPDU filter](/cumulus-linux/Layer-2/Spanning-Tree-and-Rapid-Spanning-Tree/)   | ✓  | ✓   |
| VRR | | ✓ |
| IGMP and MLD snooping |    | ✓   |
| Unicast/broadcast storm control |  | ✓   |
| CDP | |  ✓                 |

&nbsp;

| **Layer 3 Support**    | **Cumulus RMP**  | **Cumulus Linux**  |
| ---------------------- | --------------- | ----------------- |
| [Static routing](/cumulus-linux/Layer-3/Routing/)    | ✓ | ✓   |
| ECMP | | ✓  |
| ECMP resilient hashing |                 | ✓                 |
| OSPF  |                 | ✓                 |
| BGP  |                 | ✓                 |
| FRRouting |                 | ✓                 |
| BFD   |                 | ✓                 |
| IPv6  |                 | ✓                 |
| [Management VRF](/cumulus-linux/Layer-3/Management-VRF/) | ✓   | ✓  |
| Virtual routing and forwarding (VRF)  |  | ✓                 |

&nbsp;

| **Additional Functionality**  | **Cumulus RMP** | **Cumulus Linux** |
| ----------------------------- | --------------- | ----------------- |
| [Network command line utility](/cumulus-linux/System-Configuration/Network-Command-Line-Utility-NCLU/)            | ✓               | ✓                 |
| [Interface configuration & management](/cumulus-linux/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/) | ✓               | ✓                 |
| [802.1X interfaces](/cumulus-linux/Layer-1-and-Switch-Ports/802.1X-Interfaces/) |   | ✓  |
| [Zero-touch OS install & upgrade](/cumulus-linux/Installation-Management/Zero-Touch-Provisioning-ZTP/)               | ✓               | ✓                 |
| [Installation and package management](/cumulus-linux/Installation-Management/) | ✓  | ✓  |
| Full Linux extensibility | ✓  | ✓  |
| Network virtualization (VXLAN, EVPN, etc.) |   |  ✓  |
| [Monitoring & troubleshooting](/cumulus-linux/Monitoring-and-Troubleshooting/)  | ✓  | ✓   |
| [AAA](/cumulus-linux/System-Configuration/Authentication-Authorization-and-Accounting/LDAP-Authentication-and-Authorization/)  | ✓  | ✓  |
| [ACLs](/cumulus-linux/System-Configuration/Netfilter-ACLs/)  | ✓  | ✓ |
| QoS |                 | ✓                 |
| [Orchestration](/cumulus-linux/Installation-Management/Upgrading-Cumulus-Linux/) | ✓  | ✓  |

## Setting up a Cumulus RMP Switch

The [quick start guide](/cumulus-rmp/Quick-Start-Guide) walks you
through the steps necessary for getting your Cumulus RMP switch up and
running after you remove it from the box.

## Caveats and Errata

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
