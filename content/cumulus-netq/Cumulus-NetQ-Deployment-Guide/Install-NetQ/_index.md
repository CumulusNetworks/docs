---
title: Install NetQ
author: Cumulus Networks
weight: 69
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---

## Overview

The complete Cumulus NetQ solution contains several components that must be installed, including the NetQ applications, the database, and the NetQ Agents. NetQ can be deployed in two arrangements:

- All components installed locally (the applications and database are installed as a single entity, called the NetQ Platform); known hereafter as the on-premises solution
- Only the aggregation and forwarding application installed locally and the database and all other applications installed in the cloud; known hereafter as the cloud solution

The NetQ Agents reside on the switches and hosts being monitored in your network.

For the on-premises solution, the NetQ Agents collect and transmit data from the switches and/hosts back to the NetQ Platform, which in turn processes and stores the data in its database. This data is then provided for display through several user interfaces.

{{< figure src="/images/netq/install-onprem-basic-240.png" width="600">}}

For the cloud solution, the NetQ Agent function is exactly the same, transmitting collected data, but instead sends it to the NetQ Platform containing the aggregation and forwarding application. This platform then transmits this data to Cumulus Networks cloud-based infrastructure for further processing and storage. This data is then provided for display through the same user interfaces as the on-premises solution.

{{< figure src="/images/netq/install-cloud-basic-240.png" width="700">}}

## Installation Choices

There are several choices that you must make to determine what steps you need to perform to install the NetQ solution. First and foremost, you must determine whether you intend to deploy the solution fully on your premises or if you intend to deploy the cloud solution. Secondly, you must decide whether you are going to deploy a Virtual Machine on your own hardware or use one of the Cumulus NetQ appliances. If you have chosen the on-premises solution, you also must determine whether you want to install the software on a single server or as a three-server cluster. Finally, if you want to save your existing NetQ data, you must backup that data before installing the new software.

{{< figure src="/images/netq/install-decision-tree-240.png" width="400">}}

## Installation Workflow Summary

No matter how you answer the questions above, the installation workflow can be summarized as follows:

1. Prepare server(s) and collect needed information.
2. Use Admin UI (preferred) or NetQ CLI to install and configure your deployment and the NetQ software.
3. Install NetQ Agents on switches and hosts.

To get started, answer the on-premises or cloud question and then follow the instructions in the associated topic:

- [Prepare for NetQ On-premises Installation](../Prepare-NetQ-Onprem/)
- [Prepare for NetQ Cloud Installation](../Prepare-NetQ-Cloud)
