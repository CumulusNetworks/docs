---
title: Open Shortest Path First v3 - OSPFv3
author: NVIDIA
weight: 910
toc: 3
---
OSPFv3 is a revised version of OSPFv2 and supports the IPv6 address family.

{{%notice note%}}
IETF has defined extensions to OSPFv3 to support multiple address families (both IPv6 and IPv4). {{<link url="FRRouting" text="FRR">}} does not support multiple address families.
{{%/notice%}}

## Basic OSPFv3 Configuration

You can configure <span class="a-tooltip">[OSPF](## "Open Shortest Path First")</span> using either numbered interfaces or unnumbered interfaces.

{{%notice warning%}}
When you enable or disable OSPF, the FRR service restarts, which might impact traffic.
{{%/notice%}}

{{%notice note%}}
NVUE commands are not supported for OSPFv3.
{{%/notice%}}

### OSPFv3 Numbered

To configure OSPF using numbered interfaces, you specify the router ID, IP subnet prefix, and area address. All the interfaces on the switch with an IP address that matches the network subnet go into the specified area. OSPF attempts to discover other OSPF routers on those interfaces. Cumulus Linux adds all matching interface network addresses to a Type-1 Router LSA and advertises to discovered neighbors for proper reachability.

If you do not want to bring up an OSPF adjacency on certain interfaces, but want to advertise those networks in the OSPF database, you can configure the interfaces as *passive interfaces*. A passive interface creates a database entry but does not send or receive OSPF hello packets. For example, in a data center topology, the host-facing interfaces do not need to run OSPF, however, you must advertise the corresponding IP addresses to neighbors.

The following example commands configure OSPF numbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf3-numbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 2001:db8::a0a:0a01/128</li><li>The IP address on swp51 is 2001:db8::a00:0101/127</li><li>The router ID is 10.10.10.1</li><li>All the interfaces on the switch with an IP address that matches subnet 2001:db8::a0a:0a01/128 and swp51 with IP address 2001:db8::a00:0101/127 are in area 0.0.0.0</li><li>swp1 and swp2 are passive interfaces</li></ul> | <ul><li>The loopback address is 2001:db8::a0a:0a65/128</li><li>The IP address on swp1 is 22001:db8::a00:0100/127</li><li>The router ID is 10.10.10.101</li><li>All interfaces on the switch with an IP address that matches subnet 2001:db8::a0a:0a65/128 and swp1 with IP address 2001:db8::a00:0100/127 are in area 0.0.0.0.</li></ul> |

{{< tabs "TabID35 ">}}
{{< tab "leaf01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf6` daemon, then start the FRR service (see {{<link title="FRRouting">}}).

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp51:

  ```
  cumulus@leaf01:~$ sudo nano /etc/network/interfaces
  ...
  auto lo
  iface lo inet loopback
    address 2001:db8::a0a:0a01/128

  auto swp51
  iface swp51
    address 2001:db8::a00:0101/127
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@leaf01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@leaf01:~$ sudo vtysh
    ...
    leaf01# configure terminal
    leaf01(config)# router ospf6
    leaf01(config-ospf6)# ospf6 router-id 10.10.10.1
    leaf01(config-ospf6)# interface lo area 0.0.0.0
    leaf01(config-ospf6)# interface swp51 area 0.0.0.0
    leaf01(config-ospf6)# exit
    leaf01(config)# interface swp1
    leaf01(config-if)# ipv6 ospf6 passive
    leaf01(config-if)# exit
    leaf01(config)# interface swp2
    leaf01(config-if)# ipv6 ospf6 passive
    leaf01(config-if)# end
    leaf01# write memory
    leaf01# exit
    ```

{{< /tab >}}
{{< tab "spine01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf6` daemon, then start the FRR service (see {{<link title="FRRouting">}}).

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp1:

    ```
    cumulus@spine01:~$ sudo nano /etc/network/interfaces
    ...
    auto lo
    iface lo inet loopback
      address 2001:db8::a0a:0a65/128

    auto swp1
    iface swp1
      address 2001:db8::a00:0100/127
    ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@spine01:~$ sudo vtysh
    ...
    spine01# configure terminal
    spine01(config)# router ospf6
    spine01(config-ospf6)# ospf6 router-id 10.10.10.101
    spine01(config-ospf6)# interface lo area 0.0.0.0
    spine01(config-ospf6)# interface swp1 area 0.0.0.0
    spine01(config-ospf6)# end
    spine01# write memory
    spine01# exit
    ```

{{< /tab >}}
{{< /tabs >}}

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "TabID208 ">}}
{{< tab "leaf01 ">}}

```
...
router ospf6
 ospf6 router-id 10.10.10.1
 interface lo area 0.0.0.0
 interface swp51 area 0.0.0.0
interface swp1
 ipv6 ospf6 passive
interface swp2
 ipv6 ospf6 passive
...
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
...
router ospf6
 ospf router-id 10.10.10.101
 interface lo area 0.0.0.0
 interface swp1 area 0.0.0.0
...
```

{{< /tab >}}
{{< /tabs >}}

### OSPFv3 Unnumbered

Unnumbered interfaces are interfaces without unique IP addresses; multiple interfaces share the same IP address.

To configure an unnumbered interface, take the IP address of another interface (called the *anchor*) and use that as the IP address of the unnumbered interface. The anchor is typically the loopback interface on the switch.

{{%notice note%}}
OSPFv3 unnumbered supports {{<link url="#interface-parameters" text="point-to-point interfaces">}} only.
{{%/notice%}}

The following example commands configure OSPFv3 unnumbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf3-unnumbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 2001:db8::a0a:0a01/128</li><li>The router ID is 10.10.10.1</li><li>OSPF is on the loopback interface and on swp51 in area 0.0.0.0</li><li>swp1 and swp2 are passive interfaces</li><li>swp51 is a point-to-point interface (unnumbered interfaces require point-to-point)</li><ul>|<ul><li>The loopback address is 2001:db8::a0a:0a65/128</li><li>The router ID is 10.10.10.101</li><li>OSPF is on the loopback interface and on swp1 in area 0.0.0.0</li><li>swp1 is a point-to-point interface (unnumbered interfaces require point-to-point)</li><ul> |

{{< tabs "TabID211 ">}}
{{< tab "leaf01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf6` daemon, then start the FRR service (see {{<link title="FRRouting">}}).

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp51:

  ```
  cumulus@leaf01:~$ sudo nano /etc/network/interfaces
  ...
  auto lo
  iface lo inet loopback
    address 2001:db8::a0a:0a01/128

  auto swp1
  iface swp1
    address 2001:db8::a0a:0a01/128
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@leaf01:~$ sudo ifreload -a

2. From the vtysh shell, configure OSPFv3:

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router ospf6
leaf01(config-ospf6)# ospf6 router-id 10.10.10.1
leaf01(config-ospf6)# interface lo area 0.0.0.0
leaf01(config-ospf6)# interface swp51 area 0.0.0.0
leaf01(config-ospf6)# exit
leaf01(config)# interface swp1
leaf01(config-if)# ipv6 ospf6 passive
leaf01(config-if)# exit
leaf01(config)# interface swp2
leaf01(config-if)# ipv6 ospf6 passive
leaf01(config-if)# exit
leaf01(config)# interface swp51
leaf01(config-if)# ipv6 ospf6 network point-to-point
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
```

{{< /tab >}}
{{< tab "spine01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf6` daemon, then start the FRR service (see {{<link title="FRRouting">}}).

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp1:

  ```
  cumulus@spine01:~$ sudo nano /etc/network/interfaces
  ...
  auto lo
  iface lo inet loopback
    address 2001:db8::a0a:0a65/128

  auto swp1
  iface swp1
    address 2001:db8::a0a:0a65/128
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

2. From the vtysh shell, configure OSPFv3:

```
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# router ospf6
spine01(config-ospf6)# ospf router-id 10.10.10.101
spine01(config-ospf6)# interface lo area 0.0.0.0
spine01(config-ospf6)# interface swp1 area 0.0.0.0
spine01(config-ospf6)# exit
spine01(config)# interface swp1
spine01(config-if)# ipv6 ospf6 network point-to-point
spine01(config-if)# end
spine01# write memory
spine01# exit
```

{{< /tab >}}
{{< /tabs >}}

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "TabID366 ">}}
{{< tab "leaf01 ">}}

```
...
router ospf6
 ospf6 router-id 10.10.10.1
 interface lo area 0.0.0.0
 interface swp51 area 0.0.0.0
interface swp1
 ipv6 ospf6 passive
interface swp2
 ipv6 ospf6 passive
interface swp51
 ipv6 ospf6 network point-to-point
...
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
...
router ospf6
 ospf6 router-id 10.10.10.101
 interface lo area 0.0.0.0
 interface swp1 area 0.0.0.0
interface swp1
 ipv6 ospf6 network point-to-point
...
```

{{< /tab >}}
{{< /tabs >}}

## Optional OSPFv3 Configuration

This section describes optional configuration. The steps provided in this section assume that you already configured basic OSPFv3 as described in {{<link url="#basic-ospfv3-configuration" text="Basic OSPF Configuration">}}, above.

### Interface Parameters

You can define the following OSPF parameters per interface:
- Network type (point-to-point or broadcast). Broadcast is the default setting. Configure the interface as point-to-point unless you intend to use the Ethernet media as a LAN with multiple connected routers. Point-to-point provides a simplified adjacency state machine so there is no need for DR/BDR election and *LSA reflection*. See {{<exlink url="http://tools.ietf.org/rfc/rfc5309" text="RFC5309">}} for a more information.
  {{%notice note%}}
  {{<link url="#ospfv3-unnumbered" text="OSPFv3 unnumbered">}} requires Point-to-point.
  {{%/notice%}}
- Hello interval. The number of seconds between hello packets sent on the interface. The default is 10 seconds.
- Dead interval. Then number of seconds before neighbors declare the router down after they stop hearing
hello packets. The default is 40 seconds.
- Priority in becoming the OSPF <span class="a-tooltip">[DR](## "Designated Router")</span> on a broadcast interface. The default is priority 1.
- Advertise prefix list. The prefix list defines the outbound route filter.
- Cost. The cost determines the shortest paths to the destination.

The following command example sets the network type to point-to-point on swp51.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ipv6 ospf6 network point-to-point
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp51
 ipv6 ospf6 network point-to-point
...
```

The following command example sets the hello interval to 5 seconds, the dead interval to 60 seconds, and the priority to 5 for swp51. The hello interval and dead interval can be any value between 1 and 65535 seconds. The priority can be any value between 0 to 255 (0 configures the interface to never become the OSPF Designated Router (DR) on a broadcast interface).

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ipv6 ospf6 hello-interval 5
switch(config-if)# ipv6 ospf6 network dead-interval 60
switch(config-if)# ipv6 ospf6 network priority 5
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp51
 ipv6 ospf6 hello-interval 5
 ipv6 ospf6 dead-interval 60
 ipv6 ospf6 priority 5
...
```

The following example command configures interface swp51 with the IPv6 advertise prefix list named `myfilter`:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ipv6 ospf6 advertise prefix-list myfilter
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp51
  ipv6 ospf6 advertise prefix-list myfilter
...
```

The following example command configures the cost for swp51.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ipv6 ospf6 cost 1
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp51
  ipv6 ospf6 cost 1
...
```

To show the configured OSPF interface parameter values, run the vtysh `show ipv6 ospf6 interface` command.

### SPF Timer Defaults

OSPF3 uses the following default timers to prevent consecutive <span class="a-tooltip">[SPF](## "Shortest Path First")</span> from overburdening the CPU:

- 0 milliseconds from the initial event until SPF runs
- 50 milliseconds between consecutive SPF runs (the number doubles with each SPF, until it reaches the maximum time between SPF runs)
- 5000 milliseconds maximum between SPFs

The following example commands change the number of milliseconds from the initial event until SPF runs to 80, the number of milliseconds between consecutive SPF runs to 100, and the maximum number of milliseconds between SPFs to 6000.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# timers throttle spf 80 100 6000
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
 ospf router-id 10.10.10.1
 passive-interface swp1
 passive-interface swp2
 network swp51 area 0.0.0.0
 timers throttle spf 80 100 6000
...
```

To see the configured SPF timer values, run the vtysh `show ipv6 ospf6` command.

### Configure the OSPFv3 Area

You can use different areas to control routing. You can:

- Limit an OSPFv3 area from reaching another area.
- Manage the size of the routing table by creating a summary route for all the routes in a particular address range.

The following section provides command examples.

The following example command removes the `3:3::/64` route from the routing table. Without a route in the table, any destinations in that network are not reachable.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.0 range 3:3::/64 not-advertise
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The following example command creates a summary route for all the routes in the range 2001::/64:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.0 range 2001::/64 advertise
switch(config-ospf6)# end
switch# write memory
switch# exit
```

You can also configure the cost for a summary route, which Cumulus Linux uses to determine the shortest paths to the destination. The value for cost must be between 0 and 16777215.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.0 range 2001::/64 cost 160
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
  ospf6 router-id 10.10.10.1
  area 0.0.0.0 range 3:3::/64 not-advertise
  area 0.0.0.0 range 2001::/64 advertise
  area 0.0.0.0 range 2001::/64 cost 160
...
```

### Stub Areas

External routes are the routes redistributed into OSPF from another protocol. They have an AS-wide flooding scope. Typically, external link states make up a large percentage of the <span class="a-tooltip">[LSDB](## "Link-State Database")</span>. Stub *areas* reduce the LSDB size by not flooding AS-external LSAs.

All routers must agree that an area is a stub, otherwise they do not become OSPF neighbors.

To configure a stub area:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.1 stub
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
 ospf6 router-id 10.10.10.63
 area 0.0.0.1 stub
...
```

Stub areas still receive information about networks that belong to other areas of the same OSPF domain. If summarization is not configured (or is not comprehensive), the information can be overwhelming for the nodes. *Totally stubby areas* address this issue. Routers in totally stubby areas keep information about routing within their area in their LSDB.

To configure a totally stubby area:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# area 0.0.0.1 stub no-summary
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
 ospf6 router-id 10.10.10.63
 area 0.0.0.1 stub no-summary
...
```

Here is a brief summary of the area type differences:

| Type| Behavior |
| ----------- | -----------|
| Normal non-zero area | LSA types 1, 2, 3, 4 area-scoped, type 5 externals, inter-area routes summarized |
| Stub area | LSA types 1, 2, 3, 4 area-scoped, no type 5 externals, inter-area routes summarized |
| Totally stubby area | LSA types 1, 2 area-scoped, default summary, no type 3, 4, 5 LSA types allowed |
<!-- vale off -->
### Auto-cost Reference Bandwidth
<!-- vale on -->
When you set the *auto-cost reference bandwidth,* Cumulus Linux dynamically calculates the OSPF interface cost to support higher speed links. The default value is *100000* for 100Gbps link speed. The cost of interfaces with link speeds lower than 100Gbps is higher.

{{%notice tip%}}
To avoid routing loops, set the bandwidth to a consistent value across all OSPF routers.
{{%/notice%}}

The following example commands configure the auto-cost reference bandwidth for 90Gbps link speed:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# auto-cost reference-bandwidth 90000
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
 ospf6 router-id 10.10.10.1
 interface lo area 0.0.0.0
 interface swp51 area 0.0.0.0
 auto-cost reference-bandwidth 90000
...
```

### Administrative Distance

Cumulus Linux uses the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPFv3 with an administrative distance of 110 and the same route from <span class="a-tooltip">[BGP](## "Border Gateway Protocol")</span> with an administrative distance of 100, the switch chooses BGP.

Cumulus Linux provides several commands to change the administrative distance for OSPF routes. The default value is 110.

This example command sets the distance for an entire group of routes, rather than a specific route.

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance 254
switch(config-ospf6)# end
switch# write memory
switch# exit
```

This example command changes the OSPF administrative distance to 150 for internal routes and 220 for external routes:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance ospf6 intra-area 150 inter-area 150 external 220
switch(config-ospf6)# end
switch# write memory
switch# exit
```

This example command changes the OSPF administrative distance to 150 for internal routes to a subnet or network inside the same area as the router:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance ospf6 intra-area 150
switch(config-ospf6)# end
switch# write memory
switch# exit
```

This example command changes the OSPF administrative distance to 150 for internal routes to a subnet in an area of which the router is *not* a part:

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf6
switch(config-ospf6)# distance ospf6 inter-area 150
switch(config-ospf6)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration to the `/etc/frr/frr.conf` file. For example:

```
...
router ospf6
 ospf6 router-id 10.10.10.1
 interface lo area 0.0.0.0
 distance ospf6 intra-area 150 inter-area 150 external 220
...
```

## Troubleshooting

Cumulus Linux provides several OSPFv3 troubleshooting commands:

| To   | <div style="width:330px">vtysh Command |
| --- | ---- |
| Show neighbor states | `show ipv6 ospf6 neighbor` |
| Verify that the LSDB is the same across all routers in the network | `show ipv6 ospf6 database` |
| Determine why Cumulus Linux does forward an OSPF route correctly | `show ipv6 ospf6 route` |
| Show OSPF interfaces | `show ipv6 ospf6 interface` |
| Help visualize the network view | `show ipv6 ospf6 spf tree` |
| Show information about the OSPFv3 process | `show ipv6 ospf6` |

The following example shows the vtysh `show ipv6 ospf6 neighbor` command output:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ipv6 ospf6 neighbor
Neighbor ID     Pri    DeadTime    State/IfState         Duration I/F[State]
10.10.10.101      1    00:00:34     Full/BDR             00:02:58 swp51[DR]
```

The following example shows the vtysh `show ipv6 ospf6 route` command output:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ipv6 ospf6 route
Codes: K - kernel route, C - connected, S - static, R - RIPng,
       O - OSPFv3, I - IS-IS, B - BGP, N - NHRP, T - Table,
       v - VNC, V - VNC-Direct, A - Babel, D - SHARP, F - PBR,
       f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route

O   2001:db8::a00:100/127 [110/100] is directly connected, swp51, weight 1, 00:00:20
O   2001:db8::a0a:a01/128 [110/10] is directly connected, lo, weight 1, 00:01:40
O>* 2001:db8::a0a:a65/128 [110/110] via fe80::4638:39ff:fe00:2, swp51, weight 1, 00:00:15
```

To capture OSPF packets, run the `sudo tcpdump -v -i swp1 ip proto ospf6` command.

## Related Information

- {{<exlink url="http://docs.frrouting.org/en/latest/ospf6d.html" text="FRR OSPFv3">}}
- {{<exlink url="https://tools.ietf.org/html/rfc2740" text="RFC 2740 OSPFv3 OSPF for IPv6">}}
