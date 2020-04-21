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

Once you have completed these tasks, you can take advantage of the UI workflow to install or upgrade switch images. Refer to {{<link title="#Image Installation and Upgrade" text="Image Installation and Upgrade">}}.

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

Switch access credentials are needed for performing upgrades. You can choose between basic authentication (username and password) and SSH key-based authentication. These credentials apply to all switches.

### Specify Switch Credentials

To specify access credentials:

1. Open the LCM dashboard.

2. Click the link on the Access card.

3. Select the authentication method you want to use; **SSH** or **Basic Authentication**. Basic authentication is selected by default.

4. Based on your selection:

    - **Basic**: Enter a username and password
    - **SSH**: Copy and paste your SSH key

    {{<figure src="/images/netq/lcm-access-create-dialog-300.png" width="250">}}

5. Click **Save**.

    The Access card now indicates your credential configuration.

    {{<figure src="/images/netq/lcm-access-configured-300.png" width="200">}}

### Modify Switch Credentials

To change your access credentials:

You can modify your switch access credentials at any time. You can change between authentication methods or change values for either method.

1. Open the LCM dashboard.

2. On the Access card, click the link in the center of the card.

3. Select the authentication method you want to use; **SSH** or **Basic Authentication**. Basic authentication is selected by default.

4. Based on your selection:

    - **Basic**: Enter a new username and/or password
    - **SSH**: Copy and paste a new SSH key

5. Click **Save**.

## Switch Management

This lifecycle management feature provides an inventory of switches that have been automatically discovered by NetQ 3.0.0 and are available for software installation or upgrade through NetQ. This includes all switches running Cumulus NetQ Agent 2.4 or later in your network. You assign network roles to switches and select switches for software installation and upgrade from this inventory listing.

A count of the switches NetQ was able to discover and the Cumulus Linux versions that are running on those switches is available from the LCM dashboard.

{{<figure src="/images/netq/lcm-switches-card-300.png" width="200">}}

To view the list of switches, click **Manage** on the Switches card.

{{<figure src="/images/netq/lcm-switch-mgmt-list-300.png" width="700">}}

Review the list, filtering as needed to determine in the switches you want to upgrade are included. If they are not listed, verify the switches have NetQ 2.4 or later Agents on them.

To verify the NetQ Agent version, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click **Agents** in the **Network** section. Search for the switches of interest and confirm the applied version in the **Version** column. Upgrade any NetQ Agents if needed. Refer to {{<link title="Upgrade NetQ Agents">}} for instructions.

After all of the switches you want to upgrade are contained in the list, you can assign roles to them.

### Role Management

Four pre-defined switch roles are available based on the CLOS architecture:

- Superspine
- Spine
- Leaf
- Exit

Switch roles are used to:

- Identify switch dependencies and determine the order in which switches are upgraded
- Determine when to stop if an upgrade fails

When roles are assigned, the upgrade process begins with switches having the superspine role, then continues with the spine switches, leaf switches, exit switches, and finally switches with no role assigned. All switches with a given role must be successfully upgraded before the switches with the closest dependent role can be upgraded. For example, a group of seven switches are selected for upgrade. Three are spine switches and four are leaf switches. After all of the spine switches are successfully upgraded, then the leaf switches are upgraded. If one of the spine switches were to fail the upgrade, the other two spine switches are upgraded, but the upgrade process stops after that, leaving the leaf switches untouched.

While role assignment is optional, using roles can prevent switches from becoming unreachable due to dependencies between switches or single attachments, and when MLAG pairs are deployed, switch roles avoid upgrade conflicts. For these reasons, Cumulus Networks highly recommends assigning roles to all of your switches.

#### Assign Switch Roles

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one or more switches that have the same role.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}}.

5. Select the role that applies to the selected switch(es).

    {{<figure src="/images/netq/lcm-role-assign-role-selection-300.png" width="300">}}

6. Click **Assign**.

    Note that the Role column is updated with the selected role assigned to the selected switch(es).

    {{<figure src="/images/netq/lcm-switches-listing-300.png" width="700">}}

7. Continue selecting switches and assigning roles until most or all switches have roles assigned.

A bonus of assigning roles to switches is that you can then filter the list of switches by their roles by clicking the appropriate tab.

### Export List of Switches

Using the Switch Management feature you can export a listing of all or a selected set of switches.

To export the switch listing:

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one or more switches, filtering as needed, or select all switches (click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>).

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/download-bottom.svg" height="18" width="18"/>.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-222.png" width="250">}}

## Network Snapshot and Compare

Creating and comparing network snapshots can be used at various times; typically when you are upgrading or changing the configuration of your switches in some way. The instructions here describe how to create and compare network snapshots at any time. Refer to {{<link title="#Image Installation and Upgrade" text="Image Installation and Upgrade">}} to see how snapshots are automatically created in that workflow.

### Create a Network Snapshot

It is simple to capture the state of your network currently or for a time in the past using the snapshot feature.

To create a snapshot:

1. From any workbench, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

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

### Compare Network Snapshots

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

#### Interpreting the Comparison Data

For each network element that is compared, count values and changes are shown:

{{<figure src="/images/netq/snapshot-large-compare-data-interpretation-300.png" width="300">}}

In this example, a change was made to the VLAN. The snapshot taken before the change (17Apr2020) had a total count of 765 neighbors. The snapshot taken after the change (20Apr2020) had a total count of 771 neighbors. Between the two totals you can see the number of neighbors added and removed from one time to the next, resulting in six new neighbors after the change.

{{<notice note>}}
The red and green coloring indicates only that items were removed (red) or added (green). The coloring does not indicate whether the removal or addition of these items is bad or good.
{{</notice>}}

