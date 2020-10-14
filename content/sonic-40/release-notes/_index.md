---
title: SONiC Release Notes
author: Cumulus Networks
weight: 20
product: SONiC
version: 4.0
siteSlug: sonic
---

## Release Notes Update History

| Revision | Date | Description |
| -------- | ---- | ----------- |
| Rev 7.0 | October 06, 2020 | Initial release of this Release Notes version. This version introduces Changes and New Features and Bug Fixes. |

## Overview

SONiC is an open source network operating system based on Linux that runs on switches from multiple vendors and ASICs. SONiC offers a full-suite of network functionality, like BGP and RDMA, that has been production-hardened in the data centers of some of the largest cloud-service providers. It offers teams the flexibility to create the network solutions they need while leveraging the collective strength of a large ecosystem and community.

These are the release notes for SONiC software on NVIDIA® Mellanox Spectrum® based switches.

## Changes and New Features

This section provides only a list of Changes and New Features in this version. For a list of old releases, please see Changes and New Features History.

| Feature/Change | Description |
| -------------- | ----------- |
|  | Rev. SONiC 201911_MUR5 |

### Customer-Affecting Changes

| Feature/Change | Description |
| -------------- | ----------- |
|  | Rev. SONiC 201911_MUR5 |

## SONiC General Support

###	Supported Switch Systems

This software supports the switch systems listed below.

| Part Number | System Description |
| ----------- | ------------------ |
| SN2010	Mellanox Spectrum based 100GbE, Open Ethernet switch, 18 SFP+ and 4 QSFP28 ports, 2 AC power supplies, x86 quad core, short depth
SN2100	Mellanox Spectrum based 100GbE, Open Ethernet switch, 16 QSFP28 ports, short depth, Rangeley CPU
SN2410	Mellanox Spectrum based 25GbE/100GbE, Open Ethernet switch, 48 SFP28 ports, 8 QSFP28 ports, x86 dual core, short depth
SN2700	Mellanox Spectrum based 100GbE, Open Ethernet switch, 32 QSFP28 ports, x86 CPU, standard depth
SN3420	Mellanox Spectrum-2 based 25GbE/100GbE 1U Open Ethernet switch, 48 SFP28 ports and 12 QSFP28 ports, x86 CPU, Standard depth
SN3700	Mellanox Spectrum-2 based 200GbE Open Ethernet switch, 32 QSFP56 ports, x86 CPU, standard depth
SN3700C	Mellanox Spectrum-2 based 100GbE Open Ethernet switch, 32 QSFP28 ports, x86 CPU, standard depth
SN3800	Mellanox Spectrum-2 based 100GbE Open Ethernet switch, 64 QSFP28 ports, x86 CPU, standard depth
SN4600C	Mellanox Spectrum-3 based 100GbE 2U Open Ethernet Switch, 64 QSFP56 ports, 2 Power Supplies (AC), standard depth
SN4700	Mellanox Spectrum-3 based 400GbE, 1U Open Ethernet switch, 32xQSFP-DD ports, x86 CPU, standard depth
4.2	SONiC Versions
Branch	Hash	Location
SONiC 201911_MUR4	bea968bb2be64c739ed0bae7cfdcc40eccf6988b	https://github.com/Azure/sonic-buildimage/tree/201911

4.3	Package Content
This release is based on SONiC 201911_MUR3 sonic-buildimage hash. It contains the following components:
Switch Components	Version	Additional Information
Mellanox Spectrum-3 Firmware	30.2008.1910	
Mellanox Spectrum-2 Firmware	29.2008.1910	
Mellanox Spectrum Firmware	13.2008.1910	
SDK	4.4.1910	SDK API can be found at: https://github.com/Mellanox/SwitchRouterSDK-interfaces

SAI	1.17.3	Mellanox SAI implementation can be found at: https://github.com/Mellanox/SAI-Implementation/tree/sonic1910

Mellanox Firmware Tools (MFT)	4.15.0-104	•	Release Notes
•	User Manual

### Application Extensions

The following are the Mellanox Application Extensions:

| Application Extensions | Version | Additional Information |
| ---------------------- | ------- | ---------------------- |
| What-Just-Happened | what-just-happened/what-just-happened-201911_1.3.0_amd64.deb | For further information see section "What Just Happened" in the User Manual.<br />**Note:** This version is aligned with SDK v4.4.1910 as well as enabling what-just-happen integration with hardware clock. |

## Bug Fixes in this Version

