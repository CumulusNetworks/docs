---
title: Ethernet Bridging - VLANs
author: Cumulus Networks
weight: 79
aliases:
 - /display/RMP30/Ethernet+Bridging+-+VLANs
 - /pages/viewpage.action?pageId=5118717
pageID: 5118717
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
Ethernet bridges provide a means for hosts to communicate at layer 2.
Bridge members can be individual physical interfaces, bonds or logical
interfaces that traverse an 802.1Q VLAN trunk.

Cumulus RMP has two modes for configuring bridges:
*[VLAN-aware](/version/cumulus-rmp-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments)*
and *traditional*. The bridge driver in Cumulus RMP is capable of VLAN
filtering, which allows for configurations that are similar to incumbent
network devices. While Cumulus RMP supports Ethernet bridges in
traditional mode Cumulus Networks **** recommends using
[VLAN-aware](http://docs.cumulusnetworks.com/display/CL25/VLAN-aware+Bridge+Mode+for+Large-scale+Layer+2+Environments)
mode.

For a comparison of traditional and VLAN-aware modes, read [this
knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/204909397).

{{%notice tip%}}

You can configure both VLAN-aware and traditional mode bridges on the
same network in Cumulus RMP; however you should not have more than one
VLAN-aware bridge on a given switch.

{{%/notice%}}

### <span>Configuration Files</span>

  - /etc/network/interfaces

### <span>Commands</span>

  - brctl

  - bridge

  - ip addr

  - ip link

### <span>Creating a Bridge between Physical Interfaces</span>

The basic use of bridging is to connect all of the physical and logical
interfaces in the system into a single layer 2 domain.

{{% imgOld 0 %}}

#### <span>Creating the Bridge and Adding Interfaces</span>

You statically manage bridge configurations in
`/etc/network/interfaces`. The following configuration snippet details
an example bridge used throughout this chapter, explicitly enabling
[spanning
tree](/version/cumulus-rmp-301/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree)
and setting the bridge MAC address ageing timer. First, create a bridge
with a descriptive name of 15 characters or fewer. Then add the logical
interfaces (bond0) and physical interfaces (swp5, swp6) to assign to
that bridge.

    auto my_bridge
    iface my_bridge
        bridge-ports bond0 swp5 swp6
        bridge-ageing 150
        bridge-stp on

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Keyword</p></th>
<th><p>Explanation</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>bridge-ports</p></td>
<td><p>List of logical and physical ports belonging to the logical bridge.</p></td>
</tr>
<tr class="even">
<td><p>bridge-ageing</p></td>
<td><p>Maximum amount of time before a MAC addresses learned on the bridge expires from the bridge MAC cache. The default value is 300 seconds.</p></td>
</tr>
<tr class="odd">
<td><p>bridge-stp</p></td>
<td><p>Enables spanning tree protocol on this bridge. The default spanning tree mode is Per VLAN Rapid Spanning Tree Protocol (PVRST).</p>
<p>For more information on spanning-tree configurations see the configuration section: <a href="/version/cumulus-rmp-301/Layer_1_and_Layer_2_Features/Spanning_Tree_and_Rapid_Spanning_Tree">Spanning Tree and Rapid Spanning Tree</a>.</p></td>
</tr>
</tbody>
</table>

To bring up the bridge my\_bridge, use the `ifreload` command:

    cumulus@switch:~$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

To create the bridge and interfaces on the bridge, run:

    cumulus@switch:~$ sudo brctl addbr my_bridge
    
    cumulus@switch:~$ sudo brctl addif my_bridge bond0 swp5 swp6
    
    cumulus@switch:~$ sudo brctl show
    bridge name        bridge id          STP enabled     interfaces
    my_bridge          8000.44383900129b  yes             bond0
                                                          swp5
                                                          swp6

    cumulus@switch:~$ sudo ip link set up dev my_bridge

    cumulus@switch:~$ sudo ip link set up dev bond0

    cumulus@switch:~$ sudo for I in {5..6}; do  ip link set up dev swp$I; done

#### <span>Showing and Verifying the Bridge Configuration</span>

    cumulus@switch:~$ ip link show my_bridge
    56: my_bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
     link/ether 44:38:39:00:12:9b brd ff:ff:ff:ff:ff:ff

{{%notice warning%}}

Do not try to bridge the management port, eth0, with any switch ports
(like swp0, swp1, and so forth). For example, if you created a bridge
with eth0 and swp1, it will **not** work.

{{%/notice%}}

Using netshow to Display Bridge Information

`netshow` is a Cumulus RMP tool for retrieving information about your
network configuration.

    cumulus@switch$ netshow interface bridge
        Name       Speed    Mtu    Mode       Summary
    --  ---------  -------  -----  ---------  -----------------------
    UP  my_bridge  N/A      1500   Bridge/L2  Untagged: bond0, swp5-6
                                              Root Port: bond0
                                              VlanID: Untagged

#### <span>Bridge Interface MAC Address and MTU</span>

A bridge is a logical interface with a MAC address and an MTU (maximum
transmission unit). The bridge MTU is the minimum MTU among all its
members. The bridge's MAC address is inherited from the first interface
that is added to the bridge as a member. The bridge MAC address remains
unchanged until the member interface is removed from the bridge, at
which point the bridge will inherit from the next member interface, if
any. The bridge can also be assigned an IP address, as discussed below.

### <span>Examining MAC Addresses</span>

A bridge forwards frames by looking up the destination MAC address. A
bridge learns the source MAC address of a frame when the frame enters
the bridge on an interface. After the MAC address is learned, the bridge
maintains an age for the MAC entry in the bridge table. The age is
refreshed when a frame is seen again with the same source MAC address.
When a MAC is not seen for greater than the MAC ageing time, the MAC
address is deleted from the bridge table.

The following shows the MAC address table of the example bridge. Notice
that the `is local?` column indicates if the MAC address is the
interface's own MAC address (`is local` is *yes*), or if it is learned
on the interface from a packet's source MAC (where `is local` is *no*):

    cumulus@switch:~$ sudo brctl showmacs my_bridge
     port name mac addr              is local?       ageing timer
     swp4      06:90:70:22:a6:2e     no                19.47
     swp1      12:12:36:43:6f:9d     no                40.50
     bond0     2a:95:22:94:d1:f0     no                 1.98
     swp1      44:38:39:00:12:9b     yes                0.00
     swp2      44:38:39:00:12:9c     yes                0.00
     swp3      44:38:39:00:12:9d     yes                0.00
     swp4      44:38:39:00:12:9e     yes                0.00
     bond0     44:38:39:00:12:9f     yes                0.00
     swp2      90:e2:ba:2c:b1:94     no                12.84
     swp2      a2:84:fe:fc:bf:cd     no                 9.43

You can use the `bridge fdb` command to display the MAC address table as
well:

    cumulus@switch$ bridge fdb show
    70:72:cf:9d:4e:36 dev swp2 VLAN 0 master bridge-A permanent
    70:72:cf:9d:4e:35 dev swp1 VLAN 0 master bridge-A permanent
    70:72:cf:9d:4e:38 dev swp4 VLAN 0 master bridge-B permanent
    70:72:cf:9d:4e:37 dev swp3 VLAN 0 master bridge-B permanent

{{%notice note%}}

You can clear a MAC address from the table using the `bridge fdb`
command:

    cumulus@switch:~$ sudo bridge fdb del 90:e2:ba:2c:b1:94 dev swp2

{{%/notice%}}

### <span>Multiple Bridges</span>

Sometimes it is useful to logically divide a switch into multiple layer
2 domains, so that hosts in one domain can communicate with other hosts
in the same domain but not in other domains. You can achieve this by
configuring multiple bridges and putting different sets of interfaces in
the different bridges. In the following example, host-1 and host-2 are
connected to the same bridge (bridge-A), while host-3 and host-4 are
connected to another bridge (bridge-B). host-1 and host-2 can
communicate with each other, so can host-3 and host-4, but host-1 and
host-2 cannot communicate with host-3 and host-4.

{{% imgOld 1 %}}

To configure multiple bridges, edit `/etc/network/interfaces`:

    auto bridge-A
    iface bridge-A
        bridge-ports swp1 swp2
        bridge-stp on
    
    auto my_bridge
    iface my_bridge
        bridge-ports swp3 swp4
        bridge-stp on

To bring up the bridges bridge-A and bridge-B, use the `ifreload`
command:

    cumulus@switch:~$ sudo ifreload -a

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

    cumulus@switch:~$ sudo brctl addbr bridge-A
    
    cumulus@switch:~$ sudo brctl addif bridge-A swp1 swp2
    
    cumulus@switch:~$ sudo brctl addbr bridge-B
    
    cumulus@switch:~$ sudo brctl addif bridge-B swp3 swp4
    
    cumulus@switch:~$ sudo for I in {1..4}; do  ip link set up dev swp$I; done
    
    cumulus@switch:~$ sudo ip link set up dev bridge-A
    
    cumulus@switch:~$ sudo ip link set up dev bridge-B
    
    cumulus@switch:~$ sudo brctl show
     bridge name     bridge id               STP enabled     interfaces
     bridge-A        8000.44383900129b       yes             swp1
                                                             swp2
     bridge-B        8000.44383900129d       yes             swp3
                                                             swp4
            
    cumulus@switch$ ip link show bridge-A
    97: bridge-A: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
     link/ether 70:72:cf:9d:4e:35 brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ ip link show bridge-B
    98: bridge-B: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
     link/ether 70:72:cf:9d:4e:37 brd ff:ff:ff:ff:ff:ff

Using netshow to Display the Bridges

`netshow` is a Cumulus RMP tool for retrieving information about your
network configuration.

    cumulus@switch$ netshow interface bridge
        Name      Speed    Mtu    Mode       Summary
    --  --------  -------  -----  ---------  ----------------
    UP  bridge-A  N/A      1500   Bridge/L2  Untagged: swp1-2
                                             Root Port: swp2
                                             VlanID: Untagged
    UP  bridge-B  N/A      1500   Bridge/L2  Untagged: swp3-4
                                             Root Port: swp3
                                             VlanID: Untagged

### <span>Configuring an SVI (Switch VLAN Interface)</span>

A bridge creates a layer 2 forwarding domain for hosts to communicate. A
bridge can be assigned an IP address — typically of the same subnet as
the hosts that are members of the bridge — and participate in routing
topologies. This enables hosts within a bridge to communicate with other
hosts outside the bridge through layer 3 routing.

{{%notice note%}}

When an interface is added to a bridge, it ceases to function as a
router interface, and the IP address on the interface, if any, becomes
reachable.

{{%/notice%}}

{{% imgOld 2 %}}

The configuration for the two bridges example looks like the following:

    auto swp5
    iface swp5
     address 192.168.1.2/24
     address 2001:DB8:1::2/64
    auto bridge-A
    iface bridge-A
     address 192.168.2.1/24
     address 2001:DB8:2::1/64
     bridge-ports swp1 swp2
     bridge-stp on
    auto bridge-B
    iface bridge-B
     address 192.168.3.1/24
     address 2001:DB8:3::1/64
     bridge-ports swp3 swp4
     bridge-stp on

To bring up swp5 and bridges bridge-A and bridge-B, use the `ifreload`
command:

    cumulus@switch:~$ sudo ifreload -a

#### <span>Showing and Verifying the Bridge Configuration</span>

    cumulus@switch$ ip addr show bridge-A
    106: bridge-A: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
     link/ether 70:72:cf:9d:4e:35 brd ff:ff:ff:ff:ff:ff
     inet 192.168.2.1/24 scope global bridge-A
     inet6 2001:db8:2::1/64 scope global
     valid_lft forever preferred_lft forever
     inet6 fe80::7272:cfff:fe9d:4e35/64 scope link
     valid_lft forever preferred_lft forever

    cumulus@switch$ ip addr show bridge-B
    107: bridge-B: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
     link/ether 70:72:cf:9d:4e:37 brd ff:ff:ff:ff:ff:ff
     inet 192.168.3.1/24 scope global bridge-B
     inet6 2001:db8:3::1/64 scope global
     valid_lft forever preferred_lft forever
     inet6 fe80::7272:cfff:fe9d:4e37/64 scope link
     valid_lft forever preferred_lft forever

To see all the routes on the switch use the `ip route show` command:

    cumulus@switch$ ip route show
    192.168.1.0/24 dev swp5 proto kernel scope link src 192.168.1.2 dead
    192.168.2.0/24 dev bridge-A proto kernel scope link src 192.168.2.1
    192.168.3.0/24 dev bridge-B proto kernel scope link src 192.168.3.1

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

To add an IP address to a bridge:

    cumulus@switch:~$ sudo ip addr add 192.0.2.101/24 dev bridge-A
    
    cumulus@switch:~$ sudo ip addr add 192.0.2.102/24 dev bridge-B

Using netshow to Display the SVI

`netshow` is a Cumulus RMP tool for retrieving information about your
network configuration.

    cumulus@switch$ netshow interface bridge
        Name      Speed    Mtu    Mode       Summary
    --  --------  -------  -----  ---------  ------------------------------------
    UP  bridge-A  N/A      1500   Bridge/L3  IP: 192.168.2.1/24, 2001:db8:2::1/64
                                             Untagged: swp1-2
                                             Root Port: swp2
                                             VlanID: Untagged
    UP  bridge-B  N/A      1500   Bridge/L3  IP: 192.168.3.1/24, 2001:db8:3::1/64
                                             Untagged: swp3-4
                                             Root Port: swp3
                                             VlanID: Untagged

### <span>Using Trunks in Traditional Bridging Mode</span>

The [IEEE standard](http://www.ieee802.org/1/pages/802.1Q.html) for
trunking is 802.1Q. The 802.1Q specification adds a 4 byte header within
the Ethernet frame that identifies the VLAN of which the frame is a
member.

802.1Q also identifies an *untagged* frame as belonging to the *native*
VLAN (most network devices default their native VLAN to 1). The concept
of native, non-native, tagged or untagged has generated confusion due to
mixed terminology and vendor-specific implementations. Some
clarification is in order:

  - A *trunk port* is a switch port configured to send and receive
    802.1Q tagged frames.

  - A switch sending an untagged (bare Ethernet) frame on a trunk port
    is sending from the native VLAN defined on the trunk port.

  - A switch sending a tagged frame on a trunk port is sending to the
    VLAN identified by the 802.1Q tag.

  - A switch receiving an untagged (bare Ethernet) frame on a trunk port
    places that frame in the native VLAN defined on the trunk port.

  - A switch receiving a tagged frame on a trunk port places that frame
    in the VLAN identified by the 802.1Q tag.

A bridge in traditional mode has no concept of trunks, just tagged or
untagged frames. With a trunk of 200 VLANs, there would need to be 199
bridges, each containing a tagged physical interface, and one bridge
containing the native untagged VLAN. See the examples below for more
information.

<span id="src-5118717_EthernetBridging-VLANs-VLAN_tagging"></span>

{{%notice note%}}

The interaction of tagged and un-tagged frames on the same trunk often
leads to undesired and unexpected behavior. A switch that uses VLAN 1
for the native VLAN may send frames to a switch that uses VLAN 2 for the
native VLAN, thus merging those two VLANs and their spanning tree state.

{{%/notice%}}

#### <span>Trunk Example</span>

{{% imgOld 3 %}}

Configure the following in `/etc/network/interfaces`:

    auto br-VLAN100
    iface br-VLAN100
     bridge-ports swp1.100 swp2.100
     bridge-stp on
    auto br-VLAN200
    iface br-VLAN200
     bridge-ports swp1.200 swp2.200
     bridge-stp on

To bring up br-VLAN100 and br-VLAN200, use the `ifreload` command:

    cumulus@switch:~$ sudo ifreload -a

#### <span>Showing and Verifying the Trunk</span>

    cumulus@en-sw2$ brctl show
    bridge name bridge id STP enabled interfaces
    br-VLAN100 8000.7072cf9d4e35 no swp1.100
     swp2.100
    br-VLAN200 8000.7072cf9d4e35 no swp1.200
     swp2.200

Using netshow to Display the Trunk

`netshow` is a Cumulus RMP tool for retrieving information about your
network configuration.

    cumulus@switch$ netshow interface bridge
        Name        Speed    Mtu    Mode       Summary
    --  ----------  -------  -----  ---------  ----------------------
    UP  br-VLAN100  N/A      1500   Bridge/L2  Tagged: swp1-2
                                               STP: rootSwitch(32768)
                                               VlanID: 100
    UP  br-VLAN200  N/A      1500   Bridge/L2  Tagged: swp1-2
                                               STP: rootSwitch(32768)
                                               VlanID: 200

#### <span>Additional Examples</span>

You can find additional examples of VLAN tagging in [this
chapter](/version/cumulus-rmp-301/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN_Tagging).

### <span>Configuration Files</span>

  - /etc/network/interfaces

  - /etc/network/interfaces.d/

  - /etc/network/if-down.d/

  - /etc/network/if-post-down.d/

  - /etc/network/if-pre-up.d/

  - /etc/network/if-up.d/

### <span>Useful Links</span>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan>

  - <http://www.linuxjournal.com/article/8172>

### <span>Caveats and Errata</span>

  - The same bridge cannot contain multiple subinterfaces of the
    **same** port as members. Attempting to apply such a configuration
    will result in an error.
