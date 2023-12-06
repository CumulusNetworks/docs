---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.7 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.7, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.7, see the {{<link title="Cumulus Linux 5.7 Release Notes" text="Cumulus Linux 5.7 Release Notes">}}.
- To upgrade to Cumulus Linux 5.7, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.7.0
<!-- vale on -->
Cumulus Linux 5.7.0 supports new platforms, contains several new features and improvements, and provides bug fixes.

### Platforms

### New Features and Enhancements

- {{<link url="802.1X-Interfaces" text="802.1x support">}}
- {{<link url="MAC-Address-Translation" text="MAC address translation">}}
- {{<link url="ASIC-Monitoring" text="Updated histograms for ASIC monitoring">}}
- {{<link url="Pulse-Per-Second-PPS" text=" Pulse Per Second (PPS) synchronization">}}
- NVUE enhancements include:
  - {{<link url="Port-Security" text="Port security commands">}}
  - {{<link url="Network-Address-Translation-NAT" text="NAT commands">}}
  - {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="ISSU maintenance mode commands">}}
  - {{<link url="RADIUS-AAA" text="RADIUS AAA commands">}}
  - {{<link url="Interface-Configuration-and-Management/#link-flap-protection" text="Link flap protection commands ">}}
  - {{<link title="Spanning Tree and Rapid Spanning Tree - STP" text="MLAG support for PVST & PVRST VLAN-aware bridge mode">}}
  - {{<link title="Setting the Date and Time/#set-the-date-and-time" text="Set date and time command">}}
  - {{<link url="Role-Based-Access-Control" text="Role-based access control">}}
  - {{<link url="NVUE-API/#certificates" text="Manage certificate commands">}} for the NVUE REST API
  - Enhanced {{<link url="NVUE-API/#certificates" text="nv show system api">}} command output to show the certificate used for the API and additional {{<link url="NVUE-API/#certificates" text="nv show system api certificate">}} commands to show information about the certificates installed on the switch.
  - Commands to show {{<link url="Troubleshooting-EVPN" text="VLAN to VNI mapping for all bridges">}} and {{<link url="Troubleshooting-EVPN" text="VLAN to VNI mapping for a specific bridge">}}
  - Commands to show the {{<link url="Address-Resolution-Protocol-ARP/#show-the-arp-table" text="ARP table">}} and {{<link url="Neighbor-Discovery-ND#show-the-ip-neighbor-table" text="ND table">}} and to add static entries to the {{<link url="Address-Resolution-Protocol-ARP/#add-static-arp-table-entries" text="ARP table">}} and {{<link url="Neighbor-Discovery-ND/#add-static-ip-neighbor-table-entries" text="ND table">}}
  - Enhanced {{<link url="NVUE-CLI/#configuration-management-commands" text="show config history">}} command output now in table format
  - Improvements to {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="nv show mlag command outputs">}}
  - FRR now restarts only when you enable or disable a routing protocol, change the BGP ASN, or disable the SNMP server.

{{< expand "Commands that no longer require a switchd restart" >}}

```
nv set/unset system acl mode non-atomic
nv set/unset system acl mode atomic
nv set/unset system forwarding host-route-preference route
nv set/unset system forwarding host-route-preference neighbor
nv set/unset system forwarding host-route-preference route-and-neighbour
nv set/unset nve vxlan encapsulation dscp action
nv set/unset nve vxlan encapsulation dscp value
nv set/unset nve vxlan decapsulation dscp action
nv set/unset interface <interface-id> router adaptive-routing link-utilization-threshold 
nv set/unset router bgp wait-for-install
nv set/unset interface <interface-id> router
```

{{< /expand >}}

{{< expand "Changed Commands" >}}

| Previous Command  |  New Command  |
| ------------ | ------------- |
| `nv set router pim timers keep-alive`| `nv set router pim timers keepalive` |
| `nv set router pim timers rp-keep-alive`| `nv set router pim timers rp-keepalive` |
| `nv set vrf default router pim timers keep-alive`| `nv set vrf default router pim timers keepalive` |
| `nv set vrf default router pim timers rp-keep-alive`| `nv set vrf default router pim timers rp-keepalive` |
| `nv set acl <acl-ID> rule <rule-ID> match ip dest-port <port>` | `nv set acl <acl-ID> rule <rule-ID> match ip <protocol>    dest-port <port>`|
| `nv set acl <acl-ID> rule <rule-ID> match ip source-port <port>`| `nv set acl <acl-ID> rule <rule-ID> match ip <protocol>    source-port <port>` |

{{< /expand >}}

{{< expand "New NVUE Commands" >}}

For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) fCumulus Linux.

{{< tabs "TabID40 ">}}
{{< tab "nv show ">}}

```
nv show
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set
```

{{< /tab >}}
{{< tab "nv unset ">}}

``
nv unset
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action
```

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.7 includes the NVUE object model. After you upgrade to Cumulus Linux 5.7, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
