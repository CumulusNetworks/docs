---
title: Update NetQ 2.4.0 Agents
author: Cumulus Networks
weight: 146
aliases:
 - /display/NETQ/Install+NetQ
 - /pages/viewpage.action?pageId=12320951
toc: 5
---
Cumulus Networks recommends upgrading your NetQ Agents to the latest release. If you are using NetQ Agent 2.4.0 update 24 or earlier, you must upgrade to ensure proper operation.

You can verify the version of the agent software you have deployed as described in the following sections.

## For Switches Running Cumulus Linux 3.x or 4.x

Run the following command to view the NetQ Agent version.

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

The output is similar to this:

- For Cumulus Linux 3.3.2-3.7.x:
    - netq-agent_2.4.0-cl3u25~1579642196.aeb67d8_amd64.deb
    - netq-agent_2.4.0-cl3u25~1579642196.aeb67d8_armel.deb
- For Cumulus Linux 4.0.0:
    - netq-agent_2.4.0-cl4u25~1579822727.aeb67d82_amd64.deb

If you see an older version, refer to {{<link title="Upgrade NetQ Agents on Cumulus Linux Switches">}}.

## For Servers Running Ubuntu 16.04 or 18.04

Run the following command to view the NetQ Agent version.

```
root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

The output is similar to this:

- netq-agent_2.4.0-ub18.04u25~1579642196.aeb67d8_amd64.deb, or
- netq-agent_2.4.0-ub16.04u25~1579714730.aeb67d8_amd64.deb

If you see an older version, refer to {{<link title="Upgrade NetQ Agents on Ubuntu Servers">}}.

## For Servers Running RHEL7 or CentOS

Run the following command to view the NetQ Agent version.

```
root@rhel7:~# rpm -q -netq-agent
```

The output is similar to this:

- netq-agent-2.4.0-rh7u25~1579642928.aeb67d8.x86_64.rpm

If you see an older version, refer to {{<link title="Upgrade NetQ Agents on RHEL or CentOS Servers">}}.
