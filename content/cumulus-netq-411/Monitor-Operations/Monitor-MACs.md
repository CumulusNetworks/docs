---
title: MAC Addresses
author: NVIDIA
weight: 870
toc: 3
---
A MAC (media access control) address is a layer 2 construct that uses 48 bits to uniquely identify a network interface controller (NIC) for communication within a network.

With NetQ, you can:

- View MAC addresses across the network and for a given device, VLAN, egress port on a VLAN, and VRR
- View a count of MAC addresses on a given device
- View where MAC addresses have lived in the network (MAC history)
- View commentary on changes to MAC addresses (MAC commentary)
- View events related to MAC addresses

<!-- vale off -->
MAC addresses are associated with switch interfaces. They are classified as:

- **Origin**: MAC address is owned by a particular switch, on one or more interfaces. A MAC address typically has only one origin node. The exceptions are when MLAG is configured, the MAC on the VRR interfaces for the MLAG pair is the same, and when EVPN is configured, the MAC is distributed across the layer 3 gateways.
- **Remote**: MAC address is learned or distributed by the control plane on a tunnel interface pointing to a particular remote location. For a given MAC address and VLAN there is only one first-hop switch (or switch pair), but multiple nodes can have the same remote MAC address.
- **Local** (not origin and not remote): MAC address is learned on a bridge and points to an interface on another switch. If the LLDP neighbor of the interface is a host, then this switch is the first-hop switch where the MAC address is learned. For a given MAC address and VLAN there is only one first-hop switch, except if the switches are part of an MLAG pair, and the interfaces on both switches form a dually or singly connected bond.
<!-- vale on -->

## MAC Commands

Monitor MAC addresses with the following commands. Refer to the {{<link title="show/#netq-show-macs" text="command line reference">}} for additional options, definitions, and examples.

- To view all MAC addresses across the network, use the {{<link title="show/#netq-show-macs" text="netq show macs">}} command.
- To view MAC addresses associated with a VLAN, use the {{<link title="show/#netq-show-macs" text="netq show macs vlan">}} command.
- To view MAC addresses associated with an egress port, use the {{<link title="show/#netq-show-macs" text="netq show macs egress-port">}} command.
- To view all MAC addresses associated with a VRR (virtual router reflector) interface configuration, use the {{<link title="show/#netq-show-interfaces" text="netq show interfaces type macvlan">}} command.
- To view the history of a MAC address, use the {{<link title="show/#netq-show-mac-history" text="netq show mac-history">}} command.
- To view MAC address commentary, use the {{<link title="show/#netq-show-mac-commentary" text="netq show mac-commentary">}} command.

## View MAC Addresses in the UI

The NetQ UI provides a listing of current MAC addresses that you can filter by hostname, timestamp, MAC address, VLAN, or origin. You can sort the list by these parameters and also remote, static, and next hop. To view MAC addresses, open the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu** and search for **MACs**:

{{<figure src="/images/netq/macs-411.png" alt="table listing all devices and their associated MAC addresses" width="1100">}}

From this screen, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}} **Filters** to filter the results by hostname, timestamp, MAC address, VLAN, or origin.

{{<figure src="/images/netq/macs-filter-470.png" alt="filter dialog prompting user to enter a hostname" width="400">}}


## View MAC Address Commentary

You can get more descriptive information about changes to a given MAC address on a specific VLAN. Commentary is available for the following MAC address-related events based on their classification (refer to the definition of these at the beginning of this topic):

