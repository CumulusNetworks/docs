---
title: Upgrade NetQ CLI
author: NVIDIA
weight: 470
toc: 4
---

While it is not required to upgrade the NetQ CLI on your monitored switches and hosts when you upgrade to NetQ {{<version>}}, doing so gives you access to new features and important bug fixes. Refer to the {{<link title="NVIDIA Cumulus NetQ 4.0 Release Notes" text="release notes">}} for details.

To upgrade the NetQ CLI:

1. Log in to your switch or host.

2. Update and install the new NetQ Debian package.

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

3. Restart the CLI.

    ```
    netq config restart cli
    ```

To complete the upgrade, refer to {{<link url="Install-NetQ-CLI/#configure-the-netq-cli" text="Configure the NetQ CLI">}}.