{{<notice tip>}}
From this card, you can also change which snapshots to compare. Select an alternate snapshot from one of the two snapshot dropdowns and then click <strong>Compare</strong>.
{{</notice>}}

##### View Change Details

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

### Manage Network Snapshots

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

The workflow for installation and upgrade using LCM to select switches, choose options, run pre-checks, view job preview, begin job, monitor job, review snapshot comparison and analyze as needed.

{{<figure src="/images/netq/lcm-upgrade-workflow-300.png" width="700">}}

### Prepare

In preparation for switch installation or upgrade, first perform the following steps:

- Upload the required images. Refer to {{<link title="#Image Management" text="Image Management">}}.
- Configure switch access credentials. Refer to {{<link title="#Credential Management" text="Credential Management">}}.
- Verify the switches you want to manage are running NetQ Agent 2.4 or later. Refer to {{<link title="#Switch Management" text="Switch Management">}}.
- Assign each switch a role (optional, but recommended). Refer to {{<link title="#Role Management" text="Role Management">}}.

Your LCM dashboard should look similar to this after you have completed these steps:

{{<figure src="/images/netq/lcm-post-upgrade-prep-300.png" width="700">}}

### Perform Install or Upgrade

To install or upgrade switches:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the Switches card.

    {{<figure src="/images/netq/lcm-upgrade-switch-manage-button-300.png" width="700">}}

3. Select the switches you want to upgrade. If needed, use the filter to the list and find these switches.

    {{<figure src="/images/netq/lcm-switch-mgmt-list-switches-selected-300.png" width="700">}}

4. Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" height="18" width="18">}}.

    From this point on, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-tab-300.png" width="500">}}

5. Give the upgrade job a name. This is required.

    {{<notice tip>}}
    For best presentation, Cumulus Networks recommends keeping the name to a maximum of 20 characters when possible. The name can contain spaces and special characters. If you choose to use longer names, use the distinguishing part of the name at the beginning.
    {{</notice>}}

6. Verify that the switches you selected are included, and that they have the correct IP address and roles assigned.

    - If you accidentally included a switch that you do NOT want to upgrade, hover over the switch information card and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} to remove it from the upgrade job.
    - If the role is incorrect or missing, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to select a role for that switch, then click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18">}}. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18">}} to discard a role change.

    In this example, some of the selected switches do not have roles assigned.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-missing-roles-300.png" width="500">}}
    
7. When you are satisfied that the list of switches is accurate for the job, click **Next**.

8. Verify that you want to use the default Cumulus Linux version for this upgrade job. If not, click **Custom** and select an alternate image from the list.

    {{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-300.png" width="500">}}

9. Note that the switch access authentication method, *Using global access credentials*, indicates you have chosen either basic authentication with a username and password or SSH key-based authentication for all of your switches. Authentication on a per switch basis is not currently available.

10. Click **Next**.

11. Verify the upgrade job options.

    By default, NetQ takes a network snapshot before the upgrade and then one after the upgrade is complete. It also performs a roll back to the original Cumulus Linux version on any server which fails to upgrade.

    While these options provide a smoother upgrade process and are highly recommended, you have the option to disable these options by clicking **No** next to one or both options.

    {{<figure src="/images/netq/lcm-upgrade-switches-options-tab-300.png" width="500">}}

12. Click **Next**.

13. After the pre-checks have completed successfully, click **Preview**.

    If one or more of the pre-checks fails, resolve the related issue and start the upgrade again.

    {{<figure src="/images/netq/lcm-upgrade-switches-precheck-tab-success-300.png" width="500">}}

14. Review the job preview.

    Note the chosen options are visible (top center), the pre-checks were completed successfully (top right and left in Pre-Upgrade Tasks), the order in which the switches are planned for upgrade (center; upgrade starts from the left), and the post-upgrade tasks (right). Any switches without roles are upgraded last and are grouped under the label *Stage1*.

    {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-300.png" width="700">}}

15. When you are happy with the job specifications, click **Start Upgrade**.

### Analyze Results

After starting the upgrade you can monitor the progress from the preview page. A green circle with rotating arrows is shown above each step as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the Upgrade History page. The job started most recently is shown at the bottom, and the data is refreshed every minute.

{{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing and reopening your view, or refreshing the page.
{{</notice>}}

#### Sample Successful Upgrade

Two views are available for monitoring the upgrade job.

- Monitor the job with full details open:

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-300.png" width="700">}}

- Monitor the job with summary information only:

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-upgrading-summary-300.png" width="700">}}

    Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}} to view what stage the job is in.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-stage-view-300.png" width="700">}}

    Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}} to view the detailed view.

On successful completion, you can compare the network snapshots taken before and after the upgrade. You can also download details about the upgrade in the form of a JSON-formatted file, by clicking **Download Report**.

{{<figure src="/images/netq/lcm-upgrade-switches-success-detail-300.png" width="700">}}

Click **Compare Snapshots** to view the network state before and after the upgrade.

{{<figure src="/images/netq/lcm-upgrade-switches-compare-snapshots-300.png" width="700">}}

Refer to {{<link title="#interpreting-the-comparison-data" text="Interpreting the Comparison Data">}} for information about analyzing these results.

<!-- How do I get back to the Upgrade History page? -->



#### Sample Failed Upgrade

If an upgrade job fails for any reason, you can view the associated error(s):

1. From the Upgrade History dashboard, find the job of interest.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-fail-summary-300.png" width="700">}}

2. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}}.

3. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-open-300.png" width="700">}}

    Note in this example, all of the pre-upgrade tasks were successful, but backup failed on the spine switches.

4. Double-click on an error to view a more detailed error message.

    This example, shows that the upgrade failure was due to bad switch access credentials. You would need to fix those and then create a new upgrade job.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-message-300.png" width="700">}}
