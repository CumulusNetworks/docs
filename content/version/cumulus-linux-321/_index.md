---
title: Cumulus Linux User Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/CL321/Cumulus+Linux+User+Guide
 - /pages/viewpage.action?pageId=5126727
pageID: 5126727
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
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

This documentation is current as of May 1, 2017 for version 3.2.1.
Please visit the [Cumulus Networks Web
site](http://docs.cumulusnetworks.com) for the most up to date
documentation.

Read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115002201048)
for new features and known issues in this release.

### <span>What's New in Cumulus Linux 3.2.1</span>

Cumulus Linux 3.2.1 adds these new features and platforms, including:

  - **Network Command Line Utility**: We've improved the syntax so it's
    even easier for network operators to configure Cumulus Linux with
    [NCLU](/version/cumulus-linux-321/System_Configuration/Network_Command_Line_Utility).

  - **Platform Independent Multicast (PIM)**: We've improved [multicast
    latency](/version/cumulus-linux-321/Layer_Three/Protocol_Independent_Multicast_-_PIM)
    on Mellanox switches.

  - **Explicit Congestion Notification (ECN)**: We've expanded support
    for
    [ECN](Buffer_and_Queue_Management.html#src-5127004_BufferandQueueManagement-ecn)
    to Tomahawk switches.

  - **New 100G platform**: Early access support for the [Edge-Core
    AS7412-32X](https://cumulusnetworks.com/HCL), which uses the
    Mellanox Spectrum ASIC.

For further information regarding these new features, and for
information regarding bug fixes and known issues present in this
release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115002201048).

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
