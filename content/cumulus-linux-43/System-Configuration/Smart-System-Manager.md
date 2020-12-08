---
title: Smart System Manager
author: NVIDIA
weight: 275
toc: 3
---
Use Smart System Manager to upgrade and troubleshoot an active switch with minimal disruption to the network.

Smart System Manager includes the following modes:
- Restart
- Upgrade
- Maintenance

## Restart Mode

You can restart the switch in one of the following modes.

| <div style="width:150px">Option | <div style="width:150px">Desciption | <div style="width:250px">Command |
|-------------- | ---------- | ------- |
| `cold` | Completely restarts the system and resets all the hardware devices on the switch (including the switching ASIC). | `cl system mode cold` |
| `fast` | Restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system is decoupled from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The forwarding entries of the switching ASIC are maintained through the restart process and the data plane is not affected. The data plane is only interrupted when `switchd` resets and reconfigures the ASIC if the SDK is upgraded. Traffic outage is significantly lower in this mode. | `cl system mode fast` |

You must restart Cumulus Linux with either fast or cold mode after you upgrade the switch in {{<link url="#upgrade-mode" text="upgrade mode">}}. Smart System Manager performs a fast restart mode automatically when you disable {{<link url="#maintenance-mode" text="maintenance mode">}}.

## Ugrade Mode

Upgrade mode updates all the components and services on the switch to the latest Cumulus Linux release without traffic loss. After upgrade is complete, you must restart the switch with one of the {{<link url="#restart-mode" text="restart modes">}}.

Upgrade mode includes the following options.

| <div style="width:150px">Option | <div style="width:150px">Desciption | <div style="width:250px">Command |
|-------------- | ---------- | ------- |
| `all` | Runs `apt-get upgrade` to upgrade all the system components to the latest release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.  | `cl system upgrade all` |
| `dry-run` | Provides information on the components that will be upgraded. | `cl system upgrade dry-run` |
| `status` | Shows the current status of the system. | `cl system upgrade status` |

The following example commands upgrade the switch to the latest release, shows the current system status, then restarts the switch in fast mode (reloads the kernel and software stack without a hard reset of the hardware):

```
cumulus@switch:~$ cl system upgrade all
cumulus@switch:~$ cl system upgrade status
cumulus@switch:~$ cl system mode fast
```

## Maintenance Mode

Maintenance mode isolates the system from the rest of the network so that you can perform intrusive troubleshooting tasks and data collection or perform system changes, such as break out ports and replace optics or cables with minimal disruption.

{{%notice note%}}
Depending on your configuration and network topology, complete isolation might not be possible.
{{%/notice%}}

Run the following command to enable maintenance mode. When maintenance mode is enabled, Smart System Manager performs a graceful BGP shutdown, redirects traffic over the peerlink and brings down the MLAG port link. `switchd` maintains full capability.

```
cumulus@switch:~$ cl system maintenance enable
```

You can use an additional option to bring all the ports down, then up to restore the port admin state.

```
cumulus@switch:~$ cl system maintenance port down
cumulus@switch:~$ cl system maintenance port up
```

{{%notice note%}}
Before you exit maintenance mode, be sure to bring the ports back up.
{{%/notice%}}

Run the following command to disable maintenance mode and restore normal operation. When maintenance mode is disabled, Smart System Manager performs a {{<link url="#restart-mode" text="fast restart">}}, runs a BGP graceful restart and brings the MLAG port link back up. `switchd` maintains full capability.

```
cumulus@switch:~$ cl system maintenance disable
```
