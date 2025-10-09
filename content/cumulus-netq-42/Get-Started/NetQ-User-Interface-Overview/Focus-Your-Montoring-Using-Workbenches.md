---
title: Focus Your Monitoring Using Workbenches
author: NVIDIA
weight: 130
toc: 4
---
Workbenches are where you collect and view the data that is important to you.

Two types of workbenches are available:

<!-- vale off -->
- **Default**: Provided by NVIDIA; you *cannot* save changes you make to these workbenches
- **Custom**: Created by the user; changes made to these workbenches are saved automatically
<!-- vale on -->

Both types of workbenches display a set of cards. Default workbenches are public (accessible to all users), whereas custom workbenches are private (viewing is restricted to the user who created them).

## Default Workbenches

The default workbench contains Device Inventory, Switch Inventory, Events, and Network Health cards, giving you a high-level view of how your network is operating.

{{<figure src="/images/netq/access-ui-cumulus-wb-400.png" alt="default netq workbench" width="700">}}

On initial login, the NetQ Workbench opens. On subsequent logins, the last workbench you used opens.

## Custom Workbenches

Users with either administrative or user roles can create and save as many custom workbenches as suits their needs. For example, a user might create a workbench that:

- Shows all of the selected cards for the past week and one that shows all of the selected cards for the past 24 hours
- Only has data about your virtual overlays; EVPN plus events cards
- Has selected switches that you are troubleshooting
- Is focused on application or user account management

And so forth.

### Create a Workbench

To create a workbench:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"/> in the workbench header.

      {{<figure src="/images/netq/workbench-new-name-410.png" width="600">}}

2. Enter a name for the workbench.

3. Click "Set as home workbench" if you would like to set this as your new default home workbench.

4. Select the cards you would like to display on your new workbench by clicking on the desired cards:

      {{<figure src="/images/netq/workbench-new-cards-410.png" width="600">}}

5. Click **Create** to create your new workbench.

Refer to {{<link url="Access-Data-with-Cards">}} for information about interacting with cards on your workbenches.

### Clone a Workbench

To create a duplicate clone based on an existing workbench:

1. Click <img src="/images/netq/clone.svg" height="18" width="18"/> in the workbench header.

2. Set a name for the cloned workbench.

3. Click "set as home workbench" if you would like to set this as your new default home workbench.

4. Click **Clone** to clone the workbench.

      {{<figure src="/images/netq/workbench-clone-410.png" width="600">}}

### Remove a Workbench

Once you have created a number of custom workbenches, you might find that you no longer need some of them. As an administrative user, you can remove any workbench, except for the default NetQ Workbench. Users with a user role can only remove workbenches they have created.

To remove a workbench:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.

    {{<figure src="/images/netq/user-settings-profile-prefs-selected-222.png" width="150">}}

2. Click **Profile & Preferences**.

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
    - Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18"/> (main menu) and select the workbench from the **Favorites** or **NetQ** columns
- Open through the NVIDIA logo
    - Click the logo in the header to open your favorite workbench

## Manage Auto-refresh for Your Workbenches

You can specify how often to update the data displayed on your workbenches. Three refresh rates are available:

- **Analyze**: updates every 30 seconds
- **Debug**: updates every minute
- **Monitor**: updates every two (2) minutes

By default, auto-refresh is enabled and configured to update every 30 seconds.

### Disable/Enable Auto-refresh

To disable or pause auto-refresh of your workbenches, click the **Refresh** icon. This toggles between the two states, *Running* and *Paused*, where <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-play-1.svg" width="18"/> indicates it is currently disabled and <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" width="18"/> indicates it is currently enabled.

While having the workbenches update regularly is good most of the time, you might find that you want to pause the auto-refresh feature when you are troubleshooting and you do not want the data to change on a given set of cards temporarily. In this case, you can disable the auto-refresh and then enable it again when you are finished.

### View Current Settings

To view the current auto-refresh rate and operational status, hover over the **Refresh** icon on a workbench header, to open the tool tip as follows:

{{<figure src="/images/netq/wb-refresh-tooltips-231.png" width="350">}}

### Change Settings

To modify the auto-refresh setting:

1. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> the **Refresh** icon.

2. Select the refresh rate you want. The refresh rate is applied immediately. A check mark is shown next to the current selection.

    {{<figure src="/images/netq/wb-refresh-rate-set-400.png" width="150">}}

## Manage Workbenches

To manage your workbenches as a group, either:

- Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to the current workbench name, then click **Manage My WB**.
- Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" width="18"/>, select **Profiles & Preferences**.

Both of these open the Profiles & Preferences page. Look for the Workbenches card and refer to {{<link url="Set-User-Preferences#manage-your-workbenches" text="Manage Your Workbenches">}} for more information.
