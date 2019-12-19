---
title: Install NetQ
author: Cumulus Networks
weight: 69
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---

Installing NetQ software can be accomplished in one of several ways:

On a single server:

- Deploy the software on your own server. Refer to [Prerequisites](../Prerequisites) for details on hardware and software requirements. (for on-premises or cloud deployments)
- Purchase and deploy the Cumulus NetQ Appliance (for on-premises deployments)
- Purchase and deploy the Cumulus NetQ Cloud Appliance (for cloud deployments)

As a three-server cluster:

- Deploy the software on your own servers. Refer to [Prerequisites](../Prerequisites) for details on hardware and software requirements. ( for on-premises or cloud deployments)
- Purchase and deploy three Cumulus NetQ Appliances (for on-premises deployments)
- Purchase and deploy three Cumulus NetQ Cloud Appliance (for cloud deployments)

Cumulus recommends using the NetQ Admin UI versus using the NetQ CLI to install the NetQ software, but both options are available.

In all cases you must also load the NetQ Agent software onto the switches and hosts you want to monitor.

The install workflow can be summarized as follows:

1. Prepare server(s) and collect needed information. Refer to [Prepare for Installation](../Prepare-for-Install/).
2. Use Admin UI (preferred) or NetQ CLI to install and configure your deployment and the NetQ software. Refer to [Install NetQ Using Admin UI](../Install-NetQ-Using-AdminUI/)
3. Install NetQ Agents on switches and hosts. Refer to OS-specific Agent installation topic.

<!-- If you are upgrading from a prior version of NetQ, refer to [Upgrade NetQ](/cumulus-netq/Cumulus-NetQ-Deployment-Guide/Upgrade-NetQ/) instead. -->
