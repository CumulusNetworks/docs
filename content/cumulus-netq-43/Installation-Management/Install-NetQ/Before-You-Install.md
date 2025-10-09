---
title: Before You Install
author: NVIDIA
weight: 190
toc: 3
---

This overview is designed to help you understand the various NetQ deployment and installation options. 

## Installation Overview

Consider the following before you install the NetQ system:

1. Determine whether to deploy the solution fully **on premises** or as a **remote** solution.
2. Decide whether to deploy a **virtual machine** on your own hardware or use one of the **NetQ appliances**.
3. Choose whether to install the software on a **single server** or as a **server cluster**.

The following decision tree reflects these steps:

{{<figure src="/images/netq/install-decision-tree-330.png" alt="NetQ system deployment options" width="400">}}

## Deployment Type: On Premises or Remote

You can deploy NetQ in one of two ways.

<!-- vale off -->
- **Hosted on premises**: Choose this deployment if you want to host all required hardware and software at your location, and you have the in-house skill set to install, configure, and maintain it---including performing data backups, acquiring and maintaining hardware and software, and integration management. This model is also a good choice if you want very limited or no access to the internet from switches and hosts in your network or you have data residency requirements like GDPR.
- **Hosted remotely**: Choose this deployment to host a multi-site, on-premises deployment or use the NetQ Cloud service. In the multi-site deployment, you host multiple small servers at each site and a large server and database at another site. In the cloud service deployment, you host only a small local server on your premises that connects to the NetQ Cloud service over selected ports or through a proxy server. The cloud service supports only data aggregation and forwarding locally, and the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage. This remote cloud service model is often chosen when it is untenable to support deployment in-house or if you need the flexibility to scale quickly, while also reducing capital expenses.
<!-- vale on -->

With either deployment model, the NetQ Agents reside on the switches and hosts they monitor in your network.

## System: Virtual Machine or NetQ Appliances

The next installation consideration is whether you plan to use NetQ Cloud Appliances or your own servers with VMs. Both options provide the same services and features. The difference is in the implementation. When you install NetQ software on your own hardware, you create and maintain a KVM or VMware VM, and the software runs from there. This requires you to scope and order an appropriate hardware server to support the NetQ requirements, but might allow you to reuse an existing server in your stock.

When you choose to purchase and install NetQ Cloud Appliances, the initial configuration of the server with Ubuntu OS is already done for you, and the NetQ software components are pre-loaded, saving you time during the physical deployment.

### Data Flow

The flow of data differs based on your deployment model.

For the on-premises deployment, the NetQ Agents collect and transmit data from the switches and hosts back to the NetQ On-premises Appliance or virtual machine running the NetQ Platform software, which in turn processes and stores the data in its database. This data is then displayed through the user interface.

{{<figure src="/images/netq/install-onprem-basic-300.png" width="600" alt="on-premises deployment type displaying data transmission between the agents, the platform, and the user interface.">}}

For the remote, multi-site NetQ implementation, the NetQ Agents at each premises collect and transmit data from the switches and hosts at that premises to its NetQ Cloud Appliance or virtual machine running the NetQ Collector software. The NetQ Collectors then transmit this data to the common NetQ Cloud Appliance or virtual machine and database at one of your premises for processing and storage.

{{<figure src="/images/netq/install-remote-multisite-330.png" width="700" alt="">}}

For the remote, cloud-service implementation, the NetQ Agents collect and transmit data from the switches and hosts to the NetQ Cloud Appliance or virtual machine running the NetQ Collector software. The NetQ Collector then transmits this data to the NVIDIA cloud-based infrastructure for further processing and storage.

{{<figure src="/images/netq/install-remote-cloud-330.png" width="700">}}

For either remote solution, telemetry data is displayed through the same user interfaces as the on-premises solution. When using the cloud service implementation of the remote solution, the browser interface can be pointed to the local NetQ Cloud Appliance or VM, or directly to *netq.nvidia.com*.

## Server Arrangement: Single or Cluster

The next installation step is deciding whether to deploy a single server or a server cluster. Both options provide the same services and features. The biggest difference is the number of servers deployed and the continued availability of services running on those servers should hardware failures occur.

A single server is easier to set up, configure and manage, but can limit your ability to scale your network monitoring quickly. Deploying multiple servers is a bit more complicated, but you limit potential downtime and increase availability by having more than one server that can run the software and store the data. Select the standalone single-server arrangements for smaller, simpler deployments. Be sure to consider the capabilities and resources needed on this server to support the size of your final deployment.

Select the server cluster arrangement to obtain scalability and high availability for your network. The default clustering implementation has three servers: 1 master and 2 workers. However, NetQ supports up to 10 worker nodes in a cluster. <!-- and up to 5000 devices in total (switches, servers, and hosts).--> When you configure the cluster, {{<link url="Install-NetQ-Agents/#configure-netq-agent" text="configure the NetQ Agents">}} to connect to these three nodes in the cluster first by providing the IP addresses as a comma-separated list. If you decide to {{<link title="Add More Nodes to Your Server Cluster" text="add additional nodes">}} to the cluster, you do not need to configure these nodes again.

### Cluster Deployments and Kubernetes 

NetQ also monitors {{<link title="Monitor Container Environments Using Kubernetes API Server" text="Kubernetes containers">}}. If the master node ever goes down, all NetQ services should continue to work. However, keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster&mdash;such as upgrading NetQ or rescheduling pods to other workers if a worker goes down&mdash;will not work.

### Cluster Deployments and Load Balancers

You need a load balancer for high availability for the NetQ API and the NetQ UI.

However, you need to be mindful of where you {{<link title="Install a Custom Signed Certificate" text="install the certificates">}} for the NetQ UI (port 443); otherwise, you cannot access the NetQ UI. 

If you are using a load balancer in your deployment, we recommend you install the certificates directly on the load balancer for SSL offloading. However, if you install the certificates on the master node, then configure the load balancer to allow for SSL passthrough.

## Where to Go Next

After you've decided on your deployment type, you're ready to {{<link title="Install the NetQ System" text="install NetQ">}}.


<!---
## Installation Workflow Summary

No matter which choices you made above, the installation workflow can be summarized as follows:

1. Prepare the physical server or virtual machine.
1. Install the software (NetQ Platform or NetQ Collector).
1. Install and configure the NetQ Agents on switches and hosts.
1. Install and configure the NetQ CLI on switches and hosts (optional, but useful).
--->