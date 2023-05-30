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

{{%notice note%}}
Early access features are now called beta features.
{{%/notice%}}

### Platforms

### New Features and Enhancements

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
