---
title: What's New
author: Cumulus Networks
weight: 5
toc: 2
draft: True
---
This document supports the Cumulus Linux 4.1 release and lists the new platforms and features.

## What's New in Cumulus Linux 4.1.0

Cumulus Linux 4.1.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

To see a list of all the platforms supported in Cumulus Linux 4.1.0, refer to the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.

To upgrade to Cumulus Linux 4.1.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

### New Platforms

- Dell 5212F-ON (25G Trident3 X5)
- Mellanox SN2010 with 32G RAM (25G Spectrum)

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
- New NCLU commands: `net show neighbors`, `net show sensor output`, `net show system leds`
