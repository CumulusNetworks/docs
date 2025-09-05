---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.15 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.15, see the {{<link title="Cumulus Linux 5.15 Release Notes" text="Cumulus Linux 5.15 Release Notes">}}.
- To upgrade to Cumulus Linux 5.15, first check the {{<link title="#release-considerations" text="Release Considerations">}} below, then follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.15

Cumulus Linux 5.15.0 contains several new features and improvements, and provides bug fixes.

### Platforms

- NVIDIA SN5640

### New Features and Enhancements

- {{<link url="Packet-Trimming/#packet-trimming-counters" text="Packet Trimming counters">}}
- {{<link url="Bidirectional-Forwarding-Detection-BFD" text="FRR-based BFD support">}}
- {{<link url="Optional-BGP-Configuration/#ecmp" text="Support 256 BGP sessions and 256-way ECMP on Spectrum-4">}}
- {{<link url="Latency-Monitoring" text="Switch latency monitoring">}}
- {{<link url="Docker-with-Cumulus-Linux" text="Support for docker-container">}}
- {{<link url="FIPS" text="FIPS mode">}}
- {{<link url="802.1X-Interfaces/#dynamic-ipv6-multi-tenancy" text="802.1x Support for IPv6 tenant isolation">}}
- Require users to re-authenticate when changing authenticators
- Radius user Hardening
- Telemetry
  - You can now run {{<link url="Open-Telemetry-Export" text="OTLP">}} and {{<link url="gNMI-Streaming" text="gNMI streaming">}} at the same time
  - GNMI gNOI support for action commands
  - High frequency telemetry Nsight Integration
  - gNMI & OpenTelemetry  Predictive Analysis for Link Health - FEC histogram data
  - gshut metric via OLTP to track the drained devices/peers to support the site ops with remediation
  - Telemetry ACL Related Metric / X-paths support
  - Telemetry Parity between OpenTelemetry and gNMI (Phase 1)
  - {{< expand "Updated gNMI PHY metric names" >}}
Old Name | New Name|
| -------- | --------- |
| `/interfaces/interface[name]/ethernet/phy/state/effective-errors` | `/interfaces/interface[name]/phy/state/effective-errors` |
| `/interfaces/interface[name]/ethernet/phy/state/received-bits` | `/interfaces/interface[name]/phy/state/received-bits` |
| `/interfaces/interface[name]/ethernet/phy/state/symbol-errors` | `/interfaces/interface[name]/phy/state/symbol-errors` |
| `/interfaces/interface[name]/ethernet/phy/state/fec-time-since-last-clear` | `/interfaces/interface[name]/phy/fec/state/fec-time-since-last-clear` |
| `/interfaces/interface[name]/ethernet/phy/state/corrected-bits` | `/interfaces/interface[name]/phy/fec/state/corrected-bits` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-no-error-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-no-error-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-single-error-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-single-error-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/rs-fec-uncorrectable-blocks` | `/interfaces/interface[name]/phy/fec/state/rs-fec-uncorrectable-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/ber-time-since-last-clear` | `/interfaces/interface[name]/phy/ber/state/ber-time-since-last-clear` |
| `/interfaces/interface[name]/ethernet/phy/state/effective-ber` | `/interfaces/interface[name]/phy/ber/state/effective-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/symbol-ber` | `/interfaces/interface[name]/phy/ber/state/symbol-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/fc-fec-corrected-blocks` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-corrected-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/fc-fec-uncorrected-blocks` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/fc-fec-uncorrected-blocks` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/rs-fec-corrected-symbols` | `/interfaces/interface[name]/phy/channels/channel[id]/fec/state/rs-fec-corrected-symbols` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/raw-ber` | `/interfaces/interface[name]/phy/channels/channel[id]/ber/state/raw-ber` |
| `/interfaces/interface[name]/ethernet/phy/state/lane[lane]/raw-errors` | `/interfaces/interface[name]/phy//channels/channel[id]/state/raw-errors` |
{{< /expand >}}
- NVUE
  - Routing | Operational revision needs to be supported for parts of the CL Object model(Phase 2)
  - Add aging time to neighbor info
  - login brute forcing via API
  - Support for SSH CIPHER configuration
  - Refactor system aaa and tacacs to common model
  - Align system/ntp
  - Align system/message
  - Align system/dns
  - Align system/documentation
  - Align system/security
  - Align system/debug-log
  - Align system/reboot
  - Align system/cpu
  - Align system/memory
  - Align system/packages
  - Align system/events
  - Align system/tech-support
  - Align system/serial-console
  - Align system/telemetry
  - Align system/timezone
  - Align system/"top level"
  - Align system/config
  - Align interface/acl
  - Align interface/ip
  - Align interface/telemetry
  - Align interface/link
  - Align interface/lldp
  - Align interface/pluggable
  - Align interface/counters
  - Align interface/"top level views"
  - Align system/aaa/ldap
  - Align SSH PKA only
  - Unify all the object models to using enabled/disabled (remove on/off)
  - Align timestamp/duration objects across NVUE
  - Align platform/asic
