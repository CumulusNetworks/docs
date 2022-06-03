---
title: Upgrade NetQ Agents
author: NVIDIA
weight: 420
toc: 4
---
NVIDIA strongly recommends that you upgrade your NetQ Agents when you install or upgrade to a new release. The following instructions apply to Cumulus Linux for both on-premises and remote deployments.

## Upgrade NetQ Agent

To upgrade the NetQ Agent:

1. Log in to your switch or host.

2. Update and install the new NetQ Debian package.

   {{<tabs "Upgrade Agent" >}}

{{<tab "Cumulus Linux Switches or Ubuntu Hosts">}}

```
sudo apt-get update
sudo apt-get install -y netq-agent
```

{{</tab>}}

{{<tab "RHEL or CentOS Hosts">}}

```
sudo yum update
sudo yum install netq-agent
```

{{</tab>}}

{{</tabs>}}

3. Restart the NetQ Agent.

   ```
   netq config restart agent
   ```

Refer to {{<link title="Install NetQ Agents">}} to complete the upgrade.

## Verify NetQ Agent Version

You can verify the version of the agent software you have deployed as described in the following sections.

Run the following command to view the NetQ Agent version.

{{<tabs "Verify Agent Version">}}

{{<tab "Cumulus Linux">}}

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{<netq-install/agent-version version="4.2.0" opsys="cl">}}

{{</tab>}}

{{<tab "Ubuntu 18.04">}}

```
root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{<netq-install/agent-version version="4.2.0" opsys="ub">}}

{{</tab>}}

{{<tab "RHEL7 or CentOS">}}

```
root@rhel7:~# rpm -q -netq-agent
```

{{<netq-install/agent-version version="4.2.0" opsys="rh">}} <!-- UPDATE ME! -->

{{</tab>}}

{{</tabs>}}

If you see an older version, upgrade the NetQ Agent, as described above.
