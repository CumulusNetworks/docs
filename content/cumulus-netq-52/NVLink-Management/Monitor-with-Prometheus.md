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

<!--4.15 what about username and password-->

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