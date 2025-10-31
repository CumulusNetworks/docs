---
title: Before You Install
author: NVIDIA
weight: 190
toc: 3
---

This overview is designed to help you understand the various NetQ deployment and installation options. 

## Installation Overview

Consider the following deployment options and requirements before you install the NetQ system:

| Single Server | Cluster| Scale Cluster |
| --- | --- | --- |
| On-premises or cloud | On-premises only | On-premises only |
| Network size: small<ul></ul><ul><li>1-node: Supports up to 40 switches* </li></ul>| Network size: medium<ul><li>3-node: Supports up to 100 switches*</li></ul>|  Network size: large<ul><li>3-node: Supports up to 1,000 switches and 125,000 interfaces* </li><li>5-node: Supports up to 2,000 switches and 250,000 interfaces* </li></ul>|
| KVM or VMware hypervisor | KVM or VMware hypervisor | KVM or VMware hypervisor |
| No high-availability option | High availability | High availability |
| System requirements<br><br> On-premises: 16 virtual CPUs, 64GB RAM, 500GB SSD disk<br><br>Cloud: 4 virtual CPUs, 8GB RAM, 64GB SSD disk | System requirements (per node)<br><br> On-premises: 16 virtual CPUs, 64GB RAM, 500GB SSD disk<br>|  System requirements (per node)<br><br>On-premises: 48 virtual CPUs, 512GB RAM, 3.2TB SSD disk|
| Not supported:<ul><li>NVLink monitoring</li></ul> Limited support: <ul><li>OpenTelemetry (OTLP) metrics (on-prem only)</li><li>Grafana integration (on-prem only)</li><li>Slurm integration (on-prem only)</li><li>Cable validations (on-prem only)</li></ul> | Not supported:<ul><li>NVLink monitoring</li>|  Not supported:<ul><li>Network snapshots</li><li>Trace requests</li><li>Flow analysis</li><li>MAC commentary</li><li>Duplicate IP address validations</li></ul> Limited support: <ul><li>Link health view (beta)</li></ul>|

*When switches are {{<link title="Integrate NetQ with Grafana/#requirements-and-support" text="configured with both OpenTelemetry (OTLP)">}} and the NetQ agent, switch support per deployment model is reduced by half.

## Deployment Type: On-Premises or Cloud

**On-premises deployments** are hosted at your location and require the in-house skill set to install, configure, back up, and maintain NetQ. This model is a good choice if you want very limited or no access to the internet from switches and hosts in your network. 

In the **cloud deployment**, you host only a small, local server on your premises that connects to the NetQ cloud service over selected ports or through a proxy server. NetQ cloud supports local data aggregation and forwarding---the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage.

In all deployment models, NetQ agents reside on the switches and hosts they monitor in your network.

## Server Arrangement: Single or Cluster

### Single Server

A standalone server is easier to set up, configure, and manage, but limits your ability to scale your network monitoring. Deploying multiple servers allows you to limit potential downtime and increase availability by having more than one server that can run the software and store the data. Select the standalone, single-server arrangement for smaller, simpler deployments.

### Cluster of Servers

NVIDIA offers two types of cluster deployments: cluster and scale cluster. Both deployments are available on-premises and offer high-availability and provide redundancy in case of node failure. 

The **cluster** implementation comprises three servers: one master and two workers nodes. NetQ supports high availability using a virtual IP address. Even if the master node fails, NetQ services remain operational. However, keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster&mdash;such as upgrading NetQ or rescheduling pods to other workers if a worker goes down&mdash;will not work. During the installation process, you configure a virtual IP address that enables redundancy for the Kubernetes control plane. In this configuration, the majority of nodes must be operational for NetQ to function. For example, a three-node cluster can tolerate a one-node failure, but not a two-node failure. For more information, refer to the {{<exlink url="https://etcd.io/docs/v3.3/faq/" text="etcd documentation">}}.

As an alternative to the three-node cluster deployment with a virtual IP address, you can use an external load balancer to provide high availability for the NetQ API and the NetQ UI.

The **scale cluster** deployment supports large networks and offers the highest level of scalability, allowing you to adjust NetQ's network monitoring capacity by adding additional nodes to your cluster as your network expands. For example, you can deploy a three-node scale cluster that accommodates up to 1,000 switches. When you add more switches to your network, the extensible framework allows you to add two additional nodes that can accommodate a network of up to 2,000 switches. NVIDIA recommends this on-premises option for networks comprising 100 or more switches with 100 or more interfaces per switch.  

{{%notice note%}}
Large networks have the potential to generate a large amount of data. For large networks, NVIDIA does not recommend using the NetQ CLI; additionally, {{<link title="Access Data with Cards/#table-settings" text="tabular data in the UI">}} is limited to 10,000 rows. If you need to review a large amount of data, NVIDIA recommends downloading and exporting the tabular data as a CSV or JSON file and analyzing it in a spreadsheet program.
{{%/notice%}}
## Base Command Manager

NetQ is also available through NVIDIA's cluster management software, Base Command Manager. Refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}} for instructions on how to launch and configure NetQ using Base Command Manager.

## Next Steps

After you've decided on your deployment type, you're ready to {{<link title="Install the NetQ System" text="install NetQ">}}.