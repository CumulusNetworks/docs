---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 4.0 release, and lists new platforms and features.

- For complete details on the differences between Cumulus Linux 4.0 and Cumulus Linux 3.7, see [this article]({{<ref "/knowledge-base/Setup-and-Getting-Started/Whats-New-and-Different-in-Cumulus-Linux-400" >}}).
- For a list of open and fixed issues in Cumulus Linux 4.0, see the {{<link url="Cumulus-Linux-4.0-Release-Notes" text="Cumulus Linux 4.0 Release Notes">}}.
- To upgrade to Cumulus Linux 4.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 4.0

Cumulus Linux 4.0 supports new platforms, provides bug fixes, and contains several new features and improvements:

### New Platforms

- EdgeCore Minipack AS8000 (100G Tomahawk3) - Cumulus Linux supports this switch in the SPINE network role only.
- Mellanox SN3700C (100G Spectrum-2)
- Mellanox SN3700 (200G Spectrum-2): Cumulus Linux 4.0 currently supports 100G speed
- HPE SN2745M (100G Spectrum)

### New Features and Enhancements

- The Cumulus Linux operating system is now based on Debian Buster (version 10) with a 4.19 kernel.
- Capability to apt-get upgrade to a specific 4.x.y release, not just the latest (for use in future Cumulus Linux releases)
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

### Unsupported Features

- Lightweight network virtualization (LNV); see {{<link url="Migrating-from-LNV-to-EVPN" text="Migrating from LNV to EVPN">}}
- Static VRF route leaking
- Snapshots

### Unsupported Platforms

These platforms are not supported in Cumulus Linux 4.0. They are supported in Cumulus Linux 3.7 until that release reaches its end of life.

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)

The following platforms are supported in Cumulus Linux 3.7 but are not yet supported in Cumulus Linux 4.0. These platforms will be supported in a future Cumulus Linux release.

#### Dell Platforms
- Dell S4128F-ON
- Dell S4128T-ON
- Dell S4148F-ON
- Dell S4148T-ON
- Dell S5048F-ON
- Dell Z9100-ON

#### Delta Platforms

- Delta AG7648
- Delta AG9032v1
- Delta AG9032v2

#### Edgecore Platforms

- Edgecore AS4610-54P
- Edgecore AS4610-54T
- Edgecore AS4610-54T-B
- Edgecore AS5712-54X
- Edgecore AS7312-54XS
- Edgecore AS7712-32X

#### Mellanox Platforms

- Mellanox SN2010
- Mellanox SN2100

#### Penguin Platforms

- Penguin Arctica 3200xlp
- Penguin Arctica 4804ip
- Penguin Arctica 4804iq
- Penguin Arctica 4806xp

#### Quanta Platforms

- QCT QuantaMesh BMS T4048-IX2
- QCT QuantaMesh T1048-LY4R
- QCT QuantaMesh BMS T5032-LY6-x86
- QCT QuantaMesh BMS T3048-LY7
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9

#### Supermicro Platforms

- SuperMicro SSE-C3632S
- SuperMicro SSE-G3648B
- SuperMicro SSE-X3648S
