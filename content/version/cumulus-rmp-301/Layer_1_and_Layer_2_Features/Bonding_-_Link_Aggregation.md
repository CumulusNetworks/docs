---
title: Bonding - Link Aggregation
author: Cumulus Networks
weight: 77
aliases:
 - /display/RMP30/Bonding+-+Link+Aggregation
 - /pages/viewpage.action?pageId=5118715
pageID: 5118715
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
Linux bonding provides a method for aggregating multiple network
interfaces (the slaves) into a single logical bonded interface (the
bond). Cumulus RMP bonding supports the IEEE 802.3ad link aggregation
mode. Link aggregation allows one or more links to be aggregated
together to form a *link aggregation group* (LAG), such that a media
access control (MAC) client can treat the link aggregation group as if
it were a single link. The benefits of link aggregation are:

  - Linear scaling of bandwidth as links are added to LAG

  - Load balancing

  - Failover protection

The Cumulus RMP LAG control protocol is LACP version 1.

## <span>Example: Bonding 4 Slaves</span>

{{% imgOld 0 %}}

In this example, front panel port interfaces swp1-swp4 are slaves in
bond0 (swp5 and swp6 are not part of bond0).

The name of the bond is arbitrary as long as it follows Linux interface
naming guidelines, and is unique within the switch. The only bonding
mode supported in Cumulus RMP is 802.3ad. There are several 802.3ad
settings that can be applied to each bond.

All of the following settings except for `bond-slaves` are set to the
recommended defaults and should only be added to a configuration in
`/etc/network/interfaces` if you plan to use a different setting.

  - `bond-slaves`: The list of slaves in bond.

  - `bond-mode`: Is set to *802.3ad* by default and **must not** be
    changed.

  - `bond-miimon`: How often the link state of each slave is inspected
    for link failures. It *100*, the recommended value.

  - `bond-use-carrier`: How to determine link state. It defaults to *1*.

  - `bond-xmit-hash-policy`: Hash method used to select the slave for a
    given packet; it defaults to *layer3+4* and **must not** be changed.

  - `bond-lacp-rate`: Rate to ask link partner to transmit LACP control
    packets. It defaults to *1*.

  - `bond-min-links`: Specifies the minimum number of links that must be
    active before asserting carrier on the bond. It defaults to *1*, but
    a value greater than 1 is useful if higher level services need to
    ensure a minimum of aggregate bandwidth before putting the bond in
    service. Keeping `bond-min-links` set to *1* indicates the bond must
    have at least one active member for bond to assert carrier. If the
    number of active members drops below the `bond-min-links` setting,
    the bond will appear to upper-level protocols as *link-down*. When
    the number of active links returns to greater than or equal to
    `bond-min-links`, the bond will become *link-up*.

  - 
See Useful Links below for more details on settings.

To configure the bond, edit `/etc/network/interfaces` and add a stanza
for bond0:

    auto bond0
    iface bond0
        address 10.0.0.1/30
        bond-slaves swp1 swp2 swp3 swp4

However, if you are intending that the bond become part of a bridge, you
don’t need to specify an IP address. The configuration would look like
this:

    auto bond0
    iface bond0
       bond-slaves glob swp1-4

See `man interfaces` for more information on `/etc/network/interfaces`.

When networking is started on switch, bond0 is created as MASTER and
interfaces swp1-swp4 come up in SLAVE mode, as seen in the `ip link
show` command:

    3: swp1: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    4: swp2: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    5: swp3: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff
    6: swp4: <BROADCAST,MULTICAST,SLAVE,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bond0 state UP mode DEFAULT qlen 500
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff

And

    55: bond0: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT
        link/ether 44:38:39:00:03:c1 brd ff:ff:ff:ff:ff:ff

{{%notice note%}}

All slave interfaces within a bond will have the same MAC address as the
bond. Typically, the first slave added to the bond donates its MAC
address for the bond. The other slaves’ MAC addresses are set to the
bond MAC address. The bond MAC address is used as source MAC address for
all traffic leaving the bond, and provides a single destination MAC
address to address traffic to the bond.

{{%/notice%}}

## <span>Hash Distribution</span>

Egress traffic through a bond is distributed to a slave based on a
packet hash calculation. This distribution provides load balancing over
the slaves. The hash calculation uses packet header data to pick which
slave to transmit the packet. For IP traffic, IP header source and
destination fields are used in the calculation. For IP + TCP/UDP
traffic, source and destination ports are included in the hash
calculation. Traffic for a given conversation flow will always hash to
the same slave. Many flows will be distributed over all the slaves to
load balance the total traffic. In a failover event, the hash
calculation is adjusted to steer traffic over available slaves.

## <span>Configuration Files</span>

  - /etc/network/interfaces

## <span>Useful Links</span>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bonding>

  - [802.3ad](http://www.ieee802.org/3/ad/) ([Accessible
    writeup](http://cs.uccs.edu/%7Escold/doc/linkage%20aggregation.pdf))

  - [Link aggregation from
    Wikipedia](http://en.wikipedia.org/wiki/Link_aggregation)

## <span>Caveats and Errata</span>

  - An interface cannot belong to multiple bonds.

  - Slave ports within a bond should all be set to the same
    speed/duplex, and should match the link partner’s slave ports.

  - A bond cannot enslave VLAN subinterfaces. A bond can have
    subinterfaces, but not the other way around.
