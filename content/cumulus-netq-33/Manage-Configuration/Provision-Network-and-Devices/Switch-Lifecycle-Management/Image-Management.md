---
title: Manage Cumulus Linux and NetQ Images
author: NVIDIA
weight: 630
toc: 4
---
You can manage both Cumulus Linux and NetQ images with LCM. They are managed in a similar manner.

Cumulus Linux binary images can be uploaded to a local LCM repository for upgrade of your switches. NetQ debian packages can be uploaded to the local LCM repository for installation or upgrade. You can upload images from an external drive.

The Linux and NetQ images are available in several variants based on the software version (x.y.z), the CPU architecture (ARM, x86), platform (based on ASIC vendor, Broadcom or NVIDIA), SHA Checksum, and so forth. When LCM discovers Cumulus Linux switches running NetQ 2.x or later in your network, it extracts the meta data needed to select the appropriate image for a given switch. Similarly, LCM discovers and extracts the meta data from NetQ images.

{{<figure src="/images/netq/lcm-image-naming-conventions-310.png" width="400">}}

The Cumulus Linux Images and NetQ Images cards in the NetQ UI provide a summary of image status in LCM. They show the total number of images in the repository, a count of missing images, and the starting points for adding and managing your images.

The `netq lcm show cl-images` and `netq lcm show netq-images` commands also display a summary of the Cumulus Linux or NetQ images, respectively, uploaded to the LCM repo on the NetQ appliance or VM.

## Default Cumulus Linux or NetQ Version Assignment

You can assign a specific Cumulus Linux or NetQ version as the default version to use during installation or upgrade of switches. It is recommended that you choose the newest version that you intend to install or upgrade on all, or the majority, of your switches. The default selection can be overridden during individual installation and upgrade job creation if an alternate version is needed for a given set of switches.

## Missing Images

You should upload images for each variant of Cumulus Linux and NetQ currently installed on the switches in your inventory if you want to support rolling back to a known good version should an installation or upgrade fail. The NetQ UI prompts you to upload any missing images to the repository.

For example, if you have both Cumulus Linux 3.7.3 and 3.7.11 versions, some running on ARM and some on x86 architectures, then LCM verifies the presence of each of these images. If only the 3.7.3 x86, 3.7.3 ARM, and 3.7.11 x86 images are in the repository, the NetQ UI would list the 3.7.11 ARM image as missing. For NetQ, you need both the `netq-apps` and `netq-agent` packages for each release variant.

If you have specified a default Cumulus Linux and/or NetQ version, the NetQ UI also verifies that the necessary versions of the default image are available based on the known switch inventory, and if not, lists those that are missing.

While it is not required that you upload images that NetQ determines to be missing, not doing so may cause failures when you attempt to upgrade your switches.

## Upload Images

For fresh installations of NetQ {{%version%}}, no images have yet been uploaded to the LCM repository. If you are upgrading from NetQ 3.0.x-3.2.x, the Cumulus Linux images you have previously added are still present.

In preparation for *Cumulus Linux* upgrades, the recommended image upload flow is:

1. In a fresh NetQ install, add images that match your current inventory: {{<link url="#upload-missing-images" text="Upload Missing Images">}}

2. Add images you want to use for upgrade: {{<link url="#upload-upgrade-images" text="Upload Upgrade Images">}}

3. In NetQ UI, optionally specify a default version for upgrades: {{<link url="#specify-a-default-upgrade-image" text="Specify a Default Upgrade Image">}}

In preparation for *NetQ* installation or upgrade, the recommended image upload flow is:

1. Add images you want to use for installation or upgrade: {{<link url="#upload-missing-images" text="Upload Upgrade Images">}}

2. Add any missing images: {{<link url="#upload-upgrade-images" text="Upload Missing Images">}}

3. In NetQ UI, optionally specify a default version for installation or upgrade: {{<link url="#specify-a-default-upgrade-image" text="Specify a Default Upgrade Image">}}

### Upload Missing Images

Use the following instructions to upload missing Cumulus Linux and NetQ images.

For *Cumulus Linux* images:

{{< tabs "TabID61" >}}

{{< tab "NetQ UI" >}}

1. On the Manage Switch Assets page, click **Image Management**.

    {{<figure src="/images/netq/lcm-image-mgmt-tab-330.png" width="600">}}

2. On the Cumulus Linux Images card, click the *View # missing CL images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-linux-images-card-at-install-missinglink-300.png" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

3. Select one or more of the missing images and make note of the version, ASIC Vendor, and CPU architecture for each.

    {{<figure src="/images/netq/lcm-images-missing-list-320.png" width="700">}}

