---
title: In Service System Upgrade - ISSU
author: NVIDIA
weight: 275
toc: 3
---
Use <span class="a-tooltip">[ISSU](## "In Service System Upgrade")</span> to upgrade and troubleshoot an active switch with minimal disruption to the network.

ISSU includes the following modes:
- Restart
- Upgrade
- Maintenance

{{%notice note%}}
- In earlier Cumulus Linux releases, ISSU was Smart System Manager.
- The NVIDIA SN5600 (Spectrum-4) switch does not support ISSU.
{{%/notice%}}

## Restart Mode

You can configure the switch to restart in one of the following modes.

- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC).
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintains the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the system with no interruption to traffic for existing route entries. Warm mode restarts the system without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions.

   When you restart the switch in warm mode, BGP only performs a graceful restart if the BGP graceful restart option is set to `full`. To set BGP graceful restart to full, run the `nv set router bgp graceful-restart mode full` command, then apply the configuration with `nv config apply`. For more information about BGP graceful restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

{{%notice note%}}
Cumulus Linux supports:
- Fast mode for all protocols.
- Warm mode for 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN. Cumulus Linux does not support warm boot with EVPN MLAG or EVPN multihoming.
{{%/notice%}}

NVIDIA recommends you use NVUE commands to configure restart mode and reboot the system. If you prefer to use `csmgrctl` commands, you must stop NVUE from managing the `/etc/cumulus/csmgrd.conf` file before you set restart mode:

1. Run the following NVUE commands:

   ```
   cumulus@switch:~$ nv set system config apply ignore /etc/cumulus/csmgrd.conf
   cumulus@switch:~$ nv config apply
   ```

2. Edit the `/etc/cumulus/csmgrd.conf` file and set the `csmgrctl_override` option to `true`:

   ```
   cumulus@switch:~$ sudo nano /etc/cumulus/csmgrd.conf
   csmgrctl_override=true
   ...
   ```

3. Save the configuration:

   ```
   cumulus@switch:~$ nv config save
   ```

The following command configures the switch to restart in cold mode:

{{< tabs "28 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode cold
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -c
```

{{< /tab >}}
{{< /tabs >}}

The following command configures the switch to restart in fast mode:

{{< tabs "52 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode fast
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -f
```

{{< /tab >}}
{{< /tabs >}}

The following command configures the switch to restart in warm mode.
<!--
{{< notice warning >}}
Warm restart mode resets any manually configured FEC settings.
{{< /notice >}}
-->
{{< tabs "76 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode warm
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -w
```

{{< /tab >}}
{{< /tabs >}}

To reboot the switch in the restart mode you configure above with NVUE:

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{%notice note%}}
You must specify `no-confirm` at the end of the command.
{{%/notice%}}

To show system reboot information, such as the reboot date and time, reason, and reset mode (fast, cold, warm), run the NVUE `nv show system reboot` command:

```
cumulus@switch:~$ nv show system reboot
           operational                       applied  pending
---------  --------------------------------  -------  -------
reason                                                       
  gentime  2023-04-26T15:11:23.140569+00:00                  
  reason   Unknown                                           
  user     system/root
```

## Upgrade Mode

Upgrade mode updates all the components and services on the switch to the latest Cumulus Linux minor release without impacting traffic. After upgrade is complete, you must restart the switch with either a {{<link url="#restart-mode" text="warm, cold, or fast restart">}}.

If the switch is in warm restart mode, restarting the switch after an upgrade does not result in traffic loss (this is a hitless upgrade).

Upgrade mode includes the following options:
- You can upgrade all the system components to the **latest** release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.
- You can perform an upgrade dry run, which provides information on the components you want to upgrade so that you can review potential upgrade issues (in some cases, upgrading new packages might also upgrade additional existing packages due to dependencies).

The following command upgrades all the system components to the latest release:

{{< tabs "88 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action upgrade system packages to latest use-vrf default
```

By default, the NVUE `nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf>` option.

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -u
```

{{< /tab >}}
{{< /tabs >}}

The following command provides information on the components you want to upgrade:

{{< tabs "114 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action upgrade system packages to latest use-vrf default dry-run
```

By default, the NVUE `nv action upgrade system packages` command runs in the management VRF. To run the command in a non-management VRF such as `default`, you must use the `use-vrf <vrf>` option.

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -d
```

{{< /tab >}}
{{< /tabs >}}

## Maintenance Mode

Maintenance mode isolates the system from the rest of the network so that you can perform intrusive troubleshooting tasks and data collection or perform system changes with minimal disruption, such as split ports and replace optics or cables.

{{%notice note%}}
- Cumulus Linux supports maintenance mode with BGP and MLAG only.
- Complete isolation depends on your configuration and network topology.
{{%/notice%}}

### Enable Maintenance Mode

Run the following command to enable maintenance mode. When maintenance mode is on, ISSU performs a {{<link url="Optional-BGP-Configuration/#graceful-bgp-shutdown" text="graceful BGP shutdown">}}, redirects traffic over the peerlink and brings down the MLAG port link. `switchd` maintains full capability.

{{< tabs "150 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action enable system maintenance mode
System maintenance mode has been enabled successfully
 Current System Mode: Maintenance, cold  
 Maintenance mode since Sat Nov 18 07:09:25 2023 (Duration: 00:00:00)
 frr             : Maintenance, cold, down, up time: 12:55:51 (1 restart)
 switchd         : Maintenance, cold, down, up time: 13:10:16
 System Services : Maintenance, cold, down, up time: 13:10:35
Action succeeded
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -m1
```

{{< /tab >}}
{{< /tabs >}}

You can run additional commands to bring all the ports down, then up to restore the port admin state.

{{< tabs "176 ">}}
{{< tab "NVUE Command ">}}

To bring all the ports down:

```
cumulus@switch:~$ nv action enable system maintenance ports
System maintenance ports has been enabled successfully
 Current System Mode: Maintenance, cold  
 Maintenance mode since Sat Nov 18 07:09:25 2023 (Duration: 00:00:56)
 frr             : Maintenance, cold, down, up time: 12:56:47 (1 restart)
 switchd         : Maintenance, cold, down, up time: 13:11:12
 System Services : Maintenance, cold, down, up time: 13:11:31
Action succeeded
```

To restore the port admin state:

```
cumulus@switch:~$ nv action disable system maintenance ports
System maintenance ports has been disabled successfully
 Current System Mode: cold  
 Ports shutdown for Maintenance
 frr             : cold, up, up time: 13:00:57 (1 restart)
 switchd         : cold, up, up time: 13:15:22
 System Services : cold, up, up time: 13:15:41
Action succeeded
```

{{< /tab >}}
{{< tab "csmgrctl Commands ">}}

To bring  all the ports down:

```
cumulus@switch:~$ sudo csmgrctl -p0
```

To restore the port admin state:

```
cumulus@switch:~$ sudo csmgrctl -p1
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Before you disable maintenance mode, be sure to bring the ports back up.
{{%/notice%}}

### Disable Maintenance Mode

Run the following command to disable maintenance mode and restore normal operation. When maintenance mode is off, ISSU performs a soft restart, runs a BGP graceful restart, and brings the MLAG port link back up. `switchd` maintains full capability.

{{< tabs "210 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action disable system maintenance mode
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

### Show Maintenance Mode Status

To see the status of maintenance mode, run the NVUE `nv show system maintenance` command or the Linux `sudo csmgrctl -s` command. For example:

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
