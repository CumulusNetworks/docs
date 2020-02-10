---
title: Upgrade NetQ Agents on RHEL or CentOS Servers
author: Cumulus Networks
weight: 145
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 5
---
The following instructions are applicable to both on-premises and cloud deployments.

To upgrade the NetQ Agent:

1. Log in to your NetQ Platform.

2. Update your NetQ repository.

```
root@rhel7:~# sudo yum update
```

3. Install the agent software.

```
root@rhel7:~# sudo yum install netq-agent
```

4. Restart the NetQ Agent.

```
root@rhel7:~# netq config restart agent
```

Refer to [Configure Your NetQ Agents](../../Install-NetQ/Install-NetQ-Agents-and-CLI-on-RHEL/#configure-your-netq-agents/) to complete the upgrade.
