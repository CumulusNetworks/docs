---
title: NVLink4 Inventory
author: NVIDIA
weight: 1150
toc: 3

---

This section describes how to view device statistics and data for NVLink4 switches and GPUs.

Add NVLink cards to your workbench to:
 - View the distribution of software and hardware components.
 - View interface statistics.
 - View digital optics statistics.
 - View informational and error events.

 ## View NVLink4 Inventory in the UI

 In the header, select {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} **Add card**:

 {{<figure src="/images/netq/nvl4-header-card.png" alt="" width="950">}}

 Select cards to add them to your workbench. There are two NVLink4 inventory cards---NVL4 switches and NVL4 GPUs.

 Select **Open cards**, then locate the cards on the workbench. Fully expand the card to reveal a table of your networkwide inventory, with device statistics and data. The following image displays device statistics for an NVLink4 GPU:

  {{<figure src="/images/netq/nvl4-inventory-gpu.png" width="1050">}}

  Select the checkbox next to a device to reveal a card icon {{<img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18">}} above the table. Select the icon to open an individual device card on your workbench. You can also enter the name of the device in the global search field to add the device to your workbench:

   {{<figure src="/images/netq/nvlink-events-large-460.png" alt="" width="200">}}

By adjusting a card's size, you can view device statistics and data with various displays and visualizations. The following large-sized cards display interface statistics, including columns for transmit and receive data:

{{<figure src="/images/netq/nvl4-flits.png" alt="card displaying flits data" width="650">}}

{{<figure src="/images/netq/nvl4-interfaces-channels.png" alt="card displaying channel data" width="650">}}

When fully expanded, NVLink4 device cards display an events summary. Select the categories in the side menu to view, filter, or sort information about interfaces, cable ports, sensors, and digital optics.

{{<figure src="/images/netq/nvlink-events-full-460.png" alt="fully-expanded NVLink card showing devices statistics" width="1100">}}

## Related Information

- {{<link title="Access Data with Cards">}}
- {{<link title="NVLink4 Events">}}
