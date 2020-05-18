---
title: Redistribute Neighbor
author: Cumulus Networks
product: Cumulus Networks Guides
version: "1.0"
draft: true
---
If you are looking to modernise your campus network to make it more resilient and maximize utilisation, and to eliminate the use of the Spanning Tree Protocol (STP), consider using the Cumulus Linux layer 3 {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-41/Layer-3/Redistribute-Neighbor/" text="Redistribute Neighbor">}} feature.

Redistribute neighbor provides a way for IP subnets to span racks without forcing the end hosts to run a routing protocol by redistributing the Address Resolution Protocol (ARP) table (Linux IP neighbor table) into a dynamic routing protocol, such as OSPF or BGP. The host routes continue to be advertised into the routing domain as /32 prefix routes. Routing protocols can achieve reachability by routing on the Longest Prefix Match (LPM) based on these /32 host routes.

Redistribute neighbor eliminates the requirement to stretch a layer 2 domain across the entire campus network or across more than one switch. Limiting your layer 2 domain between the access switch port and the directly-connected host eliminates STP from the entire network. Without a stretched layer 2 domain, BUM traffic is limited to the access switch port, where the host is directly connected.

The multiple uplink ports on the access switch and the rest of the core network become layer 3, which provides faster convergence, greater resiliency, and packet forwarding intelligence. In addition, using Equal Cost Multipath (ECMP) on all layer 3 links lets you take advantage of the full available bandwidth. Coupling with features, such as BFD, helps you achieve essential sub-second failover and forwarding reconvergence on the core layer 3 links.

Using {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux-41/Layer-3/Border-Gateway-Protocol-BGP/#bgp-unnumbered-interfaces" text="BGP unnumbered ">}} for all layer 3 routing protocol links provides efficiency, IP address conservation, and reduces IP address management. Using BGP in the core enables you to achieve traffic engineering with route maps and prefix lists to manipulate routing and forwarding paths with the BGP attributes for certain prefixes and hosts.

Using subnets optimises performance. For example, when you have multiple buildings across the campus, you can allocate a /24 IP address block to a building, then another separate IP address block of /24 network addresses to another building, and so on. You can then perform route summarisation at the egress links of the building aggregation switches to summarise the subset /32 network prefixes and networks when advertising to the network core.

The following illustration shows a core network fabric with building A connected. The design closely reflects a multi data center spine and leaf fabric design where there is a spine and leaf fabric for the network core and for each building:

{{<img src="/images/guides/redis-neighbor.png" >}}

In the above illustrstion:

- Four hosts are connected to four separate switches (these switches can be inside a closet or connecting hosts on a floor).
- The switches then aggregate with separate layer 3 links to aggregation switches with BGP unnumbered running between them. These aggregation switches aggregate to a core spine and leaf fabric.

The routing configuration for the access swtiches (Acc-Sw1 and Acc-Sw2) is shown here:

{{< tabs "TABID01 ">}}

{{< tab "Acc-Sw1 ">}}

```
cumulus@Acc-Sw1:mgmt-vrf:~# net show configuration commands
net add bgp autonomous-system 65011
net add routing import-table 10 route-map REDIST_NEIGHBOR
net add routing route-map LOOPBACK_ROUTES permit 10 match interface lo
net add routing route-map REDIST_NEIGHBOR permit 10 match interface vlan13
net add bgp router-id 10.0.0.11
net add bgp bestpath as-path multipath-relax
net add bgp neighbor swp19 interface remote-as external
net add bgp neighbor swp20 interface remote-as external
net add bgp neighbor peerlink.4094 interface remote-as internal
net add bgp ipv4 unicast redistribute connected route-map LOOPBACK_ROUTES
net add bgp ipv4 unicast redistribute table 10
```

{{< /tab >}}

{{< tab "Acc-Sw3 ">}}

```
cumulus@Acc-Sw3:mgmt-vrf:~# net show configuration commands
net add bgp autonomous-system 65013
net add bgp router-id 10.0.0.13
net add bgp bestpath as-path multipath-relax
net add bgp neighbor swp19 interface remote-as external
net add bgp neighbor swp20 interface remote-as external
net add bgp neighbor peerlink.4094 interface remote-as internal
net add bgp ipv4 unicast redistribute connected route-map LOOPBACK_ROUTES
net add bgp ipv4 unicast redistribute table 10
```

{{< /tab >}}

{{< /tabs >}}

To verify connectivity between Host A (10.1.3.101) and Host C (10.1.3.103), which are on the same subnet, you can run these commands:

```
cumulus@host_A:~$ 10.1.3.103 show eth1
4: eth1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether 44:38:39:00:00:75 brd ff:ff:ff:ff:ff:ff
    inet 10.1.3.101/24 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::4638:39ff:fe00:75/64 scope link
       valid_lft forever preferred_lft forever
```

```
cumulus@host_C:~$ 10.1.3.101 show eth1
7: eth1: <BROADCAST,MULTICAST,MASTER,UP,LOWER_UP> mtu 9000 qdisc noqueue state UP group default qlen 1000
    link/ether 44:38:39:00:00:73 brd ff:ff:ff:ff:ff:ff
    inet 10.1.3.103/24 brd 10.1.3.255 scope global eth1
       valid_lft forever preferred_lft forever
    inet6 fe80::4638:39ff:fe00:73/64 scope link
       valid_lft forever preferred_lft forever
```

In this design, Proxy ARP is configured on the VLAN attached to the host so that the switch responds to all ARP requests when a host sends an ARP request for anything it is trying to reach on its subnet.

If you have many switches and need the VLAN across all the switches, you can specify a unique IP address on all the SVIs in the subnet, or you can use the anycast gateway with VRR. To conserve IP addresses, you can repeat physical IP addresses on a switch or switch pair (if you use MLAG).

The IP neighbor table on the hosts and the switches look like this:

```
cumulus@host_A:~$ sudo ip neighbor show | grep 10.1.3.103
10.1.3.103 dev eth1 lladdr 44:39:39:ff:00:13 REACHABLE

cumulus@host_C:~$ sudo ip neigh show | grep 10.1.3.101
10.1.3.101 dev uplink lladdr 44:38:39:00:00:74 REACHABLE

cumulus@Acc-Sw1:mgmt-vrf:~# sudo ip neigh show 10.1.3.101
10.1.3.101 dev vlan13 lladdr 44:38:39:00:00:75 REACHABLE

cumulus@Acc-Sw3:mgmt-vrf:~# sudo ip neigh show 10.1.3.103
10.1.3.103 dev vlan13 lladdr 44:38:39:00:00:73 REACHABLE
```

The routing table on the access and aggregation switches look like this:

```
cumulus@Acc-Sw1:mgmt-vrf:~# net show bgp 10.1.3.103
BGP routing table entry for 10.1.3.103/32
Paths: (2 available, best #2, table default)
  Advertised to non peer-group peers:
  BAagg-Sw1(swp19) BAagg-Sw2(swp20)
  65021 65013
    fe80::4638:39ff:fe00:4d from BAagg-Sw2(swp20) (10.0.0.22)
    (fe80::4638:39ff:fe00:4d) (used)
      Origin incomplete, valid, external, multipath
      AddPath ID: RX 0, TX 20
      Last update: Mon May  4 06:03:10 2020

  65021 65013
    fe80::4638:39ff:fe00:7b from BAagg-Sw1(swp19) (10.0.0.21)
    (fe80::4638:39ff:fe00:7b) (used)
      Origin incomplete, valid, external, multipath, bestpath-from-AS 65021, best
      AddPath ID: RX 0, TX 10
      Last update: Fri May  1 06:14:53 2020
```

```
cumulus@Acc-Sw1:mgmt-vrf:~# net show route 10.1.3.103
RIB entry for 10.1.3.103
========================
Routing entry for 10.1.3.103/32
  Known via "bgp", distance 20, metric 0, best
  Last update 00:00:11 ago
  * fe80::4638:39ff:fe00:7b, via swp19
  * fe80::4638:39ff:fe00:4d, via swp20

FIB entry for 10.1.3.103
========================
10.1.3.103  proto bgp  metric 20
        nexthop via 169.254.0.1  dev swp19 weight 1 onlink
        nexthop via 169.254.0.1  dev swp20 weight 1 onlink

cumulus@BAagg-Sw1:mgmt-vrf:~$ net show bgp 10.1.3.101
BGP routing table entry for 10.1.3.101/32
Paths: (1 available, best #1, table default)
  Advertised to non peer-group peers:
  Acc-Sw1(swp19) Acc-Sw2(swp20) Acc-Sw3(swp21) Acc-Sw4(swp22)
  65011
    fe80::4638:39ff:fe00:7c from Acc-Sw1(swp19) (10.0.0.11)
    (fe80::4638:39ff:fe00:7c) (used)
      Origin incomplete, metric 0, valid, external, bestpath-from-AS 65011, best
      AddPath ID: RX 0, TX 24
      Last update: Fri May  1 06:14:51 2020
```

```
cumulus@BAagg-Sw1:mgmt-vrf:~$ net show bgp 10.1.3.103
BGP routing table entry for 10.1.3.103/32
Paths: (2 available, best #1, table default)
  Advertised to non peer-group peers:
  Acc-Sw1(swp19) Acc-Sw2(swp20) Acc-Sw3(swp21) Acc-Sw4(swp22)
  65013
    fe80::4638:39ff:fe00:a2 from Acc-Sw3(swp21) (10.0.0.13)
    (fe80::4638:39ff:fe00:a2) (used)
      Origin incomplete, metric 0, valid, external, multipath, bestpath-from-AS 65013, best
      AddPath ID: RX 0, TX 19
      Last update: Fri May  1 06:04:32 2020

  65014
    fe80::4638:39ff:fe00:26 from Acc-Sw4(swp22) (10.0.0.14)
    (fe80::4638:39ff:fe00:26) (used)
      Origin incomplete, metric 0, valid, external, multipath, bestpath-from-AS 65014
      AddPath ID: RX 0, TX 18
      Last update: Fri May  1 06:04:32 2020
```

```
cumulus@BAagg-Sw1:mgmt-vrf:~$ net show route 10.1.3.101
RIB entry for 10.1.3.101
========================
Routing entry for 10.1.3.101/32
  Known via "bgp", distance 20, metric 0, best
  Last update 3d01h54m ago
  * fe80::4638:39ff:fe00:7c, via swp19


FIB entry for 10.1.3.101
========================
10.1.3.101 via 169.254.0.1 dev swp19  proto bgp  metric 20 onlink
```

```
cumulus@BAagg-Sw1:mgmt-vrf:~$ net show route 10.1.3.103
RIB entry for 10.1.3.103
========================
Routing entry for 10.1.3.103/32
  Known via "bgp", distance 20, metric 0, best
  Last update 3d02h04m ago
  * fe80::4638:39ff:fe00:a2, via swp21
  * fe80::4638:39ff:fe00:26, via swp22


FIB entry for 10.1.3.103
========================
10.1.3.103  proto bgp  metric 20
        nexthop via 169.254.0.1  dev swp21 weight 1 onlink
        nexthop via 169.254.0.1  dev swp22 weight 1 onlink
cumulus@BAagg-Sw1:mgmt-vrf:~$
```

```
cumulus@Acc-Sw3:mgmt-vrf:~# net show bgp 10.1.3.101  
BGP routing table entry for 10.1.3.101/32
Paths: (2 available, best #2, table default)
  Advertised to non peer-group peers:
  BAagg-Sw1(swp19) BAagg-Sw2(swp20)
  65021 65011
    fe80::4638:39ff:fe00:b7 from BAagg-Sw2(swp20) (10.0.0.22)
    (fe80::4638:39ff:fe00:b7) (used)
      Origin incomplete, valid, external, multipath
      AddPath ID: RX 0, TX 22
      Last update: Mon May  4 06:03:06 2020

  65021 65011
    fe80::4638:39ff:fe00:a1 from BAagg-Sw1(swp19) (10.0.0.21)
    (fe80::4638:39ff:fe00:a1) (used)
      Origin incomplete, valid, external, multipath, bestpath-from-AS 65021, best
      AddPath ID: RX 0, TX 19
      Last update: Fri May  1 06:14:51 2020
```

```
cumulus@Acc-Sw3:mgmt-vrf:~# net show route 10.1.3.101
RIB entry for 10.1.3.101
========================
Routing entry for 10.1.3.101/32
  Known via "bgp", distance 20, metric 0, best
  Last update 00:02:55 ago
  * fe80::4638:39ff:fe00:a1, via swp19
  * fe80::4638:39ff:fe00:b7, via swp20


FIB entry for 10.1.3.101
========================
10.1.3.101  proto bgp  metric 20
        nexthop via 169.254.0.1  dev swp19 weight 1 onlink
        nexthop via 169.254.0.1  dev swp20 weight 1 onlink
```

## Restrictions and Limitations

With existing campus networks, you need to consider current restrictions and limitations, such as switch stacking and limited fiber runs that make it difficult to transition to spine and leaf networks. If you have sufficient fiber runs, requirements for growth, scalability, redundancy, and resiliency with effective utilisation of uplinks, the spine and leaf architecture is ideal as packet forwarding is deterministic and predictable across the entire campus network.

If limitations exist, such as limited fiber runs available to a building, floor, or closet, you can use a ring topology.

Small floor or closet:

ILLUSTRATION

Larger floor or closet in a building with limited fiber runs:

ILLUSTRATION

In this deployment, you can perform segmentation in one of two ways:

- Use VRF (depending on the scale and design)
- Use 802.1x Dynamic ACL (DACL) with a NAC. This option is more suitable and scalable in this design. A host joining the network can be authenticated and policies pushed to the access switch through `iptable` rules or (access control list (ACL) to restrict the network resource access of that particular host.
