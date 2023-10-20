---
title: DPUs
author: NVIDIA
weight: 810
toc: 3
---

With the NetQ UI, you can monitor hardware resources of individual data processing units (DPUs), including CPU utilization, disk usage, and memory utilization. For DPU inventory information, refer to {{<link title="DPU Inventory" text="DPU Inventory">}}.

{{<notice note>}}
You must install and configure {{<link title="Install NIC and DPU Agents/#install-dts-on-dpus" text="install and configure the DOCA Telemetry Service">}} to display DPU data in NetQ.
{{</notice>}}

## View Overall Health of a DPU

For an overview of the current or past health of DPU hardware resources, open the DPU device card. To open a DPU device card:

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the header, then click **Open a device card**.

2. Select a DPU from the dropdown.

3. Click **Add**. This example shows that the *r-netq-bf2-01* DPU has low utilization across CPU, memory, and disks:

    {{<figure src="/images/netq/dev-medium-dpu-card-42.png" alt="DPU card displaying CPU, memory, and disk utilization statistics" width="200">}}

## View DPU Attributes

For a quick look at the key attributes of a particular DPU, expand the DPU card.

Attributes are displayed as the default tab on the large DPU card. You can view the static information about the DPU, including its hostname, ASIC vendor and model, CPU information, OS version, and agent version.

{{<figure src="/images/netq/dev-dpu-large-attributes-tab-42.png" alt="large DPU card displaying static DPU information" width="700">}}

To view a larger display of hardware resource utilization, select {{<img src="/images/netq/analytics-bars.svg" alt="" height="18" width="18">}} **Utilization**.

{{<figure src="/images/netq/dev-dpu-large-utilization-42.png" width="700">}}

Expand the card to its largest size to view a list of installed packages and RoCE counters for a given DPU. 

## Related Information

To read more about NVIDIA BlueField DPUs and the DOCA Telemetry Service, refer to the {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service/index.html" text="DOCA SDK Documentation">}}.