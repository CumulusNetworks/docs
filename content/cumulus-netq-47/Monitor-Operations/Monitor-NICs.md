---
title: NICs
author: NVIDIA
weight: 900
toc: 3
---

With the NetQ UI, you can view the attributes of individual network interface controllers (NICs), including their connection adapters and firmware versions. For NIC inventory information, refer to {{<link title="NIC Inventory" text="NIC Inventory">}}.

## View NIC Attributes in the UI

To view attributes per NIC, open a NIC device card:

1. Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the header, then click **Open a device card**.

2. Select a NIC from the dropdown.

3. Click **Add**. The following card shows that there are 6 total NICs, each with the same adapter type and firmware version.

    {{<figure src="/images/netq/single-nic-large-470.png" alt="NIC card displaying connection adapter" width="600">}}

Expand this card to full-screen to display a list of servers with their corresponding NICs.


### View NIC Attributes

For a quick look at the key attributes of a particular NIC, expand the NIC card.

Attributes are displayed as the default tab on the large NIC card. You can view the static information about the DPU, including its hostname, ASIC vendor and model, CPU information, OS version, and agent version.

{{<figure src="/images/netq/dev-dpu-large-attributes-tab-42.png" alt="large DPU card displaying static DPU information" width="700">}}

To view a larger display of hardware resource utilization, select {{<img src="/images/netq/analytics-bars.svg" alt="" height="18" width="18">}} **Utilization**.

{{<figure src="/images/netq/dev-dpu-large-utilization-42.png" width="700">}}
## View Installed Packages

To view, filter, or export the list of installed packages on a particular NIC, expand the card to its largest size:


## Related Information
