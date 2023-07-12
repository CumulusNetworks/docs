---
title: DPUs
author: NVIDIA
weight: 810
toc: 3
---

With the NetQ UI, you can monitor hardware resources of individual data processing units (DPUs), including CPU utilization, disk usage, and memory utilization.

For DPU inventory information, refer to {{<link title="DPU Inventory" text="DPU Inventory">}}.

## View Overall Health of a DPU

For an overview of the current or past health of DPU hardware resources, open the DPU device card. To open a DPU device card:

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the header, then click **Open a device card**.

2. Select a DPU from the dropdown.

3. Click **Add**. This example shows that the *r-netq-bf2-01* DPU has low utilization across CPU, memory, and disks:

    {{<figure src="/images/netq/dev-medium-dpu-card-42.png" alt="DPU card displaying CPU, memory, and disk utilization statistics" width="200">}}

### View DPU Attributes

For a quick look at the key attributes of a particular DPU, expand the DPU card.

Attributes are displayed as the default tab on the large DPU card. You can view the static information about the DPU, including its hostname, ASIC vendor and model, CPU information, OS version, and agent version.

{{<figure src="/images/netq/dev-dpu-large-attributes-tab-42.png" alt="large DPU card displaying static DPU information" width="700">}}

To view a larger display of hardware resource utilization, select {{<img src="/images/netq/analytics-bars.svg" alt="" height="18" width="18">}} **Utilization**.

{{<figure src="/images/netq/dev-dpu-large-utilization-42.png" width="700">}}
## View Installed Packages

To view, filter, or export the list of installed packages on a particular DPU, expand the card to its largest size:

{{<figure src="/images/netq/dpu-hwresources-l4-installed-packages-42.png" alt="list of packages installed on a DPU" width="1100">}}

## Related Information

To read more about NVIDIA BlueField DPUs and the DOCA Telemetry Service, refer to the {{<exlink url="https://docs.nvidia.com/doca/sdk/doca-telemetry-service/index.html" text="DOCA SDK Documentation">}}.