---
title: Upgrade NetQ Agents on Ubuntu Servers
author: Cumulus Networks
weight: 144
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
toc: 5
---
The following instructions are applicable to both NetQ Platform and NetQ Appliances running Ubuntu 16.04 or 18.04 in on-premises and cloud deployments.

To upgrade the NetQ Agent:

1. Log in to your NetQ Platform or Appliance.

2. Update your NetQ repository.

```
root@ubuntu:~# sudo apt-get update
```

3. Install the agent software.

```
root@ubuntu:~# sudo apt-get install -y netq-agent
```

4. Restart the NetQ Agent.

```
root@ubuntu:~# netq config restart agent
```

Refer to [Configure Your NetQ Agents](../../Install-NetQ/Install-NetQ-Agents-and-CLI-on-Ubuntu/#configure-your-netq-agents/) to complete the upgrade.
