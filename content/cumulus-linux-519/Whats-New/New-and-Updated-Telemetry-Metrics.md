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
{{< tab "Platform">}}

|  Name | Description |
|------ | ----------- |
| `/components/component[name]/state/name` | Component instance name. Cumulus Linux 5.19 adds the name for the ASIC and for transceivers. |
| `/components/component[name]/state/type` | OpenConfig component type. Cumulus Linux 5.19 adds the type for the ASIC, transceivers, fans, storage disks, and temperature and leakage sensors. |

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

<!-- REVIEW: the RADIUS tab below. As of the specification's revision 1.1 the OpenTelemetry
     RADIUS_STATS category and the collector label change were both on a branch with the merge
     request not yet opened, so confirm these metrics ship in 5.19 before publishing. The metric
     names and the single `server` label are settled, so only the delivery is in question. Delete
     this comment before publishing. -->

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
{{< tab "RADIUS">}}

|  Name | Description |
|------ | ----------- |
| `node_radius_auth_request_total` | Access-Request packets sent to the RADIUS server to authenticate an interactive user login, including retransmissions. |
| `node_radius_auth_accept_total` | Access-Accept messages received from the RADIUS server. |
| `node_radius_auth_reject_total` | Access-Reject messages received from the RADIUS server. |
| `node_radius_auth_timeout_total` | Access-Request messages that timed out and required retransmission. |
| `node_radius_auth_retransmit_total` | Retransmitted Access-Request messages. |
| `node_radius_auth_connection_error_total` | Login authentication attempts for which the switch could not reach the RADIUS server. |
| `node_radius_auth_bad_response_total` | Malformed or otherwise invalid RADIUS responses received during an interactive login. |

Each metric carries a single `server` label holding the RADIUS server address. For information about the counters behind these metrics, refer to {{<link url="RADIUS-AAA/#show-and-clear-radius-counters" text="Show and Clear RADIUS Counters">}}.

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.

## Updated OTEL Metrics

|  Old Metric | New Metric |
|------ | ----------- |
|
