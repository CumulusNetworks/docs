---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.5 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.5, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.5, see the {{<link title="Cumulus Linux 5.5 Release Notes" text="Cumulus Linux 5.5 Release Notes">}}.
- To upgrade to Cumulus Linux 5.5, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.5.0
<!-- vale on -->
Cumulus Linux 5.5.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

{{%notice note%}}
Early access features are now called beta features.
{{%/notice%}}
<!--
{{%notice warning%}}
- If you configured breakout ports with NVUE commands in Cumulus Linux 5.3 and earlier, the new port configuration changes might impact your Cumulus Linux 5.5 upgrade. Refer to {{<link url="Switch-Port-Attributes/#important-upgrade-information-for-breakout-ports-and-nvue" text="Important Upgrade Information for Breakout Ports and NVUE">}} for important upgrade information.
- Cumulus Linux 5.4 package upgrade (`apt-upgrade`) does not support warm restart to complete the upgrade; performing an unsupported upgrade can result in unexpected or undesirable behavior, such as a traffic outage. Refer to {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="Package Upgrade">}} for important information about package upgrade and warm restart.
{{%/notice%}}
-->
### Platforms

- NVIDIA SN3750-SX (100G Spectrum-2) is now generally available

### New Features and Enhancements

- 1G support for all NVIDIA Spectrum-2 and Spectrum-3 switches now generally available
- {{<link url="Precision-Time-Protocol-PTP/#ptp-profiles" text="PTP ITU-T G.8275.2 Profile">}}
  <!-- - PPS In or Out-->
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - TACACS+ commands are now generally available
  - {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Fast, cold, and warm">}} restart mode
  - {{<link url="VLAN-aware-Bridge-Mode#mac-address-ageing" text="MAC address aging timer">}}
  - {{<link url="SyncE" text="SyncE">}}
  - {{<link url="Precision-Time-Protocol-PTP#ptp-traffic-shaping" text="PTP traffic shaping">}} for Spectrum 1
  - {{<link url="Netfilter-ACLs/#control-plane-acls" text="Control plane ACLs">}}
  - New commands to {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE" text="show and clear interface counters">}}
  - {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#troubleshooting" text="New OSPF">}} show commands to show interface and neighbor configuration and statistics
  - Updated PBR show commands show operational data
  - Support for the named well known BGP communities for `no-export`, `no-advertise`, and `additive` options.
  - New EVPN commands to show multihoming ESI information and layer 2 nexthop group VTEP IP addresses, and to show remote router MAC addresses and nexthop VTEP
  - Updated EVPN commands show operational data
  - Updated `nv show router nexthop rib` and `nv show vrf <vrf> router nexthop-tracking ip-address` commands show operational data
  - Updated {{<link url="Troubleshooting-BGP" text="nv show vrf <vrf> router bgp neighbor">}} and {{<link url="Troubleshooting-BGP/#show-next-hop-information" text="nv show vrf <vrf> router bgp nexthop">}} commands show operational data
  - Changed commands:
    - The `nv set service dhcp-relay6 <vrf> interface upstream <interface> address <ipv6-address>` command is now `nv set service dhcp-relay6 <vrf> interface upstream <interface> server-address <ipv6-address>`
    - The `nv set service dhcp-relay6 blue interface downstream <interface> address <ipv6-address>` command is now `nv set service dhcp-relay6 blue interface downstream <interface> link-address <ipv6-address>`
    - The `nv set service dhcp-relay <vrf> giaddress-interface` is now `nv set service dhcp-relay <vrf> gateway-interface`
  - New command list:
   {{< tabs "TabID40 ">}}
{{< tab "show commands ">}}

```
Coming soon
```

{{< /tab >}}
{{< tab "set commands ">}}

```
Coming soon
```

{{< /tab >}}
{{< tab "unset commands ">}}

```
Coming soon
```

{{< /tab >}}
{{< /tabs >}}
  
{{%notice info%}}
Cumulus Linux 5.5 includes the NVUE object model. After you upgrade to Cumulus Linux 5.5, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
