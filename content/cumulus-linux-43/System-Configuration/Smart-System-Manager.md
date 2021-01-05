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

{{%notice note%}}
The Smart System Manager NCLU commands do not require a `net commit`.
{{%/notice%}}

## Restart Mode

You can restart the switch in one of the following modes.

- `cold` completely restarts the system and resets all the hardware devices on the switch (including the switching ASIC).  
- `fast` restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system is decoupled from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The forwarding entries of the switching ASIC are maintained through the restart process and the data plane is not affected. The data plane is only interrupted when `switchd` resets and reconfigures the ASIC if the SDK is upgraded. Traffic outage is significantly lower in this mode.

The following command restarts the system in cold mode:

```
cumulus@switch:~$ net system maintenance restart cold
```

The following command restarts the system in fast mode:

```
cumulus@switch:~$ net system maintenance restart fast
```

## Ugrade Mode

Upgrade mode updates all the components and services on the switch to the latest Cumulus Linux release without traffic loss. After upgrade is complete, you must restart the switch with either a {{<link url="#restart-mode" text="cold or fast restart">}}.

Upgrade mode includes the following options:
- `all` runs `apt-get upgrade` to upgrade all the system components to the latest release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.  
- `dry-run` provides information on the components that will be upgraded.

The following command upgrades all the system components:

```
cumulus@switch:~$ net system maintenance upgrade all
```

The following command provides information on the components that will be upgraded:

```
cumulus@switch:~$ net system maintenance upgrade dry-run
```

## Maintenance Mode

Maintenance mode isolates the system from the rest of the network so that you can perform intrusive troubleshooting tasks and data collection or perform system changes, such as break out ports and replace optics or cables with minimal disruption.

{{%notice note%}}
Depending on your configuration and network topology, complete isolation might not be possible.
{{%/notice%}}

### Enable Maintenance Mode

Run the following command to enable maintenance mode. When maintenance mode is enabled, Smart System Manager performs a graceful BGP shutdown, redirects traffic over the peerlink and brings down the MLAG port link. `switchd` maintains full capability.

```
cumulus@switch:~$ net system maintenance mode enable
```

You can run additional commands to bring all the ports down, then up to restore the port admin state.

```
cumulus@switch:~$ net system maintenance ports down
cumulus@switch:~$ net system maintenance ports up
```

{{%notice note%}}
Before you disable maintenance mode, be sure to bring the ports back up.
{{%/notice%}}

### Disable Maintenance Mode

Run the following command to disable maintenance mode and restore normal operation. When maintenance mode is disabled, Smart System Manager performs a {{<link url="#restart-mode" text="fast restart">}}, runs a BGP graceful restart and brings the MLAG port link back up. `switchd` maintains full capability.

```
cumulus@switch:~$ net system maintenance mode disable
```

### Show Maintenance Mode Status

To see the status of maintenance mode, run the `net system maintenance show status` command:

```
cumulus@switch:~$ net system maintenance show status
Current System Mode: Maintenance since Tue Jan  5 00:13:37 2021 (Duration: 00:00:31)
 Boot Mode: reboot_cold  
 2 registered modules
 frr     : Maintenance, down
 switchd : Maintenance, down 
```
