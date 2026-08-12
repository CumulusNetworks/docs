---
title: Monitor with Prometheus
author: NVIDIA
weight: 900
toc: 4
---

{{<exlink url="https://prometheus.io/docs/introduction/overview/" text="Prometheus">}} is open-source software used to gather and process monitoring data. After you configure a Prometheus endpoint, you can use visualization tools such as Grafana to create customized charts and graphs based on the information Prometheus collects.

## Configure Prometheus Endpoint

You can configure NetQ to expose telemetry data in a format compatible with the Prometheus protocol by setting Prometheus as the target endpoint during the Prometheus server configuration. The telemetry data available through the Prometheus metrics endpoint reflects data collected from NMX-T.

To configure NetQ as a Prometheus scraping target, add the NetQ NVLink endpoint details to the `prometheus.yml` configuration file. The following example illustrates a sample configuration, where `job_name` defines the scraping job name and `id` represents the NVLink5 domain ID:


```
global:
  scrape_interval: 15s
  evaluation_interval: 15s
scrape_configs:
  - job_name: "prometheus"
    scheme: https
    basic_auth:
      username: 'rw-user'
      password: 'rw-password'
    static_configs:
      - targets: ['10.xxx.xx.xx']
    metrics_path: '/nmx/v1/metrics'
    tls_config:
      insecure_skip_verify: true
    params:
      id: ['e83134ff-89fb-45eb-97ae-920b35f8fde5']
```
## Metrics Scraped from NMX-T

NetQ NVLink scrapes the following metrics from NMX-T:

{{<expand "metric-forwarder-values-counters.yaml">}}

```
name: metric-forwarder-counters
replicaCount: 4
nameOverride: "metric-forwarder-counters"
fullnameOverride: "metric-forwarder-counters"

cmService:
  enabled: true
  content:
    nmxmgr:
      service-name: "metric-forwarder-counters"
      version: "1.0.0"
      admin-addr: ":9081"

      kafka:
        group-id: "metric-forwarder-counters"
        batch-size: 250
        batch-period: 3s

      http:
        compression: true

      processors:
        counters:
          enabled: false

      metrics:
        counters:
          labels: "domain_id,node_guid,port_guid,port_num"
          derived_labels:
            - label: "port_type"
              conditions:
                - match:
                    node_type: "1"
                    node_type_ext: "1"
                  value: "GPU"
                - match:
                    node_type: "1"
                    node_type_ext: "2"
                  value: "HCA"
                - match:
                    node_type: "2"
                  value: "SWITCH"
                - match:
                    node_type: "3"
                  value: "ROUTER"
              default_value: "UNKNOWN"
          metric: [ "PortXmitDataExtended",
                    "PortRcvDataExtended",
                    "PortXmitPktsExtended",
                    "PortRcvPktsExtended",
                    "PortUniCastXmitPktsExtended",
                    "PortUniCastRcvPktsExtended",
                    "PortMultiCastXmitPktsExtended",
                    "PortMultiCastRcvPktsExtended",
                    "LinkErrorRecoveryCounterExtended",
                    "LinkDownedCounterExtended",
                    "PortRcvErrorsExtended",
                    "PortRcvRemotePhysicalErrorsExtended",
                    "PortRcvSwitchRelayErrorsExtended",
                    "PortXmitDiscardsExtended",
                    "PortXmitConstraintErrorsExtended",
                    "PortRcvConstraintErrorsExtended",
                    "LocalLinkIntegrityErrorsExtended",
                    "VL15DroppedExtended",
                    "PortXmitWaitExtended",
                    "phy_received_bits",
                    "phy_symbol_errors",
                    "phy_raw_errors_lane0",
                    "phy_raw_errors_lane1",
                    "phy_effective_errors",
                    "raw_ber",
                    "eff_ber",
                    "symbol_ber",
                    "link_speed_active",
                    "link_width_active",
                    "switch_voltage",
                    "switch_temperature",
                    "link_down_counter",
                    "link_down_events",
                    "plr_rcv_codes",
                    "plr_rcv_code_err",
                    "plr_rcv_uncorrectable_code",
                    "plr_xmit_retry_events",
                    "plr_codes_loss",
                    "hist5",
                    "hist6",
                    "hist7",
                    "hist8",
                    "hist9",
                    "hist10",
                    "hist11",
                    "hist12",
                    "hist13",
                    "hist14",
                    "hist15",
                    "raw_ber_lane0",
                    "raw_ber_lane1"]

containerArgs: ["server",
                "--config",
                "/metric-forwarder-counters/metric-forwarder-counters.yaml",
                "--nmxmgr.victoria-metric.prometheus-import-api=insert/0/prometheus/api/v1/import/prometheus",
                "--counters.enabled=true"]

env:
  - name: METRIC_FORWARDER_COUNTERS_KAFKA_PASSWORD
    valueFrom:
      secretKeyRef:
        name: metric-forwarder-counters
        key: password
```
{{</expand>}}

{{<expand "metric-forwarder-values-gnmi.yaml">}}

