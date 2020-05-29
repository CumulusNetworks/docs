---
title: What's New
author: Cumulus Networks
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.2 release and lists the new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 4.2, see the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 4.2, see the {{<link title="Cumulus Linux 4.2 Release Notes" text="Cumulus Linux 4.2 Release Notes">}}.
- To upgrade to Cumulus Linux 4.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.2.0

Cumulus Linux 4.2.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell S5224F-ON (25G Trident3 X5)
- Dell N3248P-ON (1G Trident3 X3)
- Delta AGV848v1 (25G Trident3 X5)
- Edgecore AS5835-54T (10G Trident3 X5)
- Edgecore AS5835-54X (10G Trident3 X5)
- EdgeCore AS4610-30P (1G Helix4) Cumulus Express
- EdgeCore AS4610-30P (24 port POE+) support
- Lenovo NE1064TO (10G Trident3 X5)
- GMS S422-SW (10G (Maverick))
- Mellanox SN4700C: (400G Spectrum-3)
- Mellanox SN4600C (100G Spectrum-3)
- Mellanox SN3420 (25G Spectrum-2)

### New Features and Enhancements

- EVPN Multihoming
- Auto BGP
- DHCP Snooping
- {{<link url="Quick-Start-Guide#login-credentials" text="Mandatory cumulus user default password change">}} upon first login
- Ability to set the *cumulus* user default password, add a license, and provide initial network configuration with {{<link url="Installing-a-New-Cumulus-Linux-Image#onie-installation-options" text="ONIE command line options">}}
- Ability to {{<link url="Installing-a-New-Cumulus-Linux-Image#edit-the-cumulus-linux-image-advanced" text="edit the Cumulus Linux image file">}}
- New Ninja profile on Mellanox switches
- Support 25g to 10g speed change without `switchd` restart
- Ability to set the CPU/control plane as a SPAN destination interface
- VXLAN flood suppression controls
- QoS now supported on Maverick
- Added all IPv6 router configuration variables per RFC 4861
- Added numerical keywords for EVPN route types in the `show bgp l2vpn evpn route type' command
