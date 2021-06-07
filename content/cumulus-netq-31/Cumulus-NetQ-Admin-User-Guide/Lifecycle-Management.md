---
title: Lifecycle Management
author: Cumulus Networks
weight: 640
toc: 4
---
As an administrator, you want to manage the deployment of Cumulus Networks product software onto your network devices (servers, appliances, and switches) in the most efficient way and with the most information about the process as possible. With this release, NetQ expands the lifecycle management (LCM) feature to include the discovery of Cumulus Linux switches that are not running NetQ, and a workflow for installation and upgrade of NetQ on switches in the LCM inventory.

LCM enables you to:

- Manage Cumulus Linux and Cumulus NetQ images in a local repository
- Configure switch access credentials (required for installations and upgrades)
- Manage Cumulus Linux switches
- Create snapshots of the network state at various times
- Create Cumulus NetQ configuration profiles
- Upgrade Cumulus NetQ (Agents and CLI) on Cumulus Linux switches with Cumulus NetQ Agents version 2.4.x or later
- Install or upgrade Cumulus NetQ (Agents and CLI) on Cumulus Linux switches with or without Cumulus NetQ Agents; all in a single job
- Upgrade Cumulus Linux on switches with Cumulus NetQ Agents version 2.4.x or later (includes upgrade of NetQ to 3.0.0 or 3.1.0)

{{<notice note>}}
This feature is fully enabled for on-premises deployments and fully disabled for cloud deployments. Contact your local Cumulus Networks sales representative or {{<exlink url="https://support.mellanox.com/s/contact-support-page" text="submit a support ticket">}} to activate LCM on cloud deployments.
{{</notice>}}

## Access Lifecycle Management Features

You can access the lifecycle management features from several places in NetQ. All of them take you to the same location:

- Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu" /> (Main Menu) and select **Upgrade Switches**
- If you have a workbench open:
     - Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**
    - Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" height="18" width="18"/> (Upgrade) in the workbench header (this option is planned for removal in later releases)

The first time you open the Manage Switch Assets view, it provides a summary card for switch inventory, uploaded Cumulus Linux images, uploaded NetQ images, NetQ configuration profiles, and switch access settings. Additional cards appear after that based on your activity.

{{<figure src="/images/netq/lcm-dashboard-310.png" width="700">}}

## Manage Cumulus Linux and NetQ Images

You can manage both Cumulus Linux and Cumulus NetQ images with LCM. They are managed in a similar manner.

Cumulus Linux binary images can be uploaded to a local LCM repository for upgrade of your switches. Cumulus NetQ debian packages can be uploaded to the local LCM repository for installation or upgrade. You can upload images from an external drive.

The Linux and NetQ images are available in several variants based on the software version (x.y.z), the CPU architecture (ARM, x86), platform (based on ASIC vendor, Broadcom or Mellanox), SHA Checksum, and so forth. When LCM discovers Cumulus Linux switches running NetQ 2.x or later in your network, it extracts the meta data needed to select the appropriate image for a given switch.  Similarly, LCM discovers and extracts the meta data from NetQ images.

{{<figure src="/images/netq/lcm-image-naming-conventions-310.png" width="400">}}

The Cumulus Linux Images and NetQ Images cards provide a summary of image status in LCM. They show the total number of images in the repository, a count of missing images, and the starting points for adding and managing your images.

### Default Cumulus Linux or Cumulus NetQ Version Assignment

You can assign a specific Cumulus Linux or Cumulus NetQ version as the default version to use during installation or upgrade of switches. It is recommended that you choose the newest version that you intend to install or upgrade on all, or the majority, of your switches. The default selection can be overridden during individual installation and upgrade job creation if an alternate version is needed for a given set of switches.

### Missing Images

You should upload images for each variant of Cumulus Linux and Cumulus NetQ currently installed on the switches in your inventory if you want to support rolling back to a known good version should an installation or upgrade fail. LCM prompts you to upload any missing images to the repository.

For example, if you have both Cumulus Linux 3.7.3 and 3.7.11 versions, some running on ARM and some on x86 architectures, then LCM verifies the presence of each of these images. If only the 3.7.3 x86, 3.7.3 ARM, and 3.7.11 x86 images are in the repository, LCM would list the 3.7.11 ARM image as missing. For Cumulus NetQ, you need both the `netq-apps` and `netq-agent` packages for each release variant.

If you have specified a default Cumulus Linux and/or Cumulus NetQ version, LCM also verifies that the necessary versions of the default image are available based on the known switch inventory, and if not, lists those that are missing.

While it is not required that you upload images that NetQ determines to be missing, it may cause failures when you attempt to upgrade your switches.

### Upload Images

For fresh installations of NetQ 3.x, no images have yet been uploaded to the LCM repository. If you are upgrading from NetQ 3.0.0, the Cumulus Linux images you have previously added are still present.

In preparation for *Cumulus Linux* upgrades, the recommended image upload flow is:

| Step | Task | Instructions |
| :----: | ---- | ---- |
| 1 | In a fresh NetQ install, add images that match your current inventory | {{<link url="Lifecycle-Management/#upload-missing-images" text="Upload Missing Images">}} |
| 2 | Add images you want to use for upgrade | {{<link url="Lifecycle-Management/#upload-upgrade-images" text="Upload Upgrade Images">}} |
| 3 | Optionally specify a default version for upgrades | {{<link url="Lifecycle-Management/#specify-a-default-upgrade-image" text="Specify a Default Upgrade Image">}} |

In preparation for *Cumulus NetQ* installation or upgrade, the recommended image upload flow is:

| Step | Task | Instructions |
| :----: | ---- | ---- |
| 1 | Add images you want to use for installation or upgrade | {{<link url="Lifecycle-Management/#upload-missing-images" text="Upload Upgrade Images">}} |
| 2 | Add any missing images based on NetQ discovery | {{<link url="Lifecycle-Management/#upload-upgrade-images" text="Upload Missing Images">}} |
| 3 | Optionally specify a default version for installation or upgrade | {{<link url="Lifecycle-Management/#specify-a-default-upgrade-image" text="Specify a Default Upgrade Image">}} |

