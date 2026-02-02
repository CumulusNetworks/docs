---
title: System Power and Switch Reboot
author: NVIDIA
weight: 295
toc: 3
---
Cumulus Linux provides commands to:
- {{<link url="#switch-reboot" text="Reboot the switch">}}
- {{<link url="#power-off" text="Power off the switch">}}

## Switch Reboot

Cumulus Linux provides these reboot modes:
- **immediate** reboots the switch immediately without notifying any running processes. Use this mode to reboot as quickly as possible, skipping graceful shutdown to avoid delays or to avoid the switch from hanging.
- **halt** shuts down the system. Use this mode to stop the switch completely instead of rebooting.
- **power-cycle** lets you power cycle the switch to recover from certain conditions, such as a thermal ASIC shutdown due to high temperatures.
- **cold** restarts the system and resets all the hardware devices on the switch (including the switching ASIC). This is the default restart mode on the switch.
- **fast** restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The switch restarts the kernel and software stack without touching the forwarding entries or the switching ASIC; therefore, the data plane is not affected as the software stack restarts. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, while the system reinitializes.
- **warm** restarts the switch with no interruption to traffic for existing route entries and without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. Warm reboot requires configuring the switch {{<link url="#resource-allocation" text="resource mode">}} to `half` to reduce the available {{<link title="Forwarding Table Size and Profiles" text="forwarding table entries">}} on the switch by half to accommodate traffic forwarding during a reboot.

  Review {{<link url="#warm-reboot-and-issu-considerations" text="Warm Reboot and ISSU Considerations">}} to understand support limitations and requirements for warm reboot and ISSU. 

### Resource Allocation

To manage switch resource allocation, you can configure the resource mode to be either `half` or `full`. By default, the resource mode is set to `full`. Warm reboot and hitless ISSU-based software upgrade requires the resource mode to be `half`.

The following example sets the switch resource mode to `half`:

{{< tabs "TabID40 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set system forwarding resource-mode half
```

To set the resource-mode back to the default value (full) run the `nv unset system forwarding resource-mode` command.

{{%notice infonopad%}}
Changing the resource mode on the switch requires a `switchd` restart, which impacts traffic forwarding. 
{{%/notice%}}

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo nano /etc/cumulus/switchd.d/resource-mode.conf
...
resource_mode = half
```

Restart the switchd service with the `sudo systemctl restart switchd.service` command.

{{< /tab >}}
{{< /tabs >}}

### Reboot

To reboot the switch, run the `nv action reboot system mode <mode>` command. To force the reboot without prompting for confirmation, add the `force` option (`nv action reboot system mode <mode> force`).

The following command reboots the switch immediately without notifying any running processes:

{{< tabs "TabID78">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv action reboot system mode immediate

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo reboot -f
```

{{< /tab >}}
{{< /tabs >}}

The following command shuts down the system:

{{< tabs "TabID101">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv action reboot system mode halt

Do you want to continue? [y/N]  
Action executing ... 
Action succeded
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo halt -f
```

{{< /tab >}}
{{< /tabs >}}

The following command power cycles the switch:

{{< tabs "TabID125">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv action reboot system mode power-cycle
The operation will Power Cycle the switch.
Type [y] to power cycle.
Type [N] to abort.

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo cl-powercycle
```

{{< /tab >}}
{{< /tabs >}}

The following command reboots the switch in cold mode without prompting for confirmation:

{{< tabs "TabID151">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv action reboot system mode cold force
```

You can also run `nv action reboot system force` because cold reboot is the default mode.
{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo csmgrctl -cf
```

{{< /tab >}}
{{< /tabs >}}

{{< tabs "TabID168">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv action reboot system mode fast

Do you want to continue? [y/N]  
Action executing ... 
Action succeeded 
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo csmgrctl -ff
```

{{< /tab >}}
{{< /tabs >}}

The following command reboots the switch in warm mode without prompting for confirmation.

{{< tabs "TabID189">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv action reboot system mode warm force
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ sudo csmgrctl -wf
```

{{< /tab >}}
{{< /tabs >}}

### Show Reboot

To show reboot information, such as the date and time, and reason, and the reboot mode, run the `nv show system reboot` command:

```
cumulus@switch:~$ nv show system reboot
           operational                       applied
---------  --------------------------------  -------
reason                                                     
  reason          Unknown                                  
  gentime         2025-09-30T14:36:27.003819+00:00         
  user            system/root                              
[history]         1                                        
[history]         2                                        
[history]         3                                        
[history]         4                                        
[history]         5                                        
[history]         6                                        
[history]         7                                        
required          no                                       
last-reboot-mode  cold
```

<!-- COMMENTED OUT AS THIS COMMAND ISN'T OPERATIONAL IN 5.15
To display the current resource mode, run the `nv show system forwarding resource-mode` command. 

```
cumulus@switch:~$ nv show system forwarding resource-mode
cumulus@switch:~$ nv config apply
```
-->

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
