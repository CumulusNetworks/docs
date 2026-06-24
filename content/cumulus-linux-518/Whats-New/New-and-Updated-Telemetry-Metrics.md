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
{{< tab "BGP">}}

|  Name | Description |
|------ | ----------- |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/state/enabled`| The admin status of the BGP peer (up or down). |
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/afi-safis/afi-safi[afi-safi-name]/state/prefixes/received-pre-policy`| The number of prefixes received from the peer before applying any policies.<br><br>The pre-policy count requires soft-reconfiguration inbound to be enabled for the peer (`nv set vrf default router bgp neighbor <neighbor-id> address-family <address-family> soft-reconfiguration enabled`).|

{{< /tab >}}
{{< tab "WJH">}}

|  Name | Description |
|------ | ----------- |
| `/wjh/channels/channel[name]/aggregate-events` | |
| `/wjh/channels/channel[name]/l1-events` | |
| `/wjh/channels/channel[name]/state` | |

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

## Deprecated gNMI Metrics

|  Name | Description |
|------ | ----------- |
| `interfaces/interface[name]/wjh/aggregate/l1` | |
| `interfaces/interface[name]/wjh/aggregate/l2/` | |
| `/interfaces/interface[name]/wjh/aggregate/router` | |
| `/interfaces/interface[name]/wjh/aggregate/tunnel` | |
| `/interfaces/interface[name]/wjh/aggregate/buffer` | |

For information about gNMI, refer to {{<link url="gNMI-Streaming" text="gNMI Streaming">}}.

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
{{< tab "BGP">}}

|  Name | Description |
|------ | ----------- |
| `nvrouting_bgp_peer_enabled` | The admin status of the BGP peer (up or down). |
| `nvrouting_bgp_peer_rib_adj_in_pre_policy` | The number of prefixes received from the peer before applying any policies.<br><br>The pre-policy count requires soft-reconfiguration inbound to be enabled for the peer (`nv set vrf default router bgp neighbor <neighbor-id> address-family <address-family> soft-reconfiguration enabled`).|

{{< /tab >}}
{{< tab "WJH">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_wjh_total_events_channel_forwarding` |  |
| `nvswitch_wjh_total_events_channel_acl` | |
| `nvswitch_wjh_total_events_channel_buffer` | |

{{< /tab >}}
{{< tab "">}}

|  Name | Description |
|------ | ----------- |


{{< /tab >}}
{{< tab "">}}

|  Name | Description |

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.
