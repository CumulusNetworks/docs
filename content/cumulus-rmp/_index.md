---
title: Cumulus RMP
author: Cumulus Networks
weight: 1
aliases:
 - /display/RMP/Cumulus-RMP
 - /pages/viewpage.action?pageId=5122807
pageID: 5122807
product: Cumulus RMP
version: '3.7'
imgData: cumulus-rmp-37
siteSlug: cumulus-rmp-37
subsection: true
---
<details>

## <span>Introducing Cumulus RMP</span>

Cumulus RMP is a network operating system in a ready-to-deploy solution
that enables out-of-band management for web-scale networks. It provides
an open platform for customers and system integrators to use as is or on
which to build rack management applications.

Cumulus RMP shares the same architecture, foundation, and user
experience with Cumulus Linux. However, the feature set is customized to
the needs of out-of-band management. For a comparison of the features
supported in Cumulus RMP, [see below](#src-5122807_CumulusRMP-features).

You can also find more information about Cumulus RMP
[here](https://cumulusnetworks.com/products/cumulus-rack-management-platform/).

{{% imgOld 0 %}}

## <span>What's New in Cumulus RMP</span>

Cumulus RMP 3.7.0 contains several bug fixes and the following new
features:

  - [RADIUS Change of Authorization (CoA)
    requests](/display/RMP/802.1X+Interfaces#id-802.1XInterfaces-CoArequests)

  - [RADIUS AAA local fallback
    authentication](/display/RMP/RADIUS+AAA#RADIUSAAA-local-fallback-auth)

  - [TACACS+ local fallback
    authentication](/display/RMP/TACACS+Plus#TACACSPlus-fallback-auth)

  - New NCLU commands:
    
      - [Show the version of a
        package](/display/RMP/Adding+and+Updating+Packages#AddingandUpdatingPackages-versionDisplay)
    
      - [Show the interface description
        (alias)](/display/RMP/Interface+Configuration+and+Management#InterfaceConfigurationandManagement-show_alias)
        for all interfaces on the switch
    
      - [Change bond mode to IEEE
        802.3ad](/display/RMP/Bonding+-+Link+Aggregation) link
        aggregation mod

For further information regarding bug fixes and known issues present in
the 3.7 release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360009508373-Cumulus-RMP-3-7-Release-Notes).

<summary>What's New in Cumulus RMP 3.6.2 </summary>

Cumulus RMP 3.6.2 contains several bug fixes and the following new
feature:

  - NCLU commands available for [configuring traditional mode
    bridges](/display/RMP/Traditional+Mode+Bridges)

For further information regarding bug fixes and known issues present in
the 3.6.2 release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360003646974-Cumulus-RMP-3-6-Release-Notes).

<summary>What's New in Cumulus RMP 3.6.0 </summary>

Cumulus RMP 3.6.0 contains several bug fixes and the following new
feature:

  - Support for a combination of local-as and allowas-in commands

For further information regarding bug fixes and known issues present in
the 3.6.0 release, refer to the [product release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/360003646974-Cumulus-RMP-3-6-Release-Notes).

## <span id="src-5122807_CumulusRMP-features" class="confluence-anchor-link"></span><span>Cumulus RMP Features</span>

Cumulus RMP shares much of the same functionality as Cumulus Linux and
comes preinstalled on your choice of [1G
switches](https://cumulusnetworks.com/products/hardware-compatibility-list/?Type=rmp).
For more information about each feature, follow the links below to the
[Cumulus Linux user guide](/display/RMP/Cumulus+Linux+User+Guide):

|                                                                                             |                 |                   |
| ------------------------------------------------------------------------------------------- | --------------- | ----------------- |
| **Layer 2 Support**                                                                         | **Cumulus RMP** | **Cumulus Linux** |
| [LLDP](/display/RMP/Link+Layer+Discovery+Protocol)                                          | ✓               | ✓                 |
| [PTM](/display/RMP/Prescriptive+Topology+Manager+-+PTM)                                     | ✓               | ✓                 |
| [Ethernet bridging](/display/RMP/Ethernet+Bridging+-+VLANs) (VLANs)                         | ✓               | ✓                 |
| [Bonds/link aggregation](/display/RMP/Bonding+-+Link+Aggregation)                           | ✓               | ✓                 |
| MLAG                                                                                        |                 | ✓                 |
| LACP                                                                                        | ✓               | ✓                 |
| LACP bypass                                                                                 |                 | ✓                 |
| [Spanning tree protocol/RST](/display/RMP/Spanning+Tree+and+Rapid+Spanning+Tree)            | ✓               | ✓                 |
| [802.1Q VLAN tagging](/display/RMP/VLAN+Tagging)                                            | ✓               | ✓                 |
| [VLAN-aware bridging](/display/RMP/VLAN-aware+Bridge+Mode)                                  | ✓               | ✓                 |
| [BPDU guard](/display/RMP/Spanning+Tree+and+Rapid+Spanning+Tree)                            | ✓               | ✓                 |
| [Bridge assurance](/display/RMP/Spanning+Tree+and+Rapid+Spanning+Tree)                      | ✓               | ✓                 |
| [BPDU filter](/display/RMP/Spanning+Tree+and+Rapid+Spanning+Tree)                           | ✓               | ✓                 |
| VRR                                                                                         |                 | ✓                 |
| IGMP and MLD snooping                                                                       |                 | ✓                 |
| Unicast/broadcast storm control                                                             |                 | ✓                 |
| CDP                                                                                         |                 | ✓                 |
| **Layer 3 Support**                                                                         | **Cumulus RMP** | **Cumulus Linux** |
| [Static routing](/display/RMP/Routing)                                                      | ✓               | ✓                 |
| ECMP                                                                                        |                 | ✓                 |
| ECMP resilient hashing                                                                      |                 | ✓                 |
| OSPF                                                                                        |                 | ✓                 |
| BGP                                                                                         |                 | ✓                 |
| FRRouting                                                                                   |                 | ✓                 |
| BFD                                                                                         |                 | ✓                 |
| IPv6                                                                                        |                 | ✓                 |
| [Management VRF](/display/RMP/Management+VRF)                                               | ✓               | ✓                 |
| Virtual routing and forwarding (VRF)                                                        |                 | ✓                 |
| **Additional Functionality**                                                                | **Cumulus RMP** | **Cumulus Linux** |
| [Network command line utility](/display/RMP/Network+Command+Line+Utility+-+NCLU)            | ✓               | ✓                 |
| [Interface configuration & management](/display/RMP/Interface+Configuration+and+Management) | ✓               | ✓                 |
| [802.1X interfaces](/display/RMP/802.1X+Interfaces)                                         |                 | ✓                 |
| [Zero-touch OS install & upgrade](/display/RMP/Zero+Touch+Provisioning+-+ZTP)               | ✓               | ✓                 |
| [Installation and package management](/display/RMP/Installation+Management)                 | ✓               | ✓                 |
| Full Linux extensibility                                                                    | ✓               | ✓                 |
| Network virtualization (VXLAN, LNV, EVPN, etc.)                                             |                 | ✓                 |
| [Monitoring & troubleshooting](/display/RMP/Monitoring+and+Troubleshooting)                 | ✓               | ✓                 |
| [AAA](/display/RMP/LDAP+Authentication+and+Authorization)                                   | ✓               | ✓                 |
| [ACLs](/display/RMP/Netfilter+-+ACLs)                                                       | ✓               | ✓                 |
| QoS                                                                                         |                 | ✓                 |
| [Orchestration](/display/RMP/Upgrading+Cumulus+Linux)                                       | ✓               | ✓                 |

## <span>Setting up a Cumulus RMP Switch</span>

The [quick start guide](/version/cumulus-rmp-37/Quick-Start-Guide) walks
you through the steps necessary for getting your Cumulus RMP switch up
and running after you remove it from the box.

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
