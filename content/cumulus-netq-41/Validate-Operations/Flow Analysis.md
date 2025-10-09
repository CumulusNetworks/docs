---
title: Flow Analysis
author: NVIDIA
weight: 1006
toc: 4
---
NetQ provides the ability to analyze active traffic flows in your network. Use the Flow Analysis tool to sample data from TCP and UDP flows in your environment and review latency and buffer utilization statistics across network paths.

<!-- vale off -->
{{<notice info>}}

Flow Analysis is supported on NVIDIA Spectrum 2 and 3 platforms, and requires a switch fabric running Cumulus Linux version 5.0 or above.

{{</notice>}}
<!-- vale on -->
## Create New Flow Analysis

To start a new flow analysis, click the **Flow Analysis** menu and select **Create New Flow Analysis**:

{{<figure src="/images/netq/new-flow-analysis.png" width="350">}}

{{<notice note>}}

Flow Analysis requires {{<link title="Manage Switches through Their Lifecycle" text="Lifecycle Management">}} (LCM) to be enabled. The Flow Analysis menu on the workbench will not be visisble when LCM is disabled. LCM is enabled for on-premises deployments by default and disabled for cloud deployments by default. Contact your local NVIDIA sales representative or submit a support ticket to activate LCM on cloud deployments.

{{</notice>}}

### Flow Analysis Settings

The Flow Analysis wizard will prompt you to enter the source IP address, destination IP address, source port, VRF, destination port, and protocol of the flow you wish to analyze. The only optional parameter is the source port, for when the ephemeral source port of a flow may be unknown:

{{<figure src="/images/netq/flow-analysis-app-params.png" width="600">}}

### Flow Monitor Settings

The monitor settings will determine how long to sample a flow, when the sampling should be scheduled, whether the sampling should be bidirectional across the network path(s), and the sampling rate for the flow:

{{<figure src="/images/netq/flow-monitor-params.png" width="600">}}

{{<notice warning>}}

Flow Analysis is impactful to switch CPU during the flow monitor liftime. For high volume flows, it is recommended to set a lower sampling rate for flow analysis to limit switch CPU impact. 

{{</notice>}}

## View Flow Analysis Data

After starting the flow analysis, a flow analysis card will appear on the NetQ Workbench.

{{<figure src="/images/netq/flow-analysis-card.png" width="550">}}

Collected flow analysis data can also be viewed by selecting **Flow Analysis** and **View Previous Flow Analysis** 

{{<figure src="/images/netq/flow-analysis-view-previous.png" width="350">}}

You can select **View details** next to the name of the flow analysis to bring up the analysis dashboard. You can use this dashboard to view latency and buffer statistics for the monitored flow. If bidirectional monitoring for the flow was enabled, you can view the reverse direction of the flow by using the {{<img src="/images/netq/reverse-toggle.svg" height="18" width="18">}} icon. The following example shows flow data across a single path:

{{<figure src="/images/netq/flow-analysis-dashboard.png" width="800">}}

The dashboard header shows the monitored flow settings:

{{<figure src="/images/netq/monitored-flow-details.png" width="1600">}}

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

The flow analysis graph is color coded relative to the values measured across devices. Lower values are displayed in green, and higher values are displayed in orange. The color gradient is displayed below the graph along with the low and high values from the collected flow data. Each hop in the path is represented in the graph with a vertical grey-striped line labeled by hostname. The following example shows a single path:

{{<figure src="/images/netq/single-path-graph.png" width="800">}}

The Flow Graph panel on the right side of the dashboard will display the devices along the selected path:

{{<figure src="/images/netq/flow-graph-single-path.png" width="200">}}

### View Flow Latency

The latency measured by Flow Analysis is the total transit time of sampled packets through individual devices. A summary of measured latency for each device is displayed above the main Flow Analysis graph:

{{<figure src="/images/netq/per-device-latency-summary.png" width="600">}}

The average latency for packets in the flow is displayed under the hostname of each device, along with the minimum and maximum latencies observed during the analysis lifetime. The 95th percentile (P95) latency value for sampled packets is also displayed. The P95 calculation represents the latency value that 95 percent of the sampled packets is lower than for the analysed flow.

You can also use your cursor to hover over sections of the main analysis graph to view average latency values for each device in a path:

{{<figure src="/images/netq/latency-hover-1.png" width="800">}}

The left panel of the Flow Analysis dashboard also displays a timeline of measured latency for each device on that path. You can use your cursor to hover over the plotted data points on the timeline for each device to view the latency measured at each time interval:

{{<figure src="/images/netq/latency-left-panel.png" width="600">}}
### View Buffer Occupancy

The main Flow Analysis dashboard also displays the buffer occupancy of each device along the path. To change the graph view to display buffer occupancy for the flow, click {{<img src="/images/netq/arrow-down-1.svg" height="18" width="18">}} next to **Avg. flow latency** and select **Avg. buffer occupancy**. You can hover over each section to see the average buffer utilization for each device:

{{<figure src="/images/netq/buffer-occupancy-main2.png" width="1000">}}

### View Multiple Paths

When packets matching the flow settings traverse multiple paths in the topology, the flow graph will display latency and buffer occupancy for each path:

{{<figure src="/images/netq/flow-multipath-demo-410.png" width="800">}}

You can switch between paths by clicking on an alternate path in the **Flow Graph** panel, or by clicking on an unselected path on the main analysis graph:

{{<figure src="/images/netq/flow-multipath-flowgraph-410.png" width="200">}}

You can also select the desired path and view the amount of packets distributed over each path on the detail panel on the left side of the dashboard:

{{<figure src="/images/netq/flow-multipath-pathselection-410.png" width="600">}}
### View Device Statistics

You can view interface statistics, resource utilization, and alarms for each device by clicking on a device in the **Flow Graph** panel, or by clicking on the striped grey line associated with a device in the main flow analysis graph. This will change the left panel details to show statistics for that device:

{{<figure src="/images/netq/device-statistics-left-panel.png" width="600">}}

The **Flow Graph** panel also presents the option to bring up the topology view where you can also click the paths and devices to view statistics. Click {{<img src="/images/netq/flow-view-in-topology-410.png" height="29" width="141">}} to bring up the topology view:

{{<figure src="/images/netq/flow-topology-view-410.png" width="600">}}



