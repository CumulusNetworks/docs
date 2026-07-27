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
| `/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries] /state/used` | The number of MAC entries used. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-routes] /state/used` | The number of IPv4 routes used. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-routes] /state/used` | The number of IPv6 routes used. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=Total-Mcast-Routes] /state/used` | The number of multicast routes used for an ASIC resource. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-host-entries] /state/used` | The number of IPv4 host entries used. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-host-entries] /state/used` | The number of IPv6 host entries. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ECMP-nexthops] /state/used` | The number of ECMP next hops used. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-Regions] /state/used` | The number of ACL-Regions used. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-18B-Rules-Key] /state/used` | The number of ACL 18B Rules Key used. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-36B-Rules-Key] /state/used` | The number of ACL 36B Rules Key used. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-54B-Rules-Key] /state/used` | The number of ACL 54B Rules Key used. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=Flow-Counters] /state/used` | The number of flow counters used. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Basic-Counters] /state/used` | The number of RIF Basic Counters used. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Enhanced-Counters] /state/used` | The number of RIF Enhanced Counters used. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries]/state/free` | The number of free MAC entries available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-routes]/state/free` | The number of free IPv4 routes available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-routes]/state/free` | The number of free IPv6 routes available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=Total-Mcast-Routes]/state/free` | The number of free multicast routes available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-host-entries]/state/free` | The number of free IPv4 host entries available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-host-entries]/state/free` | The number of free IPv6 host entries available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ECMP-nexthops]/state/free` | The number of free ECMP next hops available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-Regions]/state/free` | The number of free ACL regions available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-18B-Rules-Key]/state/free` | The number of free ACL 18B Rules Key available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-36B-Rules-Key]/state/free` | The number of free ACL 36B Rules Key available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-54B-Rules-Key]/state/free` | The number of free ACL 54B Rules Key available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=Flow-Counters]/state/free` | The number of free flow counters available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Basic-Counters]/state/free` | The number of free RIF Basic Counters available. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Enhanced-Counters]/state/free` | The number of free RIF Enhanced Counters available. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries]/state/max-limit` | The maximum limit of possible MAC entries. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-routes]/state/max-limit` | The maximum limit of possible IPv4 routes. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-routes]/state/max-limit` | The maximum limit of possible IPv6 routes. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=Total-Mcast-Routes]/state/max-limit` | The maximum limit of possible multicast routes. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-host-entries]/state/max-limit` | The maximum limit of possible IPv4 host entries. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-host-entries]/state/max-limit` | The maximum limit of possible IPv6 host entries. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=ECMP-nexthops]/state/max-limit` | The maximum limit of possible ECMP next hops. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=ACL-Regions]/state/max-limit` | The maximum limit of possible ACL regions. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=ACL-18B-Rules-Key]/state/max-limit` | The maximum limit of possible ACL 18B Rules Key. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=ACL-36B-Rules-Key]/state/max-limit` | The maximum limit of possible ACL 36B Rules Key. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=ACL-54B-Rules-Key]/state/max-limit` | The maximum limit of possible ACL 54B Rules Key. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=Flow-Counters]/state/max-limit` | The maximum limit of possible flow counters. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Basic-Counters]/state/max-limit` | The maximum limit of possibe RIF Basic Counters. |
|`/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Enhanced-Counters]/state/max-limit` | The maximum limit of possible RIF Enhanced Counters. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries] /state/high-watermark` | The highest number of MAC entries used.|
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-routes] /state/high-watermark` | The highest number of IPv4 routes used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-routes] /state/high-watermark` | The highest number of IPv6 routes used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=Total-Mcast-Routes] /state/high-watermark` | The highest number of multicast routes used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-host-entries] /state/high-watermark` | The highest number of IPv4 host entries used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-host-entries] /state/high-watermark` | The highest number of IPv6 host entries used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ECMP-nexthops] /state/high-watermark` | The highest number of ECMP next hops used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-Regions] /state/high-watermark` | The highest number of ACL regions used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-18B-Rules-Key] /state/high-watermark` | The highest number of ACL 18B Rules Key used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-36B-Rules-Key] /state/high-watermark` | The highest number of ACL 36B Rules Key used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-54B-Rules-Key] /state/high-watermark` | The highest number of ACL 54B Rules Key used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=Flow-Counters] /state/high-watermark` | The highest number of flow counters used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Basic-Counters] /state/high-watermark` | The highest number of RIF Basic Counters used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Enhanced-Counters] /state/high-watermark` | The highest number of RIF Enhanced Counters used.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries] /state/last-high-watermark` | The timestamp when the MAC entries high-watermark was last updated. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-routes] /state/last-high-watermark` | The timestamp when the IPv4 routes high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-routes] /state/last-high-watermark` | The timestamp when the IPv6 routes high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=Total-Mcast-Routes] /state/last-high-watermark` | The timestamp when the multicast routes high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv4-host-entries] /state/last-high-watermark` | The timestamp when the IPv4 host entries high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=IPv6-host-entries] /state/last-high-watermark` | The timestamp when the IPv6 host entries high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ECMP-nexthops] /state/last-high-watermark` | The timestamp when the ECMP next hops high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-Regions] /state/last-high-watermark` | The timestamp when the ACL regions high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-18B-Rules-Key] /state/last-high-watermark` | The timestamp when the ACL 18B Rules Key high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-36B-Rules-Key] /state/last-high-watermark` | The timestamp when the ACL 36B Rules Key high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=ACL-54B-Rules-Key] /state/last-high-watermark` | The timestamp when the ACL 54B Rules Key high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=Flow-Counters] /state/last-high-watermark` | The timestamp when the flow counters high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Basic-Counters] /state/last-high-watermark` | The timestamp when the RIF Basic Counters high-watermark was last updated. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=RIF-Enhanced-Counters] /state/last-high-watermark` | The timestamp when the RIF Enhanced Counters high-watermark was last updated. |

