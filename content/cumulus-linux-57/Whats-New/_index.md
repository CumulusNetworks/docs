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

- Support for Debian 12
- Shared ECMP containers for adaptive routing
- Buffer and bandwidth histograms
- 802.1x support
- PTP PPS In or Out Support
- {{<link url="Supported-Route-Table-Entries/#spectrum-2-and-spectrum-3" text="l2-heavy-v4-lpm">}} forwarding profile
- Route server support for EVPN
- NVUE enhancements include:
  - {{<link url="Port-Security" text="Port Security commands">}}
  - {{<link url="Network-Address-Translation-NAT" text="NAT commands">}}
  - {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="ISSU maintenance mode commands">}}
  - {{<link url="RADIUS-AAA" text="RADIUS AAA commands">}}
  - {{<link url="Interface-Configuration-and-Management/#link-flap-protection" text="Link flap protection ">}} commands
  - MLAG support for PVST & PVRST VLAN-aware bridge mode
  - {{<link title="Setting the Date and Time/#set-the-date-and-time" text="Set time command">}}
  - Add admin state to `nv show interface` output
  - PIM show commands for PIM RP, JOIN, PIM MLAG summary, and MLAG upstream information
  - Show commands to see the {{<link url="Troubleshooting-EVPN" text="VLAN to VNI mapping for all bridges">}} and {{<link url="Troubleshooting-EVPN" text="VLAN to VNI mapping for a specific bridge">}}
  - Replace net show neighbor
  - mlag keyword presentation
  - User permissions
  - Allow unset operations with a key and value
  - Enhanced show config history output
  - API support
  - Provide interface summary view with filtering

{{< expand "New NVUE Commands" >}}

For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.

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

```
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
