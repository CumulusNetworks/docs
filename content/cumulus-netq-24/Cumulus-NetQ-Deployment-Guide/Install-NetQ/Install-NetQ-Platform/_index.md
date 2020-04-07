---
title: Install NetQ Platform
author: Cumulus Networks
weight: 65
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
toc: 4
---
To install NetQ 2.4.1, you must first decide whether you want to install the NetQ Platform in an on-premises or cloud deployment. Both deployment options provide secure access to data and features useful for monitoring and troubleshooting your network, and each has its benefits.

It is common to select an on-premises deployment model if you want to host all required hardware and software at your location, and you have the in-house skill set to install, configure, and maintain it—including performing data backups, acquiring and maintaining hardware and software, and integration and license management. This model is also a good choice if you want very limited or no access to the Internet from switches and hosts in your network. Some companies simply want complete control of the their network, and no outside impact.

If, however, you find that you want to host only a small server on your premises and leave the details up to Cumulus Networks, then a cloud deployment might be the right choice for you. With a cloud deployment, a small local server connects to the NetQ Cloud service over selected ports or through a proxy server. Only data aggregation and forwarding is supported. The majority of the NetQ applications are hosted and data storage is provided in the cloud. Cumulus handles the backups and maintenance of the application and storage. This model is often chosen when it is untenable to support deployment in-house or if you need the flexibility to scale quickly, while also reducing capital expenses.

Click the deployment model you want to use to continue with installation:

- {{<link title="Install NetQ as an On-premises Deployment" text="Use an On-premises Deployment">}}
- {{<link title="Install NetQ as a Cloud Deployment" text="Use a Cloud Deployment">}}
