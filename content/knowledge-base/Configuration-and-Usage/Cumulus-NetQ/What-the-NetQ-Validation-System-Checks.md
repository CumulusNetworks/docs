---
title: What the NetQ Validation System Checks
author: Cumulus Networks
weight: 342
toc: 4
---

Cumulus NetQ provides the information you need to monitor the health of your network fabric, devices, and interfaces. You are able to easily validate the operation and view the configuration across the entire network from switches to hosts to containers.

## Environment

- Cumulus NetQ 2.0 - 2.3

## Issue

With the NetQ CLI, `netq check` commands provide on-demand validation of the various network protocols and services running in your network fabric, looking for inconsistencies in configuration across your fabric, connectivity faults, missing configuration, and so forth, and then display the results for your assessment. You can run them from any node in the network.

The NetQ GUI provides the same capabilities through the Validation Request card.

Both the CLI and GUI enable you to validate relevant operational characteristics for network protocols and services on devices being monitored by NetQ. The validations performed for each protocol and service include:

- **agents**: check for rotten nodes
- **bgp**: session sanity (established, router ID, AFI/SAFI consistency)
- **clag**: peering status, backup IP, system MAC, VXLAN anycast IP, bridge membership checks; list of dual-homed bonds; list of single-homed bonds, protodown bonds, dual-homed bonds in conflict states
- **evpn**: BGP AFI/SAFI consistency; VNI type consistency; VTEP IP reachability; kernel/FRR consistency; source replication list consistency for a layer 2 VNI; VLAN-to-layer-2-VNI mapping consistency; MAC destination consistency; VRF-to-layer-3-VNI mapping consistency
- **interfaces**: port speed, admin/operational state, link flap, plugin module status and link peer identity validation
- **license**: presence and validity of switch license
- **lnv**: vxrd peer database, vxsnd peer database, VNI operational state and head end replication list consistency
- **mtu**: MTU consistency on all links
- **ntp**: NTP sync state
- **ospf**: session sanity (router ID, hello time, dead time, area ID, network type consistency)
- **sensors**: fan, temperature, PSU sensor status
- **vlan**: VLAN list and PVID consistency on links; MLAG peerlink and dual-homed bonds VLAN membership check
- **vxlan**: VLAN-to-VNI mappings; source replication list consistency

To run a validation using the CLI, append one of the bold keywords from the list above to the `netq check` command. For example, `netq check agents` or `netq check evpn`:

```
cumulus@switch:~$ netq check agents
Checked nodes: 25, Rotten nodes: 1
Hostname          Status           Last Changed
----------------- ---------------- -------------------------
leaf01            Rotten           8d:13h:34m:51s
```

In the NetQ GUI, open the Validation Request card, select the validation to run, then click **Run Now**:

{{<img src="/images/knowledge-base/netq_validation_request_card.png" width="600">}}

The corresponding On-demand Validation Result card opens automatically and is populated on completion of the check. For selected protocols and services, you can click **Open \<Protocol or Service Name\> Service Card** to view more detail about the protocol or service health.
