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

- {{<link url="Bidirectional-Forwarding-Detection-BFD/#bfd-offload" text="BFD offload">}}
- {{<link url="Optional-BGP-Configuration/#bgp-conditional-disaggregation" text="BGP conditional disaggregation">}}
- {{<link url="Optional-BGP-Configuration/#bgp-pic-in-a-multiplane-topology" text="BGP PIC in a multiplane topology">}}
- {{<link url="Understanding-the-cl-support-Output-File/#automatic-cl-support-file" text="Manage automatic cl-support file generation">}}
- {{<link url="Network-Troubleshooting/#extended-traceroute" text="Extended traceroute (RFC 5837)">}}
- {{<link url="Routing-Tables/#show-fib-table-entries" text="Show FIB table entries">}}
- {{<link url="FRRouting-Log-Message-Reference" text="New FRR high severity ERROR log messages">}}
- {{<link url="Access-Control-List-Configuration/#match-on-inner-header" text="ACL matches on packet inner header">}} and {{<link url="Access-Control-List-Configuration/#match-on-packet-offset" text="ACL matches on packet offset">}}
- {{<link url="Quality-of-Service/#clear-qos-buffers" text="Clear QoS buffers on multiple interfaces">}}
- {{<link url="TACACS/#tacacs-per-command-authorization" text="TACACS per-command authorization supports NVUE tab completion, option listing (?), and command history navigation">}}
- {{<link url="DHCP-Relays/#dhcp-relay-for-ipv4-in-an-evpn-symmetric-environment-with-mlag" text="VRF-aware DHCP relay">}}
- {{<link url="Ethernet-Virtual-Private-Network-EVPN/#key-features" text="Support for EVPN VXLAN over an IPv6 underlay">}}
- {{<link url="Access-Control-List-Configuration/#clear-control-plane-policer-counters" text="Clear control plane policer counters">}}
- {{<link url="Equal-Cost-Multipath-Load-Sharing/#lag-hash-randomizer" text="LAG hash randomizer for adaptive routing">}}
- {{<link url="Interface-Configuration-and-Management/#tx-squelch-control" text="Tx squelch control">}}
- {{<link url="802.1X-Interfaces/#dynamic-vrf-assignment" text="802.1x dynamic VRF assignment">}}
- {{<link url="TACACS/#local-fallback-authentication" text="NVUE support for TACACS local fallback authentication">}}
- {{<link url="802.1X-Interfaces/#802.1x-reauthentication" text="802.1X reauthentication">}}
- {{<link url="802.1X-Interfaces/#preserve-dynamically-assigned-ipv6-addresses" text="802.1X preserve dynamically assigned IPv6 addresses">}}
- PPS mode for egress shapers
- Health Event and SDK Driver Monitoring for Multi ASIC
- Allow gNMI to export current egress buffer occupancy, preferable buffer occupancy histogram
- Security features:
  - {{<link url="FIPS" text="FIPS mode">}}
  - {{<link url="SSH-for-Remote-Access/#configure-timeouts-and-sessions" text="Maximum SSH sessions allowed for a user and     for a user group">}}
  - {{<link url="RADIUS-AAA/#required-radius-client-configuration" text="Yubikey authentication over RADIUS">}}
  - {{<link url="Syslog/#enable-secured-logs" text="Configure syslog messages">}} to include the date and time events occur, the source IP and username for NVUE commands, and when dynamic kernel modules load and unload
- Telemetry
  - You can now use {{<link url="Open-Telemetry-Export" text="Open telemetry export">}} and {{<link url="gNMI-Streaming" text="gNMI streaming">}} at the same time.
  - 802.1X {{<link url="Open-Telemetry-Export/#802.1x-statistic-format" text="OTEL metrics">}} and {{<link url="gNMI-Streaming/#metrics" text="gNMI metrics">}}
  - {{<link url="gNMI-Streaming/#metrics" text="New gNMI interface metrics">}} (`/interfaces/interface[name]/state/description`, `/interfaces/interface[name]/state/transceiver`)
  - {{<link url="gNMI-Streaming/#metrics" text="New gNMI QoS buffer metrics">}}
  - Parity between OpenTelemetry and gNMI (Phase 2)
  - YANG Browser Tool for YANG models

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.16.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#optimized-image-upgrade" text="optimized image upgrade">}} and {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.16 from Cumulus Linux 5.13 and later. Package upgrade supports ISSU (warm boot) for these upgrade paths.

To upgrade to Cumulus Linux 5.16 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#onie-image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.16 from 5.12or earlier, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

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
