---
title: Install NetQ as an On-premises Deployment
author: NVIDIA
weight: 210
toc: 5
---
On-premises deployments of NetQ can use a single server or a server cluster. In either case, you can use either the NVIDIA Cumulus NetQ Appliance or your own server running a KVM or VMware virtual machine (VM). This topic walks you through the installation for each of these on-premises options.

The next installation step is to decide whether you are deploying a single server or a server cluster. Both options provide the same services and features. The biggest difference is in the number of servers you deploy and in the continued availability of services running on those servers should hardware failures occur.

A single server is easier to set up, configure and manage, but can limit your ability to scale your network monitoring quickly. Multiple servers is a bit more complicated, but you limit potential downtime and increase availability by having more than one server that can run the software and store the data.

Select the standalone single-server arrangements for smaller, simpler deployments. Be sure to consider the capabilities and resources needed on this server to support the size of your final deployment.

Select the server cluster arrangement to obtain scalability and high availability for your network. You can configure one master node and up to nine worker nodes.

Click the server arrangement you want to use to begin installation:

- {{<link title="Choose an On-premises System Platform" text="Use a Single Server Arrangement">}}
- {{<link title="Choose an On-premises System Platform for Your Cluster" text="Use a Server Cluster Arrangement">}}
