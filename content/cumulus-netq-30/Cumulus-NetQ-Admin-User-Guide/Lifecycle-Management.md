---
title: Lifecycle Management
author: Cumulus Networks
weight: 640
toc: 4
---
As an administrator, you want to manage the deployment of Cumulus Networks product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible. With this release, NetQ expands its initial lifecycle management (LCM) feature of network Snapshot and Compare to support Cumulus Linux image, switch, and credential management, and a UI workflow for the Cumulus Linux image installation and upgrade, including backup and restoration of the switch configuration files. Each of these features can be managed separately, but the greatest benefits are seen when they are used together in the workflow.

{{<notice note>}}
This feature is only available for on-premises deployments.
{{</notice>}}

## Access Lifecycle Management Features

To manage the various lifecycle management features, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu"> (Main Menu) and select **Upgrade Switches**.

The Manage Switch Assets view provides a summary card for switch inventory, uploaded images, and switch access settings.

{{<figure src="/images/netq/lcm-dashboard-300.png" width="700">}}

{{<notice tip>}}
If you have a workbench open, you can also access this view by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg", height="18", width="18"/> (Upgrade) in the workbench header.
{{</notice>}}

## Image Management

Cumulus Linux binary images can be uploaded to a local LCM repository for use with installation and upgrade of your switches. You can upload images from an external drive. When NetQ discovers Cumulus Linux switches running NetQ 2.4 or later in your network, it extracts the meta data needed to select the appropriate image for a given switch; including the software version (x.y.z), the CPU architecture (ARM, x86), platform (based on ASIC vendor, Broadcom or Mellanox) and SHA Checksum.

The Cumulus Linux Images card provides a summary of image status in NetQ. It shows the total number of images in the repository, a count of missing images (refer to {{<link title="#Lifecycle Management" text="Missing Images">}}), and the starting points for adding and managing your images.

### Default Cumulus Linux Version Assignment

You can assign a specific Cumulus Linux version as the default version to use during installation or upgrade of switches. Choosing the version that is desired for the largest number of your switches is recommended. The default selection can be overridden during upgrade job creation if an alternate version is needed for a set of switches.

### Missing Images

You should upload images for each variant of Cumulus Linux currently installed on your switch inventory if you want to support rolling back to a known good version should an installation or upgrade fail. NetQ prompts you to upload any missing images to the repository. For example, if you have both Cumulus Linux 3.7.3 and 3.7.11 versions, some running on ARM and some on x86 architectures, then NetQ would verify the presence of each of these images. If only the 3.7.3 x86, 3.7.3 ARM, and 3.7.11 x86 images are in the repository, NetQ would list the 3.7.11 ARM image as missing.

If you have specified a default Cumulus Linux version, NetQ also verifies that the necessary images are available based on the known switch inventory, and if not, lists those that are missing.

### Upload Images

On installation of NetQ 3.0, no images have yet been uploaded to the LCM repository. Begin by adding images that match your current inventory. Then add the image you want to use for upgrading. And finally specify a default image for upgrades, if desired.

#### Upload Missing Images

To upload missing images:

1. On the Cumulus Linux Images card, click the *View missing CL images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-linux-images-card-at-install-missinglink-300.png" width="200">}}

2. Select one of the missing images and make note of the version, ASIC Vendor, and CPU architecture.

    {{<figure src="/images/netq/lcm-images-missing-list-300.png" width="700">}}

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"> (Add Image) above the table.

    {{<figure src="/images/netq/lcm-import-image-dialog-300.png" width="250">}}

4. Provide the *.bin* file from an external drive that matches the criteria for the selected image, either by dragging and dropping it onto the dialog or by selecting it from a directory.

5. Click **Import**.

    {{<figure src="/images/netq/lcm-import-image-in-process-300.png" width="250">}}

    On successful completion, you receive confirmation of the upload.

    {{<figure src="/images/netq/lcm-import-image-success-300.png" width="250">}}

    If the upload was not successful, an *Image Import Failed* message is shown. Close the Import Image dialog and try uploading the file again.

6. Click **Done**.

7. Click **Uploaded** tab to verify the image is in the repository.

