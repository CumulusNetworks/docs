---
title: Manage Cumulus Linux and NetQ Images
author: Cumulus Networks
weight: 630
toc: 4
---
You can manage both Cumulus Linux and Cumulus NetQ images with LCM. They are managed in a similar manner.

Cumulus Linux binary images can be uploaded to a local LCM repository for upgrade of your switches. Cumulus NetQ debian packages can be uploaded to the local LCM repository for installation or upgrade. You can upload images from an external drive.

The Linux and NetQ images are available in several variants based on the software version (x.y.z), the CPU architecture (ARM, x86), platform (based on ASIC vendor, Broadcom or Mellanox), SHA Checksum, and so forth. When LCM discovers Cumulus Linux switches running NetQ 2.x or later in your network, it extracts the meta data needed to select the appropriate image for a given switch.  Similarly, LCM discovers and extracts the meta data from NetQ images.

{{<figure src="/images/netq/lcm-image-naming-conventions-310.png" width="400">}}

The Cumulus Linux Images and NetQ Images cards in the NetQ UI provide a summary of image status in LCM. They show the total number of images in the repository, a count of missing images, and the starting points for adding and managing your images.

The `netq lcm show images` command also displays a summary of the images uploaded to the LCM repo on the NetQ appliance or VM.

## Default Cumulus Linux or Cumulus NetQ Version Assignment

In the NetQ UI, you can assign a specific Cumulus Linux or Cumulus NetQ version as the default version to use during installation or upgrade of switches. It is recommended that you choose the newest version that you intend to install or upgrade on all, or the majority, of your switches. The default selection can be overridden during individual installation and upgrade job creation if an alternate version is needed for a given set of switches.

## Missing Images

You should upload images for each variant of Cumulus Linux and Cumulus NetQ currently installed on the switches in your inventory if you want to support rolling back to a known good version should an installation or upgrade fail. The NetQ UI prompts you to upload any missing images to the repository.

For example, if you have both Cumulus Linux 3.7.3 and 3.7.11 versions, some running on ARM and some on x86 architectures, then LCM verifies the presence of each of these images. If only the 3.7.3 x86, 3.7.3 ARM, and 3.7.11 x86 images are in the repository, the NetQ UI would list the 3.7.11 ARM image as missing. For Cumulus NetQ, you need both the `netq-apps` and `netq-agent` packages for each release variant.

If you have specified a default Cumulus Linux and/or Cumulus NetQ version, the NetQ UI also verifies that the necessary versions of the default image are available based on the known switch inventory, and if not, lists those that are missing.

While it is not required that you upload images that NetQ determines to be missing, not doing so may cause failures when you attempt to upgrade your switches.

## Upload Images

For fresh installations of NetQ 3.2, no images have yet been uploaded to the LCM repository. If you are upgrading from NetQ 3.0.0 or 3.1.0, the Cumulus Linux images you have previously added are still present.

In preparation for *Cumulus Linux* upgrades, the recommended image upload flow is:

1. In a fresh NetQ install, add images that match your current inventory: {{<link url="#upload-missing-images" text="Upload Missing Images">}}

2. Add images you want to use for upgrade: {{<link url="#upload-upgrade-images" text="Upload Upgrade Images">}}

3. In NetQ UI, optionally specify a default version for upgrades: {{<link url="#specify-a-default-upgrade-image" text="Specify a Default Upgrade Image">}}

In preparation for *Cumulus NetQ* installation or upgrade, the recommended image upload flow is:

1. Add images you want to use for installation or upgrade: {{<link url="#upload-missing-images" text="Upload Upgrade Images">}}

2. Add any missing images: {{<link url="#upload-upgrade-images" text="Upload Missing Images">}}

3. In NetQ UI, optionally specify a default version for installation or upgrade | {{<link url="#specify-a-default-upgrade-image" text="Specify a Default Upgrade Image">}}

