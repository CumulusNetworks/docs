---
title: PTP
author: NVIDIA
weight: 930
toc: 3
---

Use the UI or CLI to monitor Precision Time Protocol (PTP), including clock hierarchies and priorities, synchronization thresholds, and accuracy rates.

{{<notice note>}}

PTP monitoring is only supported on Spectrum switches running Cumulus Linux version 5.0.0 or later.

{{</notice>}}

## PTP Commands

- {{<link title="show/#netq-show-ptp" text="netq show ptp">}}
- {{<link title="show/#netq-show-events" text="netq show events message_type ptp">}}
- {{<link title="show/#netq-show-events-config" text="netq show events-config message_type ptp">}} 

## Access the PTP Dashboard

From the header or {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} Menu, select **Spectrum-X**, then **PTP**.

The PTP summary dashboard displays:
- clock count, type, and distribution
- an overview of PTP-related events 
- a summary of PTP violations (mean path delay and offset from master)

{{<figure src="/images/netq/ptp-dashboard-460.png" alt="PTP summary screen displaying grandmaster clock details, events total, and violations summary" width="1100">}}

Navigate to the **Events** tab to view, filter, and sort PTP-related events:

{{<figure src="/images/netq/ptp-events-dash-460.png" alt="detailed display of 133 PTP events, including list of devices with PTP-related events" width="1100">}}

## View PTP on a Switch

1. Search for the device’s hostname in the global search field or from the header select <img src="https://icons.cumulusnetworks.com/44-Entertainment-Events-Hobbies/02-Card-Games/card-game-diamond.svg" height="18" width="18"/> **Add card&nbsp;<span aria-label="and then">></span> Device card**.

2. Select a switch and specify the large card.

3. Hover over the top of the card and select the {{<img src="/images/netq/ptp-icon.png" height="18" width="18">}} **PTP** tab:

{{<figure src="/images/netq/updated-ptp-450.png" alt="large switch card with PTP display selected" width="700">}}

4. For more granular data, expand the card to full-size and navigate to {{<img src="/images/netq/ptp-icon.png" height="18" width="18">}} **PTP**:

{{<figure src="/images/netq/updated-ptp-switch-450.png" alt="full screen graph of a switch's average offsest-from-master and average mean-path-delay statistics" width="1200">}}

Hover over the chart at any point to display timestamped mean-path-delay and offset-from-master data. You can drag the bottom bar to expand and compress the period of time displayed in the graph. 

Select the tabs above the chart to display information about domains, clocks, ports, and configurations:

{{<figure src="/images/netq/ptp-tabs-450.png" alt="clock domain, identiy, port, and quality information for the grandmaster clock" width="700">}}


## Related Information

- {{<exlink url="https://docs.nvidia.com/networking-ethernet-software/cumulus-linux/System-Configuration/Date-and-Time/Precision-Time-Protocol-PTP/" text="PTP and Cumulus Linux">}}