#### Upload Missing Images

Use the following instructions to upload missing images:

{{< tabs "TabID65" >}}

{{< tab "Cumulus Linux" >}}

1. On the Cumulus Linux Images card, click the *View missing CL images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-linux-images-card-at-install-missinglink-300.png" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

2. Select one of the missing images and make note of the version, ASIC Vendor, and CPU architecture.

  {{<figure src="/images/netq/lcm-images-missing-list-300.png" width="700">}}

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

  {{<figure src="/images/netq/lcm-import-linux-image-dialog-310.png" width="250">}}

4. Provide the *.bin* file from an external drive that matches the criteria for the selected image, either by dragging and dropping it onto the dialog or by selecting it from a directory.

5. Click **Import**.

    {{<figure src="/images/netq/lcm-import-linux-image-in-process-310.png" width="250">}}

<div style="padding-left: 18px;">On successful completion, you receive confirmation of the upload.</div>

    {{<figure src="/images/netq/lcm-import-linux-image-success-310.png" width="250">}}

<div style="padding-left: 18px;">If the upload was not successful, an <em>Image Import Failed</em> message is shown. Close the Import Image dialog and try uploading the file again.</div>

6. Click **Done**.

7. Click **Uploaded** tab to verify the image is in the repository.

8. Repeat Steps 1-7 until all of the missing images are uploaded to the repository. When all of the missing images have been uploaded, the Missing list will be empty.

9. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The Cumulus Linux Images card now shows the number of images you uploaded.

{{< /tab >}}

{{< tab "Cumulus NetQ" >}}

1. On the NetQ Images card, click the *View missing NetQ images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-netq-images-missinglink-310.png" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

2. Select one of the missing images and make note of the OS version, CPU architecture, and image type. Remember that you need both image types for NetQ to perform the installation or upgrade.

    {{<figure src="/images/netq/lcm-netq-images-missing-list-310.png" width="700">}}

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

    {{<figure src="/images/netq/lcm-import-netq-image-dialog-310.png" width="250">}}

4. Provide the *.deb* file from an external drive that matches the criteria for the selected image, either by dragging and dropping it onto the dialog or by selecting it from a directory.

5. Click **Import**.

    {{<figure src="/images/netq/lcm-import-netq-image-in-process-310.png" width="250">}}

<div style="padding-left: 18px;">On successful completion, you receive confirmation of the upload.</div>

    {{<figure src="/images/netq/lcm-import-netq-image-success-310.png" width="250">}}

<div style="padding-left: 18px;">If the upload was not successful, an <em>Image Import Failed</em> message is shown. Close the Import Image dialog and try uploading the file again.</div>

6. Click **Done**.

7. Click **Uploaded** tab to verify the image is in the repository.

8. Repeat Steps 1-7 until all of the missing images are uploaded to the repository. When all of the missing images have been uploaded, the Missing list will be empty.

9. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The NetQ Images card now shows the number of images you uploaded.

{{< /tab >}}

{{< /tabs >}}

#### Upload Upgrade Images

To upload the Cumulus Linux or Cumulus NetQ images that you want to use for upgrade:

1. Click **Add Image** on the Cumulus Linux Images or NetQ Images card.

    {{<img src="/images/netq/lcm-linux-images-card-at-install-addimage-300.png" width="200">}} {{<img src="/images/netq/lcm-netq-images-card-at-install-addimage-310.png" width="200">}}

2. Provide an image from an external drive, either by dragging and dropping it onto the dialog or by selecting it from a directory.

    {{<img src="/images/netq/lcm-import-linux-image-dialog-310.png" width="250">}} {{<img src="/images/netq/lcm-import-netq-image-dialog-310.png" width="250">}}

3. Click **Import**.

4. Monitor the progress until it completes. Click **Done**.

5. Repeat Steps 1-4 to upload additional images as needed.

    For example, if you are upgrading switches with different ASIC vendors or CPU architectures, you will need more than one image. For NetQ, you need both the netq-apps and netq-agent packages for each variant.

#### Specify a Default Upgrade Version

Lifecycle management does not have a default Cumulus Linux or Cumulus NetQ upgrade version specified automatically. You must specify the version that is appropriate for your network.

To specify a default Cumulus Linux or Cumulus NetQ version:

1. Click the *Click here to set the default CL version* link in the middle of the Cumulus Linux Images card, or click the *Click here to set the default NetQ version* link in the middle of the NetQ Images card.

    {{<img src="/images/netq/lcm-images-card-spec-default-cl-300.png" width="200">}} {{<img src="/images/netq/lcm-images-card-spec-default-netq-310.png" width="200">}}

2. Select the version you want to use as the default for switch upgrades.

3. Click **Save**. The default version is now displayed on the relevant Images card.

    {{<img src="/images/netq/lcm-images-card-default-assigned-300.png" width="200">}}    {{<img src="/images/netq/lcm-netq-images-default-assigned-310.png" width="200">}}

After you have specified a default version, you have the option to change it.

To change the default Cumulus Linux or Cumulus NetQ version:

1. Click **change** next to the currently identified default image on the Cumulus Linux Images or NetQ Images card.

2. Select the image you want to use as the default version for upgrades.

3. Click **Save**.

### Export Images

You can export the image listings for reference.

To export image listings:

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

3. Optionally, use the filter option above the table on the **Uploaded** tab to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

    {{<figure src="/images/netq/lcm-netq-images-uploaded-tab-310.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> above the table.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-300.png" width="250">}}

### Remove Images from Local Repository

Once you have upgraded all of your switches beyond a particular release of Cumulus Linux or NetQ, you may want to remove those images from the LCM repository to save space on the server.

