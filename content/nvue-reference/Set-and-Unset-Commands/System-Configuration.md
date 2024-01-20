---
title: System Configuration
author: Cumulus Networks
weight: 760

type: nojsscroll
---
<style>
h { color: RGB(118,185,0)}
</style>
{{%notice note%}}
The `nv unset` commands remove the configuration you set with the equivalent `nv set` commands. This guide only describes an `nv unset` command if it differs from the `nv set` command.
{{%/notice%}}

## <h>nv set system config</h>

Configures system configuration settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system config apply</h>

Configures how NVUE performs `config apply` operations.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system config apply ignore \<ignore-id\></h>

Configures NVUE to ignore a specific underlying Linux file when applying configuration changes. For example, if you push certain configuration to the switch using Ansible and Jinja2 file templates or you want to use custom configuration for a particular service such as PTP, you can ensure that NVUE never writes to those configuration files.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set system config apply ignore /etc/ptp4l.conf
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system config apply overwrite</h>

Configures which files NVUE overwrites during `nv config apply`. You can specify:
- `all` to overwrite all files. If you modified a file locally, you see a warning when you try to apply the configuration and you can stop the apply before NVUE overwrites the local modification. This is the default setting.
- `controlled` overwrites only the files that NVUE most recently changed. If you changed a file locally, you see a warning but NVUE does not overwrite the file.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system config apply overwrite controlled
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system config auto-save</h>

Configures the configuration auto save feature.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system config auto-save enable</h>

Turns auto save on or off. The auto save option lets you save the pending configuration to the startup configuration file automatically when you run `nv config apply` so that you do not have to run the `nv config save` command.

### Version History

Introduced in Cumulus Linux 5.4.0

### Example

```
cumulus@switch:~$ nv set system config auto-save enable on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane</h>

Configures control plane settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane policer \<policer-id\></h>

Configures control plane policers.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane policer \<policer-id\> burst</h>

Configures the control plane policer burst rate, which is the number of packets or kilobytes (KB) allowed to arrive sequentially. You can specify a value between 10 and 10000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The policer ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system control-plane policer acl-log burst 1000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane policer \<policer-id\> rate</h>

Configures the control plane policer forwarding rate, which is the maximum rate in kilobytes (KB) for packets. You can specify a value between 10 and 50000.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The policer ID. |

### Version History

Introduced in Cumulus Linux 5.2.0

### Example

```
cumulus@switch:~$ nv set system control-plane policer acl-log burst 5000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane policer \<policer-id\> state</h>

Turns the specified control plane policer on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<policer-id>` |  The policer ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system control-plane policer acl-log state on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane trap \<trap-id\></h>

Configures control plane traps.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system control-plane trap \<trap-id\> state</h>

Turns the specified control plane trap on or off.

### Command Syntax

| Syntax |  Description   |
| ---------  | -------------- |
| `<trap-id>` |  The trap ID. |

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system control-plane trap l3-mtu-err state on
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system counter</h>

Configures the system counter polling intervals.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system counter polling-interval</h>

Configures the system counter polling interval for logical and physical interfaces

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system counter polling-interval logical-interface</h>

Configures the system counter polling interval in seconds for logical interfaces. You can set a value between 1 and 30.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system counter polling-interval logical-interface 20
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system counter polling-interval physical-interface</h>

Configures the system counter polling interval in seconds for physical interfaces. You can set a value between 1 and 10.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system counter polling-interval physical-interface 5
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global</h>

Configures global system settings.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global anycast-id</h>

Configures the global system anycast ID for VXLAN active-active mode. Cumulus Linux derives the MAC address from the ID. You can specify a number between 1 and 65535. Cumulus Linux adds the number to the MAC address 44:38:39:ff:00:00 in hex. For example, if you specify 225, the anycast MAC address is 44:38:39:ff:00:FF.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global anycast-id 255
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global anycast-mac</h>

Configures the global anycast MAC address for VXLAN active-active mode. You can set the anycast MAC address to a value in the reserved range between 44:38:39:ff:00:00 and 44:38:39:ff:ff:ff. Be sure to use an address in this reserved range to prevent MAC address conflicts with other interfaces in the same bridged network.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global anycast-mac 44:38:39:ff:00:ff
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global fabric-id</h>

Configures the fabric ID from which Cumulus Linux derives the MAC address. You can specify a number between 1 and 225. Cumulus Linux adds the number to the MAC address 00:00:5E:00:01:00 in hex. For example, if you specify 225, the VRR MAC address is 00:00:5E:00:01:FF.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set system global fabric-id 255
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global fabric-mac</h>

Configures the VRR MAC address globally on the switch. The default fabric MAC address is 00:00:5E:00:01:01, which the switch derives from a fabric ID setting of 1.

### Version History

Introduced in Cumulus Linux 5.1.0

### Example

```
cumulus@switch:~$ nv set system global fabric-mac 00:00:5E:00:01:FF
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved</h>

