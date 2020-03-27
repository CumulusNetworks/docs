---
title: What's New
author: Cumulus Networks
weight: 5
toc: 2
draft: True
---
This document supports the Cumulus Linux 3.7 releases and describes currently available platforms and features.

## What's New in Cumulus Linux 3.7.12

Cumulus Linux 3.7.12 contains bug fixes.

Cumulus Linux 3.7.12 also includes a firmware update for Mellanox switches that addresses an issue with certain Virtium SSDs. The firmware update occurs automatically when you upgrade Cumulus Linux on a Mellanox switch and requires no user action.

## What's New in Cumulus Linux 3.7.11

Cumulus Linux 3.7.11 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms in 3.7.11

- Dell S5212F-ON (25G Trident3 X5)
- Delta AG6248C PoE (1G Helix4)
- HPE M-series SN2010M (25G Spectrum)
- Lenovo NE2580O X7 (25G Trident3)
- IBM 02JE062 (100G Spectrum)
- Penguin Arctica NX4808xxv (25G Trident3)
- Penguin Arctica NX3200c (100G Trident3 X7)

### New Features and Enhancements in 3.7.11

- Custom ECMP and LAG hashing on Mellanox switches
- DIP based multicast forwarding on Broadcom switches
- LLDPD Dot1q support
- Optimized ACL lookups on Mellanox switches for match combinations in ip6tables when VLAN subinterfaces are present
- VRRP support on layer 3 interfaces and subinterfaces that are part of a VRF, and VRRP support with EVPN (without MLAG)
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

### New Platforms in 3.7.9

- Dell S5296F-ON (25G Trident 3)
- Time-domain reflectometer (TDR) cable diagnostics

### New Features and Enhancements in 3.7.9

- IGMP Snooping over VXLAN on Mellanox switches
- QinQ single tag translation with a traditional bridge
- VLAN match support in ebtables (without SVI being defined)
- Support for non-contiguous subnet masks in IPv4 and IPv6 address rule matches (for example, 10.0.0.1/255.0.255.0)
- Multiple subnet support for a single VXLAN
- switchd: increased reliability and fixed memory leaks identified by GCC address sanitizer checks

## What's New in Cumulus Linux 3.7.8

Cumulus Linux 3.7.8 contains bug fixes and the following new transceivers:

- Mellanox 100G-PSM4 (MMS1C10-CM)
- Wave Splitter WST-QS28-CM4C-D (100G-CWDM4-OCP) and WST-QS28-CM4-C (100G CWDM4)

## What's New in Cumulus Linux 3.7.7

Cumulus Linux 3.7.7 contains bug fixes only.

## What's New in Cumulus Linux 3.7.6

Cumulus Linux 3.7.6 contains bug fixes, and the following new platform and power supply:

- Dell N3048EP-ON (1G PoE Helix4) - Depending upon the revision of the switch you have, you might not be able to install Cumulus Linux on it. For more information, read this knowledge base article.
- 48V DC PSU for the Dell Z9100-ON switch

## What's New in Cumulus Linux 3.7.5

Cumulus Linux 3.7.5 fixes an issue with EVPN centralized routing on Tomahawk and Tomahawk+ switches (RN-1353), an issue with switchd when IGMP snooping is enabled on a Broadcom switch (RN-1369) and includes additional security fixes.

Cumulus Linux 3.7.5 replaces Cumulus Linux 3.7.4 and includes all the new features and resolved issues from Cumulus Linux 3.7.4.

## What's New in Cumulus Linux 3.7.4

Cumulus Linux 3.7.4 is no longer available due to severe issues that are resolved in Cumulus Linux 3.7.5.

Cumulus Linux 3.7.4 supports one new platform, provides bug fixes, and contains several new features and improvements.

### New Platforms in 3.7.4

- FS.com N8500-48B6C (25G Tomahawk+)

### New Features and Enhancements in 3.7.4

