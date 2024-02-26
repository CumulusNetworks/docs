---
title: Network Snapshots
author: NVIDIA
weight: 690
toc: 4
---
Snapshots capture a network's state---including the services running on the network---at a particular point in time. Comparing snapshots lets you check what (if anything) changed in the network, which can be helpful when upgrading a switch or modifying its configuration. This section outlines how to create, compare, and interpret snapshots.

## Create a Network Snapshot

To create a snapshot:

1. From the workbench header, select {{<img src="/images/netq/camera.svg" alt="snapshot" width="22.5" height="18">}} **Snapshot**, then **Create snapshot**.

2. Next, enter the snapshot's name, time frame, and the elements you'd like included in the snapshot:

    {{<figure src="/images/netq/create-a-snapshot-490.png" alt="modal prompting user to add name, time frame, and options while creating a snapshot" width="400">}}

    To capture the network's current state, click **Now**. To capture the network's state at a previous date and time, click **Past**, then in the **Start Time** field, select the calendar icon.

    The **Choose options** field includes all the elements and services that may run on the network. All are selected by default. Click any element to remove it from the snapshot. Nodes and services are included in all snapshots.

    The **Notes** field is optional. You can add a note as a reminder of the snapshot's purpose.

3. Select **Finish**. The card now appears on your workbench.

4. When you are finished viewing the snapshot, click **Dismiss** to remove it from your workbench. You can add it back by selecting {{<img src="/images/netq/camera.svg" alt="snapshot" width="22.5" height="18">}} **Snapshot** in the header and navigating to the option to view snapshots. 

## Compare Network Snapshots

You can compare the state of your network before and after an upgrade or other configuration change to help avoid unwanted changes to your network's state.

To compare network snapshots:

1. From the workbench header, select {{<img src="/images/netq/camera.svg" alt="snapshot" width="22.5" height="18">}} **Snapshot**.

2. Select **Compare snapshots**, then select the two snapshots you want to compare.

3. Click **Finish**.

If the snapshot cards are already on your workbench, place the cards side-by-side for a high-level comparison. For a more detailed comparison, click **Compare** on one of the cards and select a snapshot for comparison from the list.

### Interpreting the Comparison Data

For each network element with changes, a visualization displays the differences between the two snapshots. Green represents additions, red represents subtractions, and orange represents updates. 

In the following example, Snapshot 3 and Snapshot 4 are being compared. Snapshot 3 has a BGP count of 212 and Snapshot 4 has a BGP count of 186. The comparison also shows 98 BGP updates.

{{<figure src="/images/netq/snapshot-comparison.png" alt="comparison data displayed for two snapshots" width="700">}}

From this view, you can dismiss the snapshots or select **View Details** for additional information and to filter and export the data as a JSON file.

The following table describes the information provided for each element type when changes are present:

| Element | Data Descriptions |
| ------- | ----------------- |
| BGP | <ul><li><strong>Hostname</strong>: Name of the host running the BGP session</li><li><strong>VRF</strong>: Virtual route forwarding interface if used</li><li><strong>BGP session</strong>: Session that was removed or added</li><li><strong>ASN</strong>: Autonomous system number</li></ul> |
| Config | <ul><li><strong>Hostname</strong>: Name of the host where the configuration file was added or removed</li><li><strong>Configuration file</strong>: File that was added or removed |
| Interface | <ul><li><strong>Hostname</strong>: Name of the host where the interface resides</li><li><strong>Interface name</strong>: Name of the interface that was removed or added</li></ul> |
| IP Address | <ul><li><strong>Hostname</strong>: Name of the host where address was removed or added</li><li><strong>Prefix</strong>: IP address prefix</li><li><strong>Mask</strong>: IP address mask</li><li><strong>Interface name</strong>: Name of the interface that owns the address</li></ul> |
| Links | <ul><li><strong>Hostname</strong>: Name of the host where the link was removed or added</li><li><strong>Interface name</strong>: Name of the link</li><li><strong>Kind</strong>: Bond, bridge, eth, loopback, macvlan, swp, vlan, vrf, or vxlan</li></ul> |
| LLDP | <ul><li><strong>Hostname</strong>: Name of the discovered host that was removed or added</li><li><strong>Interface name</strong>: Name of the interface</li></ul> |
| MAC Address | <ul><li><strong>Hostname</strong>: Name of the host where MAC address resides</li><li><strong>MAC address</strong>: MAC address that was removed or added</li><li><strong>VLAN</strong>: VLAN associated with the MAC address</li></ul> |
| MLAG | <ul><li><strong>Hostname</strong>: Name of the host running the MLAG session</li><li><strong>MLAG Sysmac</strong>: MAC address for a bond interface pair that was removed or added</li></ul> |
| Neighbor | <ul><li><strong>Hostname</strong>: Name of the neighbor peer that was removed or added</li><li><strong>VRF</strong>: Virtual route forwarding interface if used</li><li><strong>Interface name</strong>: Name of the neighbor interface</li><li><strong>IP address</strong>: Neighbor IP address</li></ul> |
| Node | <ul><li><strong>Hostname</strong>: Name of the network node that was removed or added</li></ul> |
| OSPF | <ul><li><strong>Hostname</strong>: Name of the host running the OSPF session</li><li><strong>Interface name</strong>: Name of the associated interface that was removed or added</li><li><strong>Area</strong>: Routing domain for this host device</li><li><strong>Peer ID</strong>: Network subnet address of router with access to the peer device</li></ul> |
| Route | <ul><li><strong>Hostname</strong>: Name of the host running the route that was removed or added</li><li><strong>VRF</strong>: Virtual route forwarding interface associated with route</li><li><strong>Prefix</strong>: IP address prefix</li></ul> |
| Sensors | <ul><li><strong>Hostname</strong>: Name of the host where sensor resides</li><li><strong>Kind</strong>: Power supply unit, fan, or temperature</li><li><strong>Name</strong>: Name of the sensor that was removed or added</li></ul> |
| Services | <ul><li><strong>Hostname</strong>: Name of the host where service is running</li><li><strong>Name</strong>: Name of the service that was removed or added</li><li><strong>VRF</strong>: Virtual route forwarding interface associated with service</li></ul> |

## Related Information

- {{<link title="Back Up and Restore NetQ">}}