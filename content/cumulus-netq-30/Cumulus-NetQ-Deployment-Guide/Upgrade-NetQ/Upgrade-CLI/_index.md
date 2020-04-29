---
title: Upgrade NetQ CLI
author: Cumulus Networks
weight: 147
aliases:
 - /display/NETQ/Upgrade+NetQ
 - /pages/viewpage.action?pageId=12320951
toc: 4
---
While it is not required to upgrade the NetQ CLI on your monitored switches and hosts when you upgrade to NetQ 2.4.1, doing so gives you access to new features and important bug fixes. Refer to the {{<link title="Cumulus NetQ 3.0 Release Notes" text="release notes">}} for details.

To upgrade the NetQ CLI:

1. Log in to your switch or host.

2. Update and install the new NetQ debian package.

    <details><summary>For Switches and Hosts Running Cumulus Linux or Ubuntu</summary>

    ```
    sudo apt-get update
    sudo apt-get install -y netq-apps
    ```

    </details>
    <details><summary>For Hosts Running RHEL or CentOS</summary>

    ```
    sudo yum update
    sudo yum install netq-apps
    ```

    </details>

3. Restart the CLI.

```
netq config restart cli
```

To complete the upgrade, refer to the relevant configuration topic:

- {{<link title="Install and Configure the NetQ CLI on Cumulus Linux Switches">}}
- {{<link title="Install and Configure the NetQ CLI on Ubuntu Servers">}}
- {{<link title="Install and Configure the NetQ CLI on RHEL and CentOS Servers">}}

<!-- - {{<link title="Configure the NetQ CLI on a Cumulus Linux Switch">}}
- {{<link title="Configure the NetQ CLI on an Ubuntu Server">}}
- {{<link title="Configure the NetQ CLI on a RHEL or CentOS Server">}} -->
