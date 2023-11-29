---
title: Routing
author: NVIDIA
weight: 720
toc: 3
---
This chapter discusses routing on switches running Cumulus Linux.

## Manage Static Routes

Static routes are added to the {{<exlink url="https://frrouting.org" text="FRRouting">}} routing table and then the kernel routing table.

To add static routes:

{{< tabs "TabID0" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add routing route 203.0.113.0/24 198.51.100.2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip route 203.0.113.0/24 198.51.100.2
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
!
ip route 203.0.113.0/24 198.51.100.2
!
...
```

To delete a static route:

{{< tabs "TabID2" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net del routing route 203.0.113.0/24 198.51.100.2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# no ip route 203.0.113.0/24 198.51.100.2
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

To view static routes, run the NCLU `net show route static` command or the vtysh `show ip route` command. For example:

```
cumulus@switch:~$ net show route static 
RIB entry for static
====================
Codes: K - kernel route, C - connected, S - static, R - RIP,
        O - OSPF, I - IS-IS, B - BGP, P - PIM, T - Table,
        > - selected route, * - FIB route
 S>* 203.0.113.0/24 [1/0] via 198.51.100.2, swp3
```

### Static Multicast Routes

To add a static multicast route (mroute):

{{< tabs "TabID4" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add routing mroute 230.0.0.0/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip mroute 203.0.0.0/24
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
!
ip mroute 230.0.0.0/24
!
...
```

To delete an mroute:

{{< tabs "TabID6" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net del routing mroute 230.0.0.0/24
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# no ip mroute 203.0.0.0/24
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

To view mroutes, run the following command from the `vtysh` shell:

```
cumulus@switch:~$ sudo vtysh
switch# show ip rpf 230.0.0.0
Routing entry for 230.0.0.0/24 using Multicast RIB
  Known via "static", distance 1, metric 0, best
  * directly connected, swp31s0
```

### Static Routing via ip route

You can also create a static route by adding the route to a switch port configuration. For example:

{{< tabs "TabID8" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add interface swp3 ip address 198.51.100.1/24
cumulus@switch:~$ net add interface swp3 post-up routing route add 203.0.113.0/24 via 198.51.100.2
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp3
switch(config-if)# post-up ip route 203.0.113.0/24 198.51.100.2
switch(config-if)# exit
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/network/interfaces` file. For example:

```
...
auto swp3
iface swp3
    address 198.51.100.1/24
    post-up ip route add 203.0.113.0/24 via 198.51.100.2
...
```

The `ip route` command allows you to manipulate the kernel routing table directly from the Linux shell. See `man ip(8)` for details. FRRouting monitors the kernel routing table changes and updates its own routing table accordingly.

To display the routing table:

```
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
```

### Apply a Route Map for Route Updates

To apply a {{<exlink url="http://docs.frrouting.org/en/latest/routemap.html" text="route map">}} to filter route updates from Zebra into the Linux kernel:

{{< tabs "TabID10" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add routing protocol static route-map myroutemap
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip protocol static route-map myroutemap
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
!
ip protocol static route-map myroutemap
!
...
```

## Configure a Gateway or Default Route

Consider creating a *gateway* or *default route* on each switch for traffic destined outside the switch's subnet or local network. All such traffic passes through the gateway, which is a host on the same network that routes packets to their destination beyond the local network.

In the following example, you create a default route in the routing table 0.0.0.0/0, which indicates any IP address can be sent to the gateway, which is another switch with the IP address 10.1.0.1.

{{< tabs "TabID12" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add routing route 0.0.0.0/0 10.1.0.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip route 0.0.0.0/0 10.1.0.1
switch(config)# exit
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
!
ip route 0.0.0.0/0 10.1.0.1
!
...
```

## Supported Route Table Entries

Cumulus Linux (via `switchd)`advertises the maximum number of route table entries that are supported on a given switch architecture, including:

- Layer 3 IPv4 LPM (longest prefix match) entries that have a mask less than /32
- Layer 3 IPv6 LPM entries that have a mask of /64 or less
- Layer 3 IPv6 LPM entries that have a mask greater than /64
- Layer 3 IPv4 neighbor (or host) entries that are the next hops seen in `ip neighbor`
- Layer 3 IPv6 neighbor entries that are the next hops seen in `ip -6 neighbor`
- ECMP next hops, which are IP address entries in a router's routing table that specify the next closest/most optimal router in its routing path
- MAC addresses

In addition, switches on the Tomahawk, Trident II, Trident II+, and Trident3 platforms are configured to manage route table entries using Algorithm Longest Prefix Match (ALPM). In ALPM mode, the hardware can store significantly more route entries.

You can use `{{<link url="Resource-Diagnostics-Using-cl-resource-query" text="cl-resource-query">}}` to determine the current table sizes on a given switch.

### Forwarding Table Profiles

On Mellanox Spectrum and some Broadcom ASICs, you can configure the allocation of forwarding table resources and mechanisms. Cumulus Linux provides a number of generalized profiles for the platforms described below. These profiles work only with layer 2 and layer 3 unicast forwarding.

Cumulus Linux defines these profiles as *default*, *l* *2-heavy*, *v4-lpm-heavy* and *v6-lpm-heavy*. Choose the profile that best suits your network architecture and specify the profile name for the `forwarding_table.profile` variable in the `/etc/cumulus/datapath/traffic.conf` file.

```
cumulus@switch:~$ cat /etc/cumulus/datapath/traffic.conf | grep forwarding_table -B 4
# Manage shared forwarding table allocations
# Valid profiles -
# default, l2-heavy, v4-lpm-heavy, v6-lpm-heavy
#
forwarding_table.profile = default
```

After you specify a different profile, {{%link url="Configuring-switchd#restart-switchd" text="restart `switchd`"%}} for the change to take effect. You can see the forwarding table profile when you run `cl-resource-query`.

{{%notice note%}}

Broadcom ASICs other than Maverick, Tomahawk/Tomahawk+, Trident II, Trident II+, and Trident3 support only the *default* profile.

{{%/notice%}}

{{%notice note%}}

For Broadcom ASICs, the maximum number of IP multicast entries is 8k.

{{%/notice%}}

### Number of Supported Route Entries By Platform

The following tables list the number of MAC addresses, layer 3 neighbors, and LPM routes validated for each forwarding table profile for the various supported platforms. If you do not specify any profiles as described above, the *default* values are the ones that the switch will use.

{{%notice tip%}}

The values in the following tables reflect results from testing on the different platforms that support Cumulus Linux, which might differ from published manufacturer specifications.

{{%/notice%}}

#### Mellanox Spectrum Switches

| <div style="width:100px">Profile| MAC Addresses | <div style="width:190px">L3 Neighbors| Longest Prefix Match (LPM)  |
| -------------- | ------------- | ------------------------- | ------------------------------ |
| default        | 40k           | 32k (IPv4) and 16k (IPv6) | 64k (IPv4) and 28k (IPv6-long) |
| l2-heavy       | 88k           | 48k (IPv4) and 40k (IPv6) | 8k (IPv4) and 8k (IPv6-long)   |
| l2-heavy-1     | 180K          | 8k (IPv4) and 8k (IPv6)   | 8k (IPv4) and 8k (IPv6-long)   |
| v4-lpm-heavy   | 8k            | 8k (IPv4) and 16k (IPv6)  | 80k (IPv4) and 16k (IPv6-long) |
| v4-lpm-heavy-1 | 8k            | 8k (IPv4) and 2k (IPv6)   | 176k (IPv4) and 2k (IPv6-long) |
| v6-lpm-heavy   | 40k           | 8k (IPv4) and 40k (IPv6)  | 8k (IPv4) and 32k (IPv6-long) and 32K (IPv6/64) |
| lpm-balanced   | 8k            | 8k (IPv4) and 8k (IPv6)   | 60k (IPv4) and 60k (IPv6-long) |

#### Broadcom Tomahawk/Tomahawk+ Switches

| Profile                    | MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)     |
| -------------------------- | ------------- | ------------ | ------------------------------ |
| default                    | 40k           | 40k          | 64k (IPv4) or 8k (IPv6-long)   |
| l2-heavy                   | 72k           | 72k          | 8k (IPv4) or 2k (IPv6-long)    |
| v4-lpm-heavy, v6-lpm-heavy | 8k            | 8k           | 128k (IPv4) or 20k (IPv6-long) |

#### Broadcom Trident II/Trident II+/Trident3 Switches

| Profile                    | MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)     |
| -------------------------- | ------------- | ------------ | ------------------------------ |
| default                    | 32k           | 16k          | 128k (IPv4) or 20k (IPv6-long) |
| l2-heavy                   | 160k          | 96k          | 8k (IPv4) or 2k (IPv6-long)    |
| v4-lpm-heavy, v6-lpm-heavy | 32k           | 16k          | 128k (IPv4) or 20k (IPv6-long) |

#### Broadcom Helix4 Switches

Helix4 switches do *not* have profiles.

| MAC Addresses | L3 Neighbors | Longest Prefix Match (LPM)    |
| ------------- | ------------ | ----------------------------- |
| 24k           | 12k          | 7.8k (IPv4) or 2k (IPv6-long) |

{{%notice note%}}

For Broadcom switches, IPv4 and IPv6 entries are not carved in separate spaces so it is not possible to define explicit numbers in the L3 Neighbors column of the tables shown above. An IPv6 entry takes up twice the space of an IPv4 entry.

{{%/notice%}}

### TCAM Resource Profiles for Spectrum Switches

On the Mellanox Spectrum ASIC, you can configure TCAM resource allocation, which is shared between IP multicast forwarding entries and ACL tables. Cumulus Linux provides a number of general profiles for this platform: *default*, *ipmc-heavy* and *acl-heavy*. Choose the profile that best suits your network architecture and specify that profile name in the `tcam_resource.profile` variable in the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf` file.

```
cumulus@switch:~$ cat /usr/lib/python2.7/dist-packages/cumulus/__chip_config/mlx/datapath.conf | grep -B3 "tcam_resource"
#TCAM resource forwarding profile

    1. Valid profiles -
    2. default, ipmc-heavy, acl-heavy, ipmc-max
       tcam_resource.profile = default
```

After you specify a different profile, {{%link url="Configuring-switchd#restart-switchd" text="restart `switchd`"%}} for the change to take effect.

When {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="nonatomic updates">}} are enabled (`acl.non_atomic_update_mode` is set to `TRUE` in the `/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL entries for each profile are:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 500 (IPv6) or 1000 (IPv4)  |
| ipmc-heavy | 8500           | 1000 (IPv6) or 1500 (IPv4) |
| acl-heavy  | 450            | 2000 (IPv6) or 3500 (IPv4) |
| ipmc-max   | 13000          | 1000 (IPv6) or 2000 (IPv4) |

When {{<link url="Netfilter-ACLs#nonatomic-update-mode-and-atomic-update-mode" text="nonatomic updates">}} are disabled (`acl.non_atomic_update_mode` is set to `FALSE` in the `/etc/cumulus/switchd.conf` file), the maximum number of mroute and ACL entries for each profile are:

| Profile    | Mroute Entries | ACL Entries                |
| ---------- | -------------- | -------------------------- |
| default    | 1000           | 250 (IPv6) or 500 (IPv4)   |
| ipmc-heavy | 8500           | 500 (IPv6) or 750 (IPv4)   |
| acl-heavy  | 450            | 1000 (IPv6) or 1750 (IPv4) |
| ipmc-max   | 13000          | 500 (IPv6) or 1000 (IPv4)  |

## Route Entry Takes Precedence Over Neighbor Entry

On Broadcom switches with Cumulus Linux 4.0 and later, when there is a /32 IPv4 or /128 IPv6 route and the same prefix is also a neighbor entry in the linux kernel, the route entry takes precedence over the neighbor entry in the forwarding lookup. To change this behavior, update the `route_preferred_over_neigh` variable to FALSE in the `/etc/cumulus/switchd.conf` file.

## Caveats and Errata

### Do Not Delete Routes through Linux Shell

**Do not** use the Linux shell to delete static routes added via FRRouting (with `vtysh` commands). Delete the routes with the `vtysh` commands; otherwise FRRouting might not be able to clean up its internal state completely, which can result in incorrect routing.

### Using NCLU Commands to Delete Routing Configuration

When you use NCLU commands to delete routing (FRR) configuration, such as static routes or route map rules  (multiples of which can exist in a configuration), commit ten or fewer delete commands at a time to avoid commit failures.

### Add IPv6 Default Route with src Address on eth0 Fails without Adding Delay

Attempting to install an IPv6 default route on eth0 with a source address fails at reboot or when running `ifup` on eth0.

The first execution of `ifup -dv` returns this warning and does not install the route:

```
cumulus@switch:~$ sudo ifup -dv eth0
warning: eth0: post-up cmd '/sbin/ip route add default via 2001:620:5ca1:160::1 /
src 2001:620:5ca1:160::45 dev eth0' failed (RTNETLINK answers: Invalid argument)<<<<<<<<<<
```

Running `ifup` a second time on eth0 successfully installs the route.

To work around this issue, either add a two second delay or exclude the `src` parameter to the `ip route add` that causes the need for the delay:

- Add a delay to the eth0 interface:

```
cumulus@switch:~$ net add interface eth0 ipv6 address 2001:620:5ca1:160::45/64 post-up /bin/sleep 2s
cumulus@switch:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:620:5ca1:160::1 src 2001:620:5ca11:160::45 dev eth0
```

- Exclude the `src` parameter to the `ip route add` that causes the need for the delay. If the `src` parameter is removed, the route is added correctly.

```
cumulus@switch:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:620:5ca1:160::1 dev eth0
```

```
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
```

### Use the Same Neighbor Cache Aging Timer for IPv4 and IPv6

Cumulus Linux does not support different neighbor cache aging timer settings for IPv4 and IPv6.

For example, see the two settings for `neigh.default.base_reachable_time_ms` in `/etc/sysctl.d/neigh.conf`:

```
cumulus@switch:~$ sudo cat /etc/sysctl.d/neigh.conf

...

net.ipv4.neigh.default.base_reachable_time_ms=1080000
net.ipv6.neigh.default.base_reachable_time_ms=1080000

...
```

## Related Information

- {{<exlink url="http://linux-ip.net/html/tools-ip-route.html" text="Linux IP - ip route command">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/static.html#static-route-commands" text="FRRouting docs - static route commands">}}
