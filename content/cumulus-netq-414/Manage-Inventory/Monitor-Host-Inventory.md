---
title: Host Inventory
author: NVIDIA
weight: 750
toc: 4
---

In the UI, you can view your inventory of hosts across the network or individually, including a host's operating system, ASIC, CPU model, disk, platform, and memory information.

## Access and View Host Inventory Data

The Inventory/Hosts card monitors the hardware- and software-component inventory on hosts running NetQ in your network. To add this card to your workbench, search for "Inventory | Hosts" in the global search field.

{{<figure src="/images/netq/inventory-hosts-med-470.png" alt="host inventory card with chart" width="200">}}

Hover over the chart in the default card view to view component details. To view the distribution of components, hover over the card header and increase the card's size. Select the corresponding icon to view a detailed chart for ASIC, platform, or software components:

{{<figure src="/images/netq/hosts-inventory-large-470.png" alt="host inventory card displaying component distribution" width="600">}}

To display detailed information as a table, expand the card to its largest size:

{{<figure src="/images/netq/full-inventory-hosts-470.png" alt="fully expanded host inventory card displaying table with hosts information" width="1000">}}

## Decommission a Host

Decommissioning hosts removes information about the host from the NetQ database. The NetQ Agent must be disabled and in a 'rotten' state to complete the decommissioning process.

{{<tabs "TabID29" >}}

{{<tab "NetQ UI">}}

1. Locate the Inventory/Devices card on your workbench and expand it to full-screen.

2. From the **Hosts** tab, locate the **Agent state** column.  

    {{<figure src="/images/netq/decom-host-agent-470.png" alt="list of hosts displaying a fresh netq agent" width="1200">}}

If the NetQ Agents is in a 'fresh' state, you must stop and disable the NetQ Agent and wait until it reflects a 'rotten' state. To disable the agent, run the following commands on the host you want to decommission:

```
cumulus@host:~$ sudo systemctl stop netq-agent
cumulus@host:~$ sudo systemctl disable netq-agent
```

It may take a few minutes for the agent's new state to be reflected in the UI.

3. After you have confirmed that the agent is in a 'rotten' state, select the host you'd like to decommission, then select **Decommission device** above the table.

    {{<figure src="/images/netq/decom-hosts-470.png" alt="" width="1200">}}

{{</tab>}}

{{<tab "NetQ CLI" >}}

To decommission a host:

1. Stop and disable the NetQ Agent service on the host:

    ```
    cumulus@host:~$ sudo systemctl stop netq-agent
    cumulus@host:~$ sudo systemctl disable netq-agent
    ```

2. On the NetQ appliance or VM, decommission the host:

    ```
    cumulus@netq-appliance:~$ netq decommission <hostname-to-decommission>
    ```

{{</tab>}}

{{</tabs>}}