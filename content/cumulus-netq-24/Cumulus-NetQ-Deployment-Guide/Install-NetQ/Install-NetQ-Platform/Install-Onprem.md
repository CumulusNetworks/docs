---
title: Install NetQ as an On-premises Deployment
author: Cumulus Networks
weight: 111
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5

---
On-premises deployments of NetQ can use a single server or a server cluster. In either case, you can use either the Cumulus NetQ Appliance or your own server running a KVM or VMware Virtual Machine (VM). This topic walks you through the installation for each of these on-premises options.

The next installation step is to decide whether you are deploying a single server or a server cluster. Both options provide the same services and features. The biggest difference is in the number of servers to be deployed and in the continued availability of services running on those servers should hardware failures occur.

A single server is easier to set up, configure and manage, but can limit your ability to scale your network monitoring quickly. Multiple servers is a bit more complicated, but you limit potential downtime and increase availability by having more than one server that can run the software and store the data.

Click the server arrangement you want to use to begin installation:

- {{<link title="Choose an On-premises System Platform" text="Use a Single Server Arrangement">}}
- {{<link url="Server-Cluster" text="Use a Server Cluster Arrangement">}}
