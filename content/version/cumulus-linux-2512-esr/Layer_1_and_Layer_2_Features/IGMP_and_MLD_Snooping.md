---
title: IGMP and MLD Snooping
author: Cumulus Networks
weight: 109
aliases:
 - /display/CL25ESR/IGMP+and+MLD+Snooping
 - /pages/viewpage.action?pageId=5116087
pageID: 5116087
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
IGMP (Internet Group Management Protocol) and MLD (Multicast Listener
Discovery) snooping functionality is implemented in the bridge driver in
the kernel. IGMP snooping processes IGMP v1/v2/v3 reports received on a
bridge port in a bridge to identify the hosts which would like to
receive multicast traffic destined to that group.

When an IGMPv2 leave message is received, a group specific query is sent
to identify if there are any other hosts interested in that group,
before the group is deleted.

An IGMP query message received on a port is used to identify the port
that is connected to a router and is interested in receiving multicast
traffic.

MLD snooping processes MLD v1/v2 reports, queries and v1 done messages
for IPv6 groups. If IGMP or MLD snooping is disabled, multicast traffic
will be flooded to all the bridge ports in the bridge. The multicast
group IP address is mapped to a multicast MAC address and a forwarding
entry is created with a list of ports interested in receiving multicast
traffic destined to that group.

{{% imgOld 0 %}}

## <span>Commands</span>

  - brctl

  - bridge

## <span>Creating a Bridge and Configuring IGMP/MLD Snooping</span>

