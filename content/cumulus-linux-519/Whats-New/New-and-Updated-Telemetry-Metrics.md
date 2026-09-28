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

<!-- REVIEW: the CPO and Laser Source tab below. The functional specification states the feature adds
     approximately 96 gNMI xpaths but never lists them; it maps internal metric names to hardware
     file paths instead. The paths in that tab are transcribed from the 5.19 demo material, which is
     the only source that gives external paths, and it labels them "Planned for 5.19" at 22 of
     30 CPO metrics, 6 of 16 optical engine metrics, and 24 of 51 ELS metrics, with four open SDK and
     firmware bugs. The tab therefore covers roughly half the paths the specification claims and may
     still list paths that slip. Reconcile it against the final metrics sheet and a candidate build
     before publishing. That material also shows a /phy subtree under /interfaces/interface[name] for
     PHY, BER, and FEC diagnostics with no leaf names given anywhere, so this draft omits it; add it
     if it ships. Delete this comment before publishing. -->

<!-- REVIEW: the per-laser ELS leaves are absent from the CPO and Laser Source tab below on purpose.
     The specification's object model defines them under laser-source/lasers/laser[index] and the
     nv show output documents them, but the 5.19 demo material records all 27 per-laser metrics as
     blocked by an open firmware bug and a dependency. Documenting them as exported would assert
     a capability the release may not have. Add them if they ship. Delete this comment before
     publishing. -->

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
{{< tab "Interfaces">}}

|  Name | Description |
|------ | ----------- |
| `/interfaces/interface[name=<interface-id>]/step-time-estimation/state/step-time-estimate` | Estimated step time, in seconds, of the AI training workload running on the interface. Requires {{<link url="High-Frequency-Telemetry/#step-time-estimation" text="step time estimation">}}. |

{{< /tab >}}
{{< tab "Microburst Histogram">}}