8. Repeat Steps 1-7 until all of the missing images are uploaded to the repository. When all of the missing images have been uploaded, the Missing list will be empty.

9. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"> to return to the LCM dashboard.

    The Cumulus Linux Images card now shows the number of images you uploaded.

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

Lifecycle management does not have a default Cumulus Linux image specified automatically. You must specify the image that is appropriate for your network.

To specify a default Cumulus Linux image:

1. Click the *Click here to set the default CL version* link in the middle of the Cumulus Linux Images card.

    {{<figure src="/images/netq/lcm-images-card-spec-default-cl-300.png" width="200">}}

2. Select the image you want to use as the default image for switch upgrades.

3. Click **Save**. The default version is now displayed on the Cumulus Linux Images card.

    {{<figure src="/images/netq/lcm-images-card-default-assigned-300.png" width="200">}}

After you have specified a default image, you have the option to change it.

To change the default Cumulus Linux image:

1. Click **change** next to the currently identified default image on the Cumulus Linux Images card.

2. Select the image you want to use as the default image for switch upgrades.

3. Click **Save**.

### Export Images

Once you have images uploaded to the NetQ LCM repository, you are able to export those images.

To export images:

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images card.

3. Select the images you want to export from the **Uploaded** tab. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> above the table.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-300.png" width="250">}}

### Remove Images from Local Repository

Once you have upgraded all of your switches beyond a particular release of Cumulus Linux, you may want to remove any associated images from the NetQ LCM repository to save space on the server.

To remove images:

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images card.

3. On the **Uploaded** tab, select the images you want to remove. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

## Credential Management

Switch access credentials are needed for performing upgrades. You can choose between basic authentication (SSH password) and SSH (Public/Private key) authentication. These credentials apply to all switches.

### Specify Switch Credentials

Switch access credentials are not specified by default. You must add these.

To specify access credentials:

1. Open the LCM dashboard.

2. Click the *Click here to add switch access* link on the Access card.

    {{<figure src="/images/netq/lcm-access-card-no-auth-300.png" width="200">}}

3. Select the authentication method you want to use; **SSH** or **Basic Authentication**. Basic authentication is selected by default.

{{< tabs "TabID183 ">}}

{{< tab "Basic Authentication ">}}

1. Enter a username.

2. Enter a password.

    {{<img src="/images/netq/lcm-access-create-dialog-300.png" width="250">}}

3. Click **Save**.

    The Access card now indicates your credential configuration.

    {{<figure src="/images/netq/lcm-access-configured-300.png" width="200">}}

{{< /tab >}}

{{< tab "SSH" >}}

{{<notice info>}}
You must have sudoer permission to properly configure switches when using the SSH Key method.
{{</notice>}}

1. Create a pair of SSH private and public keys.

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

2. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switches, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where the SSH key pair was generated for each switch

3. Copy the SSH *private* key into the text box in the Create Switch Access card.

    {{<figure src="/images/netq/lcm-access-create-SSH-300.png" width="250">}}

    {{<notice note>}}
For security, your private key is stored in an encrypted format, and only provided to internal processes while encrypted.
    {{</notice>}}

The Access card now indicates your credential configuration.

{{<figure src="/images/netq/lcm-access-ssh-configured-300.png" width="200">}}

{{< /tab >}}

{{< /tabs >}}

### Modify Switch Credentials

You can modify your switch access credentials at any time. You can change between authentication methods or change values for either method.

To change your access credentials:

1. Open the LCM dashboard.

2. On the Access card, click the *Click here to change access mode* link in the center of the card.

3. Select the authentication method you want to use; **SSH** or **Basic Authentication**. Basic authentication is selected by default.

4. Based on your selection:

    - **Basic**: Enter a new username and/or password
    - **SSH**: Copy and paste a new SSH private key

    {{<notice tip>}}
Refer to {{<link title="#Specify Switch Credentials" text="Specify Switch Credentials">}} for details.
    {{</notice>}}

5. Click **Save**.

## Switch Management

This lifecycle management feature provides an inventory of switches that have been automatically discovered by NetQ 3.0.0 and are available for software installation or upgrade through NetQ. This includes all switches running Cumulus NetQ Agent 2.4 or later in your network. You assign network roles to switches and select switches for software installation and upgrade from this inventory listing.

