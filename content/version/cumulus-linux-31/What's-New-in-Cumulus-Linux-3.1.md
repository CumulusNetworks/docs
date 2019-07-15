---
title: What's New in Cumulus Linux 3.1
author: Cumulus Networks
weight: 11
aliases:
 - /display/CL31/What's-New-in-Cumulus-Linux-3.1
 - /pages/viewpage.action?pageId=5122208
pageID: 5122208
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-31
siteSlug: cumulus-linux-31
---
## <span>What's New in Cumulus Linux 3.1.2</span>

Cumulus Linux 3.1.2 includes bug fixes as well as the following [early
access
feature](https://support.cumulusnetworks.com/hc/en-us/articles/202933878).

  - [Edge-Core 5812-54X](http://cumulusnetworks.com/HCL)

## <span>What's New in Cumulus Linux 3.1.1</span>

Cumulus Linux 3.1.1 contains bug fixes and the following [early access
features](https://support.cumulusnetworks.com/hc/en-us/articles/202933878).

  - [Priority flow
    control](Buffer-and-Queue-Management.html#src-5122108_BufferandQueueManagement-BufferandQueueManagement-pfc)
    (PFC) — Mellanox switches only

  - [Explicit congestion
    notification](http://Buffer%20and%20Queue%20Management#BufferandQueueManagement-ecn)
    (ECN) — Mellanox switches only

  - [Ethernet virtual private
    networks](/version/cumulus-linux-31/Layer-1-and-Layer-2-Features/Network-Virtualization/Ethernet-Virtual-Private-Network---EVPN)
    (EVPN) — Broadcom switches only

No special steps are needed to enable PFC and ECN, and you do not need
to enable the Early Access repository to use them. You need to install
the `cumulus-evpn` metapackage to use EVPN; read the [EVPN
chapter](/version/cumulus-linux-31/Layer-1-and-Layer-2-Features/Network-Virtualization/Ethernet-Virtual-Private-Network---EVPN)
for instructions.

## <span>What's New in Cumulus Linux 3.1.0</span>

Cumulus Linux 3.1.0 includes many new features and platforms. In
addition to this chapter, please read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/224473608)
to learn about known issues with this release.

  - Mellanox platform enhancements:
    
      - [ACL](/version/cumulus-linux-31/System-Management/Netfilter---ACLs/)
        — 512 ACLs, line rate: 128 byte
    
      - [LACP
        Bypass](/version/cumulus-linux-31/Layer-1-and-Layer-2-Features/LACP-Bypass)
    
      - [sFlow](/version/cumulus-linux-31/Monitoring-and-Troubleshooting/Network-Troubleshooting/Monitoring-System-Statistics-and-Network-Traffic-with-sFlow)
        — 32G sampling rate
    
      - [VRF](/version/cumulus-linux-31/Layer-3-Features/Virtual-Routing-and-Forwarding---VRF)

  - [PoE+](/version/cumulus-linux-31/System-Management/Power-over-Ethernet---PoE)
    (Power over Ethernet)

  - [VXLAN with VLAN-aware
    bridges](VLAN-aware-Bridge-Mode-for-Large-scale-Layer-2-Environments.html#src-5122017_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-VXLANswithVLAN-awareBridges)
    ([Broadcom switches](https://cumulusnetworks.com/hcl) only)

  - [Forwarding table profiles](Routing.html#src-5122117_Routing-uft)

New platforms include:

  - [100G platforms](https://cumulusnetworks.com/hcl):
    
      - Edge-Core AS 7712
    
      - HPE 6960
    
      - Mellanox SN2100

  - [40G platforms](https://cumulusnetworks.com/hcl):
    
      - Dell S6010
    
      - Mellanox SN2100B

  - [25G platforms](https://cumulusnetworks.com/hcl):
    
      - Mellanox SN2410

  - [10G platforms](https://cumulusnetworks.com/hcl):
    
      - HPE 6921T
    
      - Mellanox SN2410B

### <span>Early Access Features</span>

The following [early access
features](https://support.cumulusnetworks.com/hc/en-us/articles/202933878)
are included in Cumulus Linux 3.1.0:

  - [Netq](/version/cumulus-linux-31/Monitoring-and-Troubleshooting/Network-Troubleshooting/Using-netq-to-Troubleshoot-the-Network)

  - [Network command line
    utility](/version/cumulus-linux-31/Configuring-and-Managing-Network-Interfaces/Network-Command-Line-Utility)

  - [OpenStack
    ML2](/version/cumulus-linux-31/Network-Solutions/OpenStack-Neutron-ML2-and-Cumulus-Linux)

  - [PIM-SM](/version/cumulus-linux-31/Layer-3-Features/Protocol-Independent-Multicast---PIM)

  - [TACACS+](/version/cumulus-linux-31/System-Management/Authentication-Authorization-and-Accounting/TACACS+)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