<div style="padding-left: 18px;">Note the Disk Space Utilized information in the header to verify that you have enough space to upload the Cumulus Linux images.
</div>
   {{<figure src="/images/netq/lcm-disk-space-aid-320.png" width="150">}}

4. Download the Cumulus Linux disk images (*.bin* files) needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}} page, selecting the appropriate version, CPU, and ASIC. Place them in an accessible part of your local network.

5. Back in the UI, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

  {{<figure src="/images/netq/lcm-import-linux-image-dialog-320.png" width="250">}}

6. Provide the *.bin* file from an external drive that matches the criteria for the selected image(s), either by dragging and dropping onto the dialog or by selecting from a directory.

7. Click **Import**.

    {{<figure src="/images/netq/lcm-import-linux-image-in-process-320.png" width="250">}}

<div style="padding-left: 18px;">On successful completion, you receive confirmation of the upload and the Disk Space Utilization is updated.</div>

    {{<figure src="/images/netq/lcm-import-linux-image-success-320.png" width="250">}}

<div style="padding-left: 18px;">If the upload was not successful, an <em>Image Import Failed</em> message is shown. Close the Import Image dialog and try uploading the file again.
</div>

8. Click **Done**.

9. Click **Uploaded** to verify the image is in the repository.

    {{<figure src="/images/netq/lcm-import-linux-image-uploaded-320.png" width="700">}}

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The Cumulus Linux Images card now shows the number of images you uploaded.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Download the Cumulus Linux disk images (*.bin* files) needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}} page, selecting the appropriate version, CPU, and ASIC. Place them in an accessible part of your local network.

2. Upload the images to the LCM repository. This example uses a Cumulus Linux 4.2.0 disk image.

    ```
    cumulus@switch:~$ netq lcm add cl-image /path/to/download/cumulus-linux-4.2.0-mlnx-amd64.bin
    ```

3. Repeat Step 2 for each image you need to upload to the LCM repository.

{{< /tab >}}

{{< /tabs >}}

For *NetQ* images:

{{< tabs "TabID122">}}

{{< tab "NetQ UI" >}}

1. Click **Image Management**.

2. On the NetQ Images card, click the *View # missing NetQ images* link to see what images you need. This opens the list of missing images.

    {{<figure src="/images/netq/lcm-netq-images-missinglink-310.png" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

3. Select one or all of the missing images and make note of the OS version, CPU architecture, and image type. Remember that you need both `netq-apps` and `neta-agent` for NetQ to perform the installation or upgrade.

    {{<figure src="/images/netq/lcm-netq-images-missing-list-310.png" width="700">}}

4. Download the NetQ debian packages needed for upgrade from the {{<exlink url="http://apps3.cumulusnetworks.com/repos/deb/pool/netq-3.3/p/python-netq/" text="NetQ repository">}}, selecting the appropriate OS version and architecture. Place the files in an accessible part of your local network.

    {{<figure src="/images/netq/lcm-import-netq-image-repo-330.png" width="400">}}

5. Back in the UI, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} (Add Image) above the table.

    {{<figure src="/images/netq/lcm-import-netq-image-dialog-320.png" width="250">}}

6. Provide the *.deb* file(s) from an external drive that matches the criteria for the selected image, either by dragging and dropping it onto the dialog or by selecting it from a directory.

7. Click **Import**.

    {{<figure src="/images/netq/lcm-import-netq-image-in-process-320.png" width="250">}}

<div style="padding-left: 18px;">On successful completion, you receive confirmation of the upload.</div>

    {{<figure src="/images/netq/lcm-import-netq-image-success-320.png" width="250">}}

<div style="padding-left: 18px;">If the upload was not successful, an <em>Image Import Failed</em> message is shown. Close the Import Image dialog and try uploading the file again.</div>

8. Click **Done**.

9. Click **Uploaded** to verify the images are in the repository.

    When all of the missing images have been uploaded, the Missing list will be empty.

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The NetQ Images card now shows the number of images you uploaded.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

1. Download the NetQ debian packages needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads page">}}, selecting the appropriate version and hypervisor/platform. Place them in an accessible part of your local network.

2. Upload the images to the LCM repository. This example uploads the two packages (`netq-agent` and `netq-apps`) needed for NetQ version 3.3.1 for a NetQ appliance or VM running Ubuntu 18.04 with an x86 architecture.

    ```
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_3.3.1-ub18.04u33~1614767175.886b337_amd64.deb
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_3.3.1-ub18.04u33~1614767175.886b337_amd64.deb
    ```

{{< /tab >}}

{{< /tabs >}}

### Upload Upgrade Images

To upload the Cumulus Linux or NetQ images that you want to use for upgrade:

First download the Cumulus Linux disk images (*.bin* files) and NetQ debian packages needed for upgrade from the {{<exlink url="https://support.mellanox.com/s/" text="MyMellanox downloads">}} and {{<exlink url="http://apps3.cumulusnetworks.com/repos/deb/pool/netq-3.3/p/python-netq/" text="NetQ repository">}}, respectively. Place them in an accessible part of your local network.

If you are upgrading Cumulus Linux on switches with different ASIC vendors or CPU architectures, you will need more than one image. For NetQ, you need both the `netq-apps` and `netq-agent` packages for each variant.

Then continue with the instructions here based on whether you want to use the NetQ UI or CLI.

{{< tabs "TabID190" >}}

{{< tab "NetQ UI" >}}

1. Click **Image Management**.

2. Click **Add Image** on the Cumulus Linux Images or NetQ Images card.

    {{<img src="/images/netq/lcm-linux-images-card-at-install-addimage-300.png" width="200">}} {{<img src="/images/netq/lcm-netq-images-card-at-install-addimage-310.png" width="200">}}

3. Provide one or more images from an external drive, either by dragging and dropping onto the dialog or by selecting from a directory.

    {{<figure src="/images/netq/lcm-import-linux-image-dialog-320.png" width="250">}}

    {{<figure src="/images/netq/lcm-import-netq-image-dialog-320.png" width="250">}}

4. Click **Import**.

5. Monitor the progress until it completes. Click **Done**.

6. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} to return to the LCM dashboard.

    The NetQ Images card is updated to show the number of additional images you uploaded.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Use the `netq lcm add cl-image <text-image-path>` and `netq lcm add netq-image <text-image-path>` commands to upload the images. Run the relevant command for each image that needs to be uploaded.

