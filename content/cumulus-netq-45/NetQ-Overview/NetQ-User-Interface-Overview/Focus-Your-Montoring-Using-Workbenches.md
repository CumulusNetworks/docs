---
title: Focus Your Monitoring Using Workbenches
author: NVIDIA
weight: 130
toc: 4
---
Workbenches are dashboards where you collect and view data. Two types of workbenches are available:

<!-- vale off -->
- **Default**: Provided by NVIDIA; you *cannot* save changes you make to these workbenches
- **Custom**: Created by the user; changes made to these workbenches are saved automatically
<!-- vale on -->

Both types of workbenches display a set of cards. Default workbenches are public (accessible to all users), whereas custom workbenches are private (viewing is restricted to the user who created them).
## Default Workbenches

The default workbench contains Device Inventory, Switch Inventory, Events, and Validation Summary cards, giving you a high-level view of how your network is operating.

{{<figure src="/images/netq/default-workbench.png" alt="default netq workbench" width="900">}}

Upon initial login, the NetQ Workbench opens. Upon subsequent logins, the last workbench you viewed opens.

## Custom Workbenches

People with either administrative or user roles can create and save an unlimited number of custom workbenches. For example, you might create a workbench that:

- Shows network statistics for the past week alongside network statistics for the past 24 hours.
- Only displays data about virtual overlays.
- Displays switches that you are troubleshooting.
- Is focused on application or account management.

### Create a Workbench

1. Select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" alt="add icon" height="18" width="18"/> **New** in the workbench header.

2. Enter a name for the workbench and choose whether to set it as your default home workbench.

4. Select the cards you would like to display on your new workbench.

      {{<figure src="/images/netq/create-a-workbench.png" alt="interface displaying the cards a user can select to add to their workbench" width="800">}}

5. Click **Create** to create your new workbench.

Refer to {{<link url="Access-Data-with-Cards">}} for information about interacting with cards on your workbenches.

### Clone a Workbench

To create a duplicate of an existing workbench:

1. Select <img src="/images/netq/clone.svg" height="18" width="18"/> **Clone** in the workbench header.

2. Name the cloned workbench and select **Clone**.

### Remove a Workbench

Admin accounts can remove any workbench, except for the default NetQ Workbench. User accounts can only remove workbenches they have created.

To remove a workbench:

1. Select <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" alt="profile icon" height="18" width="18"/> in the upper-right corner to open the **User Settings** options.

2. Select **Profile & Preferences**.

3. Locate the Workbenches card.

4. Hover over the workbench you want to remove, and click **Delete**.

## Open an Existing Workbench

There are several options for opening workbenches:

- Open through the Workbench header
    - Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to the current workbench name and locate the workbench
        - Under My Home, click the name of your favorite workbench
        - Under My Most Recent, click the workbench if in list
        - Search by workbench name
        - Click **All My WB** to open all workbenches and select it from the list
- Open through the main menu
    - Expand the <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18"/> Menu and select the workbench from the **Favorites** or **Workbenches** sections
- Open through the NVIDIA logo
    - Click the logo in the header to open your favorite workbench

## Manage Auto-refresh for Your Workbenches

You can specify how often to update the data displayed on your workbenches. Three refresh rates are available:

- **Analyze**: updates every 30 seconds
- **Debug**: updates every minute
- **Monitor**: updates every 2 minutes

By default, auto-refresh is enabled and configured to update every 30 seconds.
### Change Settings

To modify the auto-refresh setting:

1. Select the dropdown <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to **Refresh**.

2. Select the refresh rate. A check mark is shown next to the current selection. The new refresh rate is applied immediately. 

    {{<figure src="/images/netq/wb-refresh-rate-set-400.png" alt="refresh rate dropdown listng rate options of 30 seconds, 1 minute, and 2 minutes" width="150">}}

### Disable/Enable Auto-refresh

When you are troubleshooting and do not want the displayed data to update, you can disable auto-refresh then enable it when you are finished.

To disable or pause auto-refresh, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" alt="pause icon" width="18"/> above **Refresh** in the workbench header. When you're ready for the data to refresh, select <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-play-1.svg" alt="play icon" width="18"/>.
