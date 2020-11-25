---
title: Upgrade NetQ Agents and CLI on Cumulus Linux Switches
author: Cumulus Networks
weight: 490
toc: 5
---
The following instructions are applicable to both Cumulus Linux 3.x and 4.x, and for both on-premises and cloud deployments.

To upgrade the NetQ Agent and CLI on a switch or host:

1. Log in to your switch or host.

2. Update and install the new NetQ debian packages.

    {{< tabs "TabID0" >}}

{{< tab "Cumulus Linux Switches or Ubuntu Hosts " >}}

```
sudo apt-get update
sudo apt-get install -y netq-agent netq-apps
```

{{< /tab >}}

{{< tab "RHEL or CentOS Hosts" >}}

```
sudo yum update
sudo yum install netq-agent netq-apps
```

{{< /tab >}}

{{< /tabs >}}

3. Restart the NetQ Agent and CLI.

    ```
    netq config restart agent
    netq config restart cli
    ```

Refer to {{<link title="Install and Configure the NetQ Agent on Cumulus Linux Switches">}} to complete the upgrade.
