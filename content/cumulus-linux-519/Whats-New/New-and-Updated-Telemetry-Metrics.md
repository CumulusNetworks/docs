---
title: New and Updated Telemetry Metrics
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.19"
toc: 1
---
The following tables list the new, updated, and deprecated gNMI and OTEL metrics in Cumulus Linux 5.19.

## New gNMI Metrics

For information about gNMI, refer to {{<link url="gNMI-Streaming" text="gNMI Streaming">}}.

## New OTEL Metrics

{{< tabs "TabID113 ">}}
{{< tab "WJH">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_wjh_total_events` | The total number of WJH drop-trap events received on the channel, before aggregation. |
| `nvswitch_wjh_channel_trigger` | Which triggers are enabled for each channel.|

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.

## Updated OTEL Metrics

|  Old Metric | New Metric |
|------ | ----------- |
|