Configures reserved system settings, such as the reserved routing table ranges and reserved VLAN ranges.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table</h>

Configures the reserved routing table ranges.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table pbr</h>

Configures the PBR reserved routing table ranges.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table pbr begin</h>

Configures the PBR reserved routing table start range. You can set a value between 10000 and 4294966272.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global reserved routing-table pbr begin 10000
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved routing-table pbr end</h>

Configures the PBR reserved routing table end range. You can set a value between 10000 and 4294966272.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global reserved routing-table pbr end 4294966272
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved vlan</h>

Configures the reserved VLAN range.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved vlan internal</h>

Configures the internal reserved VLAN range.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved vlan internal range</h>

Configures the reserved VLAN range. You can set a value between 4064 and 4094.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system global reserved vlan internal range 4064-4094
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved vlan l3-vni-vlan</h>

Configures the reserved VLANs to use with layer 3 VNIs.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved vlan l3-vni-vlan begin</h>

Configures the reserved VLAN start range to use with layer 3 VNIs. You can set a value between 1 and 4093.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system global reserved vlan l3-vni-vlan begin 1
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global reserved vlan l3-vni-vlan end</h>

Configures the reserved VLAN end range to use with layer 3 VNIs. You can set a value between 2 and 4093.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system global reserved vlan l3-vni-vlan begin 4093
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system global system-mac</h>

Configures the global system MAC address.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system global system-mac 44:38:39:ff:00:ff
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system hostname</h>

Configures the hostname of the switch.

### Version History

Introduced in Cumulus Linux 5.0.0

### Example

```
cumulus@switch:~$ nv set system hostname leaf01
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system message</h>

Configures the message you want users of the switch to see before and after they log in.

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system message post-login</h>

Configures the message you want users to see after they log into the switch. If the message contains more than one word, you must enclose it in quotes (").

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system message post-login "This switch is being used for testing"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system message pre-login</h>

Configures the message you want users to see before they log in to the switch. If the message contains more than one word, you must enclose it in quotes (").

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system message pre-login "This switch is under maintenance"
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system reboot mode</h>

Configures the restart mode for the switch. You can restart the switch in one of the following modes.
- `cold` restarts the system and resets all the hardware devices on the switch (including the switching ASIC).
- `fast` restarts the system more efficiently with minimal impact to traffic by reloading the kernel and software stack without a hard reset of the hardware. During a fast restart, the system decouples from the network to the extent possible using existing protocol extensions before recovering to the operational mode of the system. The restart process maintains the forwarding entries of the switching ASIC and the data plane is not affected. Traffic outage is much lower in this mode as there is a momentary interruption after reboot, after switchd restarts.
- `warm` restarts the system with minimal impact to traffic and without affecting the data plane. Warm mode diverts traffic from itself and restarts the system without a hardware reset of the switch ASIC. While this process does not affect the data plane, the control plane is absent during restart and is unable to process routing updates. However, if no alternate paths exist, the switch continues forwarding with the existing entries with no interruptions.

### Version History

Introduced in Cumulus Linux 5.5.0

### Example

```
cumulus@switch:~$ nv set system reboot mode fast
```

<HR STYLE="BORDER: DASHED RGB(118,185,0) 0.5PX;BACKGROUND-COLOR: RGB(118,185,0);HEIGHT: 4.0PX;"/>

## <h>nv set system timezone</h>

Configures the switch time zone.

To see all the available time zones, run `nv set system timezone` and press the Tab key.

### Version History

Introduced in Cumulus Linux 5.3.0

### Example

```
cumulus@switch:~$ nv set system timezone US/Eastern
```
