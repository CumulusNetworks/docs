---
title: Manage Network Snapshots
author: NVIDIA
weight: 690
toc: 4
---
Creating and comparing network snapshots can be useful to validate that the network state has not changed. Snapshots are typically created when you upgrade or change the configuration of your switches in some way. This section describes the Snapshot card and content, as well as how to create and compare network snapshots at any time. Snapshots can be automatically created during the upgrade process for Cumulus Linux or SONiC. Refer to {{<link title="Upgrade Cumulus Linux Using LCM#perform-a-cumulus-linux-upgrade" text="Perform a Cumulus Linux Upgrade">}}.

## Create a Network Snapshot

It is simple to capture the state of your network currently or for a time in the past using the snapshot feature.

To create a snapshot:

1. From any workbench in the NetQ UI, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

    {{<figure src="/images/netq/snapshot-choose-action-modal-320.png" width="400">}}

2. Click **Create Snapshot**.

3. Enter a name for the snapshot.

    {{<figure src="/images/netq/snapshot-create-snap-modal-320.png" width="400">}}

4. Choose the time for the snapshot:

    - For the current network state, click **Now**.

        {{<figure src="/images/netq/snapshot-create-snap-dialog-now-310.png" width="400">}}

    - For the network state at a previous date and time, click **Past**, then click in **Start Time** field to use the calendar to step through selection of the date and time. You may need to scroll down to see the entire calendar.

        {{<figure src="/images/netq/snapshot-create-snap-dialog-past-310.png" width="400">}}

5. Choose the services to include in the snapshot.

    In the **Choose options** field, click any service name to remove that service from the snapshot. This would be appropriate if you do not support a particular service, or you are concerned that including that service might cause the snapshot to take an excessive amount of time to complete if included. The checkmark next to the service and the service itself is grayed out when the service is removed. Click any service again to re-include the service in the snapshot. The checkmark is highlighted in green next to the service name and is no longer grayed out.

    {{<notice note>}}
The Node and Services options are mandatory, and cannot be selected or unselected.
    {{</notice>}}
    {{<notice info>}}
If you remove services, be aware that snapshots taken in the past or future may not be equivalent when performing a network state comparison.
    {{</notice>}}

    This example removes the OSPF and Route services from the snapshot being created.

    {{<figure src="/images/netq/snapshot-create-snap-dialog-svcs-removed-310.png" width="400">}}

6. Optionally, scroll down and click in the **Notes** field to add descriptive text for the snapshot to remind you of its purpose. For example: "This was taken before adding MLAG pairs," or "Taken after removing the leaf36 switch."

6. Click **Finish**.

    A medium Snapshot card appears on your desktop. Spinning arrows are visible while it works. When it finishes you can see the number of items that have been captured, and if any failed. This example shows a successful result.

    {{<figure src="/images/netq/snapshot-success-300.png" width="200">}}

    {{<notice note>}}
If you have already created other snapshots, <strong>Compare</strong> is active. Otherwise it is inactive (grayed-out).
    {{</notice>}}

7. When you are finished viewing the snapshot, click **Dismiss** to close the snapshot. The snapshot is not deleted, merely removed from the workbench.

## Compare Network Snapshots

You can compare the state of your network before and after an upgrade or other configuration change to validate that the changes have not created an unwanted change in your network state.

To compare network snapshots:

1. Create a snapshot (as described in previous section) *before* you make any changes.

2. Make your changes.

3. Create a second snapshot.

4. Compare the results of the two snapshots.

    Depending on what, if any, cards are open on your workbench:

{{<tabs "TabID80" >}}

{{<tab "Two snapshots open" >}}

1. Put the cards next to each other to view a high-level comparison. Scroll down to see all of the items.

2. To view a more detailed comparison, click **Compare** on one of the cards. Select the other snapshot from the list.

    {{<figure src="/images/netq/snapshot-compare-snap-results-300.png" width="425">}}

{{</tab>}}

{{<tab "One snapshot open" >}}

1. Click **Compare** on the open card.

2. Select the other snapshot to compare.

    {{<figure src="/images/netq/snapshot-compare-select-fr-open-card-300.png" width="250">}}

{{</tab>}}

{{<tab "No snapshots open" >}}

1. Click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}}.

2. Click **Compare Snapshots**.

3. Click on the two snapshots you want to compare.

4. Click **Finish**. Note that two snapshots must be selected before **Finish** is active.

    {{<figure src="/images/netq/snapshot-compare-selection-modal-300.png" width="500">}}

{{</tab>}}

{{</tabs>}}

In the latter two cases, the large Snapshot card opens. The only difference is in the card title. If you opened the comparison card from a snapshot on your workbench, the title includes the name of that card. If you open the comparison card through the Snapshot menu, the title is generic, indicating a comparison only. Functionally, you have reached the same point.

{{<figure src="/images/netq/snapshot-large-compare-titles-230.png" width="200">}}

{{<figure src="/images/netq/snapshot-large-compare-from-modal-oldernewer-330.png" width="500">}}

Scroll down to view all element comparisons.

### Interpreting the Comparison Data

For each network element that is compared, count values and changes are shown:

{{<figure src="/images/netq/snapshot-large-compare-data-interpretation-330.png" width="400">}}

In this example, there are changes to the MAC addresses and neighbors. The snapshot taken before the change (19JanGold) had a total count of 316 MAC addresses and 873 neighbors. The snapshot taken after the changes (Now) has a total count of 320 MAC addresses and 891 neighbors. Between the two totals you can see the number of neighbors added, updated, and removed from one time to the next. This shows four MAC addresses have been added, 9 MAC addresses have been updated, and 18 neighbors have been added.

{{<notice tip>}}
The coloring does not indicate whether the additional, removal, or update of items is bad or good. It only indicates that a change has occurred.
{{</notice>}}

Be aware that depending on the display order of the snapshots determines what is considered added or removed. Compare these two views of the same data.

{{<figure src="/images/netq/snapshot-large-compare-from-modal-oldernewer-330.png" width="500" caption="More recent snapshot on right">}}

{{<figure src="/images/netq/snapshot-large-compare-from-modal-newerolder-330.png" width="500" caption="More recent snapshot on left">}}

You can also change which snapshots to compare. Select an alternate snapshot from one or both of the two snapshot dropdowns and then click **Compare**.

#### View Change Details

You can view additional details about the changes that have occurred between the two snapshots by clicking **View Details**. This opens the full screen Detailed Snapshot Comparison card.

From this card you can:

- View changes for each of the elements that had added, updated, and removed items, and various information about each; only elements with changes are presented
- Filter the added and removed items by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">}}
- Export all differences in JSON file format by clicking {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18">}}

{{<figure src="/images/netq/snapshot-fullscr-change-details-330.png" width="700">}}

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

    Click **Choose Action** to cancel viewing of your selected snapshot(s) and choose another action. Or close the network snapshot dialog by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}.

To remove an existing snapshot:

1. From any workbench, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

2. Click **View/Delete Snapshots**.

3. Click **Delete**.

4. Click one or more snapshots you want to remove, then click **Finish**.

    Click **Choose Action** to cancel the deletion of your selected snapshot(s) and choose another action. Or close the network snapshot dialog by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}.
