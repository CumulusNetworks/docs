---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.9 release, and lists new platforms, features, and enhancements.

- For a list of all the platforms supported in Cumulus Linux 5.9, see the {{<exlink url="www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Hardware Compatibility List (HCL)">}}.
- For a list of open and fixed issues in Cumulus Linux 5.9, see the {{<link title="Cumulus Linux 5.9 Release Notes" text="Cumulus Linux 5.9 Release Notes">}}.
- To upgrade to Cumulus Linux 5.9, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.
<!-- vale off -->
## What's New in Cumulus Linux 5.9.0
<!-- vale on -->
Cumulus Linux 5.9.0 contains several new features and improvements, and provides bug fixes.

### New Features and Enhancements

- Cumulus Linux upgrade to Debian 12 (bookworm)
- ARP packet path is now handled in hardware to offload most ARP processing and save CPU cycles
- {{<link url="ASIC-Monitoring" text="Latency histogram">}} for ASIC monitoring
- {{<link url="In-Service-System-Upgrade-ISSU/#restart-mode" text="Warmboot support for VXLAN EVPN">}} is now generally available
- Transmit {{<link url="Link-Layer-Discovery-Protocol/#transmit-application-priority-tlvs" text="LLDP application priority TLVs">}}
- {{<link url="Firewall-Rules" text="Firewall rules">}}
- Support Native vtysh/FRR output
- Configure CLI Session Parameters (Pagination and Timeout)
- Interface summary view with filtering
- Admin State added to `nv show interface` output
- Support for Upgrade Mode
- Cumulus Linux includes a default `startup.yaml` file and updated `nvued` defaults
- NVUE commands for LDAP authentication and encryption
- nv show platform command redesign
- Forwarding profiles standardized at 85% KVD utilization
- {{< expand "Improved tab completion for NVUE routing commands" >}}
  ```
  ```
  {{< /expand >}}
- {{< expand "New NVUE Commands" >}}
  For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
  
  {{< tabs "TabID49 ">}}
  {{< tab "nv show ">}}
  
  ```
  ```

  {{< /tab >}}
  {{< tab "nv set ">}}

  ```
  ```
  
  {{< /tab >}}
  {{< tab "nv unset ">}}
  
  ```
  ```

  {{< /tab >}}
  {{< tab "nv action ">}}
  
  ```
  ```

  {{< /tab >}}
  {{< /tabs >}}
  
  {{< /expand >}}

{{%notice note%}}
The repository key stored in Cumulus Linux 5.5.0 and earlier has expired. Before performing a package upgrade to Cumulus Linux 5.9.0 from Cumulus Linux 5.5.0 and earlier, you must install the new key. See [this knowledge base article]({{<ref "/knowledge-base/Installing-and-Upgrading/Upgrading/Update-Expired-GPG-Keys" >}}).
{{%/notice%}}

{{%notice info%}}
Cumulus Linux 5.9 includes the NVUE object model. After you upgrade to Cumulus Linux 5.9, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

Cumulus Linux 3.7, 4.3, and 4.4 continue to support NCLU. For more information, contact your NVIDIA Spectrum platform sales representative.
{{%/notice%}}
