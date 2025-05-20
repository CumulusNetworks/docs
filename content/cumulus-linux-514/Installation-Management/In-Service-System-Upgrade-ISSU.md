---
title: In Service System Upgrade - ISSU
author: NVIDIA
weight: 35
toc: 3
---
Use <span class="a-tooltip">[ISSU](## "In Service System Upgrade")</span> (warm reboot mode) to restart the switch with minimal disruption to the network.

**Warm** reboot mode restarts the switch with no interruption to traffic for existing route entries and without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions. Warm reboot mode reduces all of the available {{<link title="Forwarding Table Size and Profiles" text="forwarding table entries">}} on the switch by half to accommodate traffic forwarding during a reboot.

When you restart the switch in warm reboot mode, BGP only performs a graceful restart if the BGP graceful restart option is set to `full`. To set BGP graceful restart to full, run the `nv set router bgp graceful-restart mode full` command, then apply the configuration with `nv config apply`. For more information about BGP graceful restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

In an eBGP multihop configuration with warm reboot mode, you must set the {{<link url="Optional-BGP-Configuration/#restart-timers" text="BGP graceful restart timer">}} to 180 seconds or more.

By default, the switch restarts in cold mode, which resets all the hardware devices on the switch (including the switching ASIC). See {{<link url="System-Power-and-Switch-Reboot/#switch-reboot" text="System Power and Switch Reboot">}}.

{{%notice note%}}
Cumulus Linux supports warm reboot mode with:
- 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN. Cumulus Linux does not support warm boot with EVPN MLAG or EVPN multihoming.
- Optimized image (two partition) upgrade and package upgrade (the switch must be in warm reboot mode before you start the upgrade).
{{%/notice%}}

## Configure Warm Reboot Mode

To configure warm reboot mode, run the following commands:

{{< tabs "23 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode warm
cumulus@switch:~$ nv config apply
```

Reboot the switch:

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{%notice note%}}
You must specify `no-confirm` at the end of the command.
{{%/notice%}}

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

NVIDIA recommends you use NVUE commands to configure warm reboot mode and reboot the system. If you prefer to use `csmgrctl` commands, you must stop NVUE from managing the `/etc/cumulus/csmgrd.conf` file before you set restart mode:

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

4. Set warm reboot mode:

   ```
   cumulus@switch:~$ sudo csmgrctl -w
   ```

5. Reboot the switch:

   ```
   cumulus@switch:~$ sudo reboot
   ```

{{< /tab >}}
{{< /tabs >}}

{{%notice warning%}}
After you set warm reboot mode on the switch with NVUE or `csmgrctl` commands, you **must** reboot the switch to activate the mode change.
{{%/notice%}}

## Show Warm Boot Configuration

You can confirm the current operational reboot mode active on the switch with the `nv show system reboot` command. The command also shows reboot information, such as the reboot date and time, and reason:

```
cumulus@switch:~$ nv show system reboot
           operational                       applied
---------  --------------------------------  -------
reason                                              
  reason   Unknown                                  
  gentime  2025-05-16T16:08:27.798068+00:00         
  user     system/root                              
mode       warm                               warm   
required   no
```
