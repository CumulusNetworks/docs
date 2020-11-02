---
title: Open Shortest Path First v2 - OSPFv2
author: Cumulus Networks
weight: 790
toc: 3
---
This topic describes OSPFv2, which is a {{<exlink url="http://en.wikipedia.org/wiki/Link-state_routing_protocol" text="link-state routing protocol">}} for IPv4. For IPv6 commands, refer to {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}}.

## Basic OSPFv2 Configuration

You can configure OSPF using either numbered interfaces or unnumbered interfaces. Both methods are described below.

### OSPF Numbered

To configure OSPF using numbered interfaces, you specify the router ID, IP subnet prefix, and area address. All the interfaces on the switch with an IP address that matches the `network` subnet are put into the specified area. The OSPF process starts bringing up peering adjacency on those interfaces. It also advertises the interface IP addresses formatted into LSAs to the neighbors for proper reachability.

If you do not want to bring up OSPF adjacency on certain interfaces, you can configure the interfaces as *passive interfaces*. A passive interface creates a database entry but does not send or recieve OSPF hello packets. For example, in a data center topology, the host-facing interfaces do not need to run OSPF, however, the corresponding IP addresses still need to be advertised to neighbors.

The subnets can be as inclusive as possible to cover the highest number of interfaces on the switch that run OSPF.

The following example commands configure OSPF numbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf-numbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 10.10.10.1/32</li><li>The IP address on swp51 is 10.0.1.0/31</li><li>The router ID is 10.10.10.1</li><li>All the interfaces on the switch with an IP address that matches subnet 10.10.10.1/32 and and swp51 with IP address 10.0.1.0/31 are in area 0</li><li>swp1 and swp2 are passive interfaces</li></ul> | <ul><li>The loopback address is 10.10.10.101/32</li><li>The IP address on swp1 is 10.0.1.1/31</li><li>The router ID is 10.10.10.101</li><li>All interfaces on the switch with an IP address that matches subnet 10.10.10.101/32 and swp1 with IP address 10.0.1.1/31 are in area 0.</li></ul> |

