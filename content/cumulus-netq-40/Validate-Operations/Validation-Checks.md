---
title: Validation Checks
author: NVIDIA
weight: 1005
toc: 3
---
NetQ provides the information you need to validate the health of your network fabric, devices, and interfaces. Whether you use the NetQ UI or the NetQ CLI to create and run validations, the underlying checks are the same. The number of checks and the type of checks are tailored to the particular protocol or element being validated.

The Test Number column in the tables below is used with the NetQ CLI when you want to include or exclude specific tests with the `netq check` command. You can get the test numbers when you run the `netq show unit-tests` command.

## NetQ Agent Validation Tests

NetQ Agent validation looks for an agent status of Rotten for each node in the network. A *Fresh* status indicates the Agent is running as expected. The Agent sends a heartbeat every 30 seconds, and if three consecutive heartbeats are missed, its status changes to *Rotten*. This is accomplished with the following test:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Agent Health | Checks for nodes that have failed or lost communication |

## BGP Validation Tests

The BGP validation tests look for indications of the session sanity (status and configuration). This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Session Establishment | Checks that BGP sessions are in an established state |
| 1 | Address Families | Checks if transmit and receive address family advertisement is consistent between peers of a BGP session |
| 2 | Router ID | Checks for BGP router ID conflict in the network |

## Cumulus Linux Version Tests

The Cumulus Linux version tests looks for version consistency. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Cumulus Linux Image Version | Checks the following: <ul><li>No version specified, checks that all switches in the network have consistent version</li><li><em>match-version</em> specified, checks that a switch's OS version is equals the specified version</li><li><em>min-version</em> specified, checks that a switch's OS version is equal to or greater than the specified version</li></ul> |

## EVPN Validation Tests

The EVPN validation tests look for indications of the session sanity and configuration consistency. This is accomplished with the following tests:

<!-- vale off -->
| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | EVPN BGP Session | Checks if: <ul><li>BGP EVPN sessions are established</li><li>The EVPN address family advertisement is consistent</li></ul> |
| 1 | EVPN VNI Type Consistency | Because a VNI can be of type L2 or L3, checks that for a given VNI, its type is consistent across the network |
| 2 | EVPN Type 2 | Checks for consistency of IP-MAC binding and the location of a given IP-MAC across all VTEPs |
| 3 | EVPN Type 3 | Checks for consistency of replication group across all VTEPs |
| 4 | EVPN Session | For each EVPN session, checks if: <ul><li><em>adv_all_vni</em> is enabled</li><li>FDB learning is disabled on tunnel interface</li></ul> |
| 5 | VLAN Consistency | Checks for consistency of VLAN to VNI mapping across the network |
| 6 | VRF Consistency | Checks for consistency of VRF to L3 VNI mapping across the network |
| 7 | L3 VNI RMAC | Checks L3 VNI router MAC and SVI |
<!-- vale on -->

## Interface Validation Tests

The interface validation tests look for consistent configuration between two nodes. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Admin State | Checks for consistency of administrative state on two sides of a physical interface |
| 1 | Oper State | Checks for consistency of operational state on two sides of a physical interface |
| 2 | Speed | Checks for consistency of the speed setting on two sides of a physical interface |
| 3 | Autoneg | Checks for consistency of the auto-negotiation setting on two sides of a physical interface |

## Link MTU Validation Tests

The link MTU validation tests look for consistency across an interface and appropriate size MTU for VLAN and bridge interfaces. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Link MTU Consistency | Checks for consistency of MTU setting on two sides of a physical interface |
| 1 | VLAN interface | Checks if the MTU of an SVI is no smaller than the parent interface, substracting the VLAN tag size |
| 2 | Bridge interface | Checks if the MTU on a bridge is not arbitrarily smaller than the smallest MTU among its members |

## MLAG Validation Tests

