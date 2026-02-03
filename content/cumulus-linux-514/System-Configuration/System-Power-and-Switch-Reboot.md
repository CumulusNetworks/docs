---
title: System Power and Switch Reboot
author: NVIDIA
weight: 295
toc: 3
---
Cumulus Linux provides commands to:
- {{<link url="#switch-reboot" text="Reboot the switch">}}
- {{<link url="#power-off" text="Power off the switch">}}
- {{<link url="#power-cycle" text="Power cycle the switch">}}

## Switch Reboot

Cumulus Linux provides these reboot modes:
- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC). This is the default restart mode on the switch.
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The switch restarts the kernel and software stack without touching the forwarding entries or the switching ASIC; therefore, the data plane is not affected as the software stack restarts. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the switch with no interruption to traffic for existing route entries and without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. Warm reboot mode reduces all the available {{<link title="Forwarding Table Size and Profiles" text="forwarding table entries">}} on the switch by half to accommodate traffic forwarding during a reboot.

  Review {{<link url="#warm-reboot-and-issu-considerations" text="Warm Reboot and ISSU Considerations">}} to understand support limitations and requirements for warm reboot and ISSU. 

NVIDIA recommends you use NVUE commands to configure reboot mode and reboot the system. If you prefer to use `csmgrctl` commands, you must stop NVUE from managing the `/etc/cumulus/csmgrd.conf` file before you set reboot mode.

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

The following commands configure the switch to restart in cold mode:

{{< tabs "108 ">}}
{{< tab "NVUE Command ">}}

```
cumulus@switch:~$ nv set system reboot mode cold
cumulus@switch:~$ nv config apply
```

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -c
```

```
cumulus@switch:~$ sudo reboot
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

```
cumulus@switch:~$ nv action reboot system no-confirm
```

{{< /tab >}}
{{< tab "csmgrctl Command ">}}

```
cumulus@switch:~$ sudo csmgrctl -f
```

```
cumulus@switch:~$ sudo reboot
```

{{< /tab >}}
{{< /tabs >}}

The following command configures the switch to restart in warm mode.

{{< tabs "85 ">}}
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

```
cumulus@switch:~$ sudo csmgrctl -w
```

```
cumulus@switch:~$ sudo reboot
```

{{< /tab >}}
{{< /tabs >}}

{{%notice warning%}}
After you change the reboot mode on the switch with NVUE or `csmgrctl` commands, you must reboot the switch to activate the mode change.
{{%/notice%}}

### Show Reboot Mode

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


## Warm Reboot and ISSU Considerations

### Warm Reboot Support

Cumulus Linux supports warm reboot mode with 802.1X, layer 2 forwarding, layer 3 forwarding with BGP, static routing, and VXLAN routing with EVPN. 

The following features are not supported during warm reboot:
- EVPN MLAG or EVPN multihoming.
- LACP bonds. LACP control plane sessions might time out before warm reboot completes. Use static LAG to keep bonds up with sub-second convergence during a warm reboot.

### BGP Graceful Restart

When you restart the switch in warm reboot mode, BGP only performs a graceful restart if the BGP graceful restart option is set to `full`. To set BGP graceful restart to full, run the `nv set router bgp graceful-restart mode full` command, then apply the configuration with `nv config apply`. For more information about BGP graceful restart, refer to {{<link url="Optional-BGP-Configuration/#graceful-bgp-restart" text="Optional BGP Configuration">}}.

 You must set the {{<link url="Optional-BGP-Configuration/#restart-timers" text="BGP graceful restart timer">}} to 180 seconds or more to accommodate ISSU.

### ARP Handling

The control plane is responsible for Address Resolution Protocol (ARP) processing. During In-Service Software Upgrade (ISSU) and warm reboot operations, the control plane becomes temporarily unavailable.

If the switch has connected hosts configured with ARP timeout values shorter than approximately 180 seconds, these hosts might experience traffic disruption when gateway ARP entries expire during ISSU. To prevent host connectivity issues during the ISSU process, use one of the following methods:

- Increase ARP parameters such as `base_reachable_time_ms` and `gc_stale_time` on linux hosts so that ARP entries remain valid for a duration longer than the ISSU window.

- Configure static ARP entries. Create required static ARP mappings on the affected hosts before initiating ISSU to ensure uninterrupted ARP resolution.

### Static Routes

When a switch uses a static default route or specific static prefix routes configured only within FRR or through NVUE using the `nv set vrf <vrf-name> router static` command, these routes become temporarily unavailable after a warm reboot while FRR services restart. This can lead to a brief loss of reachability to remote networks.

To maintain connectivity immediately following a warm reboot, configure a kernel  default route with the `nv set interface eth0 ipv4 gateway <gateway-ip>` command, or define the `gateway` parameter under `eth0` in `/etc/network/interfaces` when managing your configuration through linux configuration files.

To add more specific prefix routes directly into the kernel routing table at interface initialization, use ifupdown2 `post-up` hooks in the `/etc/network/interfaces` file:

```
auto eth0
iface eth0
 address 10.100.156.254/24
 post-up ip route add 10.100.200.0/24 via 10.100.156.1 vrf mgmt
```

## Power Off

In certain situations, you might need to power off the switch instead of rebooting. To power off the switch, run the `cl-poweroff` command, which shuts down the switch.

```
cumulus@switch:~$ sudo cl-poweroff
```

You can also run the Linux `poweroff` command, which gracefully shuts down the switch (the switch LEDs stay on). On certain switches, such as the NVIDIA SN2201, SN2010, SN2100, SN2100B, SN3420, SN3700, SN3700C, SN4410, SN4600C, SN4600, SN4700, SN5400, or SN5600, the switch reboots instead of powering off.

```
cumulus@switch:~$ sudo poweroff
```

## Power Cycle

NVUE provides the `nv action power-cycle system` command so that you can power cycle the switch remotely to recover from certain conditions, such as a thermal ASIC shutdown due to high temperatures.

When you run the `nv action power-cycle system` command, the switch prompts you for confirmation before power cycling.

```
cumulus@switch:~$ nv action power-cycle system
The operation will Power Cycle the switch.
Type [y] to power cycle.
Type [N] to abort.

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

To power cycle the switch without prompts for confirmation, run the `nv action power-cycle system force` command:

```
cumulus@switch:~$ nv action power-cycle system force 
Action executing ... 
Action succeeded
```