- Virtual Router Redundancy Protocol (VRRP)
- Dynamic VRF route leaking is now supported for EVPN
- 802.1X Multi Domain Authentication (MDA) is supported for phone and PCs connected to the same port
- Multiple Dynamic Authorization Server (DAS) support
- IGMP/MLD snooping is supported over VXLAN bridges on Broadcom switches
- Ability to disable FEC on Mellanox switches
- Lightweight network virtualization (LNV) has been deprecated. The feature will be removed in Cumulus Linux 4.0. Cumulus Networks recommends you use Ethernet virtual private network (EVPN) for network virtualization.

## What's New in Cumulus Linux 3.7.3

Cumulus Linux 3.7.3 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms in 3.7.3

- Dell Z9264F-ON (100G Broadcom Tomahawk2)
- Edgecore AS7816-64X (100G Broadcom Tomahawk2)
- Edgecore AS7726-32X (100G Broadcom Trident3)
- Edgecore AS7326-56X (25G Broadcom Trident3)
- HPE SN2700M (100G Mellanox Spectrum)
- HPE SN2100M (100G Mellanox Spectrum)
- HPE SN2410M (25G Mellanox Spectrum)
- Lenovo NE0152TO (1G Broadcom Helix4) now generally available
- Penguin Arctica NX4804x (10G Broadcom Maverick)

### New Features and Enhancements in 3.7.3

- The EVPN duplicate address detection freeze option lets you freeze a duplicate address permanently or for a certain amount of time
- The Cumulus Hyperconverged Solution (HCS) supports automated integration with the Nutanix Prism Management solution and the Nutanix AHV hypervisor

## What's New in Cumulus Linux 3.7.2

Cumulus Linux 3.7.2 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms in 3.7.2

- Dell S5232F-ON (100G Trident3)
- Delta AG9032v2 (100G Trident3)
- Lenovo NE10032O (100G Tomahawk)
- Lenovo NE2572O (25G Tomahawk+) - swp1 thru swp8 support 25G speed only
- Lenovo NE0152TO (1G Helix4) - available for Early Access

### New Features and Enhancements in 3.7.2

- On Facebook Voyager, the NCLU net show transponder command output shows the Optical Signal to Noise ratio (OSNR) in the network
- Support for VRF route leaking on Mellanox switches
- Support for egress IPv6 ACL rules on Broadcom switches
- RFC 5549 support with global IPv6 peers
- EVPN duplicate address detection
- New TCAM profile for Mellanox switches (ip-acl-heavy) to support creation of 16K 3-tuple and 5-tuple IPv4 ACLs

## What's New in Cumulus Linux 3.7.1

Cumulus Linux 3.7.1 contains bug fixes only.

## What's New in Cumulus Linux 3.7.0

Cumulus Linux 3.7.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms in 3.7.0

- QCT QuantaMesh BMS T4048-IX8 (25G Trident3)
- QCT QuantaMesh BMS T7032-IX7 (100G Trident3)
- Dell S5248F-ON (25G Trident3)
- Penguin Arctica 4806XT (10G Trident 2+)

### New Features and Enhancements in 3.7.0

- Line side loopback and terminal loopback mode for Facebook Voyager troubleshooting
- Active-active OVSDB (Early Access)
- RADIUS Change of Authorization (CoA) requests
- RADIUS AAA local fallback authentication
- TACACS Plus local fallback authentication
- EVPN enhancements
- Neighbor Discovery (ND) Extended Community support
- Extended mobility support
- ECMP support for overlay networks on RIOT-capable Broadcom switches
- New NCLU commands:
- Show the version of a package
- Show the interface description (alias) for all interfaces on the switch
- Show which interfaces are in a VRF and the VNIs for VRF interfaces
- Change bond mode to IEEE 802.3ad link aggregation mode

Whether you are installing Cumulus Linux 3.7 for the first time or upgrading from an earlier version, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

To see a list of all the platforms supported in Cumulus Linux 3.7, refer to the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.