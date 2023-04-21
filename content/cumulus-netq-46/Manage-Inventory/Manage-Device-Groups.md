---
title: Device Groups
author: NVIDIA
weight: 770
---

Device groups allow you to create a label for a subset of devices in the inventory. You can configure {{<link title="Validate Network Protocol and Service Operations#validate-device-groups" text="validation checks">}} to run on select devices by referencing group names.

## Create a Device Group

To create a device group, add the Device Groups card to your workbench. In the header, click <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Open card**. Select the **Device groups** card:

{{<figure src="/images/netq/device-groups-460.png" alt="" width="500">}}

The Device Groups card will now be displayed on your workbench. Select **Create new group** and follow the instructions in the UI create a new group:

1. Enter a name for the group.

2. Create a hostname-based rule to define which devices in the inventory should be added to the group.

3. Confirm the expected matched devices appear in the inventory, and click **Create device group**.

The following example shows a group name of "exit group" matching any device in the inventory with "exit" in the hostname:

{{<figure src="/images/netq/create-group-rule.png" alt="" width="500">}}

## Update a Device Group

When new devices that match existing group rules are added to the inventory, NetQ flags the matching devices for review. The following example shows the switch "exit-2" detected in the inventory after the group was configured:

{{<figure src="/images/netq/device-in-review-initial-view.png" alt="" width="500">}}

To add the new device to the group inventory, click {{<img src="/images/netq/add-circle.svg" width="14">}} **Add device** and then click **Update device group**.

## Delete a Device Group

To delete a device group:

1. Expand the Device Groups card:

{{<figure src="/images/netq/expand-device-groups.png" alt="" width="200">}}

2. Click {{<img src="/images/netq/navigation-menu-horizontal.svg" width="14">}} Menu on the desired group and select **Delete**.

{{<figure src="/images/netq/delete-group.png" alt="" width="800">}}