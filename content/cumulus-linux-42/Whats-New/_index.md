---
title: What's New
author: Cumulus Networks
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.2 release and lists new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 4.2, see the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 4.2, see the {{<link title="Cumulus Linux 4.2 Release Notes" text="Cumulus Linux 4.2 Release Notes">}}.
- To upgrade to Cumulus Linux 4.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.2

Cumulus Linux 4.2 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Mellanox SN4600C (100G Spectrum-3) - available for Early Access
- Mellanox SN3420 (25G Spectrum-2)

The following platforms are supported in Cumulus Linux 3.7 and are now supported in Cumulus Linux 4.2.

- Dell N3048EP-ON

### New Features and Enhancements

- {{<link url="Quick-Start-Guide#login-credentials" text="Mandatory cumulus user default password change">}} upon first login
- New {{<link url="Installing-a-New-Cumulus-Linux-Image#onie-installation-options" text="ONIE command line options">}} to set the *cumulus* user default password, add a license, and provide initial network configuration
- Ability to {{<link url="Installing-a-New-Cumulus-Linux-Image#edit-the-cumulus-linux-image-advanced" text="edit the Cumulus Linux image file">}}
- {{<link url="EVPN-Multihoming" text="EVPN multihoming">}}, supported on Mellanox switches, is a standards-based replacement for MLAG in data centers deploying Clos topologies - this feature is available for Early Access
- {{<link url="Border-Gateway-Protocol-BGP/#auto-bgp" text="Auto BGP">}}, which atomatically assigns ASNs to switches in a two-tier leaf and spine environment
- Ability to set the {{<link title="Network Troubleshooting#use-the-cpu-port-as-the-span-destination" text="CPU as a SPAN destination interface">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#ecmp-custom-hashing" text="ECMP">}} and {{<link url="Bonding-Link-Aggregation/#lag-custom-hashing" text="LAG">}} custom hash parameters have been moved to the `/etc/cumulus/datapath/traffic.conf` file and no longer require a `switchd` restart
- {{<link url="Policy-based-Routing" text="DSCP-based packet matching">}} in PBR rules

### Unsupported Platforms

Cumulus Networks does not support these platforms in Cumulus Linux 4.2. They are supported in Cumulus Linux 3.7, until that release reaches its end of life.

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)

The following platforms are supported in Cumulus Linux 3.7 but are not yet supported in Cumulus Linux 4.2. Cumulus Networks will add support for these platforms in a future Cumulus Linux release.

- Delta AG7648
- Edgecore AS4610-54T-B
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9
