---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.3 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.3, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.3, see the {{<link title="Cumulus Linux 5.3 Release Notes" text="Cumulus Linux 5.3 Release Notes">}}.
- To upgrade to Cumulus Linux 5.3, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.3.0
<!-- vale on -->
Cumulus Linux 5.3.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN3750-SX (5G Spectrum-2) available for early access

### New Features and Enhancements

- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="Configure-SNMP" text="SNMP Server">}} and {{<link url="Configure-SNMP-Traps" text="SNMP trap">}} commands
  - {{<link url="Quality-of-Service" text="QoS commands">}} to configure COS and DSCP marking, egress queue mapping, egress traffic scheduling, PFC, ECN, and traffic pools
  - {{<link url="Configuring-switchd" text="switchd commands">}} to configure the statistic polling interval for physical and logical interfaces, log level for debugging, DSCP settings for encapsulation and decapsulation, host route preference, ACL mode, and reserved VLAN range
  - New {{<link url="Monitoring-and-Troubleshooting/#show-system-information" text="nv show system commands">}} include `nv show system memory` and `nv show system cpu`
  - New BGP commands include {{<link url="Optional-BGP-Configuration/#bgp-dynamic-neighbors" text="BGP dynamic neighbor">}}, {{<link url="Optional-BGP-Configuration/#update-source" text="BGP update source">}}, {{<link url="Optional-BGP-Configuration/#bgp-neighbor-shutdown" text="BGP  neighbor shutdown">}}
  - New route map {{<link url="Route-Filtering-and-Redistribution/#match-and-set-statements" text="match and set statements">}} enable you to match on an EVPN default route, and set the BGP community, metric, originator ID, and forwarding address
  - {{<link title="What Just Happened (WJH)" text="WJH commands">}}
  - {{<link url="Prescriptive-Topology-Manager-PTM/#check-link-state" text="PTM enable command">}} to check link state
  - Support for hyphens in hostnames, VRF, route map, next hop groups, prefix list, AS path list, community list, and ACL names
  - {{<link url="Interface-Configuration-and-Management/#fast-linkup" text="Fast link up command">}} (`nv set interface <interface-id> link fast-linkup on`) to support fast link up between Spectrum1 switches and certain optic network interface cards that require links to come up fast
  <!--- Commands changed from `enable on` and `enable off` to `set enable` and `unset enable` (the `enable on` and `enable off` commands continue to be supported for backward compatability)
  <!--- Obfuscated passwords to protect passwords from casual viewing
  <!-- - {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Search for a specific configuration">}} in the entire object model-->
  
{{%notice info%}}
Cumulus Linux 5.3 includes the NVUE object model. After you upgrade to Cumulus Linux 5.3, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
