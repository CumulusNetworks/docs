---
title: Upgrade NetQ Agents
author: NVIDIA
weight: 420
toc: 4
---

After {{<link title="Upgrade NetQ Virtual Machines" text="upgrading your NetQ VM">}}, prepare your switches and hosts for the NetQ Agent upgrade. After completing these steps, {{<link title="Install NetQ Agents/#install-netq-agent" text="re-install the NetQ Agent">}} to complete the upgrade.

1. Log in to your switch or host.

2. Update and install the new NetQ Debian package.

   {{<tabs "Upgrade Agent" >}}

{{<tab "Cumulus Linux Switches or Ubuntu Hosts">}}

```
sudo apt-get update
sudo apt-get install -y netq-agent
```

{{</tab>}}

{{</tabs>}}

3. Restart the NetQ Agent with the following command. The {{<link title="Install NetQ CLI" text="NetQ CLI">}} must be installed for the command to run successfully. 

   ```
   netq config restart agent
   ```

Refer to {{<link title="Install NetQ Agents/#install-netq-agent">}} to complete the upgrade.

## Verify NetQ Agent Version

Run the following command to view the NetQ Agent version.

{{<tabs "Verify Agent Version">}}

{{<tab "Cumulus Linux">}}

```
nvidia@switch:~$ dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{</tab>}}

{{<tab "Ubuntu">}}

```
root@ubuntu:~# dpkg-query -W -f '${Package}\t${Version}\n' netq-agent
```

{{</tab>}}

{{</tabs>}}

## Next Steps

- {{<link title="Upgrade NetQ CLI">}}
