---
title: Before You Install
author: NVIDIA
weight: 190
toc: 3
---

This overview is designed to help you understand the various NetQ deployment and installation options.

## Installation Overview

Consider the following deployment options and requirements before you install the NetQ system. 

| Single Server | Cluster| Scale Cluster |
| --- | --- | --- |
| On-premises only | On-premises only | On-premises only |
| Network size: small<ul></ul><ul><li>1-node: Supports up to 40 switches* </li></ul>| Network size: medium<ul><li>3-node: Supports up to 100 switches*</li></ul>|  Network size: large<ul></ul><ul><li>Support varies based on number of nodes. See {{<link title="Before You Install/#server-arrangement" text="Server Arrangement">}}.</li></ul> |
| KVM or VMware hypervisor | KVM or VMware hypervisor | KVM or VMware hypervisor |
| No high-availability option | High-availability | High-availability |
| System requirements:<ul></ul><ul><li>16 virtual CPUs</li><li>64GB RAM</li><li>500GB SSD disk</li></ul>| System requirements (per node):<ul></ul><ul><li>16 virtual CPUs</li><li>64GB RAM</li><li>500GB SSD disk</li></ul>| System requirements (per node): <ul></ul><ul><li>48 virtual CPUs</li><li>512GB RAM </li><li>3.2TB SSD disk</li></ul>|
| Not supported:<ul><li>NVLink monitoring</li></ul> | Not supported:<ul><li>NVLink monitoring</li>|  Not supported:<ul><li>Network snapshots</li><li>Trace requests</li><li>Flow analysis</li><li>MAC commentary</li><li>Duplicate IP address validations</li></ul> Limited support: <ul><li>Link health view (beta)</li></ul>|

*When switches are {{<link title="Integrate NetQ with Grafana/#requirements-and-support" text="configured with both OpenTelemetry (OTLP)">}} and the NetQ agent, switch support per deployment model is reduced by half.<br>


## Server Arrangement

**Single server**: A standalone server is easier to set up, configure, and manage, but limits your ability to scale your network monitoring and provides no redundancy in case of a hardware failure.

**Cluster**: The cluster deployment comprises three servers: one master and two workers nodes. NetQ supports high-availability using a virtual IP address. Even if the master node fails, NetQ services remain operational.

**Scale cluster**: The scale cluster deployment is intended for large network environments and allows you to expand NetQ monitoring capacity by adding nodes as your network grows. NVIDIA typically recommends this deployment for environments with 100 or more switches. It is the only deployment model that supports monitoring for {{<exlink url="https://www.nvidia.com/en-us/data-center/nvlink/" text="NVIDIA NVLink">}}, {{<exlink url="https://www.nvidia.com/en-us/networking/spectrumx/" text="NVIDIA Spectrum-X Ethernet">}}, as well as mixed Ethernet and NVLink networks.

The following table shows high-level device support per-node for Ethernet-only, NVLink-only, and combined deployments. This deployment model is currently in beta for clusters larger than 5 nodes. See {{<link title="Before You Install/#verified-limits" text="Verified Limits">}} for detailed testing information.

| Deployment                    | 3 Nodes                         | 4 Nodes                          | 5 Nodes                          | 6 Nodes                          | 7 Nodes                          | 8 Nodes                          | 9 Nodes                          |
|------------------------------|---------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|----------------------------------|
| Exclusively Ethernet         | 500 switches, 2K hosts          | 750 switches, 3K hosts           | 1000 switches, 4K hosts          | 1250 switches, 5K hosts          | 1500 switches, 6K hosts          | 1750 switches, 7K hosts          | 2000 switches, 8K hosts          |
| Exclusively NVLink           | 128 NVL                         | 160 NVL                          | 192 NVL                          | 224 NVL                          | 256 NVL                          | 288 NVL                          | 320 NVL                          |
| Ethernet and NVLink combined | 250 switches, 1K hosts, 64 NVL | 375 switches, 1.5K hosts, 96 NVL | 500 switches, 2K hosts, 128 NVL  | 625 switches, 2.5K hosts, 160 NVL| 750 switches, 3K hosts, 192 NVL  | 875 switches, 3.5K hosts, 224 NVL| 1K switches, 4K hosts, 256 NVL   |


{{%notice note%}}

In both cluster deployments, the majority of nodes must be operational for NetQ to function. For example, a three-node cluster can tolerate a one-node failure, but not a two-node failure. Similarly, a five-node cluster can tolerate a two-node failure, but not a three-node failure. If the majority of failed nodes are Kubernetes control plane nodes, NetQ will no longer function. For more information, refer to the {{<exlink url="https://etcd.io/docs/v3.3/faq/" text="etcd documentation">}}.
{{%/notice%}}
## Verified Limits

