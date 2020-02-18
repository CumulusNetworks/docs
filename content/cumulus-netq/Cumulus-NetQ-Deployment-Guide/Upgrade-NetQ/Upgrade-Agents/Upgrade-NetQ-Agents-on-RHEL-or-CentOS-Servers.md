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

Refer to [Configure the NetQ Agent on a RHEL or CentOS Server](../../../Install-NetQ/Install-NetQ-Agents/Install-NetQ-Agents-on-RHEL/#configure-the-netq-agent-on-a-rhel-or-centos-server) to complete the upgrade.
