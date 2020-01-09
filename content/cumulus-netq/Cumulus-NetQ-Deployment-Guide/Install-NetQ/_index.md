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

- All components installed locally, known hereafter as the on-premises solution
- Only the aggregation and forwarding application installed locally and the database and all other applications installed remotely, known hereafter as the cloud solution

The NetQ Agents reside on the switches and hosts being monitored in your network.

For the on-premises solution, the NetQ Agents collect and transmit data from the switches and/hosts back to the NetQ Platform, which in turn processes and stores the data in its database. This data is then provided for display in through several user interfaces.

{{< figure src="/images/netq/install-onprem-basic-240.png" width="600">}}

For the cloud solution, the NetQ Agent function is exactly the same, transmitting collected data, but instead sends it to the NetQ Platform containing the aggregation and forwarding application. This platform then transmits this data to Cumulus Networks cloud-based infrastructure for further processing and storage. This data is then provided for display through the same user interfaces as the on-premises solution.

{{< figure src="/images/netq/install-cloud-basic-240.png" width="700">}}

No data is sent to Agents, only configuration and control commands.

## Installation Choices

There are several choices that you must make to determine what steps you need to perform to install the NetQ solution. First and foremost, you must determine whether you intend to deploy the solution fully on your premises or if you intend to deploy the cloud solution. Secondly, you must decide whether you are going to deploy a Virtual Machine on your own hardware or use one of the Cumulus NetQ appliances. If you have chosen the on-premises solution, you also must determine whether you want to install the software on a single server or as a three-server cluster. Finally, if you want to save your existing NetQ data, you must backup that data before installing the new software.

{{< figure src="/images/netq/install-decision-tree-240.png" width="400">}}

Installing NetQ software can be accomplished in one of several ways:

<!-- On a single server:

- Deploy the software on your own server. Refer to [Prerequisites](../Prerequisites) for details on hardware and software requirements. (for on-premises or cloud deployments)
- Purchase and deploy the Cumulus NetQ Appliance (for on-premises deployments)
- Purchase and deploy the Cumulus NetQ Cloud Appliance (for cloud deployments)

As a three-server cluster:

- Deploy the software on your own servers. Refer to [Prerequisites](../Prerequisites) for details on hardware and software requirements. ( for on-premises or cloud deployments)
- Purchase and deploy three Cumulus NetQ Appliances (for on-premises deployments)

Cumulus recommends using the NetQ Admin UI versus using the NetQ CLI to install the NetQ software, but both options are available.

In all cases you must also load the NetQ Agent software onto the switches and hosts you want to monitor. -->

## Installation Workflow Summary

The install workflow can be summarized as follows:

1. Prepare server(s) and collect needed information. Refer to [Prepare for Installation](../Prepare-for-Install/).
2. Use Admin UI (preferred) or NetQ CLI to install and configure your deployment and the NetQ software. Refer to [Install NetQ Using Admin UI](../Install-NetQ-Using-AdminUI/)
3. Install NetQ Agents on switches and hosts. Refer to OS-specific Agent installation topic.

<!-- If you are upgrading from a prior version of NetQ, refer to [Upgrade NetQ](/cumulus-netq/Cumulus-NetQ-Deployment-Guide/Upgrade-NetQ/) instead. -->
