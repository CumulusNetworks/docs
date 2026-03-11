---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.17 release, and lists new features and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.17, see the {{<link title="Cumulus Linux 5.17 Release Notes" text="Cumulus Linux 5.17 Release Notes">}}.
- To upgrade to Cumulus Linux 5.17, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.17

Cumulus Linux 5.17 contains new features and improvements, and provides bug fixes.

### New Features and Enhancements

- {{<link url="TACACS/#server-side-per-command-authorization" text="TACACS+ Server-side Per-command Authorization">}}
- {{<link url="Quality-of-Service/#lossless-headroom-based-on-small-packet-probability" text="Lossless headroom size based on small packet probability">}} (Beta)
- {{<link url="Quality-of-Service/#dynamic-ecn" text="Dynamic ECN">}} (Beta)
- {{<link url="802.1X-Interfaces/#lldp-on-802.1x-unauthenticated-ports" text="Allow LLDP on 802.1X unauthenticated ports">}}
- {{<link url="Interface-Configuration-and-Management/#link-debounce-timers" text="Interface debounce timer (link dampening)">}}
- {{<link url="Zero-Touch-Provisioning-ZTP/#ztp-over-dhcp" text="Revert to DHCP if the ZTP URL is not reachable">}}
- {{<link url="Bidirectional-Forwarding-Detection-BFD/#bfd-offload" text="BFD offload support for BFD sessions based on the IPv6 link-local address">}}
- Support PFC headroom pool 
- LLDP BGP Route Redistribution Extension (Beta)
- BGP/LLDP X-Plane multi-plane'd GPUs with disjoined planes (EVPN based deployments) (Beta)
- Routing Convergence Enhancement for full connectivity loss (all links Up/restart)
- Integrate logs in tc_log to the syslog​, and update log level
- Granular LLDP TLV definition and control 
- Docker Resource Governance & Policy Agent (GA)
- NVUE
  - {{<link url="Installing-a-New-Cumulus-Linux-Image-with-ONIE/#show-secure-boot-details" text="NVUE command to show secure boot status and details">}}
  - {{<link url="RDMA-over-Converged-Ethernet-RoCE/#verify-roce-configuration" text="nv show interface <interface-id> qos roce counters supports multiple interfaces, including ranges">}}
  - {{<link url="NVUE-CLI/#configuration-commands" text="NVUE prevents configuration changes during long background operations">}}
  - New command to verify a configuration before applying
- Telemetry
  - New OTEL metrics: {{<link url="Open-Telemetry-Export/#interface-statistic-format" text="link debounce">}}, {{<link url="Open-Telemetry-Export/#interface-statistic-format" text="PHY link down">}}, and {{<link url="Open-Telemetry-Export/#control-plane-statistic-format" text="control plane">}}
  - New gNMI metrics: {{<link url="gNMI-Streaming/#metrics" text="PHY link down, link debounce, and control plane">}}
  - {{<link url="Open-Telemetry-Export/#granular-metric-selection" text="OTEL granular metric selection">}} (Beta)
  - Parity between OpenTelemetry and gNMI (Phase 3)
  - High frequency telemetry - Nsight Integration - Phase 2 (Binary format)
- Security
  - {{<link url="RADIUS-AAA/#optional-radius-configuration" text="Support for RADIUS PEAP-GTC authentication type">}}
  - {{<link url="Disk-Management/#erase-data-from-the-disk" text="Extended disk erase to support SED SSDs">}}
  - {{<link url="Disk-Management/#change-the-sed-password" text="Change the SED disk password">}}
  - Alert in the event of an audit processing failure
  - Support "sudo" validation when TACACS server is connected to the default VRF
  - Ability to view Hashed password
  - Request to reauthenticae dot1x supplicant(Phase 2) 

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.17.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.17 from Cumulus Linux 5.15 and later. Package upgrade supports ISSU (warm boot) for these upgrade paths.

To upgrade to Cumulus Linux 5.17 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.17 from 5.12 or earlier, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.17.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.17 or after a new binary image installation:

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
