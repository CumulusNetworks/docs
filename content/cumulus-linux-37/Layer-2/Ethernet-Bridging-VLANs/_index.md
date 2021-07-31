---
title: Ethernet Bridging - VLANs
author: NVIDIA
weight: 121
pageID: 8362655
---
Ethernet bridges provide a means for hosts to communicate through layer
2, by connecting all of the physical and logical interfaces in the
system into a single layer 2 domain. The bridge is a logical interface
with a MAC address and an
{{<link url="Switch-Port-Attributes/#mtu" text="MTU">}}
(maximum transmission unit). The bridge MTU is the minimum MTU among all
its members. By default, the [bridge's MAC address]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Configuration/Cumulus-Linux-Derivation-of-MAC-Address-for-a-Bridge" >}})
is the MAC address of the first port in the `bridge-ports` list. The
bridge can also be assigned an IP address, as discussed
{{<link url="#configure-an-svi-switch-vlan-interface" text="below">}}.

{{%notice note%}}

Bridge members can be individual physical interfaces, bonds or logical
interfaces that traverse an 802.1Q VLAN trunk.

{{%/notice%}}

{{% img src = "/images/cumulus-linux/ethernet-bridging-example.png" %}}

{{%notice tip%}}

Use *{{<link url="VLAN-aware-Bridge-Mode" text="VLAN-aware mode">}}* bridges,
rather than *traditional mode* bridges. The bridge driver in Cumulus Linux is
capable of VLAN filtering, which allows for configurations that are similar to
incumbent network devices. While Cumulus Linux supports Ethernet bridges in
traditional mode, it's best to use VLAN-aware mode.

{{%/notice%}}

{{%notice info%}}

For a comparison of traditional and VLAN-aware modes, read this [knowledge base article]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}}).

{{%/notice%}}

{{%notice note%}}

Cumulus Linux does not put all ports into a bridge by default.

{{%/notice%}}

{{%notice tip%}}

You can configure both VLAN-aware and traditional mode bridges on the
same network in Cumulus Linux; however you cannot have more than one
VLAN-aware bridge on a given switch.

{{%/notice%}}

## Create a VLAN-aware Bridge

To learn about VLAN-aware bridges and how to configure them, read {{<link url="VLAN-aware-Bridge-Mode">}}.

## Create a Traditional Mode Bridge

To create a traditional mode bridge, see {{<link url="Traditional-Bridge-Mode">}}.

## Configure Bridge MAC Addresses

The MAC address for a frame is learned when the frame enters the bridge
via an interface. The MAC address is recorded in the bridge table, and
the bridge forwards the frame to its intended destination by looking up
the destination MAC address. The MAC entry is then maintained for a
period of time defined by the `bridge-ageing` configuration option. If
the frame is seen with the same source MAC address before the MAC entry
age is exceeded, the MAC entry age is refreshed; if the MAC entry age is
exceeded, the MAC address is deleted from the bridge table.

The following example output shows a MAC address table for the bridge:

```
cumulus@switch:~$ net show bridge macs
VLAN      Master    Interface    MAC                  TunnelDest  State      Flags    LastSeen
--------  --------  -----------  -----------------  ------------  ---------  -------  -----------------
untagged  bridge    swp1         44:38:39:00:00:03                                    00:00:15
untagged  bridge    swp1         44:38:39:00:00:04                permanent           20 days, 01:14:03
```

## MAC Address Ageing

By default, Cumulus Linux stores MAC addresses in the Ethernet switching
table for 1800 seconds (30 minutes). You can change this setting using NCLU.

You can change the setting using NCLU. For example, to change the setting to 600 seconds, run:

```
cumulus@switch:~$ net add bridge bridge ageing 600
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@switch:~$ cat /etc/network/interfaces

...
     
auto bridge
iface bridge
    bridge-ageing 600
...
```

## Configure an SVI (Switch VLAN Interface)

Bridges can be included as part of a routing topology after being
assigned an IP address. This enables hosts within the bridge to
communicate with other hosts outside of the bridge, via a *switch VLAN
interface* (SVI), which provides layer 3 routing. The IP address of the
bridge is typically from the same subnet as the bridge's member hosts.

