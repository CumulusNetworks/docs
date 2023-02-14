---
title: Upgrade NetQ CLI
author: NVIDIA
weight: 470
toc: 4
---

Upgrading the NetQ CLI is optional, but recommended.

To upgrade the NetQ CLI:

1. Log in to your switch or host.

2. Update and install the new NetQ Debian package:

    {{<tabs "Install Debian" >}}

{{<tab "Cumulus Linux and SONiC Switches and Ubuntu Hosts">}}

```
sudo apt-get update
sudo apt-get install -y netq-apps
```

{{</tab>}}

{{<tab "RHEL or CentOS Hosts">}}

```
sudo yum update
sudo yum install netq-apps
```

{{</tab>}}

{{</tabs>}}

3. Restart the CLI:

    ```
    netq config restart cli
    ```

To complete the upgrade, refer to {{<link url="Install-NetQ-CLI/#configure-the-netq-cli" text="Configure the NetQ CLI">}}.