<!-- vale off -->
| Event Triggers | Example Commentary |
| --- | --- |
| A MAC address is created, or the MAC address on the interface is changed via the `hwaddress` option in */etc/network/interface* | leaf01 00:00:5e:00:00:03 configured on interface vlan1000-v0 |
| An interface becomes a slave in, or is removed from, a bond | leaf01 00:00:5e:00:00:03 configured on interface vlan1000-v0|
| An interface is a bridge and it inherits a different MAC address due to a membership change | leaf01 00:00:5e:00:00:03 configured on interface vlan1000-v0 |
| A remote MAC address is learned or installed by control plane on a tunnel interface | 44:38:39:00:00:5d learned/installed on vni vni10 pointing to remote dest 10.0.1.34 |
| A remote MAC address is flushed or expires | leaf01 44:38:39:00:00:5d is flushed or expired |
| A remote MAC address moves from behind one remote switch to another remote switch or becomes a local MAC address | leaf02: 00:08:00:00:aa:13 moved from remote dest 27.0.0.22 to remote dest 27.0.0.34 <br> 00:08:00:00:aa:13 moved from remote dest 27.0.0.22 to local interface hostbond2 |
| A MAC address is learned at the first-hop switch (or MLAG switch pair) | leaf04 (and MLAG peer leaf05): 44:38:39:00:00:5d learned on first hop switch, pointing to local interface bond4 |
| A local MAC address is flushed or expires | leaf04 (and MLAG peer leaf05) 44:38:39:00:00:5d is flushed or expires from bond4 |
| A local MAC address moves from one interface to another interface or to another switch | leaf04: 00:08:00:00:aa:13 moved from hostbond2 to hostbond3 <br> 00:08:00:00:aa:13 moved from hostbond2 to remote dest 27.0.0.13 |
<!-- vale on -->

{{<tabs "MAC commentary" >}}

{{<tab "NetQ UI" >}}

To view MAC address commentary:

1. Select the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Search for **MACs**.

3. Select the checkbox next to one of the entries, then select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Open card** above the table.

4. Choose a time range, then click **Continue**.

5. You can scroll through the list to see comments related to the MAC address moves and changes:

   {{<figure src="/images/netq/mac-move-commentary-card.png" alt="MAC move commentary card displaying 7 results from the past 24 hours" width="500">}}

8. (Optional) From here, you can filter the list by a given device by selecting {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}} **Filters**. 

<div style="padding-left: 18px;">A red dot on the filter icon indicates that filtering is active. To remove the filter, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" width="18" height="18">}} again, then click <strong>Clear Filter</strong>.</div>

{{</tab>}}

{{<tab "NetQ CLI" >}}

To see MAC address commentary, use the `netq show mac-commentary` command. The following examples show the commentary seen in common situations.

#### MAC Address Configured Locally

In this example, the 46:38:39:00:00:44 MAC address was configured on the VlanA-1 interface of multiple switches, so we see the MAC configured commentary on each of them.

```
cumulus@server-01:~$ netq show mac-commentary 46:38:39:00:00:44 between now and 1hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Mon Aug 24 2020 14:14:33  leaf11           100    leaf11: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:03  leaf12           100    leaf12: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:19  leaf21           100    leaf21: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:40  leaf22           100    leaf22: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:19  leaf21           1003   leaf21: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:15:40  leaf22           1003   leaf22: 46:38:39:00:00:44 configured on interface VlanA-1
Mon Aug 24 2020 14:16:32  leaf02           1003   leaf02: 00:00:5e:00:01:01 configured on interface VlanA-1
```

#### MAC Address Configured on Server and Learned from a Peer

<!-- vale off -->
In this example, the 00:08:00:00:aa:13 MAC address was configured on server01. As a result, both leaf11 and leaf12 learned this address on the next hop interface serv01bond2 (learned locally), whereas, the leaf01 switch learned this address remotely on vx-34 (learned remotely).
<!-- vale on -->

```
cumulus@server11:~$ netq show mac-commentary 00:08:00:00:aa:13 vlan 1000 between now and 5hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Tue Aug 25 2020 10:29:23  leaf12           1000     leaf12: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf11           1000     leaf11: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf01           1000     leaf01: 00:08:00:00:aa:13 learned/installed on vni vx-34 pointing to remote dest 36.0.0.24
```

#### MAC Address Removed

<!-- vale off -->
In this example the bridge FDB entry for the 00:02:00:00:00:a0 MAC address, interface VlanA-1, and VLAN 100 was deleted impacting leaf11 and leaf12.
<!-- vale on -->

```
cumulus@server11:~$ netq show mac-commentary 00:02:00:00:00:a0 vlan 100 between now and 5hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Mon Aug 24 2020 14:14:33  leaf11           100    leaf11: 00:02:00:00:00:a0 configured on interface VlanA-1
Mon Aug 24 2020 14:15:03  leaf12           100    leaf12: 00:02:00:00:00:a0 learned on first hop switch interface peerlink-1
Tue Aug 25 2020 13:06:52  leaf11           100    leaf11: 00:02:00:00:00:a0 unconfigured on interface VlanA-1
```

