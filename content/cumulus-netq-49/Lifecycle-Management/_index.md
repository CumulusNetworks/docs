---
title: Lifecycle Management
author: NVIDIA
weight: 900
toc: 3
---

Using the NetQ UI or CLI, lifecycle management (LCM) allows you to:

- {{<link title="Switch Management" text="Manage switch inventory">}}
- Install or {{<link title="Upgrade NetQ Agent" text="upgrade NetQ (Agents and CLI)">}} and {{<link title="Upgrade Cumulus Linux" text="Cumulus Linux">}} on switches running Cumulus Linux
- {{<link title="NetQ and Network OS Images" text="Manage Cumulus Linux and NetQ images">}}
- {{<link title="Credentials and Profiles" text="Configure switch access credentials and profiles">}} (required for installations and upgrades)
- {{<link title="Network Snapshots" text="Create snapshots">}} of the network state at various times
- View a history of upgrade attempts

{{%notice note%}}

Lifecycle management is enabled for on-premises deployments and disabled for cloud deployments by default. Contact your NVIDIA sales representative or submit a support ticket to activate LCM on cloud deployments.

{{%/notice%}}

## Access Lifecycle Management in the UI

You can access the LCM dashboard in a few ways:

- Expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}} **Menu**, then select **Manage switches**
- Click {{<img src="https://icons.cumulusnetworks.com/05-Internet-Networks-Servers/06-Servers/server-upload.svg" width="18" height="18">}} **Upgrade** in a workbench header
- Click {{<img src="/images/netq/devices.svg" height="18" width="18">}} **Devices** in a workbench header, then select **Manage switches**

{{<figure src="/images/netq/manage-switch-assets-450.png" alt="dashboard displaying switch management tab" width="700">}}

## Access Lifecycle Management with the CLI

Lifecycle management workflows use the `netq lcm` command set. Refer to the {{<link title="lcm" text="command line reference">}} for a comprehensive list of options and definitions.

## LCM Support for In-band Management

If you manage a switch using an in-band network interface, the `inband-interface` option must be specified in the {{<link url="Install-NetQ-Agents/#configure-netq-agents-using-the-netq-cli" text="agent configuration">}} for LCM operations:

- `/etc/netq/netq.yml` configuration file example:

    ```
    netq-agent:
        inband-interface: swp1
        port: 31980
        server: 192.168.1.254
        vrf: default
    ```

- CLI configuration example:

    ```
    sudo netq config add agent server 192.168.1.254 vrf default inband-interface swp1
    ```
After the NetQ Agent is configured for in-band connections, you can {{<link title="Credentials and Profiles/#agent-configuration-profiles" text="create custom agent configuration profiles">}} using the CLI, then {{<link title="Credentials and Profiles/#apply-configuration-profiles" text="apply the custom  profiles">}} to switches during upgrades.