---
title: EVPN
author: NVIDIA
weight: 820
toc: 3
---

Use the UI or CLI to monitor Ethernet VPN (EVPN) on a networkwide or per-session basis. 
## EVPN Commands

Monitor EVPN with the following commands. See the {{<link title="show/#netq-show-evpn" text="command line reference">}} for additional options, definitions, and examples.

```
netq show evpn
netq show events message_type evpn
netq show events-config message_type evpn
```

The {{<link title="check/#netq check evpn" text="netq check evpn">}} command verifies the communication status for all nodes (leafs, spines, and hosts) running instances of EVPN in your network fabric:

```
netq check evpn
```
## View EVPN in the UI

To add the EVPN card to your workbench, navigate to the header and select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Network services&nbsp;<span aria-label="and then">></span> All EVPN Sessions card&nbsp;<span aria-label="and then">></span> Open cards**. In this example, there are 6 nodes running the EVPN service, 0 open events (from the last 24 hours), and 48 VNIs.

{{<figure src="/images/netq/evpn-med-card-450.png" width="200">}}

## View the Distribution of Layer-2 and -3 VNIs and Sessions

To view the number of sessions between devices and Virtual Network Identifiers (VNIs) that occur over layer 3, open the large EVPN Sessions card. In this example, there are 18 layer-3 VNIs.

{{<figure src="/images/netq/evpn-large-outline-450.png" width="650">}}

Select the dropdown to display the switches with the most EVPN sessions, as well as the switches with the most layer-2 and layer-3 EVPN sessions.

{{<figure src="/images/netq/evpn-large-dropdown-450.png" width="500">}}

You can view EVPN-related events by selecting the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/20-Alert/alarm-bell.svg" height="18" width="18"/> **Events** tab.

Expand the EVPN card to full-screen to view, filter, or export:

- A list of switches and their associated VNIs
- The address of the VNI endpoint
- Whether the session is part of a layer 2 or layer 3 configuration
- The associated VRF or VLAN (when defined)
- The export and import route targets used for filtering

{{<figure src="/images/netq/fullscreen-evpn-450.png" width="1300">}}

From this table, you can select a row, then click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** above the table.

NetQ adds a new, EVPN 'single-session' card to your workbench. From this card, you can view the number of VTEPs (VXLAN Tunnel Endpoints) for a given EVPN session as well as the attributes of all EVPN sessions for a given VNI.

## Monitor a Single EVPN Session

The EVPN single-session card displays the number of VTEPs for a given EVPN session (in this case, 48). 

{{<figure src="/images/netq/evpn-single-session-450.png" width="200">}}

Expand the card to display the associated VRF (layer 3) or VLAN (layer 2) on each device participating in this session. The full-screen card displays all stored attributes of all EVPN sessions running networkwide.
## Related Information

- {{<kb_link latest="cl" url="Network-Virtualization/Ethernet-Virtual-Private-Network-EVPN/_index.md" text="Cumulus Linux and EVPN ">}}