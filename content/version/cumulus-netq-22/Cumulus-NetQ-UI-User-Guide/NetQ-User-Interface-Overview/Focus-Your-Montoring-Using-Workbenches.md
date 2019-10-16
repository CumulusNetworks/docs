---
title: Focus Your Monitoring Using Workbenches
author: Cumulus Networks
weight: 507
pageID: 12321856
product: Cumulus NetQ
version: 2.2
imgData: cumulus-netq-22
siteSlug: cumulus-netq-22
---
Workbenches are an integral structure of the Cumulus NetQ application. They are where you collect and view the data that is important to you.

There are two types of workbenches:

- **Default**: Provided by Cumulus Networks for use as they exist; changes made to these workbenches *cannot* be saved
- **Custom**: Created by application users when default workbenches need some adjustments to better meet your needs or a completely different collection of cards is wanted; changes made to these workbenches *can* be saved

Both types of workbenches display a set of cards. Both types of workbenches are created on a per user basis (private) and are only viewable that user.

## Default Workbenches

In this release, only one default workbench is available, the *Cumulus Workbench*, to get you started. It contains Device Inventory, Switch Inventory, Alarm and Info Events, and Network Health cards, giving you a high-level view of how your network is operating.

{{< figure src="/images/netq/cumulus-wb-default.png" width="700" >}}

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

      {{< figure src="/images/netq/add-workbench-modal.png" width="200" >}}

2. Enter a name for the workbench.

3. Move the toggle switch to the right to make the workbench public, or leave the switch as is to keep it private. By default, workbenches are private on creation.

4. Click **Create** to open the new workbench, or **Cancel** to discard the workbench.

Refer to [Access Data with Cards](../Access-Data-with-Cards) for information about interacting with cards on your workbenches.

### Save a Workbench

Once you have created a custom workbench, you can save any changes you make to it.

To save a workbench:

1. When you have the workbench open, click <img src="https://icons.cumulusnetworks.com/03-Computers-Devices-Electronics/11-Floppy-Disks/floppy-disk-2.svg", height="18", width="18"/> in the workbench header.

      {{< figure src="/images/netq/save-custom-wb.png" width="200" >}}

2. Click **Yes** to save the changes, or click **Cancel** to discard your changes.
