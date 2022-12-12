---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.4 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.4, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.4, see the {{<link title="Cumulus Linux 5.4 Release Notes" text="Cumulus Linux 5.4 Release Notes">}}.
- To upgrade to Cumulus Linux 5.4, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.4.0
<!-- vale on -->
Cumulus Linux 5.4.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- NVIDIA SN3750-SX (200G Spectrum-2) generally available
- Support 1G for all Spectrum-2 and Spectrum-3 switches

### New Features and Enhancements

- Port configuration changes
- {{<link url="Quality-of-Service#" text="PTP Shaping">}} for Spectrum 1
- {{<link url="SyncE#synce" text="SyncE">}} available for early access
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - User management
  - TACACS Plus
  - PTP PPS In or Out Support
  - ASIC Resource Slicing (KVD)
  - LLDP Ability to set CDP-only/LLDP-only TX/RX
  - EVPN Phase 1 - EVPN Operational OM for VNI, MAC/Neigh and RIB
  - NVUE Feature gaps on CL in comparison to Onyx - QoS Phase 2
  - BGP Phase 2
  - Obfuscated passwords to protect passwords from casual viewing
  - {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Search for a specific configuration">}} in the entire object model
  - New commands:
   {{< tabs "TabID40 ">}}
{{< tab "show commands ">}}

Coming soon

{{< /tab >}}
{{< tab "set commands ">}}

Coming soon

{{< /tab >}}
{{< tab "unset commands ">}}

Coming soon

{{< /tab >}}
{{< /tabs >}}
  
{{%notice info%}}
Cumulus Linux 5.3 includes the NVUE object model. After you upgrade to Cumulus Linux 5.3, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