### Upload Missing Images

Use the following instructions to upload missing Cumulus Linux and NetQ images:

For *Cumulus Linux* images:

{{< tabs "TabID61" >}}

{{< tab "NetQ UI" >}}

1. On the Cumulus Linux Images card, click the *View # missing CL images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-linux-images-card-at-install-missinglink-300.png" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

2. Select one or more of the missing images and make note of the version, ASIC Vendor, and CPU architecture for each.

    {{<figure src="/images/netq/lcm-images-missing-list-320.png" width="700">}}

<div style="padding-left: 18px;">Note the Disk Space Utilized information in the header to verify that you have enough space to upload the Cumulus Linux images.
</div>
   {{<figure src="/images/netq/lcm-disk-space-aid-320.png" width="150">}}

3. Download the Cumulus Linux disk images (*.bin* files) needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}} page, selecting the appropriate version, CPU, and ASIC. Place them in an accessible part of your local network.

4. Back in the UI, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

  {{<figure src="/images/netq/lcm-import-linux-image-dialog-320.png" width="250">}}

5. Provide the *.bin* file from an external drive that matches the criteria for the selected image(s), either by dragging and dropping onto the dialog or by selecting from a directory.

6. Click **Import**.

    {{<figure src="/images/netq/lcm-import-linux-image-in-process-320.png" width="250">}}

<div style="padding-left: 18px;">On successful completion, you receive confirmation of the upload and the Disk Space Utilization is updated.</div>

    {{<figure src="/images/netq/lcm-import-linux-image-success-320.png" width="250">}}

<div style="padding-left: 18px;">If the upload was not successful, an <em>Image Import Failed</em> message is shown. Close the Import Image dialog and try uploading the file again.
</div>

7. Click **Done**.

8. Click **Uploaded** to verify the image is in the repository.

    {{<figure src="/images/netq/lcm-import-linux-image-uploaded-320.png" width="700">}}

9. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The Cumulus Linux Images card now shows the number of images you uploaded.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Download the Cumulus Linux disk images (*.bin* files) needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}} page, selecting the appropriate version, CPU, and ASIC. Place them in an accessible part of your local network.

2. Upload the images to the LCM repository. This example uses a Cumulus Linux 4.1.0 disk image.

    ```
    cumulus@switch:~$ netq lcm add cl-image /path/to/download/cumulus-linux-4.1.0-vx-amd64.bin
    ```

3. Repeat Step 2 for each image you need to upload to the LCM repository.

{{< /tab >}}

{{< /tabs >}}

For *Cumulus NetQ* images:

{{< tabs "TabID122">}}

{{< tab "NetQ UI" >}}

1. On the NetQ Images card, click the *View # missing NetQ images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-netq-images-missinglink-310.png" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

2. Select one or all of the missing images and make note of the OS version, CPU architecture, and image type. Remember that you need both image types for NetQ to perform the installation or upgrade.

    {{<figure src="/images/netq/lcm-netq-images-missing-list-310.png" width="700">}}

3. Download the Cumulus NetQ debian packages needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads page">}}, selecting the appropriate version and hypervisor/platform. Place them in an accessible part of your local network.

4. Back in the UI, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

    {{<figure src="/images/netq/lcm-import-netq-image-dialog-320.png" width="250">}}

5. Provide the *.deb* file(s) from an external drive that matches the criteria for the selected image, either by dragging and dropping it onto the dialog or by selecting it from a directory.

6. Click **Import**.

    {{<figure src="/images/netq/lcm-import-netq-image-in-process-320.png" width="250">}}

<div style="padding-left: 18px;">On successful completion, you receive confirmation of the upload.</div>

    {{<figure src="/images/netq/lcm-import-netq-image-success-320.png" width="250">}}

<div style="padding-left: 18px;">If the upload was not successful, an <em>Image Import Failed</em> message is shown. Close the Import Image dialog and try uploading the file again.</div>

