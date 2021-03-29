---
title: Upgrade NetQ Agents on Ubuntu Servers
author: NVIDIA
weight: 440
toc: 5
---
The following instructions are applicable to both NetQ Platform and NetQ Appliances running Ubuntu 16.04 or 18.04 in on-premises and remote deployments.

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

Refer to {{<link title="Install and Configure the NetQ Agent on Ubuntu Servers">}} to complete the upgrade.
