---
title: PTP
author: NVIDIA
weight: 930
toc: 3
bookhidden: true
---

{{<notice note>}}

PTP monitoring is an early access feature. It requires a switch fabric running Cumulus Linux version 5.0 and above and NetQ Agent 4.5.

{{</notice>}}

Use the UI or CLI to monitor Precision Time Protocol, including clock hierarchies and priorities, synchronization thresholds, and accuracy rates.

## PTP Commands

Monitor PTP with the following commands. See the {{<link title="show/#netq-show-ptp" text="command line reference">}} for additional options, definitions, and examples.

```
   netq show ptp clock-details
   netq show ptp counters (tx | rx) 
   netq show ptp global-config
   netq show ptp port-status 
```
## Access the PTP Dashboard

1. Select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**.

2. Under the Network section, select **PTP**.

The PTP summary dashboard displays:
- clock count, type, and distribution
- an overview of PTP-related events 
- a summary of PTP violations (mean path delay and offset from master)

{{<figure src="/images/netq/ptp-management-dash-violations-450.png" width="1000">}}

Navigate to the **Events** tab to view, filter, and sort PTP-related events:

{{<figure src="/images/netq/ptp-events-tab-450.png" width="1000">}}

## View PTP on a Switch

1. Select {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in the workbench header, then click **Open a device card**.

2. Select a switch from the dropdown and specify the large card.

3. Hover over the top of the card and select the PTP icon {{<img src="/images/netq/ptp-icon.png" height="18" width="18">}}:

{{<figure src="/images/netq/updated-ptp-450.png" width="700">}}

4. For more granular data, expand the card to full-size and navigate to PTP:

{{<figure src="/images/netq/updated-ptp-switch-450.png" width="1200">}}

Hover over the chart at any point to display timestamped mean-path-delay and offset-from-master data. You can drag the bottom bar to expand and compress the period of time displayed in the graph. 

Select the tabs above the chart to display information about domains, clocks, ports, and configurations:

{{<figure src="/images/netq/ptp-tabs-450.png" width="700">}}


## Related Information

- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-53/System-Configuration/Date-and-Time/Precision-Time-Protocol-PTP/" text="PTP and Cumulus Linux">}}