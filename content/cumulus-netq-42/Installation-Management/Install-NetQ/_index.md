---
title: Pre Installation Configuration Information
author: NVIDIA
weight: 190
toc: 3
---

The NetQ software contains several components that you must install, including the NetQ applications, the database, and the NetQ Agents. You can deploy NetQ in one of two ways:

<!-- vale off -->
- **Hosted on premises**: It is common to select an on-premises deployment model if you want to host all required hardware and software at your location, and you have the in-house skill set to install, configure, and maintain it---including performing data backups, acquiring and maintaining hardware and software, and integration management. This model is also a good choice if you want very limited or no access to the internet from switches and hosts in your network or you have data residency requirements like GDPR. Some companies only want complete control of the their network, and no outside impact.
- **Hosted remotely**: If you find that you want to host a multi-site on-premises deployment or use the NetQ Cloud service, you should select the remote deployment model. In the multi-site deployment, you host multiple small servers at each site and a large server and database at another site. In the cloud service deployment, you host only a small local server on your premises that connects to the NetQ Cloud service over selected ports or through a proxy server. The cloud service supports only data aggregation and forwarding locally, and the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage. This remote cloud service model is often chosen when it is untenable to support deployment in-house or if you need the flexibility to scale quickly, while also reducing capital expenses.
<!-- vale on -->

With either deployment model, the NetQ Agents reside on the switches and hosts they monitor in your network.

## NetQ Data Flow

For the on-premises solution, the NetQ Agents collect and transmit data from the switches and hosts back to the NetQ On-premises Appliance or virtual machine running the NetQ Platform software, which in turn processes and stores the data in its database. This data is then provided for display through several user interfaces.

{{<figure src="/images/netq/install-onprem-basic-300.png" width="600">}}

For the remote, multi-site NetQ implementation, the NetQ Agents at each premises collect and transmit data from the switches and hosts at that premises to its NetQ Cloud Appliance or virtual machine running the NetQ Collector software. The NetQ Collectors then transmit this data to the common NetQ Cloud Appliance or virtual machine and database at one of your premises for processing and storage.

{{<figure src="/images/netq/install-remote-multisite-330.png" width="700">}}

For the remote, cloud-service implementation, the NetQ Agents collect and transmit data from the switches and hosts to the NetQ Cloud Appliance or virtual machine running the NetQ Collector software. The NetQ Collector then transmits this data to the NVIDIA cloud-based infrastructure for further processing and storage.

{{<figure src="/images/netq/install-remote-cloud-330.png" width="700">}}

For either remote solution, telemetry data is displayed through the same user interfaces as the on-premises solution. When using the cloud service implementation of the remote solution, the browser interface can be pointed to the local NetQ Cloud Appliance or VM, or directly to *netq.cumulusnetworks.com*.

## Installation Choices

You must make several choices to determine what steps you need to perform to install the NetQ system:

1. You must determine whether you intend to deploy the solution fully on your premises or if you intend to deploy the remote solution.
1. You must decide whether you are going to deploy a virtual machine on your own hardware or use one of the NetQ appliances.
1. You must determine whether you want to install the software on a single server or as a server cluster.
1. If you have an existing on-premises solution and want to save your existing NetQ data, you must back up that data before installing the new software.

{{<figure src="/images/netq/install-decision-tree-330.png" width="400">}}

The documentation walks you through these choices and then provides the instructions specific to your selections.

### Cluster Deployments

Deploying the NetQ servers in a cluster arrangement has many benefits even though it's a more complex configuration. The primary benefits of having multiple servers that run the software and store the data are reduced potential downtime and increased availability.

The default clustering implementation has three servers: 1 master and 2 workers. However, NetQ supports up to 10 worker nodes in a cluster, and up to 5000 devices in total (switches, servers, and hosts). When you configure the cluster, {{<link url="Install-NetQ-Agents/#configure-netq-agent" text="configure the NetQ Agents">}} to connect to these three nodes in the cluster first by providing the IP addresses as a comma-separated list. If you later {{<link title="Post Installation Configuration Options#add-more-nodes-to-your-server-cluster" text="add more nodes">}} to the cluster, you do not need to configure these nodes again.

The Agents connect to the server using gRPC.

#### Cluster Deployments and Kubernetes 

NetQ also monitors {{<link title="Monitor Container Environments Using Kubernetes API Server" text="Kubernetes containers">}}. If the master node ever goes down, all NetQ services should continue to work. However, keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster &mdash; such as upgrading NetQ or rescheduling pods to other workers if a worker goes down &mdash; will not work.

#### Cluster Deployments and Load Balancers

You need a load balancer for high availability for the NetQ API and the NetQ UI.

However, you need to be mindful of where you {{<link title="Post Installation Configuration Options#install-a-custom-signed-certificate" text="install the certificates">}} for the NetQ UI (port 443); otherwise, you cannot access the NetQ UI. 

If you are using a load balancer in your deployment, we recommend you install the certificates directly on the load balancer for SSL offloading. However, if you install the certificates on the master node, then configure the load balancer to allow for SSL passthrough.

## Installation Workflow Summary

No matter which choices you made above, the installation workflow can be summarized as follows:

1. Prepare the physical server or virtual machine.
1. Install the software (NetQ Platform or NetQ Collector).
1. Install and configure the NetQ Agents on switches and hosts.
1. Install and configure the NetQ CLI on switches and hosts (optional, but useful).

## Where to Go Next

Follow the instructions in {{<link title="Install the NetQ System">}} to begin installing NetQ.