A count of the switches NetQ was able to discover and the Cumulus Linux versions that are running on those switches is available from the LCM dashboard.

{{<figure src="/images/netq/lcm-switches-card-300.png" width="400">}}

To view a list of all switches known to lifecycle management, click **Manage** on the Switches card.

{{<figure src="/images/netq/lcm-switch-mgmt-list-300.png" width="700">}}

Review the list, filtering as needed (click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18" alt="Filter Switch List">) to determine if the switches you want to upgrade are included. 

{{<notice tip>}}
If you have more than one Cumulus Linux version running on your switches, you can click a version segment on the Switches card graph to open a list of switches pre-filtered by that version.
{{</notice>}}

If the switches you are looking to upgrade are not present in the final list, verify the switches have NetQ 2.4 or later Agents on them.

To verify the NetQ Agent version, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">, then click **Agents** in the **Network** section. Search for the switches of interest and confirm the applied version in the **Version** column. Upgrade any NetQ Agents if needed. Refer to {{<link title="Upgrade NetQ Agents">}} for instructions.

After all of the switches you want to upgrade are contained in the list, you can assign roles to them.

### Role Management

Four pre-defined switch roles are available based on the CLOS architecture:

- Superspine
- Spine
- Leaf
- Exit

With this release, you cannot create your own roles.

Switch roles are used to:

- Identify switch dependencies and determine the order in which switches are upgraded
- Determine when to stop the process if a failure is encountered

When roles are assigned, the upgrade process begins with switches having the superspine role, then continues with the spine switches, leaf switches, exit switches, and finally switches with no role assigned. All switches with a given role must be successfully upgraded before the switches with the closest dependent role can be upgraded.

For example, a group of seven switches are selected for upgrade. Three are spine switches and four are leaf switches. After all of the spine switches are successfully upgraded, then the leaf switches are upgraded. If one of the spine switches were to fail the upgrade, the other two spine switches are upgraded, but the upgrade process stops after that, leaving the leaf switches untouched, and the upgrade job fails.

When only some of the selected switches have roles assigned in an upgrade job, the switches with roles are upgraded first and then all the switches with no roles assigned are upgraded.

While role assignment is optional, using roles can prevent switches from becoming unreachable due to dependencies between switches or single attachments. And when MLAG pairs are deployed, switch roles avoid upgrade conflicts. For these reasons, Cumulus Networks highly recommends assigning roles to all of your switches.

#### Assign Switch Roles

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one switch or multiple switches that should be assigned to the same role.

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">.

5. Select the role that applies to the selected switch(es).

    {{<figure src="/images/netq/lcm-role-assign-role-selection-300.png" width="300">}}

6. Click **Assign**.

    Note that the **Role** column is updated with the role assigned to the selected switch(es).

    {{<figure src="/images/netq/lcm-switches-listing-300.png" width="700">}}

7. Continue selecting switches and assigning roles until most or all switches have roles assigned.

A bonus of assigning roles to switches is that you can then filter the list of switches by their roles by clicking the appropriate tab.

#### Change the Role of a Switch

If you accidentally assign an incorrect role to a switch, it can easily be changed to the correct role.

To change a switch role:

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select the switch with the incorrect role from the list.

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">.

5. Select the correct role.

6. Click **Assign**.

### Export List of Switches

Using the Switch Management feature you can export a listing of all or a selected set of switches.

To export the switch listing:

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one or more switches, filtering as needed, or select all switches (click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18"/>).

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/>.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-300.png" width="250">}}

## Network Snapshot and Compare

Creating and comparing network snapshots can be used at various times; typically when you are upgrading or changing the configuration of your switches in some way. The instructions here describe how to create and compare network snapshots at any time. Refer to {{<link title="#Image Installation and Upgrade" text="Image Installation and Upgrade">}} to see how snapshots are automatically created in that workflow to validate that the network state has not changed after an upgrade.

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
- Filter the added and removed items by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18">
- Export all differences in JSON file format by clicking <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18">

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

## Cumulus Linux Upgrade

The workflow for installation and upgrade of Cumulus Linux using LCM is to: select switches, choose options, run pre-checks, view job preview, begin job, monitor job, review snapshot comparison and analyze as needed. Up to five jobs can be run simultaneously; however, a given switch can only be contained in one of those jobs.

{{<figure src="/images/netq/lcm-upgrade-workflow-300.png" width="700">}}

{{<notice info>}}
Upgrades can be performed between Cumulus Linux 3.x releases, and between Cumulus Linux 4.x releases. <em>Lifecycle management does not support upgrades from Cumulus Linux 3.x to 4.x releases.</em>
{{</notice>}}

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

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu"> (Main Menu) and select **Upgrade Switches**, or click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" height="18" width="18"> (Upgrade) in a workbench header.

2. Click **Manage** on the Switches card.

    {{<figure src="/images/netq/lcm-upgrade-switch-manage-button-300.png" width="700">}}

3. Select the switches you want to upgrade. If needed, use the filter to the narrow the listing and find these switches.

    {{<figure src="/images/netq/lcm-switch-mgmt-list-switches-selected-300.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" height="18" width="18"> (Upgrade Switches) above the table.

    From this point forward, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-tab-300.png" width="500">}}

5. Give the upgrade job a name. This is required.

    {{<notice tip>}}
    For best presentation, Cumulus Networks recommends keeping the name to a maximum of 22 characters when possible. The name can contain spaces and special characters. If you choose to use longer names, use the distinguishing part of the name at the beginning.
    {{</notice>}}

6. Verify that the switches you selected are included, and that they have the correct IP address and roles assigned.

    - If you accidentally included a switch that you do NOT want to upgrade, hover over the switch information card and click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"> to remove it from the upgrade job.
    - If the role is incorrect or missing, click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18"> to select a role for that switch, then click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18">. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18"> to discard a role change.

    In this example, some of the selected switches do not have roles assigned.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-missing-roles-300.png" width="500">}}
    
7. When you are satisfied that the list of switches is accurate for the job, click **Next**.

8. Verify that you want to use the default Cumulus Linux version for this upgrade job. If not, click **Custom** and select an alternate image from the list.

    {{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-300.png" width="500" caption="Default CL Version Selected">}}{{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-custom-version-300.png" width="500" caption="Custom CL Version Selected">}}

9. Note that the switch access authentication method, *Using global access credentials*, indicates you have chosen either basic authentication with a username and password or SSH key-based authentication for all of your switches. Authentication on a per switch basis is not currently available.

10. Click **Next**.

11. Verify the upgrade job options.

    By default, NetQ takes a network snapshot before the upgrade and then one after the upgrade is complete. It also performs a roll back to the original Cumulus Linux version on any server which fails to upgrade.

    While these options provide a smoother upgrade process and are highly recommended, you have the option to disable these options by clicking **No** next to one or both options.

    {{<figure src="/images/netq/lcm-upgrade-switches-options-tab-300.png" width="500">}}

12. Click **Next**.

13. After the pre-checks have completed successfully, click **Preview**.

    {{<figure src="/images/netq/lcm-upgrade-switches-precheck-tab-success-300.png" width="500">}}

    If one or more of the pre-checks fail, resolve the related issue and start the upgrade again. Expand the following dropdown to view common failures, their causes and corrective actions.

    {{< expand "Pre-check Failure Messages"  >}}

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th>Pre-check</th>
<th>Message</th>
<th>Type</th>
<th>Description</th>
<th>Corrective Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>(1) Switch Order</td>
<td>&lt;hostname1&gt; switch cannot be upgraded without isolating &lt;hostname2&gt;, &lt;hostname3&gt; which are connected neighbors. Unable to upgrade</td>
<td>Warning</td>
<td>Hostname2 and hostname3 switches will be isolated during upgrade, making them unreachable. These switches are skipped if you continue with the upgrade.</td>
<td>Reconfigure hostname2 and hostname 3 switches to have redundant connections, or continue with upgrade knowing that you will lose connectivity with these switches during the upgrade process.</td>
</tr>
<tr>
<td>(2) Version Compatibility</td>
<td>Unable to upgrade &lt;hostname&gt; with CL version &lt;3.y.z&gt; to &lt;4.y.z&gt;</td>
<td>Error</td>
<td>LCM only supports CL 3.x to 3.x and CL 4.x to 4.x upgrades</td>
<td>Perform a fresh install of CL 4.x</td>
</tr>
<tr>
<td></td>
<td>Image not uploaded for the combination: CL Version - &lt;x.y.z&gt;, Asic Vendor - &lt;Mellanox | Broadcom&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified Cumulus Linux image is not available in the LCM repository</td>
<td>Upload missing image. Refer to {{<link title="#Upload Images" text="Upload Images">}}.</td>
</tr>
<tr>
<td></td>
<td>Restoration image not uploaded for the combination: CL Version - &lt;x.y.z&gt;, Asic Vendor - &lt;Mellanox | Broadcom&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified Cumulus Linux image needed to restore the switch back to its original version if the upgrade fails is not available in the LCM repository. This applies only when the "Roll back on upgrade failure" job option is selected.</td>
<td>Upload missing image. Refer to {{<link title="#Upload Images" text="Upload Images">}}.</td>
</tr>
<tr>
<td></td>
<td>NetQ Agent and NetQ CLI Debian packages are not present for combination: CL Version - &lt;x.y.z&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified NetQ packages are not installed on the switch.</td>
<td>Upload missing packages. Refer to {{<link title="Install NetQ Agents" text="Install NetQ Agents">}} and {{<link title="Install NetQ CLI" text="Install NetQ CLI">}}.</td>
</tr>
<tr>
<td></td>
<td>Restoration NetQ Agent and NetQ CLI Debian packages are not present for combination: CL Version - &lt;x.y.z&gt;, CPU Arch - &lt;x86 | ARM &gt;</td>
<td>Error</td>
<td>The specified NetQ packages are not installed on the switch.</td>
<td>Install missing packages. Refer to {{<link title="Install NetQ Agents" text="Install NetQ Agents">}} and {{<link title="Install NetQ CLI" text="Install NetQ CLI">}}.</td>
</tr>
<tr>
<td></td>
<td>CL version to be upgraded to and current version on switch &lt;hostname&gt; are the same.</td>
<td>Warning</td>
<td>Switch is already operating the desired upgrade CL version. No upgrade is required.</td>
<td>Choose an alternate CL version for upgrade or remove switch from upgrade job.</td>
</tr>
<tr>
<td>(3) Switch Connectivity</td>
<td>Global credentials are not specified</td>
<td>Error</td>
<td>Switch access credentials are required to perform a CL upgrade, and they have not been specified.</td>
<td>Specify access credentials. Refer to {{<link title="#Specify Switch Credentials" text="Specify Switch Credentials">}}.</td>
</tr>
<tr>
<td></td>
<td>Switch is not in NetQ inventory: &lt;hostname&gt;</td>
<td>Error</td>
<td>LCM cannot upgrade a switch that is not in its inventory.</td>
<td><p>Verify you have the correct hostname or IP address for the switch. </p> <p>Verify the switch has NetQ Agent 2.4.0 or later installed: click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agents if needed. Refer to {{<link title="Upgrade NetQ Agents">}}.</p></td>
</tr>
<tr>
<td></td>
<td>Switch &lt;hostname&gt; is rotten. Cannot select for upgrade.</td>
<td>Error</td>
<td>LCM must be able to communicate with the switch to upgrade it.</td>
<td>Troubleshoot the connectivity issue and retry upgrade when the switch is fresh.</td>
</tr>
<tr>
<td></td>
<td>Total number of jobs &lt;running jobs count&gt; exceeded Max jobs supported 50</td>
<td>Error</td>
<td>LCM can support a total of 50 upgrade jobs running simultaneously.</td>
<td>Wait for the total number of simultaneous upgrade jobs to drop below 50.</td>
</tr>
<tr>
<td></td>
<td>Switch &lt;hostname&gt; is already being upgraded. Cannot initiate another upgrade.</td>
<td>Error</td>
<td>Switch is already a part of another running upgrade job.</td>
<td>Remove switch from current job or wait until the competing job has completed.</td>
</tr>
<tr>
<td></td>
<td>Backup failed in previous upgrade attempt for switch &lt;hostname&gt;.</td>
<td>Warning</td>
<td>LCM was unable to back up switch during a previously failed upgrade attempt.</td>
<td>You may want to back up switch manually prior to upgrade if you want to restore the switch after upgrade. Refer to [add link here].</td>
</tr>
<tr>
<td></td>
<td>Restore failed in previous upgrade attempt for switch &lt;hostname&gt;.</td>
<td>Warning</td>
<td>LCM was unable to restore switch after a previously failed upgrade attempt.</td>
<td>You may need to restore switch manually after upgrade. Refer to [add link here].</td>
</tr>
<tr>
<td></td>
<td>Upgrade failed in previous attempt for switch &lt;hostname&gt;.</td>
<td>Warning</td>
<td>LCM was unable to upgrade switch during last attempt.</td>
<td></td>
</tr>
<tr>
<td>(4) MLAG Configuration</td>
<td>hostname:&lt;hostname&gt;,reason:&lt;MLAG error message&gt;</td>
<td>Error</td>
<td>An error in an MLAG configuration has been detected. For example: Backup IP 10.10.10.1 does not belong to peer.</td>
<td>Review the MLAG configuration on the identified switch. Refer to the MLAG documentation for more information. Make any needed changes.</td>
</tr>
<tr>
<td></td>
<td>MLAG configuration checks timed out</td>
<td>Error</td>
<td>One or more switches stopped responding to the MLAG checks.</td>
<td></td>
</tr>
<tr>
<td></td>
<td>MLAG configuration checks failed</td>
<td>Error</td>
<td>One or more switches failed the MLAG checks.</td>
<td></td>
</tr>
<tr>
<td></td>
<td>For switch &lt;hostname&gt;, the MLAG switch with Role: secondary and ClagSysmac: &lt;MAC address&gt; does not exist.</td>
<td>Error</td>
<td>Identified switch is the primary in an MLAG pair, but the defined secondary switch is not in NetQ inventory.</td>
<td>Verify the switch has NetQ Agent 2.4.0 or later installed: click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agent if needed. Refer to {{<link title="Upgrade NetQ Agents">}}. Add the missing peer switch to NetQ inventory.</td>
</tr>
</tbody>
</table>

{{< /expand >}}

14. Review the job preview.

    - When all of your switches have roles assigned, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), the order in which the switches are planned for upgrade (center; upgrade starts from the left), and the post-upgrade tasks status (right).

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-300.png" width="700" caption="Roles assigned">}}

    - When none of your switches have roles assigned, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), a list of switches planned for upgrade (center), and the post-upgrade tasks status (right).

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-noroles-300.png" width="700" caption="No roles assigned">}}

    - When some of your switches have roles assigned, any switches without roles are upgraded last and are grouped under the label *Stage1*.

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-someroles-300.png" width="700" caption="Some roles assigned">}}

15. When you are happy with the job specifications, click **Start Upgrade**.

### Analyze Results

After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

From the preview page, a green circle with rotating arrows is shown above each step as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the Upgrade History page. The job started most recently is shown at the bottom, and the data is refreshed every minute.

{{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing (click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">) and reopening your view (click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">), or refreshing the page.
{{</notice>}}

#### Monitoring the Upgrade

Several viewing options are available for monitoring the upgrade job.

- Monitor the job with full details open:

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-300.png" width="700">}}

- Monitor the job with summary information only in the Upgrade History page. Open this view by clicking <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14"> in the full details view:

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-upgrading-summary-300.png" width="700">}}

    This view is refreshed automatically. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18"> to view what stage the job is in.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-stage-view-300.png" width="700">}}

    Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18"> to view the detailed view.

After either a successful or failed upgrade attempt has been performed, a new Upgrade History card appears on your LCM dashboard.

{{<figure src="/images/netq/lcm-upgrade-history-card-300.png" width="200">}}

Click **View** to return to the Upgrade History page as needed.

#### Sample Successful Upgrade

On successful completion, you can:

- Compare the network snapshots taken before and after the upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-success-detail-300.png" width="700">}}

    Click **Compare Snapshots** in the detail view.

    {{<figure src="/images/netq/lcm-upgrade-switches-compare-snapshots-300.png" width="700">}}

    Refer to {{<link title="#interpreting-the-comparison-data" text="Interpreting the Comparison Data">}} for information about analyzing these results.

- Download details about the upgrade in the form of a JSON-formatted file, by clicking **Download Report**.

- View the changes on the Switches card of the LCM dashboard.

    Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">, then **Upgrade Switches**.

    {{<figure src="/images/netq/lcm-switches-card-after-upgrade-300.png" width="200">}}

    In our example, all switches have been upgraded to Cumulus Linux 3.7.12.

Upgrades can be considered successful and still have post-check warnings. For example, the OS has been updated, but not all services are fully up and running after the upgrade. If one or more of the post-checks fail, warning messages are provided in the Post-Upgrade Tasks section of the preview. Click on the warning category to view the detailed messages.

<!-- Expand the following dropdown to view common failures, their causes and corrective actions.

{{< expand "Post-check Failure Messages"  >}}

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 24%" />
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr>
<th>Post-check</th>
<th>Message</th>
<th>Type</th>
<th>Description</th>
<th>Corrective Action</th>
</tr>
</thead>
<tbody>
<tr>
<td>Health of Services</td>
<td>Service &lt;service-name&gt; is missing on Host &lt;hostname&gt; for &lt;VRF default|VRF mgmt&gt;.</td>
<td>Warning</td>
<td>A given service is not yet running on the upgraded host. For example: Service ntp is missing on Host Leaf01 for VRF default.</td>
<td>Wait for up to x more minutes to see if the specified services come up. If they do not, xxx.</td>
</tr>
<tr>
<td>Switch Connectivity</td>
<td>Service &lt;service-name&gt; is missing on Host &lt;hostname&gt; for &lt;VRF default|VRF mgmt&gt;.</td>
<td>Warning</td>
<td>A given service is not yet running on the upgraded host. For example: Service ntp is missing on Host Leaf01 for VRF default.</td>
<td>Wait for up to x more minutes to see if the specified services come up. If they do not, xxx.</td>
</tr>
</tbody>
</table>

{{< /expand >}}-->

#### Sample Failed Upgrade

If an upgrade job fails for any reason, you can view the associated error(s):

1. From the Upgrade History dashboard, find the job of interest.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-fail-summary-300.png" width="700">}}

2. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">.

3. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-open-300.png" width="700">}}

    Note in this example, all of the pre-upgrade tasks were successful, but backup failed on the spine switches.

4. Double-click on an error to view a more detailed error message.

    This example, shows that the upgrade failure was due to bad switch access credentials. You would need to fix those and then create a new upgrade job.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-message-300.png" width="700">}}

#### Reasons for Upgrade Failure

Upgrades can fail at any of the stages of the process, including when backing up data, upgrading the Cumulus Linux software, and restoring the data. Failures can occur when attempting to connect to a switch or perform a particular task on the switch.

Some of the common reasons for upgrade failures and the errors they present:

| Reason | Error Message |
| --- | --- |
| Switch is not reachable via SSH | Data could not be sent to remote host "192.168.0.15". Make sure this host can be reached over ssh: ssh: connect to host 192.168.0.15 port 22: No route to host |
| Switch is reachable, but user-provided credentials are invalid | Invalid/incorrect username/password. Skipping remaining 2 retries to prevent account lockout: Warning: Permanently added '\<hostname-ipaddr\>' to the list of known hosts. Permission denied, please try again. |
| Switch is reachable, but a valid Cumulus Linux license is not installed | 1587866683.880463 2020-04-26 02:04:43 license.c:336 CRIT No license file. No license installed! |
| Upgrade task could not be run | Failure message depends on the why the task could not be run. For example: /etc/network/interfaces: No such file or directory |
| Upgrade task failed | Failed at- \<task that failed\>. For example: Failed at- MLAG check for the peerLink interface status |
| Retry failed after five attempts | FAILED In all retries to process the LCM Job |
