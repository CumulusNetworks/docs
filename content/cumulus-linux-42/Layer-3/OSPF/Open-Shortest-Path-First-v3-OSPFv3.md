---
title: Open Shortest Path First v3 - OSPFv3
author: Cumulus Networks
weight: 800
toc: 3
---
OSPFv3 is a revised version of OSPFv2 and supports the IPv6 address family. Refer to {{<link url="Open-Shortest-Path-First-OSPF">}} for a discussion on the basic concepts, which remain the same between the two versions.

OSPFv3 has changed the formatting in some of the packets and LSAs to support IPv6 and to improve the protocol behavior. OSPFv3 defines a new LSA, called intra-area prefix LSA, to separate the advertisement of stub networks attached to a router from the router LSA. It is a clear separation of node topology from prefix reachability and lends itself well to an optimized SPF computation.

{{%notice note%}}

IETF has defined extensions to OSPFv3 to support multiple address families (both IPv6 and IPv4). {{<link url="FRRouting" text="FRR">}} does not currently support multiple address families.

{{%/notice%}}

## Configure OSPFv3

### OSPFv3 Numbered

To configure OSPFv3 using numbered interfaces, you specify the router ID, IP subnet prefix, and area address. All the interfaces on the switch with an IP address that matches the `network` subnet are put into the specified area. The OSPF process starts bringing up peering adjacency on those interfaces. It also advertises the interface IP addresses formatted into LSAs to the neighbors for proper reachability.

If you do not want to bring up OSPF adjacency on certain interfaces, you can configure the interfaces as *passive interfaces*. A passive interface creates a database entry but does not send or recieve OSPF hello packets. For example, in a data center topology, the host-facing interfaces do not need to run OSPF, however, the corresponding IP addresses still need to be advertised to neighbors.

The subnets can be as inclusive as possible to cover the highest number of interfaces on the switch that run OSPF.

The following example commands configure OSPF numbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf3-numbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 2001:db8:0002::0a00:1/128</li><li>The IP address on swp51 is ??????</li><li>The router ID is 2001:db8:0002::0a00:1</li><li>All the interfaces on the switch with an IP address that matches subnet 2001:db8::1/128 and swp51 with IP address ????? are in area 0</li><li>swp1 and swp2 are passive interfaces</li></ul> | <ul><li>The loopback address is 2001:db8:0002::0a00:101/128</li><li>The IP address on swp1 is ??????</li><li>The router ID is 2001:db8:0002::0a00:101</li><li>All interfaces on the switch with an IP address that matches subnet 2001:db8:0002::0a00:101/128 and swp1 with IP address ??????? are in area 0.</li></ul> |

{{< tabs "TabID29 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "TabID49 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 2001:db8:0002::0a00:1/128
cumulus@leaf01:~$ net add interface swp51 ip address ???????
cumulus@leaf01:~$ net add ospf6 router-id 2001:db8:0002::0a00:1
cumulus@leaf01:~$ net add ospf6 network 2001:db8:0002::0a00:1/128 area 0
cumulus@leaf01:~$ net add ospf6 network ?????? area 0
cumulus@leaf01:~$ net add ospf6 passive-interface swp1
cumulus@leaf01:~$ net add ospf6 passive-interface swp2
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

You can use the `net add ospf passive-interface default` command to set all interfaces as *passive* and the `net del ospf passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@leaf01:~$ net add ospf6 passive-interface default
cumulus@leaf01:~$ net del ospf6 passive-interface swp51
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 12001:db8:0002::0a00:101/128
cumulus@spine01:~$ net add interface swp1 ip address ????
cumulus@spine01:~$ net add ospf6 router-id 2001:db8:0002::0a00:101
cumulus@spine01:~$ net add ospf6 network 2001:db8:0002::0a00:101/128 area 0
cumulus@spine01:~$ net add ospf6 network ?????? area 0
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

You can use the `net add ospf passive-interface default` command to set all interfaces as *passive* and the `net del ospf passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@spine01:~$ net add ospf6 passive-interface default
cumulus@spine01:~$ net del ospf6 passive-interface swp1
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "TabID85 ">}}

{{< tab "leaf01 ">}}

