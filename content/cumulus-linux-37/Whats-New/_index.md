---
title: What's New
author: NVIDIA
weight: 3
toc: 2
---
This document supports the Cumulus Linux 3.7 releases, and lists new platforms and features.
- For a list of open and fixed issues in Cumulus Linux 3.7, see the {{<link url="Cumulus-Linux-3.7-Release-Notes" text="Cumulus Linux 3.7 Release Notes">}}.
- To upgrade to a Cumulus Linux 3.7 release, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 3.7.16

Cumulus Linux 3.7.16 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.7.15

Cumulus Linux 3.7.15 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.7.14.2

Cumulus Linux 3.7.14.2 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.7.14

Cumulus Linux 3.7.14 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.7.13

Cumulus Linux 3.7.13 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.7.12

Cumulus Linux 3.7.12 contains bug fixes.

Cumulus Linux 3.7.12 also includes a firmware update for Mellanox switches that addresses an issue with certain Virtium SSDs. The firmware update occurs automatically when you upgrade Cumulus Linux on a Mellanox switch and requires no user action.

## What's New in Cumulus Linux 3.7.11

Cumulus Linux 3.7.11 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell S5212F-ON (25G Trident3 X5)
- Delta AG6248C PoE (1G Helix4)
- HPE M-series SN2010M (25G Spectrum)
- Lenovo NE2580O X7 (25G Trident3)
- IBM 02JE062 (100G Spectrum)
- Penguin Arctica NX4808xxv (25G Trident3)
- Penguin Arctica NX3200c (100G Trident3 X7)

### New Features and Enhancements

- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#ecmp-custom-hashing" text="Custom ECMP">}} on Mellanox switches and {{<link url="Bonding-Link-Aggregation/#lag-custom-hashing" text="LAG hashing">}}
- {{<link url="IGMP-and-MLD-Snooping/#dip-based-multicast-forwarding" text="DIP based multicast forwarding">}}
- {{<link url="Link-Layer-Discovery-Protocol/#vlan-dot1-tlv" text="LLDPD Dot1q support">}}
- Optimized ACL lookups on Mellanox switches for match combinations in ip6tables when VLAN subinterfaces are present
- {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#vrrp" text="VRRP">}} support on layer 3 interfaces and subinterfaces that are part of a VRF, and VRRP support with EVPN (without MLAG)
- New NCLU commands include:
    - net show system ztp (shows details of Zero Touch Provisioning)
    - net show system leds (shows the current state of platform LEDs on the outside of the switch)
    - net show system sensors (shows the current status of Environmental sensors)
    - net show system asic (shows the current status of ASIC utilization data)
    - net show neighbor (shows the ARP/neighbor table)

## What's New in Cumulus Linux 3.7.10

Cumulus Linux 3.7.10 contains a critical bug fix.

## What's New in Cumulus Linux 3.7.9

Cumulus Linux 3.7.9 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell S5296F-ON (25G Trident 3)

### New Features and Enhancements

- {{<link url="TDR-Cable-Diagnostics" text="Time-domain reflectometer (TDR)">}} cable diagnostics
- {{<link url="IGMP-and-MLD-Snooping" text="IGMP Snooping">}} IGMP Snooping over VXLAN on Mellanox switches
- {{<link url="Hybrid-Cloud-Connectivity-with-QinQ-and-VXLANs/#configure-single-tag-translation" text="QinQ single tag translation">}} with a traditional bridge
- {{<link url="Netfilter-ACLs/#match-on-vlan-ids-on-layer-2-interfaces" text="VLAN match support in ebtables">}} (without SVI being defined)
- Support for non-contiguous subnet masks in IPv4 and IPv6 address rule matches (for example, 10.0.0.1/255.0.255.0)
- Multiple subnet support for a single VXLAN
- switchd: increased reliability and fixed memory leaks identified by GCC address sanitizer checks

## What's New in Cumulus Linux 3.7.8

Cumulus Linux 3.7.8 contains bug fixes and the following new {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="transceivers">}}.

- Mellanox 100G-PSM4 (MMS1C10-CM)
- Wave Splitter WST-QS28-CM4C-D (100G-CWDM4-OCP) and WST-QS28-CM4-C (100G CWDM4)

## What's New in Cumulus Linux 3.7.7

Cumulus Linux 3.7.7 contains bug fixes only.

## What's New in Cumulus Linux 3.7.6

Cumulus Linux 3.7.6 contains bug fixes, and the following new platform and power supply:

