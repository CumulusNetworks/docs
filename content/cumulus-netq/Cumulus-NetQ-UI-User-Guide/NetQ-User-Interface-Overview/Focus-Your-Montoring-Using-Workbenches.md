---
title: Focus Your Monitoring Using Workbenches
author: Cumulus Networks
weight: 507
aliases:
 - /display/NETQ22/NetQ-User-Interface-Overview
 - /pages/viewpage.action?pageId=12321856
pageID: 12321856
product: Cumulus NetQ
version: 2.3
imgData: cumulus-netq
siteSlug: cumulus-netq
---
Workbenches are an integral structure of the Cumulus NetQ application. They are where you collect and view the data that is important to you.

There are two types of workbenches:

- **Default**: Provided by Cumulus Networks for use as they exist; changes made to these workbenches *cannot* be saved
- **Custom**: Created by application users when default workbenches need some adjustments to better meet your needs or a completely different collection of cards is wanted; changes made to these workbenches are saved automatically.

Both types of workbenches display a set of cards. Default workbenches are public (available for viewing by all users), whereas Custom workbenches are private (only viewable by user who created them).

## Default Workbenches

In this release, only one default workbench is available, the *Cumulus Workbench*, to get you started. It contains Device Inventory, Switch Inventory, Alarm and Info Events, and Network Health cards, giving you a high-level view of how your network is operating.

{{< figure src="/images/netq/cumulus-workbench-cloud-230.png" width="700" >}}

On initial login, the Cumulus Workbench is opened. On subsequent logins, the last workbench you had displayed is opened.

## Custom Workbenches

You can create and save as many workbenches as suit your needs. For example, create a workbench that:

- shows all of the selected cards for the past week and one that shows all of the selected cards for the past 24 hours
- only has data about your virtual overlays; EVPN plus events cards
- has selected switches that you are troubleshooting
- focused on application or user account management
- etc.

### Create a Workbench

To create a workbench:

1. Click <img src="https://icons.cumulusnetworks.com/01-Interface-Essential/43-Remove-Add/add-circle.svg", height="18", width="18"/> in the workbench header.

      {{<figure src="/images/netq/add-custom-workbench-modal-230.png" width="200">}}

2. Enter a name for the workbench.

3. Click **Create** to open a blank new workbench, or **Cancel** to discard the workbench.

4. Add cards to the workbench using <img src="https://icons.cumulusnetworks.com/44-Entertainment-Event-Hobbies/02-Card-Games/card-game-diamond.svg", height="18", width="18"/> or <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/09-Hard-Drives/hard-drive-1.svg", height="18", width="18"/>.

Refer to [Access Data with Cards](/cumulus-netq/Cumulus-NetQ-UI-User-Guide/NetQ-User-Interface-Overview/Access-Data-with-Cards) for information about interacting with cards on your workbenches.

### Remove a Workbench

Once you have created a number of custom workbenches, you might find that you no longer need some of them.

To remove a workbench:

1.  Click <img src="https://icons.cumulusnetworks.com/17-Users/19-Natural-Close%20Up-Single%20User-Man/single-man-circle.svg", height="18", width="18"/> in the application header to open the **User Settings** options.

    {{<figure src="/images/netq/user-settings-profile-prefs-selected-222.png" width="150">}}

2.  Click **Profile & Preferences**.

3. Locate the Workbenches card.

4. Hover over the workbench you want to remove, and click **Delete**.

Refer to [Manage Your Workbenches](../Set-User-Preferences/#manage-your-workbenches) for more detail about workbench management.
