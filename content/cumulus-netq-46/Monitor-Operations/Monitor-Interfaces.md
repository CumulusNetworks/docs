---
title: Interfaces
author: NVIDIA
weight: 840
toc: 3
---
## Physical Interfaces Commands

Use the CLI to monitor OSI Layer 1 physical components on network devices, including interfaces, ports, links, and peers. You can monitor transceivers and cabling deployed per port (interface), per vendor, per part number, and so forth. 

This information can help you:

- Determine which ports are empty versus which ones have cables plugged in to help validate expected connectivity.
- Audit transceiver and cable components by vendor, helping you estimate replacement costs, repair costs, and overall maintenance costs.
- Identify mismatched links.
- Identify when physical layer changes (for example, bonds and links going down or flapping) occurred.

NetQ uses {{<kb_link latest="cl" url="Layer-2/Link-Layer-Discovery-Protocol.md" text="LLDP">}} (Link Layer Discovery Protocol) to collect port information. NetQ can also identify peer ports connected to DACs (Direct Attached Cables) and AOCs (Active Optical Cables) without using LLDP, even if the link is not UP.

View performance and status information about cables, transceiver modules, and interfaces with {{<link title="show/#netq-show-interfaces" text="netq show interfaces physical">}}:

```
netq show interfaces physical 
```

## View Utilization Statistics Networkwide

Utilization statistics can indicate whether resources are becoming dangerously close to their maximum capacity or other, user-defined thresholds. Depending on the function of the switch, the acceptable thresholds can vary.

### Compute Resources Utilization

 View how many compute resources&mdash;CPU, disk, and memory&mdash;the switches on your network consume with {{<link title="show/#netq-show-resource-util" text="netq show resource-util">}}:

```
netq show resource-util 
```
### Port Statistics

 View statistics about a given node and interface, including frame errors, ACL drops, and buffer drops with {{<link title="show/#netq-show-ethtool-stats" text="netq show ethtool-stats">}}:

```
netq show ethtool-stats
```
### Interface Statistics and Utilization

NetQ Agents collect performance statistics every 30 seconds for the physical interfaces on switches in your network. The NetQ Agent does not collect statistics for non-physical interfaces, such as bonds, bridges, and VXLANs. The NetQ Agent collects the following statistics:

- Statistics
    - **Transmit**: tx\_bytes, tx\_carrier, tx\_colls, tx\_drop, tx\_errs, tx\_packets
    - **Receive**: rx\_bytes, rx\_drop, rx\_errs, rx\_frame, rx\_multicast, rx\_packets
- Utilization
    - rx\_util, tx\_util
    - port speed

To view interface statistics and utilization, run the {{<link title="show/#netq-show-interface-stats" text="netq show interface-stats">}} or {{<link title="show/#netq-show-interface-utilization" text="netq show interface-utilization">}} commands:

```
netq show interface-stats 
netq show interface-utilization
```
### ACL Resource Utilization Networkwide

 View incoming and outgoing access control lists (ACLs) configured on all switches and host with {{<link title="show/#netq-show-cl-resource" text="netq show cl-resource acl">}}:

```
netq show cl-resource acl
```
### Forwarding Resources Utilization Networkwide

View forwarding resources on all devices with {{<link title="show/#netq-show-cl-resource" text="netq show cl-resource forwarding">}}:

```
netq show cl-resource forwarding
```
### SSD Utilization Networkwide

For NetQ Appliances that have 3ME3 solid state drives (SSDs) installed (primarily in on-premises deployments), you can view the utilization of the drive on demand. A warning is generated when a drive drops below 10% health, or has more than a 2% loss of health in 24 hours, indicating the need to rebalance the drive. Tracking SSD utilization over time lets you see any downward trend or drive instability before you receive a warning message.

View SDD utilization with {{<link title="show/#netq-show-cl-ssd-util" text="netq show cl-ssd-util">}}:

```
netq show cl-ssd-util
```
### Disk Storage After BTRFS Allocation Networkwide

Customers running Cumulus Linux 3 which uses the BTRFS (b-tree file system) might experience issues with disk space management. This is a known problem of BTRFS because it does not perform periodic garbage collection, or rebalancing. If left unattended, these errors can make it impossible to rebalance the partitions on the disk. To avoid this issue, NVIDIA recommends rebalancing the BTRFS partitions in a preemptive manner, but only when absolutely needed to avoid reduction in the lifetime of the disk. By tracking the state of the disk space usage, users can determine when to rebalance.

For details about when to rebalance a partition, refer to [When to Rebalance BTRFS Partitions]({{<ref "/knowledge-base/Configuration-and-Usage/Storage/When-to-Rebalance-BTRFS-Partitions">}}).

View BTRFS disk utilization with {{<link title="show/#netq-show-cl-btrfs-info" text="netq show cl-btrfs-info">}}:

```
netq show cl-btrfs-info
```
## Link Interface Commands

View interface (link) state, type, count, aliases, and additional information with variations of the {{<link title="show/#netq-show-interfaces" text="netq show interfaces">}} command, including {{<link title="show/#netq-show-interfaces" text="netq show interfaces type">}} and {{<link title="show/#netq-show-events" text="netq show events message_type interfaces">}}:

```
netq show interfaces
netq show interfaces type
netq show events message_type interfaces 
```
The {{<link title="check/#netq check interfaces" text="netq check interfaces">}} command verifies interface communication status for all nodes (leafs, spines, and hosts) or an interface between specific nodes in your network fabric. This command only checks the physical interfaces; it does not check bridges, bonds, or other software constructs.

```
netq check interfaces
```
## View Link Interfaces in the UI 

You can monitor the same information outlined in the section above via the UI by expanding the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}} **Menu**, then selecting **Interfaces**.

## Check for MTU Inconsistencies

The maximum transmission unit (MTU) determines the largest size packet or frame that can be transmitted across a given communication link. When the MTU is not configured to the same value on both ends of the link, communication problems can occur. Use the {{<link title="check/#netq-check-mtu" text="netq check mtu">}} command to verify that the MTU is correctly specified for each link.
