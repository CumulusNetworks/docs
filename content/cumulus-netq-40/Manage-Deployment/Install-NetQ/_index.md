---
title: Install NetQ
author: NVIDIA
weight: 190
toc: 3
---
The NetQ software contains several components that must be installed, including the NetQ applications, the database, and the NetQ Agents. NetQ can be deployed two ways:

- **Hosted on premises**: This deployment model is used when you want to host a single NetQ site and have it be entirely contained on your premises. In this implementation, all NetQ components including the NetQ Platform software, hardware, and database are located on your premises. The NetQ applications and database are installed as a single entity, called the *NetQ Platform*, and are run on the *NetQ On-premises Appliance* or *NetQ On-premises virtual machine (VM)*. Note that you are responsible for installing, configuring and maintaining all of the NetQ components. This deployment model is called the *on-premises solution* in this documentation. It is suitable for organizations with data residency requirements like GDPR (general data protection regulation).

- **Hosted remotely**: This deployment model is used when you want to either set up multiple NetQ premises or use the NetQ Cloud service. In this implementation the NetQ aggregation and forwarding application software, called the *NetQ Collector*, is installed and run on the *NetQ Cloud Appliance* or *NetQ Cloud VM* on premises with a common database and all other applications installed in a single NetQ site or in the NetQ Cloud. In the multi-site implementation, you are responsible for all software, hardware, and the database. In the cloud service implementation, you are responsible for the on-premises NetQ Collector and NVIDIA is responsible for the data storage in the NetQ Cloud. This deployment model is called the *remote solution* in this documentation.

With either deployment model, the NetQ Agents reside on the switches and hosts being monitored in your network.

## NetQ Data Flow

For the on-premises solution, the NetQ Agents collect and transmit data from the switches and hosts back to the NetQ On-premises Appliance or virtual machine running the NetQ Platform software, which in turn processes and stores the data in its database. This data is then provided for display through several user interfaces.

{{<figure src="/images/netq/install-onprem-basic-300.png" width="600">}}

For the remote solution, multi-site NetQ implementation, the NetQ Agents at each premises collect and transmit data from the switches and hosts at that premises to its NetQ Cloud Appliance or virtual machine running the NetQ Collector software. The NetQ Collectors then transmit this data to the common NetQ Cloud Appliance or virtual machine and database at one of your premises for processing and storage.

{{<figure src="/images/netq/install-remote-multisite-330.png" width="700">}}

For the remote solution, cloud service implementation, the NetQ Agents collect and transmit data from the switches and hosts to the NetQ Cloud Appliance or virtual machine running the NetQ Collector software. The NetQ Collector then transmits this data to the NVIDIA cloud-based infrastructure for further processing and storage.

{{<figure src="/images/netq/install-remote-cloud-330.png" width="700">}}

For either remote solution, telemetry data is then provided for display through the same user interfaces as the on-premises solution. When using the cloud service implementation of the remote solution, the browser interface can be pointed to the local NetQ Cloud Appliance or VM, or directly to *netq.cumulusnetworks.com*.

## Installation Choices

You must make several choices to determine what steps you need to perform to install the NetQ system:

1. You must determine whether you intend to deploy the solution fully on your premises or if you intend to deploy the remote solution.
1. You must decide whether you are going to deploy a virtual machine on your own hardware or use one of the NetQ appliances.
1. You must determine whether you want to install the software on a single server or as a server cluster.
1. If you have an existing on-premises solution and want to save your existing NetQ data, you must back up that data before installing the new software.

{{<figure src="/images/netq/install-decision-tree-330.png" width="400">}}

The documentation walks you through these choices and then provides the instructions specific to your selections.

{{%notice tip%}}

**Why deploy a cluster?**

Deploying the NetQ servers in a cluster arrangement has many benefits even though it's a more complex configuration. The primary benefits of having multiple servers that run the software and store the data are reduced potential downtime and increased availability.
    
The clustering is implemented with three servers: 1 master and 2 workers, although NetQ supports up to 10 worker nodes in a cluster. NetQ supports 5000 devices (switches, servers and hosts) in a cluster.

All NetQ services should continue to work when the master node is down. Keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster, such as upgrading to a new NetQ version or rescheduling pods to other worker if a worker goes down will not work.

You only need a load balancer for API and GUI high availability.

 

    how can I shutdown/poweroff the servers/service?

 

[AS] Following are the commands

 

kubectl get nodes #### to get the list of all node in the k8 cluster
kubectl drain <node name> ### tell Kubernetes to drain the node so that the pods running on it are gracefully scheduled elsewhere.
kubectl uncordon <node name> ### Once the maintenance window is over, use this command to put node back into cluster so that k8 can start scheduling pods on it

 

    do my agents connect to just one of the server addresses (and what when this node is down)?

 

[AS] it’s recommended to connect the agents to first 3 nodes in the cluster by providing the IPs as comma separated list. If we later add more nodes in the cluster then there is no need to configure those again.

 

    the certificate to configure in the admin UI (8443) does not seem to set a certificate on the UI (443)?

 

[AS] It does set the same certificate for UI also. However, if a UI is accessed from load balancer then it won’t work. If a load balancer is used then we recommend that

    Either the certs are installed directly on the load balancer for ssl offloading
    Or if the certs are installed on the master node, then the load balancer allow ssl passthrough

 

    how do agents connect to the server, just by syslog messaging?

 

[AS] It uses GRPC protocol under the hood



{{%/notice%}}

## Installation Workflow Summary

No matter which choices you made above, the installation workflow can be summarized as follows:

1. Prepare physical server or virtual machine.
2. Install the software (NetQ Platform or NetQ Collector).
3. Install and configure NetQ Agents on switches and hosts.
4. Install and configure NetQ CLI on switches and hosts (optional, but useful).

## Where to Go Next

Follow the instructions in {{<link title="Install the NetQ System">}} to begin installation of NetQ.
