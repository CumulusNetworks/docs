---
title: Upgrade NVOS with LCM
author: NVIDIA
weight: 1153
toc: 4
---

Lifecycle management (LCM) lets you upgrade NVLink4 switches and GPU nodes to the latest NVOS version. You can run up to five upgrades concurrently.

## Prepare for an NVOS Upgrade

Before you upgrade, make sure you have {{<link title="NVOS Images/#upload-upgrade-images" text="uploaded the NVOS images to NetQ">}}.

## Perform an NVOS Upgrade

{{<tabs "TabID61" >}}

{{<tab "NetQ UI" >}}

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in any workbench header, then select **Manage switches**.

2. From the Switches card, select **Manage**:

{{<img src="/images/netq/manage-switches-nvos.png" alt="" width="650">}}

3. Select the device(s) to include in the upgrade, then click {{<img src="/images/netq/arrow-up-circle-icon.png" height="18" width="18">}} **Upgrade NVOS** above the table and follow the steps in the UI: give the upgrade a name, select the NVOS version, then choose whether to restart the devices after they've been upgraded. If you choose not to restart the devices after the upgrade, the upgrade will remain in a pending state until the devices are restarted.

4. NetQ directs you to a screen where you can monitor the upgrade and view past upgrades:

    {{<figure src="/images/netq/upgrade-progress-nvos.png" alt="" width="1500">}}

{{</tab>}}

{{</tabs>}}

## View Previous NVOS Upgrades

To view the full history of NVOS upgrades:

{{<tabs "TabID38" >}}

{{<tab "NetQ UI" >}}

1. Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18"/> Menu. Under **Admin**, select **Manage switches**.

2. Select the **Job history** tab:

{{<figure src="/images/netq/nvos-upgrade-history-450.png" alt="" width="450">}}

3. On the NVOS upgrade history card, select **View**. From here, you can sort and filter upgrades using the controls at the top of the screen.

To view information at the most granular level, expand an individual upgrade job and select the arrow:

{{<figure src="/images/netq/kong-additional-details-450.png" alt="" width="1500">}}

Select **Details** on any device to display a timestamped history of the upgrade:

{{<figure src="/images/netq/kong-details-450.png" alt="" width="1500">}}

{{</tab>}}

{{</tabs>}}
