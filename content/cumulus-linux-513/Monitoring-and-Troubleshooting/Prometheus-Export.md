---
title: Prometheus Export
author: NVIDIA
weight: 1234
toc: 3
---
Cumulus Linux supports exporting metrics through the Prometheus Client library in Prometheus metric format using a pull-based model. The switch presents the metrics to the local HTTP port. The telemetry collector is responsible for extracting the metrics and exporting them to clients.

You can export the following metrics using Prometheus:
- {{<link url="#adaptive-routing" text="Adaptive routing">}}
- {{<link url="#transceiver-metrics" text="Transceiver (temperature and power)">}}

## Adaptive Routing Metrics

You can export the following adaptive routing metrics.

| Metric | Description |
| ---------- | ------- |
| `nvswitch_ar_congestion_changes`  | The number of adaptive routing change events triggered due to congestion or link-down.|
| `nvswitch_ar_notification_tx_drops_total` | The number of adaptive routing notification packets dropped due to a lack of next hops to send adaptive routing notification packets or due to an IP address lookup failure. |
| `nvswitch_ar_notification_rx_total` | The number of adaptive routing notification packets received or dropped due an IP address lookup failure. |
| `nvswitch_ar_flow_table_entries` | The number of adaptive routing flow entries in the flow table.|
| `nvswitch_interface_ar_notification_tx_total` | The number of adaptive routing notification packets transmitted over the given port.|

### Enable Export of Adaptive Routing Metrics

To enable export of adaptive routing metrics, run the `nv set system telemetry adaptive-routing-stats export state enabled` command:

```
cumulus@leaf01:~$ nv set system telemetry adaptive-routing-stats export state enabled
cumulus@leaf01:~$ nv config apply
```

To configure the sample interval for adaptive routing metrics, run the `nv set system telemetry adaptive-routing-stats sample-interval` command. You can specify a value between ??? and ???. The default setting is 60 seconds.

```
cumulus@leaf01:~$ nv set system telemetry adaptive-routing-stats sample-interval 40
cumulus@leaf01:~$ nv config apply
```

### Export Adaptive Routing Metrics

To export adaptive routing metrics, run the following query from a terminal:

```
cumulus@leaf01:~$ curl http:/localhost:8001/metrics?collect[]=adaptive_routing_stats
```

## Transceiver Metrics

You can export the following transceiver metrics.

| Metric | Description |
| ---------- | ------- |
| `nvplatform_tranceiver_vendor_info` | The transceiver vendor information, such as which port the transceiver plugs into, the date of manufacture, the revision, the name of the manufacturer, the manufacturer part number, the serial number, and the IEEE company ID of the vendor.  |
| `nvplatform_tranceiver_info` | General information for the transceiver, such as which port the transceiver plugs into, the cable type, the cable length in meters, the status (plugged-enabled, plugged-disabled, plugged-error, or unplugged), the error status, the identifier, and the Ethernet compliance revision. |
| `nvplatform_tranceiver_temperature` |The temperature of the module in Celsius as a 64bit decimal value. |
| `nvplatform_tranceiver_temperature_alarm`| The alarm status due to temperature crossing thresholds defined for the module. The value sent for the temperature alarm is a bit mask:<br> Bit 0: high_temp_alarm<br>Bit 1: low_temp_alarm<br>Bit 2: high_temp_warning<br>Bit 3: low_temp_warning  |
| `nvplatform_tranceiver_temperature_threshold_info`| Temperature thresholds defined for the module (low or high). |
| `nvplatform_tranceiver_voltage` | The internally measured supply voltage for the module in volts (a 64bit decimal value). |
| n`vplatform_tranceiver_voltage_alarm` | The alarm status due to Voltage crossing thresholds defined for the module:<br>Bit 0: high_vcc_alarm<br>Bit 1: low_vcc_alarm<br>Bit 2: high_vcc_warning<br>Bit 3: low_vcc_warning |
| `nvplatform_tranceiver_voltage_threshold_info` | Voltage thresholds defined for the module. The level is alarm or warning. The threshold is low or high.|
| `nvplatform_transceiver_channel_power` | The transceiver channel power value in dBm units (logarithmic scale). |
| `nvplatform_transceiver_channel_power_alarm` | The alarm state for power value measured with the defined thresholds for the module as a bit mask value:<br>Bit 0: tx_power_hi_al<br>Bit 1: l tx_power_lo_al<br>Bit 2: tx_power_hi_war<br>Bit 3: l tx_power_lo_war.  |
| `nvplatform_transceiver_channel_power_threshold_info` | Threshold information for the power. The units are in dBm and represented by a 32bit decimal value. |
| `nvplatform_transceiver_channel_tx_bias_current` | tx bias current measured for the channel in milliamp units and represented by a 32bit decimal value. |
| `nvplatform_transceiver_channel_tx_bias_current_alarm` | tx bias current alarm state of tx bias current measure for the channel when compared to the threshold values for the channel defined for the module. This is a bit mask value:<br>Bit 0: tx_bias_hi_al<br>Bit 1: l tx_bias_lo_al<br>Bit 2: tx_bia_hi_war<br>Bit 3: l tx_bias_lo_war |
| `nvplatform_transceiver_channel_tx_bias_current_threshold_info` | tx bias current thresholds defined for the channel in milliamp units and represented by a 32bit decimal value. |

### Enable Export of Transceiver Metrics

To enable the export of transceiver metrics, run the `nv set system telemetry platform-stats class transceiver-info state enable` command:

```
cumulus@leaf01:~$ nv set system telemetry platform-stats class transceiver-info state enable
cumulus@leaf01:~$ nv config apply
```

To configure the sample interval for transceiver metrics, run the `nv set system telemetry platform-stats class transceiver-info sample-interval` command. You can specify a value between ??? and ???. The default setting is 60 seconds.

```
cumulus@leaf01:~$ nv set system telemetry platform-stats class transceiver-info sample-interval 40
cumulus@leaf01:~$ nv config apply
```

### Export Transceiver Metrics

To export transceiver metrics, run the following query from a terminal:

```
cumulus@leaf01:~$ curl http:/localhost:8001/metrics?collect[]=transceiver_info_stats
```
