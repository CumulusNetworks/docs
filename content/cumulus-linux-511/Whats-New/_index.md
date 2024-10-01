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

- The NVIDIA SN5400 switch supports {{<link url="Synchronous-Ethernet-SyncE" text="syncE">}} and {{<link url="Precision-Time-Protocol-PTP/#noise-transfer-servo" text="ITU-T">}}
- {{<link url="Pulse-Per-Second-PPS" text="PPS on the NVIDIA SN5400 switch">}} is now generally available.
- {{<link url="Factory-Reset" text="Factory Reset">}}
- {{<link url="Forwarding-Table-Size-and-Profiles/#spectrum-1" text="ecmp-nh-heavy forwarding profile">}} for Spectrum 1 switches
- {{<link url="Optional-BGP-Configuration/#bgp-prefix-independent-convergence" text="BGP Prefix Independent Convergence">}}
- {{<link url="RADIUS-AAA/#radius-user-command-accounting" text="RADIUS user command accounting">}}
- Upgrade using A/B type of upgrade
- OTLP phase 3
- All packet histogram configuration
- NVUE
  - {{<link url="DHCP-Snooping" text="DHCP snooping commands">}}
  - {{<link url="Link-Layer-Discovery-Protocol" text="Disable LLDP commands">}}
  - {{<link url="Resource-Diagnostics/#disable-lldp" text="Show ASIC resources commands">}} (`cl-resource-query` equivalent)
  - {{<link url="Monitoring-System-Statistics-and-Network-Traffic-with-sFlow" text="sFlow commands">}}
  - {{<link url="DHCP-Servers/#assign-port-based-ip-addresses" text="IPv6 command to assign a port-based DHCP server address">}}
  - {{<link url="Zero-Touch-Provisioning-ZTP" text="Enable ZTP and run ZTP script commands">}}
  - {{<link url="Interface-Configuration-and-Management/#port-ranges" text="Additional port range support for breakout ports and subinterfaces">}}
  - {{<link url="Interface-Configuration-and-Management/#troubleshooting" text="nv show interface <interface>">}} commands now show the date and time the operational state of an interface changes and number of carrier transitions
  - RADIUS fallback authentication support when server unavailable
  - net show interface swX details for dom and optical info for the plugables
  - L1-show equivalent
  - BGP large communities support
  - match source protocol connected in a route map applied to BGP
  - interface summary view with filtering
  - BGP presentation part 2
  - EVPN presentation - Phase 2
  - net show route summary equivalent
  - nv config show --all
  - {{< expand "Changed NVUE Commands" >}}
| New Command | Previous Command |
| ----------- | ----------------|
| nv set system snmp-server<br>nv unset system snmp-server | nv set service snmp-server<br>nv unset service snmp-server |
| nv set system snmp-server state enable<br>nv set system snmp-server state disable| nv set service snmp-server enable on<br>nv set service snmp-server enable off|
| nv show system snmp-server | nv show service snmp-server|
- {{< expand "Deprecated NVUE Commands" >}}
| Deprecated Command | Replace with |
| ----------- | ----------------|
| nv show interface pluggables  | |
| nv show interface <interface> pluggable | |

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.11.

### NVUE Commands After Upgrade

Cumulus Linux 5.11 includes the NVUE object model. After you upgrade to Cumulus Linux 5.11, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
encryption