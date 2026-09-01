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

<!-- REVIEW: the specification gives only native FRR xpaths for these metrics, and its Scope section
     says "gNMI subscription using native FRR xpaths". Its High-Level Interactions section, which the
     specification itself labels "(for context)", instead says the gNMI agent translates an
     OpenConfig xpath into the FRR-native one, which would mean the client subscribes to something
     else. Resolved by section role: the XPaths table is the only place that names the identifiers,
     so the native form below is what the draft emits. Every other gNMI path in this release is
     OpenConfig, so confirm this against a candidate build. Delete this comment before publishing. -->

{{< tabs "TabID114 ">}}
{{< tab "Routing">}}

|  Name | Description |
|------ | ----------- |
| `/frr-bgp-peer:lib/vrf[id=<vrf-id>]/ipv4-unreach-prefix-count` | Number of IPv4 prefixes in the BGP unreachability table. |
| `/frr-bgp-peer:lib/vrf[id=<vrf-id>]/ipv6-unreach-prefix-count` | Number of IPv6 prefixes in the BGP unreachability table. |
| `/frr-zebra:lib/vrf[id=<vrf-id>]/ipv4-lldp-exception/exception-count` | Number of unreachable IPv4 prefixes the switch holds to export to LLDP, excluding the default route exception. |
| `/frr-zebra:lib/vrf[id=<vrf-id>]/ipv4-lldp-exception/default-exception-active` | Whether the IPv4 default route exception is active. |
| `/frr-zebra:lib/vrf[id=<vrf-id>]/ipv6-lldp-exception/exception-count` | Number of unreachable IPv6 prefixes the switch holds to export to LLDP, excluding the default route exception. |
| `/frr-zebra:lib/vrf[id=<vrf-id>]/ipv6-lldp-exception/default-exception-active` | Whether the IPv6 default route exception is active. |
| `/frr-zebra:lib/lldp-export-stats/exception-add-total` | Number of unreachable prefixes sent to LLDP since the routing service started, including resynchronization replays. |
| `/frr-zebra:lib/lldp-export-stats/exception-remove-total` | Number of unreachable prefix withdrawals sent to LLDP since the routing service started. |
| `/frr-zebra:lib/lldp-export-stats/default-exception-add-total` | Number of default route exceptions sent to LLDP since the routing service started, counted separately for each VRF and address family. |
| `/frr-zebra:lib/lldp-export-stats/default-exception-remove-total` | Number of default route exception withdrawals sent to LLDP since the routing service started. |
| `/frr-zebra:lib/debug/lldp-export-channel/connected` | Whether the LLDP export channel is up. |
| `/frr-zebra:lib/debug/lldp-export-channel/errors-total` | Number of unreachable prefix updates that failed to reach LLDP since the routing service started. |

{{< /tab >}}
{{< /tabs >}}

For information about gNMI, refer to {{<link url="gNMI-Streaming" text="gNMI Streaming">}}.

## New OTEL Metrics

<!-- REVIEW: the specification's title page states GA for 5.19, but its feature-request table gives
     the release scope as "CL 5.18.0 (GA)" for the same FR. Confirm the release and quality level
     against the 5.19 Redmine execution query. Note also that
     nvrouting_lldp_default_exception_active_count reports a boolean but carries a _count suffix,
     while nvrouting_lldp_export_channel_connected reports a boolean with no suffix; both names are
     drafted exactly as the specification gives them. Delete this comment before publishing. -->

{{< tabs "TabID113 ">}}
{{< tab "WJH">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_wjh_total_events` | The total number of WJH drop-trap events received on the channel, before aggregation. |
| `nvswitch_wjh_channel_trigger` | Which triggers are enabled for each channel.|

{{< /tab >}}
{{< tab "Routing">}}

|  Name | Description |
|------ | ----------- |
| `nvrouting_bgp_unreach_prefix_count` | Number of prefixes in the BGP unreachability table. |
| `nvrouting_lldp_exception_count` | Number of unreachable prefixes the switch holds to export to LLDP, excluding the default route exception. |
| `nvrouting_lldp_default_exception_active_count` | Whether the default route exception is active. |
| `nvrouting_lldp_exception_add_total` | Number of unreachable prefixes sent to LLDP since the routing service started, including resynchronization replays. |
| `nvrouting_lldp_exception_remove_total` | Number of unreachable prefix withdrawals sent to LLDP since the routing service started. |
| `nvrouting_lldp_default_exception_add_total` | Number of default route exceptions sent to LLDP since the routing service started, counted separately for each VRF and address family. |
| `nvrouting_lldp_default_exception_remove_total` | Number of default route exception withdrawals sent to LLDP since the routing service started. |
| `nvrouting_lldp_export_channel_connected` | Whether the LLDP export channel is up. |
| `nvrouting_lldp_export_channel_errors_total` | Number of unreachable prefix updates that failed to reach LLDP since the routing service started. |

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.

## Updated OTEL Metrics

|  Old Metric | New Metric |
|------ | ----------- |
|
