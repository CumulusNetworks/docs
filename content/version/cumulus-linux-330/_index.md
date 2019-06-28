---
title: Cumulus Linux User Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/CL330/Cumulus+Linux+User+Guide
 - /pages/viewpage.action?pageId=5866080
pageID: 5866080
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
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

This documentation is current as of May 1, 2017 for version 3.3. Please
visit the [Cumulus Networks Web site](http://docs.cumulusnetworks.com)
for the most up to date documentation.

Read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115002201048)
for new features and known issues in this release.

### <span>What's New in Cumulus Linux 3.3</span>

Cumulus Linux 3.3 adds these new features and platforms, including:

  - New 25G platform: Expanding the 25G portfolio with the Quanta IX2.

  - [Network Command Line
    Utility](/version/cumulus-linux-330/System_Configuration/Network_Command_Line_Utility):
    Adds coverage for DNS, NTP, syslog, VRF, EVPN, 802.1X that will give
    network operators a single tool to configure and operate their
    Cumulus Linux switches. You can see the list of changes made in this
    release
    [here](https://support.cumulusnetworks.com/hc/en-us/articles/115005751268).

  - [Buffer
    monitoring](/version/cumulus-linux-330/Monitoring_and_Troubleshooting/Buffer_Monitoring):
    Proactively detect congestion events that result in latency and
    jitter by monitoring traffic patterns to identify bottlenecks early
    and effective plan for capacity.

  - [PIM-SSM](/version/cumulus-linux-330/Layer_Three/Protocol_Independent_Multicast_-_PIM):
    Source-Specific Multicast for more efficient multicast traffic
    segmentation and higher scalability.

  - [EVPN](/version/cumulus-linux-330/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN):
    Includes ARP suppression, static/sticky MAC and interoperability
    with Cisco NXOS.

  - [802.1X
    interfaces](/version/cumulus-linux-330/Interface_Configuration_and_Management/802.1X_Interfaces):
    Authenticate clients over wired media.

  - Cumulus Linux 3.3 and newer releases include support for detecting
    the physical interface a packet was received from, and using this
    value to populate the circuit-id field. This can be done with the
    --use-pif-circut-id option. This option is disabled by default.

For further information regarding these new features, and for
information regarding bug fixes and known issues present in this
release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115005751148).

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
