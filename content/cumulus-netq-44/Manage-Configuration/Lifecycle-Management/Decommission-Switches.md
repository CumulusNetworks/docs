---
title: Decommission Switches
author: NVIDIA
weight: 695
toc: 3
---

You can decommission a switch or host at any time. You might need to do this when you:

- Change the hostname of the monitored switch or host
- Move the monitored switch or host from one data center to another
- RMA the monitored switch or host

{{%notice note%}}

Decommissioning the switch or host removes information about the switch or host from the NetQ database. When the NetQ Agent restarts at a later date, it sends a connection request back to the database, so NetQ can monitor the switch or host again.

{{%/notice%}}

## Decommission from the CLI

To decommission a switch or host:

1. On the given switch or host, stop and disable the NetQ Agent service:

    ```
    cumulus@switch:~$ sudo systemctl stop netq-agent
    cumulus@switch:~$ sudo systemctl disable netq-agent
    ```

2. On the NetQ On-premises or Cloud Appliance or VM, decommission the switch or host:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>
    ```

## Decommission from the NetQ UI

You can decommission a switch or host from the NetQ UI using the Inventory/Devices card. This stops and disables the NetQ Agent service on the device, and decommissions it from the NetQ database.

1. Expand the Inventory/Devices card to list the devices in the current inventory:

{{<figure src="/images/netq/inventory-devices-card.png" alt="inventory card displaying 12 hosts and 12 switches" width="200">}}

2. Select the devices to decommission, then select the decommission icon above the table:

{{<figure src="/images/netq/decommission-select.png" alt="expanded inventory card with one device selected" width="600">}}

3. Confirm the devices to decommission:

{{<figure src="/images/netq/decommission-confirmation.png" alt="confirmation dialog with a list of devices" width="600">}}

4. Wait for the decommission process to complete, then select **Done**.


## Related Information

- {{<link title="Manage NetQ Agents">}}
- {{<link title="Uninstall NetQ">}}