1. Enable the `ospf` daemon, then start the FRRouting service. See {{<link url="Configure-FRRouting">}}.

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp51:

  ```
  cumulus@leaf01:~$ sudo nano /etc/network/interfaces
  ...
  auto lo
  iface lo inet loopback
    address 2001:db8:0002::0a00:1/128

  auto swp51
  iface swp51
    address ?????
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@leaf01:~$ sudo vtysh

    leaf01# configure terminal
    leaf01(config)# router ospf6
    leaf01(config-router)# router-id 2001:db8:0002::0a00:1
    leaf01(config-router)# network 2001:db8:0002::0a00:1/128 area 0
    leaf01(config-router)# network ??? area 0
    leaf01(config-router)# passive-interface swp1
    leaf01(config-router)# passive-interface swp2
    leaf01(config-router)# exit
    leaf01(config)# exit
    leaf01# write memory
    leaf01# exit
    cumulus@leaf01:~$
    ```

You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency only on certain interfaces:

```
leaf01(config)# router ospf6
leaf01(config-router)# passive-interface default
leaf01(config-router)# no passive-interface swp51
```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Enable the `ospf` daemon, then start the FRRouting service. See {{<link url="Configure-FRRouting">}}.

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp1:

    ```
    cumulus@leaf01:~$ sudo nano /etc/network/interfaces
    ...
    auto lo
    iface lo inet loopback
      address 2001:db8:0002::0a00:101/128

    auto swp51
    iface swp51
      address ?????
    ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@spine01:~$ sudo vtysh

    spine01# configure terminal
    spine01(config)# router ospf6
    spine01(config-router)# router-id 2001:db8:0002::0a00:101
    spine01(config-router)# network 2001:db8:0002::0a00:101/128 area 0
    spine01(config-router)# network ?????? area 0
    spine01(config-router)# exit
    spine01(config)# exit
    spine01# write memory
    spine01# exit
    cumulus@spine01:~$
    ```

You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency only on certain interfaces:

```
spine01(config)# router ospf6
spine01(config-router)# passive-interface default
spine01(config-router)# no passive-interface swp1
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "TabID208 ">}}

{{< tab "leaf01 ">}}

```
...
router ospf6
 ospf router-id 2001:db8:0002::0a00:1
 network 2001:db8:0002::0a00:1/128 area 0
 network ????? area 0
 passive-interface swp1
 passive-interface swp2
...
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
...
router ospf6
 ospf router-id 2001:db8:0002::0a00:101
 network 2001:db8:0002::0a00:101/128 area 0
 network ???? area 0
...
```

{{< /tab >}}

{{< /tabs >}}

### OSPFv3 Unnumbered

Unnumbered interfaces are interfaces without unique IP addresses; multiple interfaces share the same IP address.

To configure an unnumbered interface, take the IP address of another interface (called the *anchor*) and use that as the IP address of the unnumbered interface. The anchor is typically the loopback interface on the switch.

{{%notice note%}}

OSPFv3 Unnumbered is supported with {{<link url="#interface-options" text="point-to-point interfaces">}} only.

{{%/notice%}}

The following example commands configure OSPFv3 unnumbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf3-unnumbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 2001:db8:0002::0a00:1/128</li><li>The router ID is 2001:db8:0002::0a00:1</li><li>OSPF is enabled on the loopback interface and on swp51 in area 0</li><li>swp1 and swp2 are passive interfaces</li><li>swp51 is a point-to-point interface (point-to-point is required for unnumbered interfaces)</li><ul>|<ul><li>The loopback address is 2001:db8:0002::0a00:101/128</li><li>The router ID is 2001:db8:0002::0a00:101</li><li>OSPF is enabled on the loopback interface and on swp1 in area 0</li><li>swp1 is a point-to-point interface (point-to-point is required for unnumbered interfaces)</li><ul> |

{{< tabs "TabID257 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "TabID261 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 2001:db8:0002::0a00:1/128
cumulus@leaf01:~$ net add ospf6 router-id 2001:db8:0002::0a00:1
cumulus@leaf01:~$ net add ospf6 interface lo area 0
cumulus@leaf01:~$ net add ospf6 interface swp51 area 0
cumulus@leaf01:~$ net add interface swp1 ospf6 passive
cumulus@leaf01:~$ net add interface swp2 ospf6 passive
cumulus@leaf01:~$ net add interface swp51 ospf6 network point-to-point
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 2001:db8:0002::0a00:101/128
cumulus@spine01:~$ net add ospf6 router-id 2001:db8:0002::0a00:101
cumulus@spine01:~$ net add ospf6 interface lo area 0
cumulus@spine01:~$ net add ospf6 interface swp1 area 0
cumulus@spine01:~$ net add interface swp1 ospf6 network point-to-point
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "TabID299 ">}}

{{< tab "leaf01 ">}}

1. Enable the `ospf6` daemon, then start the FRRouting service. See {{<link url="Configure-FRRouting">}}.

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp51:

  ```
  cumulus@leaf01:~$ sudo nano /etc/network/interfaces
  ...
  auto lo
  iface lo inet loopback
    address 2001:db8:0002::0a00:1/128

  auto swp1
  iface swp1
    address 2001:db8:0002::0a00:1/128
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a

