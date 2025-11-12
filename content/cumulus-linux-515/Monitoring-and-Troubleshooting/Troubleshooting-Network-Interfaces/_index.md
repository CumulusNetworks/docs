---
title: Troubleshooting Network Interfaces
author: NVIDIA
weight: 1090
toc: 3
---
The following sections describe various ways you can troubleshoot `ifupdown2` and network interfaces.

## Monitor Interface Traffic Rate and PPS

Monitoring the traffic rate and <span class="a-tooltip">[PPS](## "Packets per Second")</span> for an interface ensures optimal network performance and reliability. You can use the data provided to allocate and utilize network resources efficiently, ensuring quality of service and preventing network bottlenecks. The data helps you to obtain a comprehensive view of network health, detect any DDoS attacks, and see if the current network can handle peak loads or if you need future network capacity expansion and upgrades.

By monitoring both the traffic rate and PPS, you can identify peak usage times and adjust bandwidth allocation or optimize packet paths to ensure low latency and high throughput.

{{%notice note%}}
- You can monitor the traffic rate and PPS of physical ports that are configured with NVUE.
- The command outputs provide approximate values.
{{%/notice%}}

To show a summary view of the traffic rate and PPS for all interfaces, run the `nv show interface rates` command.

This output shows the received and transmitted traffic rate counters in bits per second, packet rate counters in packets per second, and the link utilization percentage. The unit of measurement for rate counters changes dynamically based on the value of the rate counters. The units can be kbps, Mbps, Gbps or Tbps for bits and kpps, Mpps, Gpps, and Tpps for packets.

```
cumulus@switch:~$ nv show interface rates
Interface  Intvl  In-Bits Rate  In-Util  In-Pkts Rate  Out-Bits Rate  Out-Util  Out-Pkts Rate
---------  -----  ------------  -------  ------------  -------------  --------  -------------
swp1       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp2       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp3       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp4       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp5       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp6       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp7       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp8       60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp9       60     10.00 Gbps    100.0%   822.41 kpps   10.00 Gbps     100.0%    822.42 kpps
swp10      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp11      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp12      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp13      60     7.34 Gbps     73.4%    603.21 kpps   5.00 Gbps      50.0%     411.19 kpps
swp14      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp15      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp16      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp17      60     8.42 Gbps     84.2%    692.80 kpps   6.73 Gbps      67.3%     553.59 kpps
swp18      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp19      60     204 bps       0.0%     0 pps         539 bps        0.0%      1 pps
swp20      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp21      60     6.73 Gbps     67.3%    553.59 kpps   8.42 Gbps      84.2%     692.81 kpps
swp22      60     10.00 Gbps    100.0%   14.88 Mpps    10.00 Gbps     100.0%    14.88 Mpps
swp23      60     10.00 Gbps    100.0%   14.88 Mpps    10.00 Gbps     100.0%    14.88 Mpps
swp24      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp25      60     5.00 Gbps     50.0%    411.19 kpps   7.34 Gbps      73.4%     603.21 kpps
swp26      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp27      60     10.00 Gbps    100.0%   822.42 kpps   10.00 Gbps     100.0%    822.41 kpps
swp28      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp29      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp30      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp31      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
swp32      60     0 bps         0.0%     0 pps         0 bps          0.0%      0 pps
```

To show the traffic rate and PPS for a specific interface, run the `nv show interface <interface-id> rates` command.

```
cumulus@switch:~$ nv show interface swp1 rates
                operational
---------------  -----------
load-interval    10        
in-bits-rate     10.00 Gbps
in-utilization   100.0%    
in-pkts-rate     822.41 kpps
out-bits-rate    10.00 Gbps
out-utilization  100.0%    
out-pkts-rate    822.40 kpps
```

{{%notice note%}}
- The `nv show interface <interface-id> rates` command only supports a range of interfaces with the filter option; for example, `nv show interface rates --filter "Interface=swp1|Interface=swp2"`.
{{%/notice%}}

You can configure the load interval you want to use to calculate interface rates with the `nv set system counter rates load-interval` command. You can specify a value between 1 and 600. The default load interval is 60 seconds.

Cumulus Linux uses the data during the load interval time period and averages it to calculate the interface rate counters. Interface rates are equal weight averages. You configure the load interval globally, not for an interface.

```
cumulus@switch:~$ nv set system counter rates load-interval 30
cumulus@switch:~$ nv config apply
```

To reset the load interval to the default value of 60 seconds, run the `nv unset system counter rates load-interval` command.

To view the configured load interval, run the `nv show system counter rates` command.

## Enable Network Logging

To obtain verbose logs when you run `systemctl start networking.service` or `systemctl restart networking.service` as well as when the switch boots, create an overrides file with the `systemctl edit networking.service` command and add the following lines:

```
[Service]
# remove existing ExecStart rule
ExecStart=
# start ifup with verbose option
ExecStart=/sbin/ifup -av
```

{{%notice note%}}
When you run the `systemctl edit` command, you do *not* need to run `systemctl daemon-reload`.
{{%/notice%}}

To disable logging, either:

- Remove the overrides file. Run the `systemctl cat networking` command to show the name of the overrides file.
- Run the `systemctl edit networking.service` command and remove the lines you added.

## Exclude Certain Interfaces from Coming Up

To exclude an interface so that it does not come up when you boot the switch or when you start, stop, or reload the networking service:

1. Create a file in the `/etc/systemd/system/networking.service.d` directory (for example, `/etc/systemd/system/networking.service.d/override.conf`).
2. Add the lines `ExecStart=/sbin/ifup -a -X <interface-id>` and `ExecStop=/sbin/ifdown -a -X <interface-id>` to the file. The following example stops eth0 from coming up:

    ```
    [Service]
    ExecStart=
    ExecStart=/sbin/ifup -a -X eth0
    ExecStop=
    ExecStop=/sbin/ifdown -a -X eth0
    ```

You can exclude any interface specified in the `/etc/network/interfaces` file.

## Use ifquery to Validate and Debug Interface Configurations

You use `ifquery` to print parsed `interfaces` file entries.

To use `ifquery` to pretty print `iface` entries from the `interfaces` file, run:

```
cumulus@switch:~$ sudo ifquery bond0
auto bond0
iface bond0
    address 14.0.0.9/30
    address 2001:ded:beef:2::1/64
    bond-slaves swp25 swp26
```

Use `ifquery --check` to check the current running state of an interface within the `interfaces` file. The command returns exit code *0* or *1* if the configuration does not match. The line `bond-xmit-hash-policy layer3+7` below fails because it should read `bond-xmit-hash-policy layer3+4`.

```
cumulus@switch:~$ sudo ifquery --check bond0
iface bond0
    bond-xmit-hash-policy layer3+7  [fail]
    bond-slaves swp25 swp26         [pass]
    address 14.0.0.9/30             [pass]
    address 2001:ded:beef:2::1/64   [pass]
```

{{%notice note%}}
`ifquery --check` is an experimental feature.
{{%/notice%}}

Use `ifquery --running` to print the running state of interfaces in the `interfaces` file format:

```
cumulus@switch:~$ sudo ifquery --running swp1
auto swp1
iface swp1
	mtu 9000
	hwaddress 48:b0:2d:01:46:04
```
<!-- vale off -->
`ifquery --syntax-help` provides help on all possible attributes supported in the `interfaces` file. For complete syntax on the `interfaces` file, see `man interfaces` and `man ifupdown-addons-interfaces`.
<!-- vale on -->
You can use `ifquery --print-savedstate` to check the `ifupdown2` state database. `ifdown` works only on interfaces present in this state database.

```
cumulus@leaf1$ sudo ifquery --print-savedstate eth0  
auto eth0
iface eth0 inet dhcp
```

## Mako Template Errors

An easy way to debug and get details about template errors is to use the `mako-render` command on your interfaces template file or on `/etc/network/interfaces` itself.

```
cumulus@switch:~$ sudo mako-render /etc/network/interfaces
iface swp51

cumulus@leaf02:mgmt:~$ sudo mako-render /etc/network/interfaces
# Auto-generated by NVUE!
# Any local modifications will prevent NVUE from re-generating this file.
# md5sum: ac1ff9d35c3cd51f7aa3073ae32debf2
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

source /etc/network/interfaces.d/*.intf

auto lo
iface lo inet loopback
    address 10.10.10.1/32
    vxlan-local-tunnelip 10.10.10.1

auto mgmt
iface mgmt
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto RED
iface RED
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto BLUE
iface BLUE
    address 127.0.0.1/8
    address ::1/128
    vrf-table auto

auto eth0
iface eth0 inet dhcp
    ip-forward off
    ip6-forward off
    vrf mgmt

auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp51
iface swp51

auto swp52
iface swp52

auto bond1
iface bond1
    mtu 9000
    bond-slaves swp1
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 10

auto bond2
iface bond2
    mtu 9000
    bond-slaves swp2
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 20

auto bond3
iface bond3
    mtu 9000
    bond-slaves swp3
    bond-mode 802.3ad
    bond-lacp-bypass-allow yes
    bridge-access 30

auto vlan10
iface vlan10
    address 10.1.10.2/24
    address-virtual 00:00:5e:00:01:01 10.1.10.1/24
    hwaddress 44:38:39:22:01:78
    vrf RED
    vlan-raw-device br_default
    vlan-id 10

auto vlan20
iface vlan20
    address 10.1.20.2/24
    address-virtual 00:00:5e:00:01:01 10.1.20.1/24
    hwaddress 44:38:39:22:01:78
    vrf RED
    vlan-raw-device br_default
    vlan-id 20

auto vlan30
iface vlan30
    address 10.1.30.2/24
    address-virtual 00:00:5e:00:01:01 10.1.30.1/24
    hwaddress 44:38:39:22:01:78
    vrf BLUE
    vlan-raw-device br_default
    vlan-id 30

auto vxlan48
iface vxlan48
    bridge-vlan-vni-map 10=10 20=20 30=30
    bridge-learning off

auto vlan3159_l3
iface vlan3159_l3
    vrf RED
    vlan-raw-device br_l3vni
    vlan-id 3159

auto vlan3607_l3
iface vlan3607_l3
    vrf BLUE
    vlan-raw-device br_l3vni
    vlan-id 3607

auto vxlan99
iface vxlan99
    bridge-vlan-vni-map 3159=4001 3607=4002
    bridge-learning off

auto br_default
iface br_default
    bridge-ports bond1 bond2 bond3 vxlan48
    hwaddress 44:38:39:22:01:78
    bridge-vlan-aware yes
    bridge-vids 10 20 30
    bridge-pvid 1
    bridge-stp yes
    bridge-mcsnoop no
    mstpctl-forcevers rstp

auto br_l3vni
iface br_l3vni
    bridge-ports vxlan99
    hwaddress 44:38:39:22:01:78
    bridge-vlan-aware yes
```

## ifdown Cannot Find an Interface that Exists

If you try to bring down an interface that you know exists, use `ifdown` with the `--use-current-config` option to force `ifdown` to check the current `/etc/network/interfaces` file to find the interface. For example:

```
cumulus@switch:~$ sudo ifdown br0
error: cannot find interfaces: br0 (interface was probably never up ?)

cumulus@switch:~$ sudo brctl show
bridge name   bridge id      STP enabled interfaces
br0      8000.44383900279f   yes     downlink
                             peerlink

cumulus@switch:~$ sudo ifdown br0 --use-current-config 
```

## Remove All References to a Child Interface

If you have a configuration with a child interface, whether it is a VLAN, bond, or another physical interface and you remove that interface from a running configuration, you must remove every reference to it in the configuration. Otherwise, the parent interface continues to use the interface.

For example, consider the following configuration:

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

auto bond1
iface bond1
    bond-slaves swp2 swp1

auto bond3
iface bond3
    bond-slaves swp8 swp6 swp7

auto br0
iface br0
    bridge-ports swp3 swp5 bond1 swp4 bond3
    bridge-pathcosts  swp3=4 swp5=4 swp4=4
    address 11.0.0.10/24
    address 2001::10/64
```

bond1 is a member of br0. If you remove bond1, you must remove the reference to it from the br0 configuration. Otherwise, if you reload the configuration with `ifreload -a`, bond1 remains part of br0.

## MTU Numerical Result Out of Range Error

The MTU `Numerical result out of range` error occurs when the {{<link url="Switch-Port-Attributes#mtu" text="MTU">}} you are trying to set on an interface is higher than the MTU of the lower interface or dependent interface. Linux expects the upper interface to have an MTU less than or equal to the MTU on the lower interface.

In the example below, the swp1.100 VLAN interface is an upper interface to physical interface swp1. If you want to change the MTU to 9000 on the VLAN interface, you must include the new MTU on the lower interface swp1 as well.

```
auto swp1.100
iface swp1.100
    mtu 9000

auto swp1 
iface swp1  
    mtu 9000
```

## iproute2 batch Command Failures

`ifupdown2` batches `iproute2` commands for performance reasons. A batch command contains `ip -force -batch -` in the error message. The command number that fails is at the end of this line: `Command failed -:1`.

Below is a sample error for the command 1: `link set dev host2 master bridge`. There is an error adding the bond *host2* to the bridge named *bridge* because host2 does not have a valid address.

```
error: failed to execute cmd 'ip -force -batch - [link set dev host2 master bridge
addr flush dev host2
link set dev host1 master bridge
addr flush dev host1
]'(RTNETLINK answers: Invalid argument
Command failed -:1)
warning: bridge configuration failed (missing ports)
```

## "RTNETLINK answers: Invalid argument" Error when Adding a Port to a Bridge

This error can occur when the bridge port does not have a valid hardware address or when the interface you add to the bridge is an incomplete bond; a bond without slaves is incomplete and does not have a valid hardware address.

## MLAG Interface Drops Packets

Losing a large number of packets across an MLAG peerlink interface is often not a problem. This can occur to prevent BUM (broadcast, unknown unicast and multicast) packet looping. For more details, and for information on how to detect these drops, refer to the {{<link url="Multi-Chassis-Link-Aggregation-MLAG" text="MLAG section">}}.
