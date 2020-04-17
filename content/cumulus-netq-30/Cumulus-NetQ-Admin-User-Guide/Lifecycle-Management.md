---
title: Lifecycle Management
author: Cumulus Networks
weight: 640
aliases:
 - /display/NETQ/NetQ+Management
 - /pages/viewpage.action?pageId=12321950
pageID: 12321950
toc: 4
---
As an administrator, you want to manage the deployment of Cumulus Networks product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible. With this release, NetQ expands its initial Lifecycle Management feature of network Snapshot and Compare to support Cumulus Linux image, switch, and credential management, and a UI workflow for the Cumulus Linux image installation and upgrade, including backup and restoration of the switch configuration files. Each of these features can be managed separately, but the most benefits are seen when they are used together in the workflow.

## Access Lifecycle Management Features

To manage the various lifecycle management features, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

The Manage Switch Assets view provides a summary card for switch inventory, uploaded images, and switch access settings.

{{<figure src="/images/netq/lcm-dashboard-300.png" width="700">}}

{{<notice tip>}}
If you have a workbench open, you can also access this view by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg", height="18", width="18"/> in the workbench header.
{{</notice>}}

In preparation for using the installation and upgrade workflow:

- Upload the required images
- Configure switch access credentials (required for upgrades)
- Verify the switches you want to manage are running NetQ Agent 2.4 or later
- Assign each switch a role (optional, but recommended)

Once you have completed these tasks, you can take advantage of the UI workflow to install or upgrade switch images. Refer to {{<link title="#Lifecycle Management" text="Image Installation and Upgrade">}}.

## Image Management

Cumulus Linux binary images can be uploaded to a local LCM repository for use with installation and upgrade of your switches. You can upload images from an external drive. When NetQ discovers Cumulus Linux switches running NetQ 2.4 or later in your network or you upload an image manually, it extracts the meta data needed to select the appropriate image for a given switch; including the software version (x.y.z), the CPU architecture (ARM, x86), platform (based on ASIC vendor, Broadcom or Mellanox) and SHA Checksum.

The Cumulus Linux Images card provides a summary of image status in NetQ. It shows the total number of images in the repository, a count of missing images (refer to {{<link title="#Lifecycle Management" text="Missing Images">}}), and two actions.

### Default Cumulus Linux Version Assignment

You can assign a specific Cumulus Linux version as the default version to use during installation or upgrade of switches. The default selection can be overridden on an as needed basis.

### Missing Images

You should upload images for each variant of Cumulus Linux currently installed on your switch inventory if you want to support rolling back to a known good version should an installation or upgrade fail. NetQ prompts you to upload any missing images to the repository. For example, if you have both Cumulus Linux 3.7.3 and 3.7.11 versions, some running on ARM and some on x86 architectures, then NetQ would verify the presence of each of these images. If only the 3.7.3 x86, 3.7.3 ARM, and 3.7.11 x86 images in the repository, NetQ would list the 3.7.11 ARM image as missing.

If you have specified a default Cumulus Linux version, NetQ verifies that the necessary images are available, and if not, lists those that are missing based on the known switch inventory.

### Upload Images

On installation of NetQ 3.0, no images have yet been uploaded to the repository. Begin by adding images that match your current inventory. Then add the image you want to use for upgrading. And finally specify a default image for upgrades, if desired.

#### Upload Missing Images

To upload missing images:

1. Click the **View missing CL images** link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-linux-images-card-at-install-missinglink-300.png" width="200">}}

2. Select one of the missing images and make note of the version, ASIC Vendor, and CPU architecture.

    {{<figure src="/images/netq/lcm-images-missing-list-300.png" width="700">}}

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

    {{<figure src="/images/netq/lcm-import-image-dialog-300.png" width="250">}}

4. Provide the *.bin* file from an external drive that matches the criteria for the selected image, either by dragging and dropping it onto the dialog or by selecting it from a directory.

5. Click **Import**.

    {{<figure src="/images/netq/lcm-import-image-in-process-300.png" width="250">}}

    On completion you receive confirmation of the upload.

    {{<figure src="/images/netq/lcm-import-image-success-300.png" width="250">}}

6. Click **Done**.

7. Click **Downloaded** tab to verify the image is in the repository.

8. Repeat Steps 1-7 until all of the missing images are uploaded to the repository. When all of the missing images have been uploaded, the Missing list will be empty.

9. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

#### Upload Upgrade Images

To upload the Cumulus Linux images that you want to use for upgrade:

1. Click **Add Image** on the Cumulus Linux Images card.

    {{<figure src="/images/netq/lcm-linux-images-card-at-install-addimage-300.png" width="200">}}

2. Provide an image from an external drive, either by dragging and dropping it onto the dialog or by selecting it from a directory.

3. Click **Import**.

4. Click **Done**.

5. Repeat Steps 1-4 to upload additional images as needed.

    For example, if you are upgrading switches with different ASIC vendors or CPU architectures, you will need more than one image.

#### Specify a Default Image for Upgrade

