---
title: Open Shortest Path First v2 - OSPFv2
author: NVIDIA
weight: 900
toc: 3
---
This topic describes OSPFv2, which is a link-state routing protocol for IPv4. For IPv6 commands, refer to {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}}.

## Basic OSPFv2 Configuration

You can configure <span style="background-color:#F5F5DC">[OSPF](## "Open Shortest Path First")</span> using either numbered interfaces or unnumbered interfaces.

{{%notice warning%}}
When you enable or disable OSPF, the FRR service restarts, which might impact traffic.
{{%/notice%}}

### OSPFv2 Numbered

To configure OSPF using numbered interfaces, you specify the router ID, IP subnet prefix, and area address. You must put all the interfaces on the switch with an IP address that matches the network subnet into the specified area. OSPF attempts to discover other OSPF routers on those interfaces. Cumulus Linux adds all matching interface network addresses to a type-1 <span style="background-color:#F5F5DC">[LSA](## "Link-State Advertisement")</span> and advertises to discovered neighbors for proper reachability.

If you do not want to bring up an OSPF adjacency on certain interfaces, but want to advertise those networks in the OSPF database, you can configure the interfaces as *passive interfaces*. A passive interface creates a database entry but does not send or receive OSPF hello packets. For example, in a data center topology, the host-facing interfaces do not need to run OSPF, however, you need to advertise the corresponding IP addresses to neighbors.

Network statements can be as inclusive or generic as necessary to cover the interface networks.

The following example commands configure OSPF numbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf-numbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 10.10.10.1/32</li><li>The IP address on swp51 is 10.0.1.0/31</li><li>The router ID is 10.10.10.1</li><li>All the interfaces on the switch with an IP address that matches subnet 10.10.10.1/32 and swp51 with IP address 10.0.1.0/31 are in area 0</li><li>swp1 and swp2 are passive interfaces</li></ul> | <ul><li>The loopback address is 10.10.10.101/32</li><li>The IP address on swp1 is 10.0.1.1/31</li><li>The router ID is 10.10.10.101</li><li>All interfaces on the switch with an IP address that matches subnet 10.10.10.101/32 and swp1 with IP address 10.0.1.1/31 are in area 0.</li></ul> |

{{< tabs "TabID35 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID110 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp51 ip address 10.0.1.0/31
cumulus@leaf01:~$ nv set vrf default router ospf router-id 10.10.10.1
cumulus@leaf01:~$ nv set vrf default router ospf area 0 network 10.10.10.1/32
cumulus@leaf01:~$ nv set vrf default router ospf area 0 network 10.0.1.0/31
cumulus@leaf01:~$ nv set interface swp1 router ospf passive on
cumulus@leaf01:~$ nv set interface swp2 router ospf passive on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1 ip address 10.0.1.1/31
cumulus@spine01:~$ nv set vrf default router ospf router-id 10.10.10.101
cumulus@spine01:~$ nv set vrf default router ospf area 0 network 10.10.10.101/32
cumulus@spine01:~$ nv set vrf default router ospf area 0 network 10.0.1.1/31
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

{{< tabs "TabID156 ">}}
{{< tab "leaf01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf` daemon, then start the FRR service (see {{<link url="FRRouting">}}).

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
    cumulus@leaf01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@leaf01:~$ sudo vtysh
    ...
    leaf01# configure terminal
    leaf01(config)# router ospf
    leaf01(config-router)# ospf router-id 10.10.10.1
    leaf01(config-router)# network 10.10.10.1/32 area 0
    leaf01(config-router)# network 10.0.1.0/31 area 0
    leaf01(config-router)# passive-interface swp1
    leaf01(config-router)# passive-interface swp2
    leaf01(config-router)# exit
    leaf01(config)# exit
    leaf01# write memory
    leaf01# exit
    ```

You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency on certain interfaces:

```
leaf01(config)# router ospf
leaf01(config-router)# passive-interface default
leaf01(config-router)# no passive-interface swp51
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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

1. Edit the `/etc/frr/daemons` file to enable the `ospf` daemon, then start the FRR service (see {{<link url="FRRouting">}}).

2. Edit the `/etc/network/interfaces` file to configure the IP address for the loopback and swp1:

    ```
    cumulus@spine01:~$ sudo nano /etc/network/interfaces
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
    ...
    spine01# configure terminal
    spine01(config)# router ospf
    spine01(config-router)# ospf router-id 10.10.101.1
    spine01(config-router)# network 10.10.10.101/32 area 0
    spine01(config-router)# network 10.0.1.1/31 area 0
    spine01(config-router)# exit
    spine01(config)# exit
    spine01# write memory
    spine01# exit
    ```

You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency on certain interfaces:

```
spine01(config)# router ospf
spine01(config-router)# passive-interface default
spine01(config-router)# no passive-interface swp1
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 ospf router-id 10.10.10.101
 network 10.10.10.101/32 area 0
 network 10.0.1.1/31 area 0
...
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

### OSPFv2 Unnumbered

Unnumbered interfaces are interfaces without unique IP addresses; multiple interfaces share the same IP address. In OSPFv2, unnumbered interfaces do not need unique IP addresses on leaf and spine interfaces and simplify the OSPF database, which reduces the memory footprint and improves SPF convergence times.

To configure an unnumbered interface, take the IP address of loopback interface (called the *anchor*) and use that as the IP address of the unnumbered interface.

{{%notice note%}}
OSPF unnumbered supports {{<link url="#interface-parameters" text="point-to-point interfaces">}} only and does *not* support network statements.
{{%/notice%}}

The following example commands configure OSPF unnumbered on leaf01 and spine01.

{{< img src = "/images/cumulus-linux/ospf-unnumbered.png" >}}

| leaf01 | spine01 |
| ------ | ------- |
| <ul><li>The loopback address is 10.10.10.1/32</li><li>The IP address of the unnumbered interface (swp51) is 10.10.10.1/32</li><li>The router ID is 10.10.10.1</li><li>OSPF is on the loopback interface and on swp51 in area 0</li><li>swp1 and swp2 are passive interfaces</li><li>swp51 is a point-to-point interface (Cumulus Linux requires point-to-point for unnumbered interfaces)</li><ul>|<ul><li>The loopback address is 10.10.10.101/32</li><li>The IP address of the unnumbered interface (swp1) is 10.10.10.101/32</li><li>The router ID is 10.10.10.101</li><li>OSPF is on the loopback interface and on swp1 in area 0</li><li>swp1 is a point-to-point interface (Cumulus Linux requires point-to-point for unnumbered interfaces)</li><ul> |

{{< tabs "TabID306 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID292 ">}}
{{< tab "leaf01 ">}}

Configure the unnumbered interface:

```
cumulus@leaf01:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@leaf01:~$ nv set interface swp51 ip address 10.10.10.1/32
cumulus@leaf01:~$ nv config apply
```

Configure OSPF:

```
cumulus@leaf01:~$ nv set vrf default router ospf router-id 10.10.10.1
cumulus@leaf01:~$ nv set interface lo router ospf area 0
cumulus@leaf01:~$ nv set interface swp51 router ospf area 0
cumulus@leaf01:~$ nv set interface swp1 router ospf passive on
cumulus@leaf01:~$ nv set interface swp2 router ospf passive on
cumulus@leaf01:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "spine01 ">}}

Configure the unnumbered interface:

```
cumulus@spine01:~$ nv set interface lo ip address 10.10.10.101/32
cumulus@spine01:~$ nv set interface swp1 ip address 10.10.10.101/32
cumulus@spine01:~$ nv config apply
```

Configure OSPF:

```
cumulus@spine01:~$ nv set vrf default router ospf router-id 10.10.10.101
cumulus@spine01:~$ nv set interface lo router ospf area 0
cumulus@spine01:~$ nv set interface swp1 router ospf area 0
cumulus@spine01:~$ nv set interface swp1 router ospf network-type point-to-point
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "Linux and vtysh Commands ">}}

{{< tabs "TabID337 ">}}
{{< tab "leaf01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf` daemon, then start the FRR service (see {{<link url="FRRouting">}}).

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

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@leaf01:~$ ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@leaf01:~$ sudo vtysh
    ...
    leaf01# configure terminal
    leaf01(config)# router ospf
    leaf01(config-router)# ospf router-id 10.10.10.1
    leaf01(config-router)# interface swp51
    leaf01(config-if)# ip ospf area 0
    leaf01(config-if)# ip ospf network point-to-point
    leaf01(config-if)# exit
    leaf01(config)# interface lo
    leaf01(config-if)# ip ospf area 0
    leaf01(config-if)# exit
    leaf01(config)# router ospf
    leaf01(config-router)# passive-interface swp1,swp2
    leaf01(config-router)# end
    leaf01# write memory
    leaf01# exit
    ```

   You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency on certain interfaces:

   ```
   leaf01(config)# router ospf
   leaf01(config-router)# passive-interface default
   leaf01(config-router)# no passive-interface swp51
   ```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface lo
 ip ospf area 0
interface swp51
 ip ospf area 0
 ip ospf network point-to-point
router ospf
 ospf router-id 10.10.10.1
 passive-interface swp1,swp2
...
```

{{< /tab >}}
{{< tab "spine01 ">}}

1. Edit the `/etc/frr/daemons` file to enable the `ospf` daemon, then start the FRR service (see {{<link url="FRRouting">}}).

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

3. Run the `ifreload -a` command to load the new configuration:

    ```
    cumulus@spine01:~$ sudo ifreload -a
    ```

4. From the vtysh shell, configure OSPF:

    ```
    cumulus@spine01:~$ sudo vtysh
    ...
    spine01# configure terminal
    spine01(config)# router ospf
    spine01(config)# ospf router-id 10.10.10.101
    spine01(config)# interface swp1
    spine01(config-if)# ip ospf area 0
    spine01(config-if)# ip ospf network point-to-point
    spine01(config-if)# exit
    spine01(config)# interface lo
    spine01(config-if)# ip ospf area 0
    spine01(config-if)# exit
    spine01(config-if)# end
    spine01# write memory
    spine01# exit
    ```

   You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency on certain interfaces:

   ```
   spine01(config)# router ospf
   spine01(config-router)# passive-interface default
   spine01(config-router)# no passive-interface swp1
   ```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface lo
 ip ospf area 0
interface swp1
 ip ospf area 0
 ip ospf network point-to-point
router ospf
 ospf router-id 10.10.10.101
...
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

## Optional OSPFv2 Configuration

This section describes optional configuration. The steps provided in this section assume that you already configured basic OSPFv2 as described in {{<link url="#basic-ospfv2-configuration" text="Basic OSPF Configuration">}}, above.

### Interface Parameters

You can define the following OSPF parameters per interface:
- Network type (point-to-point or broadcast). Broadcast is the default setting. Configure the interface as point-to-point unless you intend to use the Ethernet media as a LAN with multiple connected routers. Point-to-point provides a simplified adjacency state machine so there is no need for DR/BDR election and *LSA reflection*. See {{<exlink url="http://tools.ietf.org/rfc/rfc5309" text="RFC5309">}} for a more information.
  {{%notice note%}}
  Cumulus Linux requires Point-to-point for {{<link url="#ospfv2-unnumbered" text="OSPFv2 unnumbered">}}.
  {{%/notice%}}
- Hello interval. The number of seconds between hello packets sent on the interface. The default is 10 seconds.
- Dead interval. The number of seconds before neighbors declare the router down after they stop hearing
hello packets. The default is 40 seconds.
- Priority in becoming the OSPF Designated Router (DR) on a broadcast interface. The default is priority 1.

The following command example sets the network type to point-to-point.

{{< tabs "TabID644 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp51 router ospf network-type point-to-point
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ip ospf network point-to-point
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example

```
...
interface swp51
 ip ospf network point-to-point
...
```

{{< /tab >}}
{{< /tabs >}}

The following command example sets the hello interval to 5 seconds and the dead interval to 60 seconds. The hello interval and dead interval can be any value between 1 and 65535 seconds.

{{< tabs "TabID568 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp51 router ospf timers hello-interval 5
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ip ospf network hello-interval 5
switch(config-if)# ip ospf network dead-interval 60
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example

```
...
interface swp51
 ip ospf hello-interval 5
 ip ospf dead-interval 60
...
```

{{< /tab >}}
{{< /tabs >}}

The following command example sets the priority to 5 for swp51. The priority can be any value between 0 to 255. 0 configures the interface to never become the OSPF Designated Router (DR) on a broadcast interface.

{{< tabs "TabID612 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp51 router ospf priority 5
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ip ospf network priority 5
switch(config-if)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example

```
...
interface swp51
 ip ospf priority 5
...
```

{{< /tab >}}
{{< /tabs >}}

To see the configured OSPF interface parameter values, run the vtysh `show ip ospf interface` command.

### SPF Timer Defaults

OSPF uses the following default timers to prevent consecutive <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> from overburdening the CPU:

- 0 milliseconds from the initial event until SPF runs
- 50 milliseconds between consecutive SPF runs (the number doubles with each SPF, until it reaches the maximum time between SPF runs)
- 5000 milliseconds maximum between SPFs

The following example commands change the number of milliseconds from the initial event until SPF runs to 80, the number of milliseconds between consecutive SPF runs to 100, and the maximum number of milliseconds between SPFs to 6000.

{{< tabs "TabID607 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set router ospf timers spf delay 80
cumulus@switch:~$ nv set router ospf timers spf holdtime 100
cumulus@switch:~$ nv set router ospf timers spf max-holdtime 6000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# timers throttle spf 80 100 6000
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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

{{< /tab >}}
{{< /tabs >}}

To see the configured SPF timer values, run the vtysh `show ip ospf` command.

### MD5 Authentication

To configure <span style="background-color:#F5F5DC">[MD5](## "Message Digest Algorithm")</span> authentication on the switch, you need to create a key and a key ID, then enable MD5 authentication. The *key ID* must be a value between 1 and 255 that represents the key used to create the message digest. This value must be consistent across all routers on a link. The *key* must be a value with an upper range of 16 characters (longer strings truncate) that represents the actual message digest.

The following example commands create key ID 1 with the key `thisisthekey` and enable MD5 authentication on swp51 on leaf01 and on swp1 on spine01.

{{< tabs "TabID880 ">}}
{{< tab "NVUE Commands ">}}

{{< tabs "TabID909 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ nv set interface swp51 router ospf authentication message-digest-key 1
cumulus@leaf01:~$ nv set interface swp51 router ospf authentication md5-key thisisthekey
cumulus@leaf01:~$ nv set interface swp51 router ospf authentication enable on
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab " spine01">}}

```
cumulus@spine01:~$ nv set interface swp1 router ospf authentication message-digest-key 1
cumulus@spine01:~$ nv set interface swp1 router ospf authentication md5-key thisisthekeynet 
cumulus@spine01:~$ nv set interface swp1 router ospf authentication enable on
cumulus@spine01:~$ nv config apply
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< tab "vtysh Commands ">}}

{{< tabs "TabID929 ">}}
{{< tab "leaf01 ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# interface swp51
leaf01(config-if)# ip ospf authentication message-digest
leaf01(config-if)# ip ospf message-digest-key 1 md5 thisisthekey
leaf01(config-if)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

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
cumulus@spine01:~$ sudo vtysh
...
spine01# configure terminal
spine01(config)# interface swp1
spine01(config-if)# ip ospf authentication message-digest
spine01(config-if)# ip ospf message-digest-key 1 md5 thisisthekey
spine01(config-if)# end
spine01# write memory
spine01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp1
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 thisisthekey
 ...
```

{{< /tab >}}
{{< /tabs >}}

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
To remove existing MD5 authentication hashes, run the vtysh `no ip ospf` command (`no ip ospf message-digest-key 1 md5 thisisthekey`).
{{%/notice%}}
<!-- asked not to document in 5.6
#### Password Obfuscation

By default, when you set MD5 authentication for OSPF neighbors, Cumulus Linux shows the keys in clear text in the NVUE `nv config show` command output, vtysh `show running-config output`, and in the `/etc/frr/frr.conf` file. To configure OSPF to obfuscate the keys instead of showing them in clear text:

{{< tabs "340 ">}}
{{< tab "NVUE Commands ">}}

To enable password obfuscation (show encrypted passwords):

```
cumulus@leaf01:~$ nv set router password-obfuscation enabled
cumulus@leaf01:~$ nv config apply
```

To disable password obfuscation (show clear text passwords):

```
cumulus@leaf01:~$ nv set router password-obfuscation disabled
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

To enable password obfuscation (show encrypted passwords):

```
cumulus@switch:~$ sudo vtysh
...
switch# conf t
switch(config)# service password-obfuscation
switch(config)# end
switch# write memory
switch# exit
```

To disable password obfuscation (show clear text passwords):

```
cumulus@switch:~$ sudo vtysh
...
switch# conf t
switch(config)# no service password-obfuscation
switch(config)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}
-->
### Summarization and Prefix Range

By default, an <span style="background-color:#F5F5DC">[ABR](## "Area Border Router")</span> creates a summary (type-3) <span style="background-color:#F5F5DC">[LSA](## "Link-State Advertisement")</span> for each route in an area and advertises it in adjacent areas. Prefix range configuration optimizes this behavior by creating and advertising one summary LSA for multiple routes. OSPF only allows for route summarization between areas on a ABR.

The following example shows a topology divided into area 0 and area 1. border01 and border02 are <span style="background-color:#F5F5DC">[ABRs](## "Area Border Routers")</span> that have links to multiple areas and perform a set of specialized tasks, such as <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> computation per area and summarization of routes across areas.

{{< img src = "/images/cumulus-linux/ospf-scalability-areas.png" >}}

On border01:
- swp1 is in area 1 with IP addresses 10.0.0.24/31, 172.16.1.1/32, 172.16.1.2/32, and 172.16.1.3/32
- swp51 is in area 0 with IP address 10.0.1.9/31

These commands create a summary route for all the routes in the range 172.16.1.0/24 in area 0:

{{< tabs "TabID697 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@leaf01:~$ nv show vrf default router ospf area 0 range 172.16.1.0/24
cumulus@leaf01:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@leaf01:~$ sudo vtysh
...
leaf01# configure terminal
leaf01(config)# router ospf
leaf01(config-router)# area 0 range 172.16.1.0/24
leaf01(config-router)# end
leaf01# write memory
leaf01# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
cumulus@border01:mgmt:~$ sudo cat /etc/frr/frr.conf
...
interface lo
 ip ospf area 0
interface swp1
 ip ospf area 1
interface swp2
 ip ospf area 1
interface swp51
 ip ospf area 0
interface swp52
 ip ospf area 0
router ospf
 ospf router-id 10.10.10.63
 area 0 range 172.16.1.0/24
```

{{< /tab >}}
{{< /tabs >}}

### Stub Areas

External routes are the routes redistributed into OSPF from another protocol. They have an AS-wide flooding scope. Typically, external link states make up a large percentage of the link-state database (LSDB). Stub *areas* reduce the <span style="background-color:#F5F5DC">[LSDB](## "Link State Database")</span> size by not flooding AS-external LSAs.

All routers must agree that an area is a stub, otherwise they do not become OSPF neighbors.

To configure a stub area:

{{< tabs "TabID1065 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf area 1 type stub
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 1 stub
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.63
 area 1 stub
...
```

{{< /tab >}}
{{< /tabs >}}

Stub areas still receive information about networks that belong to other areas of the same OSPF domain. If summarization is not configured (or is not comprehensive), the information can be overwhelming for the nodes. *Totally stubby areas* address this issue. Routers in totally stubby areas keep information about routing within their area in their LSDB.

To configure a totally stubby area:

{{< tabs "TabID860 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf area 1 type totally-stub 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 1 stub no-summary
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.63
 area 1 stub no-summary
...
```

{{< /tab >}}
{{< /tabs >}}

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

{{< tabs "TabID920 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf reference-bandwidth 9000
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# auto-cost reference-bandwidth 90000
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 10.10.10.1
 auto-cost reference-bandwidth 90000
...
```

{{< /tab >}}
{{< /tabs >}}

### Administrative Distance

Cumulus Linux uses the administrative distance to choose which routing protocol to use when two different protocols provide route information for the same destination. The smaller the distance, the more reliable the protocol. For example, if the switch receives a route from OSPF with an administrative distance of 110 and the same route from <span style="background-color:#F5F5DC">[BGP](## "Border Gateway Protocol")</span> with an administrative distance of 100, the switch chooses BGP.

Cumulus Linux provides several commands to change the distance for OSPF routes. The default value is 110.

The following example commands set the distance for an entire group of routes:

{{< tabs "TabID1256 ">}}
{{< tab "NVUE Commands ">}}

The NVUE command is not supported.

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# distance 254
switch(config-router)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example commands change the OSPF administrative distance to 150 for internal routes and 220 for external routes:

{{< tabs "TabID1045 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf distance intra-area 150 
cumulus@switch:~$ nv set vrf default router ospf distance inter-area 150
cumulus@switch:~$ nv set vrf default router ospf distance external 220
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# distance ospf intra-area 150 inter-area 150 external 220
switch(config-router)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example commands change the OSPF administrative distance to 150 for internal routes to a subnet or network inside the same area as the router:

{{< tabs "TabID1076 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf distance intra-area 150 
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# distance ospf intra-area 150
switch(config-router)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

The following example commands change the OSPF administrative distance to 150 for internal routes to a subnet in an area of which the router is *not* a part:

{{< tabs "TabID1364 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf distance inter-area 150
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# distance ospf inter-area 150
switch(config-router)# end
switch# write memory
switch# exit
```

The vtysh commands save the configuration to the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
  ospf router-id 10.10.10.1
  distance ospf intra-area 150 inter-area 150 external 220
...
```

{{< /tab >}}
{{< /tabs >}}

### Topology Changes and OSPF Reconvergence

When you remove a router or OSPF interface, <span style="background-color:#F5F5DC">[LSA](## "Link-State Advertisement")</span> updates trigger throughout the network to inform all routers of the topology change. When the switch receives the LSA and runs OSPF, a routing update occurs. This can cause short-duration outages while the network detects the failure and updates the OSPF database.

With a planned outage (such as during a maintenance window), you can configure the OSPF router with an OSPF max-metric to notify its neighbors not to use it as part of the OSPF topology. While the network converges, all traffic forwarded to the max-metric router is still forwarded. After you update the network, the max-metric router no longer receives any traffic and you can configure the max-metric setting. To remove a single interface, you can configure the OSPF cost for that specific interface.

For failure events, traffic loss can occur during reconvergence (until <span style="background-color:#F5F5DC">[SPF](## "Shortest Path First")</span> on all nodes computes an alternative path around the failed link or node to each of the destinations).

To configure the max-metric (for all interfaces):

{{< tabs "TabID1010 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set vrf default router ospf max-metric administrative on
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# router ospf
switch(config-router)# max-metric router-lsa administrative
switch(config-router)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

To configure the cost (for a specific interface):

{{< tabs "TabID1441 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface swp51 router ospf cost 65535
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "vtysh Commands ">}}

```
cumulus@switch:~$ sudo vtysh
...
switch# configure terminal
switch(config)# interface swp51
switch(config-if)# ospf cost 65535
switch(config-if)# end
switch# write memory
switch# exit
```

{{< /tab >}}
{{< /tabs >}}

## Troubleshooting

NVUE provides several commands to show OSPF interface and OSPF neighbor configuration and statistics.

{{%notice note%}}
- The NVUE commands show brief output. To show more detailed operational information, run the NVUE commands with the ` --operational -o json` option or run the vtysh commands.
- The following NVUE `nv show` commands support OSPF *numbered* only.
{{%/notice%}}

| Description | <div style="width:330px">NVUE Command |
| ----------- | ------------------------------------- |
| `nv show vrf <vrf> router ospf interface` | Shows all OSPF interfaces. |
| `nv show vrf <vrf> router ospf interface <interface>` | Shows information about a specific OSPF interface. |
| `nv show vrf <vrf> router ospf interface <interface> local-ip` | Shows the local IP addresses for the specified OSPF interface. |
| `nv show vrf <vrf> router ospf interface <interface> local-ip <IPv4_address>` | Shows statistics for a specific OSPF interface local IP address. |
| `nv show vrf <vrf> router ospf neighbor` | Shows the OSPF neighbor ID and the OSPF interface for all OSPF neighbors. |
| `nv show vrf <vrf> router ospf neighbor <IPv4-address>` | Shows the interface and local IP addresses for a specific OSPF neighbor. |
| `nv show vrf <vrf> router ospf neighbor <IPv4-address> interface` | Shows the local IP addresses of all the interfaces for an OSPF neighbor. |
| `nv show vrf <vrf> router ospf neighbor <IPv4-address> interface <interface> local-ip` | Shows the local IP addresses for a specific OSPF neighbor interface. |
| `nv show vrf <vrf> router ospf neighbor <IPv4-address> interface <interface> local-ip <IPv4-address>` | Shows statistics for a specific OSPF neighbor interface local IP address. |

The following example shows all OSPF interfaces:

```
cumulus@leaf01:mgmt:~$ nv show vrf default router ospf interface
Interface  Summary             
---------  --------------------
lo         local-ip: 10.10.10.1
swp51      local-ip:   10.0.1.0
```

The following example shows the OSPF neighbor ID and the OSPF interface for all OSPF neighbors:

```
cumulus@switch:~$ nv show vrf default router ospf neighbor
              Summary         
------------  ----------------
10.10.10.101  Interface: swp51
```

The following example shows detailed OSPF neighbor information, which includes statistics:

```
cumulus@leaf01:mgmt:~$ nv show vrf default router ospf neighbor --operational -o json
{
  "10.10.10.101": {
    "interface": {
      "swp51": {
        "local-ip": {
          "10.0.1.0": {
            "bdr-router-id": "10.10.10.101",
            "dead-timer-expiry": 33519,
            "dr-router-id": "10.10.10.1",
            "neighbor-ip": "10.0.1.1",
            "priority": 1,
            "role": "BDR",
            "state": "full",
            "statistics": {
              "db-summary-qlen": 0,
              "ls-request-qlen": 0,
              "ls-retrans-qlen": 0,
              "state-changes": 5
            }
          }
        }
      }
    }
  }
}
```

The following example shows the interface and local IP addresses for OSPF neighbor 10.10.10.101.

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.101
Interface  Summary             
---------  --------------------
swp51      local-ip: 10.0.1.0
```

The following example shows more detailed information for OSPF neighbor 10.10.10.101 and includes statistics:

```
cumulus@switch:~$ nv show vrf default router ospf neighbor 10.10.10.101 --operational -o json
{
  "interface": {
    "swp51": {
      "local-ip": {
        "10.0.1.0": {
          "bdr-router-id": "10.10.10.101",
          "dead-timer-expiry": 30794,
          "dr-router-id": "10.10.10.1",
          "neighbor-ip": "10.0.1.1",
          "priority": 1,
          "role": "BDR",
          "state": "full",
          "statistics": {
            "db-summary-qlen": 0,
            "ls-request-qlen": 0,
            "ls-retrans-qlen": 0,
            "state-changes": 5
          }
        }
      }
    }
  }
}
```

The following example shows configuration and statistics for OSPF neighbor 10.10.10.101 on interface swp51 with the local IP address 10.10.10.1:

```
cumulus@leaf01:mgmt:~$ nv show vrf default router ospf neighbor 10.10.10.101 interface swp51 local-ip 10.0.1.0
                   operational   applied
-----------------  ------------  -------
bdr-router-id      10.10.10.101         
dead-timer-expiry  30042                
dr-router-id       10.10.10.1           
neighbor-ip        10.0.1.1             
priority           1                    
role               BDR                  
state              full                 
statistics                              
  db-summary-qlen  0                    
  ls-request-qlen  0                    
  ls-retrans-qlen  0                    
  state-changes    5    
```

FRR (vtysh) provides several OSPF troubleshooting commands:

| Description | <div style="width:330px">vtysh Command |
| ----------- | ------------------------------------- |
| `show ip ospf neighbor` | Shows OSPF neighbor information. |
| `show ip ospf database` | Shows if the LSDB synchronizes across all routers in the network. |
| `show ip route ospf` | Shows if Cumulus Linux does not forward an OSPF route properly. |
| `show ip ospf interface` | Shows OSPF interfaces. |
| `show ip ospf` | Shows information about the OSPF process. |

The following example shows OSPF neighbor information:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip ospf neighbor
Neighbor ID     Pri State           Dead Time Address         Interface                        RXmtL RqstL DBsmL
10.10.10.101      1 Full/Backup       30.307s 10.0.1.1        swp51:10.0.1.0                       0     0     0
```

The following example shows if Cumulus Linux does not forward an OSPF route properly:

```
cumulus@leaf01:mgmt:~$ sudo vtysh
...
leaf01# show ip route ospf
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR, f - OpenFabric,
       > - selected route, * - FIB route, q - queued route, r - rejected route

O   10.0.1.0/31 [110/100] is directly connected, swp51, weight 1, 00:02:37
O   10.10.10.1/32 [110/0] is directly connected, lo, weight 1, 00:02:37
O>* 10.10.10.101/32 [110/100] via 10.0.1.1, swp51, weight 1, 00:00:57
```

To capture OSPF packets, run the `sudo tcpdump -v -i swp1 ip proto ospf` command.

### Clear OSPF Counters

You can run the following commands to clear the OSPF counters shown in the NVUE show commands.
- `nv action clear vrf <vrf> router ospf interface` clears all counters for all OSPF interfaces.
- `nv action clear vrf <vrf> router ospf interface <interface>` clears all counters for a specific OSPF interface.

The following example command clears all counters for OSPF interface swp51:

```
cumulus@leaf01:mgmt:~$ nv action clear vrf default router ospf interface swp51
...
Action succeeded
```

## Related Information
<!-- vale off -->
- {{<exlink url="http://docs.frrouting.org/en/latest/ospfd.html" text="FRR OSPFv2">}}
- Perlman, Radia (1999); *Interconnections: Bridges, Routers, Switches, and Internetworking Protocols (2 ed.)*; Addison-Wesley
- Moy, John T.; *OSPF: Anatomy of an Internet Routing Protocol*; Addison-Wesley
- {{<exlink url="https://tools.ietf.org/html/rfc2328" text="RFC 2328 OSPFv2">}}
- {{<exlink url="https://tools.ietf.org/html/rfc3101" text="RFC 3101 OSPFv2 Not-So-Stubby Area (NSSA)">}}
<!-- vale on -->
