---
title: OpenTelemetry Best Practices
author: NVIDIA
weight: 382
toc: 4
---
<span class="a-tooltip">[NCCL](## "NVIDIA Collective Communications Library")</span> and AI workloads operate in environments where every millisecond counts. High frequency telemetry in the datacenter fabric is critical for continuation of the service, and meeting <span class="a-tooltip">[SLAs](## "Service Level Agreements")</span>.

AI and NCCL workloads rely on highly synchronized, low-latency communication between multiple GPUs and nodes. Even slight network delays or congestion can bottleneck training or inference and constant, granular monitoring helps detect and address issues before they impact performance. With frequent telemetry, AI fabric operators can spot performance degradations, packet loss, or hardware faults in near real time. This immediate visibility allows for proactive troubleshooting and dynamic adjustments, keeping distributed operations smooth.

As AI workloads scale across many nodes, any inefficiency in the network fabric can lead to significant cumulative delays. Telemetry at high frequency ensures that these scaling challenges are met with data-driven optimizations, sustaining overall system efficiency.

Telemetry requires correct planning and dimensioning for implementation. You need to know how to design and implement your telemetry environment keeping the scaling of your cluster in consideration.  

This knowledge base article outlines best practices for collecting and managing telemetry data from NVIDIA switches using <span class="a-tooltip">[OTLP](## "OpenTelemetry")</span>. These best practices are based on the experience of various customers and ensure efficient data collection, optimized data transfer, and scalable <span class="a-tooltip">[TSDB](## "Time Series Database")</span> storage.

{{%notice note%}}
NVIDIA only provides best practices as seen by customer clusters; each component has its own lifecycle and maintenance expertise.
{{%/notice%}}

## Telemetry Components

{{<img src="/images/knowledge-base/otel-best-practices.png">}}

## The Collector

Use a collector if the TSDB does not support OTLP ingestion.

{{%notice note%}}
An OpenTelemetry collector is optional; the switch is able to push directly to a TSDB that supports OTLP ingestion.
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
  - If the TSDB supports OTLP ingestion, configure the OpenTelemetry collector or switch directly to push data in OTLP format. Using a collector reduces the load as the collector has to do less processing but increases the load on the TSDB that translates OTLP to the proprietary internal protocol.
  - If the TSDB only supports PRW, configure the collector accordingly.
- (Collector only) Consider incorporating compression to reduce network bandwidth.
- Use load balancing to ensure that the TSDB can handle multiple write requests efficiently by distributing the load across available instances (see {{<link url="#tsdb" text="TSDB">}}).

## TSDB

For scalable and efficient telemetry storage, NVIDIA recommends you use a high-performance TSDB, such as:
- {{<exlink url="https://thanos.io/" text="Thanos">}} is a <span class="a-tooltip">[CNCF](## " Cloud Native Computing Foundation")</span>, Incubating project. Thanos is a set of components that can be composed into a highly available metric system with unlimited storage capacity, which can be added seamlessly on top of existing Prometheus deployments.
- {{<exlink url="https://grafana.com/docs/mimir/latest/" text="Mimir">}} from Grafana Labs supports OTLP ingestion.
- {{<exlink url="https://victoriametrics.com/" text="VictoriaMetrics">}} is a growing ecosystem and supports OTLP ingestion.

Key Considerations:
- Given the scale of AI data centers and the number of switches, Prometheus might not be able to hold the scale without some deep modifications and optimizations.
- If your telemetry stack is already built around Prometheus, all three databases provide PromQL query language support.
- Mimir and VictoriaMetrics supports OTLP currently. Thanos will support OTLP soon.
- Ensure that your TSDB can handle the expected data ingestion rate and retention policy based on your network size and telemetry volume. The three TSDBs can scale on the receiving side and on the storage side. Refer to the {{<link url="#related-information" text="specific documentation">}} to learn about how to scale.

## Resource Requirements for Scale

Based on internal validation and a customer deployment fabric with around 50 switches and a sampling rate of 15 to 30 seconds, the following approximate resources are required for ingestion using OTLP (PRW typically demands more resources), along with VictoriaMetrics TSDB:  

Collector requirements (optional):
- Number of Collectors: 1-2 OpenTelemetry collectors, each with one CPU and 1GB of RAM.

TSDB requirements (VictoriaMetrics Example):
- VMInsert - Four containers, each with 1 CPU and 2GB RAM.
- VMStorage - Four containers, each with 1 CPU and 2GB RAM.
- VMSelect - Query service depends on the nature and number of queries.

{{%notice note%}}
The above numbers above are just estimates, actual numbers might vary.
{{%/notice%}}

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