7. Click **Done**.

8. Click **Uploaded** to verify the images are in the repository.

    When all of the missing images have been uploaded, the Missing list will be empty.

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The NetQ Images card now shows the number of images you uploaded.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Download the Cumulus NetQ debian packages needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads page">}}, selecting the appropriate version and hypervisor/platform. Place them in an accessible part of your local network.

2. Upload the images to the LCM repository. This example uploads the two packages (`netq-agent` and `netq-apps`) needed for NetQ version 3.2.0 for a NetQ appliance or VM running Ubuntu 18.04 with an x86 architecture.

    ```
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_3.2.1-ub18.04u31~1603789872.6f62fad_amd64
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_3.2.1-ub18.04u31~1603789872.6f62fad_amd64
    ```

{{< /tab >}}

{{< /tabs >}}

### Upload Upgrade Images

To upload the Cumulus Linux or Cumulus NetQ images that you want to use for upgrade:

First download the Cumulus Linux disk images (*.bin* files) and Cumulus NetQ debian packages needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}}. Place them in an accessible part of your local network.

If you are upgrading Cumulus Linux on switches with different ASIC vendors or CPU architectures, you will need more than one image. For NetQ, you need both the `netq-apps` and `netq-agent` packages for each variant.

Then continue with the instructions here based on whether you want to use the NetQ UI or CLI.

{{< tabs "TabID190" >}}

{{< tab "NetQ UI" >}}

1. Click **Add Image** on the Cumulus Linux Images or NetQ Images card.

    {{<img src="/images/netq/lcm-linux-images-card-at-install-addimage-300.png" width="200">}} {{<img src="/images/netq/lcm-netq-images-card-at-install-addimage-310.png" width="200">}}

2. Provide one or more images from an external drive, either by dragging and dropping onto the dialog or by selecting from a directory.

    {{<figure src="/images/netq/lcm-import-linux-image-dialog-320.png" width="250">}}

    {{<figure src="/images/netq/lcm-import-netq-image-dialog-320.png" width="250">}}

3. Click **Import**.

4. Monitor the progress until it completes. Click **Done**.

5. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The NetQ Images card is updated to show the number of additional images you uploaded.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Use the `netq lcm add cl-image <text-image-path>` and `netq lcm add netq-image <text-image-path>` commands to upload the images. Run the relevant command for each image that needs to be uploaded.

Cumulus Linux images:

```
cumulus@switch:~$ netq lcm add image /path/to/download/cumulus-linux-4.2.0-mlx-amd64.bin
```

Cumulus NetQ images:
<!-- get new image names -->
```
cumulus@switch:~$ netq lcm add image /path/to/download/netq-agent_3.2.1-ub18.04u31~1603789872.6f62fad_amd64
cumulus@switch:~$ netq lcm add image /path/to/download/netq-apps_3.2.1-ub18.04u31~1603789872.6f62fad_amd64
```

{{< /tab >}}

{{< /tabs >}}

#### Specify a Default Upgrade Version

Lifecycle management does not have a default Cumulus Linux or Cumulus NetQ upgrade version specified automatically. With the NetQ UI, you can specify the version that is appropriate for your network to ease the upgrade process.

To specify a default Cumulus Linux or Cumulus NetQ version in the NetQ UI:

1. Click the *Click here to set the default CL version* link in the middle of the Cumulus Linux Images card, or click the *Click here to set the default NetQ version* link in the middle of the NetQ Images card.

    {{<img src="/images/netq/lcm-images-card-spec-default-cl-300.png" width="200">}} {{<img src="/images/netq/lcm-images-card-spec-default-netq-310.png" width="200">}}

2. Select the version you want to use as the default for switch upgrades.

3. Click **Save**. The default version is now displayed on the relevant Images card.

    {{<figure src="/images/netq/lcm-images-cards-default-assigned-320.png" width="400">}}

