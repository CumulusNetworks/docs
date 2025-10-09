---
title: Focus Your Monitoring Using Workbenches
author: NVIDIA
weight: 130
toc: 4
---
Workbenches are an integral structure of the NetQ UI. They are where you collect and view the data that is important to you.

Two types of workbenches are available:

- **Default**: Provided by NVIDIA for use as they exist; changes made to these workbenches *cannot* be saved
- **Custom**: Created by application users when default workbenches need some adjustments to better meet your needs or a completely different collection of cards is wanted; changes made to these workbenches are saved automatically

Both types of workbenches display a set of cards. Default workbenches are public (available for viewing by all users), whereas Custom workbenches are private (only viewable by the user who created them).

## Default Workbenches

In this release, only one default workbench is available, the *Cumulus Workbench*, to get you started. It contains Device Inventory, Switch Inventory, Alarm and Info Events, and Network Health cards, giving you a high-level view of how your network is operating.

{{< figure src="/images/netq/cumulus-workbench-cloud-231.png" width="700" >}}

On initial login, the Cumulus Workbench is opened. On subsequent logins, the last workbench you had displayed is opened.

## Custom Workbenches

Users with either administrative or user roles can create and save as many custom workbenches as suits their needs. For example, a user might create a workbench that:

- Shows all of the selected cards for the past week and one that shows all of the selected cards for the past 24 hours
- Only has data about your virtual overlays; EVPN plus events cards
- Has selected switches that you are troubleshooting
- Focused on application or user account management

And so forth.

### Create a Workbench

To create a workbench:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg" height="18" width="18"/> in the workbench header.

      {{<figure src="/images/netq/add-custom-workbench-modal-230.png" width="200">}}

2. Enter a name for the workbench.

3. Click **Create** to open a blank new workbench, or **Cancel** to discard the workbench.

4. Add cards to the workbench using <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> or <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg" height="18" width="18"/>.

Refer to {{<link url="Access-Data-with-Cards">}} for information about interacting with cards on your workbenches.

### Remove a Workbench

Once you have created a number of custom workbenches, you might find that you no longer need some of them. As an administrative user, you can remove any workbench, except for the default Cumulus Workbench. Users with a user role can only remove workbenches they have created.

To remove a workbench:

1. Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" height="18" width="18"/> in the application header to open the **User Settings** options.

    {{<figure src="/images/netq/user-settings-profile-prefs-selected-222.png" width="150">}}

2. Click **Profile & Preferences**.

3. Locate the Workbenches card.

4. Hover over the workbench you want to remove, and click **Delete**.

## Open an Existing Workbench

There are several options for opening workbenches:

- Open through Workbench Header
    - Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to the current workbench name and locate the workbench
        - Under My Home, click the name of your favorite workbench
        - Under My Most Recent, click the workbench if in list
        - Search by workbench name
        - Click **All My WB** to open all workbenches and select it from the list
- Open through Main Menu
    - Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18"/> (Main Menu) and select the workbench from the **Favorites** or **NetQ** columns
- Open through Cumulus logo
    - Click the logo in the header to open your favorite workbench

## Manage Auto-refresh for Your Workbenches

With NetQ 2.3.1 and later, you can specify how often to update the data displayed on your workbenches. Three refresh rates are available:

- **Analyze**: updates every 30 seconds
- **Debug**: updates every minute
- **Monitor**: updates every two (2) minutes

By default, auto-refresh is enabled and configured to update every 30 seconds.

### Disable/Enable Auto-refresh

To disable or pause auto-refresh of your workbenches, simply click the **Refresh** icon. This toggles between the two states, *Running* and *Paused*, where <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-play-1.svg" width="18"/> indicates it is currently disabled and <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/42-Multimedia-Controls/button-pause.svg" width="18"/> indicates it is currently enabled.

While having the workbenches update regularly is good most of the time, you may find that you want to pause the auto-refresh feature when you are troubleshooting and you do not want the data to change on a given set of cards temporarily. In this case, you can disable the auto-refresh and then enable it again when you are finished.

### View Current Settings

To view the current auto-refresh rate and operational status, hover over the **Refresh** icon on a workbench header, to open the tool tip as follows:

{{<figure src="/images/netq/wb-refresh-tooltips-231.png" width="350">}}

### Change Settings

To modify the auto-refresh setting:

1. Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> on the **Refresh** icon.

2. Select the refresh rate you want. The refresh rate is applied immediately. A check mark is shown next to the current selection.

    {{<figure src="/images/netq/wb-refresh-rate-selection-231.png" width="150">}}

## Manage Workbenches

To manage your workbenches as a group, either:

- Click <img src="https://icons.cumulusnetworks.com/52-Arrows-Diagrams/01-Arrows/arrow-button-down-2.svg" width="18"/> next to the current workbench name, then click **Manage My WB**. 
- Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg" width="18"/>, select **Profiles & Preferences** option.

Both of these open the Profiles & Preferences page. Look for the Workbenches card and refer to {{<link url="Set-User-Preferences#manage-your-workbenches" text="Manage Your Workbenches">}} for more information.