The following values have been explicitly tested and validated, but they might not reflect the maximum theoretical system limits for NetQ.

| Deployment Type | Verified Features | Verified Scale Limit | Data Rate | Hardware Requirements |
|-----------------|-------------------|-------|-----------|-----------------------|
| 6-node scale cluster: Ethernet + NVLink | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations<br>- Switch OTLP data collection<br>- DPU OTLP data collection<br>- NVLink data collection: topology, partitions, metrics | - Ethernet switches: 675 (GPUs: 32K)<br>- DPUs: 8K (OTLP data)<br>- NVLink: 450 GB with 72x1 configuration | - NetQ Agent: ~7 Mbps<br>- OTLP switch: 445 MB/s (3.56 Gbps)<br>- OTLP host: 1,000,000 samples/s at 10-second interval<br>- NVLink: ~32,000 messages/s (2,628 ports)<br>- Counters: 112 per GB/s | 6 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 6-node scale cluster: Ethernet + NVLink | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations<br>- Switch OTLP data collection<br>- DPU OTLP data collection | - Ethernet switches: 1,300 (GPUs: 55K)<br>- DPUs: 14K (OTLP data) | - NetQ Agent: ~7 Mbps<br>- OTLP switch: 445 MB/s (3.56 Gbps)<br>- OTLP host: 1,718,750 samples/s at 10-second interval | 6 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 5-node scale cluster: Ethernet + NVLink (Ethernet agent only) | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations | - Ethernet switches: 1,300 (GPUs: 55K) | - NetQ Agent: ~14 Mbps | 5 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 3-node scale cluster: Ethernet + NVLink | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations<br>- Switch OTLP data collection<br>- DPU OTLP data collection<br>- NVLink data collection: topology, partitions, metrics | - Ethernet switches: 250 (GPUs: 8K)<br>- DPUs: 1K (OTLP data)<br>- NVLink: 100 GB with 72x1 configuration | - NetQ Agent: 2.5 Mbps<br>- OTLP switch: 165 MB/s (1.32 Gbps)<br>- OTLP host: 250,000 samples/s at 10-second interval<br>- NVLink: ~9,200 messages/s (2,628 ports)<br>- Counters: 112 per GB/s | 3 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 3-node scale cluster: Ethernet-only | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations<br>- Ethernet OTLP data collection | - Ethernet switches: 500 (GPUs: 16K)<br>- DPUs: 2K (OTLP data) | - NetQ Agent: 5 Mbps<br>- OTLP switch: 330 MB/s (2.64 Gbps)<br>- OTLP host: 500,000 samples/s at 10-second interval | 3 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 3-node scale cluster: NVLink-only | - NVLink data collection: topology, partitions, metrics | - NVLink: 110 GB with 72x1 configuration<br>- Partitions: 1,600 | - NVLink: ~10,000 messages/s (2,628 ports)<br>- Counters: 112 per GB/s | 3 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 5-node scale cluster: Ethernet-only | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations<br>- Ethernet OTLP data collection | - Ethernet switches: 1,000 (GPUs: 32K)<br>- DPUs: 4K (OTLP data) | - NetQ Agent: 10 Mbps<br>- OTLP switch: 660 MB/s (5.28 Gbps)<br>- OTLP host: 1,000,000 samples/s at 10-second interval | 5 nodes, each with:<br>  - 48 vCPUs<br>  - 512 GB RAM<br>  - 3 TB SSD/NVMe |
| 3-node cluster (non-scale): Ethernet-only | - Ethernet agent features: WJH, RoCE, histograms, adaptive routing, interfaces, inventory, BGP sessions, validations<br>- Ethernet OTLP data collection | - Ethernet switches: 50 (GPUs: 1.6K) | - NetQ Agent: 500 Kbps<br>- OTLP switch: 33 MB/s (264 Mbps)<br>- OTLP host: 50,000 samples/s at 10-second interval | 3 nodes, each with:<br>  - 16 vCPUs<br>  - 64 GB RAM<br>  - 500 GB SSD/NVMe |

{{%notice note%}}
Large networks have the potential to generate a large amount of data. For large networks, NVIDIA does not recommend using the NetQ CLI; additionally, {{<link title="Access Data with Cards/#table-settings" text="tabular data in the UI">}} is limited to 10,000 rows. If you need to review a large amount of data, NVIDIA recommends downloading and exporting the tabular data as a CSV or JSON file and analyzing it in a spreadsheet program.
{{%/notice%}}

## Base Command Manager

NetQ is also available through NVIDIA's cluster management software, Base Command Manager. Refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}} for instructions on how to launch and configure NetQ using Base Command Manager.

## Next Steps

After you've decided on your deployment type, you're ready to {{<link title="Install the NetQ System" text="install NetQ">}}.