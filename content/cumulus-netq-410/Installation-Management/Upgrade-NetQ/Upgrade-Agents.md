---
title: Upgrade NetQ Agents
author: NVIDIA
weight: 420
toc: 4
---

After {{<link title="Upgrade NetQ Virtual Machines" text="upgrading your NetQ VM">}}, upgrade the NetQ Agent:

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

3. Restart the NetQ Agent with the following command. The {{<link title="Install NetQ CLI" text="NetQ CLI">}} must be installed for the command to run successfully. 

   ```
   netq config restart agent
   ```

Refer to {{<link title="Install NetQ Agents/#install-netq-agent">}} to complete the upgrade.

## Verify NetQ Agent Version

You can verify the version of the agent software you have deployed as described in the following sections.

Run the following command to view the NetQ Agent version.

{{<tabs "Verify Agent Version">}}

{{<tab "Cumulus Linux">}}

```
cumulus@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{<netq-install/agent-version version="4.10.0" opsys="cl">}}

{{</tab>}}

{{<tab "Ubuntu">}}

```
root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{<netq-install/agent-version version="4.10.0" opsys="ub">}}

{{</tab>}}

{{<tab "RHEL7 or CentOS">}}

```
root@rhel7:~# rpm -q -netq-agent
```

{{<netq-install/agent-version version="4.10.0" opsys="rh">}}

{{</tab>}}

{{</tabs>}}

If you see an older version, upgrade the NetQ Agent, as described above.

## Next Steps

- {{<link title="Upgrade NetQ CLI">}}
