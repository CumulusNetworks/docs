---
title: IGMP and MLD Snooping
author: Cumulus Networks
weight: 127
aliases:
 - /display/CL34/IGMP+and+MLD+Snooping
 - /pages/viewpage.action?pageId=7112448
pageID: 7112448
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
IGMP (Internet Group Management Protocol) and MLD (Multicast Listener
Discovery) snooping are implemented in the bridge driver in the Cumulus
Linux kernel and are enabled by default. IGMP snooping processes IGMP
v1/v2/v3 reports received on a bridge port in a bridge to identify the
hosts which would like to receive multicast traffic destined to that
group.

When an IGMPv2 leave message is received, a group specific query is sent
to identify if there are any other hosts interested in that group,
before the group is deleted.

An IGMP query message received on a port is used to identify the port
that is connected to a router and is interested in receiving multicast
traffic.

MLD snooping processes MLD v1/v2 reports, queries and v1 done messages
for IPv6 groups. If IGMP or MLD snooping is disabled, multicast traffic
gets flooded to all the bridge ports in the bridge. Similarly, in the
absence of receivers in a VLAN, multicast traffic would be flooded to
all ports in the VLAN. The multicast group IP address is mapped to a
multicast MAC address and a forwarding entry is created with a list of
ports interested in receiving multicast traffic destined to that group.

{{% imgOld 0 %}}

## <span>Configuring IGMP/MLD Querier</span>

If no multicast router is sending queries to configure IGMP/MLD querier
on the switch, you can add a configuration similar to the following in
`/etc/network/interfaces`. To enable IGMP and MLD snooping for a bridge,
set `bridge-mcquerier` to *1* in the bridge stanza. By default, the
source IP address of IGMP queries is 0.0.0.0. To set the source IP
address of the queries to be the bridge IP address, configure
`bridge-mcqifaddr 1`.

For an explanation of the relevant parameters, see the
`ifupdown-addons-interfaces` man page.

For a [VLAN-aware
bridge](/version/cumulus-linux-343/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/VLAN-aware_Bridge_Mode_for_Large-scale_Layer_2_Environments),
use a configuration like the following:

    auto br0.100
    vlan br0.100
      bridge-igmp-querier-src 123.1.1.1
     
    auto br0
    iface br0
      bridge-ports swp1 swp2 swp3
      bridge-vlan-aware yes
      bridge-vids 100 200
      bridge-pvid 1
      bridge-mcquerier 1

For a VLAN-aware bridge, like br0 in the above example, to enable
querier functionality for VLAN 100 in the bridge, set `bridge-mcquerier`
to *1* in the bridge stanza and set `bridge-igmp-querier-src` to
*123.1.1.1* in the br0.100 stanza.

You can specify a range of VLANs as well. For example:

    auto bridge.[1-200]
    vlan bridge.[1-200]
      bridge-igmp-querier-src 123.1.1.1

For a bridge in [traditional
mode](/version/cumulus-linux-343/Layer_One_and_Two/Ethernet_Bridging_-_VLANs/),
use a configuration like the following:

    auto br0
    iface br0
      address 192.0.2.10/24
      bridge-ports swp1 swp2 swp3
      bridge-vlan-aware no
      bridge-mcquerier 1
      bridge-mcqifaddr 1

## <span>Disable IGMP and MLD Snooping</span>

<span id="src-7112448_IGMPandMLDSnooping-igmp_disable"></span>To disable
IGMP and MLD snooping, set the `bridge-mcsnoop` value to *0*.

{{%notice info%}}

**Example Disable IGMP MLD Snooping Configuration**

The example NCLU commands below create a VLAN-aware bridge interface for
a VRR-enabled network:

    cumulus@switch:~$ net add bridge bridge mcsnoop no
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The commands above add the `bridge-mcsnoop` line to the following
example bridge in `/etc/network/interfaces`:

    auto bridge
    iface bridge
      bridge-mcquerier 1
      bridge-mcsnoop 0
      bridge-ports swp1 swp2 swp3
      bridge-pvid 1
      bridge-vids 100 200
      bridge-vlan-aware yes

{{%/notice%}}

## <span>Debugging IGMP/MLD Snooping</span>

To get the IGMP/MLD snooping bridge state, run `brctl showstp <bridge>`:

    cumulus@switch:~$ sudo brctl showstp bridge
     bridge
     bridge id              8000.7072cf8c272c
     designated root        8000.7072cf8c272c
     root port                 0                    path cost                  0
     max age                  20.00                 bridge max age            20.00
     hello time                2.00                 bridge hello time          2.00
     forward delay            15.00                 bridge forward delay      15.00
     ageing time             300.00
     hello timer               0.00                 tcn timer                  0.00
     topology change timer     0.00                 gc timer                 263.70
     hash elasticity        4096                    hash max                4096
     mc last member count      2                    mc init query count        2
     mc router                 1                    mc snooping                1
     mc last member timer      1.00                 mc membership timer      260.00
     mc querier timer        255.00                 mc query interval        125.00
     mc response interval     10.00                 mc init query interval    31.25
     mc querier                0                    mc query ifaddr            0
     flags
     
    swp1 (1)
     port id                8001                    state                forwarding
     designated root        8000.7072cf8c272c       path cost                  2
     designated bridge      8000.7072cf8c272c       message age timer          0.00
     designated port        8001                    forward delay timer        0.00
     designated cost           0                    hold timer                 0.00
     mc router                 1                    mc fast leave              0
     flags
     
    swp2 (2)
     port id                8002                    state                forwarding
     designated root        8000.7072cf8c272c       path cost                  2
     designated bridge      8000.7072cf8c272c       message age timer          0.00
     designated port        8002                    forward delay timer        0.00
     designated cost           0                    hold timer                 0.00
     mc router                 1                    mc fast leave              0
     flags
     
    swp3 (3)
     port id                8003                    state                forwarding
     designated root        8000.7072cf8c272c       path cost                  2
     designated bridge      8000.7072cf8c272c       message age timer          0.00
     designated port        8003                    forward delay timer        8.98
     designated cost           0                    hold timer                 0.00
     mc router                 1                    mc fast leave              0
     flags

To get the groups and bridge port state, use the `bridge mdb show`
command. To display router ports and group information use the `bridge
-d -s mdb show` command:

    cumulus@switch:~$ sudo bridge -d -s mdb show
     dev bridge port swp2 grp 234.10.10.10 temp 241.67
     dev bridge port swp1 grp 238.39.20.86 permanent 0.00
     dev bridge port swp1 grp 234.1.1.1 temp 235.43
     dev bridge port swp2 grp ff1a::9 permanent 0.00
     router ports on bridge: swp3

## <span>Related Information</span>

  - [www.linuxfoundation.org/collaborate/workgroups/networking/bridge\#Snooping](http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge#Snooping)

  - [tools.ietf.org/html/rfc4541](https://tools.ietf.org/html/rfc4541)

  - [en.wikipedia.org/wiki/IGMP\_snooping](http://en.wikipedia.org/wiki/IGMP_snooping)

  - [tools.ietf.org/rfc/rfc2236.txt](http://tools.ietf.org/rfc/rfc2236.txt)

  - [tools.ietf.org/html/rfc3376](http://tools.ietf.org/html/rfc3376)

  - [tools.ietf.org/search/rfc2710](http://tools.ietf.org/search/rfc2710)

  - [tools.ietf.org/html/rfc3810](http://tools.ietf.org/html/rfc3810)