2. From the vtysh shell, configure OSPFv3:

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router ospf6
leaf01(config-ospf6)# router-id 2001:db8:0002::0a00:1
leaf01(config-ospf6)# interface lo area 0
leaf01(config-ospf6)# interface swp51 area 0
leaf01(config-ospf6)# passive-interface swp1
leaf01(config-ospf6)# passive-interface swp2
leaf01(config-ospf6)# exit
leaf01(config)# interface swp51
leaf01(config-if)# ospf network point-to-point
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Enable the `ospf6` daemon, then start the FRRouting service. See {{<link url="Configure-FRRouting">}}.

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp1:

  ```
  cumulus@leaf01:~$ sudo nano /etc/network/interfaces
  ...
  auto lo
  iface lo inet loopback
    address 2001:db8:0002::0a00:101/128

  auto swp51
  iface swp51
    address 2001:db8:0002::0a00:101/128
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

2. From the vtysh shell, configure OSPFv3:

```
cumulus@spine01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# router ospf6
spine01(config-ospf6)# router-id 2001:db8:0002::0a00:101
spine01(config-ospf6)# interface lo area 0
spine01(config-ospf6)# interface swp1 area 0
spine01(config-ospf6)# exit
spine01(config)# interface swp1
spine01(config-if)# ospf network point-to-point
spine01(config-if)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "TabID357 ">}}

{{< tab "leaf01 ">}}

```
...
interface swp51
 ip ospf network point-to-point
...
router ospf6
 ospf6 router-id 2001:db8:0002::0a00:1
 interface swp51 area 0
 interface lo area 0
...
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
...
interface swp1
 ip ospf network point-to-point
...
router ospf6
 ospf6 router-id 2001:db8:0002::0a00:101
 interface swp1 area 0
 interface lo area 0
...
```

{{< /tab >}}

{{< /tabs >}}

### Define Custom OSPFv3 Parameters

You can define additional custom parameters for OSPFv3, such as such as the network type (point-to-point or broadcast) and the interval between hello packets that OSPF sends.

The following command example sets the network type to point-to-point and the hello interval to 5 seconds. The hello interval can be any value between 1 and 65535 seconds.

