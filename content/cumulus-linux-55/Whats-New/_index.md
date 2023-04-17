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

- {{<link url="Switch-Port-Attributes/#breakout-ports" text="1G support">}} for all NVIDIA Spectrum-2 and Spectrum-3 switches now generally available
- {{<link url="Precision-Time-Protocol-PTP/#ptp-profiles" text="PTP ITU-T G.8275.2 Profile">}}
- {{<link url="SyncE" text="SyncE">}}
- {{<link url="Precision-Time-Protocol-PTP#ptp-traffic-shaping" text="PTP traffic shaping">}} for Spectrum 1
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="TACACS" text="TACACS+">}} commands are now generally available
  - {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Fast, cold, and warm">}} restart mode
  - {{<link url="VLAN-aware-Bridge-Mode#mac-address-ageing" text="MAC address aging timer">}}
  - {{<link url="Netfilter-ACLs/#control-plane-acls" text="Control plane ACLs">}}
  - New commands to {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE" text="show and clear interface counters">}}
  - New OSPF commands to {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#troubleshooting" text="show interface and neighbor configuration and statistics">}}, and {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#clear-ospf-counters" text="clear OSPF interface statistics">}}
  - New command to {{<link url="Route-Filtering-and-Redistribution/#clear-matches-against-a-route-map" text="clear matches against a route map">}}
  - New {{<link url="Troubleshooting-BGP/#clear-bgp-counters" text="BGP clear commands">}} to clear BGP counters
  - New commands to {{<link url="Precision-Time-Protocol-PTP/#ptp-configuration-and-status" text="show PTP counters">}}
  - New EVPN commands to show {{<link url="EVPN-Multihoming/#troubleshooting" text="multihoming ESI information">}}, layer 2 nexthop group VTEP IP addresses, remote router MAC addresses, and nexthop VTEPs
  - Updated EVPN commands show operational data
  - Updated {{<link url="Policy-based-Routing/#troubleshooting" text="PBR commands">}} show operational data
  - Updated `nv show router nexthop rib` and `nv show vrf <vrf> router nexthop-tracking ipv4|ipv6 ip-address` commands show operational data
  - Updated {{<link url="Troubleshooting-BGP" text="nv show vrf <vrf> router bgp neighbor">}} and {{<link url="Troubleshooting-BGP/#show-next-hop-information" text="nv show vrf <vrf> router bgp nexthop">}} commands show operational data
  - Support for the {{<link url="Optional-BGP-Configuration/#bgp-community-lists" text="named well known BGP communities">}} for `no-export`, `no-advertise`, and `additive` options

{{< expand "Updated commands" >}}
| Previous Command | New Command |
| ---------------- | ----------- |
| `nv set service dhcp-relay6 <vrf> interface upstream <interface> address <ipv6-address>`| `nv set service dhcp-relay6 <vrf> interface upstream <interface> server-address <ipv6-address>` |
| `nv set service dhcp-relay6 <vrf> interface downstream <interface> address <ipv6-address>` | `nv set service dhcp-relay6 <vrf> interface downstream <interface> server-address <ipv6-address>` |
| `nv set service dhcp-relay <vrf> giaddress-interface`| `nv set service dhcp-relay <vrf> gateway-interface`|
| `nv show interface <intf> ptp counters` | `nv show interface <intf> counters ptp`|
{{< /expand >}}

{{< expand "New Commands" >}}
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

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.5 includes the NVUE object model. After you upgrade to Cumulus Linux 5.5, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
