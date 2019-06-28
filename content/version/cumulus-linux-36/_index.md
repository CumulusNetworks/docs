---
title: Cumulus Linux User Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/CL36/Cumulus+Linux+User+Guide
 - /pages/viewpage.action?pageId=8362022
pageID: 8362022
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
subsection: true
---
## <span>Introducing Cumulus Linux</span>

Cumulus Linux is the first full-featured Linux operating system for the
networking industry. The [Debian
Jessie](https://www.debian.org/releases/jessie/)-based,
networking-focused distribution runs on hardware produced by a [broad
partner ecosystem](http://cumulusnetworks.com/hcl/), ensuring unmatched
customer choice regarding silicon, optics, cables, and systems.

This user guide provides in-depth documentation on the Cumulus Linux
installation process, system configuration and management, network
solutions, and monitoring and troubleshooting recommendations. In
addition, the quick start guide provides an end-to-end setup process to
get you started.

This documentation is current as of September 19, 2018 for version
3.6.2. Visit the [Cumulus Networks Web
site](http://docs.cumulusnetworks.com) for the most up to date
documentation.

Read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115015543848)
for new features and known issues in this release.

### <span>What's New in Cumulus Linux 3.6.2</span>

Cumulus Linux 3.6.2 contains the following new features, platforms, and
improvements:

  - [Facebook Voyager](https://cumulusnetworks.com/hcl) (DWDM) (100G
    Tomahawk) now generally available

  - NCLU commands available for [configuring traditional mode
    bridges](/version/cumulus-linux-36/Layer_2/Ethernet_Bridging_-_VLANs/Traditional_Bridge_Mode)

  - [VRF static route leaking with
    EVPN](Virtual_Routing_and_Forwarding_-_VRF.html#src-8362412_VirtualRoutingandForwarding-VRF-EVPN_static_route_leak)
    symmetric routing

  - New [`vrf_route_leak_enable`
    option](Virtual_Routing_and_Forwarding_-_VRF.html#src-8362412_VirtualRoutingandForwarding-VRF-enable_route_leaking)
    used to enable VRF route leaking

### <span>What's New in Cumulus Linux 3.6.0</span>

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

  - [Policy-based
    Routing](/version/cumulus-linux-36/Layer_3/Policy-based_Routing)

  - <span style="color: #000000;"> [VRF Route
    Leaking](/display/CL36/Virtual+Routing+and+Forwarding+-+VRF#VirtualRoutingandForwarding-VRF-VRFRouteLeaking)
    </span>

  - <span style="color: #000000;"> [PTP Boundary
    Clock](Setting_Date_and_Time.html#src-8362040_SettingDateandTime-PTP)
    on Mellanox switches </span>

  - [GRE Tunneling](/version/cumulus-linux-36/Layer_3/GRE_Tunneling) on
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
        [OSPFv3](/display/CL36/Open+Shortest+Path+First+v3+-+OSPFv3+-+Protocol#OpenShortestPathFirstv3-OSPFv3-Protocol-ConfiguringtheOSPFv3Area)

  - EVPN Enhancements:
    
      - [Type-5 routes with asymmetric
        routing](/display/CL36/Ethernet+Virtual+Private+Network+-+EVPN#EthernetVirtualPrivateNetwork-EVPN-EVPNType-5RoutingwithAsymmetricRouting)
    
      - [Originate default EVPN type-5
        routes](/display/CL36/Ethernet+Virtual+Private+Network+-+EVPN#EthernetVirtualPrivateNetwork-EVPN-OriginatingDefaultEVPNType-5Routes)
    
      - <span style="color: #000000;"> [Filter EVPN routes based on
        type](/display/CL36/Ethernet+Virtual+Private+Network+-+EVPN#EthernetVirtualPrivateNetwork-EVPN-filter_evpn_route_typeFilteringEVPNRoutesBasedonType)
        </span>
    
      - [Control which RIB routes are injected into
        EVPN](/display/CL36/Ethernet+Virtual+Private+Network+-+EVPN#EthernetVirtualPrivateNetwork-EVPN-ControllingWhichRIBRoutesAreInjectedintoEVPN)

For information on bug fixes and known issues present in this release,
refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360003039873-Cumulus-Linux-3-6-Release-Notes).

### <span>Open Source Contributions</span>

To implement various Cumulus Linux features, Cumulus Networks has forked
various software projects, like CFEngine, `Netdev` and some Puppet Labs
packages. The forked code resides in the Cumulus Networks [GitHub
repository](https://github.com/CumulusNetworks).

Cumulus Networks has also developed and released new applications as
open source. The list of open source projects is on the [open source
software](http://oss.cumulusnetworks.com/) page.

### <span>Hardware Compatibility List</span>

You can find the most up-to-date hardware compatibility list (HCL)
[here](http://cumulusnetworks.com/hcl/). Use the HCL to confirm that
your switch model is supported by Cumulus Networks. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.
