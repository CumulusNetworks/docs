---
title: In Service System Upgrade - ISSU
author: NVIDIA
weight: 275
toc: 3
---
Use <span style="background-color:#F5F5DC">[ISSU](## "In Service System Upgrade")</span> to upgrade and troubleshoot an active switch with minimal disruption to the network.

ISSU includes the following modes:
- Restart
- Upgrade
- Maintenance

{{%notice note%}}
In earlier Cumulus Linux releases, ISSU was Smart System Manager.
{{%/notice%}}

## Restart Mode

You can configure the switch to restart in one of the following modes.

- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC).
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintains the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the system with no interruption to traffic for existing route entries. Warm mode restarts the system without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions.

   When you restart the switch in warm mode, BGP performs a graceful restart if the BGP Graceful Restart option is on. To enable BGP Graceful Restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

{{%notice note%}}
Cumulus Linux supports fast mode for all protocols; however only supports warm mode for layer 2 forwarding, and layer 3 forwarding with BGP and static routing.
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
- **all** runs `apt-get upgrade` to upgrade all the system components to the latest release without affecting traffic flow. You must restart the system after the upgrade completes with one of the {{<link url="#restart-mode" text="restart modes">}}.
- **dry-run** provides information on the components you want to upgrade.

The following command upgrades all the system components:

{{< tabs "88 ">}}
{{< tab "NVUE Command ">}}

The NVUE command is not supported.

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

The NVUE command is not supported.

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
cumulus@switch:~$ nv action change system maintenance mode enabled
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

```
cumulus@switch:~$ nv action change system maintenance ports enabled
```

{{< /tab >}}
{{< tab "csmgrctl Commands ">}}

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

Run the following command to disable maintenance mode and restore normal operation. When maintenance mode is off, ISSU performs a soft restart, runs a BGP graceful restart, and brings the MLAG port link back up. `switchd` maintains full capability.

{{< tabs "210 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv action change system maintenance mode disabled
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

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
