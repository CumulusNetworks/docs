---
title: What's New
author: Cumulus Networks
weight: 5
toc: 2
draft: True
---
This document supports the Cumulus Linux 4.0 release and lists the new platforms and features.

- For complete details on the differences between Cumulus Linux 4.0 and Cumulus Linux 3.7, see the {{<exlink url="https://support.cumulusnetworks.com/hc/en-us/articles/360038231814" text="this article">}}.
- For a list of all the platforms supported in Cumulus Linux 4.0, see the {{<exlink url="https://cumulusnetworks.com/products/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- To upgrade to Cumulus Linux 4.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.0.0

Cumulus Linux 4.0.0 supports new platforms, provides bug fixes, and contains several new features and improvements:

### New Platforms

- EdgeCore Minipack AS8000 (100G Tomahawk3)
- Mellanox SN3700C (100G Spectrum-2)
- Mellanox SN3700 (200G Spectrum-2): Cumulus Linux 4.0.0 currently supports 100G speed
- HPE SN2745M (100G Spectrum)

### New Features and Enhancements

- The Cumulus Linux operating system is now based on Debian Buster (version 10) with a 4.19 kernel.
- Capability to apt-get upgrade to a specific 4.x.y release, not just the latest (for use in future Cumulus 4.0.x releases)
- {{<link url="EVPN-BUM-Traffic-with-PIM-SM" text="EVPN BUM traffic handling using PIM-SM">}} on Broadcom switches
- {{<link url="Protocol-Independent-Multicast-PIM#pim-active-active-with-mlag" text="PIM active-active with MLAG">}}
- {{<link url="Port-Security" text="Port security">}} on Broadcom switches
- {{<link title="Mellanox What Just Happened (WJH)" text="What Just Happened WJH">}} for Mellanox switches to stream detailed and contextual telemetry for off-box analysis with tools such as NetQ
- {{<link url="Back-up-and-Restore" text="New backup and restore utility">}}
- {{<link url="Inter-subnet-Routing#advertise-primary-ip-address-vxlan-active-active-mode" text="Advertise Primary IP Address for type-5 routes">}} in EVPN symmetric deployments (VXLAN active-active mode)
- {{<link url="Border-Gateway-Protocol-BGP" text="BGP">}} best path reason shown in command outputs
- The following default settings have changed:
    - {{<link url="Management-VRF" text="Management VRF">}} is enabled by default
    - {{<link url="Basic-Configuration" text="ARP/ND suppression">}} is enabled by default on all VXLAN interfaces
    - {{<link url="Basic-Configuration" text="MAC learning">}} is disabled by default on all VXLAN bridge ports
