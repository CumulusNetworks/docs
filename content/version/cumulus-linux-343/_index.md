---
title: Cumulus Linux 3.4 User Guide
author: Cumulus Networks
weight: -34
aliases:
 - /display/CL34/Cumulus+Linux+User+Guide
 - /pages/viewpage.action?pageId=7112280
pageID: 7112280
product: Cumulus Linux
version: 3.4
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
subsection: true
---
## Introducing Cumulus Linux

Cumulus Linux is the networking industry's first full-featured Linux
operating system. The [Debian Jessie](https://www.debian.org/releases/jessie/)-based,
networking-focused distribution runs on hardware produced by a 
[broad partner ecosystem](https://cumulusnetworks.com/hcl/), ensuring unmatched
customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation covering installing
Cumulus Linux, system configuration and management, network solutions,
and monitoring and troubleshooting recommendations. In addition, the
quick start guide provides an end-to-end setup process to get you
started with Cumulus Linux.

This documentation is current as of November 6, 2017 for version 3.4.3.
Please visit the 
[Cumulus Networks Web site](https://docs.cumulusnetworks.com) for the most up to date
documentation.

Read the 
[release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115013055508)
for new features and known issues in this release.

### What's New in Cumulus Linux 3.4.3

Cumulus Linux 3.4.3 contains critical bug fixes only. For more
information on the issues that were fixed, read the 
[release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115014754307).

### What's New in Cumulus Linux 3.4.2

Cumulus Linux 3.4.2 contains critical bug fixes only. For more
information on the issues that were fixed, read the 
[release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115013055508).

### What's New in Cumulus Linux 3.4.1

Cumulus Linux 3.4.1 contains critical bug fixes only. For more
information on the issues that were fixed, read the 
[release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115012218847).

### What's New in Cumulus Linux 3.4.0

Cumulus Linux 3.4.0 contains a number of new platforms, features and
improvements:

- New [platforms](https://cumulusnetworks.com/hcl) include:

  - Facebook Backpack 100G chassis now generally available
  - Facebook Wedge-100
  - QuantaMesh T1048-LY4R

    [FRRouting](/version/cumulus-linux-343/Layer-Three/FRRouting-Overview/)
    replaces Quagga as the routing suite for Cumulus Linux

- [VXLAN routing](/version/cumulus-linux-343/Network-Virtualization/VXLAN-Routing)
  (asymmetric) is now generally available
- [HTTP API](/version/cumulus-linux-343/System-Configuration/HTTP-API) to
  [NCLU](/version/cumulus-linux-343/System-Configuration/Network-Command-Line-Utility-NCLU)
  and the
  [OpenStack ML2 driver](/version/cumulus-linux-343/Network-Solutions/OpenStack-Neutron-ML2-and-Cumulus-Linux)
- [QinQ with VXLANs](/version/cumulus-linux-343/Network-Virtualization/Hybrid-Cloud-Connectivity-with-QinQ-and-VXLANs)
    is now generally available
- [PIM support](/version/cumulus-linux-343/Layer-Three/Protocol-Independent-Multicast-PIM)
    expanded to include virtual routing and forwarding (VRF) and
    bidirectional forwarding detection (BFD) for PIM neighbors
- The default [MAC ageing time](/version/cumulus-linux-343/Layer-One-and-Two/Ethernet-Bridging-VLANs/#mac-address-ageing)
    has been set to 30 minutes and the default 
    [ARP base\_reachable time](/version/cumulus-linux-343/Layer-One-and-Two/Ethernet-Bridging-VLANs/VLAN-aware-Bridge-Mode-for-Large-scale-Layer-2-Environments/#configuring-arp-timers)
    has been set to 18 minutes
- See [what's new and different with NCLU](https://support.cumulusnetworks.com/hc/en-us/articles/115011823667)
  in this release

It also contains these 
[early access](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
features and platforms:

- [Edgecore OMP-800](https://cumulusnetworks.com/products/hardware-compatibility-list/?Brand=edgecore) 100G chassis
- [Dell S4148-ON and S4148T-ON](https://cumulusnetworks.com/products/hardware-compatibility-list/?Brand=dell) 10G switches
- [Segment routing](/version/cumulus-linux-343/Layer-Three/Segment-Routing)

For further information regarding bug fixes and known issues present in
this release, refer to the 
[product release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115011217808).

### Open Source Contributions

Cumulus Networks has forked various software projects, like CFEngine,
`Netdev` and some Puppet Labs packages in order to implement various
Cumulus Linux features. The forked code resides in the Cumulus Networks
[GitHub repository](https://github.com/CumulusNetworks).

Cumulus Networks developed and released as open source some new
applications as well.

The list of open source projects is on the [open source
software](http://oss.cumulusnetworks.com/) page.

### Hardware Compatibility List

You can find the most up to date hardware compatibility list (HCL)
[here](http://cumulusnetworks.com/hcl/). Use the HCL to confirm that
your switch model is supported by Cumulus Networks. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.
