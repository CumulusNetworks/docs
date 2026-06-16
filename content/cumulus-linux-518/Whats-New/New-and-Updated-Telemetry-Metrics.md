---
title: New and Updated Telemetry Metrics
author: Cumulus Networks
weight: -30
product: Cumulus Linux
version: "5.18"
toc: 1
---
The following tables list the new, updated, and deprecated gNMI and OTEL metrics in Cumulus Linux 5.18.

## New gNMI Metrics

{{< tabs "TabID13 ">}}
{{< tab "ASIC">}}

|  Name | Description |
|------ | ----------- |
| `/components/component/integrated-circuit/utilization/resources/resource[name=<resource_name>] /state/used` | | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=< resource_name>]/state/free` | |
`/components/component/integrated-circuit/utilization/resources/resource[name=< resource_name>]/state/max-limit` | |
| `/components/component/integrated-circuit/utilization/resources/resource[name=< resource_name>] /state/high-watermark` | | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=< resource_name>] /state/last-high-watermark` | | 

{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< tab " ">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< /tabs >}}

## New OTEL Metrics

{{< tabs "TabID190 ">}}
{{< tab "ASIC">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_asic_resource_used` | | 
| `nvswitch_platform_asic_resource_free` | | 
| `nvswitch_platform_asic_resource_max_limit` | |
| `nvswitch_platform_asic_resource_high_watermark` | | 
| `nvswitch_platform_asic_resource_high_watermark_timestamp` | | 

{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |

{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< tab "">}}

|  Name | Description |

{{< /tab >}}
{{< /tabs >}}

## Updated OTEL Metrics

|  Old Name | New Name |
|------ | ----------- |
