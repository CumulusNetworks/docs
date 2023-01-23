---
title: NVOS Images
author: NVIDIA
weight: 1152
toc: 4
---

NVOS images are managed with lifecycle management in the NetQ UI. This section details how to check for missing images, upload images, and specify default images.

To complete the tasks outlined in this section, expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu. Under **Admin**, select **Manage switches**:

{{<figure src="/images/netq/lcm-nvos-450.png" alt="" width="300">}}

From the dashboard, select the **Image management** tab to display the NetQ and network OS images, including NVOS:

 {{<figure src="/images/netq/lcm-image-management-nvos.png" alt="images card with link to view missing images" width="800">}}

## View and Upload Missing Images

You should upload images for each NVOS version currently installed in your inventory so you can support rolling back to a known good version should an installation or upgrade fail. If you have specified a default NVOS version, NetQ verifies that the necessary versions of the default image are available based on the known device inventory, and if not, lists those that are missing.

To upload missing **NVOS** images:

{{<tabs "Upload Missing Network OS Images" >}}

{{<tab "NetQ UI" >}}

1. On the NVOS Images card, select *View # missing NVOS images* to see which images you need.

    {{<figure src="/images/netq/missing-nvos-450.png" alt="nvos images card with link to view missing images" width="200">}}

<div style="padding-left: 18px;">{{<notice tip>}}
If you have already specified a default image, you must click <strong>Manage</strong> and then <strong>Missing</strong> to see the missing images.
    {{</notice>}}</div>

2. Select one or more of the missing images and make note of the version, ASIC vendor, and CPU architecture for each.

<!--

3. Download the files from TKTK

-->

3. In the UI, select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18">}} **Add image** above the table.

4. Provide the file that matches the criteria for the selected image(s).

5. Click **Import**.

<div style="padding-left: 18px;">If the upload was unsuccessful, an <em>Image Import Failed</em> message appears. Close the dialog and try uploading the file again.
</div>

6. Click **Done**.

7. (Optional) Click the **Uploaded** tab to verify the image is in the repository.

{{</tab>}}

{{</tabs>}}

## Upload Images

To upload the NVOS images that you want to use for the upgrade, first download the images (*.img* files). Place them in an accessible part of your local network.

After obtaining the images, upload them to NetQ:

{{<tabs "Upload Upgrade Images">}}

{{<tab "NetQ UI">}}

1. Select the **Add image** button on the NVOS card:

{{<figure src="/images/netq/nvos-images-card-450.png" alt="nvos images card" width="200">}}

2. Upload the images, then select **Import**.

3. Monitor the progress until it completes. Click **Done**.

{{</tab>}}

{{</tabs>}}

### Specify a Default Upgrade Version

Specifying a default upgrade version is optional, but recommended. You can assign an NVOS version as the default version to use when installing or upgrading switches. The default is typically the newest version that you intend to install or upgrade on all, or the majority, of your switches. If necessary, you can override the default selection during the installation or upgrade process if an alternate version is needed for a given set of switches.

{{<tabs "Specify default version">}}

{{<tab "NetQ UI">}}

To specify a default version:

1. On the NVOS Images card, select *Click here to set default NVOS version*:

    {{<img src="/images/netq/default-nvos-450.png" alt="card highlighting link to set default NVOS version" width="200">}}

3. Select the version you want to use as the default for switch upgrades.

4. Click **Save**. The default version is now displayed on the card.


{{</tab>}}

{{</tabs>}}

## Remove Images from Local Repository

After you upgrade all your switches beyond a particular release, you can remove images from the LCM repository to save space on the server. To remove images:

{{<tabs "Remove Local Images">}}

{{<tab "NetQ UI">}}

1. Click **Manage** on the NVOS Images card.

2. On the **Uploaded** tab, select the images you want to remove. 

3. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/23-Delete/bin-1.svg" height="18" width="18"/> Delete.

{{</tab>}}

{{</tabs>}}
