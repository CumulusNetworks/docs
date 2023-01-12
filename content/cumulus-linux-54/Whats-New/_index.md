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

- `/etc/cumulus/ports.conf` configuration changes:
   - New format for {{<link url="Switch-Port-Attributes/#configure-a-breakout-port" text="port breakouts">}}
   - {{<link url="Switch-Port-Attributes/#configure-a-breakout-port" text="Breakout port speed">}} configuration is now in the `/etc/network/interfaces` file
- {{<link url="Switch-Port-Attributes/#configure-port-lanes" text="Port lane">}} and {{<link url="Switch-Port-Attributes/#configure-port-width" text="port width">}} configuration
- 1G support for all NVIDIA Spectrum-2 and Spectrum-3 switches
- {{<link url="Quality-of-Service#ptp-shaping" text="PTP Shaping">}} for Spectrum 1
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - {{<link url="User-Accounts" text="User management">}} commands
  - {{<link url="TACACS" text="TACACS+">}} commands (in Beta)
  - {{<link url="Supported-Route-Table-Entries/#change-forwarding-resource-profiles" text="ASIC Resource Slicing">}} (KVD) commands
  - {{<link url="Link-Layer-Discovery-Protocol/#set-lldp-mode" text="LLDP commands">}} to send either CDP frames only or LLDP frames only
  - QoS commands for {{<link url="Quality-of-Service/#shaping" text="egress traffic shaping">}}, {{<link url="Quality-of-Service/#pause-frames" text="link pause">}}, {{<link url="Quality-of-Service/#ingress-cos-or-dscp-for-marking" text="traffic remarking">}}, and advanced buffer configuration
  - BGP commands to {{<link url="Optional-BGP-Configuration#bgp-clear" text="clear a BGP session">}}, {{<link url="Optional-BGP-Configuration#bgp-debug" text="enable debugging">}}, and to show BGP operational information
  - Operational data in EVPN show commands
  - Obfuscated passwords to protect passwords from casual viewing
  - {{<link url="NVUE-CLI/#search-for-a-specific-configuration" text="Search for a specific configuration">}} in the entire object model
  - {{<link url="NVUE-CLI/#configure-auto-save" text="Auto save configuration">}} option
  - {{<link url="NVUE-CLI/#add-configuration-apply-messages" text="Configuration apply messages">}}
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
