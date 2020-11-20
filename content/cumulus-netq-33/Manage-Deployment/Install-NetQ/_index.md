---
title: Install NetQ
author: Cumulus Networks
weight: 190
toc: 3
---
The Cumulus NetQ software contains several components that must be installed, including the NetQ applications, the database, and the NetQ Agents. NetQ can be deployed in two arrangements:

- All software components installed locally (the applications and database are installed as a single entity, called the *NetQ Platform*) running on the *NetQ On-premises Appliance* or *NetQ On-premises Virtual Machine (VM)*; known hereafter as the *on-premises solution*
- Only the aggregation and forwarding application software installed locally (called the *NetQ Collector*) running on the *NetQ Cloud Appliance* or *NetQ Cloud VM*, with the database and all other applications installed in the cloud; known hereafter as the *cloud solution*

The NetQ Agents reside on the switches and hosts being monitored in your network.

For the on-premises solution, the NetQ Agents collect and transmit data from the switches and/or hosts back to the NetQ On-premises Appliance or Virtual Machine running the NetQ Platform, which in turn processes and stores the data in its database. This data is then provided for display through several user interfaces.

{{< figure src="/images/netq/install-onprem-basic-300.png" width="600">}}

For the cloud solution, the NetQ Agent function is exactly the same, transmitting collected data, but instead sends it to the NetQ Collector containing only the aggregation and forwarding application. The NetQ Collector then transmits this data to Cumulus Networks cloud-based infrastructure for further processing and storage. This data is then provided for display through the same user interfaces as the on-premises solution. In this solution, the browser interface can be pointed to the local NetQ Cloud Appliance or VM, or directly to *netq.cumulusnetworks.com*.

{{< figure src="/images/netq/install-cloud-basic-300.png" width="700">}}

## Installation Choices

There are several choices that you must make to determine what steps you need to perform to install the NetQ solution. First and foremost, you must determine whether you intend to deploy the solution fully on your premises or if you intend to deploy the cloud solution. Secondly, you must decide whether you are going to deploy a Virtual Machine on your own hardware or use one of the Cumulus NetQ appliances. Thirdly, you also must determine whether you want to install the software on a single server or as a server cluster. Finally, if you have an existing on-premises solution and want to save your existing NetQ data, you must backup that data before installing the new software.

{{< figure src="/images/netq/install-decision-tree-240.png" width="400">}}

The documentation walks you through these choices and then provides the instructions specific to your selections.

## Installation Workflow Summary

No matter how you answer the questions above, the installation workflow can be summarized as follows:

1. Prepare physical server or virtual machine.
2. Install the software (NetQ Platform or NetQ Collector).
3. Install and configure NetQ Agents on switches and hosts.
4. Install and configure NetQ CLI on switches and hosts (optional, but useful).

## Where to Go Next

Follow the instructions in {{<link title="Install the NetQ System" text="Install the NetQ System">}} to begin installation of Cumulus NetQ.
