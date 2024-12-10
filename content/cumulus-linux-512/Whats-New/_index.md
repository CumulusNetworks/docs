---
title: What's New
author: NVIDIA
weight: 5
toc: 2
---
This document supports the Cumulus Linux 5.12 release, and lists new platforms, features, and enhancements.
- For a list of open and fixed issues in Cumulus Linux 5.12, see the {{<link title="Cumulus Linux 5.12 Release Notes" text="Cumulus Linux 5.12 Release Notes">}}.
- To upgrade to Cumulus Linux 5.12, follow the steps in {{<link url="Upgrading-Cumulus-Linux">}}.

## What's New in Cumulus Linux 5.12

### Platforms

- SN5610 (800G Spectrum-4)
- SN5400 ITU-T G.82732 Class C compliant

### New Features and Enhancements

- {{<link url="RDMA-over-Converged-Ethernet-RoCE/#roce-single-shared-buffer-pool" text="RoCE single shared buffer pool">}}
- {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown-on-a-peer-group" text="Graceful BGP shutdown on a peer group">}}
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#reset-a-transceiver" text="Software module reset">}}
- {{<link url="VLAN-aware-Bridge-Mode/#clear-dynamic-mac-address-entries" text="Clear dynamic MAC address entries from the forwarding database">}}
- {{<link url="Optional-BGP-Configuration/#bgp-prefix-independent-convergence" text="BGP Prefix Independent Convergence">}}
- {{<link url="BGP-Weighted-Equal-Cost-Multipath/#ecmp-resource-sharing-during-next-hop-group-updates" text="ECMP Resource Sharing During Next Hop Group Updates">}}
- Switch Telemetry Exposure - OTLP(Phase 3)
- OTLP | Support different sample rate per OTLP exporter destination
- Create a single CLI service check for OTLP exporter(s)
- BER monitoring - GSHUT and port down due to error disabled
- Align system/aaa/radius
- Align system/log
- Command logging for RADIUS users (Phase 2)
- IPV6 SLAAC (Stateless Address Auto-Configuration) Support
- Implement flow-control/backpressure between zebra and clients (like bgpd) to handle heavy churn at high scale( EVPN Scenarios)
- SN5400 Hippo | Add SyncE support at 1G (optical)
- NVUE
  - {{<link title="Network Troubleshooting/#print-route-trace-with-traceroute" text="Traceroute command">}}
  - {{<link title="Network Troubleshooting/#check-if-a-host-is-reachable-with-ping" text="Ping command">}}
  - support SPIFFE ID for AAA (Validation)
  - Support for defining APT sources
  - API call for "ls" linux command to list files in a directory
  - Support for defining APT sources
  - Storage Utilization Visibility
  - {{<link url="FRRouting/#look-up-the-route-for-a-destination" text="Look up the route for a destination">}}
  - Show Logging Information
  - View support for API as well as CLI
  - ping command to check the reachability of a destination on a network
  - Filtering based on FRR – Phase-1
  - {{< expand "Changed NVUE Commands" >}}
| New Commands | Previous Commands |
| ----------- | ----------------|
|  | |
{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
| Removed Commands |
| --------------- |
| |

{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```

```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set qos roce mode lossless-single-ipool
nv set vrf <vrf> router bgp peer-group <peer-group-id> graceful-shutdown
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset vrf <vrf> router bgp peer-group <peer-group-id> graceful-shutdown
```

{{< /tab >}}
{{< tab "nv action ">}}

```
nv action clear bridge domain <bridge-id> mac-table dynamic
nv action clear bridge domain <bridge-id> mac-table dynamic interface <interface-id
nv action clear bridge domain <bridge-id> mac-table dynamic vlan <vlan-id>
nv action clear bridge domain <bridge-id> mac-table dynamic interface <interface-id> vlan <vlan-id>
nv action clear bridge domain <domain-id> mac-table dynamic mac <mac-address> vlan <vlan-id>
nv action clear bridge domain <domain-id> mac-table dynamic mac <mac-address> interface <interface-id>
nv action clear bridge domain <domain-id> mac-table dynamic mac <mac-address> vlan <vlan-id interface <interface-id>
nv action lookup vrf <vrf-id> router fib <address-family> <ip-address>
nv action reset platform transceiver <port>
```

{{< /tab >}}
{{< tab "nv config ">}}

```

```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

{{%notice warning%}}
To align with a long-term vision of a common interface between Cumulus Linux, Nvidia OS (NVOS), and Host-Based Networking, certain NVUE commands in Cumulus Linux 5.12 have changed. Before you upgrade to 5.12, review the list of changed and removed NVUE commands above and be sure to make any necessary changes to your automation.
{{%/notice%}}

## Release Considerations

Review the following considerations before you upgrade to Cumulus Linux 5.12.

### Linux Configuration Files Overwritten

{{%notice warning%}}
If you use Linux commands to configure the switch, read the following information before you upgrade to Cumulus Linux 5.12.0 or later.
{{%/notice%}}

Cumulus Linux includes a default NVUE `startup.yaml` file. In addition, NVUE configuration auto save is enabled by default. As a result, Cumulus Linux overwrites any manual changes to Linux configuration files on the switch when the switch reboots after upgrade or you change the `cumulus` user account password with the Linux `passwd` command.

{{%notice note%}}
These issues occur only if you use Linux commands to configure the switch. If you use NVUE commands to configure the switch, these issues do not occur and no action is needed.
{{%/notice%}}

To prevent Cumulus Linux from overwriting manual changes to the Linux configuration files when the switch reboots or when changing the `cumulus` user account password with the `passwd` command, follow the steps below **before** you upgrade to 5.12.0 or later, or after a new binary image installation:

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

Cumulus Linux 5.12 includes the NVUE object model. After you upgrade to Cumulus Linux 5.12, running NVUE configuration commands might override configuration for features that are now configurable with NVUE and removes configuration you added manually to files or with automation tools like Ansible, Chef, or Puppet. To keep your configuration, you can do one of the following:
- Update your automation tools to use NVUE.
- {{<link url="NVUE-CLI/#configure-nvue-to-ignore-linux-files" text="Configure NVUE to ignore certain underlying Linux files">}} when applying configuration changes.
- Use Linux and FRR (vtysh) commands instead of NVUE for **all** switch configuration.
