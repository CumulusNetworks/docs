---
title: Routing
author: Cumulus Networks
weight: 171
aliases:
 - /display/CL34/Routing
 - /pages/viewpage.action?pageId=7112651
pageID: 7112651
product: Cumulus Linux
version: 3.4.3
imgData: cumulus-linux-343
siteSlug: cumulus-linux-343
---
This chapter discusses routing on switches running Cumulus Linux.

## <span>Managing Static Routes</span>

You manage static routes using
[NCLU](/version/cumulus-linux-343/System_Configuration/Network_Command_Line_Utility_-_NCLU)
or the Cumulus Linux `ip route` command. The routes are added to the
[FRRouting](https://frrouting.org) routing table, and are then updated
into the kernel routing table as well.

To add a static route, run:

    cumulus@switch:~$ net add routing route 203.0.113.0/24 198.51.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/frr/frr.conf` file:

    !
    ip route 203.0.113.0/24 198.51.100.2
    !

To delete a static route, run:

    cumulus@switch:~$ net del routing route 203.0.113.0/24 198.51.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To view static routes, run:

    cumulus@switch:~$ net show route static 
    RIB entry for static
    ====================
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, P - PIM, T - Table,
           > - selected route, * - FIB route
    S>* 203.0.113.0/24 [1/0] via 198.51.100.2, swp3

### <span>Static Multicast Routes</span>

Static mroutes are also managed with NCLU, or with the `ip route`
command. To add an mroute:

    cumulus@switch:~$ net add routing mroute 230.0.0.0/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/frr/frr.conf` file:

    !
    ip mroute 230.0.0.0/24
    !

To delete an mroute, run:

    cumulus@switch:~$ net del routing mroute 230.0.0.0/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To view mroutes, open the FRRouting CLI, and run the following command:

    cumulus@switch:~$ sudo vtysh
    switch# show ip rpf 230.0.0.0
    Routing entry for 230.0.0.0/24 using Multicast RIB
      Known via "static", distance 1, metric 0, best
      * directly connected, swp31s0

### <span>Static Routing via ip route</span>

A static route can also be created by adding ` post-up ip route add
 `command to a switch port configuration. For example:

    cumulus@switch:~$ net add interface swp3 ip address 198.51.100.1/24
    cumulus@switch:~$ net add interface swp3 post-up routing route add 203.0.113.0/24 via 198.51.100.2
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands produce the following configuration in the
`/etc/network/interfaces` file:

    auto swp3
    iface swp3
        address 198.51.100.1/24
        post-up ip route add 203.0.113.0/24 via 198.51.100.2

{{%notice note%}}

If an IPv6 address is assigned to a DOWN interface, the associated route
is still installed into the routing table. The type of IPv6 address
doesn't matter: link local, site local and global all exhibit the same
problem.

If the interface is bounced up and down, then the routes are no longer
in the route table.

{{%/notice%}}

The `ip route` command allows manipulating the kernel routing table
directly from the Linux shell. See `man ip(8)` for details. FRRouting
monitors the kernel routing table changes and updates its own routing
table accordingly.

To display the routing table:

    cumulus@switch:~$ ip route show
    default via 10.0.1.2 dev eth0
    10.0.1.0/24 dev eth0  proto kernel  scope link  src 10.0.1.52
    192.0.2.0/24 dev swp1  proto kernel  scope link  src 192.0.2.12
    192.0.2.10/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.20/24  proto zebra  metric 20
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    192.0.2.30/24 via 192.0.2.1 dev swp1  proto zebra  metric 20
    192.0.2.40/24 dev swp2  proto kernel  scope link  src 192.0.2.42
    192.0.2.50/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.60/24 via 192.0.2.2 dev swp2  proto zebra  metric 20
    192.0.2.70/24  proto zebra  metric 30
         nexthop via 192.0.2.1  dev swp1 weight 1
         nexthop via 192.0.2.2  dev swp2 weight 1
    198.51.100.0/24 dev swp3  proto kernel  scope link  src 198.51.100.1
    198.51.100.10/24 dev swp4  proto kernel  scope link  src 198.51.100.11
    198.51.100.20/24 dev br0  proto kernel  scope link  src 198.51.100.21

### <span>Applying a Route Map for Route Updates</span>

To apply a [route
map](http://www.nongnu.org/quagga/docs/docs-multi/Route-Map.html#Route-Map)
to filter route updates from Zebra into the Linux kernel:

    cumulus@switch:$ net add ip protocol static route-map <route-map-name>

## <span>Configuring a Gateway or Default Route</span>

On each switch, it's a good idea to create a *gateway* or *default
route* for traffic destined outside the switch's subnet, or local
network. All such traffic passes through the gateway, which is a host on
the same network that routes packets to their destination beyond the
local network.

In the following example, you create a default route in the routing
table — 0.0.0.0/0 — which indicates any IP address can get sent to the
gateway, which is another switch with the IP address 10.1.0.1.

    cumulus@switch:~$ net add routing route 0.0.0.0/0 10.1.0.1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

## <span>Supported Route Table Entries</span>

Cumulus Linux — via `switchd` — advertises the maximum number of route
table entries that are supported on a given switch architecture,
including:

  - L3 IPv4 LPM (longest prefix match) entries, which have a mask that
    is less than /32

  - L3 IPv6 LPM entries, which have a mask that is /64 or less

  - L3 IPv6 LPM entries, which have a mask that is greater than /64

  - L3 IPv4 neighbor (or host) entries, which are the next hops seen in
    `ip neighbor`

  - L3 IPv6 neighbor entries, which are the next hops seen in `ip -6
    neighbor`

  - ECMP next hops, which are IP address entries in a router's routing
    table that specify the next closest/most optimal router in its
    routing path

  - MAC addresses

In addition, switches on the Tomahawk, Trident II+ and Trident II
platforms are configured to manage route table entries using Algorithm
Longest Prefix Match (ALPM). In ALPM mode, the hardware can store
significantly more route entries.

You can use
[`cl-resource-query`](/version/cumulus-linux-343/Monitoring_and_Troubleshooting/Resource_Diagnostics_Using_cl-resource-query)
to determine the current table sizes on a given switch.

### <span id="src-7112651_Routing-uft" class="confluence-anchor-link"></span><span>Forwarding Table Profiles</span>

Mellanox Spectrum and some Broadcom ASICs provide the ability to
configure the allocation of forwarding table resources and mechanisms.
Cumulus Linux provides a number of generalized profiles for the
platforms described below. These profiles work only with layer 2 and
layer 3 unicast forwarding.

Cumulus Linux defines these profiles as *default*, *l* *2-heavy*,
*v4-lpm-heavy* and *v6-lpm-heavy*. Choose the profile that best suits
your network architecture and specify the profile name for the
`forwarding_table.profile` variable in the
`/etc/cumulus/datapath/traffic.conf` file.

    cumulus@switch:~$ cat /etc/cumulus/datapath/traffic.conf | grep forwarding_table -B 4
    # Manage shared forwarding table allocations
    # Valid profiles - 
    # default, l2-heavy, v4-lpm-heavy, v6-lpm-heavy
    #
    forwarding_table.profile = default

After you specify a different profile, [restart
`switchd`](Configuring_switchd.html#src-7112319_Configuringswitchd-restartswitchd)
for the change to take effect. You can see the forwarding table profile
when you run `cl-resource-query`.

{{%notice note%}}

Broadcom ASICs other than Tomahawk and Trident II/Trident II+ support
only the *default* profile.

{{%/notice%}}

{{%notice note%}}

For Broadcom ASICs, the maximum number of IP multicast entries is 8k.

{{%/notice%}}

### <span id="src-7112651_Routing-tcam" class="confluence-anchor-link"></span><span>TCAM Resource Profiles for Mellanox Switches</span>

The Mellanox Spectrum ASIC provides the ability to configure the TCAM
resource allocation, which is shared between IP multicast forwarding
entries and ACL tables. Cumulus Linux provides a number of general
profiles for this platform: *default*, *ipmc-heavy* and *acl-heavy*.
Choose the profile that best suits your network architecture and specify
that profile name in the `tcam_resource.profile` variable in the
`/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf`
file.

    cumulus@switch:~$ cat /usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf | grep -B3 "tcam_resource"
    #TCAM resource forwarding profile
     
     
        1. Valid profiles -
        2. default, ipmc-heavy, acl-heavy, ipmc-max
           tcam_resource.profile = default

After you specify a different profile, [restart
`switchd`](/display/CL34/Configuring+switchd#Configuringswitchd-restartswitchd)
for the change to take effect.

When [nonatomic
updates](Netfilter_-_ACLs.html#src-7112321_Netfilter-ACLs-nonatomic) are
enabled (that is, the `acl.non_atomic_update_mode` is set to *TRUE* in
`/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL
entries for each profile are as follows:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 1500 (IPv6) or 3500 (IPv4) |
| ipmc-heavy | 8500           | 160 (IPv6) or 400 (IPv4)   |
| acl-heavy  | 450            | 4000 (IPv6) or 8000 (IPv4) |
| ipmc-max   | 13000          | 160 (IPv6) or 400 (IPv4)   |

When [nonatomic
updates](Netfilter_-_ACLs.html#src-7112321_Netfilter-ACLs-nonatomic) are
disabled (that is, the `acl.non_atomic_update_mode` is set to *FALSE* in
`/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL
entries for each profile are as follows:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 750 (IPv6) or 1750 (IPv4)  |
| ipmc-heavy | 8500           | 80 (IPv6) or 200 (IPv4)    |
| acl-heavy  | 450            | 2000 (IPv6) or 4000 (IPv4) |
| ipmc-max   | 13000          | 80 (IPv6) or 200 (IPv4)    |

### <span>Number of Supported Route Entries, by Platform</span>

The following tables list the number of MAC addresses, layer 3 neighbors
and LPM routes validated for each forwarding table profile for the
various supported platforms. If you are not specifying any profiles as
described above, the *default* values are the ones that the switch will
use.

{{%notice tip%}}

The values in the following tables reflect results from our testing on
the different platforms we support, and may differ from published
manufacturers' specifications provided about these chipsets.

{{%/notice%}}

#### <span>Mellanox Spectrum Switches</span>

| Profile        | MAC Addresses | L3 Neighbors              | Longest Prefix Match (LPM)     |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 16k (IPv6) | 64k (IPv4) or 28k (IPv6-long)  |
| l2-heavy       | 88k           | 48k (IPv4) and 40k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 180K          | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long) |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 40k           | 8k (IPv4) and 40k (IPv6)  | 8k (IPv4) and 64k (IPv6-long)  |

#### <span>Broadcom Tomahawk Switches</span>

| Profile                    | MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)     |
| -------------------------- | ------------- | ------------ | ------------------------------ |
| default                    | 40k           | 40k          | 64k (IPv4) or 8k (IPv6-long)   |
| l2-heavy                   | 72k           | 72k          | 8k (IPv4) or 2k (IPv6-long)    |
| v4-lpm-heavy, v6-lpm-heavy | 8k            | 8k           | 128k (IPv4) or 20k (IPv6-long) |

#### <span>Broadcom Trident II/Trident II+ Switches</span>

| Profile                    | MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)     |
| -------------------------- | ------------- | ------------ | ------------------------------ |
| default                    | 32k           | 16k          | 128k (IPv4) or 20k (IPv6-long) |
| l2-heavy                   | 160k          | 96k          | 8k (IPv4) or 2k (IPv6-long)    |
| v4-lpm-heavy, v6-lpm-heavy | 32k           | 16k          | 128k (IPv4) or 20k (IPv6-long) |

#### <span>Broadcom Helix4 Switches</span>

Note that Helix4 switches do not have profiles

| MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)    |
| ------------- | ------------ | ----------------------------- |
| 24k           | 12k          | 7.8k (IPv4) or 2k (IPv6-long) |

## <span>Caveats and Errata</span>

### <span>Don't Delete Routes via Linux Shell</span>

Static routes added via FRRouting can be deleted via Linux shell. This
operation, while possible, should be avoided. Routes added by FRRouting
should only be deleted by FRRouting, otherwise FRRouting might not be
able to clean up all its internal state completely and incorrect routing
can occur as a result.

### <span>Adding IPv6 Default Route with src Address on eth0 Fails without Adding Delay</span>

Attempting to install an IPv6 default route on eth0 with a source
address fails at reboot or when running `ifup` on eth0.

The first execution of `ifup -dv` returns this warning and does not
install the route:

    cumulus@switch:~$ sudo ifup -dv eth0
    warning: eth0: post-up cmd '/sbin/ip route add default via 2001:620:5ca1:160::1 /
    src 2001:620:5ca1:160::45 dev eth0' failed (RTNETLINK answers: Invalid argument)<<<<<<<<<<

Running `ifup` a second time on eth0 successfully installs the route.

There are two ways you can work around this issue.

  - Add a sleep 2 to the eth0 interface in `/etc/network/interfaces`:
    
        cumulus@switch:~$ net add interface eth0 ipv6 address 2001:620:5ca1:160::45/64 post-up /bin/sleep 2s
        cumulus@switch:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:620:5ca1:160::1 src 2001:620:5ca11:160::45 dev eth0

  - Exclude the `src` parameter to the `ip route add` that causes the
    need for the delay. If the `src` parameter is removed, the route is
    added correctly.
    
        cumulus@switch:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:620:5ca1:160::1 dev eth0
    
        cumulus@switch:~$ ifdown eth0
        Stopping NTP server: ntpd.
        Starting NTP server: ntpd.
        cumulus@switch:~$ ip -6 r s
        cumulus@switch:~$ ifup eth0
        Stopping NTP server: ntpd.
        Starting NTP server: ntpd.
        cumulus@switch:~$ ip -6 r s
        2001:620:5ca1:160::/64 dev eth0  proto kernel  metric 256 
        fe80::/64 dev eth0  proto kernel  metric 256 
        default via 2001:620:5ca1:160::1 dev eth0  metric 1024 

## <span>Related Information</span>

  - [Linux IP - ip route
    command](http://linux-ip.net/html/tools-ip-route.html)

  - [FRRouting docs - static route
    commands](https://frrouting.org/user-guide/Static-Route-Commands.html#Static-Route-Commands)
