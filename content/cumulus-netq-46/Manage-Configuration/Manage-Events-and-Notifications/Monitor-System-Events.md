---
title: Monitor Events
author: NVIDIA
weight: 775
toc: 4
---
Use the UI or CLI to monitor events: you can view all events across the entire network or all events on a device, then filter events according to their type, severity, or timeframe.

Refer to {{<link title="Configure System Event Notifications">}} and {{<link title="Configure Threshold-Crossing Event Notifications">}} for information about configuring and managing these events.

Note that in the UI, it can take several minutes for NetQ to process and accurately display network events. The delay is caused by events with multiple network dependencies. It takes between 5 and 10 minutes for NetQ to consolidate and display these events.

## Event Commands

Monitor events with the following command. See the {{<link title="show/#netq-show-events" text="command line reference">}} for additional options, definitions, and examples.

```
netq show events
```

## Monitor Events in the UI

{{<tabs "TabID29" >}}

{{<tab "NetQ UI" >}}

1. Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" height="18" width="18">}} **Menu**, then select **Events**.

    The dashboard presents a timeline of events alongside the devices that are causing the most events. 

    {{<figure src="/images/netq/events-full-460.png" width="1200" alt="Events dashboard with networkwide error and info events.">}}

  Use the controls above the summary to filter events by time, device (hostname), type, severity, or state.

  {{<figure src="/images/netq/event-controls-460.png" width="500" alt="">}}

  Select the tabs below the controls to display all events networkwide, interface events, network services events, system events, or threshold-crossing events. The charts and tables update according to the tab you've selected. In this example, the TCA tab is selected; the chart and tables update to reflect only threshold-crossing events:

      {{<figure src="/images/netq/tca-events-full-460.png" width="1200" alt="Events dashboard with networkwide error and info events.">}}

 If you are receiving too many event notifications, you can create rules to suppress events. Select **Show suppression rules** in the top-right corner to view rules that prevent NetQ from displaying an event message. Refer to {{<link title="Configure System Event Notifications#suppress-events" text="Configure System Event Notifications">}} for information about event suppression.

  Events are also generated when streaming {{<link title="Validate Overall Network Health" text="validation checks">}} detect a failure. If an event is generated from a failed validation check, it will be marked resolved automatically the next time the check runs successfully.