To remove images:

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

3. On the **Uploaded** tab, select the images you want to remove. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

    {{<figure src="/images/netq/lcm-netq-images-uploaded-tab-310.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

## Manage Switch Access Credentials

Switch access credentials are needed for performing upgrades. You can choose between basic authentication (SSH password) and SSH (Public/Private key) authentication. These credentials apply to all switches. If you have switches with varying access credentials you will have to work with one set at a time and change the credentials as needed.

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
You must have sudoer permission to properly configure switch access for the SSH Key method.
{{</notice>}}

1. Enter the username of the user(s) that has access to switches for configuration.

2. Create a pair of SSH private and public keys.

    ```
    ssh-keygen -t rsa -C "<USER>"
    ```

3. Copy the SSH *public* key to each switch that you want to upgrade using one of the following methods:

    - Manually copy SSH public key to the */home/\<USER\>/.ssh/authorized_keys* file on each switch, or
    - Run `ssh-copy-id USER@<switch_ip>` on the server where the SSH key pair was generated for each switch

4. Copy the SSH *private* key into the text box in the Create Switch Access card.

    {{<figure src="/images/netq/lcm-access-create-SSH-310.png" width="250">}}

<div style="padding-left: 18px;">
{{<notice note>}}
For security, your private key is stored in an encrypted format, and only provided to internal processes while encrypted.
{{</notice>}}

The Access card now indicates your credential configuration.</div>

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
    - **SSH**: Enter a new username and/or SSH private key

    {{<notice tip>}}
Refer to {{<link title="#Specify Switch Credentials" text="Specify Switch Credentials">}} for details.
    {{</notice>}}

5. Click **Save**.

## Manage Switches

This lifecycle management feature provides an inventory of switches that have been automatically discovered by NetQ and are available for software installation or upgrade through NetQ. This includes all Cumulus Linux switches with or without Cumulus NetQ Agent 2.4 or later installed in your network. You assign network roles to switches and select switches for software installation and upgrade from this inventory listing.

A count of the switches NetQ was able to discover and the Cumulus Linux versions that are running on those switches is available from the LCM dashboard.

{{<figure src="/images/netq/lcm-switches-card-310.png" width="400">}}

To view a list of all switches known to LCM, click **Manage** on the Switches card.

{{<figure src="/images/netq/lcm-switch-mgmt-list-300.png" width="700">}}

Review the list, filtering as needed (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/15-Filter/filter-1.svg" height="18" width="18" alt="Filter Switch List">}}) to determine if the switches you want to upgrade are included.

If the switches you are looking to upgrade are not present in the final list, you can:

- Work with the list you have and add them later
- Verify the missing switches are reachable using `ping`
- Verify NetQ Agent is fresh for switches that already have the agent installed (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click **Agents** or run `netq show agents`)
- Install NetQ on the switch (refer to {{<link url="Lifecycle-Management/#use-switch-discovery-to-install-and-upgrade-netq" text="Install NetQ">}})

After all of the switches you want to upgrade are contained in the list, you can assign roles to them.

### Role Management

Four pre-defined switch roles are available based on a CLOS architecture:

- Superspine
- Spine
- Leaf
- Exit

With this release, you cannot create your own roles.

Switch roles are used to:

- Identify switch dependencies and determine the order in which switches are upgraded
- Determine when to stop the process if a failure is encountered

When roles are assigned, the upgrade process begins with switches having the superspine role, then continues with the spine switches, leaf switches, exit switches, and finally switches with no role assigned. All switches with a given role must be successfully upgraded before the switches with the closest dependent role can be upgraded.

For example, a group of seven switches are selected for upgrade. Three are spine switches and four are leaf switches. After all of the spine switches are successfully upgraded, then the leaf switches are upgraded. If one of the spine switches were to fail the upgrade, the other two spine switches are upgraded, but the upgrade process stops after that, leaving the leaf switches untouched, and the upgrade job fails. The spine switch that failed to upgrade is rolled back to its original release if that option is chosen in the upgrade job.

When only some of the selected switches have roles assigned in an upgrade job, the switches with roles are upgraded first and then all the switches with no roles assigned are upgraded.

While role assignment is optional, using roles can prevent switches from becoming unreachable due to dependencies between switches or single attachments. And when MLAG pairs are deployed, switch roles avoid upgrade conflicts. For these reasons, Cumulus Networks highly recommends assigning roles to all of your switches.

#### Assign Switch Roles

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select one switch or multiple switches that should be assigned to the same role.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}}.

5. Select the role that applies to the selected switch(es).

    {{<figure src="/images/netq/lcm-role-assign-role-selection-300.png" width="300">}}

6. Click **Assign**.

    Note that the **Role** column is updated with the role assigned to the selected switch(es).

    {{<figure src="/images/netq/lcm-switches-listing-310.png" width="700">}}

7. Continue selecting switches and assigning roles until most or all switches have roles assigned.

A bonus of assigning roles to switches is that you can then filter the list of switches by their roles by clicking the appropriate tab.

#### Change the Role of a Switch

If you accidentally assign an incorrect role to a switch, it can easily be changed to the correct role.

To change a switch role:

1. Open the LCM dashboard.

2. On the Switches card, click **Manage**.

3. Select the switch(es) with the incorrect role from the list.

4. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/58-Tags-Bookmarks/tags.svg" height="18" width="18" alt="Assign Role">}}.

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

## Configuration Management

With the NetQ 3.1.0 release, you can set up a configuration profile to indicate how you want NetQ configured when it is installed or upgraded on your Cumulus Linux switches.

The default configuration profile, *NetQ default config*, is set up to run in the management VRF and provide info level logging. Both WJH and CPU Limiting are disabled.

You can view, add, and remove NetQ configuration profiles at any time.

### View Cumulus NetQ Configuration Profiles

To view existing profiles:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the NetQ Configurations card.

    Note that the initial value on first installation of NetQ shows one profile. This is the default profile provided with NetQ.

    {{<figure src="/images/netq/lcm-netq-config-card-on-install-310.png" width="200">}}

3. Review the profiles.

    {{<figure src="/images/netq/lcm-netq-config-profiles-list-310.png" width="550">}}

### Create Cumulus NetQ Configuration Profiles

You can specify four options when creating NetQ configuration profiles:

- Basic: VRF assignment and Logging level
- Advanced: CPU limit and what just happened (WJH)

To create a profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the NetQ Configurations card.

3. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18" alt="Add Config Profile">}} (Add Config).

    {{<figure src="/images/netq/lcm-netq-config-profile-create-310.png" width="450">}}

4. Enter a name for the profile.

5. If you do not want NetQ Agent to run in the management VRF, select either *Default* or *Custom*. The Custom option lets you enter the name of a user-defined VRF.

6. Optionally enable WJH.

    Refer to {{<link url="Monitor-Network-Elements/#view-what-just-happened" text="WJH">}} for information about this feature. *WJH is only available on Mellanox switches.*

7. To set a logging level, click **Advanced**, then choose the desired level.

    {{<figure src="/images/netq/lcm-netq-config-profile-log-level-310.png" width="450">}}

8. Optionally set a CPU usage limit for the NetQ Agent. Click **Enable** and drag the dot to the desired limit. Refer to this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Cumulus-NetQ/NetQ-Agent-CPU-Utilization-on-Cumulus-Linux-Switches" >}}) for information about this feature.

9. Click **Add** to complete the configuration or **Close** to discard the configuration.

    This example shows the addition of a profile with the CPU limit set to 75 percent.

    {{<figure src="/images/netq/lcm-netq-config-profile-added-310.png" width="550">}}

### Remove Cumulus NetQ Configuration Profiles

To remove a NetQ configuration profile:

1. Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**, or click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**.

2. Click **Manage** on the NetQ Configurations card.

3. Select the profile(s) you want to remove and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" width="18" height="18">}} (Delete).

## Upgrade Cumulus NetQ

LCM enables you to upgrade to Cumulus NetQ 3.1.0 on switches with an existing NetQ Agent 2.4.x or 3.0.0 release. You can upgrade the entire application or only the NetQ Agent. Up to five jobs can be run simultaneously; however, a given switch can only be contained in one running job at a time.

The upgrade workflow includes the following steps:

{{<figure src="/images/netq/lcm-netq-upgrade-workflow-310.png" width="600">}}

{{<notice info>}}
Upgrades can be performed from NetQ 2.4.x and 3.0.0 releases to the NetQ 3.1.0 release. <em>Lifecycle management does not support upgrades from NetQ 2.3.1 or earlier releases; you must perform a new installation in these cases.</em>
{{</notice>}}

### Prepare for a Cumulus NetQ Upgrade

In preparation for Cumulus NetQ upgrade on switches, perform the following steps:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**, or click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**.

2. Add the {{<link url="Lifecycle-Management/#upload-upgrade-images" text="upgrade images">}}.

3. Optionally, specify a {{<link url="Lifecycle-Management/#specify-a-default-upgrade-version" text="default upgrade version">}}.

4. Optionally, create a new {{<link url="Lifecycle-Management/#create-cumulus-netq-configuration-profiles" text="configuration profile">}}.

Your LCM dashboard should look similar to this after you have completed the above steps:

{{<figure src="/images/netq/lcm-netq-upgrade-dashboard-post-prep-310.png" width="600">}}

### Perform a Cumulus NetQ Upgrade

To upgrade Cumulus NetQ on switches:

1. Click **Manage** on the Switches card.

2. Select the individual switches (or click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="16" width="18"/> to select all switches) with older NetQ releases that you want to upgrade. If needed, use the filter to narrow the listing and find the relevant switches.

3. Click {{<img src="/images/netq/netq-upgrade-icon-blk.png" height="18" width="18">}} above the table.

    From this point forward, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-netq-upgrade-review-switches-tab-310.png" width="500">}}

4. Verify that the number of switches selected for upgrade matches your expectation.

5. Enter a name for the upgrade job. The name can contain a maximum of 22 characters.

6. Review each switch:

    - Is the NetQ version 2.4.x or 3.0.0? If not, this switch can only be upgraded through the {{<link url="Lifecycle-Management/#switch-discovery" text="switch discovery">}} process.
    - Is the configuration profile the one you want to apply? If not, click **Change config**, then select an alternate profile to apply to all selected switches. 
    
    {{%notice tip%}}
You can apply *different* profiles to switches in a *single* upgrade job by selecting a subset of switches (click checkbox for each switch) and then choosing a different profile. You can also change the profile on a per switch basis by clicking the current profile link and selecting an alternate one.

{{<img src="/images/netq/lcm-netq-upgrade-select-alternate-profile-310.png" width="450">}}
    {{%/notice%}}

    Scroll down to view all selected switches or use **Search** to find a particular switch of interest.

7. After you are satisfied with the included switches, click **Next**.

8. Review the summary indicating the number of switches and the configuration profile to be used. If either is incorrect, click **Back** and review your selections.

    {{<figure src="/images/netq/lcm-netq-upgrade-select-version-tab-310.png" width="500">}}

9. Select the version of NetQ for upgrade. If you have designated a default version, keep the **Default** selection. Otherwise, select an alternate version by clicking **Custom** and selecting it from the list.

    By default, the NetQ Agent and CLI are upgraded on the selected switches. If you *do not* want to upgrade the NetQ CLI, click **Advanced** and change the selection to **No**.

10. Click **Next**.

11. Three checks are performed to eliminate preventable problems during the upgrade process.

    {{<figure src="/images/netq/lcm-netq-upgrade-precheck-tab-310.png" width="500">}}

    The first check verifies that the selected switches are not currently scheduled for, or in the middle of, a Cumulus Linux or NetQ upgrade. The second check verifies that the selected versions of Cumulus Linux and NetQ are valid upgrade paths. And the final check verifies that all mandatory parameters have valid values.

    If any of the pre-checks fail, review the error messages and take appropriate action.

    If all of the pre-checks pass, click **Upgrade** to initiate the upgrade job.

### Analyze the NetQ Upgrade Results

After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

From the preview page, a green circle with rotating arrows is shown on each switch as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the NetQ Install and Upgrade History page. The job started most recently is shown at the top, and the data is refreshed periodically.

{{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.
{{</notice>}}

#### Monitor the NetQ Upgrade Job

Several viewing options are available for monitoring the upgrade job.

- Monitor the job with full details open:

    {{<figure src="/images/netq/lcm-netq-upgrade-inprogress-310.png" width="700">}}

- Monitor the job with only summary information in the NetQ Install and Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view; useful when you have multiple jobs running simultaneously

    {{<figure src="/images/netq/lcm-netq-upgrade-history-summ-view-310.png" width="700">}}

    - Monitor the job through the NetQ Install and Upgrade History card on the LCM dashboard. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} twice to return to the LCM dashboard.

        {{<figure src="/images/netq/lcm-netq-upgrade-history-card-inprogress-310.png" width="200">}}

#### Sample Successful NetQ Upgrade

This example shows that all four of the selected switches were upgraded successfully. You can see the results in the Switches list as well.

{{<figure src="/images/netq/lcm-netq-upgrade-example-success-310.png" width="700">}}

#### Sample Failed NetQ Upgrade

This example shows that an error has occurred trying to upgrade two of the four switches in a job. The error indicates that the access permissions for the switches are invalid. In this case, you need to modify the {{<link url="Lifecycle-Management/#modify-switch-credentials" text="switch access credentials">}} and then create a new upgrade job.

{{<figure src="/images/netq/lcm-netq-upgrade-example-failure-310.png" width="700">}}

If you were watching this job from the LCM dashboard view, click **View** on the NetQ Install and Upgrade History card to return to the detailed view to resolve any issues that occurred.

#### Reasons for NetQ Upgrade Failure

Upgrades can fail at any of the stages of the process, including when backing up data, upgrading the Cumulus NetQ software, and restoring the data. Failures can occur when attempting to connect to a switch or perform a particular task on the switch.

Some of the common reasons for upgrade failures and the errors they present:

| Reason | Error Message |
| --- | --- |
| Switch is not reachable via SSH | Data could not be sent to remote host "192.168.0.15". Make sure this host can be reached over ssh: ssh: connect to host 192.168.0.15 port 22: No route to host |
| Switch is reachable, but user-provided credentials are invalid | Invalid/incorrect username/password. Skipping remaining 2 retries to prevent account lockout: Warning: Permanently added '\<hostname-ipaddr\>' to the list of known hosts. Permission denied, please try again. |
| Switch is reachable, but a valid Cumulus Linux license is not installed | 1587866683.880463 2020-04-26 02:04:43 license.c:336 CRIT No license file. No license installed! |
| Upgrade task could not be run | Failure message depends on the why the task could not be run. For example: /etc/network/interfaces: No such file or directory |
| Upgrade task failed | Failed at- \<task that failed\>. For example: Failed at- MLAG check for the peerLink interface status |
| Retry failed after five attempts | FAILED In all retries to process the LCM Job |

## Use Switch Discovery to Install and Upgrade NetQ

When you want to update Cumulus NetQ on both Cumulus Linux switches with and without NetQ installed, NetQ provides the LCM switch discovery feature. The feature browses your network to find all Cumulus Linux Switches, with and without NetQ currently installed and determines the versions of Cumulus Linux and NetQ installed. The results of switch discovery are then used to install or upgrade NetQ on all discovered switch in a single procedure rather than in two steps. Up to five jobs can be run simultaneously; however, a given switch can only be contained in one running job at a time.

The upgrade workflow includes the following steps:

{{<figure src="/images/netq/lcm-netq-upgrade-workflow-discovery-310.png" width="600">}}

{{<notice info>}}
Upgrades can be performed from NetQ 2.4.x and 3.0.0 releases to the NetQ 3.1.0 release. <em>Lifecycle management does not support upgrades from NetQ 2.3.1 or earlier releases; you must perform a new installation in these cases.</em>
{{</notice>}}

If all of your Cumulus Linux switches already have NetQ 2.4.x or later installed, you can upgrade them directly. Refer to {{<link url="Lifecycle-Management/#upgrade-cumulus-netq" text="Upgrade Cumulus NetQ">}}.

To discover Cumulus Linux switches and install or upgrade NetQ on them:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**, or click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**.

2. On the Switches card, click **Discover**.

    {{<figure src="/images/netq/lcm-switches-card-discovery-selected-310.png" width="200">}}

3. Enter a name for the scan.

    {{<figure src="/images/netq/lcm-discover-search-switches-tab-310.png" width="500">}}

4. Choose whether you want to look for switches by entering IP address ranges OR import switches using a comma-separated values (CSV) file.

    {{< tabs "TabID314" >}}

{{< tab "IP Address Range" >}}

If you do not have a switch listing, then you can manually add the address ranges where your switches are located in the network. This has the advantage of catching switches that may have been missed in a file.

{{<notice tip>}}
A maximum of 50 addresses can be included in an address range. If necessary, break the range into smaller ranges.
{{</notice>}}

To discover switches using address ranges:

1. Enter an IP address range in the **IP Range** field.

    Ranges can be contiguous, for example *192.168.0.24-64*, or non-contiguous, for example *192.168.0.24-64,128-190,235*, but they must be contained within a single subnet.

2. Optionally, enter another IP address range (in a different subnet) by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}}.

    For example, *198.51.100.0-128* or *198.51.100.0-128,190,200-253*.

