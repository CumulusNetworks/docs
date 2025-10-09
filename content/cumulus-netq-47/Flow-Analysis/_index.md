---
title: Flow Analysis
author: NVIDIA
weight: 1006
toc: 4
---
Create a flow analysis to sample data from TCP and UDP flows in your environment and to review latency and buffer utilization statistics across network paths.

<!-- vale off -->
{{<notice info>}}

Flow analysis is supported on NVIDIA Spectrum-2 switches and above. It requires a switch fabric running Cumulus Linux version 5.0 or above.

You must enable {{<link title="Lifecycle Management" text="Lifecycle Management">}} (LCM) to run a flow analysis. If LCM is disabled, you will not see the flow analysis icon in the UI. LCM is enabled for on-premises deployments by default and disabled for cloud deployments by default. Contact your local NVIDIA sales representative or submit a support ticket to activate LCM on cloud deployments.

{{</notice>}}
<!-- vale on -->
## Create a New Flow Analysis

To start a new flow analysis, click the **Flow analysis** icon and select **Create new flow analysis**.

{{<figure src="/images/netq/flow-analysis-select-icon-450.png" alt="flow analysis menu with options to create a new flow analysis or view a previous analysis" width="350">}}

In the dialog, enter the application parameters, including the source IP address, destination IP address, source port, and destination port of the flow you wish to analyze. Select the protocol and VRF for the flow from the dropdown menus.

{{<figure src="/images/netq/create-new-flow-450.png" alt="flow analysis wizard prompting user to enter application parameters" width="600">}}

After you enter the application parameters, enter the monitor settings, including the sampling rate and time parameters.

{{<figure src="/images/netq/flow-monitor-params.png" alt="flow analysis wizard prompting user to enter sampling and scheduling information" width="600">}}

If you attempt to run a flow analysis that includes switches assigned a default, unmodified access profile, the process will fail. {{<link title="Credentials and Profiles" text="Create a unique access profile">}} (or update the default profile with unique credentials), then {{<link title="Switch Management/#assign-a-profile-to-a-switch" text="assign the profile">}} to the switches you want to include in the flow analysis.

{{<notice warning>}}

Running a flow analysis will affect switch CPU performance. For high-volume flows, set a lower sampling rate to limit switch CPU impact. 

{{</notice>}}

## View Flow Analysis Data

After starting the flow analysis, a flow analysis card will appear on the NetQ Workbench.

{{<figure src="/images/netq/flow-analysis-card.png" alt="flow analysis card showing that a flow analysis is in progress" width="550">}}

View a previous flow analysis by selecting **Flow analysis** and **View previous flow analysis**. 

{{<figure src="/images/netq/flow-analysis-view-previous.png" alt="flow analysis menu with the option to view previous flow analysis highlighted" width="350">}}

Select **View details** next to the name of the flow analysis to display the analysis dashboard. You can use this dashboard to view latency and buffer statistics for the monitored flow. If bi-directional monitoring was enabled, you can view the reverse direction of the flow by selecting the {{<img src="/images/netq/reverse-toggle.svg" height="18" width="18">}} icon. The following example shows flow data across a single path:

{{<figure src="/images/netq/flow-analysis-dashboard.png" alt="flow analysis dashboard displaying flow data across a single path" width="1000">}}

The dashboard header shows the monitored flow settings:

{{<figure src="/images/netq/monitored-flow-details.png" alt="dashboard header displaying settings and paramters selected with the flow analysis wizard" width="1600">}}

| Flow Settings | Description |
| --------------- | ------- |
| Lifetime | The lifetime of the flow analysis. This example completed in 11 minutes. |
| Source IP | The source IP address of the flow. In this example it is 10.1.100.125. |
| Destination IP | The destination IP address of the flow. In this example it is 10.1.10.105. |
| Source Port | The source port of the flow. In this example it displays N/A because it was not set. |
| Destination Port | The destination port of the flow. In this example it is 2222. |
| Protocol | The protocol of the monitored flow. In this example it is UDP. |
| Sampling Rate | The sampling rate of the flow. In this example it is low. |
| VRF | The VRF the flow is present in. In this example it is the default VRF. |
| Bi-directional Monitoring | This determines if the flow is monitored in both directions between the source IP address and the destination IP address. In this example it is enabled. Click {{<img src="/images/netq/reverse-toggle.svg" height="18" width="18">}} to change the direction that is displayed.|