{{< tabs "TabID29 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "TabID49 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add interface swp51 ip address 10.0.1.0/31
cumulus@leaf01:~$ net add ospf router-id 10.10.10.1
cumulus@leaf01:~$ net add ospf network 10.10.10.1/32 area 0
cumulus@leaf01:~$ net add ospf network 10.0.1.0/31 area 0
cumulus@leaf01:~$ net add ospf passive-interface swp1
cumulus@leaf01:~$ net add ospf passive-interface swp2
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

You can use the `net add ospf passive-interface default` command to set all interfaces as *passive* and the `net del ospf passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@leaf01:~$ net add ospf passive-interface default
cumulus@leaf01:~$ net del ospf passive-interface swp51
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp1 ip address 10.0.1.1/31
cumulus@spine01:~$ net add ospf router-id 10.10.10.101
cumulus@spine01:~$ net add ospf network 10.10.10.101/32 area 0
cumulus@spine01:~$ net add ospf network 10.0.1.1/31 area 0
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

You can use the `net add ospf passive-interface default` command to set all interfaces as *passive* and the `net del ospf passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@spine01:~$ net add ospf passive-interface default
cumulus@spine01:~$ net del ospf passive-interface swp1
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
    address 10.10.10.1/32

  auto swp51
  iface swp51
    address 10.0.1.0/31
  ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@leaf01:~$ sudo vtysh

    leaf01# configure terminal
    leaf01(config)# router ospf
    leaf01(config-router)# router-id 10.10.10.1
    leaf01(config-router)# network 10.10.10.1/32 area 0
    leaf01(config-router)# network 10.0.1.0/31 area 0
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
leaf01(config)# router ospf
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
      address 10.10.10.101/32

    auto swp51
    iface swp51
      address 10.0.1.1/31
    ```

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@spine01:~$ sudo vtysh

    spine01# configure terminal
    spine01(config)# router ospf
    spine01(config-router)# router-id 10.10.101.1
    spine01(config-router)# network 10.10.10.101/32 area 0
    spine01(config-router)# network 10.0.1.1/31 area 0
    spine01(config-router)# exit
    spine01(config)# exit
    spine01# write memory
    spine01# exit
    cumulus@spine01:~$
    ```

You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency only on certain interfaces:

```
spine01(config)# router ospf
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
router ospf
 ospf router-id 10.10.10.1
 network 10.10.10.1/32 area 0
 network 10.0.1.0/31 area 0
 passive-interface swp1
 passive-interface swp2
...
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
...
router ospf
 ospf router-id 10.10.101.1
 network 10.10.10.101/32 area 0
 network 10.0.1.1/31 area 0
...

```
{{< /tab >}}

{{< /tabs >}}

### OSPF Unnumbered

Unnumbered interfaces are interfaces without unique IP addresses; multiple interfaces share the same IP address. In OSPFv2, unnumbered interfaces reduce the links between routers into pure topological elements, which simplifies network configuration and reconfiguration. In addition, the routing database contains only the real networks, so the memory footprint is reduced and SPF is faster.

To configure an unnumbered interface, take the IP address of another interface (called the *anchor*) and use that as the IP address of the unnumbered interface. The anchor is typically the loopback interface on the switch.

{{%notice note%}}

OSPF Unnumbered is supported with {{<link url="#interface-options" text="point-to-point interfaces">}} only.

{{%/notice%}}

The following example commands configure OSPF unnumbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf-unnumbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 10.10.10.1/32</li><li>The IP address of the unnumbered interface (swp51) is 10.10.10.1/32</li><li>The router ID is 10.10.10.1</li><li>OSPF is enabled on the loopback interface and on swp51 in area 0</li><li>swp1 and swp2 are passive interfaces</li><li>swp51 is a point-to-point interface</li><ul>|<ul><li>The loopback address is 10.10.10.101/32</li><li>The IP address of the unnumbered interface (swp1) is 10.10.10.101/32</li><li>The router ID is 10.10.10.101</li><li>OSPF is enabled on the loopback interface and on swp1 in area 0</li><li>swp1 is a point-to-point interface</li><ul> |

{{< tabs "TabID260 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "TabID252 ">}}

{{< tab "leaf01 ">}}

Configure the unnumbered interface:

```
cumulus@leaf01:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@leaf01:~$ net add interface swp51 ip address 10.10.10.1/32
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

Configure OSPF:

```
cumulus@leaf01:~$ net add ospf router-id 10.10.10.1
cumulus@leaf01:~$ net add loopback lo ospf area 0
cumulus@leaf01:~$ net add interface swp51 ospf area 0
cumulus@leaf01:~$ net add ospf passive-interface swp1
cumulus@leaf01:~$ net add ospf passive-interface swp2
cumulus@leaf01:~$ net add interface swp51 ospf network point-to-point
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

You can use the `net add ospf passive-interface default` command to set all interfaces as *passive* and the `net del ospf` `passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@leaf01:~$ net add ospf passive-interface default
cumulus@leaf01:~$ net del ospf passive-interface swp51
```

{{< /tab >}}

{{< tab "spine01 ">}}

Configure the unnumbered interface:

```
cumulus@spine01:~$ net add loopback lo ip address 10.10.10.101/32
cumulus@spine01:~$ net add interface swp1 ip address 10.10.10.101/32
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

Configure OSPF:

```
cumulus@spine01:~$ net add ospf router-id 10.10.10.101
cumulus@spine01:~$ net add loopback lo ospf area 0
cumulus@spine01:~$ net add interface swp1 ospf area 0
cumulus@spine01:~$ net add interface swp1 ospf network point-to-point
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

You can use the `net add ospf passive-interface default` command to set all interfaces as *passive* and the `net del ospf` `passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@spine01:~$ net add ospf passive-interface default
cumulus@spine01:~$ net del ospf passive-interface swp1
```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "Linux and vtysh Commands ">}}

{{< tabs "TabID337 ">}}

{{< tab "leaf01 ">}}

1. Enable the `ospf` daemon, then start the FRRouting service. See {{<link url="Configure-FRRouting">}}.

2. Edit the `/etc/network/interfaces` file to configure the loopback and unnumbered interface address:

    ```
    cumulus@leaf01:~$ sudo nano /etc/network/interfaces
    ...
    auto lo
    iface lo inet loopback
      address 10.10.10.1/32

    auto swp51
    iface swp51
      address 10.10.10.1/32
    ```

2. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@switch:~$ ifreload -a
    ```

3. From the `vtysh` shell, configure OSPF:

    ```
    cumulus@leaf01:~$ sudo vtysh

    leaf01# configure terminal
    leaf01(config)# interface swp51
    leaf01(config-if)# ip ospf area 0
    leaf01(config-if)# ip ospf network point-to-point
    leaf01(config-if)# exit
    leaf01(config)# interface lo
    leaf01(config-if)# ip ospf area 0
    leaf01(config-if)# exit
    leaf01(config)# router ospf
    leaf01(config-router)# router-id 10.10.10.1
    leaf01(config-router)# passive-interface swp1,swp2
    leaf01(config-router)# end
    leaf01# write memory
    leaf01# exit
    cumulus@leaf01:~$
    ```

   You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency only on certain interfaces:

   ```
   leaf01(config)# router ospf
   leaf01(config-router)# passive-interface default
   leaf01(config-router)# no passive-interface swp51
   ```

{{< /tab >}}

{{< tab "spine01 ">}}

1. Enable the `ospf` daemon, then start the FRRouting service. See {{<link url="Configure-FRRouting">}}.

2. Edit the `/etc/network/interfaces` file to configure the loopback and unnumbered interface address:

    ```
    cumulus@spine01:~$ sudo nano /etc/network/interfaces
    ...
    auto lo
    iface lo inet loopback
       address 10.10.10.101/32

    auto swp1
    iface swp1
      address 10.10.10.101/32
    ```

2. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

3. From the `vtysh` shell, configure OSPF:

    ```
    cumulus@spine01:~$ sudo vtysh

    spine01# configure terminal
    spine01(config)# interface swp1
    spine01(config-if)# ip ospf area 0
    spine01(config-if)# ip ospf network point-to-point
    spine01(config-if)# exit
    spine01(config)# interface lo
    spine01(config-if)# ip ospf area 0
    spine01(config-if)# exit
    spine01(config)# router ospf
    spine01(config-router)# router-id 10.10.10.101
    spine01(config-if)# end
    spine01# write memory
    spine01# exit
    cumulus@spine01:~$
    ```

   You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency only on certain interfaces:

   ```
   spine01(config)# router ospf
   spine01(config-router)# passive-interface default
   spine01(config-router)# no passive-interface swp1
   ```

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "TabID452 ">}}

{{< tab "leaf01 ">}}

```
...
!
interface lo
 ip ospf area 0
!
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
!
router ospf
 ospf router-id 10.10.10.1
 passive-interface swp1,swp2
!
line vty
!

...
```

{{< /tab >}}

{{< tab "spine01 ">}}

```
...
!
interface lo
 ip ospf area 0
!
interface swp1
 ip ospf area 0
 ip ospf network point-to-point
!
router ospf
 ospf router-id 10.10.10.101
!
line vty
!
```

{{< /tab >}}

{{< /tabs >}}

## Optional OSPFv2 Configuration

This section describes optional configuration. The steps provided in this section assume that you already configured basic OSPFv2 as described in {{<link url="#basic-ospfv2-configuration" >}}, above.

### Redistribute Protocol Routes

To redistribute protocol routes, run the `net add ospf redistribute connected` command.

Redistribution loads the database unnecessarily with type-5 LSAs. Only use this method to generate real external prefixes (type-5 LSAs). For example:

{{< tabs "TabID509 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add ospf redistribute connected
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# redistribute connected
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

### Interface Parameters

You can define the following OSPF parameters per interface:
- Network type (point-to-point or broadcast). Broadcast is the default setting.
- Interval between hello packets sent on the interface.

Cumulus Networks recommends that you configure the interface as point-to-point unless you intend to use the Ethernet media as a LAN with multiple connected routers. Point-to-point provides a simplified adjacency state machine; there is no need for DR/BDR election and *LSA reflection*. See {{<exlink url="http://tools.ietf.org/rfc/rfc5309" text="RFC5309">}} for a more information.

{{%notice note%}}

Point-to-point is required for OSPF unnumbered.

{{%/notice%}}

The following command example sets the network type to point-to-point and the hello interval to 5 seconds for swp51. The hello interval can be any value between 1 and 65535 seconds.

{{< tabs "TabID555 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp51 ospf network point-to-point
cumulus@switch:~$ net add interface swp51 ospf hello-interval 5
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ospf network point-to-point
switch(config-if)# ospf network hello-interval 5
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example

```
...
interface swp51
 ip ospf network point-to-point
 ip ospf hello-interval 5
...
```

### SPF Timer Defaults

OSPF uses the following default timers to prevent consecutive SPFs from overburdening the CPU:

- 0 milliseconds from the initial event until SPF runs
- 50 milliseconds between consecutive SPF runs (the number doubles with each SPF, until it reaches the value of C)
- 5000 milliseconds maximum between SPFs

The following example commands change the number of milliseconds from the initial event until SPF runs to 80, the number of milliseconds between consecutive SPF runs to 100, and the maximum number of milliseconds between SPFs to 6000.

{{< tabs "TabID607 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add ospf timers throttle spf 80 100 6000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# timers throttle spf 80 100 6000
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 ospf router-id 10.10.10.1
 passive-interface swp1
 passive-interface swp2
 network 10.10.10.1/32 area 0
 timers throttle spf 80 100 6000
...
```

### MD5 Authentication

To configure MD5 authentication on the switch, you need to create a key and a key ID, then enable MD5 authentication. The *key ID* must be a value between 1 and 255 that represents the key used to create the message digest. This value must be consistent across all routers on a link. The *key* must be a value with an upper range of 16 characters (longer strings are truncated) that represents the actual message digest.

The following example commands create key ID 1 with the key `thisisthekey` and enable MD5 authentication on swp51 on leaf01 and on swp1 on spine01.

{{< tabs "TabID656 ">}}

{{< tab "NCLU Commands ">}}

{{< tabs "TabID662 ">}}

{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ net add interface swp51 ospf message-digest-key 1 md5 thisisthekey
cumulus@leaf01:~$ net add interface swp51 ospf authentication message-digest
cumulus@leaf01:~$ net pending
cumulus@leaf01:~$ net commit
```

{{< /tab >}}

{{< tab " spine01">}}

```
cumulus@spine01:~$ net add interface swp1 ospf message-digest-key 1 md5 thisisthekey
cumulus@spine01:~$ net add interface swp1 ospf authentication message-digest
cumulus@spine01:~$ net pending
cumulus@spine01:~$ net commit
```

{{%notice note%}}

You can remove existing MD5 authentication hashes with the `net del` command. For example, `net del interface swp51 ospf message-digest-key 1 md5 thisisthekey`

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

{{< /tab >}}

{{< tab "vtysh Commands ">}}

{{< tabs "TabID698 ">}}

{{< tab "leaf01 ">}}

```
cumulus@spine01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# interface swp51
leaf01(config-if)# ip ospf authentication message-digest
leaf01(config-if)# ip ospf message-digest-key 1 md5 thisisthekey
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

{{< /tab >}}

{{< tab " spine01">}}

```
cumulus@leaf01:~$ sudo vtysh

spine01# configure terminal
spine01(config)# interface swp1
spine01(config-if)# ip ospf authentication message-digest
spine01(config-if)# ip ospf message-digest-key 1 md5 thisisthekey
spine01(config-if)# end
spine01# write memory
spine01# exit
cumulus@spine01:~$
```
{{< /tab >}}

{{< /tabs >}}

{{%notice note%}}

You can remove existing MD5 authentication hashes with the `no ip ospf message-digest-key` command. For example, `no ip ospf message-digest-key 1 md5 thisisthekey`

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

{{< tabs "TabID747 ">}}

{{< tab "leaf01 ">}}

```
...
interface swp51
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 thisisthekey
 ...
```

{{< /tab >}}

{{< tab " spine01">}}

```
...
interface swp1
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 thisisthekey
 ...
```

{{< /tab >}}

{{< /tabs >}}

### Summarization

By default, an area border router (ABR) creates a summary (type-3) LSA for each route in an area and advertises it in adjacent areas. Prefix range configuration optimizes this behavior by creating and advertising one summary LSA for multiple routes.

The following example commands create a summary route for all the routes in the range 10.10.10.63/32 in area 1:

```
cumulus@leaf01:~$ sudo vtysh

leaf01# configure terminal
leaf01(config)# router ospf
leaf01(config-router)# area 1 range 10.10.10.63/32
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
cumulus@leaf01:~$
```

The `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.63
 area 1 range 10.10.10.63/32
 ...
```

{{%notice note%}}

- Always configure the summary towards the backbone. The backbone receives summarized routes and injects them to other areas already summarized.
- Summarization can cause *non-optimal* forwarding of packets during failures.

{{%/notice%}}

### Stub Areas

External routes are the routes redistributed into OSPF from another protocol. They have an AS-wide flooding scope. In many cases, external link states make up a large percentage of the LSDB. Stub *areas* reduce the link-state database size by not flooding AS-external LSAs.

To configure a stub area:

{{< tabs "TabID816 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add ospf area 1 stub
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 1 stub
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.63
 area 1 stub
...
```

Stub areas still receive information about networks that belong to other areas of the same OSPF domain. If summarization is not configured (or is not comprehensive), the information can be overwhelming for the nodes. *Totally stubby areas* address this issue. Routers in totally stubby areas keep information about routing within their area in their LSDB.

To configure a totally stubby area:

{{< tabs "TabID860 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add ospf area 1 stub no-summary
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 1 stub no-summary
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.63
 area 1 stub no-summary
...
```

Here is a brief summary of the area type differences:

| Type| Behavior |
| ----------- | -----------|
| Normal non-zero area | LSA types 1, 2, 3, 4 area-scoped, type 5 externals, inter-area routes summarized |
| Stub area | LSA types 1, 2, 3, 4 area-scoped, no type 5 externals, inter-area routes summarized |
| Totally stubby area | LSA types 1, 2 area-scoped, default summary, no type 3, 4, 5 LSA types allowed |

### Auto-cost Reference Bandwidth

When you set the *auto-cost reference bandwidth,* Cumulus Linux dynamically calculates the OSPF interface cost to support higher speed links. The default value is *100000* for 100Gbps link speed. The cost of interfaces with link speeds lower than 100Gbps is higher.

{{%notice tip%}}

To avoid routing loops, set the bandwidth to a consistent value across all OSPF routers.

{{%/notice%}}

The following example commands configure the auto-cost reference bandwidth for 90Gbps link speed:

{{< tabs "TabID920 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add ospf auto-cost reference-bandwidth 90000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# auto-cost reference-bandwidth 90000
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.1
 auto-cost reference-bandwidth 90000
...
```

### Apply a Route Map for Route Updates

You can apply a {{<exlink url="http://docs.frrouting.org/en/latest/routemap.html" text="route map">}} to filter route updates from Zebra into the Linux kernel.

{{< tabs "TabID964 ">}}

{{< tab "NCLU Commands ">}}

The following example commands apply the route map called `map1`:

```
cumulus@switch:~$ net add routing protocol ospf route-map map1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The following example commands apply the route map called `map1`:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# ip protocol ospf route-map map1
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
router ospf
  ospf router-id 10.10.10.1
  ...
!
ip protocol ospf route-map map1
!
...
```

To apply a route map to redistributed routes:

{{< tabs "TabID1012 ">}}

{{< tab "NCLU Commands ">}}

The following example commands apply the route map called `map1` to redistributed routes:

```
cumulus@switch:~$ net add ospf redistribute connected route-map map1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

The following example commands apply the route map called `map1` to redistributed routes:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# redistribute connected route-map map1
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
router ospf
 ospf router-id 10.10.10.1
 redistribute connected route-map map1
...
```

### Topology Changes and OSPF Reconvergence

Topology changes usually occur when a router or a link undergoes maintenance or experiences a failure.

For maintenance events, you can raise the OSPF administrative weight of the links to ensure that all traffic is diverted from the link or the node (referred to as *costing out*). The speed of reconvergence does not matter. Changing the OSPF cost causes LSAs to be reissued, but the links remain in service during the SPF computation process of all routers in the network.

For failure events, traffic might be lost during reconvergence (until SPF on all nodes computes an alternative path around the failed link or node to each of the destinations). The reconvergence depends on layer 1 failure detection capabilities and the *DeadInterval* OSPF timer.

Example configuration for router maintenance:

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# router ospf
switch(config-router)# max-metric router-lsa administrative
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

Example configuration for link maintenance:

{{< tabs "TabID1013 ">}}

{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp51 ospf cost 65535
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ospf cost 65535
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

## Troubleshooting

Cumulus Linux provides several troubleshooting commands for OSPF:

| To...   | <div style="width:330px">NCLU Command | <div style="width:330px">vtysh Command |
| --- | ---- | ----- |
| Show neighbor states: | `net show ospf neighbor` | `show ip ospf neighbor` |
| Verify that the LSDB is synchronized across all routers in the network: | `net show ospf database` | `show ip ospf database` |
| Determine why an OSPF route is not being forwarded correctly: |`net show route ospf` | `show ip route ospf` |
| Capture OSPF packets: |  `sudo tcpdump -v -i swp1 ip proto ospf`|

The following example shows the `net show ospf neighbor` command:

```
cumulus@leaf01:mgmt:~$ net show ospf neighbor
Neighbor ID     Pri State           Dead Time Address         Interface                        RXmtL RqstL DBsmL
10.10.10.101      1 Full/Backup       30.307s 10.0.1.1        swp51:10.0.1.0                       0     0     0
```

The following example shows the `net show route ospf` command output:

```
cumulus@leaf01:mgmt:~$ net show route ospf
RIB entry for ospf
==================
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route

O   10.0.1.0/31 [110/100] is directly connected, swp51, weight 1, 00:02:37
O   10.10.10.1/32 [110/0] is directly connected, lo, weight 1, 00:02:37
O>* 10.10.10.101/32 [110/100] via 10.0.1.1, swp51, weight 1, 00:00:57
```

For a list all of the OSPF debug options, refer to {{<exlink url="http://docs.frrouting.org/en/latest/ospfd.html#id7" text="Debugging OSPF">}}.

## Related Information

- {{<link url="Bidirectional-Forwarding-Detection-BFD#bfd-in-ospf" text="Bidirectional forwarding detection">}} (BFD) and OSPF
- {{<exlink url="http://en.wikipedia.org/wiki/Open_Shortest_Path_First" text="Wikipedia - Open Shortest Path First">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/ospfd.html" text="FRR OSPFv2">}}
- Perlman, Radia (1999); *Interconnections: Bridges, Routers, Switches, and Internetworking Protocols (2 ed.)*; Addison-Wesley
- Moy, John T.; *OSPF: Anatomy of an Internet Routing Protocol*; Addison-Wesley
- {{<exlink url="https://tools.ietf.org/html/rfc2328" text="RFC 2328 OSPFv2">}}
- {{<exlink url="https://tools.ietf.org/html/rfc3101" text="RFC 3101 OSPFv2 Not-So-Stubby Area (NSSA)">}}