3. Add additional ranges as needed. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/subtract-circle.svg" height="18" width="18">}} to remove a range if needed.

If you decide to use a CSV file instead, the ranges you entered will remain if you return to using IP ranges again.

{{< /tab >}}

{{< tab "CSV Import" >}}

If you have a file of switches that you want to import, then it can be easier to use that, than to enter the IP address ranges manually.

To import switches through a CSV file:

1. Click **Browse**.

2. Select the CSV file containing the list of switches.

    The CSV file must include a header containing *hostname*, *ip*, and *port*. They can be in any order you like, but the data must match that order. For example, a CSV file that represents the Cumulus reference topology could look like this:

    {{<figure src="/images/netq/lcm-import-switches-310.png" width="200">}}

<div style="padding-left: 18px;">or this:</div>

    {{<figure src="/images/netq/lcm-import-switches-2-310.png" width="200">}}

<div style="padding-left: 18px;">
{{<notice note>}}
You must have an IP address in your file, but the hostname is optional and if the port is blank, NetQ uses switch port 22 by default.
{{</notice>}}
</div>

Click **Remove** if you decide to use a different file or want to use IP address ranges instead. If you had entered ranges prior to selecting the CSV file option, they will have  remained.

{{< /tab >}}

    {{< /tabs >}}

