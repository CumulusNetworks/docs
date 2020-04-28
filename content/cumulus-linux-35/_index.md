---
title: Cumulus Linux 3.5 User Guide
author: Cumulus Networks
weight: -35
aliases:
 - /display/CL35/Cumulus+Linux+User+Guide
 - /pages/viewpage.action?pageId=8357317
pageID: 8357317
subsection: true
cascade:
  product: Cumulus Linux
  version: "3.5"
  imgData: cumulus-linux-35
  siteSlug: cumulus-linux-35
  old: true
---
## Introducing Cumulus Linux

Cumulus Linux is the networking industry's first full-featured Linux
operating system. The 
[Debian Jessie](https://www.debian.org/releases/jessie/)-based,
networking-focused distribution runs on hardware produced by a 
[broad partner ecosystem](http://cumulusnetworks.com/hcl/), ensuring unmatched
customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation covering installing
Cumulus Linux, system configuration and management, network solutions,
and monitoring and troubleshooting recommendations. In addition, the
quick start guide provides an end-to-end setup process to get you
started with Cumulus Linux.

This documentation is current as of March 2, 2018 for version 3.5.3.
Please visit the [Cumulus Networks Web site](http://docs.cumulusnetworks.com) 
for the most up to date documentation.

Read the [release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848)
for new features and known issues in this release.

## What's New in Cumulus Linux 3.5

Cumulus Linux 3.5 contains a number of new platforms, features and
improvements:

  - New [platforms](https://cumulusnetworks.com/hcl) include:
      - Accton OMP-800 chassis/Cumulus Express CX-10256-S (100G)
      - Delta 9032-v1 (100G Tomahawk) and AG7648 (10G Trident II)
      - Broadcom Maverick-based 10G switches, including Dell S4128F-ON
      - Edgecore AS5812 AC with 3Y PSU
      - Facebook Wedge-100S now generally available
      - Mellanox Spectrum A1 chipsets in the 2100, 2410 and 2700 models;
        Mellanox 2740 (100G) and 2740B (40G)
      - Quanta LY7 (10G)
      - 10GBASE-LR BiDi optics

  - [Symmetric VXLAN routing](/cumulus-linux-35/Network-Virtualization/VXLAN-Routing)
  - VLAN-aware bridge support for ovs-vtepd, for 
    [VXLAN solutions using controllers](/cumulus-linux-35/Network-Virtualization/Virtualization-Integrations/)
  - OSPF is now
    [VRF-aware](/cumulus-linux-35/Layer-3/Virtual-Routing-and-Forwarding-VRF)
  - [Voice VLAN](/cumulus-linux-35/Layer-1-and-2/Link-Layer-Discovery-Protocol/Voice-VLAN)
  - [PIM](/cumulus-linux-35/Layer-3/Protocol-Independent-Multicast-PIM)
    now supports overlapping IP addresses and IP multicast boundaries
  - [Bridge layer 2 protocol tunnels](https://support.cumulusnetworks.com/hc/en-us/articles/115015809147)
  - The SNMP
    [Cumulus-Counters-MIB](/cumulus-linux-35/Monitoring-and-Troubleshooting/SNMP-Monitoring/#supported-mibs)
    file includes a new table `pfcClCountersTable` for link pause and
    priority flow control counters
  - See [what's new and different with NCLU](https://support.cumulusnetworks.com/hc/en-us/articles/115015593787)
    in this release

For further information regarding bug fixes and known issues present in
this release, refer to the 
[product release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848).

## Open Source Contributions

Cumulus Networks has forked various software projects, like CFEngine,
`Netdev` and some Puppet Labs packages in order to implement various
Cumulus Linux features. The forked code resides in the Cumulus Networks
[GitHub repository](https://github.com/CumulusNetworks).

Cumulus Networks developed and released as open source some new
applications as well.

The list of open source projects is on the 
[open source software](http://oss.cumulusnetworks.com/) page.

## Hardware Compatibility List

You can find the most up to date hardware compatibility list (HCL)
[here](https://cumulusnetworks.com/hcl/). Use the HCL to confirm that
your switch model is supported by Cumulus Networks. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.

## Download the User Guide

You can download a PDF of the user guide for versions {{<exlink url="https://drive.google.com/file/d/1_77_pdyRPMjzkqpA75GsE0G0uVQmfxnW/view?usp=sharing" text="3.5.0">}}, {{<exlink url="https://drive.google.com/file/d/1sOajT8pCBM9a5afu-dw6X-6Spt40uKfG/view?usp=sharing" text="3.5.1">}}, {{<exlink url="https://drive.google.com/file/d/1UZ0W1I17FOR1ysbVlO7I6GIpNYSAv3IP/view?usp=sharing" text="3.5.2">}} and {{<exlink url="https://drive.google.com/file/d/1pEA0pUEW4-1qlKKO7q0-R0mKjqgDhZ5x/view?usp=sharing" text="3.5.3">}}.
