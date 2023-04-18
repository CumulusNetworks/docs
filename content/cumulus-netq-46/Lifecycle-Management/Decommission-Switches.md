---
title: Decommission Switches
author: NVIDIA
weight: 695
toc: 3
---

You might need to decommission a switch when you:

- Change the hostname of the monitored switch or host
- Move the monitored switch or host from one data center to another
- RMA the monitored switch or host

{{%notice note%}}

Decommissioning the switch or host removes information about the switch or host from the NetQ database. When the NetQ Agent restarts at a later date, it sends a connection request back to the database, so NetQ can monitor the switch or host again.

{{%/notice%}}

## Decommission a Switch

{{<tabs "TabID22" >}}

{{<tab "NetQ UI" >}}

1. From the LCM dashboard, navigate to the **Switch management** tab.

2. On the Switches card, select **Manage**.

3. Select the devices to decommission, then select the decommission icon above the table:

{{<figure src="/images/netq/decom-switch-box-450.png" alt="" width="600">}}

If you attempt to decommission a switch that is assigned a default, unmodified access profile, the process will fail. {{<link title="Credentials and Profiles" text="Create a unique access profile">}} (or update the default with unique credentials), then {{<link title="Switch Management/#attach-a-profile-to-a-switch" text="attach the profile">}} to the switch you want to decommission.

4. Confirm the devices you want to decommission.

5. Wait for the decommission process to complete, then select **Done**.

{{</tab>}}

{{<tab "NetQ CLI" >}}

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
{{</tab>}}

{{</tabs>}}


## Related Information

- {{<link title="Manage NetQ Agents">}}
- {{<link title="Uninstall NetQ">}}
