---
title: What's New
author: Cumulus Networks
weight: 5
---

This document supports the Cumulus Linux 3.6 releases, and lists new platforms and features.

- For a list of all the platforms supported in a Cumulus Linux 3.6 release, see the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 3.6, see the {{<link url="Cumulus-Linux-3.6-Release-Notes">}}.
- To upgrade to a Cumulus Linux 3.6 release, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 3.6.2

Cumulus Linux 3.6.2 contains the following new features, platforms, and improvements:

- {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Facebook Voyager">}} (DWDM) (100G Tomahawk) now generally available
- NCLU commands available for {{<link url="Traditional-Bridge-Mode" text="configuring traditional mode bridges">}}
- {{<link url="Virtual-Routing-and-Forwarding-VRF/#configuring-static-route-leaking-with-evpn" text="VRF static route leaking with EVPN">}} symmetric routing
- New {{<link url="Virtual-Routing-and-Forwarding-VRF/#enabling-vrf-route-leaking" text="vrf_route_leak_enable option">}} used to enable VRF route leaking

## What's New in Cumulus Linux 3.6.2

Cumulus Linux 3.6.1 contains bug fixes and security fixes.

## What's New in Cumulus Linux 3.6.0

Cumulus Linux 3.6.0 contains a number of new platforms, features and improvements:

- New {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="platforms">}} include:
    - Dell S4128T-ON (10GBASE-T Maverick)
    - Dell S5048-ON (25G Tomahawk+)
    - Delta AG-5648v1 (25G Tomahawk+)
    - Edgecore AS7312-54XS (Tomahawk+)
    - Facebook Voyager (100G Tomahawk/DWDM) Early Access
    - Penguin Arctica 1600CS (100G Spectrum)
    - Penguin Arctica 3200CS (100G Spectrum)
    - Penguin Arctica 4808X (10G Spectrum)
- {{<link url="Policy-based-Routing" text="Policy-based routing">}}
- {{<link url="Virtual-Routing-and-Forwarding-VRF/#vrf-route-leaking" text="VRF route leaking">}}
- {{<link url="Setting-Date-and-Time/#precision-time-protocol-ptp-boundary-clock" text="PTP boundary clock">}} on Mellanox switches
- {{<link url="GRE-Tunneling" text="GRE tunneling">}} on Mellanox switches
- New `/etc/cumulus/ports.conf` file validator finds syntax errors and provides a reason for each invalid line. Error messages are shown when you run the `net commit` command.
- Support for the combination of the `local-as` and `allowas-in` commands
- OSPFv3 enhancements:
    - Validated interoperability with other routers at a scale of 120 neighbors
    - New NCLU commands to configure {{<link url="Open-Shortest-Path-First-v3-OSPFv3-Protocol/#configuring-the-ospfv3-area" text="OSPFv3">}}
- EVPN Enhancements:
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#evpn-type-5-routing-with-asymmetric-routing" text="Type-5 routes with asymmetric routing">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#originating-default-evpn-type-5-routes" text="Originate default EVPN type-5 routes">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#filtering-evpn-routes-based-on-type" text="Filter EVPN routes based on type">}}
    - {{<link url="Ethernet-Virtual-Private-Network-EVPN/#controlling-which-rib-routes-are-injected-into-evpn" text="Control which RIB routes are injected into EVPN">}}

For information on bug fixes and known issues present in this release, refer to the {{<link url="Cumulus-Linux-3.6-Release-Notes/" text="product release notes">}}.
