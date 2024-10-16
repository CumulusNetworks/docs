---
title: Before You Install
author: NVIDIA
weight: 190
toc: 3
---

This overview is designed to help you understand the various NetQ deployment and installation options. 

## Installation Overview

Consider the following deployment options and requirements before you install the NetQ system: <!--add BCM column?-->

| Single Server | Three-Node Cluster| Scale Cluster |
| --- | --- | --- |
| On-prem or cloud | On-prem or cloud | On-prem only |
| Low scale<ul><li>Single server supports up to TKTK devices</li></ul>| Medium scale<ul><li>3-node deployment supports up to 150 devices and 1500 interfaces</li></ul>|  High scale<ul><li>3-node deployment supports up to 1000 devices</li><li>5-node deployment supports up to 2000 devices</li><li>7-node deployment supports up to 3000 devices</li></ul>|
| KVM or VMware hypervisor | KVM or VMware hypervisor | KVM or VMware hypervisor |
| System requirements:<ul><li>TKTK</li></ul>| System requirements (per node):<ul><li>TKTK</li></ul>|  System requirements (per node):<ul><li>48 virtual CPUs</li><li>512GB RAM</li><li>3.2TB SSD</li></ul>|
| All features supported | All features supported|  Limited or no support for:<ul><li>Topology dashboard</li><li>Network snapshots</li><li>Trace requests</li><li>Flow analysis</li><li>Duplicate IP address validations</li><li>MAC move commentary</li></ul>|

## Deployment Type: On-premises or Cloud

**On-premises deployments** are hosted at your location and require the in-house skill set to install, configure, back up, and maintain NetQ. This model is a good choice if you want very limited or no access to the internet from switches and hosts in your network. In the **cloud deployment**, you host only a small, local server on your premises that connects to the NetQ cloud service over selected ports or through a proxy server. NetQ cloud supports local data aggregation and forwarding---the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage.

In all deployment models, the NetQ Agents reside on the switches and hosts they monitor in your network.

## Server Arrangement: Single or Cluster

A **single server** is easier to set up, configure, and manage, but can limit your ability to scale your network monitoring quickly. Deploying multiple servers is more complicated, but you limit potential downtime and increase availability by having more than one server that can run the software and store the data. Select the standalone, single-server arrangements for smaller, simpler deployments.

Select the **three-node cluster** arrangement to obtain for greater device support and high availability for your network. The clustering implementation comprises three servers: one master and two workers. In a clustered environment, NVIDIA recommends installing the virtual machines on different physical servers to increase redundancy in the event of a hardware failure. NetQ supports high availability server-cluster deployments using a virtual IP address. Even if the master node fails, NetQ services remain operational. However, keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster&mdash;such as upgrading NetQ or rescheduling pods to other workers if a worker goes down&mdash;will not work.

During the installation process, you configure a virtual IP address that enables redundancy for the Kubernetes control plane. In this configuration, the majority of nodes must be operational for NetQ to function. For example, a three-node cluster can tolerate a one-node failure, but not a two-node failure. For more information, refer to the {{<exlink url="https://etcd.io/docs/v3.3/faq/" text="etcd documentation">}}. <!--how do we want to frame this? when will we stop promoting?-->

The **scale cluster** deployment provides support for the most number of devices. It is extensible: as your network grows, you can add additional nodes to the cluster to accommodate more devices. 

### Cluster Deployments and Load Balancers

As an alternative to the three-node cluster deployment with a virtual IP address, you can use an external load balancer to provide high availability for the NetQ API and the NetQ UI.

However, you need to be mindful of where you {{<link title="Install a Custom Signed Certificate" text="install the certificates">}} for the NetQ UI (port 443); otherwise, you cannot access the NetQ UI. If you are using a load balancer in your deployment, NVIDIA recommends that you install the certificates directly on the load balancer for SSL offloading. However, if you install the certificates on the master node, then configure the load balancer to allow for SSL passthrough.

## Next Steps

After you've decided on your deployment type, you're ready to {{<link title="Install the NetQ System" text="install NetQ">}}.

Alternately, you can launch NetQ using NVIDIA Base Command Manager. To get started, refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}}.