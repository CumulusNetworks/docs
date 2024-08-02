---
title: Before You Install
author: NVIDIA
weight: 190
toc: 3
---

This overview is designed to help you understand the various NetQ deployment and installation options. 

## Installation Overview

Consider the following before you install the NetQ system:

1. Determine whether to deploy fully **on-premises** or as a **remote** solution.
2. Choose whether to install the software on a **single server** or as a **server cluster**.
3. Alternately, you can launch NetQ using NVIDIA Base Command Manager. To get started, refer to the {{<exlink url="https://docs.nvidia.com/base-command-manager/#product-manuals" text="Base Command Manager administrator and containerization manuals">}}.

## Deployment Type: On-premises or Remote

You can deploy NetQ in one of two ways:

- **Hosted on-premises**: Choose this deployment if you want to host at your location and have the in-house skill set to install, configure, back up, and maintain NetQ. This model is also a good choice if you want very limited or no access to the internet from switches and hosts in your network, or if you have data-residency requirements like GDPR.
- **Hosted remotely**: Choose this deployment to host a multi-site, on-premises deployment or use NetQ cloud. In the multi-site deployment, you host multiple small servers at each site and an on-premises appliance at a central location. In the cloud deployment, you host only a small, local server on your premises that connects to the NetQ cloud service over selected ports or through a proxy server. NetQ cloud supports local data aggregation and forwarding---the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage. This remote cloud service model is a good choice when you have limited in-house support or if you need the flexibility to scale quickly, while also reducing capital expenses.

In all deployment models, the NetQ Agents reside on the switches and hosts they monitor in your network. Refer to {{<link title="Install the NetQ System">}} for a comprehensive list of deployment types and their respective requirements.
<!--
### Data Flow

The flow of data differs based on your deployment model.

For the on-premises deployment, the NetQ Agents collect and transmit data from the switches and hosts back to the NetQ on-premises appliance running the NetQ software. The software processes and stores the data, which is then displayed through the user interface.

{{<figure src="/images/netq/install-onprem-basic-300.png" width="600" alt="on-premises deployment type displaying data transmission between the agents, the platform, and the user interface.">}}

For the remote, multi-site NetQ implementation, the NetQ Agents at each secondary premises collect and transmit data from the switches and hosts from the secondary premises to the NetQ cloud appliance. The cloud appliance transmits this data to the primary NetQ on-premises appliance for processing and storage. This deployment is a good choice when you want to store all the data from multiple premises on one NetQ on-premises appliance.

{{<figure src="/images/netq/install-remote-multisite-330.png" width="700" alt="">}}

For the remote, cloud-service implementation, the NetQ Agents collect and transmit data from the switches and hosts to the NetQ cloud appliance. The NetQ cloud appliance then transmits this data to the NVIDIA cloud-based infrastructure for further processing and storage.

{{<figure src="/images/netq/install-remote-cloud-330.png" width="700">}}

To access the NetQ UI from the cloud-service implementation, visit *https://netq.nvidia.com*.

-->

## Server Arrangement: Single or Cluster

Both single-server and server-cluster deployments provide identical services and features. The biggest difference is the number of servers deployed and the continued availability of services running on those servers should hardware failures occur.

A single server is easier to set up, configure, and manage, but can limit your ability to scale your network monitoring quickly. Deploying multiple servers is more complicated, but you limit potential downtime and increase availability by having more than one server that can run the software and store the data. Select the standalone, single-server arrangements for smaller, simpler deployments. Be sure to consider the capabilities and resources needed on this server to support the size of your final deployment.

Select the server-cluster arrangement to obtain scalability and high availability for your network. The clustering implementation comprises three servers: one master and two workers. In a clustered environment, NVIDIA recommends installing the virtual machines on different physical servers to increase redundancy in the event of a hardware failure.

NetQ cloud deployments support 250 switches and up to 3000 interfaces. NetQ on-premises cluster deployments support 150 switches and up to 1500 interfaces.

<!-- However, NetQ supports up to 10 worker nodes in a cluster. and up to 5000 total devices (switches, servers, and hosts).-->

### Cluster Deployments and Kubernetes 

NetQ supports high availability server-cluster deployments using a virtual IP address. Even if the master node fails, NetQ services remain operational. However, keep in mind that the master hosts the Kubernetes control plane so anything that requires connectivity with the Kubernetes cluster&mdash;such as upgrading NetQ or rescheduling pods to other workers if a worker goes down&mdash;will not work.

During the installation process, you configure a virtual IP address that enables redundancy for the Kubernetes control plane. In this configuration, the majority of nodes must be operational for NetQ to function. For example, a three-node cluster can tolerate a one-node failure, but not a two-node failure. For more information, refer to the {{<exlink url="https://etcd.io/docs/v3.3/faq/" text="etcd documentation">}}.

### Cluster Deployments and Load Balancers

As an alternative to the high availability server-cluster deployment with a virtual IP address, you can use an external load balancer to provide high availability for the NetQ API and the NetQ UI.

However, you need to be mindful of where you {{<link title="Install a Custom Signed Certificate" text="install the certificates">}} for the NetQ UI (port 443); otherwise, you cannot access the NetQ UI. If you are using a load balancer in your deployment, NVIDIA recommends that you install the certificates directly on the load balancer for SSL offloading. However, if you install the certificates on the master node, then configure the load balancer to allow for SSL passthrough.

## Next Steps

After you've decided on your deployment type, you're ready to {{<link title="Install the NetQ System" text="install NetQ">}}.