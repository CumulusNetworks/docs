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

- 1G (optical) supported with SyncE on the SN5400 switch  
- {{<link url="Upgrading-Cumulus-Linux/#upgrade-cumulus-linux" text="Ability to ugrade from Cumulus Linux 5.11 with Optimized Image Upgrade">}}
- {{<link url="RDMA-over-Converged-Ethernet-RoCE/#roce-single-shared-buffer-pool" text="RoCE single shared buffer pool">}}
- {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown-on-a-peer-group" text="Graceful BGP shutdown on a peer group">}}
- {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#reset-a-transceiver" text="Software module reset">}}
- {{<link url="VLAN-aware-Bridge-Mode/#clear-dynamic-mac-address-entries" text="Clear dynamic MAC address entries from the forwarding database">}}
- {{<link url="Optional-BGP-Configuration/#bgp-prefix-independent-convergence" text="BGP Prefix Independent Convergence">}}
- {{<link url="BGP-Weighted-Equal-Cost-Multipath/#ecmp-resource-sharing-during-next-hop-group-updates" text="ECMP Resource Sharing During Next Hop Group Updates">}}
-  {{<link url="RADIUS-AAA/#radius-user-command-accounting" text="RADIUS user command accounting support for multiple servers with first response option">}}
- {{<link url="Neighbor-Discovery-ND" text="IPV6 Stateless Address Auto-Configuration">}}
- {{<link url="Open-Telemetry-Export/#layer-3-router-statistics" text="OTLP new routing metrics">}}
- Support different sample rate for OTLP exporter destinations
- Create a single CLI service check for OTLP exporters
- Support for defining APT sources
- NVUE
  - {{<link title="Network Troubleshooting/#traceroute" text="Traceroute command">}}
  - {{<link title="Network Troubleshooting/#ping" text="Ping command">}}
  - {{<link title="Troubleshooting Network Interfaces/#monitor-interface-traffic-rate-and-pps" text="Commands to monitor interface traffic rate and PPS">}}
  - {{<link url="Monitoring-Best-Practices/#disk-usage" text="Command to monitor disk usage">}}
  - {{<link url="FRRouting/#look-up-the-route-for-a-destination" text="Look up the route for a destination">}}
  - {{<link url="NVUE-CLI/#filter-nv-show-command-output" text="Filter FRR nv show command output">}}
  - {{<link title="Log Files with NVUE" text="Logging commands">}}
  - {{<link url="NVUE-CLI/#translate-a-configuration-revision-or-file" text="Commands to translate a revision or yaml configuration file">}}
  - {{< expand "Changed NVUE Commands" >}}
| New Commands | Previous Commands |
| ----------- | ----------------|
|  | |
{{< /expand >}}
  - {{< expand "Removed NVUE Commands" >}}
| Removed Commands |
| --------------- |
| `nv set system aaa radius enable` |
| `nv set system aaa ldap ssl ca-list`|

{{< /expand >}}
  - {{< expand "New NVUE Commands" >}}
For descriptions and examples of all NVUE commands, refer to the [NVUE Command Reference]({{<ref "/nvue-reference" >}}) for Cumulus Linux.
{{< tabs "TabID108 ">}}
{{< tab "nv show ">}}

```
nv show interface <interface> rates
nv show interface rates
nv show system disk usage
nv show system log
nv show system log file
nv show system log component

```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set qos roce mode lossless-single-ipool
nv set system counter rates load-interval
nv set vrf <vrf> router bgp peer-group <peer-group-id> graceful-shutdown
nv set vrf <vrf> router bgp address-family <address-family> advertise-origin
nv set vrf <vrf> router bgp address-family <address-family> nhg-per-origin
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset system counter rates load-interval
nv unset vrf <vrf> router bgp peer-group <peer-group-id> graceful-shutdown
nv unset vrf <vrf> router bgp address-family <address-family> advertise-origin
nv unset vrf <vrf> router bgp address-family <address-family> nhg-per-origin
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
nv action ping system <destination>
nv action ping system <destination> count
nv action ping system <destination> interval
nv action ping system <destination> size
nv action ping system <destination> time
nv action ping system <destination> do-not-fragment
nv action ping system <destination> source <source-ip-address>
nv action ping system <destination> vrf
nv action ping system <destination> l3protocol
nv action ping system <destination> source-interface <interface>
nv action traceroute interface <interface> 
nv action traceroute interface <interface> packet_len
nv action traceroute interface <interface> hop-count
nv action traceroute interface <interface> source-address
nv action traceroute interface <interface> protocol
nv action delete system log component <component-name> file <file-name>`
nv action delete system log file <file-name>
nv action upload system log file <file-name> <remote-url-upload>
nv action upload system log component <component-name> file <file-name> <remote-url-upload>
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