### Understanding the Flow Analysis Graph

The flow analysis graph is color coded relative to the values measured across devices. Lower values are displayed in green, and higher values are displayed in orange. The color gradient is displayed below the graph along with the low and high values from the collected flow data. Each hop in the path is represented in the graph with a vertical, gray-striped line labeled by hostname. The following example shows a single path:

{{<figure src="/images/netq/single-path-graph.png" alt="single-path flow analysis with five hops ranging from low to high values" width="800">}}

The flow graph panel on the right side of the dashboard displays the devices along the selected path.

{{<figure src="/images/netq/flow-graph-single-path.png" alt="flow graph panel showing the five devices associated with the flow analysis graph" width="200">}}

### View Flow Latency

The latency measured by the flow analysis is the total transit time of the sampled packets through individual devices. A summary of measured latency for each device is displayed above the main flow analysis graph.

{{<figure src="/images/netq/per-device-latency-summary.png" alt="three devices displaying their average latencies, including minimum, maximum and P95 value." width="600">}}

The average latency for packets in the flow is displayed under the hostname of each device, along with the minimum and maximum latencies observed during the analysis lifetime. The 95th percentile (P95) latency value for sampled packets is also displayed. The P95 calculation means that 95% of the sampled packets have a latency value less than or equal to the calculation.

Use your cursor to hover over sections of the main analysis graph to view average latency values for each device in a path.

{{<figure src="/images/netq/latency-hover-1.png" alt="cursor hovering over a device to show latency values" width="800">}}

The left panel of the flow analysis dashboard also displays a timeline of measured latency for each device on that path. Use your cursor to hover over the plotted data points on the timeline for each device to view the latency measured at each time interval.

{{<figure src="/images/netq/latency-left-panel.png" alt="a cursor hovering over a device's timeline showing maximum, minimum, and average latency at 6:15 AM on November 24th 2021"  width="600">}}
### View Buffer Occupancy

The main flow analysis dashboard also displays the buffer occupancy of each device along the path. To change the graph view to display buffer occupancy for the flow, click {{<img src="/images/netq/arrow-down-1.svg" height="18" width="18">}} next to **Avg. flow latency** and select **Avg. buffer occupancy**. You can view an overview graph of buffer occupancy or select each device to see the buffer occupancy for the analyzed flow:

{{<figure src="/images/netq/buffer-occupancy-main-42.png" alt="overview graph displaying average buffer occupancy between 8 total devices" width="900">}}

The percentages represent the amount of buffer space on the switch that the analyzed flow occupied while the analysis was running.

{{<figure src="/images/netq/buffer-occupancy-hover-42.png" alt="buffer occupancy displaying percentages at 0" width="400">}}


### View Multiple Paths

When packets matching the flow settings traverse multiple paths in the topology, the flow graph displays latency and buffer occupancy for each path:

{{<figure src="/images/netq/flow-analysis-multipath-example-42.png" alt="flow graph displaying multiple paths along with latency and buffer-occupancy data along those paths" width="1000">}}

You can switch between paths by clicking on an alternate path in the **Flow graph** panel, or by clicking on an unselected path on the main analysis graph:

{{<figure src="/images/netq/flow-multipath-flowgraph-410.png" alt="flow graph panel highlighting a selected path with several unselected paths also displayed" width="200">}}

 In the detail panel on the left side of the dashboard, you can select a path to view the percent of packets distributed over each path.

{{<figure src="/images/netq/flow-analysis-select-path-42.png" alt="a selected path showing that 50.1% of packets are distributed over that path" width="600">}}

### Partial Path Support

Some flows can still be analyzed if they traverse a network path that includes switches lacking flow analysis support. Partial-path flow analysis is supported in the following conditions:

- The unsupported device cannot be the initial ingress or terminating egress device in the path of the analyzed flow.
- If there is more than one consecutive transit device in the path that lacks flow analysis support, the path discovery will terminate at that point in the topology and some devices will not be displayed in the flow graph.

