---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.0 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.0, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.0, see the {{<link title="Cumulus Linux 5.0 Release Notes" text="Cumulus Linux 5.0 Release Notes">}}.
- To upgrade to Cumulus Linux 5.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.0.0
<!-- vale on -->
Cumulus Linux 5.0.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN3700C-S (100G Spectrum-2) with Secure Boot is now GA
<!-- - NVIDIA SN4700 (400G Spectrum A1)
- NVIDIA SN4410 (100G Spectrum A1)
- NVIDIA SN4600C (100G Spectrum A1)-->

### New Features and Enhancements

- The {{<link url="NVIDIA-User-Experience-NVUE" text="NVUE object model">}} is now the default CLI (replacing NCLU) and includes many improvements with updated and additional commands. You can now run NVUE commands to configure:
     - {{<link url="Protocol-Independent-Multicast-PIM" text="PIM">}}
     - {{<link url="IGMP-and-MLD-Snooping" text="IGMP">}}
     - {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#vrrp" text="VRRP">}}
     - {{<link title="Setting the Date and Time" text="The time zone">}}
     - {{<link url="Interface-Configuration-and-Management/#interface-descriptions" text="Interface descriptions (aliases)">}}

  Important command changes include:
     - BGP `peer` is now BGP `neighbor` (for example, `nv set vrf default router bgp peer swp51 remote-as external`)
     - BGP `static-network` is now `network` (for example, `nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32`)
     - The Cumulus Linux 4.4 `platform` commands are now under `system` (for example, `nv set system hostname`)
     - The `platform` commands now configure hardware components (for example, `nv set platform hardware component device type linecard`)

- {{<link url="Precision-Time-Protocol-PTP" text="PTP Boundary Clock">}} enhancements; {{<link url="Precision-Time-Protocol-PTP/#mixed-mode" text="mixed mode">}}, {{<link url="Precision-Time-Protocol-PTP/#acceptable-master-table" text="acceptable master table">}}, {{<link url="Precision-Time-Protocol-PTP/#dscp" text="DSCP">}}, and {{<link url="Precision-Time-Protocol-PTP/#ttl-for-a-ptp-message" text="TTL for a PTP message">}} are now GA.
- The maximum number of {{<link url="VLAN-aware-Bridge-Mode/#configure-multiple-vlan-aware-bridges" text="VLAN elements">}} supported with multiple bridges increases to 16K.
- SNMP enhancements include VRF-aware FRRouting MIBs and the ability to get the link up and link down count.
- DHCPv6 supports SVI interfaces.
- {{<link url="Optional-BGP-Configuration/#suppress-route-advertisement" text="Suppress route advertisement">}} is now GA.
<!-- - Host Based Networking (HBN) support. Cumulus Linux on the DPU simplifies host networking so that you can manage your network policies end to end, regardless of the server end point type. With HBN, you do not need to configure LACP or MLAG. In addition, ECMP provides high availablity.-->

{{%notice note%}}
Cumulus Linux 5.0.0 replaces NCLU with the NVUE object model. After you upgrade to Cumulus Linux 5.0.0, running NVUE configuration commands replaces the configuration in the applicable configuration files and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux commands to configure the switch instead of NVUE.

Cumulus Linux 3.7, 4.3, and 4.4 releases continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