5. Note that the switch access credentials defined in {{<link title="Lifecycle Management#Credentials Management" text="Credentials Management">}} are used to access these switches. If you have issues accessing the switches, you may need to update your credentials.

6. Click **Next**.

    When the network discovery is complete, NetQ presents the number of Cumulus Linux switches it has found. They are displayed in categories:

    - **Discovered without NetQ**: Switches found without NetQ installed
    - **Discovered with NetQ**: Switches found with some version of NetQ installed
    - **Discovered but Rotten**: Switches found that are unreachable
    - **Incorrect Credentials**: Switches found that cannot be reached because the provided access credentials do not match those for the switches
    - **OS not Supported**: Switches found that are running Cumulus Linux version not supported by the LCM upgrade feature
    - **Not Discovered**: IP addresses which did not have an associated Cumulus Linux switch

    If no switches are found for a particular category, that category is not displayed.

    {{<figure src="/images/netq/lcm-discover-select-switches-tab-310.png" width="500">}}

7. Select which switches you want to upgrade from each category by clicking the checkbox on each switch card.

    {{<figure src="/images/netq/lcm-discover-select-switches-tab-chosen-switches-310.png" width="500">}}

8. Click **Next**.

9. Verify the number of switches identified for upgrade and the configuration profile to be applied is correct.

