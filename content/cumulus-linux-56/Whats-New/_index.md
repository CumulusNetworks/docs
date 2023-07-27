---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.6 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.6, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.6, see the {{<link title="Cumulus Linux 5.6 Release Notes" text="Cumulus Linux 5.6 Release Notes">}}.
- To upgrade to Cumulus Linux 5.6, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.6.0
<!-- vale on -->
Cumulus Linux 5.6.0 supports new platforms, contains several new features and improvements, and provides bug fixes.

### Platforms

- NVIDIA SN5600 (800G Spectrum-4). This switch only supports 1G on the bonus port.
- NVIDIA SN3750-SX (200G Spectrum-2) is now generally available

### New Features and Enhancements

- {{<link url="Switch-Port-Attributes/#breakout-ports" text="PAM4 encoding ">}} support for the NVIDIA SN4410 switch
- {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Adaptive routing">}} is now generally available and includes these enhancements:
  - {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Multiple adaptive routing profiles">}}
  - {{<link title="Unequal Cost Multipath with BGP Link Bandwidth/#ucmp-and-adaptive-routing" text="BGP UCMP support">}}
  - {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="VXLAN interface support">}}
- {{<link url="Quality-of-Service/#pfc-watchdog" text="QOS PFC watchdog">}} for lossless queues
- {{<link url="Monitoring-System-Hardware" text="Fan airflow direction">}} now shows in NVUE `nv show platform environment fan` command output and Linux `smonctl -v` command output, and a {{<link url="Monitoring-Best-Practices#hardware" text="fan direction mismatch">}} triggers a log message
- {{<link url="Precision-Time-Protocol-PTP#clock-correction-mode" text="PTP one-step clock correction mode">}}
- NVUE enhancements include:
  - PVST and PVRST with VLAN-aware bridges
  - {{<link url="Address-Resolution-Protocol-ARP/#global-timer-settings" text="ARP global timer configuration">}} and {{<link url="Neighbor-Discovery-ND/#global-timer-settings" text="ND global timer configuration">}}
  - {{<link url="SSH-for-Remote-Access" text="SSH commands">}}
  - {{<link url="Virtual-Router-Redundancy-Protocol-VRRP/#show-vrrp-configuration" text="VRRP show commands ">}} show configuration and operational data
  - {{<link url="NVUE-API/#enable-the-nvue-rest-api" text="Enable and Disable external API access">}}
  - Additional {{<link url="Troubleshooting-BGP/#clear-bgp-routes" text="clear BGP route">}} commands to clear all BGP sessions and to refresh routes for all neighbors
  - {{<link url="Protocol-Independent-Multicast-PIM/#clear-pim-state-and-statistics" text="Clear PIM state and statistics">}} commands
  - {{<link url="EVPN-Enhancements/#clear-duplicate-addresses" text="Clear EVPN duplicate address">}} commands
  - {{<link url="Protocol-Independent-Multicast-PIM/#pim-show-commands" text="IGMP group show commands ">}}: `nv show interface <interface-id> ip igmp group` and `nv show interface <interface-id> ip igmp group <static-group-id>`
  - Commands to set the time
  - Changes to `nv show platform` command outputs to improve readability

{{< expand "Changed Commands" >}}
| Previous Command | New Command |
| ---------------- | ----------- |
| | |

{{< /expand >}}

{{< expand "New Commands" >}}

{{< tabs "TabID40 ">}}
{{< tab "nv show commands ">}}

{{< /tab >}}
{{< tab "nv set commands ">}}

{{< /tab >}}
{{< tab "nv unset commands ">}}

{{< /tab >}}
{{< tab "nv action commands ">}}

{{< /tab >}}
{{< /tabs >}}

{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.6 includes the NVUE object model. After you upgrade to Cumulus Linux 5.6, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
