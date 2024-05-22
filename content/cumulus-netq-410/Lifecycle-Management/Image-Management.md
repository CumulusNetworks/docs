---
title: NetQ and Network OS Images
author: NVIDIA
weight: 640
toc: 4
---

NetQ and network operating system images (Cumulus Linux and SONiC) are managed with LCM. This section explains how to check for missing images, upgrade images, and specify default images.
## View and Upload Missing Images

You should upload images for each network OS and NetQ version currently installed in your inventory so you can support rolling back to a known good version should an installation or upgrade fail. If you have specified a default network OS and/or NetQ version, the NetQ UI also verifies that the necessary versions of the default image are available based on the known switch inventory, and if not, lists those that are missing.

To upload missing network OS images:

{{<tabs "Upload Missing Network OS Images" >}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**. Select the **Image management** tab.

2. On the Cumulus Linux Images card, select *View # missing CL images* to see which images you need.

    {{<figure src="/images/netq/view-missing-cl-image.png" alt="cumulus linux images card with link to view missing images" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

3. Select one or more of the missing images and take note of the version, ASIC vendor, and CPU architecture for each.

4. Download the network OS disk images (*.bin* files) from the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Enterprise Support Portal">}}. Log in to the portal and from the **Downloads** tab, select **Switches and Gateways**. Under **Switch Software**, click **All downloads** next to **Cumulus Linux for Mellanox Switches**. Select the current version and the target version, then click **Show Downloads Path**. Download the file.

5. In the UI, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} **Add image** above the table.

6. Provide the *.bin* file from an external drive that matches the criteria for the selected image(s).

7. Click **Import**.

<div style="padding-left: 18px;">If the upload was unsuccessful, an <em>Image Import Failed</em> message appears. Close the dialog and try uploading the file again.
</div>

8. Click **Done**.

9. (Optional) Click the **Uploaded** tab to verify the image is in the repository.

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" alt="close" height="14" width="14">}} **Close** to return to the LCM dashboard.

    The Cumulus Linux Images card reflects the number of images you uploaded.

{{</tab>}}

{{<tab "NetQ CLI" >}}

1. (Optional) Display a summary of Cumulus Linux images uploaded to the LCM repo on the NetQ appliance or VM:

```
netq lcm show cl-images
```

2. Download the network OS disk images (*.bin* files) from the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Enterprise Support Portal">}}. Log into the portal and from the **Downloads** tab, select **Switches and Gateways**. Under **Switch Software**, click **All downloads** next to **Cumulus Linux for Mellanox Switches**. Select the current version and the target version, then click **Show Downloads Path**. Download the file.

2. Upload the images to the LCM repository. The following example uses a Cumulus Linux 4.2.0 disk image.

    ```
    cumulus@switch:~$ netq lcm add cl-image /path/to/download/cumulus-linux-4.2.0-mlnx-amd64.bin
    ```

3. Repeat step 2 for each image you need to upload to the LCM repository.

{{</tab>}}

{{</tabs>}}

To upload missing **NetQ** images:

{{<tabs "Upload Missing NetQ Images">}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> **Menu** and select **Manage switches**. Select the **Image management** tab.

2. On the NetQ Images card, select *View # missing NetQ images* to see which images you need.

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

3. Select one or all of the missing images and make note of the OS version, CPU architecture, and image type. Remember that you need both `netq-apps` and `netq-agent` for NetQ to perform the installation or upgrade.

4. Download the NetQ Debian packages needed for upgrade from the {{<exlink url="https://download.nvidia.com/cumulus/apps3.cumulusnetworks.com/repos/deb/pool/netq-4.10/p/python-netq/" text="NetQ repository">}}, selecting the appropriate OS version and architecture. Place the files in an accessible part of your local network.

5. In the UI, click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} **Add image** above the table.

6. Provide the *.deb* file(s) from an external drive that matches the criteria for the selected image.

   {{<figure src="/images/netq/import-netq-images-450.png" alt="dialog prompting the user to import the NetQ images" width="450">}}

7. Click **Import**.

<div style="padding-left: 18px;">If the upload was unsuccessful, an <em>Image Import Failed</em> message appears. Close the dialog and try uploading the file again.</div>

8. Click **Done**.

9. (Optional) Click the **Uploaded** tab to verify that the image is in the repository.

10. Click {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/33-Form-Validation/close.svg" height="14" width="14">}} **Close** to return to the LCM dashboard.

   The NetQ Images card reflects the number of images you uploaded.

{{</tab>}}

{{<tab "NetQ CLI">}}

1. (Optional) Display a summary of NetQ images uploaded to the LCM repo on the NetQ appliance or VM:

```
netq lcm show netq-images
```

2. Download the NetQ Debian packages needed for upgrade from the {{<exlink url="https://download.nvidia.com/cumulus/apps3.cumulusnetworks.com/repos/deb/pool/netq-4.10/p/python-netq/" text="NetQ repository">}}, selecting the appropriate version and hypervisor/platform. Place them in an accessible part of your local network.

3. Upload the images to the LCM repository. This example uploads the two packages (`netq-agent` and `netq-apps`) needed for NetQ version 4.4.0 for a NetQ appliance or VM running Ubuntu 18.04 with an x86 architecture.

    ```
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-agent_4.4.0-ub18.04u40~1667493385.97ef4c9_amd64.deb
    cumulus@switch:~$ netq lcm add netq-image /path/to/download/netq-apps_4.4.0-ub18.04u40~1667493385.97ef4c9_amd64.deb
    ```

{{</tab>}}

{{</tabs>}}

## Upload Upgrade Images

To upload the network OS or NetQ images that you want to use for upgrade, first download the Cumulus Linux or SONiC disk images (*.bin* files) and NetQ Debian packages from the {{<exlink url="https://enterprise-support.nvidia.com/s/" text="NVIDIA Enterprise Support Portal">}} and {{<exlink url="https://download.nvidia.com/cumulus/apps3.cumulusnetworks.com/repos/deb/pool/netq-4.10/p/python-netq/" text="NetQ repository">}}, respectively. Place them in an accessible part of your local network.

If you are upgrading the network OS on switches with different ASIC vendors or CPU architectures, you need more than one image. For NetQ, you need both the `netq-apps` and `netq-agent` packages for each variant.

After obtaining the images, upload them to NetQ with the UI or CLI:

{{<tabs "Upload Upgrade Images">}}

{{<tab "NetQ UI">}}

1. From the LCM dashboard, select the **Image management** tab.

2. Select **Add image** on the appropriate card:

    {{<img src="/images/netq/add-image-updated-450.png" alt="cumulus linux and netq image cards prompting the user to add an image" width="500">}}

3. Provide one or more images from an external drive.

4. Click **Import**.

5. Monitor the progress until it completes. Click **Done**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

Use the `netq lcm add cl-image <text-cl-image-path>` and `netq lcm add netq-image <text-image-path>` commands to upload the images. Run the relevant command for each image that needs to be uploaded.

Network OS images:

```
cumulus@switch:~$ netq lcm add image /path/to/download/cumulus-linux-4.2.0-mlx-amd64.bin
```

NetQ images:

```
cumulus@switch:~$ netq lcm add image /path/to/download/netq-agent_4.4.0-ub18.04u40~1667493385.97ef4c9_amd64.deb
cumulus@switch:~$ netq lcm add image /path/to/download/netq-apps_4.4.0-ub18.04u40~1667493385.97ef4c9_amd64.deb
```

{{</tab>}}

{{</tabs>}}

### Specify a Default Upgrade Version

Specifying a default upgrade version is optional, but recommended. You can assign a specific OS or NetQ version as the default version to use when installing or upgrading switches. The default is typically the newest version that you intend to install or upgrade on all, or the majority, of your switches. If necessary, you can override the default selection during the installation or upgrade process if an alternate version is needed for a given set of switches.

{{<tabs "Specify default version">}}

{{<tab "NetQ UI">}}

To specify a default version in the NetQ UI:

1. From the LCM dashboard, select the **Image management** tab.

2. Select *Click here to set default x version* on the relevant card.

    {{<img src="/images/netq/default-image-link-450.png" alt="card highlighting link to set default version" width="500">}} 

3. Select the version you want to use as the default for switch upgrades.

4. Click **Save**. The default version is now displayed on the relevant Images card.


{{</tab>}}

{{<tab "NetQ CLI">}}

To specify a default network OS version, run:

```
cumulus@switch:~$ netq lcm add default-version cl-images <text-cumulus-linux-version>
```
To verify the default network OS version, run:

```
cumulus@switch:~$ netq lcm show default-version cl-images
```

To specify a default NetQ version, run:

```
cumulus@switch:~$ netq lcm add default-version netq-images <text-netq-version>
```
To verify the default NetQ version, run:

```
cumulus@switch:~$ netq lcm show default-version netq-images
```

{{</tab>}}

{{</tabs>}}

## Remove Images from Local Repository

After you upgrade all your switches beyond a particular release, you can remove images from the LCM repository to save space on the server. To remove images:

{{<tabs "Remove Local Images">}}

{{<tab "NetQ UI">}}

1. From the LCM dashboard, select the **Image management** tab.

2. Click **Manage** on the Cumulus Linux Images or NetQ Images card.

3. On the **Uploaded** tab, select the images you want to remove. 

4. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/> **Delete**. 

{{</tab>}}

{{<tab "NetQ CLI">}}

To remove Cumulus Linux images, run:


    netq lcm show cl-images [json]
    netq lcm del cl-image <text-cl-image-id>


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

3. Verify the command removed the image.

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
netq lcm del netq-image <text-netq-image-id>
```

1. Determine the ID of the image you want to remove.

    ```
    cumulus@switch:~$ netq lcm show netq-images json
    [
        {
            "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
            "name": "netq-agent_4.0.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
            "netqVersion": "4.0.0",
            "clVersion": "cl4u32",
            "cpu": "x86_64",
            "imageType": "NETQ_AGENT",
            "lastChanged": 1609885430638.0
        }, 
        {
            "id": "image_68db386683c796d86422f2172c103494fef7a820d003de71647315c5d774f834",
            "name": "netq-apps_4.0.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
            "netqVersion": "4.0.0",
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

3. Verify the command removed the image.

    ```
    cumulus@switch:~$ netq lcm show netq-images json
    [
        {
            "id": "image_d23a9e006641c675ed9e152948a9d1589404e8b83958d53eb0ce7698512e7001",
            "name": "netq-agent_4.0.0-cl4u32_1609391187.7df4e1d2_amd64.deb",
            "netqVersion": "4.0.0",
            "clVersion": "cl4u32",
            "cpu": "x86_64",
            "imageType": "NETQ_AGENT",
            "lastChanged": 1609885430638.0
        }
    ]
    ```

{{</tab>}}

{{</tabs>}}
