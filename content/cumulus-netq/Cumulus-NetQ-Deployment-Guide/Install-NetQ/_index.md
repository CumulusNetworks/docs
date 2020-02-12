---
title: Install NetQ
author: Cumulus Networks
weight: 60
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 3
---
## Overview

The complete Cumulus NetQ solution contains several components that must be installed, including the NetQ applications, the database, and the NetQ Agents. NetQ can be deployed in two arrangements:

- All components installed locally (the applications and database are installed as a single entity, called the NetQ Platform); known hereafter as the on-premises solution
- Only the aggregation and forwarding application installed locally, with the database and all other applications installed in the cloud; known hereafter as the cloud solution

The NetQ Agents reside on the switches and hosts being monitored in your network.

For the on-premises solution, the NetQ Agents collect and transmit data from the switches and/or hosts back to the NetQ Platform, which in turn processes and stores the data in its database. This data is then provided for display through several user interfaces.

{{< figure src="/images/netq/install-onprem-basic-240.png" width="600">}}

For the cloud solution, the NetQ Agent function is exactly the same, transmitting collected data, but instead sends it to the NetQ Platform containing only the aggregation and forwarding application. This platform then transmits this data to Cumulus Networks cloud-based infrastructure for further processing and storage. This data is then provided for display through the same user interfaces as the on-premises solution. In this solution, the browser interface can be pointed to the local NetQ Cloud Platform/Appliance or directly to *netq.cumulusnetworks.com*.

{{< figure src="/images/netq/install-cloud-basic-240.png" width="700">}}

## Installation Choices

There are several choices that you must make to determine what steps you need to perform to install the NetQ solution. First and foremost, you must determine whether you intend to deploy the solution fully on your premises or if you intend to deploy the cloud solution. Secondly, you must decide whether you are going to deploy a Virtual Machine on your own hardware or use one of the Cumulus NetQ appliances. Thirdly, you also must determine whether you want to install the software on a single server or as a server cluster. Finally, if you have an existing on-premises solution and want to save your existing NetQ data, you must backup that data before installing the new software.

{{< figure src="/images/netq/install-decision-tree-240.png" width="400">}}

### Choose between On-premises or Cloud Deployment

Both deployments provide secure access to data and features useful for monitoring and troubleshooting your network, and each has its benefits.

It is common to select an on-premises deployment model if you want to host all required hardware and software at your location, and you have the in-house skill set to install, configure, and maintain it—including performing data backups, acquiring and maintaining hardware and software, and integration and license management. This model is also a good choice if you want very limited or no access to the Internet from switches and hosts in your network. Some companies simply want complete control of the their network, and no outside impact.

If, however, you find that you want to host only a small server on your premises and leave the details up to Cumulus Networks, then a cloud deployment might be the right choice for you. With a cloud deployment, a small local server connects to the NetQ Cloud service over selected ports or through a proxy server. Only data aggregation and forwarding is supported. The majority of the NetQ applications are hosted and data storage is provided in the cloud. Cumulus handles the backups and maintenance of the application and storage. This model is often chosen when it is untenable to support deployment in-house or if you need the flexibility to scale quickly, while also reducing capital expenses.

### Choose between a Virtual Machine or Cumulus NetQ Appliance

Both options ultimately provide the same services and features. The difference is in the implementation. When you choose to install NetQ software on your own hardware, you create and maintain a KVM or VMware VM, and the software is run from there. This requires you to scope and order an appropriate hardware server to support the NetQ requirements, but may allow you to reuse an existing server in your stock.

When you choose to purchase and install NetQ software on a Cumulus hardware appliance (either the NetQ Appliance for on-premises deployments or the NetQ Cloud Appliance for cloud deployments), the initial configuration of the server with Ubuntu OS is already done for you, and the NetQ software components are pre-loaded, saving you time during the physical deployment.

### Choose between a Single Server or Server Cluster

Again, both options provide the same services and features. The biggest difference is in the number of servers to be deployed and in the continued availability of services running on those servers should hardware failures occur.

A single server is easier to set up, configure and manage, but can limit your ability to scale your network monitoring quickly. Multiple servers is a bit more complicated, but you limit potential downtime and increase availability with the master and two worker nodes supported in the NetQ 2.4.0 release. 

<!-- For more detail about clustering, refer to [Server Clustering](tbd). -->

## Installation Workflow Summary

No matter how you answer the questions above, the installation workflow can be summarized as follows:

1. Prepare server(s) and collect needed information.
2. Use Admin UI (preferred) or NetQ CLI to install and configure your deployment and the NetQ software.
3. Install NetQ Agents on switches and hosts.

<!-- ## Get Started

Follow the instructions contained in the section identified in these tables based on your answers to the installation choices you have made.

### Single Server

| On Prem/ Cloud | VM + Your HW/ Cumulus NetQ HW | Get Started Here |
| ---- | ---- | ---- |
| On premises | VM + your hardware | [Prepare Your Hardware and VM for a NetQ On-premises Deployment](x) |
| On premises | NetQ 2.4 Appliance | [Prepare Your New NetQ Appliance for a NetQ On-premises Deployment](x) |
| Cloud | VM + your hardware | [Prepare Your Hardware and VM for a NetQ Cloud Deployment](x) |
| Cloud | NetQ 2.4 Cloud Appliance | [Prepare Your New NetQ Cloud Appliance for a NetQ Cloud Deployment](x) |
| On premises, cloud | NetQ 2.3 and earlier Appliances | [Prepare Your Existing NetQ Appliances for a NetQ 2.4 Deployment](x) |

### Server Cluster

| On Prem/ Cloud | VM + Your HW/ Cumulus NetQ HW | Get Started Here |
| ---- | ---- | ---- |
| On premises | VM + your hardware | [Prepare Your Hardware and VM for a NetQ On-premises Cluster Deployment](x) |
| On premises | NetQ Appliance | [Prepare Your New NetQ Appliances for a NetQ On-premises Cluster Deployment](x) |
| Cloud | VM + your hardware | [Prepare Your Hardware and VM for a NetQ Cloud Cluster Deployment](x) |
| Cloud | NetQ Cloud Appliance | [Prepare Your New NetQ Cloud Appliance for a NetQ Cloud Cluster Deployment](x) |
| On premises, cloud | NetQ 2.3 and earlier Appliances | [Prepare Your Existing NetQ Appliances for a NetQ 2.4 Cluster Deployment](x) |

After you have completed the necessary preparations, you can install the NetQ software and Agents. -->