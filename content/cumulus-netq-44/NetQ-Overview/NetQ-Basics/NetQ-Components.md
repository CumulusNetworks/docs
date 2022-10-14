---
title: NetQ Components
author: NVIDIA
weight: 60
toc: 4
---

NetQ contains the following applications and key components:

- Telemetry data collection and aggregation via
  - NetQ switch agents
  - NetQ host agents
  - Database
- Data streaming
- Network services
- User interfaces

While these functions apply to both the on-premises and cloud solutions, they are configured differently, as shown in the following diagrams.

{{<figure src="/images/netq/netq-comps-onpremises-230.png" alt="diagram of NetQ on-premises configuration" width="700">}}

{{<figure src="/images/netq/netq-comps-cloud-230.png" alt="diagram of NetQ cloud configuration" width="450">}}

## NetQ Agents

NetQ Agents are installed via software and run on every monitored node in the network&mdash;including Cumulus® Linux® switches, Linux bare metal hosts, and virtual machines. The NetQ Agents push network data regularly and event information immediately to the NetQ Platform.

### Switch Agents

The NetQ Agents running on Cumulus Linux or SONiC switches gather the following network data via {{<exlink url="https://tools.ietf.org/html/rfc3549" text="Netlink">}}:

  - Interfaces
  - IP addresses (v4 and v6)
  - IP routes (v4 and v6)
  - Links
  - Bridge FDB (MAC address table)
  - ARP Entries/Neighbors (IPv4 and IPv6)

for the following protocols:

  - Bridging protocols: LLDP, STP, MLAG
  - Routing protocols: BGP, OSPF
  - Network virtualization: EVPN, VXLAN

### Host Agents

The NetQ Agents running on hosts gather the same information as that for switches, plus the following network data:

  - Network IP and MAC addresses
  - Container IP and MAC addresses

The NetQ Agent obtains container information by listening to the Kubernetes orchestration tool.

## NetQ Core

The NetQ core performs the data collection, storage, and processing for delivery to various user interfaces. It consists of a collection of scalable components running entirely within a single server. The NetQ software queries this server, rather than individual devices, enabling greater system scalability.

### Data Aggregation

The data aggregation component collects data coming from all of the NetQ Agents. It then filters, compresses, and forwards the data to the streaming component. The server monitors for missing messages and also monitors the NetQ Agents themselves, sending notifications about events when appropriate. In addition to the telemetry data collected from the NetQ Agents, the aggregation component collects information from the switches and hosts, such as vendor, model, version, and basic operational state.

### Data Stores

NetQ uses two types of data stores. The first stores the raw data, data aggregations, and discrete events needed for quick response to data requests. The second stores data based on correlations, transformations, and raw-data processing.

<!-- vale off -->
### Real-time Streaming
<!-- vale on -->

The streaming component processes the incoming raw data from the aggregation server in real time. It reads the metrics and stores them as a time series, and triggers alarms based on anomaly detection, thresholds, and events.

### Network Services

The network services component monitors protocols and services operation individually and on a networkwide basis and stores status details.

### User Interfaces

NetQ data is available through several interfaces:

  - NetQ CLI (command-line interface)
  - NetQ GUI (graphical user interface)
  - NetQ RESTful API (representational state transfer application programming interface)

The CLI and UI query the RESTful API to present data. NetQ can integrate with event notification applications and third-party analytics tools.
