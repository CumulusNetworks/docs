---
title: PTP
author: NVIDIA
weight: 930
toc: 3
---

{{<notice note>}}

PTP monitoring is an early access feature and is supported on NVIDIA Spectrum 2 and 3 platforms. It requires a switch fabric running Cumulus Linux version 5.0 or above.

{{</notice>}}

Use the UI or CLI to monitor PTP (Precision Time Protocol) in your network.

## PTP Commands

PTP commands include:

```
   netq [<hostname>] show ptp clock-details 
    [around <text-time>] 
    [json]
   
   netq [<hostname>] show ptp global-config 
    [around <text-time>] 
    [json]

   netq [<hostname>] show ptp port-status [<text-port>] 
    [around <text-time>] 
    [json]

   netq [<hostname>] show ptp counters [<text-port>]
    tx | rx 
   [around <text-time>] 
   [json]
```

See the {{<link title="show/#netq-show-ptp" text="command line reference">}} for additional details and examples.

## Access the PTP Dashboard

1. Select {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu.

2. Under the **Network** heading, select **PTP**.

The PTP summary dashboard displays:
- clock count, type, and distribution
- an overview of PTP-related events 
- a summary of PTP violations (mean path delay and offset from master)

{{<figure src="/images/netq/ptp-management-dash-violations-450.png" width="1000">}}

Navigate to the **Events** tab to view, filter, and sort PTP-related events:

{{<figure src="/images/netq/ptp-events-tab-450.png" width="1000">}}

## View PTP on a Switch

1. Select {{<img src="/images/netq/devices.svg" height="18" width="18">}} Devices in the workbench header, then click **Open a device card**.

2. Select a switch from the dropdown and specify the large card.

3. Hover over the top of the card and select the PTP icon {{<img src="/images/netq/ptp-icon.png" height="18" width="18">}}:

{{<figure src="/images/netq/ptp-large-450.png" width="600">}}

4. For more granular data, expand the card to full-size and navigate to PTP:

{{<figure src="/images/netq/full-screen-ptp-450.png" width="1000">}}

Hover over the chart at any point to display timestamped mean-path-delay and offset-from-master data. You can drag the bottom bar to expand and compress the period of time displayed in the graph. 

Select the tabs above the chart to display information about domains, clocks, ports, and configurations:

{{<figure src="/images/netq/ptp-tabs-450.png" width="600">}}





## Related Information

- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux-53/System-Configuration/Date-and-Time/Precision-Time-Protocol-PTP/" text="PTP and Cumulus Linux">}}