The MLAG validation tests look for misconfigurations, peering status, and bond error states. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Peering | Checks if: <ul><li>MLAG peerlink is up</li><li>MLAG peerlink bond slaves are down (not in full capacity and redundancy)</li><li>Peering is established between two nodes in a MLAG pair</li></ul> |
| 1 | Backup IP | Checks if: <ul><li>MLAG backup IP configuration is missing on a MLAG node</li><li>MLAG backup IP is correctly pointing to the MLAG peer and its connectivity is available</li></ul> |
| 2 | CLAG Sysmac | Checks if: <ul><li>MLAG Sysmac is consistently configured on both nodes in a MLAG pair</li><li>Any duplication of a MLAG sysmac exists within a bridge domain </li></ul> |
| 3 | VXLAN <!-- vale off -->Anycast IP<!-- vale on --> | Checks if the VXLAN anycast IP address is consistently configured on both nodes in an MLAG pair |
| 4 | Bridge Membership | Checks if the MLAG peerlink is part of bridge |
| 5 | Spanning Tree | Checks if: <ul><li>STP is enabled and running on the MLAG nodes</li><li>MLAG peerlink role is correct from STP perspective</li><li>The bridge ID is consistent between two nodes of a MLAG pair</li><li>The VNI in the bridge has BPDU guard and BPDU filter enabled</li></ul> |
| 6 | Dual Home | Checks for: <ul><li>MLAG bonds that are not in dually connected state</li><li>Dually connected bonds have consistent VLAN and MTU configuration on both sides</li><li>STP has consistent view of bonds' dual connectedness</li></ul> |
| 7 | Single Home | Checks for: <ul><li>Singly connected bonds</li><li>STP has consistent view of bond's single connectedness</li></ul> |
| 8 | Conflicted Bonds | Checks for bonds in MLAG conflicted state and shows the reason |
| 9 | ProtoDown Bonds | Checks for bonds in protodown state and shows the reason |
| 10 | SVI | Checks if: <ul><li>An SVI is configured on both sides of a MLAG pair</li><li>SVI on both sides have consistent MTU setting</li></ul> |

## NTP Validation Tests

The NTP validation test looks for poor operational status of the NTP service. This is accomplished with the following test:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | NTP Sync | Checks if the NTP service is running and in sync state |

## OSPF Validation Tests

The OSPF validation tests look for indications of the service health and configuration consistency. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Router ID | Checks for OSPF router ID conflicts in the network |
| 1 | Adjacency | Checks or OSPF adjacencies in a down or unknown state |
| 2 | Timers | Checks for consistency of OSPF timer values in an OSPF adjacency |
| 3 | Network Type | Checks for consistency of network type configuration in an OSPF adjacency |
| 4 | Area ID | Checks for consistency of area ID configuration in an OSPF adjacency |
| 5 | Interface MTU | Checks for MTU consistency in an OSPF adjacency |
| 6 | Service Status | Checks for OSPF service health in an OSPF adjacency |

## Sensor Validation Tests

The sensor validation tests looks for chassis power supply, fan, and temperature sensors that are in a bad state. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | PSU sensors | Checks for power supply unit sensors that are not in ok state |
| 1 | Fan sensors | Checks for fan sensors that are not in ok state |
| 2 | Temperature sensors | Checks for temperature sensors that are not in ok state |

## VLAN Validation Tests

The VLAN validation tests look for configuration consistency between two nodes. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | Link Neighbor VLAN Consistency | Checks for consistency of VLAN configuration on two sides of a port or a bond |
| 1 | CLAG Bond VLAN Consistency | Checks for consistent VLAN membership of a CLAG (MLAG) bond on each side of the CLAG (MLAG) pair |

## VXLAN Validation Tests

The VXLAN validation tests look for configuration consistency across all VTEPs. This is accomplished with the following tests:

| Test Number | Test Name | Description |
| :---------: | --------- | ----------- |
| 0 | VLAN Consistency | Checks for consistent VLAN to VXLAN mapping across all VTEPs |
| 1 | BUM replication | Checks for consistent replication group membership across all VTEPs |