|  Name | Description |
|------ | ----------- |
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]`| Per-interface microburst telemetry container. `dir` is `rx` or `tx`; quantity is `packets` or `bytes`.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/bin[upper-boundary]/count` | Histogram bin count for the most recent collection window.  The value covers a single collection window and resets on read.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/score` | Burstiness score computed as σ² × μ in bin-index space.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/mean-bin-index` | Mean bin index μ over the current window.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/distribution-variance` | Bin-index variance σ² over the current window.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/peak-value` | Raw `max_watermark` value for the current window. Interpretation depends on quantity.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/threshold-state` | Operational threshold state for the configured score threshold.|
| `/performance/interfaces/interface[name]/histograms/microburst/direction[dir][quantity]/last-triggered` | Last time the threshold entered triggered state. Absent or unset if never triggered.|

The telemetry model names the packets or bytes selector `quantity`, where the NVUE command that configures it is `unit`. The two names refer to the same setting; `quantity` avoids a collision with the standard OTEL instrument descriptor field.

{{< /tab >}}
{{< tab "CPO and Laser Source">}}

The following paths are present on a switch with co-packaged optics (CPO) only. The `name` key is the CPO module, optical engine, or laser source identifier, such as `cpo1`, `oe1`, or `els1`. For the commands that show the same data on the switch, refer to {{<link url="Monitoring-Interfaces-and-Transceivers-with-NVUE/#show-cpo-module-and-laser-source-information" text="Show CPO Module and Laser Source Information">}}.

|  Name | Description |
|------ | ----------- |
| `/components/component[name=<cpo-id>]/state/name` | CPO module name. |
| `/components/component[name=<cpo-id>]/state/type` | OpenConfig component type for the CPO module. |
| `/components/component[name=<cpo-id>]/state/description` | CPO module identifier string. |
| `/components/component[name=<cpo-id>]/state/firmware-version` | Firmware version of the CPO module. |
| `/components/component[name=<cpo-id>]/state/oper-status` | Operational status of the CPO module. |
| `/components/component[name=<cpo-id>]/subcomponents/subcomponent[name]` | The laser source and optical engines that belong to the CPO module. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/laser-source-input-power/instant` | Power the laser source delivers into the optical engine for the channel. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/laser-source-input-power/alarm-status` | Whether the laser source input power for the channel is in alarm. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/laser-source-input-power/alarm-severity` | Severity of the laser source input power alarm for the channel. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/input-power/instant` | Received optical power on the channel. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/input-power/alarm-status` | Whether the received optical power on the channel is in alarm. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/input-power/alarm-severity` | Severity of the received optical power alarm for the channel. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/output-power/instant` | Transmitted optical power on the channel. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/output-power/alarm-status` | Whether the transmitted optical power on the channel is in alarm. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/output-power/alarm-severity` | Severity of the transmitted optical power alarm for the channel. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/rx-los` | Whether the channel has loss of received signal. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/tx-failure` | Whether the channel has a transmit failure. |
| `/components/component[name=<cpo-id>]/cpo/physical-channels/channel[index]/state/fault-opcode` | Advanced troubleshooting fault opcode for the channel. |
| `/components/component[name=<cpo-id>]/cpo/host-lanes/lane[lane-number]/lane-number` | Host lane number on the CPO module. |
| `/components/component[name=<cpo-id>]/cpo/host-lanes/lane[lane-number]/state/tx-los` | Whether the host lane has loss of transmitted signal. |
| `/components/component[name=<cpo-id>]/cpo/host-lanes/lane[lane-number]/state/dp-state` | Data path state of the host lane. |
| `/components/component[name=<oe-id>]/state/name` | Optical engine name. |
| `/components/component[name=<oe-id>]/state/description` | Optical engine identifier string. |
| `/components/component[name=<oe-id>]/state/parent` | The CPO module the optical engine belongs to. |
| `/components/component[name=<oe-id>]/state/type` | OpenConfig component type for the optical engine. |
| `/components/component[name=<oe-id>]/state/firmware-version` | Firmware version of the optical engine. |
| `/components/component[name=<oe-id>]/state/serial-no` | Serial number of the optical engine. |
| `/components/component[name=<els-id>]/state/name` | Laser source name. |
| `/components/component[name=<els-id>]/state/description` | Laser source identifier string. |
| `/components/component[name=<els-id>]/state/parent` | The CPO module the laser source feeds. |
| `/components/component[name=<els-id>]/state/type` | OpenConfig component type for the laser source. |
| `/components/component[name=<els-id>]/state/serial-no` | Serial number of the laser source. |
| `/components/component[name=<els-id>]/state/part-no` | Part number of the laser source. |
| `/components/component[name=<els-id>]/state/firmware-version` | Firmware version of the laser source. |
| `/components/component[name=<els-id>]/state/oper-status` | Operational status of the laser source. |
| `/components/component[name=<els-id>]/state/error-status` | Error status of the laser source. |
| `/components/component[name=<els-id>]/state/used-power` | Power the laser source consumes. |
| `/components/component[name=<els-id>]/state/temperature/instant` | Current laser source temperature. |
| `/components/component[name=<els-id>]/state/temperature/avg` | Average laser source temperature over the interval. |
| `/components/component[name=<els-id>]/state/temperature/min` | Minimum laser source temperature over the interval. |
| `/components/component[name=<els-id>]/state/temperature/max` | Maximum laser source temperature over the interval. |
| `/components/component[name=<els-id>]/state/temperature/interval` | Length of the interval the average, minimum, and maximum cover. |
| `/components/component[name=<els-id>]/state/temperature/min-time` | Time within the interval at which the minimum occurred. |
| `/components/component[name=<els-id>]/state/temperature/max-time` | Time within the interval at which the maximum occurred. |
| `/components/component[name=<els-id>]/state/temperature/alarm-status` | Whether the laser source temperature is in alarm. |
| `/components/component[name=<els-id>]/state/temperature/alarm-severity` | Severity of the laser source temperature alarm. |
| `/components/component[name=<els-id>]/state/temperature/alarm-threshold` | Threshold at which the laser source temperature alarm triggers. |
| `/components/component[name=<els-id>]/laser-source/state/vendor` | Laser source vendor. |
| `/components/component[name=<els-id>]/laser-source/state/date-code` | Laser source vendor date code. |
| `/components/component[name=<els-id>]/laser-source/state/present` | Whether the laser source is present. |
| `/components/component[name=<els-id>]/laser-source/state/icc-current` | ICC current the laser source draws. |
| `/interfaces/interface[name=<interface-id>]/state/cpo-module` | The CPO module that carries the interface. |
| `/interfaces/interface[name=<interface-id>]/state/cpo-channels` | The CPO module channels assigned to the interface. |

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

