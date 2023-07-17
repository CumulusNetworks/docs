---
title: NIC Inventory
author: NVIDIA
weight: 760
toc: 4
---

Use the UI or CLI to view your network interface controller (NIC) inventory. For NIC performance information, refer to {{<link title="NICs" text="NIC Monitoring">}}.


## NIC Inventory Commands

Several forms of this command are available based on the inventory component you'd like to view. See the {{<link title="show/#netq-show-inventory" text="command line reference">}} for additional options, definitions, and examples.

```
netq show inventory (brief | asic | board | cpu | disk | memory | license | os)
```
## View NIC Inventory in the UI

The Inventory/NIC card displays the hardware- and software-component inventory on NICs running NetQ in your network, including connection adapters and firmware versions. 

To add this card to your workbench, select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card**&nbsp;<span aria-label="and then">></span>**Inventory**&nbsp;<span aria-label="and then">></span> **Inventory/NICs card**&nbsp;<span aria-label="and then">></span> **Open cards**. Select the dropdown on the card to display alternately connection adapters or firmware versions.

{{<figure src="/images/netq/inventory-nics-med-470.png" alt="NIC inventory card displaying firmware version" width="200">}}

Expand the card to full-screen to view a list of hosts and their associated NICs:

{{<figure src="/images/netq/single-nic-full-crop-470.png" alt="fullscreen NIC inventory card displaying hosts and their associated NICs" width="1100">}}

To view data from an individual NIC, select it from the table, then select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card** above the table. An individual {{<link title="NICs" text="NIC monitoring card">}} opens on your workbench, displaying ports, packets, and bytes information:

{{<figure src="/images/netq/ind-nic-470.png" alt="" width="200">}}

You can expand this card to large or full-screen to view detailed interface statistics, including frame and carrier errors. 

## Decommission a NIC

Decommissioning NICs removes information about the NIC from the NetQ database. The NetQ Agent must be disabled and in a 'rotten' state to complete the decommissioning process.

{{<tabs "TabID29" >}}

{{<tab "NetQ UI">}}

1. Locate the Inventory/Devices card on your workbench and expand it to full-screen.

2. From the **NICs** tab, locate the **Agent state** column.  

    {{<figure src="/images/netq/decom-host-agent-470.png" alt="list of hosts displaying a fresh netq agent" width="1200">}}

If the NetQ Agents is in a 'fresh' state, you must stop and disable the NetQ Agent and wait until it reflects a 'rotten' state. To disable the agent, stop the DTS container on the server with the following command:

```
docker stop doca_telemetry
```
{{<notice info>}}
It may take up to 30 minutes for the agent's new state to be reflected in the UI.
{{</notice>}}
3. After you have confirmed that the agent is in a 'rotten' state, select the host you'd like to decommission, then select **Decommission device** above the table.

    {{<figure src="/images/netq/decom-hosts-470.png" alt="" width="1200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To decommission a NIC:

1. 

2. On the NetQ appliance or VM, decommission the NIC:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>
    ```

{{</tab>}}

{{</tabs>}}

