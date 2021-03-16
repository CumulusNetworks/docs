---
title: Static Routing
author: NVIDIA
weight: 730
toc: 3
---
You can use static routing if you do not require the complexity of a dynamic routing protocol (such as BGP or OSPF), if you have routes that do not change frequently and for which the destination is only one or two paths away.

With static routing, you configure the switch manually to send traffic with a specific destination prefix to a specific next hop. When the switch receives a packet, it looks up the destination IP address in the routing table and forwards the packet accordingly.

## Configure a Static Route

Static routes are added to the {{<exlink url="https://frrouting.org" text="FRRouting">}} routing table and then the kernel routing table.

The following example commands configure Cumulus Linux to send traffic with the destination prefix 10.10.10.101/32 out swp51 (10.0.1.1/31) to the next hop 10.0.1.0.

{{< img src="/images/cumulus-linux/static-routing.png" width="300" >}}

{{< tabs "TabID17 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set interface swp1 ip address 10.0.1.1/31
cumulus@leaf01:~$ cl set vrf default router static 10.10.10.101/32 via 10.0.1.0
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add interface swp51 ip address 10.0.1.1/31
cumulus@leaf01:~$ net add routing route 10.10.10.101/32 10.0.1.0
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

Edit the `/etc/network/interfaces` file to configure an IP address for the interface on the switch that sends out traffic. For example:

```
cumulus@leaf01:~$ sudo nano /etc/network/interfaces
...
auto swp51
iface swp51
    address 10.0.1.1/31
...
```

Run `vtysh` commands to configure the static route (the destination prefix and next hop). For example:

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# ip route 10.10.10.101/32 10.0.1.0
leaf01(config)# exit
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The commands save the static route configuration in the `/etc/frr/frr.conf` file. For example:

```
...
!
ip route 10.10.10.101/32 10.0.1.0
!
...
```

{{< /tab >}}
{{< /tabs >}}

The following example commands configure Cumulus Linux to send traffic with the destination prefix 10.10.10.61/32 out swp3 (10.0.0.32/31) to the next hop 10.0.0.33 in vrf BLUE.

{{< img src="/images/cumulus-linux/static-vrf-example.png" width="400" >}}

{{< tabs "TabID76 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@border01:~$ cl set interface swp3 ip address 10.0.0.32/31
cumulus@border01:~$ cl set interface swp3 ip vrf BLUE
cumulus@border01:~$ cl set vrf BLUE router static 10.10.10.61/32 via 10.0.0.33
cumulus@border01:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@border01:~$ net add interface swp3 ip address 10.0.0.32/31
cumulus@border01:~$ net add interface swp51 vrf BLUE
cumulus@border01:~$ net add routing route 10.10.10.61/32 10.0.0.33 vrf BLUE
cumulus@border01:~$ net pending
cumulus@border01:~$ net commit
```

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

Edit the `/etc/network/interfaces` file to configure an IP address for the interface on the switch that sends out traffic. For example:

```
cumulus@border01:~$ sudo nano /etc/network/interfaces
...
auto swp3
iface swp3
    address 10.0.0.32/31
    vrf BLUE
...
```

Run `vtysh` commands to configure the static route (the destination prefix and next hop). For example:

```
cumulus@border01:~$ sudo vtysh

border01# configure terminal
border01(config)# ip route 10.10.10.61/32 10.0.0.33 vrf BLUE
border01(config)# exit
border01# write memory
border01# exit
cumulus@border01:~$
```

The commands save the static route configuration in the `/etc/frr/frr.conf` file. For example:

```
...
vrf BLUE
 ip route 10.10.10.61/32 10.0.0.33
...
```

{{< /tab >}}
{{< /tabs >}}

To delete a static route:

{{< tabs "TabID58 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl unset vrf default router static 10.10.10.101/32 via 10.0.1.0
cumulus@leaf01:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net del routing route 10.10.10.101/32 10.0.1.0
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{%notice tip%}}
When you use NCLU commands to delete routing configuration such as static routes, commit ten or fewer delete commands at a time to avoid commit failures.
{{%/notice%}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# no ip route 10.10.10.101/32 10.0.1.0
leaf01(config)# exit
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}
{{< /tabs >}}

To view static routes, run the NCLU `net show route static` command or the vtysh `show ip route` command. For example:

```
cumulus@leaf01:mgmt:~$ net show route static
RIB entry for static
====================
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route

S>* 10.10.10.101/32 [1/0] via 10.0.1.0, swp51, weight 1, 00:02:07
```

You can also create a static route by adding the route to a switch port configuration. For example:

{{< tabs "TabID187 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add interface swp51 ip address 10.0.1.1/31
cumulus@leaf01:~$ net add interface swp51 post-up ip route add 10.10.10.101/32 via 10.0.1.0
cumulus@leaf01:~$ net add interface swp51 post-down ip route del 10.10.10.101/32 via 10.0.1.0
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file and add the following `post-up` and `post-down` lines to the interface stanza:

```
cumulus@leaf01:~$  sudo nano /etc/network/interfaces
...
auto swp51
iface swp51
    address 10.0.1.1/31
    post-up ip route add 10.10.10.101/32 via 10.0.1.0
    post-down ip route del 10.10.10.101/32 via 10.0.1.0
```

The `ip route` command allows you to manipulate the kernel routing table directly from the Linux shell. See `man ip(8)` for details. FRRouting monitors the kernel routing table changes and updates its own routing table accordingly.

{{< /tab >}}
{{< /tabs >}}

## Configure a Gateway or Default Route

On each switch, consider creating a *gateway* or *default route* for traffic destined outside the switch's subnet or local network. All such traffic passes through the gateway, which is a system on the same network that routes packets to their destination beyond the local network.

The following example configures the default route 0.0.0.0/0, which indicates any IP address can be sent to the gateway. The gateway is another switch with the IP address 10.0.1.0.

{{< tabs "TabID310 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@leaf01:~$ cl set vrf default router static 0.0.0.0/0 via 10.0.1.0
cumulus@leaf01:~$ cl config apply
```

{{%notice note%}}
Instead of 0.0.0.0/0, you can specify `default` or `default6`.
{{%/notice%}}

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@leaf01:~$ net add routing route 0.0.0.0/0 10.0.1.0
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# ip route 0.0.0.0/0 10.0.1.0
leaf01(config)# exit
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
!
ip route 0.0.0.0/0 10.0.1.0
!
...
```

{{%notice note%}}
The default route created by the `gateway` parameter in ifupdown2 is not installed in FRR and cannot be redistributed into other routing protocols. See {{<link url="Interface-Configuration-and-Management#ifupdown2-and-the-gateway-parameter" text="ifupdown2 and the gateway Parameter" >}} for more information.
{{%/notice%}}

{{< /tab >}}
{{< /tabs >}}

## Considerations

### Deleting Routes through the Linux Shell

To avoid incorrect routing, **do not** use the Linux shell to delete static routes that you added with `vtysh` commands. Delete the routes with the `vtysh` commands.

### IPv6 Default Route with a Source IP Address on eth0

If you install an IPv6 default route on eth0 with a source IP address, the configuration either fails at reboot or the first time you run `ifup -dv eth0`, you see a warning and the route is not installed. (If you run `ifup -dv eth0` a second time, the route is installed successfully.)

```
cumulus@leaf01:~$ sudo ifup -dv eth0
warning: eth0: post-up cmd '/sbin/ip route add default via 2001:db8:5ca1:160::1 /
src 2001:db8:5ca1:160::45 dev eth0' failed (RTNETLINK answers: Invalid argument)<<<<<<<<<<
```

To avoid this issue, you can do one of the following:

- Add a delay to the eth0 interface:

   ```
   cumulus@leaf01:~$ net add interface eth0 ipv6 address 2001:db8:5ca1:160::45/64 post-up /bin/sleep 2s
   cumulus@leaf01:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:db8:5ca1:160::1 src 2001:db8:5ca11:160::45 dev eth0
   cumulus@leaf01:~$ net pending
   cumulus@leaf01:~$ net commit
   ```

- Exclude the `src` parameter with the `ip route add` command:

   ```
   cumulus@leaf01:~$ net add interface eth0 ipv6 address 2001:db8:5ca1:160::45/64 post-up
   cumulus@leaf01:~$ net add interface eth0 post-up /sbin/ip route add default via 2001:db8:5ca1:160::1 dev eth0
   cumulus@leaf01:~$ net pending
   cumulus@leaf01:~$ net commit
   ```

### IPv4 and IPv6 Neighbor Cache Aging Timer

Cumulus Linux does not support different neighbor cache aging timer settings for IPv4 and IPv6.

The `net.ipv4.neigh.default.base_reachable_time_ms` and `net.ipv6.neigh.default.base_reachable_time_ms` settings in the `/etc/sysctl.d/neigh.conf` file must have the same value:

```
cumulus@leaf01:~$ sudo cat /etc/sysctl.d/neigh.conf
...
net.ipv4.neigh.default.base_reachable_time_ms=1080000
net.ipv6.neigh.default.base_reachable_time_ms=1080000
...
```

## Related Information

- {{<exlink url="http://linux-ip.net/html/tools-ip-route.html" text="Linux IP - ip route command">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/static.html#static-route-commands" text="FRRouting docs - static route commands">}}
