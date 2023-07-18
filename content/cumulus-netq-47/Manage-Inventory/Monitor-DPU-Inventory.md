---
title: DPU Inventory
author: NVIDIA
weight: 760
toc: 4
---

Use the UI or CLI to view your data processing unit (DPU) inventory. For DPU performance information, refer to {{<link title="DPUs" text="DPU Monitoring">}}.

## DPU Inventory Commands

Several forms of this command are available based on the inventory component you'd like to view. See the {{<link title="show/#netq-show-inventory" text="command line reference">}} for additional options, definitions, and examples.

```
netq show inventory (brief | asic | board | cpu | disk | memory | license | os)
```

## View DPU Inventory in the UI

The Inventory/DPU card displays the hardware- and software-component inventory on DPUs running NetQ in your network, including operating system, ASIC, CPU model, disk, platform, and memory information. 

To add this card to your workbench, select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card**&nbsp;<span aria-label="and then">></span>**Inventory**&nbsp;<span aria-label="and then">></span> **Inventory/DPU card**&nbsp;<span aria-label="and then">></span> **Open cards**.

{{<figure src="/images/netq/dpu-inventory-updated.png" alt="DPU inventory card with chart" width="200">}}

Hover over the chart to view component details. To view the distribution of components, hover over the card header and increase the card's size. Select the corresponding icon to view a detailed chart for ASIC, platform, or software components:

{{<figure src="/images/netq/dpu-inventory-l3-42.png" alt="medium DPU inventory card displaying component distribution" width="650">}}

Expand the card to its largest size to view, filter, and export detailed information: 

{{<figure src="/images/netq/dpu-inventory-l4-42.png" alt="fully expanded DPU inventory card displaying a table with data" width="1100">}}

## Decommission a DPU

Decommissioning DPUs removes information about the DPU from the NetQ database. The NetQ Agent must be disabled and in a 'rotten' state to complete the decommissioning process.

{{<tabs "TabID29" >}}

{{<tab "NetQ UI">}}

1. Locate the Inventory/Devices card on your workbench and expand it to full-screen.

2. From the **DPUs** tab, locate the **Agent state** column.  

If the NetQ Agent is in a 'fresh' state, you must stop and disable the NetQ Agent and wait until it reflects a 'rotten' state. To disable the agent, run the following command on the DPU you want to decommission. Replace *<netq_server>* with the IP address of your NetQ VM:

```
sed -i s'/<netq_server>/127.0.0.1/g' /etc/kubelet.d/doca_telemetry_standalone.yaml
```

{{<notice info>}}
It may take up to 30 minutes for the agent's new state to be reflected in the UI.
{{</notice>}}
3. After you have confirmed that the agent is in a 'rotten' state, select the DPU you'd like to decommission, then select **Decommission device** above the table.

{{</tab>}}

{{<tab "NetQ CLI" >}}

To decommission a host:

1. Stop and disable the NetQ Agent service on the host. Replace *<netq_server>* with the IP address of your NetQ VM:

    ```
    sed -i s'/<netq_server>/127.0.0.1/g' /etc/kubelet.d/doca_telemetry_standalone.yaml
    ```

2. On the NetQ appliance or VM, decommission the DPU:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>
    ```

{{</tab>}}

{{</tabs>}}

## Related Information

To read more about NVIDIA BlueField DPUs and the DOCA Telemetry Service, refer to the {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service/index.html" text="DOCA SDK Documentation">}}.