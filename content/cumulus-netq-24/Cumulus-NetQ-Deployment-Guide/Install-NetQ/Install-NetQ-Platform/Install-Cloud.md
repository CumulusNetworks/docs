---
title: Install NetQ as a Cloud Deployment
author: Cumulus Networks
weight: 112
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
pageID: 12320951
toc: 5
---
Cloud deployments of NetQ can use a single server or a server cluster on site. The NetQ database remains in the cloud either way.  You can use either the Cumulus NetQ Cloud Appliance or your own server running a KVM or VMware Virtual Machine (VM). This topic walks you through the installation for each of these cloud options.

The next installation step is to decide whether you are deploying a single server or a server cluster. Both options provide the same services and features. The biggest difference is in the number of servers to be deployed and in the continued availability of services running on those servers should hardware failures occur.

A single server is easier to set up, configure and manage, but can limit your ability to scale your network monitoring quickly. Multiple servers is a bit more complicated, but you limit potential downtime and increase availability by having more than one server that can run the software and store the data.

Click the server arrangement you want to use to begin installation:

- {{<link title="Choose a Cloud System Platform" text="Use a Single Server Arrangement">}}
- {{<link url="Server-Cluster" text="Use a Server Cluster Arrangement">}}

 Server Arrangement | System | Hypervisor | Installation Instructions |
| --- | --- | --- | --- |
| Single server | Cumulus NetQ Cloud Appliance | NA | link |
| Single server | Own Hardware plus VM | KVM | link |
| Single server | Own Hardware plus VM | VMware | link |
| Server Cluster | Cumulus NetQ Cloud Appliance | NA | link |
| Server Cluster | Own Hardware plus VM | KVM | link |
| Server Cluster | Own Hardware plus VM | VMware | link |