- Dell N3048EP-ON (1G PoE Helix4) - Depending upon the revision of the switch you have, you might not be able to install Cumulus Linux on it. For more information, read [this knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Hardware-and-Platform-Issues/Dell-N3048EP-ON-Cumulus-Linux-Installation-Fails" >}}).
- 48V DC PSU for the Dell Z9100-ON switch

## What's New in Cumulus Linux 3.7.5

Cumulus Linux 3.7.5 fixes an issue with EVPN centralized routing on Tomahawk and Tomahawk+ switches (CM-24495), an issue with switchd when IGMP snooping is enabled on a Broadcom switch (CM-24508) and includes additional security fixes.

Cumulus Linux 3.7.5 replaces Cumulus Linux 3.7.4.

### New Platforms

- FS.com N8500-48B6C (25G Tomahawk+)

### New Features and Enhancements

- {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP#vrrp" text="Virtual Router Redundancy Protocol (VRRP)">}}
- {{<link url="Virtual-Routing-and-Forwarding-VRF/#vrf-route-leaking" text="Dynamic VRF route leaking">}} is now supported for EVPN
- {{<link url="802.1X-Interfaces" text="802.1X Multi Domain Authentication (MDA)">}} is supported for phone and PCs connected to the same port
- {{<link url="802.1X-Interfaces/#radius-change-of-authorization-and-disconnect-requests" text="Multiple Dynamic Authorization Server (DAS)">}} support
- {{<link url="IGMP-and-MLD-Snooping" text="IGMP/MLD snooping">}} is supported over VXLAN bridges on Broadcom switches
- {{<link url="Switch-Port-Attributes#fec" text="Ability to disable FEC">}} on Mellanox switches
- {{<link url="Lightweight-Network-Virtualization-Overview" text="Lightweight network virtualization (LNV)">}} has been deprecated. The feature will be removed in Cumulus Linux 4.0. Use Ethernet virtual private network (EVPN) for network virtualization.

## What's New in Cumulus Linux 3.7.4

Cumulus Linux 3.7.4 is no longer available due to issues that are resolved in Cumulus Linux 3.7.5.

## What's New in Cumulus Linux 3.7.3

Cumulus Linux 3.7.3 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell Z9264F-ON (100G Broadcom Tomahawk2)
- Edgecore AS7816-64X (100G Broadcom Tomahawk2)
- Edgecore AS7726-32X (100G Broadcom Trident3)
- Edgecore AS7326-56X (25G Broadcom Trident3)
- HPE SN2700M (100G Mellanox Spectrum)
- HPE SN2100M (100G Mellanox Spectrum)
- HPE SN2410M (25G Mellanox Spectrum)
- Lenovo NE0152TO (1G Broadcom Helix4) now generally available
- Penguin Arctica NX4804x (10G Broadcom Maverick)

### New Features and Enhancements

- The {{<link url="Ethernet-Virtual-Private-Network-EVPN#freeze-a-detected-duplicate-address" text="EVPN duplicate address detection freeze option">}} lets you freeze a duplicate address permanently or for a certain amount of time.

## What's New in Cumulus Linux 3.7.2

Cumulus Linux 3.7.2 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell S5232F-ON (100G Trident3)
- Delta AG9032v2 (100G Trident3)
- Lenovo NE10032O (100G Tomahawk)
- Lenovo NE2572O (25G Tomahawk+) - swp1 thru swp8 support 25G speed only
- Lenovo NE0152TO (1G Helix4) - available for Early Access

### New Features and Enhancements

- On Facebook Voyager, the NCLU net show transponder command output shows {{<link url="Facebook-Voyager-Optical-Interfaces" text="the Optical Signal to Noise ratio (OSNR)">}} in the network
- {{<link url="Virtual-Routing-and-Forwarding-VRF#vrf-route-leaking" text="Support for VRF route leaking">}} on Mellanox switches
- Support for {{<link url="Netfilter-ACLs/#supported-rule-types" text="egress IPv6 ACL rules">}} on Broadcom switches
- {{<link url="Border-Gateway-Protocol-BGP/#rfc-5549-support-with-global-ipv6-peers-cumulus-linux-372-and-later" text="RFC 5549 support with global IPv6 peers">}}
- {{<link url="Ethernet-Virtual-Private-Network-EVPN/#duplicate-address-detection" text="EVPN duplicate address detection">}}
- New TCAM profile for Mellanox switches {{<link url="/Netfilter-ACLs/#mellanox-spectrum-limits" text="(ip-acl-heavy)">}} to support creation of 16K 3-tuple and 5-tuple IPv4 ACLs

## What's New in Cumulus Linux 3.7.1

Cumulus Linux 3.7.1 contains bug fixes only.

## What's New in Cumulus Linux 3.7.0

Cumulus Linux 3.7.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- QCT QuantaMesh BMS T4048-IX8 (25G Trident3)
- QCT QuantaMesh BMS T7032-IX7 (100G Trident3)
- Dell S5248F-ON (25G Trident3)
- Penguin Arctica 4806XT (10G Trident 2+)

### New Features and Enhancements

- {{<link url="Facebook-Voyager-Optical-Interfaces/#configure-a-line-side-loopback" text="Line side loopback and terminal loopback mode">}} for Facebook Voyager troubleshooting
- {{<link url="802.1X-Interfaces/#radius-change-of-authorization-and-disconnect-requests" text="RADIUS Change of Authorization (CoA) requests">}}
- {{<link url="RADIUS-AAA/#local-fallback-authentication" text="RADIUS AAA local fallback authentication">}}
- {{<link url="TACACS-Plus/#local-fallback-authentication" text="TACACS Plus local fallback authentication">}}
- EVPN enhancements
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN#support-for-evpn-neighbor-discovery-nd-extended-community" text="Neighbor Discovery (ND) Extended Community support">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#extended-mobility" text="Extended mobility support">}}
    - ECMP support for overlay networks on RIOT-capable Broadcom switches
- New NCLU commands:
    - {{<link url="Adding-and-Updating-Packages/#display-the-version-of-a-package" text="Show the version of a package">}}
    - {{<link url="Interface-Configuration-and-Management/#add-descriptions-to-interfaces" text="Show the interface description (alias) for all interfaces on the switch">}}
    - {{<link url="Virtual-Routing-and-Forwarding-VRF/#show-vrf-information" text="Show which interfaces are in a VRF and the VNIs for VRF interfaces">}}
    - {{<link url="Bonding-Link-Aggregation" text="Change bond mode to IEEE 802.3ad link aggregation mode">}}
