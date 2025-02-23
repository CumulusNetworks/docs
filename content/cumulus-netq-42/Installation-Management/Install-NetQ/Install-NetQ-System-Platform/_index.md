---
title: Install the NetQ System
author: NVIDIA
weight: 200
toc: 4
---
{{<notice note>}}
The installation process has been simplified to use a single installer tarball. If you are familiar with installing previous versions of NetQ, review the instructions for your deployment type.
{{</notice>}}

This topic walks you through the NetQ System installation decisions and then provides installation steps based on those choices. If you are already comfortable with your installation choices, you can use the matrix in {{<link title="Install NetQ Quick Start">}} to go directly to the installation steps.

To install NetQ {{<version>}}, you must first decide whether you want to install the NetQ System in an on-premises or remote deployment. Both deployment options provide secure access to data and features useful for monitoring and troubleshooting your network, and each has its benefits.

It is common to select an on-premises deployment model if you want to host all required hardware and software at your location, and you have the in-house skill set to install, configure, and maintain it &mdash; including performing data backups, acquiring and maintaining hardware and software, and integration management. This model is also a good choice if you want very limited or no access to the Internet from switches and hosts in your network or you have data residency requirements like GDPR. Some companies only want complete control of the their network, and no outside impact.

If, however, you find that you want to host a multi-site on-premises deployment or use the NetQ Cloud service, you should select the remote deployment model. In the multi-site deployment, you host multiple small servers at each site and a large server and database at another site. In the cloud service deployment, you host only a small local server on your premises that connects to the NetQ Cloud service over selected ports or through a proxy server. The cloud service supports only data aggregation and forwarding locally, and the majority of the NetQ applications use a hosted deployment strategy, storing data in the cloud. NVIDIA handles the backups and maintenance of the application and storage. This remote cloud service model is often chosen when it is untenable to support deployment in-house or if you need the flexibility to scale quickly, while also reducing capital expenses.

Click the deployment model you want to use to continue with installation:

- {{<link title="Install NetQ as an On-premises Deployment" text="On-premises deployment">}}
- {{<link title="Install NetQ as a Remote Deployment" text="Remote deployment">}}
