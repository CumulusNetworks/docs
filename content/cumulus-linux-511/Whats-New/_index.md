---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.11 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.11, see the {{<link title="Cumulus Linux 5.11 Release Notes" text="Cumulus Linux 5.11 Release Notes">}}.
- To upgrade to Cumulus Linux 5.11, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->

## What's New in Cumulus Linux 5.11

### Platforms

### New Features and Enhancements

- {{<link url="Factory-Reset" text="Factory Reset">}}
- {{<link url="Forwarding-Table-Size-and-Profiles/#spectrum-1" text="ecmp-nh-heavy forwarding profile">}} for Spectrum 1 switches
- Upgrade using A/B type of upgrade
- OTLP phase 3
- All packet histogram configuration
- SN5400 - syncE
- SN5400 - ITU-T
- NVUE
  - {{<link url="DHCP-Snooping" text="DHCP snooping commands">}}
  - {{<link url="Link-Layer-Discovery-Protocol" text="Disable LLDP commands">}}
  - {{<link url="Resource-Diagnostics/#disable-lldp" text="Show ASIC resources commands">}} (`cl-resource-query` equivalent)
  - {{<link url="Monitoring-System-Statistics-and-Network-Traffic-with-sFlow" text="sFlow commands">}}
  - {{<link url="DHCP-Servers/#assign-port-based-ip-addresses" text="IPv6 command to assign a port-based DHCP server address">}}
  - {{<link url="Zero-Touch-Provisioning-ZTP" text="Enable ZTP and run ZTP script commands">}}
  - {{<link url="Interface-Configuration-and-Management/#port-ranges" text="Additional port range support for breakout ports and subinterfaces">}}
  - `nv show interface <interface>` commands show the last operational state change for an interface
  - net show interface swX details for dom and optical info for the pluggables
  - L1-show equivalent
  - BGP large communities support
  - match source protocol connected in a route map applied to BGP
  - interface summary view with filtering
  - BGP presentation part 2
  - EVPN presentation - Phase 2
  - net show route summary equivalent
  - Command logging for RADIUS users
  - RADIUS fallback authentication support when server unavailable
  - nv config show --all
  - LSAP encryption
  - Align with common OM - many commands

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.11.

### NVUE Commands After Upgrade

Cumulus Linux 5.11 includes the NVUE object model. After you upgrade to Cumulus Linux 5.11, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
