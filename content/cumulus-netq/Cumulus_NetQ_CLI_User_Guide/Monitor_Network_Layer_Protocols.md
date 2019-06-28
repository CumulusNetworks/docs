---
title: Monitor Network Layer Protocols
author: Cumulus Networks
weight: 41
aliases:
 - /display/NETQ/Monitor+Network+Layer+Protocols
 - /pages/viewpage.action?pageId=10456375
pageID: 10456375
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
---
With NetQ, a network administrator can monitor OSI Layer 3 network
protocols running on Linux-based hosts, including IP (Internet
Protocol), BGP (Border Gateway Protocol) and OSPF (Open Shortest Path
First). NetQ provides the ability to:

  - Validate protocol configurations

  - Validate layer 3 communication paths

It helps answer questions such as:

  - Who are the IP neighbors for a switch?

  - How many IPv4 and IPv6 addresses am I using?

  - When did changes occur to my IP configuration?

  - Is BGP working as expected?

  - Is OSPF working as expected?

  - Can device A reach device B using IP addresses?

## <span>Monitor IP Configuration</span>

NetQ enables you to view the current status and the status an earlier
point in time. From this information, you can:

  - determine IP addresses of one or more interfaces

  - determine IP neighbors for one or more devices

  - determine IP routes owned by a device

  - identify changes to the IP configuration

<span style="color: #000000;"> The `netq show ip` command is used to
obtain the address, neighbor, and route information from the devices.
Its syntax is: </span>

    netq <hostname> show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
    netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [json]
    netq <hostname> show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [json]
    netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
    netq <hostname> show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
    netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [json]
     
    netq <hostname> show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
    netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [json]
    netq <hostname> show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
    netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [json]
    netq <hostname> show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
    netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [json]

