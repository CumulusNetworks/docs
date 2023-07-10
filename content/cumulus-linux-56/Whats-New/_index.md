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

- Adaptive routing enhancements include:
  - {{<link url="Equal-Cost-Multipath-Load-Sharing-Hardware-ECMP/#adaptive-routing" text="Multiple adaptive routing profiles">}}
  - BGP WCMP for adaptive routing enabled traffic
  - Adaptive routing for RoCE with VXLAN
- {{<link url="Quality-of-Service/#pfc-watchdog" text="QOS PFC watchdog">}} for lossless queues
- Indication for secure firmware boot failure
- Deterministic warm boot switchover
- {{<link url="Monitoring-System-Hardware" text="Fan direction">}} now shows in NVUE and Linux `smonctl -v` command output, and a {{<link url="Monitoring-Best-Practices#hardware" text="fan direction mismatch">}} triggers a log message
- Service password-encryption support for BGP and OSPF in FRR - integration
- {{<link url="Precision-Time-Protocol-PTP#clock-correction-mode" text="PTP one-step clock correction mode">}}
- NVUE enhancements include:
  - PVST and PVRST with VLAN-aware bridges
  - {{<link url="EVPN-Enhancements/#timer-settings" text="ARP and ND timer configuration">}}
  - Support templating SSH service options
  - VRRP operational data
  - {{<link url="NVUE-API/#enable-the-nvue-rest-api" text="Enable and Disable external API access">}}
  - Clear operation for all routing protocols
  - IGMP commands
  - Commands to set the time
  - Platform keyword presentation

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
