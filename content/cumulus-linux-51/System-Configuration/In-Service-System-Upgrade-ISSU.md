---
title: In Service System Upgrade - ISSU
author: NVIDIA
weight: 275
toc: 3
---
Use [ISSU](## "In Service System Upgrade") to upgrade and troubleshoot an active switch with minimal disruption to the network.

ISSU includes the following modes:
- Restart
- Upgrade
- Maintenance mode
- Maintenance ports

{{%notice note%}}
In earlier Cumulus Linux releases, ISSU was Smart System Manager.
{{%/notice%}}

## Restart Mode

You can restart the switch in one of the following modes.

- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC).
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintains the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode as there is only a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the system with no interruption to traffic for existing route entries. Warm mode diverts traffic from itself and restarts the system without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions.

   When you restart the switch in warm mode, BGP performs a graceful restart if the BGP Graceful Restart option is on. To enable BGP Graceful Restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

{{%notice note%}}
Cumulus Linux supports fast mode for all protocols; however only supports warm mode for layer 2 forwarding, and layer 3 forwarding with BGP and static routing.
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

Upgrade mode updates all the components and services on the switch to the latest Cumulus Linux minor release without impacting traffic. After upgrade is complete, you must restart the switch with either a {{<link url="#restart-mode" text="cold or fast restart">}}.

Upgrade mode includes the following options:
- **all** runs `apt-get upgrade` to upgrade all the system components to the latest minor release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.
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

Maintenance mode globally manages the BGP and MLAG control plane.
- When you enable maintenance mode, BGP and MLAG shut down gracefully.
- When you disable maintenance mode, BGP and MLAG are enabled based on the individual parameter settings.

To enable maintenance mode:

{{< tabs "203 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action enable system maintenance mode
Action executing ...
System maintenance mode has been enabled successfully
 Current System Mode: Maintenance, cold  
 Maintenance mode since Thu Jun 13 23:59:47 2024 (Duration: 00:00:00)
 Ports shutdown for Maintenance
 frr             : Maintenance, cold, down, up time: 29:06:27
 switchd         : Maintenance, cold, down, up time: 29:06:31
 System Services : Maintenance, cold, down, up time: 29:07:00

Action succeeded
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -m1
```

{{< /tab >}}
{{< /tabs >}}

To disable maintenance mode:

{{< tabs "229 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action disable system maintenance mode
Action executing ...
System maintenance mode has been disabled successfully
 Current System Mode: cold  
 frr             : cold, up, up time: 12:57:48 (1 restart)
 switchd         : cold, up, up time: 13:12:13
 System Services : cold, up, up time: 13:12:32
Action succeeded
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -m0
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Before you disable maintenance mode, be sure to bring the ports back up.
{{%/notice%}}

To show maintenance mode status either run the NVUE `nv show system maintenance` command or the Linux `sudo csmgrctl -s` command:

```
cumulus@switch:~$ nv show system maintenance 
       operational
-----  -----------
mode   enabled   
ports  disabled 
```

```
cumulus@switch:~$ sudo csmgrctl -s
Current System Mode: cold  
 frr             : cold, up, up time: 00:14:51 (2 restarts)
 clagd           : cold, up, up time: 00:14:47
 switchd         : cold, up, up time: 01:09:48
 System Services : cold, up, up time: 01:10:07
```

## Maintenance Ports

Maintenance ports globally disables or enables all configured ports.
- When you enable maintenance ports, swp interfaces follow individual admin states.
- When you disable maintenance ports, swp interfaces are globally admin down, overriding the admin state in the configuration.

To enable maintenance ports:

{{< tabs "279 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action enable system maintenance ports
Action executing ...
System maintenance ports has been enabled successfully
 Current System Mode: cold  
 frr             : cold, up, up time: 28:54:36
 switchd         : cold, up, up time: 28:54:40
 System Services : cold, up, up time: 28:55:09

Action succeeded
```

{{< /tab >}}
{{< tab "csmgrctl Commands ">}}

```
cumulus@switch:~$ sudo csmgrctl -p0
```

{{< /tab >}}
{{< /tabs >}}

To disable maintenance ports:

{{< tabs "315 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action disable system maintenance ports
Action executing ...
System maintenance ports has been disabled successfully
 Current System Mode: cold  
 Ports shutdown for Maintenance
 frr             : cold, up, up time: 28:55:49
 switchd         : cold, up, up time: 28:55:53
 System Services : cold, up, up time: 28:56:22

Action succeeded
```

{{< /tab >}}
{{< tab "csmgrctl Commands ">}}

```
cumulus@switch:~$ sudo csmgrctl -p1
```

{{< /tab >}}
{{< /tabs >}}

To see the status of maintenance ports, run the NVUE `nv show system maintenance` command:

```
cumulus@switch:~$ nv show system maintenance 
       operational
-----  -----------
mode   enabled   
ports  disabled 
```
