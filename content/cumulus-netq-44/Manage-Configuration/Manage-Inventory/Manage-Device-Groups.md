---
title: Device Groups
author: NVIDIA
weight: 770
---

Device groups allow you to create a label for a subset of devices in the inventory. You can configure {{<link title="Validate Network Protocol and Service Operations#validate-device-groups" text="validation checks">}} to run on select devices by referencing group names.

## Create a Device Group

To create a device group, add the Device Groups card to your workbench. Click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> to navigate to the **Device Groups** section and click **Open Cards** after selecting the **Device groups** card:

{{<figure src="/images/netq/device-groups-add-card.png" width="700">}}

The Device groups card will now be displayed on your workbench. Click **Create New Group** to create a new device group:

{{<figure src="/images/netq/create-new-group-card.png" width="200">}}

The Create New Group wizard will be displayed. To finish creating a new group:

1. Set the name of the group of devices.

2. Declare a hostname-based rule to define which devices in the inventory should be added to the group.

3. Confirm the expected matched devices appear in the inventory, and click **Create device group**.

The following example shows a group name of "exit group" matching any device in the inventory with "exit" in the hostname:

{{<figure src="/images/netq/create-group-rule.png" width="500">}}

## Updating a Device Group

When new devices that match existing group rules are added to the inventory, those devices matching the rule criteria will be flagged for review to be added to the group inventory. The following example shows the switch "exit-2" being detected in the inventory after the group was already configured:

{{<figure src="/images/netq/device-in-review-initial-view.png" width="500">}}

To add the new device to the group inventory, click {{<img src="/images/netq/add-circle.svg" width="14">}} and then click **Update device group**.


## Removing a Device Group

To delete a device group:

1. Expand the Device Groups card:

{{<figure src="/images/netq/expand-device-groups.png" width="200">}}

2. Click {{<img src="/images/netq/navigation-menu-horizontal.svg" width="14">}} on the desired group and select **Delete**.

{{<figure src="/images/netq/delete-group.png" width="800">}}