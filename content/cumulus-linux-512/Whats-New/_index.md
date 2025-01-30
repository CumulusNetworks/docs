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

<!-- - SN5610 (800G Spectrum-4)-->
- NVIDIA SN2201M includes an updated Parameter-Set IDentification (PSID) and firmware. You cannot downgrade the switch to 5.11.

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
- {{<link title="User Accounts/#default-roles" text="SPIFFE ID support for user accounts">}}
- Open Telemetry:
  - {{<link url="Open-Telemetry-Export/#system-information-format" text="New system information data">}}
  - {{<link url="Open-Telemetry-Export/#router-statistic-format" text="New router statistics">}}
  - {{<link url="Open-Telemetry-Export/#interface-statistic-format" text="New interface PHY statistics">}}
  - {{<link url="Open-Telemetry-Export/#buffer-statistic-format" text="New buffer statistics">}}
  - {{<link url="Open-Telemetry-Export/#customize-export" text="Export different statistics and sample rates to different destinations">}}
  - {{<link url="Open-Telemetry-Export/#show-telemetry-health-metrics" text="Commands to show telemetry health metrics">}}
- NVUE
  - {{<link title="Network Troubleshooting/#traceroute" text="Traceroute command">}}
  - {{<link title="Network Troubleshooting/#ping" text="Ping command">}}
  - {{<link title="Troubleshooting Network Interfaces/#monitor-interface-traffic-rate-and-pps" text="Commands to monitor interface traffic rate and PPS">}}
  - {{<link url="Monitoring-Best-Practices/#disk-usage" text="Command to monitor disk usage">}}
  - {{<link url="Adding-and-Updating-Packages/#configure-additional-repositories" text="Configure additional package repositories">}}
  - {{<link url="FRRouting/#look-up-the-route-for-a-destination" text="Look up the route for a destination">}}
  - {{<link url="NVUE-CLI/#filter-nv-show-command-output" text="Addtional nv show command filters to filter by protocol, filter by neighbor state, and to filter neighbor details">}}
  - {{<link url="NVUE-API/#retrieve-view-types" text="API support for views with show commands">}}
  - {{<link title="Log Files with NVUE" text="Logging commands">}}
  - {{<link url="NVUE-CLI/#translate-a-configuration-revision-or-file" text="Commands to translate a revision or yaml configuration file">}}
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
nv show system aaa user <user-id> spiffe-id <spiffe-id>
nv show system counter rates
nv show system disk usage
nv show system log
nv show system log file
nv show system log file brief
nv show system log file list
nv show system log file follow
nv show system log file <file-name>nv show system packages
nv show system log file <file-name> brief
nv show system log component
nv show system log component <component-name>
nv show system log component <component-name> file
nv show system log component <component-name> file <file-name>
nv show system packages
nv show system packages key
nv show system packages key <key-id>
nv show system packages repository
nv show system packages repository <repo-url-id>
nv show system packages repository <repo-url-id> distribution
nv show system packages repository <repo-url-id> distribution <repo-dist-id>
nv show system packages repository <repo-url-id> distribution <repo-dist-id> pool
nv show system packages repository <repo-url-id> distribution <repo-dist-id> pool <repo-pool-id>
nv show system telemetry buffer-stats
nv show system telemetry buffer-stats export
nv show system telemetry health
nv show system telemetry health internal-metrics exporters
nv show system telemetry health internal-metrics process
nv show system telemetry health internal-metrics processors
nv show system telemetry health internal-metrics receivers
nv show system telemetry interface-stats class
nv show system telemetry interface-stats class phy
nv show system telemetry stats-group
nv show system telemetry stats-group <stats-group-id>
nv show system telemetry stats-group <stats-group-id> interface-stats
nv show system telemetry stats-group <stats-group-id> interface-stats export
nv show system telemetry stats-group <stats-group-id> buffer-stats
nv show system telemetry stats-group <stats-group-id> buffer-stats export
nv show system telemetry stats-group <stats-group-id> histogram
nv show system telemetry stats-group <stats-group-id> histogram export
nv show system telemetry stats-group <stats-group-id> router
nv show system telemetry stats-group <stats-group-id> router export
nv show system telemetry stats-group <stats-group-id> control-plane-stats
nv show system telemetry stats-group <stats-group-id> control-plane-stats export
nv show system telemetry stats-group <stats-group-id> platform-stats
nv show system telemetry stats-group <stats-group-id> platform-stats export
nv show system telemetry stats-group <stats-group-id> platform-stats class
nv show system telemetry stats-group <stats-group-id> platform-stats class cpu
nv show system telemetry stats-group <stats-group-id> platform-stats class disk
nv show system telemetry stats-group <stats-group-id> platform-stats class file-system
nv show system telemetry stats-group <stats-group-id> platform-stats class environment-sensor
nv show system telemetry stats-group <stats-group-id> platform-stats class memory
nv show system telemetry router
nv show system telemetry router export
nv show system telemetry router bgp
nv show system telemetry router bgp export
nv show system telemetry router rib
nv show system telemetry router rib export
nv show system telemetry router vrf
nv show system telemetry router vrf <vrf-id>
nv show system telemetry router vrf <vrf-id> bgp
nv show system telemetry router vrf <vrf-id> bgp export
nv show system telemetry router vrf <vrf-id> bgp peer
nv show system telemetry router vrf <vrf-id> bgp peer <neighbor-id>
nv show system telemetry router vrf <vrf-id> bgp peer <neighbor-id> export
nv show system telemetry router vrf <vrf-id> rib
nv show system telemetry router vrf <vrf-id> rib export
```

{{< /tab >}}
{{< tab "nv set ">}}

```
nv set system aaa radius accounting send-records
nv set system aaa user <user-id> spiffe-id <spiffe-id>
nv set system counter rates load-interval
nv set system packages repository <repository> distribution <distribution> pool <pool>
nv set system packages repository <repository> insecure
nv set system packages repository <repository> key <key>
nv set system packages repository <repository> source
nv set system packages use-vrf
nv set system telemetry export otlp grpc destination <destination-id> stats-group <value>
nv set system telemetry buffer-stats export state
nv set system telemetry buffer-stats sample-interval
nv set system telemetry interface-stats class phy state
nv set system telemetry router bgp export state
nv set system telemetry router rib export state
nv set system telemetry router sample-interval <interval>
nv set system telemetry router vrf <vrf> bgp export state
nv set system telemetry router vrf <vrf> bgp peer <peer-id> export state
nv set system telemetry router vrf <vrf> rib export state
nv set system telemetry router bgp export state
nv set system telemetry stats-group <stats-group-id>
nv set system telemetry stats-group <stats-group-id> interface-stats export state 
nv set system telemetry stats-group <stats-group-id> interface-stats sample-interval 
nv set system telemetry stats-group <stats-group-id> buffer-stats export state 
nv set system telemetry stats-group <stats-group-id> buffer-stats sample-interval 
nv set system telemetry stats-group <stats-group-id> histogram export state 
nv set system telemetry stats-group <stats-group-id> router export state 
nv set system telemetry stats-group <stats-group-id> router sample-interval <interval>
nv set system telemetry stats-group <stats-group-id> control-plane-stats export state
nv set system telemetry stats-group <stats-group-id> control-plane-stats sample-interval 
nv set system telemetry stats-group <stats-group-id> platform-stats export state
nv set system telemetry stats-group <stats-group-id> platform-stats export sample-interval
nv set system telemetry stats-group <stats-group-id> platform-stats class cpu state 
nv set system telemetry stats-group <stats-group-id> platform-stats class cpu sample-interval 
nv set system telemetry stats-group <stats-group-id> platform-stats class disk state
nv set system telemetry stats-group <stats-group-id> platform-stats class disk sample-interval
nv set system telemetry stats-group <stats-group-id> platform-stats class file-system state 
nv set system telemetry stats-group <stats-group-id> platform-stats class file-system sample-interval
nv set system telemetry stats-group <stats-group-id> platform-stats class environment-sensor state
nv set system telemetry stats-group <stats-group-id> platform-stats class environment-sensor sample-interval 
nv set system telemetry stats-group <stats-group-id> platform-stats class memory state 
nv set system telemetry stats-group <stats-group-id> platform-stats class memory sample-interval 
nv set qos roce mode lossless-single-ipool
nv set vrf <vrf> router bgp peer-group <peer-group-id> graceful-shutdown
nv set vrf <vrf> router bgp address-family <address-family> advertise-origin
nv set vrf <vrf> router bgp address-family <address-family> nhg-per-origin
```

{{< /tab >}}
{{< tab "nv unset ">}}

```
nv unset system aaa radius accounting send-records
nv unset system aaa user <user-id> spiffe-id <spiffe-id>
nv unset system counter rates load-interval
nv unset system packages repository <repository> distribution <distribution> pool <pool>
nv unset system packages repository <repository> insecure
nv unset system packages repository <repository> key <key>
nv unset system packages repository <repository> source
nv unset system packages use-vrf
nv unset system telemetry export otlp grpc destination <destination-id> stats-group <value>
nv unset system telemetry buffer-stats export state
nv unset system telemetry buffer-stats sample-interval
nv unset system telemetry interface-stats class phy state
nv unset system telemetry router bgp export state
nv unset system telemetry router rib export state
nv unset system telemetry router sample-interval <interval>
nv unset system telemetry router vrf <vrf> bgp export state
nv unset system telemetry router vrf <vrf> bgp peer <peer-id> export state
nv unset system telemetry router vrf <vrf> rib export state
nv unset system telemetry router bgp export state
nv unset system telemetry stats-group <stats-group-id>
nv unset system telemetry stats-group <stats-group-id> interface-stats export state 
nv unset system telemetry stats-group <stats-group-id> interface-stats sample-interval 
nv unset system telemetry stats-group <stats-group-id> buffer-stats export state 
nv unset system telemetry stats-group <stats-group-id> buffer-stats sample-interval 
nv unset system telemetry stats-group <stats-group-id> histogram export state 
nv unset system telemetry stats-group <stats-group-id> router export state 
nv unset system telemetry stats-group <stats-group-id> router sample-interval <interval>
nv unset system telemetry stats-group <stats-group-id> control-plane-stats export state
nv unset system telemetry stats-group <stats-group-id> control-plane-stats sample-interval 
nv unset system telemetry stats-group <stats-group-id> platform-stats export state
nv unset system telemetry stats-group <stats-group-id> platform-stats export sample-interval
nv unset system telemetry stats-group <stats-group-id> platform-stats class cpu state 
nv unset system telemetry stats-group <stats-group-id> platform-stats class cpu sample-interval 
nv unset system telemetry stats-group <stats-group-id> platform-stats class disk state
nv unset system telemetry stats-group <stats-group-id> platform-stats class disk sample-interval
nv unset system telemetry stats-group <stats-group-id> platform-stats class file-system state 
nv unset system telemetry stats-group <stats-group-id> platform-stats class file-system sample-interval
nv unset system telemetry stats-group <stats-group-id> platform-stats class environment-sensor state
nv unset system telemetry stats-group <stats-group-id> platform-stats class environment-sensor sample-interval 
nv unset system telemetry stats-group <stats-group-id> platform-stats class memory state 
nv unset system telemetry stats-group <stats-group-id> platform-stats class memory sample-interval 
nv unset qos roce mode lossless-single-ipool
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
nv action delete system log component <component-name> file <file-name>`
nv action delete system log file <file-name>
nv action delete system packages key <key>
nv action fetch system packages key <key>
nv action fetch system packages key <key> scope
nv action fetch system image files
nv action lookup vrf <vrf-id> router fib <address-family> <ip-address>
nv action ping system <destination>
nv action ping system <destination> count
nv action ping system <destination> interval
nv action ping system <destination> size
nv action ping system <destination> wait
nv action ping system <destination> do-not-fragment
nv action ping system <destination> source <source-ip-address>
nv action ping system <destination> vrf
nv action ping system <destination> l3protocol
nv action ping system <destination> source-interface <interface>
nv action reset platform transceiver <port>
nv action traceroute interface <interface> 
nv action traceroute interface <interface> packet_len
nv action traceroute interface <interface> hop-count
nv action traceroute interface <interface> source-address
nv action traceroute interface <interface> protocol
nv action upload system log component <component-name> file <file-name> <remote-url-upload>
nv action upload system log file <file-name> <remote-url-upload>
```

{{< /tab >}}
{{< tab "nv config ">}}

```
nv config translate revision
nv config translate filename <filename>
```

{{< /tab >}}
{{< /tabs >}}
{{< /expand >}}

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