Cumulus Linux images:

```
cumulus@switch:~$ netq lcm add image /path/to/download/cumulus-linux-4.2.0-mlx-amd64.bin
```

NetQ images:

```
cumulus@switch:~$ netq lcm add image /path/to/download/	netq-agent_3.3.1-ub18.04u33~1614767175.886b337_amd64.deb
cumulus@switch:~$ netq lcm add image /path/to/download/netq-apps_3.3.1-ub18.04u33~1614767175.886b337_amd64.deb
```

{{< /tab >}}

{{< /tabs >}}

#### Specify a Default Upgrade Version

Lifecycle management does not have a default Cumulus Linux or NetQ upgrade version specified automatically. With the NetQ UI, you can specify the version that is appropriate for your network to ease the upgrade process.

To specify a default Cumulus Linux or NetQ version in the NetQ UI:

{{< tabs "Specify default version" >}}

{{< tab "NetQ UI" >}}

1. Click **Image Management**.

2. Click the *Click here to set the default CL version* link in the middle of the Cumulus Linux Images card, or click the *Click here to set the default NetQ version* link in the middle of the NetQ Images card.

    {{<img src="/images/netq/lcm-images-card-spec-default-cl-300.png" width="200">}} {{<img src="/images/netq/lcm-images-card-spec-default-netq-310.png" width="200">}}

3. Select the version you want to use as the default for switch upgrades.