After you have specified a default version, you have the option to change it.

To change the default Cumulus Linux or Cumulus NetQ version:

1. Click **change** next to the currently identified default image on the Cumulus Linux Images or NetQ Images card.

2. Select the image you want to use as the default version for upgrades.

3. Click **Save**.

## Export Images

You can export a listing of the Cumulus Linux and NetQ images stored in the LCM repository for reference.

To export image listings:

{{< tabs "TabID265" >}}

{{< tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

3. Optionally, use the filter option above the table on the **Uploaded** tab to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

    {{<figure src="/images/netq/lcm-netq-images-uploaded-tab-310.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> above the table.

5. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-300.png" width="250">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Use the `json` option with the `netq lcm show images` command to output a list of the Cumulus Linux image files stored in the LCM repository.

```
cumulus@switch:~$ netq lcm show images json
[
    {
        "id": "image_cc97be3955042ca41857c4d0fe95296bcea3e372b437a535a4ad23ca300d52c3",
        "name": "cumulus-linux-4.2.0-vx-amd64-1594775435.dirtyzc24426ca.bin",
        "clVersion": "4.2.0",
        "cpu": "x86_64",
        "asic": "VX",
        "lastChanged": 1600726385400.0
    },
    {
        "id": "image_c6e812f0081fb03b9b8625a3c0af14eb82c35d79997db4627c54c76c973ce1ce",
        "name": "cumulus-linux-4.1.0-vx-amd64.bin",
        "clVersion": "4.1.0",
        "cpu": "x86_64",
        "asic": "VX",
        "lastChanged": 1600717860685.0
    }
]
```

{{< /tab >}}

{{< /tabs >}}

## Remove Images from Local Repository

Once you have upgraded all of your switches beyond a particular release of Cumulus Linux or NetQ, you may want to remove those images from the LCM repository to save space on the server.

To remove images:

{{< tabs "TabID306" >}}

{{< tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

3. On **Uploaded**, select the images you want to remove. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

    {{<figure src="/images/netq/lcm-netq-images-uploaded-tab-310.png" width="700">}}

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To remove Cumulus Linux images, run:

```
netq lcm show images [json]
netq lcm del image <text-image-id>
```

1. Determine the ID of the image you want to remove.

    ```
    cumulus@switch:~$ netq lcm show images
    [
        {
            "id": "image_cc97be3955042ca41857c4d0fe95296bcea3e372b437a535a4ad23ca300d52c3",
            "name": "cumulus-linux-4.2.0-vx-amd64-1594775435.dirtyzc24426ca.bin",
            "clVersion": "4.2.0",
            "cpu": "x86_64",
            "asic": "VX",
            "lastChanged": 1600726385400.0
        },
        {
            "id": "image_c6e812f0081fb03b9b8625a3c0af14eb82c35d79997db4627c54c76c973ce1ce",
            "name": "cumulus-linux-4.1.0-vx-amd64.bin",
            "clVersion": "4.1.0",
            "cpu": "x86_64",
            "asic": "VX",
            "lastChanged": 1600717860685.0
        }
    ]
    ```

2. Remove the image you no longer need.

    ```
    cumulus@switch:~$ netq lcm del image image_c6e812f0081fb03b9b8625a3c0af14eb82c35d79997db4627c54c76c973ce1ce
    ```

3. Verify it has been removed.

    ```
    cumulus@switch:~$ netq lcm show images
    [
        {
            "id": "image_cc97be3955042ca41857c4d0fe95296bcea3e372b437a535a4ad23ca300d52c3",
            "name": "cumulus-linux-4.2.0-vx-amd64-1594775435.dirtyzc24426ca.bin",
            "clVersion": "4.2.0",
            "cpu": "x86_64",
            "asic": "VX",
            "lastChanged": 1600726385400.0
        }
    ]
    ```

{{< /tab >}}

{{< /tabs >}}
