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

- Headroom Size based on the average packet size
- Dynamic ECN (Beta)
- Instant Retransmission System (Beta)
- LLDP BGP Route Redistribution Extension (Beta)
- Open Telemetry  Granular metric selection (Beta)
- BGP/LLDP X-Plane multi-plane'd GPUs with disjoined planes (EVPN based deployments) (Beta)
- Debounce timer for regular interface (Link Dampening)
- Add Secure Boot status to nv show system
- Block NVUE CLI during Long Background Operations
- Security - Alert in the event of an audit processing failure\
- Security - Support organizational requirements to conduct backups of information system documentation
- Support SSD-SED disable in BIOS (Spectrum-6)
- Allow LLDP to work on 802.1X unauthenticated ports 
- Routing Convergence Enhancement for full connectivity loss (all links Up/restart)
- BER monitoring | GSHUT and port down due to error disabled
- Security - Support "sudo" validation when TACACS server is connected to the default VRF 
- Telemetry - amBER Link Down Information (gNMI & OTEL)
- Support For TACACS Per Command Authorization on TACACS Server Instead of Locally 
- Integrate logs in tc_log to the syslog​, and update log level
- NV config verify (User can verify a config before apply
- High frequency telemetry - Nsight Integration - Phase 2 (Binary format) 
- Revert to DHCP if ZTP URL is not reachable in 10 attempts 
- BFD offload to sx-bfd for BFD sessions based on LLA
- Granular LLDP TLV definition and control 
- Ability to view Hashed password
- Parity between OpenTelemetry and gNMI (Phase 3) 
- Support PFC headroom pool 
- Allow user to be able to add multiple interfaces for visibility in buffer "nv show interface swp1s0 qos roce counters"
- Security - Graceful SSD Wipe
- Security - API to change SED password (Cumulus)
- Streaming Telemetry support for system software forwarding counters
- Security  Support PEAP-GTC tunneling for Radius 
- Request to get Missing serial number of the device with GNMI subscription 
- Request to Re authentication of dot1x supplicant(Phase 2) 
- Docker Resource Governance & Policy Agent (GA)

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
