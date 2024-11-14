---
title: Before You Install
author: NVIDIA
weight: 190
toc: 3
---

This overview is designed to help you understand the various NetQ deployment and installation options. 

## Installation Overview

Consider the following deployment options and requirements before you install the NetQ system: <!--add BCM column?-->

| Single Server | High-Availability Cluster| High-Availability Scale Cluster |
| --- | --- | --- |
| On-premises or cloud | On-premises or cloud | On-premises only |
| Network size: small<ul></ul>| Network size: medium<ul><li>Supports up to 100 switches and 128 interfaces per switch*</li></ul>|  Network size: large<ul><li>Supports up to 1,000 switches and 125 interfaces per switch*</li></ul>|
| KVM or VMware hypervisor | KVM or VMware hypervisor | KVM or VMware hypervisor |
| System requirements<br><br> On-premises: 16 virtual CPUs, 64GB RAM, 500GB SSD disk<br><br>Cloud: 4 virtual CPUs, 8GB RAM, 64GB SSD disk | System requirements (per node)<br><br> On-premises: 16 virtual CPUs, 64GB RAM, 500GB SSD disk<br><br>Cloud: 4 virtual CPUs, 8GB RAM, 64GB SSD disk |  System requirements (per node)<br><br>On-premises: 48 virtual CPUs, 512GB RAM, 3.2TB SSD disk|
| All features supported | All features supported|  No support for:<ul><li>Network snapshots</li><li>Trace requests</li><li>Flow analysis</li><li>Duplicate IP address validations</li><li>MAC commentary</li><li>Link health view</li></ul> Limited support for:<ul><li>Topology validations</li></ul>|

*Exact device support counts can vary based on multiple factors, such as the number of links, routes, and IP addresses in your network. Contact NVIDIA for assistance in selecting the appropriate deployment model for your network.


## Deployment Type: On-Premises or Cloud

**On-premises deployments** are hosted at your location and require the in-house skill set to install, configure, back up, and maintain NetQ. This model is a good choice if you want very limited or no access to the internet from switches and hosts in your network. 

In the **cloud deployment**, you host only a small, local server on your premises that connects to the NetQ cloud service over selected ports or through a proxy server. NetQ cloud supports local data aggregation and forwarding---the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage.

In all deployment models, the NetQ Agents reside on the switches and hosts they monitor in your network.

## Server Arrangement: Single or Cluster

A **single server** is easier to set up, configure, and manage, but limits your ability to scale your network monitoring. Deploying multiple servers allows you to limit potential downtime and increase availability by having more than one server that can run the software and store the data. Select the standalone, single-server arrangement for smaller, simpler deployments.

The **high-availability cluster** deployment supports a greater number of switches and provides high availability for your network. The clustering implementation comprises three servers: one master and two workers nodes. NetQ supports high availability server-cluster deployments using a virtual IP address. Even if the master node fails, NetQ services remain operational. However, keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster&mdash;such as upgrading NetQ or rescheduling pods to other workers if a worker goes down&mdash;will not work.

During the installation process, you configure a virtual IP address that enables redundancy for the Kubernetes control plane. In this configuration, the majority of nodes must be operational for NetQ to function. For example, a three-node cluster can tolerate a one-node failure, but not a two-node failure. For more information, refer to the {{<exlink url="https://etcd.io/docs/v3.3/faq/" text="etcd documentation">}}.

The **high-availability scale cluster** deployment provides the same benefits as the high-availability cluster deployment, but supports larger networks of up to 1,000 switches. NVIDIA recommends this option for networks that have over 100 switches and at least 100 interfaces per switch. It offers the highest level of scalability, allowing you to adjust NetQ's network monitoring capacity as your network expands. Depending on the size of your network, NetQ might experience delays in data retrieval. NVIDIA recommends exporting the data provided by NetQ as a CSV or JSON file when possible. 

<!--As the number of devices in your network grows, you can add additional nodes to the cluster to support the additional devices. 4.12 supports only 3-node cluster-->

### Cluster Deployments and Load Balancers

As an alternative to the three-node cluster deployment with a virtual IP address, you can use an external load balancer to provide high availability for the NetQ API and the NetQ UI.

However, you need to be mindful of where you {{<link title="Install a Custom Signed Certificate" text="install the certificates">}} for the NetQ UI (port 443); otherwise, you cannot access the NetQ UI. If you are using a load balancer in your deployment, NVIDIA recommends that you install the certificates directly on the load balancer for SSL offloading. However, if you install the certificates on the master node, then configure the load balancer to allow for SSL passthrough.

## Base Command Manager

NetQ is also available through NVIDIA Base Command Manager. To get started, refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}}.

## Next Steps

After you've decided on your deployment type, you're ready to {{<link title="Install the NetQ System" text="install NetQ">}}.