{{< /tab >}}
{{< tab "WJH">}}

|  Name | Description |
|------ | ----------- |
| `/wjh/channels/channel[name]/aggregate-events` | Total number of aggregate events for the channel. |
| `/wjh/channels/channel[name]/l1-events` | Total number of layer 1 channel events for the channel.|
| `/wjh/channels/channel[name]/state` | If the channel is enabled.|
| `/wjh/channels/channel[name]/state/categories` | Total number of categories for the channel. |
| `/wjh/channels/channel[name]/state/total-events` | Total number of events for the channel. |
| `/wjh/state/service-state` | The state of the WJH service. |

{{< /tab >}}
{{< /tabs >}}

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
| `nvswitch_dot1x_radius_server_retransmissions_total` | Number of timeout retried access requests and accounting retransmissions. |
| `nvswitch_dot1x_radius_server_timeouts_total` | Number of timeout access requests and accounting timeouts. |
| `nvswitch_dot1x_radius_server_pending_requests` | Number of RADIUS requests destined for the server that have not yet received a response or been removed from the retransmit list after the maximum number of retransmit attempts. |
| `nvswitch_dot1x_radius_server_round_trip_time_ms`  | Most recent round-trip time, in milliseconds, between a RADIUS request and its matching response.  |

To enable the new 802.1x RADIUS Server metrics, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export/#8021x-statistics">}}.

