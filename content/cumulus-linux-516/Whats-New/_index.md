---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.16 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.16, see the {{<link title="Cumulus Linux 5.16 Release Notes" text="Cumulus Linux 5.16 Release Notes">}}.
- To upgrade to Cumulus Linux 5.16, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.16

Cumulus Linux 5.16 contains new features and improvements, and provides bug fixes.

### New Features and Enhancements

- {{<link url="FIPS" text="FIPS">}}
- {{<link url="FRRouting-Log-Message-Reference" text="New FRR high severity ERROR log messages">}}
- You can now use {{<link url="Open-Telemetry-Export" text="Open telemetry export">}} and {{<link url="gNMI-Streaming" text="gNMI streaming">}} at the same time.
- {{<link url="Access-Control-List-Configuration/#clear-control-plane-policer-counters" text="Clear control plane policer counters">}}
- {{<link url="Access-Control-List-Configuration/#match-on-inner-header" text="ACL matches on packet inner header">}} and {{<link url="Access-Control-List-Configuration/#match-on-packet-offset" text="ACL matches on packet offset">}}
- {{<link url="Quality-of-Service/#clear-qos-buffers" text="Clear QoS buffers on multiple interfaces">}}
- {{<link url="Understanding-the-cl-support-Output-File/#automatic-cl-support-file" text="Manage cl-support file cyclic collection">}}
- {{<link url="Network-Troubleshooting/#extended-traceroute" text="Extended traceroute (RFC 5837)">}}
- DHCP relay vrf-aware
- 802.1x on router ports with dynamic VRF assignment
- Security features
- Routing convergence enhancement for EVPN
- Dynamic IPv6 multi tenancy EVPN VXLAN encap in IPv6 header
- BFD offload
- SPC-1 Alligator PSID and CPLD update
- activate authorization without rbash
- 802.1x Related Metric / X-paths support
- Parity between OpenTelemetry and gNMI (Phase 2)
- Same user created locally and on Tacacs server, need NVUE support
- LAG - Random Hash support for Adaptive Routing Eligible Traffic???
- BGP conditional disaggregation for multi-planed GPUs
- BGP Prefix Independent Convergence for Anycast Scenarios
- Health Event and SDK Driver Monitoring for Multi ASIC
- Add Bulk option for route
- Scale up number of BGP paths supported on Cumulus Linux to enable 16K GPU cluster with 128-way ECMP
- NVUE
  - {{<link url="View-Routing-Tables/#show-fib-table-entries" text="Show FIB table entries">}}
  - map port to connector

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.16.

### New, Changed, and Deprecated NVUE Commands

{{%notice warning%}}
To align with a long-term vision of a common interface between Cumulus Linux, Nvidia OS (NVOS), and Host-Based Networking, many NVUE commands in Cumulus Linux 5.16 have changed. Before you upgrade to 5.16, review the following list and be sure to make any necessary changes to your automation.
{{%/notice%}}

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.16 from Cumulus Linux 5.12 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.16 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.15
- Cumulus Linux 5.14
- Cumulus Linux 5.13

To upgrade to Cumulus Linux 5.16 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.16 from 5.12, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.16.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.16 or after a new binary image installation:

1.  Disable NVUE auto save:

   ```
   cumulus@switch:~$ nv set system config auto-save state disabled
   cumulus@switch:~$ nv config apply
   cumulus@switch:~$ nv config save
   ```

2. Delete the `/etc/nvue.d/startup.yaml` file:

   ```
   cumulus@switch:~$ sudo rm -rf /etc/nvue.d/startup.yaml
   ```

3. Add the `PASSWORD_NVUE_SYNC=no` line to the `/etc/default/nvued` file:
   ```
   cumulus@switch:~$ sudo nano /etc/default/nvued
   PASSWORD_NVUE_SYNC=no
   ```

### DHCP Lease with the host-name Option

When a Cumulus Linux switch with NVUE enabled receives a DHCP lease containing the host-name option, it ignores the received hostname and does not apply it. For details, see this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Administration/Hostname-Option-Received-From-DHCP-Ignored" >}}).

### NVUE Commands After Upgrade

After you upgrade to Cumulus Linux, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.

### Cumulus VX

NVIDIA no longer releases Cumulus VX as a standalone image. To simulate a Cumulus Linux switch, use {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/nvidia-air/" text="NVIDIA AIR">}}.