10. Accept the default NetQ version or click **Custom** and select an alternate version.

11. By default, the NetQ Agent and CLI are upgraded on the selected switches. If you *do not* want to upgrade the NetQ CLI, click **Advanced** and change the selection to **No**.

12. Click **Next**.

13. Three checks are performed to eliminate preventable problems during the install process.

    {{<figure src="/images/netq/lcm-netq-upgrade-precheck-tab-310.png" width="500">}}

    The first check verifies that the selected switches are not currently scheduled for, or in the middle of, a Cumulus Linux or NetQ upgrade. The second check verifies that the selected versions of Cumulus Linux and NetQ are valid upgrade paths. And the final check verifies that all mandatory parameters have valid values.

    If any of the pre-checks fail, review the error messages and take appropriate action.

    If all of the pre-checks pass, click **Install** to initiate the job.

14. Monitor the job progress.

    After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

    From the preview page, a green circle with rotating arrows is shown on each switch as it is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the NetQ Install and Upgrade History page. The job started most recently is shown at the top, and the data is refreshed periodically.

    {{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.
    {{</notice>}}

    Several viewing options are available for monitoring the upgrade job.

    - Monitor the job with full details open:

        {{<figure src="/images/netq/lcm-discover-netq-upgrade-inprogress-310.png" width="700">}}

    - Monitor the job with only summary information in the NetQ Install and Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view; useful when you have multiple jobs running simultaneously

        {{<figure src="/images/netq/lcm-netq-upgrade-history-summ-view-310.png" width="700">}}

    - Monitor the job through the NetQ Install and Upgrade History card on the LCM dashboard. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} twice to return to the LCM dashboard.

        {{<figure src="/images/netq/lcm-netq-upgrade-history-card-inprogress-310.png" width="200">}}

15. Investigate any failures and create new jobs to reattempt the upgrade.

## Upgrade Cumulus Linux

LCM enables you to upgrade to Cumulus Linux on switches with an existing NetQ Agent 2.4.x or 3.0.0 release. As part of the Cumulus Linux upgrade, if a NetQ Agent 2.4.x release is installed, that is also upgraded. Up to five jobs can be run simultaneously; however, a given switch can only be contained in one running job at a time.

The upgrade workflow includes the following steps:

{{<figure src="/images/netq/lcm-upgrade-workflow-310.png" width="700">}}

{{<notice info>}}
Upgrades can be performed between Cumulus Linux 3.x releases, and between Cumulus Linux 4.x releases. <em>Lifecycle management does not support upgrades from Cumulus Linux 3.x to 4.x releases.</em>
{{</notice>}}

### Prepare for a Cumulus Linux Upgrade

In preparation for switch installation or upgrade, first perform the following steps:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**, or click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**.

2. Upload the Cumulus Linux and NetQ {{<link url="Lifecycle-Management/#upload-upgrade-images" text="upgrade images">}}.

3. Optionally, specify a {{<link url="Lifecycle-Management/#specify-a-default-upgrade-version" text="default upgrade version">}}.

4. Verify the switches you want to manage are running NetQ Agent 2.4 or later. Refer to {{<link title="#Switch Management" text="Switch Management">}}.

5. Optionally, create a new NetQ {{<link url="Lifecycle-Management/#create-cumulus-netq-configuration-profiles" text="configuration profile">}}.

6. Configure {{<link url="Lifecycle-Management/#manage-switch-access-credentials" text="switch access credentials">}}.

7. Assign each switch a role (optional, but recommended). Refer to {{<link title="#Role Management" text="Role Management">}}.

Your LCM dashboard should look similar to this after you have completed these steps:

{{<figure src="/images/netq/lcm-netq-upgrade-dashboard-post-prep-310.png" width="700">}}

### Perform a Cumulus Linux Upgrade

To upgrade switches:

1. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}} (Main Menu) and select **Upgrade Switches**, or click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**.

