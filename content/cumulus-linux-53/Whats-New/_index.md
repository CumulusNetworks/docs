---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.3 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.3, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.3, see the {{<link title="Cumulus Linux 5.3 Release Notes" text="Cumulus Linux 5.3 Release Notes">}}.
- To upgrade to Cumulus Linux 5.3, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.3.0
<!-- vale on -->
Cumulus Linux 5.3.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- {{<link url="Interface-Configuration-and-Management/#chassis-management" text="NVIDIA SN4800 (100G Spectrum-3)">}} generally available access
- All NVIDIA Spectrum-2 and Spectrum-3 switches support 1G

### New Features and Enhancements

- Refactor port configuration
- PTP shaper for Spectrum-1
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - user management
  - SNMP Server
  - RoCE options
  - support for switchd knobs
  - add memory and CPU utilization (more info in nv show platform hardware output)
  - BGP phase 1 (additional commands)
  - routing phase 1 (additional route-map commands)
  - FRR Zebra Phase 1
  - WJH commands
  - text obfuscation support
  - support hyphens in more places
  - improved performance
  - add username info to Action command
  - change commands from enable on/off to set enable/unset enable
  - New commands:
   {{< tabs "TabID34 ">}}
{{< tab "show commands ">}}

```
ADD HERE
```

{{< /tab >}}
{{< tab "set commands ">}}

```
ADD HERE
```

{{< /tab >}}
{{< tab "unset commands ">}}

```
ADD HERE
```

{{< /tab >}}
{{< /tabs >}}

{{%notice info%}}
Cumulus Linux 5.3 includes the NVUE object model. After you upgrade to Cumulus Linux 5.3, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