To specify a default Cumulus Linux image:

1. Click the link in the middle of the Cumulus Linux Images card.

    {{<figure src="/images/netq/lcm-images-card-none-missing-300.png" width="200">}}

2. Select the image you want to use as the default image for switch upgrades.

3. Click **Save**. The default version is now highlighted on the Cumulus Linux Images card.

    {{<figure src="/images/netq/lcm-images-card-default-assigned-300.png" width="200">}}

### Export Images

Once you have images uploaded to the NetQ LCM repository, you are able to export those images.

To export images:

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images card.

3. Select the images you want to export from the **Downloaded** tab. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-downloaded-tab-300.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/>.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-222.png" width="250">}}

### Remove Images from Local Repository

Once you have upgraded all of your switches beyond a particular release of Cumulus Linux, you may want to remove any associated images from the NetQ LCM repository to save space on the server.

To remove images:

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images card.

3. On the **Downloaded** tab, select the images you want to remove. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-downloaded-tab-300.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

## Credential Management



## Switch Management

This lifecycle management feature provides an inventory of switches that have been automatically discovered by NetQ 3.0.0 and are available for software installation or upgrade. This includes all switches running Cumulus NetQ 2.4 or later in your network. You assign network roles to switches and select switches for software installation and upgrade from this inventory listing.

<!-- Insert image here -->

### Role Management

## Configuration Management

## Network Snapshot and Compare

Creating and comparing network snapshots can be used at various times; typically when you are upgrading or changing the configuration of your switches in some way. The instructions here describe how to create and compare network snapshots at any time. Refer to {{<link title="Image Installation and Upgrade">}} to see how it is incorporated into that workflow.

### Create a Network Snapshot

It is simple to capture the state of your network using the snapshot feature.

To create a snapshot:

1. From any workbench, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

2. Click **Create Snapshot**.

3. Enter a name and, optionally, a descriptive note for the snapshot.

    {{<figure src="/images/netq/snapshot-create-snap-modal-ex-230.png" width="500">}}

4. Click **Finish**.

    A medium Snapshot card appears on your desktop. Spinning arrows are visible while it works. When it finishes you can see the number of items that have been captured, and if any failed. This example shows a successful result.

    {{<figure src="/images/netq/snapshot-success-231.png" width="200">}}

    {{%notice note%}}
If you change your mind and do not want to create the snapshot, click **Back** or **Choose Action**. Do not click **Done** until you are ready to close the card. Done saves the snapshot automatically.
    {{%/notice%}}

### Compare Network Snapshots

You can compare the state of your network before and after an upgrade or other configuration change to validate the changes.

To compare network snapshots:

1. Create a snapshot (as described in previous section) *before* you make any changes.

2. Make your changes.

3. Create a second snapshot.

4. Compare the results of the two snapshots:

    - If you have the two desired snapshot cards open:
        - Simply put them next to each other to view an overview.
        - Scroll down to see all of the items.

        {{<figure src="/images/netq/snapshot-compare-snap-results-231.png" width="425">}}

    - If you have only one of the cards open:
        - Click **Compare** on the open card.
        - Select the snapshot to compare with. Note that only snapshots taken before this snapshot appear in the selection list.

        {{<figure src="/images/netq/snapshot-compare-select-fr-open-card-231.png" width="250">}}

    - If you have closed one or both of the cards (you may have created them some time before):
        - Click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}}.
        - Click **Compare Snapshots**.
        - Click on the two snapshots you want to compare.
        - Click **Finish**. Note that two snapshots must be selected before **Finish** is active.

        {{<figure src="/images/netq/snapshot-compare-selection-modal-231.png" width="500">}}

    In the latter two cases, the large Snapshot card opens. The only difference is in the card title. If you opened the comparison card from a snapshot on your workbench, the title includes the name of that card. If you open the comparison card through the Snapshot menu, the title is generic, indicating a comparison only. Functionally, you have reached the same point.

    {{<figure src="/images/netq/snapshot-large-compare-titles-230.png" width="200">}}

    {{<figure src="/images/netq/snapshot-large-compare-from-modal-240.png" width="500">}}

#### Interpreting the Comparison Data

For each network element that is compared, count values and changes are shown:

{{<figure src="/images/netq/snapshot-large-compare-data-interpretation-240.png" width="300">}}

For example, if the snapshot taken first had a total count of 110 interfaces, changes were made that added 40 interfaces and removed 32 interfaces before the second snapshot was taken, the second snapshot total count of interfaces would be eight more than in the first snapshot, or 118.

From this card, you can also change which snapshots to compare. Select an alternate snapshot from one of the two snapshot dropdowns and then click **Compare**.

##### View Change Details

You can view additional details about the changes that have occurred between the two snapshots by clicking **View Details**. This opens the full screen Detailed Snapshot Comparison card.

From this card you can:

- see each of the elements that was added and removed, and various information about each
- export the results per element

{{<figure src="/images/netq/snapshot-fullscr-change-details-230.png" width="700">}}

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

## Image Installation and Upgrade