2. Click **Manage** on the Switches card.

    {{<figure src="/images/netq/lcm-upgrade-switch-manage-button-310.png" width="700">}}

3. Select the individual switches (or click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="16" width="18"/> to select all switches) that you want to upgrade. If needed, use the filter to the narrow the listing and find the relevant switches.

    {{<figure src="/images/netq/lcm-switch-mgmt-list-switches-selected-300.png" width="700">}}

4. Click {{<img src="/images/netq/cl-upgrade-icon-blk.png" height="14" width="18">}} (Upgrade CL) above the table.

    From this point forward, the software walks you through the upgrade process, beginning with a review of the switches that you selected for upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-tab-310.png" width="500">}}

5. Give the upgrade job a name. This is required.

    {{<notice tip>}}
    The name can be a maximum of 22 characters and contain spaces and special characters.
    {{</notice>}}

6. Verify that the switches you selected are included, and that they have the correct IP address and roles assigned.

    - If you accidentally included a switch that you do NOT want to upgrade, hover over the switch information card and click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18">}} to remove it from the upgrade job.
    - If the role is incorrect or missing, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/22-Edit/pencil-1.svg" height="18" width="18">}} to select a role for that switch, then click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/check-circle-1.svg" height="18" width="18">}}. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/delete-2.svg" height="18" width="18">}} to discard a role change.

    In this example, some of the selected switches do not have roles assigned.

    {{<figure src="/images/netq/lcm-upgrade-switches-review-switches-missing-roles-300.png" width="500">}}

7. When you are satisfied that the list of switches is accurate for the job, click **Next**.

8. Verify that you want to use the default Cumulus Linux or NetQ version for this upgrade job. If not, click **Custom** and select an alternate image from the list.

    {{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-310.png" width="500" caption="Default CL Version Selected">}}{{<figure src="/images/netq/lcm-upgrade-switches-describe-tab-custom-version-310.png" width="500" caption="Custom CL Version Selected">}}

9. Note that the switch access authentication method, *Using global access credentials*, indicates you have chosen either basic authentication with a username and password or SSH key-based authentication for all of your switches. Authentication on a per switch basis is not currently available.

10. Click **Next**.

11. Verify the upgrade job options.

    By default, NetQ takes a network snapshot before the upgrade and then one after the upgrade is complete. It also performs a roll back to the original Cumulus Linux version on any server which fails to upgrade.

    You can exclude selected services and protocols from the snapshots. By default, node and services are included, but you can deselect any of the other items. Click on one to remove it; click again to include it. This is helpful when you are not running a particular protocol or you have concerns about the amount of time it will take to run the snapshot. Note that removing services or protocols from the job may product unequivalent results compared with prior snapshots.

    While these options provide a smoother upgrade process and are highly recommended, you have the option to disable these options by clicking **No** next to one or both options.

    {{<figure src="/images/netq/lcm-upgrade-switches-options-tab-310.png" width="500">}}

12. Click **Next**.

13. After the pre-checks have completed successfully, click **Preview**.

    {{<figure src="/images/netq/lcm-upgrade-switches-precheck-tab-success-310.png" width="500">}}

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
<td><p>Verify you have the correct hostname or IP address for the switch. </p> <p>Verify the switch has NetQ Agent 2.4.0 or later installed: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agents if needed. Refer to {{<link title="Upgrade NetQ Agents">}}.</p></td>
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
<td>Verify the switch has NetQ Agent 2.4.0 or later installed: click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18" alt="Main Menu">}}, then click <strong>Agents</strong> in the <strong>Network</strong> section, view <strong>Version</strong> column. Upgrade NetQ Agent if needed. Refer to {{<link title="Upgrade NetQ Agents">}}. Add the missing peer switch to NetQ inventory.</td>
</tr>
</tbody>
</table>

{{< /expand >}}

14. Review the job preview.

    - When all of your switches have roles assigned, this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), the order in which the switches are planned for upgrade (center; upgrade starts from the left), and the post-upgrade tasks status (right).

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-300.png" width="700" caption="Roles assigned">}}

    - When none of your switches have roles assigned (or they are all of the same role), this view displays the chosen job options (top center), the pre-checks status (top right and left in Pre-Upgrade Tasks), a list of switches planned for upgrade (center), and the post-upgrade tasks status (right).

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-single-roll-310.png" width="700" caption="No roles assigned">}}

    - When some of your switches have roles assigned, any switches without roles are upgraded last and are grouped under the label *Stage1*.

        {{<figure src="/images/netq/lcm-upgrade-switches-preview-job-someroles-310.png" width="700" caption="Some roles assigned">}}

15. When you are happy with the job specifications, click **Start Upgrade**.

16. Confirm the upgrade request.

    {{<figure src="/images/netq/lcm-upgrade-confirmation-310.png" width="250">}}

### Analyze Cumulus Linux Results

After starting the upgrade you can monitor the progress from the preview page or the Upgrade History page.

From the preview page, a green circle with rotating arrows is shown above each step set of switches (if roles are configured) and on each switch as as the job is working. Alternately, you can close the detail of the job and see a summary of all current and past upgrade jobs on the Upgrade History page. The job started most recently is shown at the top, and the data is refreshed periodically.

Switches are displayed in the order of upgrade, by role/category and within roles/categories. Switches that are planned for upgrade first are listed first. You can scroll down within a role or category to see the additional switches to be upgraded.

{{<notice tip>}}
If you are disconnected while the job is in progress, it may appear as if nothing is happening. Try closing (click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}}) and reopening your view (click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}), or refreshing the page.
{{</notice>}}

