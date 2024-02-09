---
title: NIC Inventory
author: NVIDIA
weight: 760
toc: 4
---

Use the UI or CLI to view your network interface controller (NIC) inventory. For NIC performance information, refer to {{<link title="NICs" text="NIC Monitoring">}}.

{{<notice note>}}
NIC telemetry for ConnectX adapters is supported for on-premises NetQ deployments. You must have {{<link title="Install NIC and DPU Agents" text="DOCA Telemetry Service enabled">}} and Prometheus targets configured to display NIC data in NetQ.
{{</notice>}}


## NIC Inventory Commands

Run the {{<link title="show/#netq-show-inventory" text="netq show inventory brief">}} command to display an inventory summary, including a list of NICs.

```
netq show inventory brief
```
## View NIC Inventory in the UI

The Inventory/NIC card displays the hardware- and software-component inventory on NICs running NetQ in your network, including connection adapters and firmware versions. 

To add this card to your workbench, select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card**&nbsp;<span aria-label="and then">></span> **Inventory**&nbsp;<span aria-label="and then">></span> **Inventory/NICs card**&nbsp;<span aria-label="and then">></span> **Open cards**. Select the dropdown on the card to display either connection adapters or firmware versions.

{{<figure src="/images/netq/invent-nic-470.png" alt="NIC inventory card displaying firmware version" width="200">}}

Expand the card to full-screen to view a list of hosts and their associated NICs:

{{<figure src="/images/netq/fullscreen-nics-470.png" alt="fullscreen NIC inventory card displaying hosts and their associated NICs" width="1100">}}

To view data from an individual NIC, select it from the table, then select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** above the table. An individual {{<link title="NICs" text="NIC monitoring card">}} opens on your workbench, displaying ports, packets, and bytes information:

{{<figure src="/images/netq/ind-nic-res-470.png" alt="" width="200">}}

You can expand this card to large or full-screen to view detailed interface statistics, including frame and carrier errors. 

## Decommission a NIC

Decommissioning removes information about the NIC from the NetQ database.

{{<tabs "TabID29" >}}

{{<tab "NetQ UI">}}

1. Stop the DTS container on the NIC's host with the following command:

    ```
    docker stop doca_telemetry
    ```

2. Locate the Inventory/Devices card on your workbench and expand it to full-screen.

3. Navigate to the **NICs** tab.  

    {{<figure src="/images/netq/decom-nics-rotten-470.png" alt="list of nics displaying a rotten netq agent" width="1200">}}

4. Select the NIC you'd like to decommission, then select **Decommission device** above the table.

    {{<figure src="/images/netq/decom-nics-icon-470.png" alt="" width="1200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To decommission a NIC:

1. Stop the DTS container on the NIC's host with the following command:

    ```
    docker stop doca_telemetry
    ```

2. On the NetQ appliance or VM, decommission the NIC:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>/<NIC-guid>
    ```

Either obtain the NIC guid from the NetQ UI in the full-screen NIC Inventory card, or use tab completion with the `netq decommission <hostname>` command to view the NIC guids.

{{</tab>}}

{{</tabs>}}

## Related Information

- {{<link title="NICs" text="NIC Monitoring">}}

