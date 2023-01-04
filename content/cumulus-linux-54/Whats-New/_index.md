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

### New Features and Enhancements

- Support for 1G speed on all NVIDIA Spectrum-2 and Spectrum-3 switches
- Port configuration changes; you now {{<link url="Quality-of-Service#ptp-shaping" text="configure port breakouts">}} in the `/etc/cumulus/ports.conf` file and port speed in the `/etc/network/interfaces` file
- {{<link url="Quality-of-Service#ptp-shaping" text="PTP Shaping">}} for Spectrum 1
- {{<link url="SyncE#synce" text="SyncE">}} available for early access
- PTP PPS In or Out
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - User management commands
  - TACACS Plus commands
  - {{<link url="Supported-Route-Table-Entries/#change-forwarding-resource-profiles" text="ASIC Resource Slicing">}} (KVD) commands
  - {{<link url="Link-Layer-Discovery-Protocol/#set-lldp-mode" text="LLDP commands">}} to send either CDP frames only or LLDP frames only
  - EVPN show commands show operational data
  - QoS commands for {{<link url="Quality-of-Service/#shaping" text="egress traffic shaping">}}, {{<link url="Quality-of-Service/#pause-frames" text="link pause">}}, {{<link url="Quality-of-Service/#ingress-cos-or-dscp-for-marking" text="traffic remarking">}}, and advanced buffer configuration
  - BGP commands to {{<link url="Optional-BGP-Configuration#bgp-clear" text="clear a BGP session">}}, {{<link url="Optional-BGP-Configuration#bgp-debug" text="enable debugging">}}, and to show BGP operational information
  - Obfuscated passwords to protect passwords from casual viewing
  - {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Search for a specific configuration">}} in the entire object model
  - Support interactive commands (less, tail -f)
  - Auto save configuration
  - Show version information in configuration output
  - Commit messages with the `nv config apply` command
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
