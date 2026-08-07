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

| Name | Description |
|----- | ----------- |
| `MAC-entries` | Layer 2 MAC address table entries.|
| `IPv4-Routes` | IPv4 routing table entries.|
| `IPv6-Routes` | IPv6 routing table entries.|
| `Total-Mcast-Routes` | Multicast routing entries.|
| `IPv4-host-entries` | IPv4 neighbor entries. |
| `IPv6-host-entries` | IPv6 neighbor entries. |
| `ECMP-nexthops` | Equal-Cost Multi-Path (ECMP) next-hop paths. |
| `ACL-Regions` | Hardware regions allocated for Access Control Lists (ACLs). |
| `ACL-18B-Rules-Key` | ACL rules using an 18-byte key. |
| `ACL-36B-Rules-Key` | ACL rules using a 36-byte key. |
| `ACL-54B-Rules-Key` | ACL rules using a 54-byte key. |
| `Flow-Counters` | Hardware counters for tracking specific traffic flows.|
| `RIF-Basic-Counters` | Basic statistics counters for router interfaces (RIFs). |
| `RIF-Enhanced-Counters` | Detailed statistics counters for router interfaces (RIFs). |

For example, `/components/component/integrated-circuit/utilization/resources/resource[name=MAC-entries]/state/used`.

{{%notice note%}}
- ACL maximum limits are dynamic and depend on the distribution of 18B, 36B, and 54B ACL rules.
- The maximum value for the `IPv6-Routes` ASIC resource represents the number of single-width IPv6 route entries. In hardware, IPv6 routes with prefix lengths from /0 to /64 consume one entry each, whereas routes with prefix lengths from /65 to /128 consume two entries each. As a result, the actual number of free hardware entries depends on the mix of IPv6 route prefix lengths programmed into the table.
{{%/notice%}}

{{< /tab >}}
{{< tab "Patches">}}

|  Name | Description |
|------ | ----------- |
| `/components/component[name=<archive-id>]/state/name` | The patch archive name. |
| `/components/component[name=<archive-id>]/state/type` | The type: OPERATING_SYSTEM_UPDATE.|
| `/components/component[name=<archive-id>]/software-package-archive/state/failure-state` | The failure state:<br>0: none<br>1: PRE_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>2: PRE_INSTALL_FAILED_ROLLBACK_FAILED<br>3: PRE_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>4: APT_FAILED_ROLLBACK_SUCCESSFULL<br>5: APT_FAILED_ROLLBACK_FAILED<br>6: APT_FAILED_ROLLBACK_IN_PROGRESS<br>7: POST_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>8: POST_INSTALL_FAILED_ROLLBACK_FAILED<br>9: POST_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>10: UNKNOWN_FAILURE_ROLLBACK_SUCCESSFULL<br>11: UNKNOWN_FAILURE_ROLLBACK_FAILED<br>12: UNKNOWN_FAILURE_ROLLBACK_IN_PROGRESS.|
| `/components/component[name=<archive-id>]/software-package-archive/state/status` | The installation status:<br>0: not-installed<br>1: installed<br>2: partially-installed<br>3: failed<br>4: operation-in-progress.|
| `/components/component[name=<archive-id>]/software-package-archive/state/installed-at` | The time a patch archive was installed (Unix timestamp).|
| `/system/state/installed-software-package-archives` | Installed patch archives.|

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
{{< tab "Platform Power Supply">}}

|  Name | Description |
|------ | ----------- |
| `/components/component[name=PDBn-HSCm]/state/name` |	Component name Power Distribution Board (PDB) hotswap controllers (HSC).|
| `/components/component[name=PDBn-HSCm]/state/description` | Human-readable description. |
| `/components/component[name=PDBn-HSCm]/state/type` | Component type; POWER_SUPPLY (derived). |
| `/components/component[name=PDBn-HSCm]/state/oper-status`	| Operational status (such as ACTIVE).|
| `/components/component[name=PDBn-HSCm]/power-supply/state/capacity` |	HSC capacity in Watts (per-HSC) — max INPUT power the HSC can handle, not PSU rated OUTPUT.|
| `/components/component[name=PDBn-HSCm]/power-supply/state/input-voltage` | Input-side voltage at the hotswap controller.|
| `/components/component[name=PDBn-HSCm]/power-supply/state/input-current` | Input-side current at the hotswap controller. |
| `/components/component[name=PDBn-HSCm]/power-supply/state/input-power` | Input-side power (normative).|

