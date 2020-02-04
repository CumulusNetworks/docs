---
title: Upgrade NetQ Agents on Cumulus Linux Switches
author: Cumulus Networks
weight: 133
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
product: Cumulus NetQ
version: 2.4
imgData: cumulus-netq
siteSlug: cumulus-netq
---
The following instructions are applicable to both Cumulus Linux 3.x and 4.x, and for both on-premises and cloud deployments.

To upgrade the NetQ Agent:

1. Log in to your NetQ Platform.

2. Update your NetQ repository.

```
cumulus@<hostname>:~$ sudo apt-get update
```

3. Update the NetQ Agent.

```
cumulus@<hostname>:~$ sudo apt-get install -y netq-agent
```

4. Restart the NetQ Agent.

```
cumulus@<hostname>:~$ netq config restart agent
```

Refer to [Configure Your NetQ Agents](../../Install-NetQ/Install-NetQ-Agents-and-CLI-on-CL/#configure-your-netq-agents/) to complete the upgrade.
