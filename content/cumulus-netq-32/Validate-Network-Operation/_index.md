---
title: Validate Network Operation
author: Cumulus Networks
weight: 1000
toc: 2
---
NetQ provides the information you need to validate the operation and configuration of your network fabric, devices, interfaces, and containers. For example, you can validate the operation of routing protocols and virtual network configurations, the status of NetQ Agents and hardware components, and the operation and efficiency of interfaces.

With NetQ, you can view the overall health of your network at a glance and then delve deeper for periodic checks or as conditions arise that require attention. When issues are present, NetQ makes it easy to identify and resolve them. You can also see when changes have occurred to the network, devices, and interfaces by viewing their operation, configuration, and status at an earlier point in time.

NetQ enables you to validate the:

- Overall health of the network
- Operation of the network protocols and services running in your network (either on demand or on a scheduled basis)
- Configuration of physical layer protocols and services

Validation support is available in the NetQ UI and the NetQ CLI as shown here.

| Item | NetQ UI | NetQ CLI |
| --- | :---: | :---: |
| Agents | Yes | Yes |
| BGP | Yes | Yes |
| Cumulus Linux version | No | Yes |
| EVPN | Yes | Yes |
| Interfaces | Yes | Yes |
| License | Yes | Yes |
| LLDP | No | Yes |
| MLAG (CLAG) | Yes | Yes |
| MTU | Yes | Yes |
| NTP | Yes | Yes |
| OSPF | Yes | Yes |
| Sensors | Yes | Yes |
| VLAN | Yes | Yes |
| VXLAN | Yes | Yes |

The NetQ UI uses the following cards to create validations and view results for these protocols and services:

- Network Health
- Validation Request
- On-demand and Scheduled Validation Results

For a general understanding of how well your network is operating, the Network Health card workflow is the best place to start as it contains the highest-level view and performance roll-ups. Refer to the {{<link title="NetQ UI Card Reference" text="NetQ UI Card Reference">}} for details about the components on these cards.

The NetQ CLI uses the `netq check` commands to validate the various elements of your network fabric, looking for inconsistencies in configuration across your fabric, connectivity faults, missing configuration, and so forth, and then display the results for your assessment. They can be run from any node in the network.