A hotswap controller has no EEPROM or VPD and a PDB is input-only. The following metrics are not populated for Power Distribution Board (PDB) hotswap controllers (HSC) (PDB-based switches, such as the SN6600_LD - Spectrum-6).

|  Name | Description |
|------ | ----------- |
| `/components/component[name=PDBn-HSCm]/state/serial-no` |	No EEPROM on hotswap controller — PSU platforms only; not applicable to input-only PDB/HSC.|
| `/components/component[name=PDBn-HSCm]/state/part-no` |	No EEPROM on hotswap controller — PSU platforms only; not applicable to input-only PDB/HSC.|
| `/components/component[name=PDBn-HSCm]/state/mfg-name` |	No source in the platform inventory metric - not populated for PSU components either.|
| `/components/component[name=PDBn-HSCm]/state/model-name` |	No EEPROM on hotswap controller — PSU platforms only; not applicable to input-only PDB/HSC.|
| `/components/component[name=PDBn-HSCm]/state/hardware-version` |	No EEPROM on hotswap controller — PSU platforms only; not applicable to input-only PDB/HSC.|
| `/components/component[name=PDBn-HSCm]/power-supply/state/output-power`| Input-only device (no output metering) — not exposed|
| `/components/component[name=PDBn-HSCm]/power-supply/state/output-current` |Input-only device (no output metering) — not exposed|
|`/components/component[name=PDBn-HSCm]/power-supply/state/output-voltage` |Input-only device (no output metering) — not exposed |
| `/components/component[name=PSUn]/state/serial-no` | From PSU VPD/EEPROM. Not populated for PDB/HSC.|
| `/components/component[name=PSUn]/state/part-no` | From PSU VPD/EEPROM. Not populated for PDB/HSC.|
| `/components/component[name=PSUn]/state/model-name` | From PSU VPD/EEPROM. Not populated for PDB/HSC.|
| `/components/component[name=PSUn]/state/hardware-version` | From PSU VPD/EEPROM. Not populated for PDB/HSC.|
| `/components/component[name=PSUn]/power-supply/state/output-power` | PSU output side. Not populated for PDB/HSC.|
| `/components/component[name=PSUn]/power-supply/state/output-current` | PSU output side. Not populated for PDB/HSC.|
| `/components/component[name=PSUn]/power-supply/state/output-voltage` | PSU output side. Not populated for PDB/HSC.|

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

| Name | Description |
|----- | ----------- |
| `MAC-entries` | Layer 2 MAC address table entries.|
| `IPv4-Routes` | IPv4 routing table entries.|
| `IPv6-Routes` | IPv6 routing table entries.|
| `Total-Mcast-Routes` | Multicast routing entries.|
| `IPv4-host-entries` | IPv4 neighbor entries. |
| `IPv6-host-entries` | IPv6 neighbor entries. |
| `ECMP-nexthops` | Equal-Cost Multi-Path (ECMP) next-hop paths. |
| `ACL-Regions` | Hardware regions allocated for Access Control Lists (ACLs). |
| `ACL-18B-Rules-Key` | ACL rules using an 18-byte key. |
| `ACL-36B-Rules-Key` | ACL rules using a 36-byte key. |
| `ACL-54B-Rules-Key` | ACL rules using a 54-byte key. |
| `Flow-Counters` | Hardware counters for tracking specific traffic flows.|
| `RIF-Basic-Counters` | Basic statistics counters for router interfaces (RIFs). |
| `RIF-Enhanced-Counters` | Detailed statistics counters for router interfaces (RIFs). |

For example, `nvswitch_platform_asic_resource_free{resource_name="MAC-entries"}`.

{{%notice note%}}
- ACL maximum limits are dynamic and depend on the distribution of 18B, 36B, and 54B ACL rules.
- The maximum value for the `IPv6-Routes` ASIC resource represents the number of single-width IPv6 route entries. In hardware, IPv6 routes with prefix lengths from /0 to /64 consume one entry each, whereas routes with prefix lengths from /65 to /128 consume two entries each. As a result, the actual number of free hardware entries depends on the mix of IPv6 route prefix lengths programmed into the table.
{{%/notice%}}

To enable the new ASIC Resource metrics, refer to {{<link url="Open-Telemetry-Export/#platform-statistics" text="OTEL Telemetry Export">}}.

