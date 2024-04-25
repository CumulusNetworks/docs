---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.2 release, and lists new platforms and features.
- For a list of open and fixed issues in Cumulus Linux 4.2, see the {{<link title="Cumulus Linux 4.2 Release Notes" text="Cumulus Linux 4.2 Release Notes">}}.
- To upgrade to Cumulus Linux 4.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.2.1

Cumulus Linux 4.2.1 supports a new platform, provides bug fixes, and contains certain enhancements.

### New Platforms

- Mellanox SN4700 (Spectrum-3-A0)

### Enhancements

- The Mellanox SN3700 Spectrum-2 switch now supports 200G (100G was supported previously)
- {{<link url="EVPN-Multihoming" text="EVPN multihoming">}} is now generally available on Mellanox switches
- {{<link url="Virtual-Routing-and-Forwarding-VRF/#vrf-route-leaking" text="Inter-VRF route leaking">}} is now ASIC accelerated by default

## What's New in Cumulus Linux 4.2.0

Cumulus Linux 4.2.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Mellanox SN4600C (100G Spectrum-3-A0)
- Mellanox SN3420 (25G Spectrum-2)

### New Features and Enhancements

- {{<link url="EVPN-Multihoming" text="EVPN multihoming">}}, supported on Mellanox switches, is a standards-based replacement for MLAG in data centers deploying Clos topologies - this feature is available for Early Access
- {{<link url="Border-Gateway-Protocol-BGP/#auto-bgp" text="Auto BGP">}}, which automatically assigns ASNs to switches in a two-tier leaf and spine environment
- {{<link url="Quick-Start-Guide#login-credentials" text="Mandatory cumulus user default password change">}} upon first login
- New {{<link url="Installing-a-New-Cumulus-Linux-Image#onie-installation-options" text="ONIE command line options">}} to set the *cumulus* user default password, add a license, and provide initial network configuration
- Ability to {{<link url="Installing-a-New-Cumulus-Linux-Image#edit-the-cumulus-linux-image-advanced" text="edit the Cumulus Linux image file">}}
- Ability to set the {{<link title="Network Troubleshooting#use-the-cpu-port-as-the-span-destination" text="CPU as a SPAN destination interface">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#ecmp-custom-hashing" text="ECMP">}} and {{<link url="Bonding-Link-Aggregation/#lag-custom-hashing" text="LAG">}} custom hash parameters have been moved to the `/etc/cumulus/datapath/traffic.conf` file and no longer require a `switchd` restart
- {{<link url="Policy-based-Routing" text="DSCP-based packet matching">}} in PBR rules
- {{<link title="Buffer and Queue Management" text="Link pause and priority flow control">}} are now supported on the Edgecore Minipack-AS8000

### Unsupported Platforms

These platforms are not supported in Cumulus Linux 4.2. They are supported in Cumulus Linux 3.7, until that release reaches its end of life.

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)
- Delta AG7648
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9
