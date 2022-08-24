---
title: Network Snapshots
author: NVIDIA
weight: 690
toc: 4
---
Snapshots capture a network's state---including the services running on the network---at a particular point in time. They are helpful when upgrading a switch or modifying its configuration. Comparing snapshots lets you check what (if anything) changed in the network. This section outlines how to create, compare, and interpret snapshots.

## Create a Network Snapshot

To create a snapshot:

1. From the workbench header, select {{<img src="/images/netq/camera.svg" alt="snapshot" width="22.5" height="18">}}, then **Create Snapshot**:

    {{<figure src="/images/netq/create-network-snapshot.png" alt="modal prompting user to create, compare, view, or delete snapshots" width="400">}}

2. Next, enter the snapshot's name, time frame, and the elements you'd like included in the snapshot:

    {{<figure src="/images/netq/create-network-snapshot-enter-name.png" alt="modal prompting user to add name, time frame, and options while creating a snapshot" width="400">}}

To capture the network's current state, click **Now**. To capture the network's state at a previous date and time, click **Past**. In the **Start Time** field, select the calendar icon.

The **Choose options** field includes all the elements and services that may run on the network. All are selected by default. Click any element to remove it from the snapshot. The Node and Services options are required.

The **Notes** field is optional. Here you can add descriptive text to remind you of the snapshot's purpose.

3. Select **Finish**. The card now appears on your workbench.

4. When you are finished viewing the snapshot, click **Dismiss** to remove it from your workbench. You can add it back by selecting {{<img src="/images/netq/camera.svg" alt="snapshot" width="22.5" height="18">}} in the header and navigating to the option to view snapshots. 

## Compare Network Snapshots

You can compare the state of your network before and after an upgrade or other configuration change to help avoid unwanted changes to your network's state. Remember to create a snapshot before you make any changes so that you have a point of comparison.

To compare network snapshots:

1. From the workbench header, click {{<img src="/images/netq/camera.svg" alt="snapshot" width="22.5" height="18">}}.

2. Select **Compare Snapshots**, then select the two snapshots you want to compare.

3. Click **Finish**.

If the snapshot cards are already present on your workbench, place the cards side-by-side for a high-level comparison. For a more detailed comparison, click **Compare** on one of the cards and select a snapshot for comparison from the list.

### Interpreting the Comparison Data

For each network element with changes, a visualization displays the differences between the two snapshots. In the following example, there are changes to the MAC addresses and neighbors. The snapshot taken before the change had a total count of 316 MAC addresses and 873 neighbors. The snapshot taken after the changes has a total count of 320 MAC addresses and 891 neighbors. Between the two totals you can see the number of neighbors added, updated, and removed. This shows four MAC addresses have been added, 9 MAC addresses have been updated, and 18 neighbors have been added.

{{<figure src="/images/netq/snapshot-large-compare-data-interpretation-330.png" width="400">}}

Note that the snapshots' display order determines what is considered added or removed. Compare these two views of the same data:

{{<figure src="/images/netq/snapshot-large-compare-from-modal-oldernewer-330.png" width="500" caption="Most recent snapshot on right">}}

{{<figure src="/images/netq/snapshot-large-compare-from-modal-newerolder-330.png" width="500" caption="Most recent snapshot on left">}}

You can also change which snapshots to compare. Select an alternate snapshot from one or both of the two snapshot dropdowns, then click **Compare**.

From this view, you can dismiss the snapshots or select **View Details** for additional information and to filter and export the data as a JSON file.

The following table describes the information provided for each element type when changes are present:

| Element | Data Descriptions |
| ------- | ----------------- |
| BGP | <ul><li><strong>Hostname</strong>: Name of the host running the BGP session</li><li><strong>VRF</strong>: Virtual route forwarding interface if used</li><li><strong>BGP Session</strong>: Session that was removed or added</li><li><strong>ASN</strong>: Autonomous system number</li></ul> |
| CLAG | <ul><li><strong>Hostname</strong>: Name of the host running the CLAG session</li><li><strong>CLAG Sysmac</strong>: MAC address for a bond interface pair that was removed or added</li></ul> |
| Interface | <ul><li><strong>Hostname</strong>: Name of the host where the interface resides</li><li><strong>IF Name</strong>: Name of the interface that was removed or added</li></ul> |
| IP Address | <ul><li><strong>Hostname</strong>: Name of the host where address was removed or added</li><li><strong>Prefix</strong>: IP address prefix</li><li><strong>Mask</strong>: IP address mask</li><li><strong>IF Name</strong>: Name of the interface that owns the address</li></ul> |
| Links | <ul><li><strong>Hostname</strong>: Name of the host where the link was removed or added</li><li><strong>IF Name</strong>: Name of the link</li><li><strong>Kind</strong>: Bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, or vxlan</li></ul> |
| LLDP | <ul><li><strong>Hostname</strong>: Name of the discovered host that was removed or added</li><li><strong>IF Name</strong>: Name of the interface</li></ul> |
| MAC Address | <ul><li><strong>Hostname</strong>: Name of the host where MAC address resides</li><li><strong>MAC address</strong>: MAC address that was removed or added</li><li><strong>VLAN</strong>: VLAN associated with the MAC address</li></ul> |
| Neighbor | <ul><li><strong>Hostname</strong>: Name of the neighbor peer that was removed or added</li><li><strong>VRF</strong>: Virtual route forwarding interface if used</li><li><strong>IF Name</strong>: Name of the neighbor interface</li><li><strong>IP address</strong>: Neighbor IP address</li></ul> |
| Node | <ul><li><strong>Hostname</strong>: Name of the network node that was removed or added</li></ul> |
| OSPF | <ul><li><strong>Hostname</strong>: Name of the host running the OSPF session</li><li><strong>IF Name</strong>: Name of the associated interface that was removed or added</li><li><strong>Area</strong>: Routing domain for this host device</li><li><strong>Peer ID</strong>: Network subnet address of router with access to the peer device</li></ul> |
| Route | <ul><li><strong>Hostname</strong>: Name of the host running the route that was removed or added</li><li><strong>VRF</strong>: Virtual route forwarding interface associated with route</li><li><strong>Prefix</strong>: IP address prefix</li></ul> |
| Sensors | <ul><li><strong>Hostname</strong>: Name of the host where sensor resides</li><li><strong>Kind</strong>: Power supply unit, fan, or temperature</li><li><strong>Name</strong>: Name of the sensor that was removed or added</li></ul> |
| Services | <ul><li><strong>Hostname</strong>: Name of the host where service is running</li><li><strong>Name</strong>: Name of the service that was removed or added</li><li><strong>VRF</strong>: Virtual route forwarding interface associated with service</li></ul> |

## Related Information

- {{<link title="Back Up and Restore NetQ">}}