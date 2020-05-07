---
title: What's New
author: Cumulus Networks
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.2 release and lists the new platforms and features.

- For a list of all the platforms supported in Cumulus Linux 4.2, see the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 4.2, see the {{<link title="Cumulus Linux 4.1 Release Notes" text="Cumulus Linux 4.1 Release Notes">}}.
- To upgrade to Cumulus Linux 4.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.2.0

Cumulus Linux 4.2.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### New Platforms

- Dell S5224F-ON (25G Trident3 X5)
- Dell N3248P-ON (1G Trident3 X3)
- Delta AGV848v1 (25G Trident3 X5)
- Edgecore AS5835-54T (10G Trident3 X5 copper)
- Edgecore AS5835-54X (10G Trident3 X5 sfp+)
- Edgecore Qumran-MX AS5916-54XL (10G ??? )
- EdgeCore AS4610-30P (1G Helix4) Cumulus Express 
- Lenovo NE1064TO (10G Trident3 X5)
- Mellanox SN4600C: (100G Spectrum-3)
- Mellanox SN3700 (200G Spectrum-2)
- Mellanox SN3420 (25G Spectrum-2)

### New Features and Enhancements

- EVPN Multihoming
- Auto BGP
- DHCP Snooping
- Mandatory password change upon first login
- Ability to set the default password in a Binary Image File
- Ability to set the default password with an option in the ONIE-NOS-INSTALL command
- BGP Graceful Restart helper mode in FRR??
- Support 25g to 10g speed change without `switchd` restart
- Added all IPv6 router configuration variables per RFC 4861
- Added numerical keywords for EVPN route types in the `show bgp l2vpn evpn route type' command
- Set the CPU/control plane as a SPAN destination interface to mirror data plane traffic to the CPU for tcpdump capture.
- VXLAN flood suppression controls
