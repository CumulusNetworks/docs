---
title: Cumulus Linux User Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/CL35/Cumulus+Linux+User+Guide
 - /pages/viewpage.action?pageId=8357317
pageID: 8357317
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
subsection: true
---
## <span>Introducing Cumulus Linux</span>

Cumulus Linux is the networking industry's first full-featured Linux
operating system. The [Debian
Jessie](https://www.debian.org/releases/jessie/)-based,
networking-focused distribution runs on hardware produced by a [broad
partner ecosystem](http://cumulusnetworks.com/hcl/), ensuring unmatched
customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation covering installing
Cumulus Linux, system configuration and management, network solutions,
and monitoring and troubleshooting recommendations. In addition, the
quick start guide provides an end-to-end setup process to get you
started with Cumulus Linux.

This documentation is current as of March 2, 2018 for version 3.5.3.
Please visit the [Cumulus Networks Web
site](http://docs.cumulusnetworks.com) for the most up to date
documentation.

Read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848)
for new features and known issues in this release.

### <span>What's New in Cumulus Linux 3.5</span>

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

  - [Symmetric VXLAN
    routing](/version/cumulus-linux-35/Network_Virtualization/VXLAN_Routing)

  - VLAN-aware bridge support for ovs-vtepd, for [VXLAN solutions using
    controllers](/version/cumulus-linux-35/Network_Virtualization/Virtualization_Integrations/)

  - OSPF is now
    [VRF-aware](/version/cumulus-linux-35/Layer_3/Virtual_Routing_and_Forwarding_-_VRF)

  - [Voice
    VLAN](/version/cumulus-linux-35/Layer_1_and_2/Link_Layer_Discovery_Protocol/Voice_VLAN)

  - [PIM](/version/cumulus-linux-35/Layer_3/Protocol_Independent_Multicast_-_PIM)
    now supports overlapping IP addresses and IP multicast boundaries

  - [Bridge layer 2 protocol
    tunnels](https://support.cumulusnetworks.com/hc/en-us/articles/115015809147)

  - The SNMP
    [Cumulus-Counters-MIB](SNMP_Monitoring.html#src-8357390_SNMPMonitoring-supported_mibs)
    file includes a new table `pfcClCountersTable` for link pause and
    priority flow control counters

  - See [what's new and different with
    NCLU](https://support.cumulusnetworks.com/hc/en-us/articles/115015593787)
    in this release

For further information regarding bug fixes and known issues present in
this release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848).

### <span>Open Source Contributions</span>

Cumulus Networks has forked various software projects, like CFEngine,
`Netdev` and some Puppet Labs packages in order to implement various
Cumulus Linux features. The forked code resides in the Cumulus Networks
[GitHub repository](https://github.com/CumulusNetworks).

Cumulus Networks developed and released as open source some new
applications as well.

The list of open source projects is on the [open source
software](http://oss.cumulusnetworks.com/) page.

### <span>Hardware Compatibility List</span>

You can find the most up to date hardware compatibility list (HCL)
[here](http://cumulusnetworks.com/hcl/). Use the HCL to confirm that
your switch model is supported by Cumulus Networks. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.
