---
title: NICs
author: NVIDIA
weight: 900
toc: 3
---

With the NetQ UI, you can view the attributes of individual network interface controllers (NICs), including their connection adapters and firmware versions. For NIC inventory information, refer to {{<link title="NIC Inventory" text="NIC Inventory">}}.

{{<notice note>}}
You must have {{<link title="Install NIC and DPU Agents" text="DOCA Telemetry Service enabled">}} to display NIC data in NetQ.
{{</notice>}}

## View NIC Attributes in the UI

To view attributes per NIC, open a NIC device card:

1. Search for the device’s hostname in the global search field or from the header select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Device card**.

2. Select a NIC from the dropdown.

3. Click **Add** to open an individual NIC card on your workbench, displaying ports, packets, and bytes information:

{{<figure src="/images/netq/ind-nic-res-470.png" alt="" width="250">}}

For a quick look at the key attributes of a particular NIC, expand the NIC card. Attributes are displayed as the default tab on the large NIC card. Select the **Interface stats** tab at the top of the card to view detailed interface statistics, including frame and carrier errors. 

{{<figure src="/images/netq/ind-nic-bytes-470.png" alt="NIC card displaying transmit and recieve data" width="800">}}

Expand the card to its largest size to view this information as tabular data, which you can filter and export.

## Related Information

- {{<link title="NIC Inventory" text="NIC Inventory">}}