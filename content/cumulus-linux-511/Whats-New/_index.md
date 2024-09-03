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

- Upgrade using A/B type of upgrade
- Factory Reset
- OTLP phase 3
- Improved interface range behaviors for breakouts
- All packet histogram configuration
- New profile for spectrum1
- SN5400 - syncE
- SN5400 -  ITU-T
- NVUE
  - `nv show interface <interface>> link stats`, commands include the date and time the operational state of an interface changes
  - net show interface swX details for dom and optical info for the pluggables
  - L1-show equivalent
  - DHCP6 server - support static IP by iframe
  - BGP large communities support
  - DHCP snooping
  - control ZTP enable disable
  - enable and disable CDP or LLDP at global and interface level
  - cl-resource-query equivalent
  - match source protocol connected in a route map applied to BGP
  - interface summary view with filtering
  - L# BGP presentation part 2
  - EVPN presentation - Phase 2
  - net show route summary equivalent
  - Command logging for RADIUS users
  - RADIUS fallback authentication support when server unavailable
  - nv config show --all
  - SFlow
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
