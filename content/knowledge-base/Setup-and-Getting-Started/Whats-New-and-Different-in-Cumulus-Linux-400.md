---
title: What's New and Different in Cumulus Linux 4.0.0
author: Cumulus Networks
weight: 107
toc: 3
---

Cumulus Linux 4.0.0 is the biggest update to the operating system in years\! We've changed many things both cosmetic and under the hood, including a new kernel and several new platforms — but we've also removed some platforms and features — so it's a good idea for you to understand all that's changed **before** you upgrade.

As always, please read the {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Whats-New/rn/" text="release notes">}} to learn about all the open and fixed issues in this release.

**For more recent releases, you can always get the latest Cumulus Linux information {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Whats-New/" text="here">}}.**

## What's New and Different in Cumulus Linux 4.0.0?

Cumulus Linux 4.0.0 supports the following new platforms, new features, and enhancements.

New platforms include:

- EdgeCore Minipack AS8000 (100G Tomahawk3)
- Mellanox SN3700C (100G Spectrum-2)
- Mellanox SN3700 (200G Spectrum-2)
  - Note that Cumulus Linux 4.0.0 currently supports 100G speeds
- HPE SN2745M (100G Spectrum)

New features and enhancements include:

- Cumulus Linux is now based on Debian Buster (version 10) with a 4.19 kernel
  - In this kernel, {{<link url="Spectre-and-Meltdown-Vulnerability-Fixes" text="Meltdown/Spectre fixes">}} are all fully up to date
- Capability to `apt-get upgrade` to a specific 4.y.z release, not just the latest version (for use in future Cumulus 4.0.z releases)
- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-PIM/" text="EVPN BUM traffic handling">}} using PIM-SM on  Broadcom switches
- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-3/Protocol-Independent-Multicast-PIM/#pim-active-active-with-mlag" text="PIM active-active with MLAG">}}
- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-1-and-Switch-Ports/Port-Security/" text="Port security">}} on Broadcom switches
- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH/" text="What Just Happened">}} (WJH) for Mellanox switches to stream detailed and contextual telemetry for off-box analysis with tools such as Cumulus NetQ
- A new {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Installation-Management/Back-up-and-Restore/" text="backup and restore utility">}}
- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing/#advertise-primary-ip-address" text="Advertise primary IP address type-5 routes">}} in an EVPN symmetric configuration in VXLAN active-active mode
- {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-3/Border-Gateway-Protocol-BGP/" text="BGP best path reason">}} shown in command outputs
- On Mellanox switches, certain {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-1-and-Switch-Ports/Buffer-and-Queue-Management/" text="buffer and queue configuration settings">}} no longer require `switchd` restart
- The {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-3/FRRouting-Overview/" text="FRRouting">}} `daemons` and `daemons.conf` files have been merged together into the `daemons` file, which may affect your automation scripts
- The NetQ agent and CLI are installed by default in Cumulus Linux; these packages are also present in the `apt.cumulusnetworks.com` repository and are updated as new versions of NetQ become available
- The following files have been added to the Cumulus Linux base image:
  - `bwm-ng`
  - `dos2unix`
  - `mtr-tiny`
- The following default settings have changed:
  - {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-3/Management-VRF/" text="Management VRF">}} is enabled by default
    - The management VRF must have both an IPv6 address and an IPv4 address to work correctly; the default IP address is ::1/128
  - {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Layer-3/Configuring-FRRouting/" text="Zebra">}}
    is enabled by default in the `daemons` file
  - {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration/#arp-and-nd-suppression" text="ARP/ND suppression">}} is enabled by default on all VXLAN interfaces
  - {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration/" text="MAC learning">}} is disabled by default on all VXLAN bridge ports
  - On Broadcom switches, the default value for `route_preferred_over_neigh` in `/etc/cumulus/switchd.conf` is now TRUE
- A {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-40/Installation-Management/Adding-and-Updating-Packages/#add-packages-from-the-cumulus-linux-local-archive" text="local archive">}} is now embedded in the Cumulus Linux disk image that contains the packages required to install ifplugd, LDAP, RADIUS or TACACS+ without needing a network connection; the archive is called `cumulus-local-apt-archive` and is referenced in the `/etc/apt/cumulus-local-apt-archive-sources.list` file
- The `apps` repository has been removed
- The following tools/commands have changed:
  - `vim` is now installed instead of `vim-tiny`
  - `rasdaemon` has replaced `mcelog`
  - The `date` command has changed from 24 hour time to 12 hour AM/PM and European-style day, month, year
  - Old ciphers, such as SHA-1, are no longer supported for SSH and SSL

## Currently Supported Platforms

The following list identifies all the platforms supported in Cumulus Linux 4.0.0. Note that some platforms that are supported in 3.7.z may not appear here, but will be back in a future release if they are still supported (see the list of platforms that are no longer supported below).

- 100G
    - Dell S5232F-ON
    - Dell Z9264F-ON
    - Edgecore AS7816-64X
    - Edgecore AS7726-32X
    - EdgeCore Minipack AS8000
    - HPE SN2745M
    - Lenovo NE10032O
    - Mellanox SN2700
    - Mellanox SN3700
    - Mellanox SN3700C
    - QCT QuantaMesh BMS T7032-IX1
    - QCT QuantaMesh BMS T7032-IX7
- 40G  
    - Dell S6010-ON
    - Edgecore AS6812-32X
    - Edgecore AS6712-32X
-  25G
    - Dell S5248F-ON
    - Dell S5296F-ON
    - Delta AG-5648v1
    - Edgecore AS7326-56X
    - Fiberstore N8500-48B6C
    - Lenovo NE2572O
    - Mellanox SN2410
    - QCT QuantaMesh BMS T4048-IX8
- 10G
    - Dell S4048-ON
    - Edgecore AS5812-54T
    - Edgecore AS5812-54X
    - Penguin Arctica NX4804x
- 1G
    - Dell S3048-ON
    - Lenovo NE0152TO

## Platforms No Longer Supported

Cumulus Networks does not support these platforms in Cumulus Linux 4.0.0 (they are still supported in Cumulus Linux 3.7.z until that version reaches its end of life). Do **not** install Cumulus Linux 4.0.0 on any of these platforms as it will not run correctly:

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- EdgeCore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)

## Platforms Supported under Cumulus Linux 3.7.z but not Currently Supported

The following platforms are supported on Cumulus Linux 3.7.z but are not supported yet in Cumulus Linux 4.0. Support for these platforms will return at some point during the version 4.y.z release cycle.

- Dell N3048EP-ON
- Dell S4128F-ON
- Dell S4128T-ON
- Dell S4148F-ON
- Dell S4148T-ON
- Dell S5048F-ON
- Dell Z9100-ON
- Delta AG7648
- Delta AG9032v1
- Delta AG9032v2
- Edgecore AS4610-54P
- Edgecore AS4610-54T
- Edgecore AS4610-54T-B
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
- QCT QuantaMesh T1048-LY4R
- QCT QuantaMesh BMS T5032-LY6-x86
- QCT QuantaMesh BMS T3048-LY7
- QCT QuantaMesh BMS T3048-LY8
- QCT QuantaMesh BMS T3048-LY9
- SuperMicro SSE-C3632S
- SuperMicro SSE-G3648B
- SuperMicro SSE-X3648S

## Features Removed

- LNV is no longer included in Cumulus Linux
