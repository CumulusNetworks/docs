---
title: Verify NetQ Agent Version
author: Cumulus Networks
weight: 146
toc: 5
---
You can verify the version of the agent software you have deployed as described in the following sections.

## For Switches Running Cumulus Linux 3.x or 4.x

Run the following command to view the NetQ Agent version.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{<netq-install/agent-version version="3.1.0" opsys="cl">}}

If you see an older version, refer to {{<link title="Upgrade NetQ Agents on Cumulus Linux Switches">}}.

## For Servers Running Ubuntu 16.04 or 18.04

Run the following command to view the NetQ Agent version.

```
root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{<netq-install/agent-version version="3.1.0" opsys="ub">}}

If you see an older version, refer to {{<link title="Upgrade NetQ Agents on Ubuntu Servers">}}.

## For Servers Running RHEL7 or CentOS

Run the following command to view the NetQ Agent version.

```
root@rhel7:~# rpm -q -netq-agent
```

{{<netq-install/agent-version version="3.1.0" opsys="rh">}}

If you see an older version, refer to {{<link title="Upgrade NetQ Agents on RHEL or CentOS Servers">}}.
