---
title: Lifecycle Management
author: NVIDIA
weight: 900
toc: 3
---

Using the NetQ UI or CLI, lifecycle management (LCM) allows you to:

- {{<link title="Switch Management" text="Manage Cumulus Linux switch inventory">}} and roles
- {{<link title="NetQ and Network OS Images" text="Manage Cumulus Linux and NetQ images">}} in a local repository
- Install or {{<link title="Upgrade NetQ Agent" text="upgrade NetQ (Agents and CLI)">}} and {{<link title="Upgrade Cumulus Linux" text="Cumulus Linux">}} on switches
- Create NetQ Agent {{<link title="Upgrade NetQ Agent/#agent-configuration-profiles" text="configuration profiles">}}
- {{<link title="Credentials and Profiles" text="Configure switch access credentials and profiles">}} (required for installations and upgrades)
- View a history of upgrade attempts

{{%notice note%}}

Lifecycle management is enabled for on-premises deployments and disabled for cloud deployments by default. Contact your NVIDIA sales representative or submit a support ticket to activate LCM on cloud deployments.

{{%/notice%}}

## Access Lifecycle Management in the UI

To access the lifecycle management dashboard, expand the {{<img src="https://icons.cumulusnetworks.com/01-Interface-Essential/03-Menu/navigation-menu.svg" width="18" height="18">}} **Menu**, then select **Manage switches**:

{{<figure src="/images/netq/manage-switch-assets-450.png" alt="dashboard displaying switch management tab" width="700">}}

## LCM Summary

This table summarizes LCM functionalities in the UI and CLI:

| <div style="width:30px">Function </div> | <div style="width:220px">Description</div> | <div style="width:220px">NetQ UI Cards</div> | <div style="width:220px">NetQ CLI Commands</div> |
| --- | --- | --- | --- |
| Switch management | Discover switches, view switch inventory, assign roles, set user access credentials, perform software installation and upgrade networkwide | <ul><li>Switches</li><li>Access profiles</li></ul> | <ul><li>netq lcm show switches</li><li>netq lcm add role</li><li>netq lcm upgrade</li><li>netq lcm add/del/show credentials</li><li>netq lcm discover</li></ul> |
| Image management | View, add, and remove images for software installation and upgrade | <ul><li>Cumulus Linux images</li><li>NetQ images</li></ul> | <ul><li>netq lcm add/del/show netq-image</li><li>netq lcm add/del/show cl-images</li><li>netq lcm add/show default-version</li></ul> |
| NetQ agent configurations | Customize configuration profiles for NetQ Agents running on switches | <ul><li>NetQ agent configurations</li>| <ul><li>netq lcm add/del/show netq-config</li></ul> |
| Job history | View the results of installation, upgrade, and configuration assignment jobs | <ul><li>CL upgrade history</li><li>NetQ install and upgrade history</li></ul> | <ul><li>netq lcm show status</li><li>netq lcm show upgrade-jobs</li></ul> |
## LCM Support for In-band Management

If you manage a switch using an in-band network interface, the `inband-interface` option must be specified in the {{<link url="Install-NetQ-Agents/#configure-netq-agents-using-the-netq-cli" text="initial agent configuration">}} for LCM operations to function as expected. You can configure the agent by specifying the in-band interface in the `/etc/netq/netq.yml` file. Alternately, you can use the CLI and include the `inband-interface` option.

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
After the NetQ Agent is configured for in-band connections, you can {{<link title="Upgrade NetQ Agent/#agent-configuration-profiles" text="create custom agent configuration profiles">}}, then {{<link title="Upgrade NetQ Agent/#apply-configuration-profiles" text="apply the custom profiles">}} to switches during upgrades.