#### MAC Address Moved on Server and Learned from a Peer

The MAC address on server11 changed from 00:08:00:00:aa:13. In this example, the MAC learned remotely on leaf01 is now a locally learned MAC address from its local interface swp6. Similarly, the locally learned MAC addresses on leaf11 and leaf12 are now learned from remote dest 27.0.0.22.

```
cumulus@server11:~$ netq show mac-commentary 00:08:00:00:aa:13 vlan 1000 between now and 5hr
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Tue Aug 25 2020 10:29:23  leaf12           1000   leaf12: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf11           1000   leaf11: 00:08:00:00:aa:13 learned on first hop switch interface serv01bond2
Tue Aug 25 2020 10:29:23  leaf01           1000   leaf01: 00:08:00:00:aa:13 learned/installed on vni vx-34 pointing to remote dest 36.0.0.24
Tue Aug 25 2020 10:33:06  leaf01           1000   leaf01: 00:08:00:00:aa:13 moved from remote dest 36.0.0.24 to local interface swp6
Tue Aug 25 2020 10:33:06  leaf12           1000   leaf12: 00:08:00:00:aa:13 moved from local interface serv01bond2 to remote dest 27.0.0.22
Tue Aug 25 2020 10:33:06  leaf11           1000   leaf11: 00:08:00:00:aa:13 moved from local interface serv01bond2 to remote dest 27.0.0.22
```

#### MAC Address Learned from MLAG Pair

In this example, after the local first hop learning of the 00:02:00:00:00:1c MAC address on leaf11 and leaf12, the MLAG exchanged the learning on the dually connected interface serv01bond3.

```
cumulus@server11:~$ netq show mac-commentary 00:02:00:00:00:1c vlan 105 between now and 2d
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Sun Aug 23 2020 14:13:39  leaf11          105    leaf11: 00:02:00:00:00:1c learned on first hop switch interface serv01bond3
Sun Aug 23 2020 14:14:02  leaf12          105    leaf12: 00:02:00:00:00:1c learned on first hop switch interface serv01bond3
Sun Aug 23 2020 14:14:16  leaf11          105    leaf11: 00:02:00:00:00:1c moved from interface serv01bond3 to interface serv01bond3
Sun Aug 23 2020 14:14:23  leaf12          105    leaf12: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
Sun Aug 23 2020 14:14:37  leaf11          105    leaf11: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
Sun Aug 23 2020 14:14:39  leaf12          105    leaf12: 00:02:00:00:00:1c moved from interface serv01bond3 to interface serv01bond3
Sun Aug 23 2020 14:53:31  leaf11          105    leaf11: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
Mon Aug 24 2020 14:15:03  leaf12          105    leaf12: 00:02:00:00:00:1c learned on MLAG peer dually connected interface serv01bond3
```

#### MAC Address Flushed

<!-- vale off -->
In this example, the interface VlanA-1 associated with the 00:02:00:00:00:2d MAC address and VLAN 1008 is deleted, impacting leaf11 and leaf12.
<!-- vale on -->

```
cumulus@server11:~$ netq show mac-commentary 00:02:00:00:00:2d vlan 1008 between now and 5hr 
Matching mac_commentary records:
Last Updated              Hostname         VLAN   Commentary
------------------------- ---------------- ------ --------------------------------------------------------------------------------
Mon Aug 24 2020 14:14:33  leaf11           1008   leaf11:  00:02:00:00:00:2d learned/installed on vni vx-42 pointing to remote dest 27.0.0.22
Mon Aug 24 2020 14:15:03  leaf12           1008   leaf12:  00:02:00:00:00:2d learned/installed on vni vx-42 pointing to remote dest 27.0.0.22
Mon Aug 24 2020 14:16:03  leaf01           1008   leaf01:  00:02:00:00:00:2d learned on MLAG peer dually connected interface swp8
Tue Aug 25 2020 11:36:06  leaf11           1008   leaf11:  00:02:00:00:00:2d is flushed or expired
Tue Aug 25 2020 11:36:06  leaf11           1008   leaf11:  00:02:00:00:00:2d on vni 1008 remote dest changed to 27.0.0.22
```

{{</tab>}}

{{</tabs>}}