- {{< expand "Removed NVUE commands" >}}
```
nv set interface <interface-id> router ospf bfd enable
nv set interface <interface-id> router ospf bfd detect-multiplier
nv set interface <interface-id> router ospf bfd min-receive-interval 
nv set interface <interface-id> router ospf bfd min-transmit-interval
nv set interface <interface-id> router pim bfd enable
nv set interface <interface-id> router pim bfd detect-multiplier
nv set interface <interface-id> router pim bfd min-receive-interval
nv set interface <interface-id> router pim bfd min-transmit-interval
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval
nv unset interface <interface-id> router ospf bfd enable 
nv unset interface <interface-id> router ospf bfd detect-multiplier 
nv unset interface <interface-id> router ospf bfd min-receive-interval 
nv unset interface <interface-id> router ospf bfd min-transmit-interval 
nv unset interface <interface-id> router pim bfd 
nv unset interface <interface-id> router pim bfd enable 
nv unset interface <interface-id> router pim bfd detect-multiplier 
nv unset interface <interface-id> router pim bfd min-receive-interval 
nv unset interface <interface-id> router pim bfd min-transmit-interval 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd enable 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd detect-multiplier 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-rx-interval 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd min-tx-interval 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd enable 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd detect-multiplier 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-rx-interval 
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd min-tx-interval 
```
{{< /expand >}}
- {{< expand "New NVUE commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show router bfd profile <profile-name>  
nv show vrf <vrf-id> router bgp peer-group <peer-group-id> bfd 
nv show vrf <vrf-id> router bgp neighbor <neighbor-id> bfd 
nv show vrf <vrf-id> router bfd peers 
nv show vrf <vrf-id> router bfd peers --view brief 
nv show vrf <vrf-id> router bfd peers --view standard 
nv show vrf <vrf-id> router bfd peers --view detail 
nv show vrf <vrf-id> router bfd peers --view counters 
nv show vrf <vrf-id> router bfd peers <session-id> 
nv show interface <interface-id> router ospf bfd  
nv show interface <interface-id> router pim bfd  
nv show vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd 
nv show vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set router bfd state
nv set router bfd profile <profile-name>
nv set router bfd profile <profile-name> 
nv set router bfd profile <profile-name> min-rx-interval 
nv set router bfd profile <profile-name> shutdown
nv set router bfd profile <profile-name> passive-mode 
nv set router bfd profile <profile-name> minimum-ttl
nv set vrf <vrf-id> router bgp peer-group <peer-group-id> bfd profile <profile-name> 
nv set vrf <vrf-id> router bgp neighbor <neighbor-id> bfd profile <profile-name>
nv set interface <interface-id> router ospf bfd profile <profile-name> 
nv set interface <interface-id> router pim bfd profile <profile-name> 
nv set vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd profile <profile-name> 
nv set vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd multi-hop
nv set vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd source
nv set vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd profile <profile-name>
nv set vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd multi-hop
nv set vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd source  
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset router bfd profile <profile-name> detect-multiplier 
nv unset router bfd profile <profile-name> min-tx-interval 
nv unset router bfd profile <profile-name> min-rx-interval  
nv unset router bfd profile <profile-name> shutdown 
nv unset router bfd profile <profile-name> passive-mode 
nv unset router bfd profile <profile-name> minimum-ttl 
nv unset vrf <vrf-id> router bgp peer-group <peer-group-id> bfd  
nv unset vrf <vrf-id> router bgp neighbor <neighbor-id> bfd 
nv unset interface <interface-id> router ospf bfd  
nv unset interface <interface-id> router pim bfd 
nv unset vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd 
nv unset vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd multi-hop 
nv unset vrf <vrf-id> router static <ipv4-prefix> via <ipv4> bfd source  
nv unset vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd  
nv unset vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd multi-hop 
nv unset vrf <vrf-id> router static <ipv4-prefix> distance <integer> via <ipv4> bfd source
```

{{< /tab >}}
{{< tab "nv action ">}}

```
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.15.

### Upgrade Requirements

You can use {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="optimized image upgrade">}} to upgrade the switch to Cumulus Linux 5.15 from Cumulus Linux 5.12 and later.

You can use {{<link url="Upgrading-Cumulus-Linux/#package-upgrade" text="package upgrade ">}} to upgrade the switch to Cumulus Linux 5.15 from the following releases. Package upgrade supports ISSU (warm boot) for these upgrade paths.
- Cumulus Linux 5.14.0
- Cumulus Linux 5.13.1
- Cumulus Linux 5.13.0

To upgrade to Cumulus Linux 5.15 from a release that does not support package upgrade or optimized image upgrade, you can install an image with {{<link url="Upgrading-Cumulus-Linux/#image-upgrade" text="ONIE">}}.

### Maximum Number of NVUE Revisions

Cumulus Linux includes an option to set the {{<link url="NVUE-CLI/#maximum-revisions-limit" text="maximum number of revisions">}} after which NVUE deletes older revisions automatically. The default setting is 100. If you upgrade to Cumulus Linux 5.15 from 5.12, the first time you run `nv set` or `nv unset` commands, NVUE deletes older revisions if the number of revisions on the switch is greater than 100.

### Linux Configuration Files Overwritten

If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.15.

NVUE includes a default `startup.yaml` file. In addition, NVUE enables configuration auto save by default. As a result, NVUE overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade, or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.15 or after a new binary image installation:

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
