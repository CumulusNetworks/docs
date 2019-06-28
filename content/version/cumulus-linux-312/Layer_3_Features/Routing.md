---
title: Routing
author: Cumulus Networks
weight: 129
aliases:
 - /display/CL31/Routing
 - /pages/viewpage.action?pageId=5122117
pageID: 5122117
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
This chapter discusses routing on switches running Cumulus Linux.

## <span>Commands</span>

  - ip route

## <span>Static Routing via ip route</span>

A static route can be persistently added by adding `up ip route add ..`
into `/etc/network/interfaces`. For example:

    cumulus@switch:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
     
    auto swp3
    iface swp3
        address 198.51.100.1/24
        up ip route add 203.0.113.0/24 via 198.51.100.2

{{%notice tip%}}

Notice the simpler configuration of swp3 due to `ifupdown2`. For more
information, see [Configuring and Managing Network
Interfaces](/version/cumulus-linux-312/Configuring_and_Managing_Network_Interfaces/).

{{%/notice%}}

{{%notice note%}}

If an IPv6 address is assigned to a DOWN interface, the associated route
is still installed into the routing table. The type of IPv6 address
doesn't matter: link local, site local and global all exhibit the same
problem.

If the interface is bounced up and down, then the routes are no longer
in the route table.

{{%/notice%}}

The `ip route` command allows manipulating the kernel routing table
directly from the Linux shell. See `man ip(8)` for details. `quagga`
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

Runtime configuration (Advanced)

{{%notice warning%}}

A runtime configuration does not persist across reboots of the switch.

{{%/notice%}}

To add a static route:

    cumulus@switch:~$ sudo ip route add 203.0.113.0/24 via 198.51.100.2
    cumulus@switch:~$ ip route
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
    203.0.113.0/24 via 198.51.100.2 dev swp3

To delete a static route:

    cumulus@switch:~$ sudo ip route del 203.0.113.0/24
    cumulus@switch:~$ ip route
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

## <span>Static Routing via Quagga</span>

You can also manage static routes via `vtysh`, the Quagga CLI. The
routes are added to the `quagga` routing table, and then will be updated
into the kernel routing table as well.

However, creating routes in this manner is non-persistent, so they do
not remain after you reboot the switch. To save the running
configuration so it persists between reboots, run `write mem` in the
`vtysh` CLI:

    switch# write mem
    Configuration saved to /etc/quagga/zebra.conf
    switch# end

To add a static route in Quagga (does not persist across reboot):

    cumulus@switch:~$ sudo vtysh
     
    Hello, this is Quagga (version 0.99.23.1+cl3.0).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
     
    switch# conf t
    switch(config)# ip route 203.0.113.0/24 198.51.100.2
    switch(config)# end
    switch# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
     
    K>* 0.0.0.0/0 via 10.0.1.2, eth0
    C>* 10.0.1.0/24 is directly connected, eth0
    O   192.0.2.0/24 [110/10] is directly connected, swp1, 00:13:25
    C>* 192.0.2.0/24 is directly connected, swp1
    O>* 192.0.2.10/24 [110/20] via 192.0.2.1, swp1, 00:13:09
    O>* 192.0.2.20/24 [110/20] via 192.0.2.1, swp1, 00:13:09
      *                      via 192.0.2.41, swp2, 00:13:09
    O>* 192.0.2.30/24 [110/20] via 192.0.2.1, swp1, 00:13:09
    O   192.0.2.40/24 [110/10] is directly connected, swp2, 00:13:25
    C>* 192.0.2.40/24 is directly connected, swp2
    O>* 192.0.2.50/24 [110/20] via 192.0.2.41, swp2, 00:13:09
    O>* 192.0.2.60/24 [110/20] via 192.0.2.41, swp2, 00:13:09
    O>* 192.0.2.70/24 [110/30] via 192.0.2.1, swp1, 00:13:09
      *                      via 192.0.2.41, swp2, 00:13:09
    O   198.51.100.0/24 [110/10] is directly connected, swp3, 00:13:22
    C>* 198.51.100.0/24 is directly connected, swp3
    O   198.51.100.10/24 [110/10] is directly connected, swp4, 00:13:22
    C>* 198.51.100.10/24 is directly connected, swp4
    O   198.51.100.20/24 [110/10] is directly connected, br0, 00:13:22
    C>* 198.51.100.20/24 is directly connected, br0
    S>* 203.0.113.0/24 [1/0] via 198.51.100.2, swp3
    C>* 127.0.0.0/8 is directly connected, lo

