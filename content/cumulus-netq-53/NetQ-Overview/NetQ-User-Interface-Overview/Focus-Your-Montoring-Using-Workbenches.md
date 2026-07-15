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

## Get Started with Workbenches

NVIDIA includes two example workbenches---NetQ Workbench and Fabric Dashboard---to help get you started with NetQ. To access these workbenches or switch between them, select the workbench's name in the header. The menu displays recently accessed workbenches and the date at which they were created. 

{{<figure src="/images/netq/fabric-wb-local-412.png" alt="list of available workbenches" width="300">}}

**NetQ Workbench** includes cards displaying your network’s device inventory, switch inventory, validation summary, What Just Happened events, host inventory, DPU inventory, and system events. This workbench is visible to all users within an organization and any changes to it will not be saved.

**Fabric Dashboard** includes cards displaying link status and events, sensor health, queue lengths, What Just Happened and system events, BGP and EVPN sessions, and device inventory. You can modify this workbench by adding or deleting cards and NetQ saves the changes automatically. This workbench is local to each premises, meaning that changes made to the workbench on one premises will not be reflected when you switch to a different premises.


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


## Manage Workbenches

The changes you make to a custom workbench are saved automatically. To change a workbench from local to global (or global to local) availability, select the workbench's name in the header and select **Manage my WB**. From the Workbenches card, locate the workbench whose availability you'd like to change and select **Local** or **Global**.

You can also change your home workbench (the workbench that loads when you log in to NetQ) from this view. Select the {{<img src="/images/netq/home-workbench.png" width="18px">}} house to the left of the workbench that you want to set as your home workbench. The next time you log in from this premises, the workbench you selected will be displayed.
{{<figure src="/images/netq/wb-card-414.png" alt="" width="600">}}

## Delete a Workbench

You can only delete workbenches that you created. The NVIDIA-supplied NetQ Workbench and Fabric Dashboard workbenches cannot be deleted. When you delete a workbench that you have designated as your home workbench, NetQ Workbench will replace it as the home workbench. To delete a workbench:

1. Select <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" alt="" height="18" width="18"/> **User Settings** &nbsp;<span aria-label="and then">> **Profile & Preferences**.

3. Locate the Workbenches card.

4. Hover over the name of the workbench you want to remove, and click **Delete**.

## Manage Auto-refresh

You can specify how often to update the data displayed on a workbench. By default, NetQ updates the data every five minutes. To alternately disable or re-enable auto-refresh, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" alt="pause icon" width="18"/> **Pause** or <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-play-1.svg" alt="play icon" width="18"/> **Play**. Each workbench refreshes according to its respective refresh interval. 

To modify the refresh rate:

1. In the header, select the dropdown next to **Refresh**.

2. Select the refresh rate. A check mark indicates the current selection. The new refresh rate is applied immediately. 

    {{<figure src="/images/netq/refresh-411.png" alt="refresh rate dropdown listng rate options of 1 minute, 2 minutes, and 5 minutes" width="150">}}

To disable auto-refresh on individual cards, select the card's three-dot menu and click **Manual refresh**. The option to disable auto-refresh is not available on all cards.

## Related Information

- {{<link title="Configure Premises" text="Configure Premises">}}
- {{<link title="Access Data with Cards" text="Access Data with Cards">}}