---
title: Focus Your Monitoring Using Workbenches
author: NVIDIA
weight: 130
toc: 4
---
Workbenches are dashboards where you can visualize and curate different aspects of your network {{<link text="with cards" url="Access-Data-with-Cards">}}. For example, you might create a workbench that:

- Shows network statistics for the past week alongside network statistics for the past 24 hours.
- Only displays data about virtual overlays.
- Displays switches that you are troubleshooting.
- Is focused on application or account management.

NVIDIA provides an example workbench that opens when you first log in to NetQ, called NetQ Workbench. It includes cards displaying your network's device inventory, switch inventory, validation summary, What Just Happened events, host inventory, DPU inventory, and system events. This workbench is visible to all users wtihin an organization and any changes to it will not be saved.

{{<figure src="/images/netq/default-wb-460.png" alt="default netq workbench" width="900">}}

## Create a Custom Workbench

You can create an unlimited number of custom workbenches. These workbenches are only visible to the user who created them and changes are saved automatically. To create a new workbench:

1. Select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" alt="add icon" height="18" width="18"/> **New** in the workbench header and give the workbench a name.

2. Choose whether to restrict access to this workbench to a single premises (local) or make it available across all premises (global). You can modify this setting later if you change your mind.

{{<notice tip>}}
Refer to the {{<link title="Configure Premises" text="premises management chapter">}} for more information about setting up and managing data between multiple premises.
{{</notice>}}

3. (Optional) Set the workbench as your home workbench, which is displayed when you log in to NetQ.

4. Select the cards you would like displayed on your new workbench.

      {{<figure src="/images/netq/create-a-workbench.png" alt="interface displaying the cards a user can select to add to their workbench" width="800">}}

4. Click **Create**.

{{<notice tip>}}
You can clone a workbench to quickly create a workbench with the same cards as the one you're viewing. In the header, select <b>Clone</b>, modify the workbench settings, then click <b>Clone</b>.
{{</notice>}}

## Switch Between Workbenches

There are several ways to access workbenches:

- In the header, select <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to the current workbench to open a menu listing recently accessed workbenches. Click **All my WB** to open a list of all workbenches.
{{<figure src="/images/netq/expanded-wb-470.png" alt="list of available workbenches" width="250">}}
- Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18"/> **Menu** and select the workbench from the **Favorites** or **Workbenches** sections.
- Select the NVIDIA logo to open your home workbench.

## Edit a Workbench

The changes you make to a workbench are saved automatically. To change a workbench from local to global (or global to local) availability, select <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to the current workbench and select **Manage my WB**. Locate the workbench whose availability you'd like to edit and select **Local** or **Global**.

## Delete a Workbench

You can only delete workbenches that you created. The default NetQ Workbench cannot be deleted. To delete a workbench:

1. Select <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" alt="profile icon" height="18" width="18"/> **User Settings** in the top-right corner.

2. Select **Profile & Preferences**.

3. Locate the Workbenches card.

4. Hover over the workbench you want to remove, and click **Delete**.

## Manage Auto-refresh

You can specify how often to update the data displayed on your workbenches. Three refresh rates are available:

- **Analyze**: updates every 30 seconds
- **Debug**: updates every minute
- **Monitor**: updates every 2 minutes

To modify the auto-refresh setting:

1. In the header, select the dropdown <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to **Refresh**.

2. Select the refresh rate. A check mark indicates the current selection. The new refresh rate is applied immediately. 

    {{<figure src="/images/netq/refresh-rate-470.png" alt="refresh rate dropdown listng rate options of 30 seconds, 1 minute, and 2 minutes" width="250">}}

To disable auto-refresh, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" alt="pause icon" width="18"/> **Pause**. When you're ready for the data to refresh, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-play-1.svg" alt="play icon" width="18"/> **Play**.

## Related Information

- {{<link title="Configure Premises" text="Configure Premises">}}