{{< /tab >}}
{{< tab "Platform Leakage Sensor">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_environment_leak_sensor_status` | Leak sensor status. Liquid-cooled NVIDIA switch only.|
| `nvswitch_platform_environment_leakage_status` | Leakage status. Liquid-cooled NVIDIA switch only. |

{{< /tab >}}
{{< tab "Platform Power Supply">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_environment_power_supply_state` | Operational state of the power component. Enum: 0 ABSENT, 1 OK, 2 FAILED, 3 BAD, 4 HIGH, 5 LOW, 6 CRITICAL, 7 LCRITICAL, 8 UNKNOWN.|
| `nvswitch_platform_environment_power_supply_capacity` | Power supply capacity in Watts. For input-only Power Distribution Boards (PDBs) this is the hotswap-controller power1_max (max INPUT power the hotswap controller (HSC) can handle, not a PSU rated OUTPUT capacity).
| `nvswitch_platform_environment_power_supply_input_voltage` | Input-side voltage measured at the hotswap controller. |
| `nvswitch_platform_environment_power_supply_input_current` | Input-side current measured at the hotswap controller. |
| `nvswitch_platform_environment_power_supply_power` | Power-supply power in Watts (normative power metric). For input-only PDBs, this is the input-side power surfaced as the gNMI input-power leaf. |
| `nvswitch_platform_environment_power_supply_current` | Output current (PSU output side). Emitted on PSU platforms only; not applicable to input-only PDB/HSC. |
| `nvswitch_platform_environment_power_supply_voltage`| Output voltage (PSU output side). Emitted on PSU platforms only; not applicable to input-only PDB/HSC.|

To enable the new the platform power supply metrics, refer to {{<link url="Open-Telemetry-Export/#platform-statistics" text="OTEL Telemetry Export">}}.

{{< /tab >}}
{{< tab "Patches">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_package_archive_failure_state` | The failure state if the patch archive installation fails:<br>0: none<br>1: PRE_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>2: PRE_INSTALL_FAILED_ROLLBACK_FAILED<br>3: PRE_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>4: APT_FAILED_ROLLBACK_SUCCESSFULL<br>5: APT_FAILED_ROLLBACK_FAILED<br>6: APT_FAILED_ROLLBACK_IN_PROGRESS<br>7: POST_INSTALL_FAILED_ROLLBACK_SUCCESSFULL<br>8: POST_INSTALL_FAILED_ROLLBACK_FAILED<br>9: POST_INSTALL_FAILED_ROLLBACK_IN_PROGRESS<br>10: UNKNOWN_FAILURE_ROLLBACK_SUCCESSFULL<br>11: UNKNOWN_FAILURE_ROLLBACK_FAILED<br>12: UNKNOWN_FAILURE_ROLLBACK_IN_PROGRESS|
| `nvswitch_platform_package_archive_status` | The patch archive status:<br>0: not-installed<br>1: installed<br>2: partially-installed<br>3: failed<br>4: operation-in-progress.|
| `nvswitch_platform_package_archive_installed_time` | The time the patch archive was installed (Unix timestamp). |

{{< /tab >}}
{{< /tabs >}}


For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.

## Updated OTEL Metrics

|  Old Metric | New Metric |
|------ | ----------- |
| `nvswitch_platform_environment_psu_state` | `nvswitch_platform_environment_power_supply_state` |
| `nvswitch_platform_environment_psu_capacity` | `nvswitch_platform_environment_power_supply_capacity` |
| `nvswitch_platform_environment_psu_input_voltage` | `nvswitch_platform_environment_power_supply_input_voltage` |
| `nvswitch_platform_environment_psu_input_current` | `nvswitch_platform_environment_power_supply_input_current` |
| `nvswitch_platform_environment_psu_power` | `nvswitch_platform_environment_power_supply_power` |
| `nvswitch_platform_environment_psu_current` |	`nvswitch_platform_environment_power_supply_current` |
| `nvswitch_platform_environment_psu_voltage` |	`nvswitch_platform_environment_power_supply_voltage` |

{{%notice note%}}
On PSU-based platforms, the legacy `psu_*` metric family and the common `power_supply_*` family are emitted together for a three-release migration window. The legacy `psu_*` family is deprecated and will be removed after that window; make sure to migrate your dashboards and queries to `power_supply_*` during the window. The gNMI/OpenConfig PSU representation is unchanged.
{{%/notice%}}

|  Old Metric | New Metric|
|------ | ----------- |
| `nvswitch_platform_info_hw_details`|`nvswitch_platform_info_hw_details{serial_no}`: Serial number. Emitted for PSU components; not emitted for PDBn-HSCm (no EEPROM/VPD on a hotswap controller).<br>`nvswitch_platform_info_hw_details{part_no}`: Part number.<br>`nvswitch_platform_info_hw_details{model_name}`: Model name.<br>`nvswitch_platform_info_hw_details{hardware_version}`: Hardware revision.|