{{%notice note%}}

When an interface is added to a bridge, it ceases to function as a
router interface, and the IP address on the interface, if any, becomes
unreachable.

{{%/notice%}}

To configure the SVI, use {{<link url="Network-Command-Line-Utility-NCLU" text="NCLU">}}:

```
cumulus@switch:~$ net add bridge bridge ports swp1-2
cumulus@switch:~$ net add vlan 10 ip address 10.100.100.1/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following SVI configuration in the `/etc/network/interfaces` file:

```
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-vids 10
    bridge-vlan-aware yes

auto vlan10
iface vlan10
    address 10.100.100.1/24
    vlan-id 10
    vlan-raw-device bridge
```

{{%notice tip%}}

Notice the `vlan-raw-device` keyword, which NCLU includes automatically.
NCLU uses this keyword to associate the SVI with the VLAN-aware bridge.

{{%/notice%}}

Alternately, you can use the *bridge.VLAN-ID* naming convention for the
SVI. The following example configuration can be manually created in the
`/etc/network/interfaces` file, which functions identically to the above
configuration:

```
auto bridge
iface bridge
    bridge-ports swp1 swp2
    bridge-vids 10
    bridge-vlan-aware yes
     
auto bridge.10
iface bridge.10
    address 10.100.100.1/24
```

When a switch is initially configured, all southbound bridge ports may
be down, which means that, by default, the SVI is also down. However,
you may want to force the SVI to always be up, to perform connectivity
testing, for example. To do this, you essentially need to disable
interface state tracking, leaving the SVI in the UP state always, even
if all member ports are down. Other implementations describe this
feature as *no autostate*.

In Cumulus Linux, you can keep the SVI perpetually UP by creating a
dummy interface, and making the dummy interface a member of the bridge.
Consider the following configuration, without a dummy interface in the
bridge:

```
cumulus@switch:~$ cat /etc/network/interfaces
...
auto bridge
iface bridge
    bridge-vlan-aware yes
    bridge-ports swp3
    bridge-vids 100
    bridge-pvid 1
...
```

With this configuration, when swp3 is down, the SVI is also down:

```
cumulus@switch:~$ ip link show swp3
5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT group default qlen 1000
    link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show bridge
35: bridge: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
    link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
```

Now add the dummy interface to your network configuration:

1.  Create a dummy interface, and add it to the bridge configuration.
    You do this by editing the `/etc/network/interfaces` file and adding
    the dummy interface stanza before the bridge stanza:
```
    cumulus@switch:~$ sudo nano /etc/network/interfaces
    ...
         
    auto dummy
    iface dummy
        link-type dummy
         
    auto bridge
    iface bridge
    ...
```

2.  Continue editing the `interfaces` file. Add the dummy interface to
    the `bridge-ports` line in the bridge configuration:
```
    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports swp3 dummy
        bridge-vids 100
        bridge-pvid 1
```

3.  Save and exit the file, then reload the configuration:
```
    cumulus@switch:~$ sudo ifreload -a
```

Now, even when swp3 is down, both the dummy interface and the bridge remain up:

```
cumulus@switch:~$ ip link show swp3
5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT group default qlen 1000
    link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show dummy
37: dummy: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default
    link/ether 66:dc:92:d4:f3:68 brd ff:ff:ff:ff:ff:ff
cumulus@switch:~$ ip link show bridge
35: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
    link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
```

## IPv6 Link-local Address Generation

By default, Cumulus Linux automatically generates IPv6
{{<exlink url="https://en.wikipedia.org/wiki/Link-local_address" text="link-local addresses">}} on VLAN
interfaces. If you want to use a different mechanism to assign
link-local addresses, you should disable this feature. You can disable
link-local automatic address generation for both regular IPv6 addresses
and address-virtual (macvlan) addresses.

To disable automatic address generation for a regular IPv6 address on VLAN 100, run:

```
cumulus@switch:~$ net add vlan 100 ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@switch:~$ cat /etc/network/interfaces
...
auto vlan100
iface vlan 100
    ipv6-addrgen off
    vlan-id 100
    vlan-raw-device bridge