<!-- REVIEW: the Microburst Histogram tab below states that the temporality of
     nvswitch_histogram_interface_microburst is delta. The telemetry change proposal says the
     bins reset on read and that consumers receive per-window state rather than cumulative
     totals, but it does not say whether `nv set system telemetry histogram temporality
     cumulative` has any effect on the microburst metric. Confirm, and if the microburst
     histogram ignores that setting, say so here and in the Temporality Mode section of
     Open-Telemetry-Export.md. Delete this comment before publishing. -->

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
{{< tab "Step Time Estimation">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_interface_step_time_estimate` | Estimated step time, in seconds, of the AI training workload running on an interface. |

This metric is a gauge carrying a single `interface` label holding the interface name. The switch exports a data point only for an interface for which the algorithm produces an estimate, and exports no metric at all when it produces no estimate for any interface. For information about the feature behind this metric, refer to {{<link url="High-Frequency-Telemetry/#step-time-estimation" text="Step Time Estimation">}}.

{{< /tab >}}
{{< tab "Microburst Histogram">}}

|  Name | Description |
|------ | ----------- |
| `nvswitch_histogram_interface_microburst` | Per-window microburst histogram distribution. Bucket counts are exported after each poll cycle; temporality is delta. The values are the packet-delta or byte-delta per sampling window, depending on the value of quantity.|
| `nvswitch_histogram_interface_microburst_score` | Burstiness score σ² × μ for the current window.|
| `nvswitch_histogram_interface_microburst_mean_bin_index` | Mean bin index μ for the current window.|
| `nvswitch_histogram_interface_microburst_distribution_variance` | Bin-index variance σ² for the current window.|
| `nvswitch_histogram_interface_microburst_peak_value` | Peak raw watermark for the current window (packets or bytes, depending on quantity). Omitted when no valid watermark is available for the window.|
| `nvswitch_histogram_interface_microburst_threshold_state` | Threshold state for the configured score threshold. Omitted when no threshold is configured.|
| `nvswitch_histogram_interface_microburst_last_triggered` | (Unix epoch) timestamp of the last transition into triggered state. Omitted when the threshold has never triggered.|

Each microburst metric carries an `interface` label, a `direction` label (`rx` or `tx`), and a `quantity` label (`packets` or `bytes`). The telemetry model names this selector `quantity`, where the NVUE command that configures it is `unit`; the two names refer to the same setting. `nvswitch_histogram_interface_microburst` is a histogram and the rest are gauges, with `threshold_state` reporting 0 for clear and 1 for triggered. For information about the feature behind these metrics, refer to {{<link url="ASIC-Monitoring/#microburst-histogram" text="Microburst Histogram">}}.

{{< /tab >}}
{{< tab "CPO and Laser Source">}}

The switch exports these metrics on a switch with CPO only. Enable them with the `transceiver-info` and `laser-source-info` platform statistic classes, where `transceiver-info` covers the CPO modules and optical engines and `laser-source-info` covers the laser sources; refer to {{<link url="Open-Telemetry-Export/#platform-statistics" text="Platform Statistics">}}.

|  Name | Description |
|------ | ----------- |
| `nvswitch_platform_cpo_info` | CPO module inventory. Carries `name`, `type`, `description`, and `fw_version` labels. |
| `nvswitch_platform_cpo_status` | Operational status of the CPO module. Carries a `name` label. |
| `nvswitch_platform_cpo_subcomponent_info` | The laser source and optical engines that belong to the CPO module. Carries `name`, `subcomponent_type`, and `subcomponent_name` labels. |
| `nvswitch_platform_cpo_channel_laser_source_input_power` | Power the laser source delivers into the optical engine for a channel. Carries `name` and `channel` labels. |
| `nvswitch_platform_cpo_channel_laser_source_input_power_alarm` | Alarm status and severity for the laser source input power on a channel. Carries `name` and `channel` labels. |
| `nvswitch_platform_cpo_channel_power` | Received and transmitted optical power on a channel. Carries `name`, `channel`, and `direction` labels. |
| `nvswitch_platform_cpo_channel_power_alarm` | Alarm status and severity for the optical power on a channel. Carries `name`, `channel`, and `direction` labels. |
| `nvswitch_platform_cpo_channel_state` | Loss of received signal and transmit failure state for a channel. Carries `name`, `channel`, and `state` labels. |
| `nvswitch_platform_cpo_channel_fault_opcode` | Advanced troubleshooting fault opcode for a channel. Carries `name` and `channel` labels. |
| `nvswitch_platform_cpo_host_lane_state` | Loss of transmitted signal state for a host lane. Carries `name`, `lane`, and `state` labels. |
| `nvswitch_platform_cpo_host_lane_dp_state` | Data path state of a host lane. Carries `name` and `lane` labels. |
| `nvswitch_platform_oe_info` | Optical engine inventory. Carries `name`, `type`, `description`, `serial_no`, `firmware_version`, and `cpo_module` labels. |
| `nvswitch_platform_els_info` | Laser source inventory. Carries `name`, `type`, `description`, `vendor`, `vendor_rev`, `part_no`, `serial_no`, `date_code`, `firmware_version`, `present`, and `cpo_module` labels. |
| `nvswitch_platform_els_status` | Operational status of the laser source. Carries a `name` label. |
| `nvswitch_platform_els_error_status` | Error status of the laser source. Carries `name` and `error_status` labels. |
| `nvswitch_platform_els_power_consumption` | Power the laser source consumes. Carries a `name` label. |
| `nvswitch_platform_els_temperature` | Laser source temperature, with the average, minimum, and maximum over the interval. Carries a `name` label. |
| `nvswitch_platform_els_temperature_alarm` | Alarm status and severity for the laser source temperature. Carries a `name` label. |
| `nvswitch_platform_els_temperature_threshold_info` | Threshold at which the laser source temperature alarm triggers. Carries a `name` label. |
| `nvswitch_platform_els_icc_current` | ICC current the laser source draws. Carries a `name` label. |

{{< /tab >}}
{{< /tabs >}}

For information about OTEL, refer to {{<link url="Open-Telemetry-Export" text="OTEL Telemetry Export">}}.
