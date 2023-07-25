---
title: NICs
author: NVIDIA
weight: 900
toc: 3
---

With the NetQ UI, you can view the attributes of individual network interface controllers (NICs), including their connection adapters and firmware versions. For NIC inventory information, refer to {{<link title="NIC Inventory" text="NIC Inventory">}}.

{{<notice note>}}
NIC telemetry for ConnectX adapters is supported for on-premises NetQ deployments. You must have {{<link title="Install NIC and DPU Agents" text="DOCA Telemetry Service enabled">}} and Prometheus targets configured to display NIC data in NetQ.
{{</notice>}}

## View NIC Attributes in the UI

To view attributes per NIC, open a NIC device card:

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the header, then click **Open a device card**.

2. Select a NIC from the dropdown.

3. Click **Add** to open an individual NIC card on your workbench, displaying ports, packets, and bytes information:

{{<figure src="/images/netq/ind-nic-res-470.png" alt="" width="250">}}

For a quick look at the key attributes of a particular NIC, expand the NIC card. Attributes are displayed as the default tab on the large NIC card. Select the **Interface stats** tab at the top of the card to view detailed interface statistics, including frame and carrier errors. 

{{<figure src="/images/netq/ind-nic-bytes-470.png" alt="NIC card displaying transmit and recieve data" width="800">}}

Expand the card to its largest size to view this information as tabular data, which you can filter and export.

## Related Information

- {{<link title="NIC Inventory" text="NIC Inventory">}}