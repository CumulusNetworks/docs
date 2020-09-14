---
title: Manage Network Snapshots
author: Cumulus Networks
weight: 690
toc: 4
---
Creating and comparing network snapshots can be used at various times; typically when you are upgrading or changing the configuration of your switches in some way. The instructions here describe how to create and compare network snapshots at any time using the NetQ UI.

The NetQ CLI can only create network snapshots during a Cumulus Linux upgrade. The results are only visible from the NetQ UI.

Refer to {{<link title="#Image Installation and Upgrade" text="Image Installation and Upgrade">}} to see how snapshots are automatically created during upgrades to validate that the network state has not changed unexpectedly after an upgrade.

## Create a Network Snapshot

It is simple to capture the state of your network currently or for a time in the past using the snapshot feature.

To create a snapshot:

1. From any workbench in the NetQ UI, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

2. Click **Create Snapshot**.

3. Enter a name for the snapshot.

    {{<figure src="/images/netq/snapshot-create-snap-modal-ex-300.png" width="450">}}

4. Accept the time provided or enter a previous date and time.

5. Optionally, add a descriptive note for the snapshot.

6. Click **Finish**.

    A medium Snapshot card appears on your desktop. Spinning arrows are visible while it works. When it finishes you can see the number of items that have been captured, and if any failed. This example shows a successful result.

    {{<figure src="/images/netq/snapshot-success-300.png" width="200">}}

    {{<notice note>}}
If you have already created other snapshots, <strong>Compare</strong> is active. Otherwise it is inactive (grayed-out).
    {{</notice>}}

## Compare Network Snapshots

You can compare the state of your network before and after an upgrade or other configuration change to validate the changes.

To compare network snapshots:

1. Create a snapshot (as described in previous section) *before* you make any changes.

2. Make your changes.

3. Create a second snapshot.

4. Compare the results of the two snapshots. Depending on what, if any, cards are open on your workbench:

    - If you have the two desired snapshot cards open:
        - Simply put them next to each other to view a high-level comparison.
        - Scroll down to see all of the items.
        - To view a more detailed comparison, click **Compare** on one of the cards. Select the other snapshot from the list.

        {{<figure src="/images/netq/snapshot-compare-snap-results-300.png" width="425">}}

    - If you have only one of the cards open:
        - Click **Compare** on the open card.
        - Select the other snapshot to compare.

        {{<figure src="/images/netq/snapshot-compare-select-fr-open-card-300.png" width="250">}}

    - If no snapshot cards are open (you may have created them some time before):
        - Click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}}.
        - Click **Compare Snapshots**.
        - Click on the two snapshots you want to compare.
        - Click **Finish**. Note that two snapshots must be selected before **Finish** is active.

        {{<figure src="/images/netq/snapshot-compare-selection-modal-300.png" width="500">}}

    In the latter two cases, the large Snapshot card opens. The only difference is in the card title. If you opened the comparison card from a snapshot on your workbench, the title includes the name of that card. If you open the comparison card through the Snapshot menu, the title is generic, indicating a comparison only. Functionally, you have reached the same point.

    {{<figure src="/images/netq/snapshot-large-compare-titles-230.png" width="200">}}

    {{<figure src="/images/netq/snapshot-large-compare-from-modal-300.png" width="500">}}

    Scroll down to view all element comparisons.

### Interpreting the Comparison Data

For each network element that is compared, count values and changes are shown:

{{<figure src="/images/netq/snapshot-large-compare-data-interpretation-300.png" width="300">}}

In this example, a change was made to the VLAN. The snapshot taken before the change (17Apr2020) had a total count of 765 neighbors. The snapshot taken after the change (20Apr2020) had a total count of 771 neighbors. Between the two totals you can see the number of neighbors added and removed from one time to the next, resulting in six new neighbors after the change.

{{<notice note>}}
The red and green coloring indicates only that items were removed (red) or added (green). The coloring does not indicate whether the removal or addition of these items is bad or good.
{{</notice>}}

{{<notice tip>}}
From this card, you can also change which snapshots to compare. Select an alternate snapshot from one of the two snapshot dropdowns and then click <strong>Compare</strong>.
{{</notice>}}

#### View Change Details

You can view additional details about the changes that have occurred between the two snapshots by clicking **View Details**. This opens the full screen Detailed Snapshot Comparison card.

From this card you can:

- View changes for each of the elements that had added and/or removed items, and various information about each; only elements with changes are presented
- Filter the added and removed items by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}}
- Export all differences in JSON file format by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18">}}

{{<figure src="/images/netq/snapshot-fullscr-change-details-300.png" width="700">}}

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

## Manage Network Snapshots

You can create as many snapshots as you like and view them at any time. When a snapshot becomes old and no longer useful, you can remove it.

To view an existing snapshot:

1. From any workbench, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

2. Click **View/Delete Snapshots**.

3. Click **View**.

4. Click one or more snapshots you want to view, then click **Finish**.

    Click **Back** or **Choose Action** to cancel viewing of your selected snapshot(s).

To remove an existing snapshot:

1. From any workbench, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

2. Click **View/Delete Snapshots**.

3. Click **Delete**.

4. Click one or more snapshots you want to remove, then click **Finish**.

    Click **Back** or **Choose Action** to cancel the deletion of your selected snapshot(s).
