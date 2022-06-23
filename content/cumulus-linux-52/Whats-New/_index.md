---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.2 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.2, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.2, see the {{<link title="Cumulus Linux 5.2 Release Notes" text="Cumulus Linux 5.2 Release Notes">}}.
- To upgrade to Cumulus Linux 5.2, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.2.0
<!-- vale on -->
Cumulus Linux 5.2.0 supports new platforms, provides bug fixes, and contains several new features and improvements.

### Platforms

- {{<link url="Interface-Configuration-and-Management/#chassis-management" text="NVIDIA SN4800 (100G Spectrum-3) now generally available">}}
- NVIDIA SN2201 (1G and 100G Spectrum-1)

### New Features and Enhancements

- {{<link url="Precision-Time-Protocol-PTP/#ptp-profiles" text="PTP profiles">}}: ITU-T G.8275.1 and ITU-T G.8275.2
- {{<link url="SyncE" text="SyncE">}}
- `cl-support` file includes WJH event collection
- ECMP performance improvements
- {{<link url="NVUE-Object-Model" text="NVUE">}} enhancements include:
  - Abbreviated commands
  - Tab completion shows the TYPE associated with valid values
  - Tab completion for `nv set` commands indicates if you can create a new instance
  - PTP unicast command
  - {{< expand "New NVUE commands" >}}
  
```
ADD NEW NVUE COMMANDS HERE
```
{{< /expand >}}

{{%notice info%}}
Cumulus Linux 5.2 includes the NVUE object model. After you upgrade to Cumulus Linux 5.2, running NVUE configuration commands replaces the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf` and removes any configuration you add manually or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:

- Update your automation tools to use NVUE.
- {{<link url="NVIDIA-User-Experience-NVUE/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
