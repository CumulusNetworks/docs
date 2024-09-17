---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.1 releases, and lists new platforms and features.
- For a list of open and fixed issues in Cumulus Linux 4.1, see the {{<link url="Cumulus-Linux-4.1-Release-Notes" text="Cumulus Linux 4.1 Release Notes">}}.
- To upgrade to Cumulus Linux 4.1, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.1.1

Cumulus Linux 4.1.1 contains security bug fixes.

## What's New in Cumulus Linux 4.1.0

Cumulus Linux 4.1.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell 5212F-ON (25G Trident3 X5)
- Mellanox SN2010 with 32G RAM (25G Spectrum)

The following platforms are supported in Cumulus Linux 3.7 and are now supported in Cumulus Linux 4.1:

- Dell S4128F-ON
- Dell S4128T-ON
- Dell S4148F-ON
- Dell S4148T-ON
- Dell Z9100-ON
- Dell S5048F-ON
- Delta AG9032v1
- Delta AG9032v2
- Edgecore AS4610-54P
- Edgecore AS4610-54T
- Edgecore AS5712-54X
- Edgecore AS7312-54XS
- Edgecore AS7712-32X
- Mellanox SN2010
- Mellanox SN2100
- Penguin Arctica 3200xlp
- Penguin Arctica 4804ip
- Penguin Arctica 4804iq
- Penguin Arctica 4806xp
- QCT QuantaMesh BMS T4048-IX2
- QCT QuantaMesh BMS T5032-LY6-x86
- QCT QuantaMesh BMS T3048-LY7
- SuperMicro SSE-C3632S
- SuperMicro SSE-G3648B
- SuperMicro SSE-X3648S

### New Features and Enhancements

- {{<link url="Network-Address-Translation-NAT" text="Static and dynamic NAT">}}
- {{<link url="EVPN-Enhancements/#disable-bum-flooding" text="Configuration to disable EVPN flooding">}}
- {{<link url="802.1X-Interfaces/#dynamic-acls" text="Dynamic access control lists for 802.1X interfaces at the port level">}}
- {{<link url="Unequal-Cost-Multipath-with-BGP-Link-Bandwidth" text="Unequal Cost Multipath (UCMP) with BGP link bandwidth">}}
- {{<link url="Buffer-and-Queue-Management#syntax-checker" text="Syntax checker">}} for the /etc/cumulus/datapath/traffic.conf file
- {{<link url="Port-Security" text="Port security">}} also now supported on Mellanox switches
- {{<link url="EVPN-BUM-Traffic-with-PIM-SM" text="EVPN PIM">}} also now supported on Mellanox switches
- {{<link url="Switch-Port-Attributes#breakout-ports" text="Port breakout configuration">}} without restarting `switchd` on Mellanox switches
- Custom layer 2 RASH heavy profiles available on Mellanox switches
- {{<link url="Static-VXLAN-Tunnels#control-link-local-multicast-across-a-static-vxlan-tunnel" text="Control link-local multicast">}} across a static VXLAN tunnel
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP#ipv6-route-replacement" text="IPv6 route replacement option">}} to maintain resilient hashing for IPv6 flows
- {{<link url="VLAN-aware-Bridge-Mode/#reserved-vlan-range" text="Default reserved VLAN range">}} reduced to 3600-3999
- The default {{<link url="Switch-Port-Attributes/#mtu" text="MTU">}} has changed to 9216 from 1500
- New NCLU commands: `net show neighbors`, `net show sensor output`, `net show system leds` `net show system asic`, `net show system ztp`

### Unsupported Platforms

These platforms are not supported in Cumulus Linux 4.1. They are supported in Cumulus Linux 3.7 until that release reaches its end of life.

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)

The following platforms are supported in Cumulus Linux 3.7 but are not yet supported in Cumulus Linux 4.1. Support for these platforms will be added in a future Cumulus Linux release.

- Delta AG7648
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9