{{< /tab >}}
{{< tab "ASIC Resource">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_asic_MAC_entries_used` | The number of MAC entries used. |
| `nvswitch_platform_asic_IPv4_routes_used` | The number of IPv4 routes used. |
| `nvswitch_platform_asic_IPv6_routes_used` | The number of IPv6 routes used. |
| `nvswitch_platform_asic_Total_Mcast-Routes_used` | The number of total multicast routes used. |
| `nvswitch_platform_asic_IPv4_host_entries_used` | The number of IPv4 host entries used. |
| `nvswitch_platform_asic_IPv6_host_entries_used` | The number of IPv4 host entries used. |
| `nvswitch_platform_asic_ECMP_nexthops_used` | The number of ECMP next hops used. |
| `nvswitch_platform_asic_ACL_Regions_used` | The number of ACL regions used. |
| `nvswitch_platform_asic_ACL_18B_Rules_Key_used` | The number of ACL 18B Rules Key used. |
| `nvswitch_platform_asic_ACL_36B_Rules_Key_used` | The number of ACL 36B Rules Key used. |
| `nvswitch_platform_asic_ACL_54B_Rules_Key_used` | The number of ACL 54B Rules Key used. |
| `nvswitch_platform_asic_Flow_Counters_used` | The number of flow counters used. |
| `nvswitch_platform_asic_RIF_Basic_Counters_used` | The number of RIF basic counters used. |
| `nvswitch_platform_asic_RIF_Enhanced_Counters_used` | The number of RIF enhanced counters used. |
| `nvswitch_platform_asic_MAC_entries_free` | The number of free MAC entries available. |
| `nvswitch_platform_asic_IPv4_routes_free` | The number of free IPv4 routes available. | 
| `nvswitch_platform_asic_IPv6_routes_free` | The number of free IPv6 routes available. | 
| `nvswitch_platform_asic_Total_Mcast-Routes_free` | The number of multicast routes available. |
| `nvswitch_platform_asic_IPv4_host_entries_free` | The number of IPv4 host entries available. |
| `nvswitch_platform_asic_IPv6_host_entries_free` | The number of IPv6 host entries available. |
| `nvswitch_platform_asic_ECMP_nexthops_free` | The number of ECMP next hops available. |
| `nvswitch_platform_asic_ACL_Regions_free` | The number of ACL regions available. |
| `nvswitch_platform_asic_ACL_18B_Rules_Key_free` | The number of ACL 18B Rules Key available. |
| `nvswitch_platform_asic_ACL_36B_Rules_Key_free` | The number of ACL 36B Rules Key available. |
| `nvswitch_platform_asic_ACL_54B_Rules_Key_free` | The number of ACL 54B Rules Key available. |
| `nvswitch_platform_asic_Flow_Counters_free` | The number of flow counters available. |
| `nvswitch_platform_asic_RIF_Basic_Counters_free` | The number of RIF basic counters available. |
| `nvswitch_platform_asic_RIF_Enhanced_Counters_free` | The number of RIF basic enhanced counters available. |
| `nvswitch_platform_asic_MAC_entries_max_limit` | The maximum limit of possible MAC entries.|
| `nvswitch_platform_asic_IPv4_routes_max_limit` | The maximum limit of possible IPv4 routes.|
| `nvswitch_platform_asic_IPv6_routes_max_limit` | The maximum limit of possible IPv6 routes.|
| `nvswitch_platform_asic_Total_Mcast_Routes_max_limit` | The maximum limit of possible multicast routes.|
| `nvswitch_platform_asic_IPv4_host_entries_max_limit` | The maximum limit of possible IPv4 host entries.|
| `nvswitch_platform_asic_IPv6_host_entries_max_limit` | The maximum limit of possible IPv6 host entries.|
| `nvswitch_platform_asic_ECMP_nexthops_max_limit` | The maximum limit of possible ECMP next hops available.|
| `nvswitch_platform_asic_ACL_Regions_max_limit` | The maximum limit of possible ACL regions.|
| `nvswitch_platform_asic_ACL_18B_Rules_Key_max_limit` | The maximum limit of possible ACL 18B Rules Key.|
| `nvswitch_platform_asic_ACL_36B_Rules_Key_max_limit` | The maximum limit of possible ACL 36B Rules Key.|
| `nvswitch_platform_asic_ACL_54B_Rules_max_limit` | The maximum limit of possible ACL 54B Rules Key.|
| `nvswitch_platform_asic_Flow_Counters_max_limit` | The maximum limit of possible flow counters.|
| `nvswitch_platform_asic_RIF_Basic_Counters_max_limit` | The maximum limit of possible RIF basic counters.|
| `nvswitch_platform_asic_RIF_Enhanced_Counters_max_limit` | The maximum limit of possible RIF enhanced counters.|
| `nvswitch_platform_asic_MAC_entries_high_watermark` | The highest number of MAC entries used. |
| `nvswitch_platform_asic_IPv4_routes_high_watermark` | The highest number of IPv4 routes used. | 
| `nvswitch_platform_asic_IPv6_routes_high_watermark` | The highest number of IPv6 routes used. | 
| `nvswitch_platform_asic_Total_Mcast_Routes_high_watermark` | The highest number of multicast routes used. | 
| `nvswitch_platform_asic_IPv4_host_entries_high_watermark` | The highest number of IPv4 host entries used. | 
| `nvswitch_platform_asic_IPv6_host_entries_high_watermark` | The highest number of IPv6 host entries used. | 
| `nvswitch_platform_asic_ECMP_nexthops_high_watermark` | The highest number of ECMP next hops used. | 
| `nvswitch_platform_asic_ACL_Regions_high_watermark` | The highest number of ACL regions used. | 
| `nvswitch_platform_asic_ACL_18B-Rules_high_watermark` | The highest number of ACL 18B Rules Key used. | 
| `nvswitch_platform_asic_ACL_36B_Rules_high_watermark` | The highest number of ACL 36B Rules Key used. | 
| `nvswitch_platform_asic_ACL_54B_Rules_high_watermark` | The highest number of ACL 54B Rules Key used. | 
| `nvswitch_platform_asic_Flow_Counters_high_watermark` | The highest number of flow counters used. | 
| `nvswitch_platform_asic_RIF_Basic_Counters_high_watermark` | The highest number of RIF basic counters used. | 
| `nvswitch_platform_asic_RIF_Enhanced_Counters_high_watermark` | The highest number of RIF enhanced counters used. | 
| `nvswitch_platform_asic_MAC_entries_high_watermark_timestamp` | The timestamp when the MAC entries high-watermark was last updated.|
| `nvswitch_platform_asic_IPv4_routes_high_watermark_timestamp` | The timestamp when the IPv4 routes high-watermark was last updated.|
| `nvswitch_platform_asic_IPv6_routes_high_watermark_timestamp` | The timestamp when the IPv6 routeshigh-watermark was last updated.|
| `nvswitch_platform_asic_Total_Mcast_Routes_high_watermark_timestamp` | The timestamp when the multicast routes high-watermark was last updated.|
| `nvswitch_platform_asic_IPv4_host_entries_high_watermark_timestamp` | The timestamp when the IPv4 host entries high-watermark was last updated.|
| `nvswitch_platform_asic_IPv6_host_entries_high_watermark_timestamp` | The timestamp when the IPv6 host entrieshigh-watermark was last updated.|
| `nvswitch_platform_asic_ECMP_nexthops_high_watermark_timestamp` | The timestamp when the ECMP next hops high-watermark was last updated.|
| `nvswitch_platform_asic_ACL_Regions_high_watermark_timestamp` | The timestamp when the ACL regions high-watermark was last updated.|
| `nvswitch_platform_asic_ACL_18B_Rules_high_watermark_timestamp` | The timestamp when the ACL 18B Rules Key high-watermark was last updated.|
| `nvswitch_platform_asic_ACL_36B_Rules_high_watermark_timestamp` | The timestamp when the ACL 36B Rules Key high-watermark was last updated.|
| `nvswitch_platform_asic_ACL_54B_Rules_high_watermark_timestamp` | The timestamp when the ACL 54B Rules Key high-watermark was last updated.|
| `nvswitch_platform_asic_Flow_Counters_high_watermark_timestamp` | The timestamp when the flow counters high-watermark was last updated.|
| `nvswitch_platform_asic_RIF_Basic_Counters_high_watermark_timestamp` | The timestamp when the RIF basic counters high-watermark was last updated.|
| `nvswitch_platform_asic_RIF_Enhanced_Counters_high_watermark_timestamp` | The timestamp when the RIF enhanced counters high-watermark was last updated.|

To enable the new ASIC Resource metrics, refer to {{<link url="Open-Telemetry-Export/#platform-statistics" text="OTEL Telemetry Export">}}.

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.