#### Monitoring the Cumulus Linux Upgrade

Several viewing options are available for monitoring the upgrade job.

- Monitor the job with full details open:

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-310.png" width="700" caption="Single role or no roles">}}

    {{<figure src="/images/netq/lcm-upgrade-switches-job-upgrading-2-310.png" width="700" caption="Multiple roles and some without roles">}}

    Each switch goes through a number of steps. To view these steps, click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}} and scroll down as needed. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-up-1.svg" height="18" width="18">}} to close the detail.

- Monitor the job with summary information only in the CL Upgrade History page. Open this view by clicking {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} in the full details view:

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-upgrading-summary-310.png" width="700">}}

    This view is refreshed automatically. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}} to view what stage the job is in.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-stage-view-310.png" width="700">}}

    Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}} to view the detailed view.

- Monitor the job through the CL Upgrade History card on the LCM dashboard. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} twice to return to the LCM dashboard. As you perform more upgrades the graph displays the success and failure of each job.

    {{<figure src="/images/netq/lcm-cl-upgrade-history-card-inprogress-310.png" width="450">}}

    Click **View** to return to the Upgrade History page as needed.

After either a successful or failed upgrade attempt has been performed, the CL Upgrade History card is updated on your LCM dashboard.

#### Sample Successful Upgrade

On successful completion, you can:

- Compare the network snapshots taken before and after the upgrade.

    {{<figure src="/images/netq/lcm-upgrade-switches-success-detail-300.png" width="700">}}

    Click **Compare Snapshots** in the detail view.

    {{<figure src="/images/netq/lcm-upgrade-switches-compare-snapshots-300.png" width="700">}}

    Refer to {{<link title="#interpreting-the-comparison-data" text="Interpreting the Comparison Data">}} for information about analyzing these results.

- Download details about the upgrade in the form of a JSON-formatted file, by clicking **Download Report**.

- View the changes on the Switches card of the LCM dashboard.

    Click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/> (Switches) in the workbench header, then click **Manage switches**.

    {{<figure src="/images/netq/lcm-switches-card-after-upgrade-310.png" width="700">}}

    In our example, all spine switches have been upgraded to Cumulus Linux 3.7.13. Leaf and other switches have not been upgraded, so both Cumulus Linux versions 3.7.12 and 3.7.13 are shown.

Upgrades can be considered successful and still have post-check warnings. For example, the OS has been updated, but not all services are fully up and running after the upgrade. If one or more of the post-checks fail, warning messages are provided in the Post-Upgrade Tasks section of the preview. Click on the warning category to view the detailed messages. Sometimes waiting another few minutes will clear service-related warnings.

Expand the following dropdown to view common failures, their causes and corrective actions.

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

{{< /expand >}}

#### Sample Failed Upgrade

If an upgrade job fails for any reason, you can view the associated error(s):

1. From the Upgrade History dashboard, find the job of interest.

    {{<figure src="/images/netq/lcm-upgrade-switches-upg-history-fail-summary-310.png" width="700">}}

2. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-down-1.svg" height="18" width="18">}}.

3. Click {{<img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-right-1.svg" height="18" width="18">}}.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-open-310.png" width="700">}}

    In this example, all of the pre-upgrade tasks were successful, but the spine switches were unreachable. Checking the status of the switches, they were rotten.

4. Double-click on an error to view a more detailed error message.

    This example, shows that the upgrade failure was due to bad switch access credentials. You would need to fix those and then create a new upgrade job.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-error-message-300.png" width="700">}}

    This example shows that only one spine switch was upgraded and three failed to be upgraded and failed to roll back to the original release.

    {{<figure src="/images/netq/lcm-upgrade-switches-upgrade-rollback-error-310.png" width="700">}}

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

## Create and Compare Network Snapshots

Creating and comparing network snapshots can be useful to validate that the network state has not changed. Snapshots are typically created when you upgrade or change the configuration of your switches in some way.  This section describes the Snapshot card and content, as well as how to create and compare network snapshots at any time. Snapshots can be automatically created during the upgrade process for Cumulus Linux or NetQ. Refer to {{<link title="#Image Installation and Upgrade" text="Image Installation and Upgrade">}}.

<!-- Add additional links here for netq upgrade/install? -->

### Create a Network Snapshot

It is simple to capture the state of your network currently or for a time in the past using the snapshot feature.

To create a network snapshot:

1. From any workbench, click {{<img src="/images/netq/camera.svg" width="22.5" height="18">}} in the workbench header.

2. Click **Create Snapshot**.

    {{<figure src="/images/netq/snapshot-create-snap-dialog-310.png" width="450">}}

3. Enter a name for the snapshot.

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

7. Click **Finish**.

    A medium Snapshot card appears on your desktop. Spinning arrows are visible while it works. When it finishes you can see the number of items that have been captured, and if any failed. This example shows a successful result.

    {{<figure src="/images/netq/snapshot-success-300.png" width="200">}}

    {{<notice note>}}
If you have already created other snapshots, <strong>Compare</strong> is active. Otherwise it is inactive (grayed out).
    {{</notice>}}

Click **Dismiss** to close the snapshot. The snapshot is not deleted, merely removed from the workbench.

### Compare Network Snapshots

You can compare the state of your network before and after an upgrade or other configuration change to validate that the changes have not created an unwanted change in your network state.

To compare network snapshots:

1. Create a snapshot (as described in previous section) *before* you make any changes.

2. Make your changes.

3. Create a second snapshot.

4. Compare the results of the two snapshots.

    Depending on what, if any, cards are open on your workbench:

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
