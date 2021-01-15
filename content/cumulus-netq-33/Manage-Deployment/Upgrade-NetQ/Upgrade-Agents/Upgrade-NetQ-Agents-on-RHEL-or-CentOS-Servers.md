---
title: Upgrade NetQ Agents on RHEL or CentOS Servers
author: NVIDIA
weight: 450
toc: 5
---
The following instructions are applicable to both on-premises and remote deployments.

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

Refer to {{<link title="Install and Configure the NetQ Agent on RHEL and CentOS Servers">}} to complete the upgrade.