...
```

To disable automatic address generation for a virtual IPv6 address on VLAN 100, run:

```
cumulus@switch:~$ net add vlan 100 address-virtual-ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

These commands create the following configuration in the `/etc/network/interfaces` file:

```
cumulus@switch:~$ cat /etc/network/interfaces
...

auto vlan100
iface vlan 100
    address-virtual-ipv6-addrgen off
    vlan-id 100
    vlan-raw-device bridge

...
```

To reenable automatic link-local address generation, run:

```
cumulus@switch:~$ net del vlan 100 ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

or

```
cumulus@switch:~$ net del vlan 100 address-virtual-ipv6-addrgen off
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

This removes the relevant configuration from the `interfaces` file.

## Understanding bridge fdb Output

The `bridge fdb` command in Linux interacts with the forwarding database
table, which the bridge uses to store MAC addresses it has learned and
on which ports it learned those MAC addresses. The `bridge fdb show`
command output contains some specific keywords that require further
explanation:

- **self**: the Linux kernel FDB entry flag indicating the FDB entry belongs to the FDB on the device referenced by the device. For example, this FDB entry belongs to the VXLAN device vx-1000: `"00:02:00:00:00:08 dev vx-1000 dst 27.0.0.10 self"`
- **master**: the Linux kernel FDB entry flag indicating the FDB entry belongs to the FDB on the device's master, and the FDB entry is pointing to a master's port. For example, this FDB entry is from the master device named *bridge* and is pointing to the VXLAN bridge port vx-1001: `02:02:00:00:00:08 dev vx-1001 vlan 1001 master bridge`
- **offload**: the Linux kernel FDB entry flag indicating the FDB entry is managed (or offloaded) by an external control plane - for example, the BGP control plane for EVPN.

Consider the following output of the `bridge fdb show` command:

```
cumulus@switch:~$ bridge fdb show | grep 02:02:00:00:00:08
02:02:00:00:00:08 dev vx-1001 vlan 1001 offload master bridge
02:02:00:00:00:08 dev vx-1001 dst 27.0.0.10 self offload
```

Some things you should note about the output:

- *02:02:00:00:00:08* is the MAC address learned via BGP EVPN.
- The first FDB entry points to a Linux bridge entry pointing to the VXLAN device *vx-1001*.
- The second FDB entry points to the same entry on the VXLAN device with additional remote destination information.
- The VXLAN FDB augments the bridge FDB with additional remote destination information.
- All FDB entries pointing to a VXLAN port appear as two such entries with the second entry augmenting the remote destination information.

## Caveats and Errata

- A bridge cannot contain multiple subinterfaces of the **same** port. Attempting this configuration results in an error.
- In environments where both VLAN-aware and traditional bridges are in use, if a traditional bridge has a subinterface of a bond that is a normal interface in a VLAN-aware bridge, the bridge is flapped when the traditional bridge's bond subinterface is brought down.
- You cannot enslave a VLAN raw device to a different master interface (that is, you cannot edit the `vlan-raw-device` setting in the `/etc/network/interfaces` file). You need to delete the VLAN and create it again.
- Cumulus Linux supports up to 2000 VLANs. This includes the internal interfaces, bridge interfaces, logical interfaces, and so on.
- In Cumulus Linux, MAC learning is enabled by default on traditional or VLAN-aware bridge interfaces. Do not disable MAC learning unless you are using EVPN. See {{<link url="Ethernet-Virtual-Private-Network-EVPN">}}.

## Related Information

- {{<exlink url="http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan" text="Linux Foundation - VLANs">}}
- {{<exlink url="http://www.linuxjournal.com/article/8172" text="Linux Journal - Linux as an Ethernet Bridge">}}
- [Comparing Traditional Bridge Mode to VLAN-aware Bridge Mode]({{<ref "/knowledge-base/Configuration-and-Usage/Network-Interfaces/Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" >}})
