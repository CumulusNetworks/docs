---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.0 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.0, see the {{<link title="Cumulus Linux 5.0 Release Notes" text="Cumulus Linux 5.0 Release Notes">}}.
- To upgrade to Cumulus Linux 5.0, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.0.1
<!-- vale on -->
Cumulus Linux 5.0.1 resolves an issue with the Cumulus Linux repository that enabled an unnecessary package upgrade.
<!-- vale off -->
## What's New in Cumulus Linux 5.0.0
<!-- vale on -->
Cumulus Linux 5.0.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN3700C-S (100G Spectrum-2) with Secure Boot is now GA

### New Features and Enhancements

- The {{<link url="NVIDIA-User-Experience-NVUE" text="NVUE object model">}} is now the default CLI (replacing NCLU) and includes many improvements with updated and additional commands. You can now run NVUE commands to configure:
     - {{<link url="Protocol-Independent-Multicast-PIM" text="PIM">}}
     - {{<link url="IGMP-and-MLD-Snooping" text="IGMP">}}
     - {{<link url="Virtual-Router-Redundancy-VRR-and-VRRP/#vrrp" text="VRRP">}}
     - {{<link title="Setting the Date and Time" text="The time zone">}}
     - {{<link url="Interface-Configuration-and-Management/#interface-descriptions" text="Interface descriptions (aliases)">}}

  Important NVUE command updates include:
     - {{<link url="Basic-BGP-Configuration" text="BGP">}} `peer` is now BGP `neighbor`. For example, the `nv set vrf default router bgp peer swp51 remote-as external` command is now `nv set vrf default router bgp neighbor swp51 remote-as external`.
     - {{<link url="Basic-BGP-Configuration" text="BGP">}} `static-network` is now `network`. For example, the `nv set vrf default router bgp address-family ipv4-unicast static-network 10.10.10.1/32` command is now `nv set vrf default router bgp address-family ipv4-unicast network 10.10.10.1/32`.
     - The Cumulus Linux 4.4 `platform` {{<link url="NVIDIA-User-Experience-NVUE/#command-categories" text="commands">}} are now under `system` (for example, `nv set system hostname`)
     - The `platform` {{<link url="NVIDIA-User-Experience-NVUE/#command-categories" text="commands">}} now configure hardware components (for example, `nv set platform hardware component device type linecard`)
     - New {{<link url="NVIDIA-User-Experience-NVUE/#configuration-management-commands" text="configuration management commands">}}: `nv config show -o commands` shows the currently applied configuration commands and `nv config diff -o commands` shows differences between two configuration revisions.

- {{<link url="Precision-Time-Protocol-PTP" text="PTP Boundary Clock">}} enhancements; {{<link url="Precision-Time-Protocol-PTP/#message-mode" text="Message mode">}}, {{<link url="Precision-Time-Protocol-PTP/#acceptable-master-table" text="acceptable master table">}}, {{<link url="Precision-Time-Protocol-PTP/#dscp" text="DSCP">}}, and {{<link url="Precision-Time-Protocol-PTP/#ttl-for-a-ptp-message" text="TTL for a PTP message">}} are now GA.
- The maximum number of {{<link url="VLAN-aware-Bridge-Mode/#configure-multiple-vlan-aware-bridges" text="VLAN elements">}} supported with multiple bridges increases to 16K.
- {{<link url="Simple-Network-Management-Protocol-SNMP" text="SNMP">}} enhancements include VRF-aware FRRouting MIBs and the ability to get the link up and link down count.
- {{<link url="Optional-BGP-Configuration/#suppress-route-advertisement" text="Suppress route advertisement">}} is now GA.
- {{<link url="Netfilter-ACLs" text="Netfilter-ACL">}} enhancements include:
  - {{<link url="Netfilter-ACLs/#control-plane-policers" text="New control plane policer configuration">}}
  - {{<link url="Netfilter-ACLs/#install-and-manage-acl-rules-with-nvue" text="Updated rules">}}; Cumulus Linux now uses the `-t mangle -A PREROUTING` chain for ingress rules and the `-t mangle -A POSTROUTING` chain for egress rules instead of the `- A FORWARD` chain. Previously configured rules with `- A FORWARD` chain are still supported.

{{%notice note%}}
Cumulus Linux 5.0.0 replaces NCLU with the {{<link url="NVIDIA-User-Experience-NVUE" text="NVUE object model">}}. After you upgrade to Cumulus Linux 5.0.0, running NVUE configuration commands replaces the configuration in the applicable configuration files and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux commands to configure the switch instead of NVUE.

Cumulus Linux 3.7, 4.3, and 4.4 releases continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
