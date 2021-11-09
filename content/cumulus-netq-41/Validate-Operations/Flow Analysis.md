---
title: Flow Analysis
author: NVIDIA
weight: 1006
toc: 4
---
NetQ provides the ability to analyze active traffic flows in your network. Use the Flow Analysis tool to sample data from TCP and UDP flows in your environment and review latency and buffer utilization statistics across network paths.

{{<notice info>}}

Flow Analysis is supported on NVIDIA Spectrum 2 and 3 platforms, and requires a switch fabric running Cumulus Linux version 5.0 or above.

{{</notice>}}

## Create New Flow Analysis

To start a new flow analysis, click on the **Flow Analysis** menu and select **Create New Flow Analysis**:

{{<figure src="/images/netq/new-flow-analysis.png" width="350">}}

## Flow Analysis Settings

The new flow analysis wizard will prompt you to enter the source IP address, destination IP address, source port, VRF, destination port, and protocol of the flow you wish to analyze. The only optional parameter is the source port, for when the ephemeral source port of a flow may be unknown.

{{<figure src="/images/netq/flow-analysis-app-params.png" width="600">}}

## Flow Monitor Settings

The monitor settings will determine how long to sample a flow, when the sampling should be scheduled, whether the sampling should be bidirectional across the network path(s), and the sampling rate for the flow.

{{<figure src="/images/netq/flow-monitor-params.png" width="600">}}

## View Flow Analysis Data

After starting the flow analysis, a flow analysis card will appear on the NetQ Workbench.

{{<figure src="/images/netq/flow-analysis-card.png" width="550">}}

Collected flow analysis data can also be viewed by selecting **Flow Analysis** and **View Previous Flow Analysis** 

{{<figure src="/images/netq/flow-analysis-view-previous.png" width="350">}}

You can select **View details** next to the name of the flow analysis to bring up the analysis dashboard. You can use this dashboard to view latency and buffer statistics for the monitored flow. If bidirectional monitoring for the flow was enabled, you can view the reverse direction of the flow by using the {{<img src="/images/netq/reverse-toggle.svg" height="18" width="18">}} icon.

{{<figure src="/images/netq/flow-analysis-dashboard.png" width="800">}}

