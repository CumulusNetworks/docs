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
{{< tab "802.1X RADIUS Server">}}

|  Name | Description |
|------ | ----------- |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-requests` | Number of authentication access requests that the switch sends to this server for 802.1x. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/retried-access-requests` | Number of RADIUS Access-Request packets that the switch retransmits to this RADIUS server. The Counter is cumulative across all 802.1x interfaces communicating with this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/timeout-access-requests` |  Number of authentication timeouts to this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-accepts` | Number of RADIUS Access-Accept packets (valid or invalid) received from this server. | 
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-rejects` | Number of RADIUS Access-Reject packets (valid or invalid) received from this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-challenges` | Number of RADIUS Access-Challenge packets (valid or invalid) received from this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-malformed-responses` | Number of malformed RADIUS Access-Response packets received from this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-bad-authenticators` | Number of RADIUS Access-Response packets containing invalid authenticators or signature attributes received from this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-unknown-types` | Number of RADIUS packets of unknown type received from this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-packets-dropped` | Packets that are dropped either because the UDP frame is too big (more than 4100 bytes) or because the parsed reply has no matching pending request. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-connection-errors` | Number of failures encountered when trying to reach the radius server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-receive-errors` | Error on the recv() call when trying to fetch the RADIUS server response on the per 802.1x interface. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-vrf-bind-errors` | Number of failures binding the socket to the configured VRF for this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-initialization-errors` |  Number of failures (re)initializing the local RADIUS transport on behalf of this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/access-out-queue-drops` | Number of outbound RADIUS requests to this server not be retained on the local retransmit queue. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/access-pending-requests` | Number of RADIUS Access-Request packets destined for this server that have not yet received a response or been removed from the retransmit list after the maximum number of retransmit attempts.|
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/access-round-trip-time` | Round-trip time, in milliseconds, between the most recent Access-Request sent to this server and the corresponding Access-Response received.|
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-requests` | Number of RADIUS Accounting-Request packets that the switch sends to this RADIUS server for 802.1x related session events. The counter is cumulative across all 802.1x interfaces communicating with this server. |
| /`system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-start-requests` | Number of RADIUS Accounting-Request packets that the switch sends to this RADIUS server with Acct-Status-Type = Start (per-station session start). The counter is cumulative across all 802.1x interfaces communicating with this server. | 
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-interim-update-requests` | Number of RADIUS Accounting-Request packets that the switch sends to this RADIUS server with Acct-Status-Type = Interim-Update (mid-session updates, driven by the accounting interim interval). The counter is cumulative across all 802.1x interfaces communicating with this server. | 
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-stop-requests` | Number of RADIUS Accounting-Request packets that the switch sends to this RADIUS server with Acct-Status-Type = Stop (per-station session stop). The counter is cumulative across all 802.1x interfaces communicating with this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-retransmissions` |  Number of RADIUS Accounting-Request packets that the switch retransmits to this RADIUS server when an initial Accounting-Request times out without a response. The counter is cumulative across all 802.1x interfaces communicating with this server.|
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-responses` | Number of RADIUS Accounting-Response packets that the switch receives from this RADIUS server. The counter is cumulative across all 802.1x interfaces communicating with this server. | 
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-timeouts` | Number of RADIUS Accounting-Request packets that timed out waiting for a response from this RADIUS server. The counter is cumulative across all 802.1x interfaces communicating with this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-malformed-responses` | Number of malformed RADIUS Accounting-Response packets received from this RADIUS server (invalid length, bad packet structure). The counter is cumulative across all 802.1x interfaces communicating with this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-bad-authenticators` | Number of RADIUS Accounting-Response packets received from this RADIUS server with an invalid Response Authenticator field (RFC 2866 §3). The counter is cumulative across all 802.1x interfaces communicating with this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-unknown-types` | Number of RADIUS accounting packets of unknown type which were received from this server on the accounting port. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-packets-dropped` | Packets that are dropped either because the UDP frame is too big (more than 4100 bytes) or because the parsed reply has no matching pending request. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-connection-errors` |  Number of failures encountered when trying to reach the RADIUS server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-receive-errors` | Error on the recv() call when trying to fetch the RADIUS server response on the per 802.1x interface socket. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-vrf-bind-errors` | Number of failures binding the socket to the configured VRF for this server.|
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-initialization-errors` | Number of failures (re)initializing the local RADIUS transport on behalf of this server. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/counters/accounting-out-queue-drops` | Number of outbound RADIUS requests to this server not retained on the local retransmit queue. | 
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/accounting-pending-requests` | Number of RADIUS Accounting-Request packets destined for this server that have not yet received a response or been removed from the retransmit list after the maximum number of retransmit attempts. |
| `/system/aaa/server-groups/server-group[name=dot1x]/servers/server[address]/radius/state/accounting-round-trip-time` | Round-trip time, in milliseconds, between the most recent Accounting-Request sent to this server and the corresponding Accounting-Response received. |

{{< /tab >}}
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
| `/network-instances/network-instance[name]/protocols/protocol[identifier][name]/bgp/neighbors/neighbor[neighbor-address]/afi-safis/afi-safi[afi-safi-name]/state/prefixes/received-pre-policy`| Number of prefixes received from the peer before applying any policies.<br><br>The pre-policy count requires soft-reconfiguration inbound to be enabled for the peer (`nv set vrf default router bgp neighbor <neighbor-id> address-family <address-family> soft-reconfiguration enabled`).|

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

{{< tabs "TabID113 ">}}
{{< tab "802.1x RADIUS Server">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_dot1x_radius_server_errors_total` | All RADIUS error counters from `hostapd`, exposed per server. Each time-series is aggregated across 802.1x interfaces communicating with the server. |
| `nvswitch_dot1x_radius_server_requests_total` | Number of access and accounting requests. |
| `nvswitch_dot1x_radius_server_accounting_requests_total` | Number of accounting requests. |
| `nvswitch_dot1x_radius_server_responses_total`  | Total number of responses. |
| `nvswitch_dot1x_radius_server_retransmissions_total` | Number of timeout access requests  or  accounting timeouts. |
| `nvswitch_dot1x_radius_server_pending_requests` | Number of RADIUS requests destined for the server that have not yet received a response or been removed from the retransmit list after the maximum number of retransmit attempts. |
| `nvswitch_dot1x_radius_server_round_trip_time_ms`  | Most recent round-trip time, in milliseconds, between a RADIUS request and its matching response.  |

{{< /tab >}}
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
| `nvrouting_bgp_peer_rib_adj_in_pre_policy` | Number of prefixes received from the peer before applying any policies.<br><br>The pre-policy count requires soft-reconfiguration inbound to be enabled for the peer (`nv set vrf default router bgp neighbor <neighbor-id> address-family <address-family> soft-reconfiguration enabled`).|

{{< /tab >}}
{{< tab "WJH">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_wjh_total_events_channel_forwarding` |  |
| `nvswitch_wjh_total_events_channel_acl` | |
| `nvswitch_wjh_total_events_channel_buffer` | |

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.