An unsupported device is represented in the flow analysis graph as a black bar lined with red x's. Flow statistics are not displayed for that device.

{{<figure src="/images/netq/partial-path-overview-42.png" alt="flow analysis graph showing an unsupported switch" width="900">}}

Unsupported devices are also designated in the flow graph panel:

{{<figure src="/images/netq/partial-path-flow-graph-42.png" alt="flow graph panel with an unsupported switch" width="200">}}

Selecting the unsupported device displays device statistics in the left panel if they are available to NetQ. Otherwise, the display will indicate why the device is not supported:

{{<figure src="/images/netq/partial-path-device-stats-unsupported-42.png" alt="a panel showing an unsupported device. The device is not supported because the CL version is not supported for flow analysis" width="400">}}

Path discovery will terminate if multiple consecutive switches do not support flow analysis.  When additional data is available from switches outside of discovered paths, you can view data from those devices from the menu at the top of the page:

{{<figure src="/images/netq/undiscovered-paths-devices-dropdown.png" alt="menu displaying three unsupported devices" width="400">}}

The left panel displays the data, along with ingress and egress ports.
## View Device Statistics

You can view latency, buffer occupancy, interface statistics, resource utilization, and WJH events for each device by clicking on a device in the **Flow Graph** panel, or by clicking on the line associated with a device in the main flow analysis graph. The left panel will then update to reflect statistics for the respective device.

{{<figure src="/images/netq/device-stats-latency-view-42.png" alt="panel displaying statistics of a selected device" width="500">}}

After selecting a device, click {{<img src="/images/netq/device-stats-expand-chart-icon-42.png" height="18" width="18">}} to expand the statistics chart:

{{<figure src="/images/netq/device-stats-expand-chart-42.png" alt="a cursor hovering over an icon that, when selected, expands the chart" width="500">}}

In this view, you can select additional categories to add to the chart:

{{<figure src="/images/netq/device-stats-expanded-chart-stats-42.png" alt="expanded chart displaying latency and WJH data, with buffer occupancy and total packet unselected and therefore not dispayed" swidth="900">}}

The **Flow Graph** panel allows you to access the topology view, where you can also click the paths and devices to view statistics. Click **View in topology** to switch to the topology view.

{{<figure src="/images/netq/flow-topology-view-410.png" alt="topology view showing both selected and unselected devices and their paths" width="600">}}


### View WJH Events

Flow analysis monitors the path for WJH events and records any drops for the flow. Switches with WJH events recorded are represented in the flow analysis graph as a red bar with white stripes. Hover over the device to see a WJH event summary:

{{<figure src="/images/netq/wjh-flow-graph-overview-42.png" alt="a user hovering over a device in the main flow analysis graph with a WJH event summary showing 94,300 total packet drops" width="900">}}

You can also view devices with WJH events in the flow graph panel:

{{<figure src="/images/netq/wjh-flow-graph-hover-42.png" alt="a user hovering over a device in the flow graph panel with a WJH event summary showing 94,300 total packet drops" width="300">}}

Click on a device with WJH events to see the statistics in the left panel. Hover over the data to reveal the type of drops over time:

{{<figure src="/images/netq/wjh-device-stats-hover-42.png" alt="invdividual device WJH statistics showing 2673 router drops" width="400">}}

WJH drops can also be viewed from the expanded device chart by selecting the WJH category:

{{<figure src="/images/netq/wjh-larger-chart-hover-42.png" alt="expanded device chart showing WJH data of 24 total router drops" width="600">}}

Select **Show all drops** to display a list of all WJH drops for the device:

{{<figure src="/images/netq/wjh-all-drops-panel-42.png" alt="WJH statistics for all drops, including tabular information on count, drop type, drop reason, severity, and corrective action" width="600">}}

<!-- hiding this until the simulation works
## Related Information

You can run a flow analysis in a simulated environment with NVIDIA Air. Launch the {{<exlink url="https://air.nvidia.com/marketplace?demo_id=649868d2-8c6c-4817-a4c3-fc904f4b0f8f" text="flow analysis demo">}} to try it out.

-->