{{%notice info%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)

  - h: hour(s)

  - m: minute(s)

  - s: second(s)

  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### <span>View IP Address Information</span>

You can view the IPv4 and IPv6 address information for all of your
devices, including the interface and VRF for each device. Additionally,
you can:

  - view the information at an earlier point in time

  - filter against a particular device, interface or VRF assignment

  - obtain a count of all of the addresses

Each of these provides information for troubleshooting potential
configuration and communication issues at the layer 3 level.

**Example: View IPv4 address information for all devices**

    cumulus@switch:~$ netq show ip addresses
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    10.0.0.11/32              leaf01            lo                        default         Thu Feb  7 18:30:53 2019
    10.0.0.12/32              leaf02            lo                        default         Thu Feb  7 18:30:53 2019
    10.0.0.13/32              leaf03            lo                        default         Thu Feb  7 18:30:53 2019
    10.0.0.14/32              leaf04            lo                        default         Thu Feb  7 18:30:53 2019
    10.0.0.21/32              spine01           lo                        default         Thu Feb  7 18:30:53 2019
    10.0.0.22/32              spine02           lo                        default         Thu Feb  7 18:30:53 2019
    10.0.0.254/32             oob-mgmt-server   eth0                      default         Thu Feb  7 18:30:53 2019
    172.16.1.1/24             leaf01            br0                       default         Thu Feb  7 18:30:53 2019
    172.16.1.101/24           server01          eth1                      default         Thu Feb  7 18:30:53 2019
    172.16.2.1/24             leaf02            br0                       default         Thu Feb  7 18:30:53 2019
    172.16.2.101/24           server02          eth2                      default         Thu Feb  7 18:30:53 2019
    172.16.3.1/24             leaf03            br0                       default         Thu Feb  7 18:30:53 2019
    172.16.3.101/24           server03          eth1                      default         Thu Feb  7 18:30:53 2019
    172.16.4.1/24             leaf04            br0                       default         Thu Feb  7 18:30:53 2019
    172.16.4.101/24           server04          eth2                      default         Thu Feb  7 18:30:53 2019
    172.17.0.1/16             oob-mgmt-server   docker0                   default         Thu Feb  7 18:30:53 2019
    192.168.0.11/24           leaf01            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.12/24           leaf02            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.13/24           leaf03            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.14/24           leaf04            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.21/24           spine01           eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.22/24           spine02           eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.254/24          oob-mgmt-server   eth1                      default         Thu Feb  7 18:30:53 2019
    192.168.0.31/24           server01          eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.32/24           server02          eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.33/24           server03          eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.34/24           server04          eth0                      default         Thu Feb  7 18:30:53 2019

**Example: View IPv6 address information for all devices**

    cumulus@switch:~$ netq show ipv6 addresses 
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    fe80::203:ff:fe11:1101/64 server01          eth1                      default         Thu Feb  7 18:30:53 2019
    fe80::203:ff:fe22:2202/64 server02          eth2                      default         Thu Feb  7 18:30:53 2019
    fe80::203:ff:fe33:3301/64 server03          eth1                      default         Thu Feb  7 18:30:53 2019
    fe80::203:ff:fe44:4402/64 server04          eth2                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:18/6 leaf02            br0                       default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:1b/6 leaf03            swp52                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:1c/6 spine02           swp3                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:23/6 leaf03            br0                       default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:24/6 leaf01            swp52                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:25/6 spine02           swp1                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:28/6 leaf02            swp51                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:29/6 spine01           swp2                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:2c/6 leaf04            br0                       default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:3/64 leaf01            br0                       default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:3b/6 leaf04            swp51                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:3c/6 spine01           swp4                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:46/6 leaf04            swp52                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:47/6 spine02           swp4                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:4f/6 leaf03            swp51                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:50/6 spine01           swp3                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:53/6 leaf01            swp51                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:54/6 spine01           swp1                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:57/6 oob-mgmt-server   eth1                      default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:5d/6 leaf02            swp52                     default         Thu Feb  7 18:30:53 2019
    fe80::4638:39ff:fe00:5e/6 spine02           swp2                      default         Thu Feb  7 18:30:53 2019
    fe80::5054:ff:fe77:c277/6 oob-mgmt-server   eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:11/64  leaf01            eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:12/64  leaf02            eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:13/64  leaf03            eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:14/64  leaf04            eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:21/64  spine01           eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:22/64  spine02           eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:31/64  server01          eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:32/64  server02          eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:33/64  server03          eth0                      default         Thu Feb  7 18:30:53 2019
    fe80::a200:ff:fe00:34/64  server04          eth0                      default         Thu Feb  7 18:30:53 2019

**Example: Filter IP Address Information for a Specific Interface**

This example shows the IPv4 address information for the eth0 interface
on all devices.

    cumulus@switch:~$ netq show ip addresses eth0
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    10.0.0.254/32             oob-mgmt-server   eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.11/24           leaf01            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.12/24           leaf02            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.13/24           leaf03            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.14/24           leaf04            eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.21/24           spine01           eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.22/24           spine02           eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.31/24           server01          eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.32/24           server02          eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.33/24           server03          eth0                      default         Thu Feb  7 18:30:53 2019
    192.168.0.34/24           server04          eth0                      default         Thu Feb  7 18:30:53 2019

**Example: Filter IP Address Information for a Specific Device**

This example shows the IPv6 address information for the leaf01 switch.

    cumulus@switch:~$ netq leaf01 show ipv6 addresses 
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    2001:c15c:d06:f00d::16/12 leaf01            lo                        default         Fri Feb  8 00:35:07 2019
    8
    2001:cafe:babe:0:22::/128 leaf01            DataVrf1080               DataVrf1080     Fri Feb  8 00:35:07 2019
    2001:cafe:babe:1:22::/128 leaf01            DataVrf1081               DataVrf1081     Fri Feb  8 00:35:07 2019
    2001:cafe:babe:2:22::/128 leaf01            DataVrf1082               DataVrf1082     Fri Feb  8 00:35:07 2019
    2001:fee1:600d:10::1/64   leaf01            VlanA-1.102               DataVrf1082     Fri Feb  8 00:35:07 2019
    2001:fee1:600d:11::1/64   leaf01            VlanA-1.103               default         Fri Feb  8 00:35:07 2019
    2001:fee1:600d:12::1/64   leaf01            VlanA-1.104               default         Fri Feb  8 00:35:07 2019
    2001:fee1:600d:13::1/64   leaf01            VlanA-1.105               default         Fri Feb  8 00:35:07 2019
    2001:fee1:600d:14::1/64   leaf01            VlanA-1.106               default         Fri Feb  8 00:35:07 2019
    2001:fee1:600d:e::1/64    leaf01            VlanA-1.100               DataVrf1080     Fri Feb  8 00:35:07 2019
    2001:fee1:600d:f::1/64    leaf01            VlanA-1.101               DataVrf1081     Fri Feb  8 00:35:07 2019
    2001:fee1:d00d:1::1/64    leaf01            vlan1001-v0               vrf1            Fri Feb  8 00:35:07 2019
    2001:fee1:d00d:1::2/64    leaf01            vlan1001                  vrf1            Fri Feb  8 00:35:07 2019
    2001:fee1:d00d:2::1/64    leaf01            vlan1002-v0               vrf1            Fri Feb  8 00:35:07 2019

**Example: View Changes to IP Address Information**

This example shows the IPv4 address information that changed for all
devices around 1 day ago.

    cumulus@switch:~$ netq show ip addresses around 1d 
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    192.168.0.15/24           leaf01            eth0                      mgmt            Thu Feb  7 22:49:26 2019
    27.0.0.22/32              leaf01            lo                        default         Thu Feb  7 22:49:26 2019
    3.0.3.129/26              leaf01            VlanA-1.100               DataVrf1080     Thu Feb  7 22:49:26 2019
    3.0.3.193/26              leaf01            VlanA-1.101               DataVrf1081     Thu Feb  7 22:49:26 2019
    3.0.4.1/26                leaf01            VlanA-1.102               DataVrf1082     Thu Feb  7 22:49:26 2019
    3.0.4.129/26              leaf01            VlanA-1.104               default         Thu Feb  7 22:49:26 2019
    3.0.4.193/26              leaf01            VlanA-1.105               default         Thu Feb  7 22:49:26 2019
    3.0.4.65/26               leaf01            VlanA-1.103               default         Thu Feb  7 22:49:26 2019
    3.0.5.1/26                leaf01            VlanA-1.106               default         Thu Feb  7 22:49:26 2019
    30.0.0.22/32              leaf01            DataVrf1080               DataVrf1080     Thu Feb  7 22:49:26 2019
    30.0.1.22/32              leaf01            DataVrf1081               DataVrf1081     Thu Feb  7 22:49:26 2019
    30.0.2.22/32              leaf01            DataVrf1082               DataVrf1082     Thu Feb  7 22:49:26 2019
    45.0.0.13/26              leaf01            NetQBond-1                mgmt            Thu Feb  7 22:49:26 2019
    6.0.0.1/26                leaf01            vlan1000-v0               vrf1            Thu Feb  7 22:49:26 2019
    6.0.0.129/26              leaf01            vlan1002-v0               vrf1            Thu Feb  7 22:49:26 2019

**Example: Obtain a Count of IP Addresses Used on a Node**

This example shows the number of IPv4 and IPv6 addresses on the node
leaf01. Note that you must specify a hostname to use the count option.

    cumulus@switch:~$ netq leaf01 show ip addresses count
    Count of matching address records: 33
     
    cumulus@switch:~$ netq leaf01 show ipv6 addresses count
    Count of matching address records: 42

### <span>View IP Neighbor Information</span>

You can view the IPv4 and IPv6 neighbor information for all of your
devices, including the interface port, MAC address, VRF assignment, and
whether it learns the MAC address from the peer (remote=yes).
Additionally, you can:

  - view the information at an earlier point in time

  - filter against a particular device, interface, address or VRF
    assignment

  - obtain a count of all of the addresses

Each of these provides information for troubleshooting potential
configuration and communication issues at the layer 3 level.

**Example: View IPv4 Neighbor Information for All Devices**

    cumulus@switch:~$ netq show ip neighbors 
    Matching neighbor records:
    IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
    ------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
    10.255.5.1                oob-mgmt-server   eth0                      52:54:00:0f:79:30  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf01            swp51                     44:38:39:00:00:54  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf01            swp52                     44:38:39:00:00:25  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf02            swp51                     44:38:39:00:00:29  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf02            swp52                     44:38:39:00:00:5e  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf03            swp51                     44:38:39:00:00:50  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf03            swp52                     44:38:39:00:00:1c  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf04            swp51                     44:38:39:00:00:3c  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               leaf04            swp52                     44:38:39:00:00:47  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine01           swp1                      44:38:39:00:00:53  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine01           swp2                      44:38:39:00:00:28  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine01           swp3                      44:38:39:00:00:4f  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine01           swp4                      44:38:39:00:00:3b  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine02           swp1                      44:38:39:00:00:24  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine02           swp2                      44:38:39:00:00:5d  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine02           swp3                      44:38:39:00:00:1b  default         no     Thu Feb  7 22:49:26 2019
    169.254.0.1               spine02           swp4                      44:38:39:00:00:46  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.11              oob-mgmt-server   eth1                      a0:00:00:00:00:11  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.12              oob-mgmt-server   eth1                      a0:00:00:00:00:12  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.13              oob-mgmt-server   eth1                      a0:00:00:00:00:13  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.14              oob-mgmt-server   eth1                      a0:00:00:00:00:14  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.21              oob-mgmt-server   eth1                      a0:00:00:00:00:21  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.22              oob-mgmt-server   eth1                      a0:00:00:00:00:22  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.253             oob-mgmt-server   eth1                      a0:00:00:00:00:50  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.254             leaf01            eth0                      44:38:39:00:00:57  default         no     Thu Feb  7 22:49:26 2019
    192.168.0.254             leaf02            eth0                      44:38:39:00:00:57  default         no     Thu Feb  7 22:49:26 2019
    ...

**Example: View IPv6 Neighbor Information for a Given Device**

This example shows the IPv6 neighbors for leaf02 switch.

    cumulus@switch$ netq leaf02 show ipv6 neighbors 
    Matching neighbor records:
    IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
    ------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
    fe80::203:ff:fe22:2202    leaf02            br0                       00:03:00:22:22:02  default         no     Thu Feb  7 22:49:26 2019
    fe80::4638:39ff:fe00:29   leaf02            swp51                     44:38:39:00:00:29  default         no     Thu Feb  7 22:49:26 2019
    fe80::4638:39ff:fe00:4    leaf02            eth0                      44:38:39:00:00:04  default         no     Thu Feb  7 22:49:26 2019
    fe80::4638:39ff:fe00:5e   leaf02            swp52                     44:38:39:00:00:5e  default         no     Thu Feb  7 22:49:26 2019
    fe80::a200:ff:fe00:31     leaf02            eth0                      a0:00:00:00:00:31  default         no     Thu Feb  7 22:49:26 2019
    fe80::a200:ff:fe00:32     leaf02            eth0                      a0:00:00:00:00:32  default         no     Thu Feb  7 22:49:26 2019
    fe80::a200:ff:fe00:33     leaf02            eth0                      a0:00:00:00:00:33  default         no     Thu Feb  7 22:49:26 2019
    fe80::a200:ff:fe00:34     leaf02            eth0                      a0:00:00:00:00:34  default         no     Thu Feb  7 22:49:26 2019

### <span>View IP Routes Information</span>

You can view the IPv4 and IPv6 routes for all of your devices, including
the IP address (with or without mask), the destination (by hostname) of
the route, next hops available, VRF assignment, and whether a host is
the owner of the route or MAC address. Additionally, you can:

  - view the information at an earlier point in time

  - filter against a particular address or VRF assignment

  - obtain a count of all of the routes

Each of these provides information for troubleshooting potential
configuration and communication issues at the layer 3 level.

**Example: View IP Routes for All Devices**

This example shows the IPv4 and IPv6 routes for all devices in the
network.

    cumulus@switch:~$ netq show ipv6 routes 
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    yes    default         ::/0                           server04          lo                                  Thu Feb  7 22:49:26 2019
    yes    default         ::/0                           server03          lo                                  Thu Feb  7 22:49:26 2019
    yes    default         ::/0                           server01          lo                                  Thu Feb  7 22:49:26 2019
    yes    default         ::/0                           server02          lo                                  Thu Feb  7 22:49:26 2019
     
    cumulus@switch:~$ netq show ip routes 
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    yes    DataVrf1080     3.0.3.128/26                   leaf01            VlanA-1.100                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1080     3.0.3.129/32                   leaf01            VlanA-1.100                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1080     30.0.0.22/32                   leaf01            DataVrf1080                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1081     3.0.3.192/26                   leaf01            VlanA-1.101                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1081     3.0.3.193/32                   leaf01            VlanA-1.101                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1081     30.0.1.22/32                   leaf01            DataVrf1081                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1082     3.0.4.0/26                     leaf01            VlanA-1.102                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1082     3.0.4.1/32                     leaf01            VlanA-1.102                         Fri Feb  8 00:46:17 2019
    yes    DataVrf1082     30.0.2.22/32                   leaf01            DataVrf1082                         Fri Feb  8 00:46:17 2019
    yes    default         27.0.0.22/32                   leaf01            lo                                  Fri Feb  8 00:46:17 2019
    yes    default         3.0.4.128/26                   leaf01            VlanA-1.104                         Fri Feb  8 00:46:17 2019
    yes    default         3.0.4.129/32                   leaf01            VlanA-1.104                         Fri Feb  8 00:46:17 2019
    yes    default         3.0.4.192/26                   leaf01            VlanA-1.105                         Fri Feb  8 00:46:17 2019
    yes    default         3.0.4.193/32                   leaf01            VlanA-1.105                         Fri Feb  8 00:46:17 2019
    ...

**Example: View IP Routes for a Given IP** **Address**

This example shows the routes available for an IP address of 10.0.0.12.

    cumulus@switch:~$ netq show ip routes 10.0.0.12
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         10.0.0.12/32                   leaf03            10.0.0.21: swp51, 10.0.0.22: swp52  Fri Feb  8 00:46:17 2019
    no     default         10.0.0.12/32                   leaf01            10.0.0.21: swp51, 10.0.0.22: swp52  Fri Feb  8 00:46:17 2019
    no     default         10.0.0.12/32                   leaf04            10.0.0.21: swp51, 10.0.0.22: swp52  Fri Feb  8 00:46:17 2019
    no     default         10.0.0.12/32                   spine02           10.0.0.12: swp2                     Fri Feb  8 00:46:17 2019
    no     default         10.0.0.12/32                   spine01           10.0.0.12: swp2                     Fri Feb  8 00:46:17 2019
    yes    default         10.0.0.12/32                   leaf02            lo                                  Fri Feb  8 00:46:17 2019

**Example: View IP Routes Owned by a Given Device**

This example shows the IPv4 routes that are owned by spine01 switch.

    cumulus@switch:~$ netq spine01 show ip routes origin 
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    yes    default         10.0.0.21/32                   spine01           lo                                  Fri Feb  8 00:46:17 2019
    yes    default         192.168.0.0/24                 spine01           eth0                                Fri Feb  8 00:46:17 2019
    yes    default         192.168.0.21/32                spine01           eth0                                Fri Feb  8 00:46:17 2019

**Example: View IP Routes for a Given Device at a Prior Time**

This example show the IPv4 routes for spine01 switch about 24 hours ago.

    cumulus@switch:~$ netq spine01 show ip routes around 24h
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         10.0.0.11/32                   spine01           169.254.0.1: swp1                   Fri Feb  8 00:46:17 2019
    no     default         10.0.0.12/32                   spine01           169.254.0.1: swp2                   Fri Feb  8 00:46:17 2019
    no     default         10.0.0.13/32                   spine01           169.254.0.1: swp3                   Fri Feb  8 00:46:17 2019
    no     default         10.0.0.14/32                   spine01           169.254.0.1: swp4                   Fri Feb  8 00:46:17 2019
    no     default         172.16.1.0/24                  spine01           169.254.0.1: swp1                   Fri Feb  8 00:46:17 2019
    no     default         172.16.2.0/24                  spine01           169.254.0.1: swp2                   Fri Feb  8 00:46:17 2019
    no     default         172.16.3.0/24                  spine01           169.254.0.1: swp3                   Fri Feb  8 00:46:17 2019
    no     default         172.16.4.0/24                  spine01           169.254.0.1: swp4                   Fri Feb  8 00:46:17 2019
    yes    default         10.0.0.21/32                   spine01           lo                                  Fri Feb  8 00:46:17 2019
    yes    default         192.168.0.0/24                 spine01           eth0                                Fri Feb  8 00:46:17 2019
    yes    default         192.168.0.21/32                spine01           eth0                                Fri Feb  8 00:46:17 2019

**Example: View the Number of IP Routes on a Node**

This example shows the total number of IP routes for all devices on a
node.

    cumulus@switch:~$ netq leaf01 show ip routes count
    Count of matching routes records: 125
     
    cumulus@switch:~$ netq leaf01 show ipv6 routes count
    Count of matching routes records: 5

## <span>Monitor BGP Configuration</span>

<span style="color: #000000;"> If you have BGP running on your switches
and hosts, you can monitor its operation using the NetQ CLI. For each
device, you can view its associated neighbors, ASN (autonomous system
number), peer ASN, receive IP or EVPN address prefixes, and </span> VRF
assignment. Additionally, you can:

  - view the information at an earlier point in time

  - filter against a particular device, ASN, or VRF assignment

  - validate it is operating correctly across the network

The `netq show bgp` command is used to obtain the BGP configuration
information from the devices. The `netq check bgp` command is used to
validate the configuration. The syntax of these commands is:

    netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type bgp [between <text-time> and <text-endtime>] [json]
    netq check bgp [vrf <vrf>] [around <text-time>] [json]

{{%notice info%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)

  - h: hour(s)

  - m: minute(s)

  - s: second(s)

  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### <span>View BGP Configuration Information</span>

NetQ enables you to view the BGP configuration of a single device or
across all of your devices at once. You can filter the results based on
an ASN, BGP session (IP address or interface name), or VRF assignment.
You can view the configuration in the past and view changes made to the
configuration within a given timeframe.

**Example: View BGP Configuration Information Across Network**

This example shows the BGP configuration across all of your switches. In
this scenario, BGP routing is configured between two spines and four
leafs. Each leaf switch has a unique ASN and the spine switches share an
ASN. The PfxRx column indicates that these devices have IPv4 address
prefixes. The second and third values in this column indicate IPv6 and
EVPN address prefixes when configured. This configuration was changed
just over one day ago.

    cumulus@switch:~$ netq show bgp
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    exit-1            swp3(spine-1)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
    exit-1            swp3.2(spine-1)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp3.3(spine-1)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp3.4(spine-1)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp4(spine-2)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
    exit-1            swp4.2(spine-2)              DataVrf1080     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp4.3(spine-2)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp4.4(spine-2)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp5(spine-3)                default         655537     655435     30/25/434    Thu Feb  7 18:19:50 2019
    exit-1            swp5.2(spine-3)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp5.3(spine-3)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp5.4(spine-3)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit-1            swp7                         default         655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit-1            swp7.2                       DataVrf1080     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit-1            swp7.3                       DataVrf1081     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit-1            swp7.4                       DataVrf1082     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit-2            swp3(spine-1)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
    exit-2            swp3.2(spine-1)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp3.3(spine-1)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp3.4(spine-1)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp4(spine-2)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
    exit-2            swp4.2(spine-2)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp4.3(spine-2)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp4.4(spine-2)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp5(spine-3)                default         655538     655435     27/24/434    Thu Feb  7 18:19:50 2019
    exit-2            swp5.2(spine-3)              DataVrf1080     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp5.3(spine-3)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp5.4(spine-3)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit-2            swp7                         default         655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    exit-2            swp7.2                       DataVrf1080     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    exit-2            swp7.3                       DataVrf1081     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    exit-2            swp7.4                       DataVrf1082     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    spine-1           swp10(exit-2)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp10.2(exit-2)              DataVrf1080     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp10.3(exit-2)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp10.4(exit-2)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp3(leaf-11)                default         655435     655559     19/6/94      Thu Feb  7 18:19:50 2019
    spine-1           swp3.2(leaf-11)              DataVrf1080     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp3.3(leaf-11)              DataVrf1081     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp3.4(leaf-11)              DataVrf1082     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp4(leaf-12)                default         655435     655560     19/6/64      Thu Feb  7 18:19:50 2019
    spine-1           swp4.2(leaf-12)              DataVrf1080     655435     655560     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp4.3(leaf-12)              DataVrf1081     655435     655560     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp4.4(leaf-12)              DataVrf1082     655435     655560     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp5(leaf-21)                default         655435     655561     19/6/50      Thu Feb  7 18:19:50 2019
    spine-1           swp5.2(leaf-21)              DataVrf1080     655435     655561     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp5.3(leaf-21)              DataVrf1081     655435     655561     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp5.4(leaf-21)              DataVrf1082     655435     655561     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp6(leaf-22)                default         655435     655562     19/6/62      Thu Feb  7 18:19:50 2019
    spine-1           swp6.2(leaf-22)              DataVrf1080     655435     655562     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp6.3(leaf-22)              DataVrf1081     655435     655562     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp6.4(leaf-22)              DataVrf1082     655435     655562     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp7(leaf-1)                 default         655435     655557     17/5/54      Thu Feb  7 18:19:50 2019
    spine-1           swp7.2(leaf-1)               DataVrf1080     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp7.3(leaf-1)               DataVrf1081     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp7.4(leaf-1)               DataVrf1082     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp8(leaf-2)                 default         655435     655558     17/5/54      Thu Feb  7 18:19:50 2019
    spine-1           swp8.2(leaf-2)               DataVrf1080     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp8.3(leaf-2)               DataVrf1081     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp8.4(leaf-2)               DataVrf1082     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine-1           swp9(exit-1)                 default         655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp9.2(exit-1)               DataVrf1080     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp9.3(exit-1)               DataVrf1081     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine-1           swp9.4(exit-1)               DataVrf1082     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine-2           swp10(exit-2)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-2           swp10.3(exit-2)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-2           swp10.4(exit-2)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine-2           swp3.2(leaf-11)              DataVrf1080     655435     655559     14/2/0       Thu Feb  7 18:19:50 2019
     
    ...

**Example: View BGP Configuration Information for a Given Device**

This example shows the BGP configuration information for the spine02
switch. The switch is peered with swp1 on leaf01, swp2 on leaf02, and so
on. Spine02 has an ASN of 65020 and each of the leafs have unique ASNs.

    cumulus@switch:~$ netq spine02 show bgp 
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    spine02           swp3(spine01)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    spine02           swp3.2(spine01)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp3.3(spine01)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp3.4(spine01)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp5(spine03)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    spine02           swp5.2(spine03)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp5.3(spine03)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp5.4(spine03)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019

**Example: View BGP Configuration Information for a Given ASN**

This example shows the BGP configuration information for ASN of
*655557*. This ASN is associated with spine02 and so the results show
the BGP neighbors for that switch.

    cumulus@switch:~$ netq show bgp asn 655557 
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    spine02           swp3(spine01)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    spine02           swp3.2(spine01)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp3.3(spine01)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp3.4(spine01)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp5(spine03)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    spine02           swp5.2(spine03)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp5.3(spine03)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    spine02           swp5.4(spine03)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019

**Example: View BGP Configuration Information for a Prior Time**

This example shows the BGP configuration information as it was 12 hours
earlier.

    cumulus@switch:~$ netq show bgp around 12h
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    exit01            swp3(spine01)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
    exit01            swp3.2(spine01)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp3.3(spine01)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp3.4(spine01)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp4(spine02)                default         655537     655435     29/25/434    Thu Feb  7 18:19:50 2019
    exit01            swp4.2(spine02)              DataVrf1080     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp4.3(spine02)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp4.4(spine02)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp5(spine03)                default         655537     655435     30/25/434    Thu Feb  7 18:19:50 2019
    exit01            swp5.2(spine03)              DataVrf1080     655537     655435     15/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp5.3(spine03)              DataVrf1081     655537     655435     14/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp5.4(spine03)              DataVrf1082     655537     655435     16/13/0      Thu Feb  7 18:19:50 2019
    exit01            swp6(firewall01)             default         655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
    exit01            swp6.2(firewall01)           DataVrf1080     655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
    exit01            swp6.3(firewall01)           DataVrf1081     655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
    exit01            swp6.4(firewall01)           DataVrf1082     655537     655539     73/69/-      Thu Feb  7 18:26:30 2019
    exit01            swp7                         default         655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit01            swp7.2                       DataVrf1080     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit01            swp7.3                       DataVrf1081     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit01            swp7.4                       DataVrf1082     655537     -          NotEstd      Thu Feb  7 18:31:44 2019
    exit02            swp3(spine01)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
    exit02            swp3.2(spine01)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp3.3(spine01)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp3.4(spine01)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp4(spine02)                default         655538     655435     28/24/434    Thu Feb  7 18:19:50 2019
    exit02            swp4.2(spine02)              DataVrf1080     655538     655435     14/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp4.3(spine02)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp4.4(spine02)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp5(spine03)                default         655538     655435     27/24/434    Thu Feb  7 18:19:50 2019
    exit02            swp5.2(spine03)              DataVrf1080     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp5.3(spine03)              DataVrf1081     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp5.4(spine03)              DataVrf1082     655538     655435     15/12/0      Thu Feb  7 18:19:50 2019
    exit02            swp6(firewall01)             default         655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
    exit02            swp6.2(firewall01)           DataVrf1080     655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
    exit02            swp6.3(firewall01)           DataVrf1081     655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
    exit02            swp6.4(firewall01)           DataVrf1082     655538     655539     7/5/-        Thu Feb  7 18:26:30 2019
    exit02            swp7                         default         655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    exit02            swp7.2                       DataVrf1080     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    exit02            swp7.3                       DataVrf1081     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    exit02            swp7.4                       DataVrf1082     655538     -          NotEstd      Thu Feb  7 18:31:49 2019
    firewall01        swp3(exit01)                 default         655539     655537     29/27/-      Thu Feb  7 18:26:30 2019
    firewall01        swp3.2(exit01)               default         655539     655537     15/15/-      Thu Feb  7 18:26:30 2019
    firewall01        swp3.3(exit01)               default         655539     655537     15/15/-      Thu Feb  7 18:26:30 2019
    firewall01        swp3.4(exit01)               default         655539     655537     15/15/-      Thu Feb  7 18:26:30 2019
    firewall01        swp4(exit02)                 default         655539     655538     29/27/-      Thu Feb  7 18:26:30 2019
    firewall01        swp4.2(exit02)               default         655539     655538     15/15/-      Thu Feb  7 18:26:30 2019
    firewall01        swp4.3(exit02)               default         655539     655538     15/15/-      Thu Feb  7 18:26:30 2019
    firewall01        swp4.4(exit02)               default         655539     655538     15/15/-      Thu Feb  7 18:26:30 2019
    spine01           swp10(exit02)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp10.2(exit02)              DataVrf1080     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp10.3(exit02)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp10.4(exit02)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp7(leaf01)                 default         655435     655557     17/5/54      Thu Feb  7 18:19:50 2019
    spine01           swp7.2(leaf01)               DataVrf1080     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine01           swp7.3(leaf01)               DataVrf1081     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine01           swp7.4(leaf01)               DataVrf1082     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine01           swp8(leaf02)                 default         655435     655558     17/5/54      Thu Feb  7 18:19:50 2019
    spine01           swp8.2(leaf02)               DataVrf1080     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine01           swp8.3(leaf02)               DataVrf1081     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine01           swp8.4(leaf02)               DataVrf1082     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine01           swp9(exit01)                 default         655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp9.2(exit01)               DataVrf1080     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp9.3(exit01)               DataVrf1081     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine01           swp9.4(exit01)               DataVrf1082     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp10(exit02)                default         655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp10.3(exit02)              DataVrf1081     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp10.4(exit02)              DataVrf1082     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp7(leaf01)                 default         655435     655557     17/5/62      Thu Feb  7 18:19:50 2019
    spine02           swp7.2(leaf01)               DataVrf1080     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine02           swp7.3(leaf01)               DataVrf1081     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine02           swp7.4(leaf01)               DataVrf1082     655435     655557     14/2/0       Thu Feb  7 18:19:50 2019
    spine02           swp8(leaf02)                 default         655435     655558     17/5/62      Thu Feb  7 18:19:50 2019
    spine02           swp8.2(leaf02)               DataVrf1080     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine02           swp8.3(leaf02)               DataVrf1081     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine02           swp8.4(leaf02)               DataVrf1082     655435     655558     14/2/0       Thu Feb  7 18:19:50 2019
    spine02           swp9(exit01)                 default         655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp9.2(exit01)               DataVrf1080     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp9.4(exit01)               DataVrf1082     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp10.2(exit02)              DataVrf1080     655435     655538     10/5/0       Thu Feb  7 18:19:50 2019
    spine02           swp9.3(exit01)               DataVrf1081     655435     655537     19/5/0       Thu Feb  7 18:19:50 2019
    leaf01            swp3(spine01)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    leaf01            swp3.2(spine01)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp3.3(spine01)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp3.4(spine01)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp4(spine02)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    leaf01            swp4.2(spine02)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp4.3(spine02)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp4.4(spine02)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp5(spine03)                default         655557     655435     42/27/324    Thu Feb  7 18:19:50 2019
    leaf01            swp5.2(spine03)              DataVrf1080     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp5.3(spine03)              DataVrf1081     655557     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf01            swp5.4(spine03)              DataVrf1082     655557     655435     29/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp3(spine01)                default         655558     655435     42/27/372    Thu Feb  7 18:19:50 2019
    leaf02            swp3.2(spine01)              DataVrf1080     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp3.3(spine01)              DataVrf1081     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp3.4(spine01)              DataVrf1082     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp4(spine02)                default         655558     655435     42/27/372    Thu Feb  7 18:19:50 2019
    leaf02            swp4.2(spine02)              DataVrf1080     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp4.3(spine02)              DataVrf1081     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp4.4(spine02)              DataVrf1082     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp5(spine03)                default         655558     655435     42/27/372    Thu Feb  7 18:19:50 2019
    leaf02            swp5.2(spine03)              DataVrf1080     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp5.3(spine03)              DataVrf1081     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    leaf02            swp5.4(spine03)              DataVrf1082     655558     655435     31/18/0      Thu Feb  7 18:19:50 2019
    ...

**Example: View BGP Configuration Changes**

This example shows that BGP configuration changes were made about five
days ago on this network.

    cumulus@switch:~$ netq show events type bgp between now and 5d
     
    Matching bgp records:
    Hostname          Message Type Severity Message                             Timestamp
    ----------------- ------------ -------- ----------------------------------- -------------------------
    leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine03 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine02 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
    leaf01            bgp          info     BGP session with peer spine01 @desc 2h:10m:11s
                                            : state changed from failed to esta
                                            blished
     
    ...

### <span>Validate BGP Operation</span>

A single command enables you to validate that all configured route
peering is established across the network. The command checks for
duplicate router IDs and sessions that are in an unestablished state.
Either of these conditions trigger a configuration check failure. When a
failure is found, the reason is identified in the output along with the
time the issue occurred.

This example shows a check on the BGP operations that found no failed
sessions.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0

This example shows 24 failed BGP sessions with a variety of reasons.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 25, Failed Nodes: 3, Total Sessions: 220 , Failed Sessions: 24, 
    Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
    ----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
    exit-1            DataVrf1080     swp6.2            firewall-1        BGP session with peer firewall-1 swp6.2: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-1            DataVrf1080     swp7.2            firewall-2        BGP session with peer firewall-2 (swp7.2 vrf  1d:7h:49m:31s
                                                                          DataVrf1080) failed,                         
                                                                          reason: Peer not configured                  
    exit-1            DataVrf1081     swp6.3            firewall-1        BGP session with peer firewall-1 swp6.3: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-1            DataVrf1081     swp7.3            firewall-2        BGP session with peer firewall-2 (swp7.3 vrf  1d:7h:49m:31s
                                                                          DataVrf1081) failed,                         
                                                                          reason: Peer not configured                  
    exit-1            DataVrf1082     swp6.4            firewall-1        BGP session with peer firewall-1 swp6.4: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-1            DataVrf1082     swp7.4            firewall-2        BGP session with peer firewall-2 (swp7.4 vrf  1d:7h:49m:31s
                                                                          DataVrf1082) failed,                         
                                                                          reason: Peer not configured                  
    exit-1            default         swp6              firewall-1        BGP session with peer firewall-1 swp6: AFI/SA 1d:7h:56m:9s
                                                                          FI evpn not activated on peer                
    exit-1            default         swp7              firewall-2        BGP session with peer firewall-2 (swp7 vrf de 1d:7h:49m:31s
                                                                          fault) failed, reason: Peer not configured   
    exit-2            DataVrf1080     swp6.2            firewall-1        BGP session with peer firewall-1 swp6.2: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    exit-2            DataVrf1080     swp7.2            firewall-2        BGP session with peer firewall-2 (swp7.2 vrf  1d:7h:49m:26s
                                                                          DataVrf1080) failed,                         
                                                                          reason: Peer not configured                  
    exit-2            DataVrf1081     swp6.3            firewall-1        BGP session with peer firewall-1 swp6.3: AFI/ 1d:7h:56m:9s
                                                                          SAFI evpn not activated on peer              
    ...

## <span>Monitor OSPF Configuration</span>

<span style="color: #000000;"> If you have OSPF running on your switches
and hosts, you can monitor its operation using the NetQ CLI. For each
device, you can view its </span> <span style="color: #000000;">
associated interfaces, areas, peers, state, and type of OSPF running
(numbered or unnumbered). </span> Additionally, you can:

  - view the information at an earlier point in time

  - filter against a particular device, interface, or area

  - <span style="color: #000000;"> validate it is operating correctly
    across the network </span>

<span style="color: #000000;"> The </span> `netq show ospf`
<span style="color: #000000;"> command is used to obtain the OSPF
configuration information from the devices. The `netq check ospf`
command is used to validate the configuration. The syntax of these
commands is: </span>

    netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] [around <text-time>] [json]
    netq [<hostname>] show events [level info|level error|level warning|level critical|level debug] type ospf [between <text-time> and <text-endtime>] [json]
    netq check ospf [around <text-time>] [json]

{{%notice info%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)

  - h: hour(s)

  - m: minute(s)

  - s: second(s)

  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### <span>View OSPF Configuration Information</span>

<span style="color: #000000;"> NetQ enables you to view the OSPF
configuration of a single device or across all of your devices at once.
You can filter the results based on a device, interface, or area. You
can view the configuration in the past and view changes made to the
configuration within a given timeframe. </span>

**<span style="color: #000000;"> Example: View OSPF Configuration
Information Across the Network </span>**

<span style="color: #000000;"> This example shows all devices included
in OSPF unnumbered routing, the assigned areas, state, peer and
interface, and the last time this information was changed. </span>

    cumulus@switch:~$ netq show ospf
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
    leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
    leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
    leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
    leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
    leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
    leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
    leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019
    spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     Thu Feb  7 14:42:16 2019
    spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     Thu Feb  7 14:42:16 2019
    spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     Thu Feb  7 14:42:16 2019
    spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     Thu Feb  7 14:42:16 2019
    spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     Thu Feb  7 14:42:16 2019
    spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     Thu Feb  7 14:42:16 2019
    spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     Thu Feb  7 14:42:16 2019
    spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     Thu Feb  7 14:42:16 2019

**<span style="color: #000000;"> Example: View
<span style="color: #000000;"> OSPF Configuration Information for a
Given Device </span> </span>**

<span style="color: #000000;"> <span style="color: #000000;"> This
example show the OSPF configuration information for leaf01. </span>
</span>

    cumulus@switch:~$ netq leaf01 show ospf
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
    leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019

**<span style="color: #000000;"> Example: View </span>
<span style="color: #000000;"> OSPF Configuration Information for a
Given Interface </span>**

<span style="color: #000000;"> This example shows the OSPF configuration
for all devices with the swp51 interface. </span>

    cumulus@switch:~$ netq show ospf swp51 
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
    leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
    leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
    leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019

**<span style="color: #000000;"> <span style="color: #000000;">
<span style="color: #000000;"> <span style="color: #000000;"> Example:
View </span> <span style="color: #000000;"> OSPF Configuration
Information at a Prior Time </span> </span> </span> </span>**

<span style="color: #000000;"> <span style="color: #000000;">
<span style="color: #000000;"> <span style="color: #000000;"> This
example shows the OSPF configuration for all leaf switches about five
minutes ago. </span> </span> </span> </span>

    cumulus@switch:~$ netq leaf* show ospf around 5m
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      Thu Feb  7 14:42:16 2019
    leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      Thu Feb  7 14:42:16 2019
    leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      Thu Feb  7 14:42:16 2019
    leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      Thu Feb  7 14:42:16 2019
    leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      Thu Feb  7 14:42:16 2019
    leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      Thu Feb  7 14:42:16 2019
    leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      Thu Feb  7 14:42:16 2019
    leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      Thu Feb  7 14:42:16 2019

### <span>Validate OSPF Operation</span>

A single command, `netq check ospf`, enables you to validate that all
configured route peering is established across the network. The command
checks for:

  - router ID conflicts, such as duplicate IDs

  - links that are down, or have mismatched MTUs

  - mismatched session parameters (hello timer, dead timer, area ids,
    and network type)

When peer information is not available, the command verifies whether
OSPF is configured on the peer and if so, whether the service is
disabled, shutdown, or not functioning.

All of these conditions trigger a configuration check failure. When a
failure is found, the reason is identified in the output along with the
time the issue occurred.

<span style="color: #000000;"> <span style="color: #000000;">
<span style="color: #000000;"> <span style="color: #000000;"> This
example shows a check on the OSPF operations that found no failed
sessions. </span> </span> </span> </span>

    cumulus@switch:~$ netq check ospf
    Total Sessions: 16, Failed Sessions: 0

<span style="color: #000000;"> This example shows a check on the OSPF
operations that found two failed sessions. The results indicate the
reason for the failure is a mismatched MTU for two links </span>
<span style="color: #000000;"> . </span>

    cumulus@switch:~$ netq check ospf
    Total Nodes: 21, Failed Nodes: 2, Total Sessions: 40 , Failed Sessions: 2,
    Hostname          Interface                 PeerID                    Peer IP                   Reason                                        Last Changed
    ----------------- ------------------------- ------------------------- ------------------------- --------------------------------------------- -------------------------
    spine03           swp6                      0.0.0.23                  27.0.0.23                 mtu mismatch, mtu mismatch                    Thu Feb  7 14:42:16 2019
    leaf22            swp5                      0.0.0.17                  27.0.0.17                 mtu mismatch, mtu mismatch                    Thu Feb  7 14:42:16 2019

## <span>View Paths between Devices</span>

<span style="color: #000000;"> You can <span style="color: #353744;">
view the available paths between two devices on the network currently
and at a time in the past using their IPv4 or IPv6 addresses </span> .
You can <span style="color: #353744;"> view the output in one of three
formats ( </span> *json, pretty,* <span style="color: #353744;"> and
</span> *detail* <span style="color: #353744;"> ). JSON output provides
the output in a JSON file format for ease of importing to other
applications or software. Pretty output lines up the paths in a
pseudo-graphical manner to help visualize multiple paths. Detail output
is the default when not specified, and is useful for traces with higher
hop counts where the pretty output wraps lines, making it harder to
interpret the results. The detail output displays a table with a row per
hop and a set of rows per path. </span> </span>

<span style="color: #000000;"> <span style="color: #353744;">
<span style="color: #000000;"> To view the paths, first identify the
addresses for the source and destination devices using the </span> `netq
show ip addresses` <span style="color: #000000;"> command (see syntax
above), and then use the </span> `netq trace`
<span style="color: #000000;"> command to see the available paths
between those devices. </span> </span> </span>
<span style="color: #353744;"> The trace command syntax is: </span>

    netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [json|detail|pretty] [debug]

{{%notice info%}}

The syntax requires the destination device address first, *\<ip\>*, and
then the source device address or hostname.

The tracing function only knows about addresses that have already been
learned. If you find that a path is invalid or incomplete, you may need
to ping the identified device so that its address becomes known.

{{%/notice%}}

### <span>View Paths between Two Switches with Pretty Output</span>

This example first determines the IP addresses of the leaf01 and leaf03
switches, then shows the available paths between them. The results
include a summary of the trace, including the total number of paths
available, those with errors and warnings, and the MTU of the paths. In
this case, the results are displayed in pseudo-graphical output.

``` 
cumulus@switch:~$ netq leaf01 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.0.0.11/32              leaf01            lo                        default         Fri Feb  8 01:35:49 2019
10.0.0.11/32              leaf01            swp51                     default         Fri Feb  8 01:35:49 2019
10.0.0.11/32              leaf01            swp52                     default         Fri Feb  8 01:35:49 2019
172.16.1.1/24             leaf01            br0                       default         Fri Feb  8 01:35:49 2019
192.168.0.11/24           leaf01            eth0                      default         Fri Feb  8 01:35:49 2019
 
cumulus@switch:~$ netq leaf03 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.0.0.13/32              leaf03            lo                        default         Thu Feb  7 18:31:29 2019
10.0.0.13/32              leaf03            swp51                     default         Thu Feb  7 18:31:29 2019
10.0.0.13/32              leaf03            swp52                     default         Thu Feb  7 18:31:29 2019
172.16.3.1/24             leaf03            br0                       default         Thu Feb  7 18:31:29 2019
192.168.0.13/24           leaf03            eth0                      default         Thu Feb  7 18:31:29 2019
 
cumulus@switch:~$ netq trace 10.0.0.13 from 10.0.0.11 pretty
Number of Paths: 2
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 1500
 
 leaf01 swp52 -- swp1 spine02 swp3 -- swp52 leaf03 <lo>  
        swp51 -- swp1 spine01 swp3 -- swp51 leaf03 <lo>  
```

### <span>View Paths between Two Switches with Detailed Output</span>

This example provides the same path information as the pretty output,
but displays the information in a tabular output. In this case there, no
VLAN is configured, so the related fields are left blank.

    cumulus@switch:~$ netq trace 10.0.0.13 from 10.0.0.11 detail
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 1500
     
    Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    1   1   leaf01                                                                                       swp52           default                               swp52
        2   spine02         swp1                                         swp1            default         swp3            default                               swp3
        3   leaf03          swp52                                        swp52           default         lo
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    2   1   leaf01                                                                                       swp51           default                               swp51
        2   spine01         swp1                                         swp1            default         swp3            default                               swp3
        3   leaf03          swp51                                        swp51           default         lo
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
