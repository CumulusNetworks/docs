---
title: Ethernet Bridging - VLANs
author: Cumulus Networks
weight: 79
aliases:
 - /display/RMP321/Ethernet+Bridging+-+VLANs
 - /pages/viewpage.action?pageId=5127597
pageID: 5127597
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
Ethernet bridges provide a means for hosts to communicate through layer
2, by connecting all of the physical and logical interfaces in the
system into a single layer 2 domain. The bridge is a logical interface
with a MAC address and an
[MTU](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120636)
(maximum transmission unit). The bridge MTU is the minimum MTU among all
its members. The bridge's MAC address is inherited from the first
interface that is added to the bridge as a member. The bridge MAC
address remains unchanged until the member interface is removed from the
bridge, at which point the bridge will inherit from the next member
interface, if any. The bridge can also be assigned an IP address, as
discussed [below](#src-5127597_EthernetBridging-VLANs-svi).

{{%notice note%}}

Bridge members can be individual physical interfaces, bonds or logical
interfaces that traverse an 802.1Q VLAN trunk.

{{%/notice%}}

{{% imgOld 0 %}}

{{%notice tip%}}

Cumulus Networks recommends using *[VLAN-aware
mode](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120547)*
bridges, rather than *traditional mode* bridges. The bridge driver in
Cumulus RMP is capable of VLAN filtering, which allows for
configurations that are similar to incumbent network devices. While
Cumulus RMP supports Ethernet bridges in traditional mode, Cumulus
Networks **** recommends using
[VLAN-aware](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120547)
mode.

{{%/notice%}}

{{%notice info%}}

For a comparison of traditional and VLAN-aware modes, read [this
knowledge base
article](https://support.cumulusnetworks.com/hc/en-us/articles/204909397).

{{%/notice%}}

{{%notice note%}}

Cumulus RMP does not put all ports into a bridge by default.

{{%/notice%}}

{{%notice tip%}}

You can configure both VLAN-aware and traditional mode bridges on the
same network in Cumulus RMP; however you should not have more than one
VLAN-aware bridge on a given switch.

{{%/notice%}}

## <span>Creating a VLAN-aware Bridge</span>

To learn about VLAN-aware bridges and how to configure them, read
[VLAN-aware Bridge Mode for Large-scale Layer 2
Environments](/version/cumulus-rmp-321/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments).

## <span>Creating a Traditional Mode Bridge</span>

To create a traditional mode bridge, see [Traditional Mode
Bridges](/version/cumulus-rmp-321/Layer_1_and_Layer_2_Features/Ethernet_Bridging_-_VLANs/Traditional_Mode_Bridges).

## <span>Configuring Bridge MAC Addresses</span>

The MAC address for a frame is learned when the frame enters the bridge
via an interface. The MAC address is recorded in the bridge table, and
the bridge forwards the frame to its intended destination by looking up
the destination MAC address. The MAC entry is then maintained for a
period of time defined by the `bridge-ageing` configuration option. If
the frame is seen with the same source MAC address before the MAC entry
age is exceeded, the MAC entry age is refreshed; if the MAC entry age is
exceeded, the MAC address is deleted from the bridge table.

The following example output shows a MAC address table for the bridge:

    cumulus@switch:~$ net show bridge macs 
    VLAN      Master    Interface    MAC                  TunnelDest  State      Flags    LastSeen
    --------  --------  -----------  -----------------  ------------  ---------  -------  -----------------
    untagged  bridge    swp1         44:38:39:00:00:03                                    00:00:15
    untagged  bridge    swp1         44:38:39:00:00:04                permanent           20 days, 01:14:03

## <span id="src-5127597_EthernetBridging-VLANs-svi" class="confluence-anchor-link"></span><span>Configuring an SVI (Switch VLAN Interface)</span>

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

To configure the SVI, use
[NCLU](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=5120643):

    cumulus@switch:~$ net add bridge bridge ports swp1-2
    cumulus@switch:~$ net add vlan 10 ip address 10.100.100.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following SVI configuration in the
`/etc/network/interfaces` file:

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

Alternately, you can use the *bridge.VLAN-ID* naming convention for the
SVI. The following example configuration can be manually created in the
`/etc/network/interfaces` file, which functions identically to the above
configuration:

    auto bridge
    iface bridge
        bridge-ports swp1 swp2
        bridge-vids 10
        bridge-vlan-aware yes
     
    auto bridge.10
    auto bridge.10
        address 10.100.100.1/24

### <span>Keeping the SVI in an UP State</span>

When a switch is initially configured, all southbound bridge ports may
be down, which means that, by default, the SVI is also down. However,
you may want to force the SVI to always be up, to perform connectivity
testing, for example. To do this, you essentially need to disable
interface state tracking, leaving the SVI in the UP state always, even
if all member ports are down. Other implementations describe this
feature as "no autostate".

In Cumulus RMP, you can keep the SVI perpetually UP by creating a dummy
interface, and making the dummy interface a member of the bridge.
Consider the following configuration, without a dummy interface in the
bridge:

    cumulus@switch:~$ cat /etc/network/interfaces
    ...
     
    auto bridge
    iface bridge
        bridge-vlan-aware yes
        bridge-ports swp3
        bridge-vids 100
        bridge-pvid 1
     
    ...

With this configuration, when swp3 is down, the SVI is also down:

    cumulus@switch:~$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT group default qlen 1000
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show bridge
    35: bridge: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc noqueue state DOWN mode DEFAULT group default
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff

Now add the dummy interface to your network configuration:

1.  Create a dummy interface, and add it to the bridge configuration.
    You do this by editing the `/etc/network/interfaces` file and adding
    the dummy interface stanza before the bridge stanza:
    
        cumulus@switch:~$ sudo nano /etc/network/interfaces
        ...
         
        auto dummy
        iface dummy
            link-type dummy
         
        auto bridge
        iface bridge
        ...

2.  Continue editing the `interfaces` file. Add the dummy interface to
    the `bridge-ports` line in the bridge configuration:
    
        auto bridge
        iface bridge
            bridge-ports swp3 dummy
            bridge-pvid 1
            bridge-vids 100
            bridge-vlan-aware yes

3.  Save and exit the file, then reload the configuration:
    
        cumulus@switch:~$ sudo ifreload -a

Now, even when swp3 is down, both the dummy interface and the bridge
remain up:

    cumulus@switch:~$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast master bridge state DOWN mode DEFAULT group default qlen 1000
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show dummy
    37: dummy: <BROADCAST,NOARP,UP,LOWER_UP> mtu 1500 qdisc noqueue master bridge state UNKNOWN mode DEFAULT group default
        link/ether 66:dc:92:d4:f3:68 brd ff:ff:ff:ff:ff:ff
    cumulus@switch:~$ ip link show bridge
    35: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
        link/ether 2c:60:0c:66:b1:7f brd ff:ff:ff:ff:ff:ff

## <span>Caveats and Errata</span>

  - A bridge cannot contain multiple subinterfaces of the **same** port.
    Attempting this configuration results in an error.

  - In environments where both VLAN-aware and traditional bridges are in
    use, if a traditional bridge has a subinterface of a bond that is a
    normal interface in a VLAN-aware bridge, the bridge will be flapped
    when the traditional bridge's bond subinterface is brought down.

## <span>Related Information</span>

  - [Linux Foundation -
    Bridges](http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge)

  - [Linux Foundation -
    VLANs](http://www.linuxfoundation.org/collaborate/workgroups/networking/vlan)

  - [Linux Journal - Linux as an Ethernet
    Bridge](http://www.linuxjournal.com/article/8172)

  - [Comparing Traditional Bridge Mode to VLAN-aware Bridge
    Mode](https://support.cumulusnetworks.com/hc/en-us/articles/204909397)
