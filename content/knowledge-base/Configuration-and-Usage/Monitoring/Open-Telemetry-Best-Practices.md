---
title: Open Telemetry Best Practices
author: NVIDIA
weight: 382
toc: 4
draft: true
---
This knowledge base article outlines best practices for collecting and managing telemetry data from NVIDIA switches using <span class="a-tooltip">[OTLP](## "OpenTelemetry")</span>. These best practices are based on the experience of various customers and ensure efficient data collection, optimized data transfer, and scalable <span class="a-tooltip">[TSDB](## "Time Series Database")</span> storage.

{{%notice note%}}
NVIDIA only provides best practices as seen by customer clusters; each component has its own satellites, configurations, and maintenance expertise.
{{%/notice%}}

## Telemetry Components

{{<img src="/images/knowledge-base/otel-best-practices.png">}}

## The Collector

Use a collector if the TSDB does not support OTLP ingestion.

{{%notice note%}}
An OpenTelemetry collector is optional as the switch can push directly to a TSDB that supports OTLP ingestion.
{{%/notice%}}

The NVIDIA switch exports OTLP metrics, while some TSDBs can only ingest  <span class="a-tooltip">[PRW](## "Prometheus Remote Write")</span>; NVIDIA recommends you use an OpenTelemetry collector to aggregate telemetry data from the switch and export the data to TSDB through PRW.

Follow these key guidelines:
- Switch-to-Collector Communication - Each switch must send telemetry data to a single OpenTelemetry collector instance (sticky assignment). This avoids issues related to out-of-order data processing and ensures consistent metadata association.
- Collector Scalability - You can deploy the OpenTelemetry collector with multiple replicas to handle high telemetry throughput. Configure load balancing to ensure each switch maintains a persistent connection to a single collector instance.
- Deployment Considerations:
  - Collector CPU and memory usage might vary depending on scale, setup, and other environment considerations.
  - If a backend TSDB causes backpressure, the queue grows on the collector, which increases memory usage. As a guideline, the collector exporter queue size should be 0.

## Data Export to TSDB

After the OpenTelemetry collector receives data, you need to push it to a TSDB for storage and analysis using either the OTLP or PRW protocols, depending on the TSDB supported ingestion methods.

Follow these best practices for pushing data to the TSDB:
- (Collector only) Configure the OpenTelemetry collector to batch telemetry data before pushing it to the TSDB to reduce network overhead and improve ingestion performance.
- Protocol selection:
  - If the TSDB supports OTLP ingestion, configure the OpenTelemetry collector or switch directly to push data in OTLP format. Using a collector reduces the load as the collector has to do less processing and increases the load on the TSDB that translates OTLP to the proprietary internal protocol.
  - If the TSDB only supports PRW, configure the collector accordingly.
- (Collector only) Consider incorporating compression to reduce network bandwidth.
- Use load balancing to ensure that the TSDB can handle multiple write requests efficiently by distributing the load across available instances (see {{<link url="#tsdb" text="TSDB">}}).

## TSDB

For scalable and efficient telemetry storage, NVIDIA recommends you use a high-performance TSDB, such as:
- {{<exlink url="https://thanos.io/" text="Thanos">}} is a <span class="a-tooltip">[CNCF](## " Cloud Native Computing Foundation")</span>, has high resiliency, and will support OTLP in upcoming releases.
- {{<exlink url="https://grafana.com/docs/mimir/latest/" text="Mimir">}} from Grafana Labs supports OTLP ingestion.
- {{<exlink url="https://victoriametrics.com/" text="VictoriaMetrics">}} is a growing ecosystem and supports OTLP ingestion.

Key Considerations:
- Given the scale of the VAST data center and number of switches, Prometheus might not be able to hold the scale without some deep modifications and optimizations.
- If your telemetry stack is already built around Prometheus, all three databases provide PromQL query language support.
- VictoriaMetrics offers OTLP support. Others will add support with time at various maturity levels.
- Ensure your TSDB can handle the expected data ingestion rate and retention policy based on your network size and telemetry volume. The three TSDBs can scale on the receiving side and on the storage side. Refer to the specific documentation to learn about how to scale.

## Resource Requirements for VAST Scale

Based on VAST’s scale of 68 switches and increasing in number, and a sampling rate of 15 to 30 seconds, the following approximate resources are required for ingestion using OTLP (PRW typically demands more resources), along with VictoriaMetrics TSDB:

Collector requirements [optional]:
- Number of Collectors: 1-2 OpenTelemetry collectors, each with one CPU and 1GB of RAM.

TSDB requirements (VictoriaMetrics Example):
- VMInsert - Four containers, each with one CPU and 2GB RAM.
- VMStorage - Four containers, each with one CPU and 2GB RAM.
- VMSelect - Query service depends on the nature and number of queries.

## Conclusion

Implementing a robust switch telemetry collection system using OpenTelemetry and a scalable TSDB ensures reliable network monitoring and observability. Following these best practices help you optimize performance, reduce operational overhead, and enhance long-term data retention capabilities. For further assistance, reach out to NVIDIA Support or consult the official OpenTelemetry and TSDB documentation.

## Related Information

- {{<exlink url="https://github.com/thanos-io/thanos" text="Thanos (Github)">}}
- {{<exlink url="https://thanos.io/" text="Thanos">}}
- {{<exlink url="https://github.com/grafana/mimir" text="Mimir (Github)">}}
- {{<exlink url="https://grafana.com/docs/mimir/latest/" text="Mimir">}}
- {{<exlink url="https://github.com/VictoriaMetrics/VictoriaMetrics" text="VictoriaMetrics (Github)">}}
- {{<exlink url="https://victoriametrics.com/" text="VictoriaMetrics">}}
- {{<exlink url="https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/main/exporter/prometheusremotewriteexporter" text="OpenTelemetry Prometheus Remote Write Exporter">}}
- {{<exlink url="https://github.com/open-telemetry/opentelemetry-collector/tree/main/exporter/otlpexporter" text="OpenTelemetry OTLP gRPC Exporter">}}
- {{<exlink url="https://github.com/open-telemetry/opentelemetry-collector/tree/main/exporter/otlphttpexporter" text="OpenTelemetry OTLP HTTP Exporter">}}