To delete a static route in Quagga (does not persist across reboot):

    cumulus@switch:~$ sudo vtysh
     
    Hello, this is Quagga (version 0.99.23.1+cl3.0).
    Copyright 1996-2005 Kunihiro Ishiguro, et al.
     
    switch# conf t
    switch(config)# no ip route 203.0.113.0/24 198.51.100.2
    switch(config)# end
    switch# show ip route
    Codes: K - kernel route, C - connected, S - static, R - RIP,
           O - OSPF, I - IS-IS, B - BGP, A - Babel,
           > - selected route, * - FIB route
     
    K>* 0.0.0.0/0 via 10.0.1.2, eth0
    C>* 10.0.1.0/24 is directly connected, eth0
    O   192.0.2.0/24 [110/10] is directly connected, swp1, 00:13:55
    C>* 192.0.2.0/24 is directly connected, swp1
    O>* 192.0.2.10/24 [110/20] via 11.0.0.1, swp1, 00:13:39
    O>* 192.0.2.20/24 [110/20] via 11.0.0.1, swp1, 00:13:39
      *                      via 11.0.4.1, swp2, 00:13:39
    O>* 192.0.2.30/24 [110/20] via 11.0.0.1, swp1, 00:13:39
    O   192.0.2.40/24 [110/10] is directly connected, swp2, 00:13:55
    C>* 192.0.2.40/24 is directly connected, swp2
    O>* 192.0.2.50/24 [110/20] via 11.0.4.1, swp2, 00:13:39
    O>* 192.0.2.60/24 [110/20] via 11.0.4.1, swp2, 00:13:39
    O>* 192.0.2.70/24 [110/30] via 11.0.0.1, swp1, 00:13:39
      *                      via 11.0.4.1, swp2, 00:13:39
    O   198.51.100.0/24 [110/10] is directly connected, swp3, 00:13:52
    C>* 198.51.100.0/24 is directly connected, swp3
    O   198.51.100.10/24 [110/10] is directly connected, swp4, 00:13:52
    C>* 198.51.100.10/24 is directly connected, swp4
    O   198.51.100.20/24 [110/10] is directly connected, br0, 00:13:52
    C>* 198.51.100.20/24 is directly connected, br0
    C>* 127.0.0.0/8 is directly connected, lo
    switch#

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
[`cl-resource-query`](/version/cumulus-linux-312/Monitoring_and_Troubleshooting/Resource_Diagnostics_Using_cl-resource-query)
to determine the current table sizes on a given switch.

### <span id="src-5122117_Routing-uft" class="confluence-anchor-link"></span><span>Forwarding Table Profiles</span>

Mellanox Spectrum and some Broadcom ASICs provide the ability to
configure the allocation of forwarding table resources and mechanisms.
Cumulus Linux 3.1.0 provides a number of generalized profiles for the
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
`switchd`](Configuring_switchd.html#src-5121932_Configuringswitchd-restartswitchd)
for the change to take effect. You can see the forwarding table profile
when you run `cl-resource-query`.

{{%notice note%}}

Broadcom chips other than Tomahawk and Trident II/Trident II+ support
only the *default* profile.

{{%/notice%}}

### <span>Number of Supported Route Entries, by Platform</span>

The following tables list the number of MAC addresses, layer 3 neighbors
and LPM routes validated for each forwarding table profile for the
various supported platforms. If you are not specifying any profiles as
described above, the *default* values are the ones that the switch will
use.

#### <span>Mellanox Spectrum Switches</span>

| Profile        | MAC Addresses | L3 Neighbors              | Longest Prefix Match (LPM)     |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 8k (IPv6)  | 64k (IPv4) or 8k (IPv6-long)   |
| l2-heavy       | 72k           | 32k (IPv4) and 24k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 8k (IPv6)   | 80k (IPv4) and 8k (IPv6-long)  |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 128k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 8k            | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 40k (IPv6-long)  |

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

## <span>Configuration Files</span>

  - /etc/cumulus/datapath/traffic.conf

  - /etc/network/interfaces

  - /etc/quagga/zebra.conf

## <span>Useful Links</span>

  - [linux-ip.net/html/tools-ip-route.html](http://linux-ip.net/html/tools-ip-route.html)

  - [www.nongnu.org/quagga/docs/docs-info.html\#Static-Route-Commands](http://www.nongnu.org/quagga/docs/docs-info.html#Static-Route-Commands)

## <span>Caveats and Errata</span>

### <span>Don't Delete Routes via Linux Shell</span>

Static routes added via Quagga can be deleted via Linux shell. This
operation, while possible, should be avoided. Routes added by Quagga
should only be deleted by Quagga, otherwise Quagga might not be able to
clean up all its internal state completely and incorrect routing can
occur as a result.

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

  - Add a sleep 2 to the eth0 stanza in `/etc/network/interfaces`:
    
        iface eth0 inet6 static
            address 2001:620:5ca1:160::45/64
            post-up /bin/sleep 2s
            post-up /sbin/ip route add default via 2001:620:5ca1:160::1 src 2001:620:5ca11
        :160::45 dev eth0

  - Exclude the `src` parameter to the `ip route add` that causes the
    need for the delay. If the `src` parameter is removed, the route is
    added correctly.
    
        iface eth0 inet6 static
            address 2001:620:5ca1:160::45/64
           post-up /sbin/ip route add default via 2001:620:5ca1:160::1 dev eth0
    
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
