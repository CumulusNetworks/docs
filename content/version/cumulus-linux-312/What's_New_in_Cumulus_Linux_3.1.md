---
title: What's New in Cumulus Linux 3.1
author: Cumulus Networks
weight: 11
aliases:
 - /display/CL31/What's+New+in+Cumulus+Linux+3.1
 - /pages/viewpage.action?pageId=5122208
pageID: 5122208
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
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
    control](Buffer_and_Queue_Management.html#src-5122108_BufferandQueueManagement-BufferandQueueManagement-pfc)
    (PFC) — Mellanox switches only

  - [Explicit congestion
    notification](http://Buffer%20and%20Queue%20Management#BufferandQueueManagement-ecn)
    (ECN) — Mellanox switches only

  - [Ethernet virtual private
    networks](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN)
    (EVPN) — Broadcom switches only

No special steps are needed to enable PFC and ECN, and you do not need
to enable the Early Access repository to use them.
<span style="color: #000000;"> You need to install the </span>
`cumulus-evpn` <span style="color: #000000;"> metapackage to use EVPN;
read the </span> [EVPN
chapter](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/Network_Virtualization/Ethernet_Virtual_Private_Network_-_EVPN)
<span style="color: #000000;"> for instructions. </span>

## <span>What's New in Cumulus Linux 3.1.0</span>

Cumulus Linux 3.1.0 includes many new features and platforms. In
addition to this chapter, please read the [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/224473608)
to learn about known issues with this release.

  - Mellanox platform enhancements:
    
      - [ACL](/version/cumulus-linux-312/System_Management/Netfilter_-_ACLs/)
        — 512 ACLs, line rate: 128 byte
    
      - [LACP
        Bypass](/version/cumulus-linux-312/Layer_1_and_Layer_2_Features/LACP_Bypass)
    
      - [sFlow](/version/cumulus-linux-312/Monitoring_and_Troubleshooting/Network_Troubleshooting/Monitoring_System_Statistics_and_Network_Traffic_with_sFlow)
        — 32G sampling rate
    
      - [VRF](/version/cumulus-linux-312/Layer_3_Features/Virtual_Routing_and_Forwarding_-_VRF)

  - [PoE+](/version/cumulus-linux-312/System_Management/Power_over_Ethernet_-_PoE)
    (Power over Ethernet)

  - [VXLAN with VLAN-aware
    bridges](VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments.html#src-5122017_VLAN-awareBridgeModeforLarge-scaleLayer2Environments-VXLANswithVLAN-awareBridges)
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

  - [Netq](/version/cumulus-linux-312/Monitoring_and_Troubleshooting/Network_Troubleshooting/Using_netq_to_Troubleshoot_the_Network)

  - [Network command line
    utility](/version/cumulus-linux-312/Configuring_and_Managing_Network_Interfaces/Network_Command_Line_Utility)

  - [OpenStack
    ML2](/version/cumulus-linux-312/Network_Solutions/OpenStack_Neutron_ML2_and_Cumulus_Linux)

  - [PIM-SM](/version/cumulus-linux-312/Layer_3_Features/Protocol_Independent_Multicast_-_PIM)

  - [TACACS+](/version/cumulus-linux-312/System_Management/Authentication_Authorization_and_Accounting/TACACS+)
