---
title: Traditional Bridge Mode
author: NVIDIA
weight: 440
toc: 4
---
For traditional Linux bridges, the kernel supports VLANs in the form of VLAN subinterfaces. When you enable bridging on multiple VLANs, you configure a bridge for each VLAN and create one or more VLAN subinterfaces for each member port on the bridge. This mode can pose scalability challenges with configuration size as well as boot time and run time state management when the number of ports times the number of VLANs becomes large.

{{%notice note%}}
- Use *{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode">}}* bridges instead of *traditional mode* bridges. 
- Use traditional mode bridges if you need to use PVSTP+.
{{%/notice%}}

## Configure a Traditional Mode Bridge

The following example commands configure a traditional mode bridge called `my_bridge`, where swp1, swp2, swp3, and swp4 are members of the bridge. The example also configures the bridge with IP address 10.10.10.10/24 to provide IP access to the bridge interface.

{{< tabs "TabID24 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for traditional bridge mode.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file, then run the `ifreload -a` command.

```
...
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3

auto swp4
iface swp4

auto my_bridge
iface my_bridge
    address 10.10.10.10/24
    bridge-ports swp1 swp2 swp3 swp4
    bridge-vlan-aware no
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
- Do not bridge the management port, eth0, with any switch ports (swp0, swp1, and so on). For example, if you create a bridge with eth0 and swp1, it does **not** work.
- The name of the bridge must be compliant with Linux interface naming conventions and unique within the switch.
{{%/notice%}}

To configure spanning tree options for a bridge interface, refer to {{<link title="Spanning Tree and Rapid Spanning Tree - STP">}}.

## Configure Multiple Traditional Mode Bridges

You can configure multiple bridges to divide a switch into multiple layer 2 domains. This enables hosts to communicate with other hosts in the same domain, while separating them from hosts in other domains.

The example below shows a multiple bridge configuration, where host-1 and host-2 connect to bridge-A, and host-3 and host-4 connect to bridge-B:

- host-1 and host-2 can communicate with each other
- host-3 and host-4 can communicate with each other
- host-1 and host-2 cannot communicate with host-3 and host-4

{{< img src = "/images/cumulus-linux/ethernet-bridging-multiple-bridges.png" >}}

This example configuration looks like this in the `/etc/network/interfaces` file:

```
...
auto bridge-A
iface bridge-A
    bridge-ports swp1 swp2
    bridge-vlan-aware no

auto bridge-B
iface bridge-B
    bridge-ports swp3 swp4
    bridge-vlan-aware no
...
```

## Trunks in Traditional Bridge Mode

The {{<exlink url="http://www.ieee802.org/1/pages/802.1Q.html" text=" standard">}} for trunking is 802.1Q. The 802.1Q specification adds a four byte header within the Ethernet frame that identifies the VLAN of which the frame is a member.

802.1Q also identifies an *untagged* frame as belonging to the *native* VLAN (most network devices default their native VLAN to 1). In Cumulus Linux:

- A *trunk port* is a switch port configured to send and receive 802.1Q tagged frames.
- A switch sending an untagged (bare Ethernet) frame on a trunk port is sending from the native VLAN defined on the trunk port.
- A switch sending a tagged frame on a trunk port is sending to the VLAN identified by the 802.1Q tag.
- A switch receiving an untagged (bare Ethernet) frame on a trunk port places that frame in the native VLAN defined on the trunk port.
- A switch receiving a tagged frame on a trunk port places that frame in the VLAN identified by the 802.1Q tag.

A bridge in traditional mode has no concept of trunks, just tagged or untagged frames. With a trunk of 200 VLANs, there needs to be 199 bridges, each containing a tagged physical interface, and one bridge containing the native untagged VLAN.

{{%notice note%}}
The interaction of tagged and untagged frames on the same trunk often leads to undesired and unexpected behavior. A switch that uses VLAN 1 for the native VLAN can send frames to a switch that uses VLAN 2 for the native VLAN, merging those two VLANs and their spanning tree state.
{{%/notice%}}

{{< img src = "/images/cumulus-linux/ethernet-bridging-trunk1.png" >}}

To create the above example:

{{< tabs "TabID128 ">}}
{{< tab "NVUE Commands ">}}

Cumulus Linux does not provide NVUE commands for traditional bridge mode.

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the following configuration to the `/etc/network/interfaces` file:

```
...
auto br-VLAN10
iface br-VLAN10
   bridge-ports swp1.10 swp2.10

auto br-VLAN20
iface br-VLAN20
   bridge-ports swp1.20 swp2.20
...
```

{{< /tab >}}
{{< /tabs >}}

## Advanced VLAN Tagging Example

The following advanced VLAN tagging configuration shows three hosts and two switches, with several bridges and a bond that connects them all.
<!-- vale off -->
{{< img src = "/images/cumulus-linux/vlan-tagging-trunks-bond-adv.png" >}}
<!-- vale on -->
- *host1* connects to bridge *br-untagged* with bare Ethernet frames and to bridge *br-tag100* with 802.1q frames tagged for *vlan100*.
- *host2* connects to bridge *br-tag100* with 802.1q frames tagged for *vlan100* and to bridge *br-vlan120* with 802.1q frames tagged for *vlan120*.
- *host3* connects to bridge *br-vlan120* with 802.1q frames tagged for *vlan120* and to bridge *v130* with 802.1q frames tagged for *vlan130*.
- *bond2* carries tagged and untagged frames in this example.

The bridge member ports function as 802.1Q *access ports* and *trunk ports*. To compare Cumulus Linux with a traditional Cisco device:

- *swp1* is equivalent to a trunk port with untagged and *vlan100*.
- *swp2* is equivalent to a trunk port with *vlan100* and *vlan120*.
- *swp3* is equivalent to a trunk port with *vlan120* and *vlan130*.
- *bond2* is equivalent to an EtherChannel in trunk mode with untagged, *vlan100*, *vlan120*, and *vlan130*.
- Bridges *br-untagged*, *br-tag100*, *br-vlan120*, and *v130* are equivalent to SVIs (switched virtual interfaces).

To create the above configuration, edit the `/etc/network/interfaces` file and add a configuration like the following:

```
# Config for host1

# swp1 does not need an iface section unless it has a specific setting
# it will be picked up as a dependent of swp1.100
# swp1 must exist in the system to create the .1q subinterfaces
# but it is not applied to any bridge or assigned an address

auto swp1.100
iface swp1.100

# Config for host2
# swp2 does not need an iface section unless it has a specific setting
# it will be picked up as a dependent of swp2.100 and swp2.120
# swp2 must exist in the system to create the .1q subinterfaces
# but it is not applied to any bridge or assigned an address

auto swp2.100
iface swp2.100

auto swp2.120
iface swp2.120

# Config for host3
# swp3 does not need an iface section unless it has a specific setting
# it will be picked up as a dependent of swp3.120 and swp3.130
# swp3 must exist in the system to create the .1q subinterfaces
# but it is not applied to any bridge or assigned an address

auto swp3.120
iface swp3.120

auto swp3.130
iface swp3.130

# configure the bond

auto bond2
iface bond2
  bond-slaves glob swp4-7

# configure the bridges

auto br-untagged
iface br-untagged
    address 10.0.0.1/24
    bridge-ports swp1 bond2
    bridge-stp on

auto br-tag100
iface br-tag100
    address 10.0.100.1/24
    bridge-ports swp1.100 swp2.100 bond2.100
    bridge-stp on

auto br-vlan120
iface br-vlan120
    address 10.0.120.1/24
    bridge-ports swp2.120 swp3.120 bond2.120
    bridge-stp on

auto v130
iface v130
    address 10.0.130.1/24
    bridge-ports swp3.130 bond2.130
    bridge-stp on
```

To verify the configuration:

```
cumulus@switch:~$ sudo mstpctl showbridge br-tag100
br-tag100 CIST info
  enabled         yes
  bridge id       8.000.44:38:39:00:32:8B
  designated root 8.000.44:38:39:00:32:8B
  regional root   8.000.44:38:39:00:32:8B
  root port       none
  path cost     0          internal path cost   0
  max age       20         bridge max age       20
  forward delay 15         bridge forward delay 15
  tx hold count 6          max hops             20
  hello time    2          ageing time          300
  force protocol version     rstp
  time since topology change 333040s
  topology change count      1
  topology change            no
  topology change port       swp2.100
  last topology change port  None
```

```
cumulus@switch:~$ sudo mstpctl showportdetail br-tag100  | grep -B 2 state
br-tag100:bond2.100 CIST info
  enabled            yes                     role                 Designated
  port id            8.003                   state                forwarding
--
br-tag100:swp1.100 CIST info
  enabled            yes                     role                 Designated
  port id            8.001                   state                forwarding
--
  br-tag100:swp2.100 CIST info
  enabled            yes                     role                 Designated
  port id            8.002                   state                forwarding
```

```
cumulus@switch:~$ cat /proc/net/vlan/config
VLAN Dev name    | VLAN ID
Name-Type: VLAN_NAME_TYPE_RAW_PLUS_VID_NO_PAD
bond2.100      | 100  | bond2
bond2.120      | 120  | bond2
bond2.130      | 130  | bond2
swp1.100       | 100  | swp1
swp2.100       | 100  | swp2
swp2.120       | 120  | swp2
swp3.120       | 120  | swp3
swp3.130       | 130  | swp3
```

{{%notice warning%}}
A single bridge cannot contain multiple subinterfaces of the **same** port. If you try to apply this configuration, you see an error:

```
cumulus@switch:~$ sudo brctl addbr another_bridge
cumulus@switch:~$ sudo brctl addif another_bridge swp9 swp9.100
bridge cannot contain multiple subinterfaces of the same port: swp9, swp9.100
```
{{%/notice%}}

## VLAN Translation

By default, Cumulus Linux does not allow VLAN subinterfaces associated with different VLAN IDs to be part of the same bridge. Base interfaces do not associate with any VLAN IDs and are exempt from this restriction.

In some cases, it is useful to relax this restriction. For example, when two servers connect to the switch using VLAN trunks, but the VLAN numbering on the two servers is not consistent. You can bridge two VLAN subinterfaces of different VLAN IDs from the servers by enabling the `sysctl net.bridge.bridge-allow-multiple-vlans` option. Packets that enter a bridge from a member VLAN subinterface egress another member VLAN subinterface with the VLAN ID translated.

The following example enables the VLAN translation `sysctl`:

```
cumulus@switch:~$ echo net.bridge.bridge-allow-multiple-vlans = 1 | sudo tee /etc/sysctl.d/multiple_vlans.conf
net.bridge.bridge-allow-multiple-vlans = 1
cumulus@switch:~$ sudo sysctl -p /etc/sysctl.d/multiple_vlans.conf
net.bridge.bridge-allow-multiple-vlans = 1
```

After you enable `sysctl`, you can add ports with different VLAN IDs to the same bridge. In the following example, the switch bridges packets that enter the bridge `br-mix` from swp10.100 to swp11.200. Cumulus Linux translates the VLAN ID from 100 to 200:

```
cumulus@switch:~$ sudo brctl addif br_mix swp10.100 swp11.200

cumulus@switch:~$ sudo brctl show br_mix
bridge name     bridge id               STP enabled     interfaces
br_mix          8000.4438390032bd       yes             swp10.100
                                                        swp11.200
```
