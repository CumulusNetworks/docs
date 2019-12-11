---
title: Cumulus Linux 3.6 User Guide
author: Cumulus Networks
weight: -36
aliases:
 - /display/CL36/Cumulus+Linux+User+Guide
 - /display/CL36/Cumulus+Linux+Index/
 - /pages/viewpage.action?pageId=8362022
pageID: 8362022
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
subsection: true
---
## Introducing Cumulus Linux

Cumulus Linux is the first full-featured Linux operating system for the
networking industry. The 
[Debian Jessie](https://www.debian.org/releases/jessie/)-based,
networking-focused distribution runs on hardware produced by a 
[broad partner ecosystem](http://cumulusnetworks.com/hcl/), ensuring 
unmatched customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation on the Cumulus Linux
installation process, system configuration and management, network
solutions, and monitoring and troubleshooting recommendations. In
addition, the quick start guide provides an end-to-end setup process to
get you started.

### What's New in Cumulus Linux 3.6.2

Cumulus Linux 3.6.2 contains the following new features, platforms, and
improvements:

  - [Facebook Voyager](https://cumulusnetworks.com/hcl) (DWDM) (100G
    Tomahawk) now generally available
  - NCLU commands available for 
    [configuring traditional mode bridges](/version/cumulus-linux-36/Layer-2/Ethernet-Bridging-VLANs/Traditional-Bridge-Mode)
  - [VRF static route leaking with EVPN](/version/cumulus-linux-36/Layer-3/Virtual-Routing-and-Forwarding-VRF/#configuring-static-route-leaking-with-evpn)
    symmetric routing
  - New [`vrf_route_leak_enable` option](/version/cumulus-linux-36/Layer-3/Virtual-Routing-and-Forwarding-VRF/#enabling-vrf-route-leaking)
    used to enable VRF route leaking

### What's New in Cumulus Linux 3.6.0

Cumulus Linux 3.6.0 contains a number of new platforms, features and
improvements:

  - New [platforms](https://cumulusnetworks.com/hcl) include:
      - Dell S4128T-ON (10GBASE-T Maverick)
      - Dell S5048-ON (25G Tomahawk+)
      - Delta AG-5648v1 (25G Tomahawk+)
      - Edgecore AS7312-54XS (Tomahawk+)
      - Facebook Voyager (100G Tomahawk/DWDM) Early Access
      - Penguin Arctica 1600CS (100G Spectrum)
      - Penguin Arctica 3200CS (100G Spectrum)
      - Penguin Arctica 4808X (10G Spectrum)
  - [Policy-based Routing](/version/cumulus-linux-36/Layer-3/Policy-based-Routing)
  - [VRF Route Leaking](/version/cumulus-linux-36/Layer-3/Virtual-Routing-and-Forwarding-VRF/#vrf-route-leaking)
  - [PTP Boundary Clock](/version/cumulus-linux-36/System-Configuration/Setting-Date-and-Time/#precision-time-protocol-ptp-boundary-clock)
    on Mellanox switches
  - [GRE Tunneling](/version/cumulus-linux-36/Layer-3/GRE-Tunneling) on
    Mellanox switches
  - New `/etc/cumulus/ports.conf` file validator finds syntax errors and
    provides a reason for each invalid line. Error messages are shown
    when you run the `net commit` command.
  - Support for the combination of the `local-as` and `allowas-in`
    commands
  - OSPFv3 enhancements:
      - Validated interoperability with other routers at a scale of 120
        neighbors
      - New NCLU commands to configure
        [OSPFv3](/version/cumulus-linux-36/Layer-3/Open-Shortest-Path-First-v3-OSPFv3-Protocol/#configuring-the-ospfv3-area)
  - EVPN Enhancements:
      - [Type-5 routes with asymmetric routing](/version/cumulus-linux-36/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/#evpn-type-5-routing-with-asymmetric-routing)
      - [Originate default EVPN type-5 routes](/version/cumulus-linux-36/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/#originating-default-evpn-type-5-routes)
      - [Filter EVPN routes based on type](/version/cumulus-linux-36/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/#filtering-evpn-routes-based-on-type)
      - [Control which RIB routes are injected into EVPN](/version/cumulus-linux-36/Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/#controlling-which-rib-routes-are-injected-into-evpn)

For information on bug fixes and known issues present in this release,
refer to the 
[product release notes](https://support.cumulusnetworks.com/hc/en-us/articles/360003039873-Cumulus-Linux-3-6-Release-Notes).

### Open Source Contributions

To implement various Cumulus Linux features, Cumulus Networks has forked
various software projects, like CFEngine, `Netdev` and some Puppet Labs
packages. The forked code resides in the Cumulus Networks 
[GitHub repository](https://github.com/CumulusNetworks).

Cumulus Networks has also developed and released new applications as
open source. The list of open source projects is on the [open source
software](http://oss.cumulusnetworks.com/) page.

### Hardware Compatibility List

You can find the most up-to-date hardware compatibility list (HCL)
[here](https://cumulusnetworks.com/hcl/). Use the HCL to confirm that
your switch model is supported by Cumulus Networks. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.
