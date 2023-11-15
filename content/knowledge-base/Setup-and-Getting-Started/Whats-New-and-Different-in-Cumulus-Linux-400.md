---
title: What's New and Different in Cumulus Linux 4.0.0
author: NVIDIA
weight: 107
toc: 3
---
<!-- vale off -->
Cumulus Linux 4.0.0 is the biggest update to the operating system in years! This version has many changes, both cosmetic and under the hood, including a new kernel and several new platforms &mdash; but we've also removed some platforms and features &mdash; so it is a good idea for you to understand everything that changed **before** you upgrade.
<!-- vale on -->
As always, read the [release notes]({{<ref "/cumulus-linux-40/Whats-New/rn" >}}) to learn about all the open and fixed issues in this release.

**For more recent releases, you can always get the latest Cumulus Linux information [here]({{<ref "/cumulus-linux-40/Whats-New" >}}).**
<!-- vale off -->
## What's New and Different in Cumulus Linux 4.0.0?
<!-- vale on -->
Cumulus Linux 4.0.0 supports the following new platforms, new features, and enhancements.

New platforms include:

- Edgecore Minipack AS8000 (100G Tomahawk3)
- NVIDIA Spectrum SN3700C (100G Spectrum-2)
- NVIDIA Spectrum SN3700 (200G Spectrum-2)
  - Note that Cumulus Linux 4.0.0 currently supports 100G speeds
- HPE SN2745M (100G Spectrum)

New features and enhancements include:
<!-- vale off -->
- Cumulus Linux is now based on Debian Buster (version 10) with a 4.19 kernel
  - In this kernel, {{<link url="Spectre-and-Meltdown-Vulnerability-Fixes" text="Meltdown/Spectre fixes">}} are all fully up to date
- Capability to `apt-get upgrade` to a specific 4.y.z release, not just the latest version (for use in future Cumulus 4.0.z releases)
- [EVPN BUM traffic handling]({{<ref "/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/EVPN-PIM" >}}) using PIM-SM on  Broadcom switches
- [PIM active-active with MLAG]({{<ref "/cumulus-linux-40/Layer-3/Protocol-Independent-Multicast-PIM#pim-active-active-with-mlag" >}})
- [Port security]({{<ref "/cumulus-linux-40/Layer-1-and-Switch-Ports/Port-Security" >}}) on Broadcom switches
- [What Just Happened]({{<ref "/cumulus-linux-40/Monitoring-and-Troubleshooting/Network-Troubleshooting/Mellanox-WJH" >}}) (WJH) for NVIDIA Spectrum switches to stream detailed and contextual telemetry for off-box analysis with tools such as NVIDIA NetQ
- A new [backup and restore utility]({{<ref "/cumulus-linux-40/Installation-Management/Back-up-and-Restore" >}})
- [Advertise primary IP address type-5 routes]({{<ref "/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Inter-subnet-Routing#advertise-primary-ip-address" >}}) in an EVPN symmetric configuration in VXLAN active-active mode
- [BGP best path reason]({{<ref "/cumulus-linux-40/Layer-3/Border-Gateway-Protocol-BGP" >}}) shown in command outputs
- On NVIDIA Spectrum switches, certain [buffer and queue configuration settings]({{<ref "/cumulus-linux-40/Layer-1-and-Switch-Ports/Buffer-and-Queue-Management" >}}) no longer require `switchd` restart
- The [FRRouting]({{<ref "/cumulus-linux-40/Layer-3/FRRouting-Overview" >}}) `daemons` and `daemons.conf` files have been merged together into the `daemons` file, which may affect your automation scripts
- The NetQ agent and CLI are installed by default in Cumulus Linux; these packages are also present in the `apt.cumulusnetworks.com` repository and are updated as new versions of NetQ become available
- The following files have been added to the Cumulus Linux base image:
  - `bwm-ng`
  - `dos2unix`
  - `mtr-tiny`
- The following default settings have changed:
  - [Management VRF]({{<ref "/cumulus-linux-40/Layer-3/Management-VRF" >}}) is enabled by default
    - The management VRF must have both an IPv6 address and an IPv4 address to work correctly; the default IP address is ::1/128
  - [Zebra]({{<ref "/cumulus-linux-40/Layer-3/Configuring-FRRouting" >}})
    is enabled by default in the `daemons` file
  - [ARP/ND suppression]({{<ref "/cumulus-linux-40/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration#arp-and-nd-suppression" >}}) is enabled by default on all VXLAN interfaces
  - [MAC learning]({{<ref "/cumulus-linux-43/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/Basic-Configuration" >}}) is disabled by default on all VXLAN bridge ports
  - On Broadcom switches, the default value for `route_preferred_over_neigh` in `/etc/cumulus/switchd.conf` is now TRUE
- A [local archive]({{<ref "/cumulus-linux-40/Installation-Management/Adding-and-Updating-Packages#add-packages-from-the-cumulus-linux-local-archive" >}}) is now embedded in the Cumulus Linux disk image that contains the packages required to install ifplugd, LDAP, RADIUS or TACACS+ without needing a network connection; the archive is called `cumulus-local-apt-archive` and is referenced in the `/etc/apt/cumulus-local-apt-archive-sources.list` file
- The `apps` repository has been removed
- The following tools/commands have changed:
  - `vim` is now installed instead of `vim-tiny`
  - `rasdaemon` has replaced `mcelog`
  - The `date` command has changed from 24 hour time to 12 hour AM/PM and European-style day, month, year
  - Old ciphers, such as SHA-1, are no longer supported for SSH and SSL
<!-- vale on -->
## Currently Supported Platforms

The following list identifies all the platforms supported in Cumulus Linux 4.0.0. Note that some platforms supported in 3.7.z might not appear here, but should return in a future release if they are still supported (see the list of platforms no longer supported below).

- 100G
    - Dell S5232F-ON
    - Dell Z9264F-ON
    - Edgecore AS7816-64X
    - Edgecore AS7726-32X
    - Edgecore Minipack AS8000
    - HPE SN2745M
    - Lenovo NE10032O
    - NVIDIA Spectrum SN2700
    - NVIDIA Spectrum SN3700
    - NVIDIA Spectrum SN3700C
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
    - NVIDIA Spectrum SN2410
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

NVIDIA does not support these platforms in Cumulus Linux 4.0.0 (they are still supported in Cumulus Linux 3.7.z until that version reaches its end of life). Do **not** install Cumulus Linux 4.0.0 on any of these platforms as it does not run correctly:

- Cumulus Express CX-10256-S/Edgecore OMP-800 (100G Tomahawk)
- Dell S6000-ON (40G Trident2)
- Edgecore Wedge-100 (100G Tomahawk)
- Facebook Backpack (100G Tomahawk)
- Facebook Voyager (100G Tomahawk)
<!-- vale off -->
## Platforms Supported under Cumulus Linux 3.7.z but not Currently Supported

The following platforms are supported on Cumulus Linux 3.7.z but are not supported yet in Cumulus Linux 4.0. Support for these platforms should return at some point during the version 4.y.z release cycle.
<!-- vale on -->
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
- NVIDIA Spectrum SN2010
- NVIDIA Spectrum SN2100
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
- Supermicro SSE-C3632S
- Supermicro SSE-G3648B
- Supermicro SSE-X3648S

## Features Removed

- LNV is no longer included in Cumulus Linux
