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
{{< tab "ASIC Resource">}}

|  Name | Description |
|------ | ----------- |
| `/components/component/integrated-circuit/utilization/resources/resource[name=<resource_name>]/state/used` | The number of entries used for an ASIC resource. | 
| `/components/component/integrated-circuit/utilization/resources/resource[name=<resource_name>]/state/free` | The number of free entries available for an ASIC resource. |
`/components/component/integrated-circuit/utilization/resources/resource[name=<resource_name>]/state/max-limit` | The maximum limit of possible entries for an ASIC resource. |
| `/components/component/integrated-circuit/utilization/resources/resource[name=<resource_name>]/state/high-watermark` | The highest number of entries used for an ASIC resource.| 
| `/components/component/integrated-circuit/utilization/resources/resource[name=<resource_name>]/state/last-high-watermark` | The timestamp when the high-watermark was last updated. |

The ASIC resource is one of the following:

| Name |
|----- |
| `MAC-entries` | 
| `IPv4-Routes` |
| `IPv6-Routes` |
| `Total-Mcast-Routes` |
| `IPv4-host-entries` |
| `IPv6-host-entries` |
| `ECMP-nexthops` |
| `ACL-Regions` |
| `ACL-18B-Rules-Key` |
| `ACL-36B-Rules-Key` |
| `ACL-54B-Rules-Key` |
| `Flow-Counters` |
| `RIF-Basic-Counters` |
| `RIF-Enhanced-Counters` |

For example, `/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries]/state/used`.

{{%notice note%}}
The maximum value for the `IPv6-Routes` ASIC resource represents the number of single-width IPv6 route entries. In hardware, IPv6 routes with prefix lengths from /0 to /64 consume one entry each, whereas routes with prefix lengths from /65 to /128 consume two entries each. As a result, the actual number of free hardware entries depends on the mix of IPv6 route prefix lengths programmed into the table.
{{%/notice%}}

{{< /tab >}}
{{< tab "Micro Updates">}}

|  Name | Description |
|------ | ----------- |
| `/components/component[name=<archive-id>]/state/name` | The package archive name. |
| `/components/component[name=<archive-id>]/state/type` | The type: OPERATING_SYSTEM_UPDATE.|
| `/components/component[name=<archive-id>]/software-package-archive/state/failure-state` | The failure state:<br>0: none<br>1: PRE_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>2: PRE_INSTALL_FAILED_ROLLBACK_FAILED<br>3: PRE_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>4: APT_FAILED_ROLLBACK_SUCCESSFULL<br>5: APT_FAILED_ROLLBACK_FAILED<br>6: APT_FAILED_ROLLBACK_IN_PROGRESS<br>7: POST_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>8: POST_INSTALL_FAILED_ROLLBACK_FAILED<br>9: POST_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>10: UNKNOWN_FAILURE_ROLLBACK_SUCCESSFULL<br>11: UNKNOWN_FAILURE_ROLLBACK_FAILED<br>12: UNKNOWN_FAILURE_ROLLBACK_IN_PROGRESS.|
| `/components/component[name=<archive-id>]/software-package-archive/state/status` | The installation status:<br>0: not-installed<br>1: installed<br>2: partially-installed<br>3: failed<br>4: operation-in-progress.|
| `/components/component[name=<archive-id>]/software-package-archive/state/installed-at` | The installation time (Unix timestamp).|
| `/system/state/installed-software-package-archives` | Installed micro update archives.|

{{< /tab >}}
{{< tab "Platform Leakage Sensor">}}

|  Name | Description |
|------ | ----------- |
| `/components/component[name=leakage1]/state/name` | Leakage1 sensor name. Liquid-cooled NVIDIA switch only.|
| `/components/component[name=leakage1]/state/oper-status` | Leakage1 sensor operational health (ACTIVE on valid reading) Liquid-cooled NVIDIA switch only.|
| `/components/component[name=leakage1]/state/leakage/alarm-status` | Leakage1 alarm status. Liquid-cooled NVIDIA switch only.|
| `/components/component[name=leakage2]/state/name` | Leakage2 sensor name. Liquid-cooled NVIDIA switch only.|
| `/components/component[name=leakage2]/state/oper-status` | Leakage2 sensor operational health (ACTIVE on valid reading) Liquid-cooled NVIDIA switch only.|
| `/components/component[name=leakage2]/state/leakage/alarm-status` | Leakage2 alarm status. Liquid-cooled NVIDIA switch only.|

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

To enable the new 802.1x RADIUS Server metrics, refer to {{<link url="Open-Telemetry-Export/#8021x-statistics" text="OTEL Telemetry Export">}}.

{{< /tab >}}
{{< tab "ASIC Resource">}}

| Name | Description |
|----- | ----------- |
| `nvswitch_platform_asic_resource_used{resource_name="<name>"}` | The number of entries used for an ASIC resource. | 
| `nvswitch_platform_asic_resource_free{resource_name="<name>"}` | The number of free entries available for an ASIC resource. | 
| `nvswitch_platform_asic_resource_max_limit{resource_name="<name>"}` | The maximum limit of possible entries for an ASIC resource.|
| `nvswitch_platform_asic_resource_high_watermark{resource_name="<name>"}` | The highest number of entries used for an ASIC resource. | 
| `nvswitch_platform_asic_resource_high_watermark_timestamp{resource_name="<name>"}` | The timestamp when the high-watermark was last updated.|

The ASIC resource is one of the following:

| Name |
|----- |
| `MAC-entries` | 
| `IPv4-Routes` |
| `IPv6-Routes` |
| `Total-Mcast-Routes` |
| `IPv4-host-entries` |
| `IPv6-host-entries` |
| `ECMP-nexthops` |
| `ACL-Regions` |
| `ACL-18B-Rules-Key` |
| `ACL-36B-Rules-Key` |
| `ACL-54B-Rules-Key` |
| `Flow-Counters` |
| `RIF-Basic-Counters` |
| `RIF-Enhanced-Counters` |

For example, `nvswitch_platform_asic_resource_free{resource_name="MAC-entries"}`.

To enable the new ASIC Resource metrics, refer to {{<link url="Open-Telemetry-Export/#platform-statistics" text="OTEL Telemetry Export">}}.

{{< /tab >}}
{{< tab "Platform Leakage Sensor">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_environment_leak_sensor_status` | Leak sensor status. Liquid-cooled NVIDIA switch only.|
| `nvswitch_platform_environment_leakage_status` | Leakage status. Liquid-cooled NVIDIA switch only. |

{{< /tab >}}
{{< tab "Micro Updates">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_package_archive_failure_state` | The failure state if the micro update installation fails:<br>0: none<br>1: PRE_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>2: PRE_INSTALL_FAILED_ROLLBACK_FAILED<br>3: PRE_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>4: APT_FAILED_ROLLBACK_SUCCESSFULL<br>5: APT_FAILED_ROLLBACK_FAILED<br>6: APT_FAILED_ROLLBACK_IN_PROGRESS<br>7: POST_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>8: POST_INSTALL_FAILED_ROLLBACK_FAILED<br>9: POST_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>10: UNKNOWN_FAILURE_ROLLBACK_SUCCESSFULL<br>11: UNKNOWN_FAILURE_ROLLBACK_FAILED<br>12: UNKNOWN_FAILURE_ROLLBACK_IN_PROGRESS|
| `nvswitch_platform_package_archive_status` | The package archive status:<br>0: not-installed<br>1: installed<br>2: partially-installed<br>3: failed<br>4: operation-in-progress.|
| `nvswitch_platform_package_archive_installed_time` | The micro update package installed time (Unix timestamp). |

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.