You need to set a number of parameters for IGMP and MLD snooping, but
the setting to enable it is `bridge-mcsnoop 1`. The following
configuration in `/etc/network/interfaces` is for the example bridge
above. For an explanation of the relevant parameters, see the
`ifupdown-addons-interfaces` man page. In terms of IGMP/MLD snooping,
make sure `bridge-mcsnoop` is true (it's enabled by default) and set the
IP address for the querier in an SVI under the bridge.

    auto br0
    iface br0
      bridge-vlan-aware yes
      bridge-ports swp1 swp2 swp3
      bridge-vids 100 200
      bridge-pvid 1
      bridge-stp on
      bridge-mclmc 2
      bridge-mcrouter 1
      bridge-mcsnoop  1
      bridge-mcsqc    2
      bridge-mcqifaddr 0
      bridge-mcquerier 0
      bridge-hashel 4096
      bridge-hashmax 4096
      bridge-mclmi 1
      bridge-mcmi 260
      bridge-mcqpi 255
      bridge-mcqi  125
      bridge-mcqri 10
      bridge-mcsqi 31
    
    # configure the source IP for the IGMP querier
    auto bridge br0.100
    iface br0.100
      bridge-mcsnoop 1
      bridge-igmp-querier-source 123.1.1.1
      
    auto swp1
    iface swp1
      bridge-vids 100
      bridge-portmcrouter 1
      bridge-portmcfl 0
    
    auto swp2
    iface swp2
      bridge-vids 200
      bridge-portmcrouter 1
      bridge-portmcfl 0
    
    auto swp3
    iface swp3
      bridge-access 100

Runtime Configuration (Advanced)

{{%notice warning%}}

A runtime configuration is non-persistent, which means the configuration
you create here does not persist after you reboot the switch.

{{%/notice%}}

To enable snooping at runtime, use the `brctl` command. Create a bridge
and add bridge ports to the bridge. IGMP and MLD snooping are enabled by
default on the bridge:

    cumulus@switch:~$ sudo brctl addbr br0
    cumulus@switch:~$ sudo brctl addif br0 swp1 swp2 swp3
    cumulus@switch:~$ sudo ifconfig br0 up

To get the IGMP/MLD snooping bridge state, use:

    cumulus@switch:~$ sudo brctl showstp br0
     br0
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

To get the groups and bridge port state, use `bridge mdb show` command.
To display router ports and group information use `bridge -d mdb show`
command:

    cumulus@switch:~$ sudo bridge -d mdb show
     dev br0 port swp2 grp 234.10.10.10 temp
     dev br0 port swp1 grp 238.39.20.86 permanent
     dev br0 port swp1 grp 234.1.1.1 temp
     dev br0 port swp2 grp ff1a::9 permanent
     router ports on br0: swp3
    
    cumulus@switch:~$ sudo bridge mdb show
     dev br0 port swp2 grp 234.10.10.10 temp
     dev br0 port swp1 grp 238.39.20.86 permanent
     dev br0 port swp1 grp 234.1.1.1 temp
     dev br0 port swp2 grp ff1a::9 permanent

<span id="src-5116087_IGMPandMLDSnooping-igmp_disable"></span>To disable
IGMP and MLD snooping, use:

    cumulus@switch:~$ sudo brctl setmcsnoop br0 0

## <span>Configuring IGMP/MLD Snooping Parameters</span>

For an explanation of these parameters, see the `brctl` and
`ifupdown-addons-interfaces` man pages:

    cumulus@switch:~$ sudo brctl setmclmc br0 2
    cumulus@switch:~$ sudo brctl setmcrouter br0 1
    cumulus@switch:~$ sudo brctl setmcsqc br0 2
    cumulus@switch:~$ sudo brctl sethashel br0 4096
    cumulus@switch:~$ sudo brctl sethashmax br0 4096
    cumulus@switch:~$ sudo brctl setmclmi br0 1
    cumulus@switch:~$ sudo brctl setmcmi br0 260
    cumulus@switch:~$ sudo brctl setmcqpi br0 255
    cumulus@switch:~$ sudo brctl setmcqi br0 125
    cumulus@switch:~$ sudo brctl setmcqri br0 10
    cumulus@switch:~$ sudo brctl setmsqi br0 31

## <span>Querier and Fast Leave Configuration</span>

If there is no multicast router in the VLAN, the IGMP/MLD snooping
querier can be configured to generate query messages.

To send queries with a non-zero IP address, configure an IP address on
the bridge device, then set `setmcqifaddr` to 1:

    cumulus@switch:~$ sudo brctl setmcquerier br0 1
    cumulus@switch:~$ sudo brctl setmcqifaddr br0 1

If only one host is attached to each host port, fast leave can be
configured on that port. When a leave message is received on that port,
no query messages will be sent and the group will be deleted
immediately:

    cumulus@switch:~$ sudo brctl setportmcfl br0 swp1 1

## <span>Static Group and Router Port Configuration</span>

To configure static permanent multicast group on a port, use:

    cumulus@switch:~$ sudo bridge mdb add dev br0 port swp2 grp ff1a::9 permanent
    cumulus@switch:~$ sudo bridge mdb add dev br0 port swp1 grp 238.39.20.86 permanent

A static temporary multicast group can also be configured on a port,
which would be deleted after the membership timer expires, if no report
is received on that port:

    cumulus@switch:~$ sudo bridge mdb add dev br0 port swp1 grp 238.39.20.86 temp

To configure a static router port, use:

    cumulus@switch:~$ sudo brctl setportmcrouter br0 swp3 2

## <span>Configuration Files</span>

  - /etc/network/interfaces

## <span>Man Pages</span>

  - brctl(8)

  - bridge(8)

  - ifupdown-addons-interfaces(5)

## <span>Useful Links</span>

  - <http://www.linuxfoundation.org/collaborate/workgroups/networking/bridge#Snooping>

  - <https://tools.ietf.org/html/rfc4541>

  - <http://en.wikipedia.org/wiki/IGMP_snooping>

  - <http://tools.ietf.org/rfc/rfc2236.txt>

  - <http://tools.ietf.org/html/rfc3376>

  - <http://tools.ietf.org/search/rfc2710>

  - <http://tools.ietf.org/html/rfc3810>
