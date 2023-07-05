---
title: Monitoring Virtual Device Counters
author: NVIDIA
weight: 1220
toc: 3
---
Cumulus Linux gathers statistics for VXLANs and VLANs using virtual device counters. These counters are supported on Tomahawk, Trident II+ and Trident II-based platforms only; see the {{<exlink url="https://www.nvidia.com/en-us/networking/ethernet-switching/hardware-compatibility-list/" text="Cumulus Linux HCL">}} for a list of supported platforms.

You can retrieve the data from these counters using tools like `ip -s link show`, `ifconfig`, `/proc/net/dev` or `netstat -i`.

{{%notice note%}}
On Mellanox switches, Cumulus Linux updates physical counters to the kernel every two seconds and virtual interfaces (such as VLAN interfaces) every ten seconds. You cannot change these values. Because the update process takes a lower priority than other `switchd` processes, the interval might be longer when the system is under a heavy load.
{{%/notice%}}

## Sample VXLAN Statistics

VXLAN statistics are available as follows:

- Aggregate statistics are available per VNI; this includes access and network statistics.
- Network statistics are available for each VNI and displayed against the VXLAN device. This is independent of the VTEP used, so this is a summary of the VNI statistics across all tunnels.
- Access statistics are available per VLAN subinterface.

To show interface information about the VXLAN bridge:

```
cumulus@switch:~$ brctl show br-vxln16757104
bridge name        bridge id            STP enabled    interfaces
-vxln16757104      8000.443839006988    no             swp2s0.6
                                                       swp2s1.6
                                                       swp2s2.6
                                                       swp2s3.6
                                                       vxln16757104
```

To show VNI statistics, run:

```
cumulus@switch:~$ ip -s link show br-vxln16757104
62: br-vxln16757104: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
    link/ether 44:38:39:00:69:88 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    10848      158      0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    27816      541      0       0       0       0
```

To show access statistics, run:

```
cumulus@switch:~$ ip -s link show swp2s0.6
63: swp2s0.6@swp2s0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-vxln16757104 state UP mode DEFAULT
    link/ether 44:38:39:00:69:88 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    2680       39       0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    7558       140      0       0       0       0
```

To show network statistics, run:

```
cumulus@switch:~$ ip -s link show vxln16757104
61: vxln16757104: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-vxln16757104 state UNKNOWN mode DEFAULT
    link/ether e2:37:47:db:f1:94 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    0          0        0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    0          0        0       9       0       0
```

## Sample VLAN Statistics

### For VLANs Using the VLAN-aware Bridge Mode Driver

For a bridge using the {{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware bridge mode">}} driver, the bridge is a just a container and each VLAN (VID/PVID) in the bridge is an independent layer 2 broadcast domain. As there is no `netdev` available to display these VLAN statistics, the `switchd` nodes are used instead:

```
cumulus@switch:~$ ifquery bridge
auto bridge
iface bridge inet static
  bridge-vlan-aware yes
  bridge-ports swp2s0 swp2s1
  bridge-stp on
  bridge-vids 2000-2002 4094

cumulus@switch:~$ ls /cumulus/switchd/run/stats/vlan/
2  2000  2001  2002  all

cumulus@switch:~$ cat /cumulus/switchd/run/stats/vlan/2000/aggregate
Vlan id                         : 2000
L3 Routed In Octets             : -
L3 Routed In Packets            : -
L3 Routed Out Octets            : -
L3 Routed Out Packets           : -
Total In Octets                 : 375
Total In Packets                : 3
Total Out Octets                : 387
Total Out Packets               : 3
```

### For VLANs Using the Traditional Bridge Mode Driver

For a bridge using the {{<link url="Traditional-Bridge-Mode" text="traditional bridge mode">}} driver, each bridge is a single L2 broadcast domain and is associated with an internal VLAN. This internal VLAN's counters are displayed as bridge netdev stats.

```
cumulus@switch:~$ brctl show br0
bridge name   bridge id            STP enabled   interfaces
br0           8000.443839006989    yes           bond0.100
                                                 swp2s2.100
cumulus@switch:~$ ip -s link show br0
42: br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
    link/ether 44:38:39:00:69:89 brd ff:ff:ff:ff:ff:ff
    RX: bytes  packets  errors  dropped overrun mcast
    23201498   227514   0       0       0       0
    TX: bytes  packets  errors  dropped carrier collsns
    18198262   178443   0       0       0       0
```

## Configure the Counters in switchd

These counters are enabled by default. To configure them, use `cl-cfg` and configure them as you would any other {{%link url="Configuring-switchd" text="`switchd` parameter"%}}. The `switchd` parameters are:

- `stats.vlan.aggregate`, which controls the statistics available for each VLAN. Its value defaults to *BRIEF*.
- `stats.vxlan.aggregate`, which controls the statistics available for each VNI (access and network). Its value defaults to *DETAIL*.
- `stats.vxlan.member`, which controls the statistics available for each local/access port in a VXLAN bridge. Its value defaults to *BRIEF*.

The values for each parameter can be one of the following:

- NONE: This disables the counter.
- BRIEF: This provides tx/rx packet/byte counters for the associated parameter.
- DETAIL: This provides additional feature-specific counters. In the case of `stats.vxlan.aggregate`, DETAIL provides access vs. network statistics. For the other types, DETAIL has the same effect as BRIEF.

{{%notice note%}}

If you change one of these settings on the fly, the new configuration applies only to those VNIs or VLANs set up after the configuration changed; previously allocated counters remain as is.

{{%/notice%}}

### Configure the Poll Interval

The virtual device counters are polled periodically. This can be CPU intensive, so the interval is configurable in `switchd`, with a default of 2 seconds.

```
# Virtual devices hw-stat poll interval (in seconds)
#stats.vdev_hw_poll_interval = 2
```

### Configure Internal VLAN Statistics

For debugging purposes, you can access packet statistics associated with internal VLAN IDs. These statistics are hidden by default, but you can configure them in `switchd`:

```
#stats.vlan.show_internal_vlans = FALSE
```

### Clear Statistics

Because `ethtool` is not supported for virtual devices, you *cannot* clear the statistics cache maintained by the kernel. You can clear the hardware statistics via `switchd`:

```
cumulus@switch:~$ sudo echo 1 > /cumulus/switchd/clear/stats/vlan
cumulus@switch:~$ sudo echo 1 > /cumulus/switchd/clear/stats/vxlan
```

## Considerations

- Currently the CPU port is internally added as a member of all VLANs.Therefore, packets sent to the CPU are counted against the corresponding VLAN's tx packets/bytes. There is no workaround.
- When checking the virtual counters for the bridge, the TX count is the number of packets destined to the CPU before any hardware policers take effect. For example, if 500 broadcast packets are sent into the bridge, the CPU is also sent 500 packets. These 500 packets are policed by the default ACLs in Cumulus Linux, so the CPU might receive fewer than the 500 packets if the incoming packet rate is too high. The TX counter for the bridge should be equal to 500\*(number of ports in the bridge - incoming port + CPU port) or just 500 \* number of ports in the bridge.
- You cannot use `ethtool -S` for virtual devices. This is because the counters available via `netdev` are sufficient to display the VLAN/VXLAN counters currently supported in the hardware (only rx/tx packets/bytes are supported currently).
