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

- Upgrade to Python 3.x
- Support Debian 12 (kernel 6.1.x) with its applicable Release kernel
- Flash PSID automatically during Installation of Cumulus Linux
- Ethernet AI | Adaptive routing | Shared AR ECMP containers
- Ethernet AI | Parity with Onyx | Telemetry – buffer histograms and gaps in CLI for the ASIC Monitoring Service 
- Ethernet AI | Buffer and Bandwidth histograms with GUI
- Route Server Support for EVPN
- 802.1x support
- MAC address translation support
- SyncE (Phase adjustment support)
- GA | NVUE | PTP PPS In or Out Support
- New forwarding profile: {{<link url="Supported-Route-Table-Entries/#spectrum-2-and-spectrum-3" text="l2-heavy-v4-lpm">}}
- NVUE enhancements include:
  - {{<link url="Port-Security" text="Port Security commands">}}
  - {{<link url="Network-Address-Translation-NAT" text="NAT commands">}}
  - {{<link url="In-Service-System-Upgrade-ISSU/#maintenance-mode" text="ISSU maintenance mode commands">}}
  - {{<link url="RADIUS-AAA" text="RADIUS AAA">}} commands
  - MLAG support for PVST & PVRST VLAN-aware bridge mode
  - SB-327 Compliance | First-Use API to Change Password
  - Add Admin State to `nv show interface` output
  - {{<link url="Interface-Configuration-and-Management/#link-flap-protection" text="Link flap protection ">}} commands
  - Command to set the time
  - PIM show commands to show PIM RP, JOIN, PIM MLAG summary, and MLAG upstream information
  - Show Command for VLAN/VNI/Bridge Mapping
  - Replace net show neighbor
  - 'mlag' keyword Presentation
  - User Permissions
  - Allow Unset Operations with a Key and Value
  - Enhance Show Config History Output
  - API Support
  - Provide Interface Summary View with filtering

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