{{< tabs "TabID82 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp1 ospf6 network point-to-point
cumulus@switch:~$ net add interface swp1 ospf6 hello-interval 5
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ipv6 ospf6 network point-to-point
switch(config-if)# ipv6 ospf6 hello-interval 5
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp1
 ipv6 ospf6 hello-interval 5
 ipv6 ospf6 network point-to-point
...
```

{{%notice note%}}

Unlike OSPFv2, OSPFv3 intrinsically supports unnumbered interfaces. Forwarding to the next hop router is done entirely using IPv6 link local addresses. You do not need to configure any global IPv6 address to interfaces between routers.

{{%/notice%}}

## Configure the OSPFv3 Area

You can use different areas to control routing. You can:

- Limit an OSPFv3 area from reaching another area.
- Manage the size of the routing table by creating a summary route for all the routes in a particular address range.

The following section provides command examples.

{{< tabs "TabID139 ">}}

{{< tab "NCLU Commands ">}}

The following example command removes the `3:3::/64` route from the routing table. Without a route in the table, any destinations in that network are not reachable.

```
cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 3:3::/64 not-advertise
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The following example command creates a summary route for all the routes in the range 2001::/64:

```
cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 2001::/64 advertise
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can also configure the cost for a summary route, which is used to determine the shortest paths to the destination. The value for cost must be between 0 and 16777215.

```
cumulus@switch:~$ net add ospf6 area 0.0.0.0 range 2001::/64 cost 160
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The following example command removes the `3:3::/64` route from the routing table. Without a route in the table, any destinations in that network are not reachable.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.0 range 3:3::/64 not-advertise
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~
```

The following example command creates a summary route for all the routes in the range 2001::/64:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.0 range 2001::/64 advertise
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

You can also configure the cost for a summary route, which is used to determine the shortest paths to the destination. The value for cost must be between 0 and 16777215.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.0 range 2001::/64 cost 160
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
  area 0.0.0.0 range 3:3::/64 not-advertise
  area 0.0.0.0 range 2001::/64 advertise
  area 0.0.0.0 range 2001::/64 cost 160
...
```

## Configure the OSPFv3 Distance

Cumulus Linux provides several commands to change the administrative distance for OSPF routes.

{{< tabs "TabID232 ">}}

{{< tab "NCLU Commands ">}}

This example command sets the distance for an entire group of routes, rather than a specific route.

```
cumulus@switch:~$ net add ospf6 distance 254
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

This example command changes the OSPF administrative distance to 150 for internal routes and 220 for external routes:

```
cumulus@switch:~$ net add ospf6 distance ospf6 intra-area 150 inter-area 150 external 220
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

This example command changes the OSPF administrative distance to 150 for internal routes to a subnet or network inside the same area as the router:

```
cumulus@switch:~$ net add ospf6 distance ospf6 intra-area 150
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

This example command changes the OSPF administrative distance to 150 for internal routes to a subnet in an area of which the router is *not* a part:

```
cumulus@switch:~$ net add ospf6 distance ospf6 inter-area 150
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

This example command sets the distance for an entire group of routes, rather than a specific route.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance 254
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

This example command changes the OSPF administrative distance to 150 for internal routes and 220 for external routes:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance ospf6 intra-area 150 inter-area 150 external 220
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

This example command changes the OSPF administrative distance to 150 for internal routes to a subnet or network inside the same area as the router:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance ospf6 intra-area 150
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

This example command changes the OSPF administrative distance to 150 for internal routes to a subnet in an area of which the router is *not* a part:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance ospf6 inter-area 150
switch(config-ospf6)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration to the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
  distance ospf6 intra-area 150 inter-area 150 external 220
...
```

## Configure OSPFv3 Interfaces

You can configure an interface, a bond interface, or a VLAN with an existing advertise prefix list. The prefix list defines the outbound route filter.

{{< tabs "TabID345 ">}}

{{< tab "NCLU Commands ">}}

The following example command configures interface swp3s1 with the IPv6 advertise prefix list named `filter`:

```
cumulus@switch:~$ net add interface swp3s1 ospf6 advertise prefix-list filter
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can also configure the cost for a particular interface, bond interface, or VLAN. The following example command configures the cost for swp2.

```
cumulus@switch:~$ net add interface swp2 ospf6 cost 1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The following example command configures interface swp3s1 with the IPv6 advertise prefix-list named `filter`.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp3s1
switch(config-if)# ipv6 ospf advertise prefix-list filter
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

You can also configure the cost for a particular interface, bond interface, or VLAN. The following example command configures the cost for swp2.

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp2
switch(config-if)# ipv6 ospf cost 1
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp2
  ipv6 ospf6 cost 1
...
```

## Troubleshooting

Cumulus Linux provides troubleshooting commands for OSPFv3:

- To show neighbor states, run the NCLU `net show ospf6 neighbor` command or the vtysh `show ip ospf6 neighbor` command.
- To verify that the LSDB is synchronized across all routers in the network, run the NCLU `net show ospf6 database` command or the vtysh `show ip ospf6 database` command.
- To determine why an OSPF route is not being forwarded correctly, run the NCLU `net show route ospf6` command or the vtysh `show ip route ospf6` command. These commands show the outcome of the SPF computation downloaded to the forwarding table.
- To help visualize the network view, run the NCLU `net show ospf6 spf tree` command or the `show ip ospf6 spf tree` command. These commands show the node topology as computed by SPF.

For example:

```
cumulus@switch:~$ net show ospf6 neighbor
Neighbor ID     Pri    DeadTime    State/IfState         Duration I/F[State]
10.0.0.21         1    00:00:37     Full/DROther         00:11:32 swp51[PointToPoint]
10.0.0.22         1    00:00:37     Full/DROther         00:11:32 swp52[PointToPoint]
```

Run the `net show ospf6 help` command to show available NCLU command options.

For a list of all the OSPF debug options, refer to {{<exlink url="http://docs.frrouting.org/en/latest/ospfd.html#id7" text="Debugging OSPF">}}.

## Related Information

- {{<link url="Bidirectional-Forwarding-Detection-BFD#bfd-in-ospf" text="Bidirectional forwarding detection">}} (BFD) and OSPF
- {{<exlink url="http://en.wikipedia.org/wiki/Open_Shortest_Path_First" text="Wikipedia - Open Shortest Path First">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/ospf6d.html" text="FRR OSPFv3">}}
- {{<exlink url="https://tools.ietf.org/html/rfc2740" text="RFC 2740 OSPFv3 OSPF for IPv6">}}
- {{<link url="Open-Shortest-Path-First-v2-OSPFv2/#auto-cost-reference-bandwidth" text="Auto-cost reference bandwidth">}}