```
name: metric-forwarder-gnmi
replicaCount: 4
nameOverride: "metric-forwarder-gnmi"
fullnameOverride: "metric-forwarder-gnmi"

cmService:
  enabled: true
  content:
    nmxmgr:
      service-name: "metric-forwarder-gnmi"
      version: "1.0.0"
      admin-addr: ":9081"

      kafka:
        group-id: metric-forwarder-gnmi
        batch-size: 250
        batch-period: 3s

      http:
        compression: true

      processors:
        # GNMI
        components:
          enabled: false


      metrics:
        components:
          labels: "domain_id,name,target"
          metric: ["speed",
                   "utilization",
                   "input_current",
                   "input_voltage",
                   "output_current",
                   "output_voltage",
                   "output_power"]
      gnmi-paths:
        - path: [ "components", "component", "power-supply", "state", "input-voltage" ]
          index: 4
        - path: [ "components", "component", "power-supply", "state", "input-current" ]
          index: 4
        - path: [ "components", "component", "power-supply", "state", "output-voltage" ]
          index: 4
        - path: [ "components", "component", "power-supply", "state", "output-current" ]
          index: 4
        - path: [ "components", "component", "power-supply", "state", "output-power" ]
          index: 4
        - path: [ "components", "component", "fan", "state", "speed" ]
          index: 4
        - path: [ "components", "component", "cpu", "utilization", "state", "avg" ]
          index: 3

containerArgs: ["server",
                "--config",
                "/metric-forwarder-gnmi/metric-forwarder-gnmi.yaml",
                "--components.enabled=true",
                "--nmxmgr.victoria-metric.prometheus-import-api=insert/0/prometheus/api/v1/import/prometheus"]

env:
  - name: METRIC_FORWARDER_GNMI_KAFKA_PASSWORD
    valueFrom:
      secretKeyRef:
        name: metric-forwarder-gnmi
        key: password
```
{{</expand>}}

{{<expand "metric-forwarder-values-others.yaml">}}
```
name: metric-forwarder-others
replicaCount: 4
nameOverride: "metric-forwarder-others"
fullnameOverride: "metric-forwarder-others"

cmService:
  enabled: true
  content:
    nmxmgr:
      service-name: "metric-forwarder-others"
      version: "1.0.0"
      admin-addr: ":9081"

      kafka:
        group-id: "metric-forwarder-others"
        batch-size: 250
        batch-period: 3s

      http:
        compression: true

      processors:
        switch_temperature:
          enabled: false
        switch_fan:
          enabled: false
        switch_power:
          enabled: false
        switch_total_power_managed:
          enabled: false
        switch_power_supplies:
          enabled: false
        switch_power_supplies_managed:
          enabled: false
        switch_general:
          enabled: false
        pciinfo:
          enabled: false
        nvl_reduction_counters:
          enabled: false
        cableinfo:
          enabled: false

      metrics:
        switch_temperature:
          labels: "domain_id,node_guid,sensor_index"
          metric: [ "temperature",
                    "max_temperature" ]
        switch_fan:
          labels: "domain_id,node_guid,sensor_index"
          metric: [ "fan_speed",
                    "fan_speed_f1_managed",
                    "fan_speed_f2_managed" ]
        switch_power:
          labels: "domain_id,node_guid,sensor_index"
          metric: [ "voltage",
                    "current",
                    "feed_managed",
                    "voltage_managed",
                    "power_managed",
                    "current_managed",
                    "capacity_managed" ]
        switch_total_power_managed:
          labels: "domain_id,node_guid"
          metric: [ "total_power_managed" ]
        switch_power_supplies:
          labels: "domain_id,node_guid,psu_idx"
          metric: [ "fan_psu",
                    "temp_psu",
                    "power_consumption" ]
        switch_power_supplies_managed:
          labels: "domain_id,node_guid,psu_idx"
          metric: [ "power_managed_sup",
                    "voltage_managed_sup",
                    "current_managed_sup" ]
        switch_general:
          labels: "domain_id,node_guid"
          metric: [ "port_state_change" ]
        pciinfo:
          labels: "domain_id,node_guid"
          metric: [ "switch_voltage",
                    "switch_temperature",
                    "rx_errors",
                    "tx_errors" ]
        nvl_reduction_counters:
          labels: "domain_id,node_guid,port_num"
          metric: [ "dropped_pkt",
                    "trapped_pkt",
                    "nvl_reduction_errors" ]
        cableinfo:
          labels: "domain_id,node_guid,Port"
          metric: [ "cable_temperature",
                    "transmitter_technology",
                    "cable_vendor",
                    "rx_power_lane0",
                    "rx_power_lane1",
                    "diag_supply_voltage",
                    "WarnVoltageHighThresh",
                    "rx_cdr_lol" ]

containerArgs: ["server",
                "--config",
                "/metric-forwarder-others/metric-forwarder-others.yaml",
                "--cableinfo.enabled=true",
                "--nmxmgr.victoria-metric.prometheus-import-api=insert/0/prometheus/api/v1/import/prometheus",
                "--pciinfo.enabled=true",
                "--switch_fan.enabled=true",
                "--switch_general.enabled=true",
                "--switch_power.enabled=true",
                "--switch_power_supplies.enabled=true",
                "--switch_power_supplies_managed.enabled=true",
                "--switch_temperature.enabled=true",
                "--switch_total_power_managed.enabled=true",
                "--nvl_reduction_counters.enabled=true"]

env:
  - name: METRIC_FORWARDER_OTHERS_KAFKA_PASSWORD
    valueFrom:
      secretKeyRef:
        name: metric-forwarder-others
        key: password
```
{{</expand>}}
