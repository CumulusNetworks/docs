---
title: Focus Your Monitoring Using Workbenches
author: NVIDIA
weight: 130
toc: 4
---
Workbenches are dashboards where you can visualize and curate data representing different aspects of your network. For example, you might create a workbench that:

- Shows network statistics for the past week alongside network statistics for the past 24 hours.
- Only displays data about virtual overlays.
- Displays switches that you are troubleshooting.
- Is focused on application or account management.

NVIDIA provides an example workbench that opens when you first log in to NetQ, called NetQ Workbench. It includes cards displaying your network's device inventory, switch inventory, validation summary, What Just Happened events, host inventory, DPU inventory, and system events. This workbench is visible to all users within an organization and any changes to it will not be saved.

{{<figure src="/images/netq/default-wb-411.png" alt="default netq workbench" width="1000">}}

## Create a Custom Workbench

You can create an unlimited number of custom workbenches. These workbenches are only visible to the user who created them and changes are saved automatically. 

To create a new workbench:

1. Select **Workbench** in the header, then select **New**.

2. Enter a name for the workbench and choose whether to restrict access to this workbench to a single premises (local) or make it available across all premises (global). You can modify this setting later if you change your mind.

3. (Optional) Set the workbench as your home workbench, which opens when you log in to NetQ from the premises where the workbench was created.

4. Select the cards you want to display on your new workbench, then click **Create**.

5. (Optional) To add cards that display data for individual switches, select **Add card** in the header, then **Device card**. Select a device and card size. Repeat these steps for each device you'd like to add to the workbench.

{{<notice tip>}}
You can clone a workbench to quickly create a new workbench with the same cards as the one you're viewing. In the header, select <b>Clone</b>, modify the workbench settings, then click <b>Clone</b>.
{{</notice>}}

## Switch Between Workbenches

To access a different workbench, select the current workbench in the header. The menu displays recently accessed workbenches. Click **All my WB** to open a list of all workbenches.
{{<figure src="/images/netq/wb-dropdown-411.png" alt="list of available workbenches" width="300">}}

## Manage Workbenches

The changes you make to a custom workbench are saved automatically. To change a workbench from local to global (or global to local) availability, select the workbench's name in the header and select **Manage my WB**. From the Workbenches card, locate the workbench whose availability you'd like to change and select **Local** or **Global**.

You can also change your home workbench (the workbench that loads when you log in to NetQ) from this view. Select the {{<img src="/images/netq/home-workbench.png" width="18px">}} icon to the left of the workbench that you want to set as your home workbench. The next time you log in from this premises, the workbench you selected will be displayed.
{{<figure src="/images/netq/wb-card-411.png" alt="" width="600">}}

## Delete a Workbench

You can only delete workbenches that you created. The NVIDIA-supplied NetQ Workbench cannot be deleted. When you delete a workbench that you have designated as your home workbench, the NetQ Workbench will replace it as the home workbench. To delete a workbench:

1. Select the **User Settings** dropdown menu in the top-right corner.

2. Select **Profile & Preferences**.

3. Locate the Workbenches card.

4. Hover over the name of the workbench you want to remove, and click **Delete**.

## Manage Auto-refresh

You can specify how often to update the data displayed on your workbenches. By default, NetQ updates the data every five minutes. To alternately disable and re-enable auto-refresh, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" alt="pause icon" width="18"/> **Pause** or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-play-1.svg" alt="play icon" width="18"/> **Play**. To modify the refresh rate:

1. In the header, select the dropdown next to **Refresh**.

2. Select the refresh rate. A check mark indicates the current selection. The new refresh rate is applied immediately. 

    {{<figure src="/images/netq/refresh-411.png" alt="refresh rate dropdown listng rate options of 1 minute, 2 minutes, and 5 minutes" width="150">}}

## Related Information

- {{<link title="Configure Premises" text="Configure Premises">}}
- {{<link title="Access Data with Cards" text="Access Data with Cards">}}