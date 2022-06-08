---
title: Smart System Manager
author: NVIDIA
weight: 275
toc: 3
---
Use Smart System Manager, also known as [ISSU](## "In Service System Upgrade"), to upgrade and troubleshoot an active switch with minimal disruption to the network.

Smart System Manager includes the following modes:
- Restart
- Upgrade
- Maintenance

## Restart Mode

You can restart the switch in one of the following modes.

- **cold** Restarts the system and resets all the hardware devices on the switch (including the switching ASIC).
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintain the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode; there is a momentary interruption after reboot, after `switchd` restarts.
- **warm** restarts the system with minimal impact to traffic and without affecting the data plane. Warm mode diverts traffic from itself and restarts the system without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions.

   When you restart the switch in warm mode, BGP performs a graceful restart if the BGP Graceful Restart option is on. To enable BGP Graceful Restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

   {{%notice note%}}
   A warm boot disrupts bonds, VXLAN traffic, and IP multicast traffic until reboot completes.
   {{%/notice%}}

The following command restarts the system in cold mode:

{{< tabs "28 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -c
```

{{< /tab >}}
{{< /tabs >}}

The following command restarts the system in fast mode:

{{< tabs "52 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -f
```

{{< /tab >}}
{{< /tabs >}}

The following command restarts the system in warm mode.

{{< notice warning >}}
Warm boot resets any manually configured FEC settings.
{{< /notice >}}

{{< tabs "76 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -w
```

{{< /tab >}}
{{< /tabs >}}

## Upgrade Mode

Upgrade mode updates all the components and services on the switch to the latest Cumulus Linux release without traffic loss. After upgrade is complete, you must restart the switch with either a {{<link url="#restart-mode" text="cold or fast restart">}}.

Upgrade mode includes the following options:
- **all** runs `apt-get upgrade` to upgrade all the system components to the latest release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.
- **dry-run** provides information on the components you want to upgrade.

The following command upgrades all the system components:

{{< tabs "88 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -u
```

{{< /tab >}}
{{< /tabs >}}

The following command provides information on the components you want to upgrade:

{{< tabs "114 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -d
```

{{< /tab >}}
{{< /tabs >}}

## Maintenance Mode

Maintenance mode isolates the system from the rest of the network so that you can perform intrusive troubleshooting tasks and data collection or perform system changes, such as break out ports and replace optics or cables with minimal disruption.

{{%notice note%}}
Depending on your configuration and network topology, complete isolation is not possible.
{{%/notice%}}

### Enable Maintenance Mode

Run the following command to enable maintenance mode. When maintenance mode is on, Smart System Manager performs a {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown" text="graceful BGP shutdown">}}, redirects traffic over the peerlink and brings down the MLAG port link. `switchd` maintains full capability.

{{< tabs "150 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -m1
```

{{< /tab >}}
{{< /tabs >}}

You can run additional commands to bring all the ports down, then up to restore the port admin state.

{{< tabs "176 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo csmgrctl -p0
cumulus@switch:~$ sudo csmgrctl -p1
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Before you disable maintenance mode, be sure to bring the ports back up.
{{%/notice%}}

### Disable Maintenance Mode

Run the following command to disable maintenance mode and restore normal operation. When maintenance mode is off, Smart System Manager performs a soft restart, runs a BGP graceful restart, and brings the MLAG port link back up. `switchd` maintains full capability.

{{< tabs "210 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "Linux Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -m0
```

{{< /tab >}}
{{< /tabs >}}

### Show Maintenance Mode Status

To see the status of maintenance mode, run the Linux `sudo csmgrctl -s` command. For example:

```
cumulus@switch:~$ sudo csmgrctl -s
Current System Mode: Maintenance since Tue Jan  5 00:13:37 2021 (Duration: 00:00:31)
 Boot Mode: reboot_cold  
 2 registered modules
 frr     : Maintenance, down
 switchd : Maintenance, down 
```