4. Click **Save**. The default version is now displayed on the relevant Images card.

    {{<figure src="/images/netq/lcm-images-cards-default-assigned-330.png" width="400">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To specify a default Cumulus Linux version, run:

```
cumulus@switch:~$ netq lcm add default-version cl-images <text-cumulus-linux-version>
```

To specify a default NetQ version, run:

```
cumulus@switch:~$ netq lcm add default-version netq-images <text-netq-version>
```

{{< /tab >}}

{{< /tabs >}}

After you have specified a default version, you have the option to change it.

To change the default Cumulus Linux or NetQ version:

{{< tabs "Change default version" >}}

{{< tab "NetQ UI" >}}

1. Click **change** next to the currently identified default image on the Cumulus Linux Images or NetQ Images card.

2. Select the image you want to use as the default version for upgrades.

3. Click **Save**.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To change the default Cumulus Linux version, run:

```
cumulus@switch:~$ netq lcm add default-version cl-images <text-cumulus-linux-version>
```

To change the default NetQ version, run:

```
cumulus@switch:~$ netq lcm add default-version netq-images <text-netq-version>
```

{{< /tab >}}

{{< /tabs >}}

In the CLI, you can check which version of Cumulus Linux or NetQ has been configured as the default.

To see which version of Cumulus Linux has been configured as the default, run `netq lcm show default-version cl-images`:

```
cumulus@switch:~$ netq lcm show default-version cl-images 
ID                        Name            CL Version  CPU      ASIC            Last Changed
------------------------- --------------- ----------- -------- --------------- -------------------------
image_cc97be3955042ca4185 cumulus-linux-4 4.2.0       x86_64   VX              Tue Jan  5 22:10:59 2021
7c4d0fe95296bcea3e372b437 .2.0-vx-amd64-1
a535a4ad23ca300d52c3      594775435.dirty
                          zc24426ca.bin
```

To see which version of NetQ has been configured as the default, run `netq lcm show default-version netq-images`:

```
cumulus@switch:~$ netq lcm show default-version netq-images 
ID                        Name            NetQ Version  CL Version  CPU      Image Type           Last Changed
------------------------- --------------- ------------- ----------- -------- -------------------- -------------------------
image_d23a9e006641c675ed9 netq-agent_3.3. 3.3.0         cl4u32      x86_64   NETQ_AGENT           Tue Jan  5 22:23:50 2021
e152948a9d1589404e8b83958 0-cl4u32_160939
d53eb0ce7698512e7001      1187.7df4e1d2_a
                          md64.deb
image_68db386683c796d8642 netq-apps_3.3.0 3.3.0         cl4u32      x86_64   NETQ_CLI             Tue Jan  5 22:23:54 2021
2f2172c103494fef7a820d003 -cl4u32_1609391
de71647315c5d774f834      187.7df4e1d2_am
                          d64.deb
```

## Export Images

You can export a listing of the Cumulus Linux and NetQ images stored in the LCM repository for reference.

To export image listings:

{{< tabs "TabID265" >}}

{{< tab "NetQ UI" >}}

1. Open the LCM dashboard.

2. Click **Image Management**.

3. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

4. Optionally, use the filter option above the table on the **Uploaded** tab to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

    {{<figure src="/images/netq/lcm-netq-images-uploaded-tab-310.png" width="700">}}

5. Click <img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/08-Upload-Download/upload-bottom.svg" height="18" width="18"/> above the table.

6. Choose the export file type and click **Export**.

    {{<figure src="/images/netq/export-data-dialog-300.png" width="250">}}

{{< /tab >}}

{{< tab "NetQ CLI" >}}

Use the `json` option with the `netq lcm show cl-images` command to output a list of the Cumulus Linux image files stored in the LCM repository.

```
cumulus@switch:~$ netq lcm show cl-images json
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

2. Click **Image Management**.

3. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

4. On **Uploaded**, select the images you want to remove. Use the filter option above the table to narrow down a large listing of images.

    {{<figure src="/images/netq/lcm-images-uploaded-tab-300.png" width="700">}}

    {{<figure src="/images/netq/lcm-netq-images-uploaded-tab-310.png" width="700">}}

5. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/>.

{{< /tab >}}

{{< tab "NetQ CLI" >}}

To remove Cumulus Linux images, run:

```
netq lcm show cl-images [json]
netq lcm del cl-image <text-image-id>
```

1. Determine the ID of the image you want to remove.

    ```
    cumulus@switch:~$ netq lcm show cl-images json
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
    cumulus@switch:~$ netq lcm del cl-image image_c6e812f0081fb03b9b8625a3c0af14eb82c35d79997db4627c54c76c973ce1ce
    ```

3. Verify it has been removed.

    ```
    cumulus@switch:~$ netq lcm show cl-images json
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

To remove NetQ images, run:

```
netq lcm show netq-images [json]
netq lcm del netq-image <text-image-id>
```

1. Determine the ID of the image you want to remove.

    ```
    cumulus@switch:~$ netq lcm show netq-images json
    [
        {
            "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
            "name": "netq-agent_3.3.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
            "netqVersion": "3.3.0",
            "clVersion": "cl4u32",
            "cpu": "x86_64",
            "imageType": "NETQ_AGENT",
            "lastChanged": 1609885430638.0
        }, 
        {
            "id": "image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834",
            "name": "netq-apps_3.3.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
            "netqVersion": "3.3.0",
            "clVersion": "cl4u32",
            "cpu": "x86_64",
            "imageType": "NETQ_CLI",
            "lastChanged": 1609885434704.0
        }
    ]
    ```

2. Remove the image you no longer need.

    ```
    cumulus@switch:~$ netq lcm del netq-image image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834
    ```

3. Verify it has been removed.

    ```
    cumulus@switch:~$ netq lcm show netq-images json
    [
        {
            "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
            "name": "netq-agent_3.3.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
            "netqVersion": "3.3.0",
            "clVersion": "cl4u32",
            "cpu": "x86_64",
            "imageType": "NETQ_AGENT",
            "lastChanged": 1609885430638.0
        }
    ]
    ```

{{< /tab >}}

{{< /tabs >}}
