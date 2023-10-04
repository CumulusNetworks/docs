---
title: Open Shortest Path First - OSPF
author: NVIDIA
weight: 790
toc: 3
---
OSPF maintains the view of the network topology conceptually as a directed graph. Each router represents a vertex in the graph. Each link between neighboring routers represents a unidirectional edge and has an associated weight (called cost) that is either automatically derived from its bandwidth or administratively assigned. Using the weighted topology graph, each router computes a shortest path tree (SPT) with itself as the root, and applies the results to build its forwarding table. The computation is generally referred to as *SPF computation* and the resultant tree as the *SPF tree*.

An LSA (*link-state advertisement*) is the fundamental piece of information that OSPF routers exchange with each other. It seeds the graph building process on the node and triggers SPF computation. LSAs originated by a node are distributed to all the other nodes in the network through a mechanism called *flooding*. Flooding is done hop-by-hop. OSPF ensures reliability by using link state acknowledgement packets. The set of LSAs in a router's memory is termed *link-state database* (LSDB) and is a representation of the network graph. OSPF ensures a consistent view of the LSDB on each node in the network in a distributed fashion, which is key to the protocol's correctness.

This topic describes OSPFv2, which is a {{<exlink url="http://en.wikipedia.org/wiki/Link-state_routing_protocol" text="link-state routing protocol">}} for IPv4. For IPv6 commands, refer to {{<link url="Open-Shortest-Path-First-v3-OSPFv3">}}.

## Scalability and Areas

The OSPF protocol advocates hierarchy as a *divide and conquer* approach to achieve high scale. You can divide the topology into areas, resulting in a two-level hierarchy. Area 0 (or 0.0.0.0), called the backbone area, is the top level of the hierarchy. Packets traveling from one non-zero area to another must go through the backbone area. For example, you can divide the leaf-spine topology into the following areas:

{{< img src = "/images/cumulus-linux/ospf-areas.png" >}}

{{%notice note%}}

- Routers R3, R4, R5, R6 are *area border routers* (ABRs). These routers have links to multiple areas and perform a set of specialized tasks, such as SPF computation per area and summarization of routes across areas.
- Most of the LSAs have an area-level flooding scope. These include router LSA, network LSA, and summary LSA.
- Where ABRs do not connect to multiple non-zero areas, you can use the same area address.

{{%/notice%}}

## Configure OSPFv2

Before you configure OSPF, you need to identify:

- Which router has the router ID
- With which device the router communicates
- What information to advertise (the prefix reachability)

To configure OSPF, you specify the router ID, IP subnet prefix, and area address. All the interfaces on the router whose IP address matches the `network` subnet are put into the specified area. The OSPF process starts bringing up peering adjacency on those interfaces. It also advertises the interface IP addresses formatted into LSAs (of various types) to the neighbors for proper reachability.

If you do not want to bring up OSPF adjacency on certain interfaces, you can configure the interfaces as *passive interfaces*. For example, in a data center topology, the host-facing interfaces do not need to run OSPF, however, the corresponding IP addresses still need to be advertised to neighbors.

{{%notice note%}}

The subnets can be as inclusive as possible to cover the highest number of interfaces on the router that run OSPF.

{{%/notice%}}

The example commands below perform the following configuration:

- Set the router ID to 0.0.0.1
- Put all the interfaces on the router whose IP address matches subnet 10.0.0/16 into area 0.0.0.0.
- Put all interfaces on the router whose IP address matches subnet 192.0.2.0/16 into area 0.0.0.1.
- Set swp10 and swp11 as passive interfaces.

{{< tabs "TabID0" >}}

{{< tab "NCLU Commands" >}}

{{%notice info%}}
When you commit a change that configures a new routing service such as OSPF, the FRR daemon restarts and might interrupt network operations for other configured routing services.
{{%/notice%}}

```
cumulus@switch:~$ net add ospf router-id 0.0.0.1
cumulus@switch:~$ net add ospf network 10.0.0.0/16 area 0.0.0.0
cumulus@switch:~$ net add ospf network 192.0.2.0/16 area 0.0.0.1
cumulus@switch:~$ net add ospf passive-interface swp10
cumulus@switch:~$ net add ospf passive-interface swp11
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice note%}}

Instead of configuring the IP subnet prefix with an area address per network with the `net add ospf` `network` command, you can configure OSPF *per interface* with the `net add interface` command. However, you cannot use both configuration methods at the same time. Here is an example of configuring OSPF per interface:

```
cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.0 
```

{{%/notice%}}

You can use the `net add ospf` `passive-interface default` command to set all interfaces as *passive* and the `net del ospf` `passive-interface <interface>` command to selectively bring up protocol adjacency only on certain interfaces:

```
cumulus@switch:~$ net add ospf passive-interface default
cumulus@switch:~$ net del ospf passive-interface swp1
```

To redistribute protocol routes, run the `net add ospf redistribute <connected|bgp|zebra>` command. Redistribution loads the database unnecessarily with type-5 LSAs. Only use this method to generate real external prefixes (type-5 LSAs). For example:

```
cumulus@switch:~$ net add ospf redistribute connected
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

1. Enable the `ospf` daemon, then start the FRRouting service. See {{<link url="Configuring-FRRouting">}}.

2. From the vtysh shell, configure OSPF.

   ```
   cumulus@switch:~$ sudo vtysh

   switch# configure terminal
   switch(config)# router ospf
   switch(config-router)# router-id 0.0.0.1
   switch(config-router)# network 10.0.0.0/16 area 0.0.0.0
   switch(config-router)# network 192.0.2.0/16 area 0.0.0.1
   switch(config-router)# passive-interface swp10
   switch(config-router)# passive-interface swp11
   switch(config-router)# exit
   switch(config)# exit
   switch# write memory
   switch# exit
   cumulus@switch:~$
   ```

   {{%notice note%}}

Instead of configuring the IP subnet prefix and area address per network with the `router ospf` `network` command, you can configure OSPF *per interface* with the `interface` command. However, you cannot use both configuration methods at the same time. Here is an example of configuring OSPF per interface:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ip ospf area 0.0.0.0
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{%/notice%}}

You can use the `passive-interface default` command to set all interfaces as *passive* and selectively bring up protocol adjacency only on certain interfaces:

```
switch(config)# router ospf
switch(config-router)# passive-interface default
switch(config-router)# no passive-interface swp1
```

To redistribute protocol routes, run the `redistribute <connected|bgp|zebra>` command. Redistribution loads the database unnecessarily with type-5 LSAs. Only use this method to generate real external prefixes (type-5 LSAs). For example:

```
switch(config)# router ospf
switch(config-router)# redistribute connected
```

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
router-id 0.0.0.1
network 10.0.0.0/30 area 0.0.0.0
network 192.0.2.0/16 area 0.0.0.1
passive-interface swp10
passive-interface swp11
...
```

### Define Custom OSPF Parameters on Interfaces

You can define additional custom parameters for OSPF per interface, such as the network type (point-to-point or broadcast) and the interval between hello packets that OSPF sends on the interface.

Configure the interface as point-to-point unless you intend to use the Ethernet media as a LAN with multiple connected routers. Point-to-point has the additional advantage of a simplified adjacency state machine; there is no need for DR/BDR election and *LSA reflection*. See {{<exlink url="http://tools.ietf.org/rfc/rfc5309" text="RFC5309">}} for a more information.

The following command example sets the network type to point-to-point and the hello interval to 5 seconds. The hello interval can be any value between 1 and 65535 seconds.

{{< tabs "TabID2" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add interface swp1 ospf network point-to-point
cumulus@switch:~$ net add interface swp1 ospf hello-interval 5
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp1
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
interface swp1
 ip ospf area 0.0.0.1
 ip ospf hello-interval 5
 ip ospf network point-to-point
...
```

### SPF Timer Defaults

OSPF uses the following default timers to prevent consecutive SPFs from overburdening the CPU:

- 0 milliseconds from the initial event until SPF runs
- 50 milliseconds between consecutive SPF runs (the number doubles with each SPF, until it reaches the value of C)
- 5000 milliseconds maximum between SPFs

The following example commands change the number of milliseconds from the initial event until SPF runs to 80, the number of milliseconds between consecutive SPF runs to 100, and the maximum number of milliseconds between SPFs to 6000.

{{< tabs "TabID4" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add ospf timers throttle spf 80 100 6000 
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

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
 router-id 0.0.0.1
 timers throttle spf 80 100 6000
...
```

### Configure MD5 Authentication

To configure MD5 authentication on the switch, you need to create a key and a key ID, then enable MD5 authentication. The *key ID* must be a value between 1 and 255 that represents the key used to create the message digest. This value must be consistent across all routers on a link. The *key* must be a value with an upper range of 16 characters (longer strings are truncated) that represents the actual message digest.

The following example commands create key ID 1 with the key `thisisthekey` and enable MD5 authentication on swp1.

{{< tabs "TabID6" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add interface swp1 ospf message-digest-key 1 md5 thisisthekey
cumulus@switch:~$ net add interface swp1 ospf authentication message-digest
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{%notice info%}}

You can remove existing MD5 authentication hashes with the `net del` command. For example, `net del interface swp1 ospf message-digest-key 1 md5 thisisthekey`

{{%/notice%}}

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ip ospf authentication message-digest
switch(config-if)# ip ospf message-digest-key 1 md5 thisisthekey
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{%notice info%}}

You can remove existing MD5 authentication hashes with the `no ip ospf message-digest-key` command. For example, `no ip ospf message-digest-key 1 md5 thisisthekey`

{{%/notice%}}

{{< /tab >}}

{{< /tabs >}}

The NCLU and `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
interface swp1
 ip ospf authentication message-digest
 ip ospf message-digest-key 1 md5 thisisthekey
 ...
```

## Summarization

By default, an ABR creates a summary (type-3) LSA for each route in an area and advertises it in adjacent areas. Prefix range configuration optimizes this behavior by creating and advertising one summary LSA for multiple routes.

The following example commands create a summary route for all the routes in the range 30.0.0.0/8 in area 0.0.0.1:

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 0.0.0.1 range 30.0.0.0/8
switch(config-router)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

The `vtysh` commands save the configuration in the `/etc/frr/frr.conf` file. For example:

```
...
router ospf
 router-id 0.0.0.1
 area 0.0.0.1 range 30.0.0.0/8
 ...
```

{{%notice tip%}}

Make sure you configure the summary towards the backbone. The backbone receives summarized routes and injects them to other areas already summarized.

{{%/notice%}}

Summarization can cause *non-optimal* forwarding of packets during failures:

{{< img src = "/images/cumulus-linux/ospf-summarization.png" >}}

The ABRs in the right non-zero area summarize the host prefixes as 10.1.0.0/16.

When the link between R5 and R10 fails, R5 sends a worse metric for the summary route (the metric for the summary route is the maximum of the metrics of intra-area routes that are covered by the summary route). The metric for 10.1.2.0/24 increases at R5 as the path is R5-R9-R6-R10). As a result, other backbone routers shift traffic destined to 10.1.0.0/16 towards R6. This breaks ECMP and is an under-utilization of network capacity for traffic destined to 10.1.1.0/24.

## Stub Areas

External routes are the routes redistributed into OSPF from another protocol. They have an AS-wide flooding scope. In many cases, external link states make up a large percentage of the LSDB. Stub *areas* reduce the link-state database size by not flooding AS-external LSAs.

To configure a stub area:

{{< tabs "TabID8" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add ospf area 0.0.0.1 stub
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 0.0.0.1 stub
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
 router-id 0.0.0.1
 area 0.0.0.1 stub
...
```

Stub areas still receive information about networks that belong to other areas of the same OSPF domain. If summarization is not configured (or is not comprehensive), the information can be overwhelming for the nodes. *Totally stubby areas* address this issue. Routers in totally stubby areas keep information about routing within their area in their LSDB.

To configure a totally stubby area:

{{< tabs "TabID10" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add ospf area 0.0.0.1 stub no-summary
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh

switch# configure terminal
switch(config)# router ospf
switch(config-router)# area 0.0.0.1 stub no-summary
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
 router-id 0.0.0.1
 area 0.0.0.1 stub no-summary
...
```

Here is a brief summary of the area type differences:

| Type| Behavior |
| ----------- | -----------|
| Normal non-zero area | LSA types 1, 2, 3, 4 area-scoped, type 5 externals, inter-area routes summarized |
| Stub area | LSA types 1, 2, 3, 4 area-scoped, no type 5 externals, inter-area routes summarized |
| Totally stubby area | LSA types 1, 2 area-scoped, default summary, no type 3, 4, 5 LSA types allowed |

## Multiple ospfd Instances

The `ospfd` daemon can have up to five independent processes, where each OSPF instance has its own routing table isolated from the others. Each instance must have an ID (any value between 1 and 65535).

{{%notice note%}}

Multiple `ospfd` instances (processes) are supported with:

- The default VRF.
- OSPFv2 only.

{{%/notice%}}

To configure multi-instance OSPF:

1. Edit the `/etc/frr/daemons` file to add `ospfd_instances` to the `ospfd` line. Specify an instance ID for each separate instance. For example, the following configuration enables two `ospfd` instances, 11 and 22:

   ```
   cumulus@switch:~$ cat /etc/frr/daemons
   ...
   bgpd=no
   ospfd=yes ospfd_instances="11 22"
   ospf6d=no
   ripd=no
   ...
   ```

2. {{<cl/restart-frr>}}

3. Assign and enable an OSPF interface for each instance:

{{< tabs "TabID514 ">}}

  {{< tab "NCLU Commands ">}}

  ```
  cumulus@switch:~$ net add interface swp1 ospf instance-id 11
  cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.0
  cumulus@switch:~$ net add ospf router-id 1.1.1.1
  cumulus@switch:~$ net add interface swp2 ospf instance-id 22
  cumulus@switch:~$ net add interface swp2 ospf area 0.0.0.0
  cumulus@switch:~$ net add ospf router-id 1.1.1.1
  cumulus@switch:~$ net pending
  cumulus@switch:~$ net commit
  ```

  {{< /tab >}}

  {{< tab "vtysh Commands ">}}

  ```
  cumulus@switch:~$ sudo vtysh

  switch# configure terminal
  switch(config)# interface swp1
  switch(config-if)#  ip ospf 11 area 0.0.0.0
  switch(config-if)# router ospf 11
  switch(config-router)# ospf router-id 0.0.0.1
  ...
  switch(config)# interface swp2
  switch(config-if)#  ip ospf 22 area 0.0.0.0
  switch(config-if)# router ospf 22
  switch(config-router)# ospf router-id 0.0.0.1
  switch(config-router)# end
  switch# write memory
  switch# exit
  cumulus@switch:~$
  ```

  {{< /tab >}}

{{< /tabs >}}

To confirm that all the OSPF instances are running:

```
cumulus@switch:~$ ps -ax | grep ospf
21135 ?        S<s    0:00 /usr/lib/frr/ospfd --daemon -A 127.0.0.1 -n 11
21139 ?        S<s    0:00 /usr/lib/frr/ospfd --daemon -A 127.0.0.1 -n 22
21160 ?        S<s    0:01 /usr/lib/frr/watchfrr -adz -r /usr/sbin/servicebBfrrbBrestartbB%s -s /usr/sbin/servicebBquaggabBstartbB%s -k /usr/sbin/servicebBfrrbBstopbB%s -b bB -t 30 zebra ospfd-11 ospfd-22 pimd
22021 pts/3    S+     0:00 grep ospf
```

You can use the `redistribute ospf` option with the instance ID in your `frr.conf` file to route between the instances. For example:

```
cumulus@switch:~$ cat /etc/frr/frr.conf
hostname zebra
log file /var/log/frr/zebra.log
username cumulus nopassword
!
service integrated-vtysh-config
!
...
!
router ospf 11
  ospf router-id 0.0.0.1
!
router ospf 22
  ospf router-id 0.0.0.1
  redistribute ospf 11
!
...
```

{{%notice note%}}

If you disable the {{<link url="Configuring-FRRouting" text="integrated">}} FRRouting configuration, you must create a separate `ospfd` configuration file for each instance. The `ospfd.conf` file must include the instance ID in the file name. For example, create `/etc/frr/ospfd-11.conf` and `/etc/frr/ospfd-22.conf`.

```
cumulus@switch:~$ cat /etc/frr/ospfd-11.conf 
!
hostname zebra
log file /var/log/frr/zebra.log
username cumulus nopassword
!
service integrated-vtysh-config
!
interface eth0
  ipv6 nd suppress-ra
  link-detect
!
interface lo
  link-detect
!
interface swp1
  ip ospf 11 area 0.0.0.0
  link-detect
!
interface swp2
  ip ospf 22 area 0.0.0.0
  link-detect
!
interface swp45
  link-detect
!
interface swp46
  link-detect
...
!
router ospf 11
  ospf router-id 0.0.0.1
!
router ospf 22
  ospf router-id 0.0.0.1
!
ip forwarding
ipv6 forwarding
!
line vty
!
```

{{%/notice%}}

## Auto-cost Reference Bandwidth

When you set the *auto-cost reference bandwidth,* Cumulus Linux dynamically calculates the OSPF interface cost to cater for higher speed links. The default value is *100000* for 100Gbps link speed. The cost of interfaces with link speeds lower than 100Gbps is higher.

{{%notice tip%}}

To avoid routing loops, set the bandwidth to a consistent value across all OSPF routers.

{{%/notice%}}

The following example commands configure the auto-cost reference bandwidth for 90Gbps link speed:

{{< tabs "TabID14" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add ospf auto-cost reference-bandwidth 90000
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

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
 router-id 0.0.0.1
 auto-cost reference-bandwidth 90000
...
```

## Unnumbered Interfaces

Unnumbered interfaces are interfaces without unique IP addresses. In OSPFv2, configuring unnumbered interfaces reduces the links between routers into pure topological elements, which simplifies network configuration and reconfiguration. In addition, the routing database contains only the real networks, so the memory footprint is reduced and SPF is faster.

{{%notice note%}}

Unnumbered is supported with point-to-point interfaces only.

{{%/notice%}}

To configure an unnumbered interface, take the IP address of another interface (called the *anchor*) and use that as the IP address of the unnumbered interface:

{{< tabs "TabID16" >}}

{{< tab "NCLU Commands" >}}

Configure the unnumbered interface:

```
cumulus@switch:~$ net add loopback lo ip address 192.0.2.1/32
cumulus@switch:~$ net add interface swp1 ip address 192.0.2.1/32
cumulus@switch:~$ net add interface swp2 ip address 192.0.2.1/32
```

Enable OSPF on the unnumbered interface:

```
cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "Linux and vtysh Commands" >}}

1. Edit the `/etc/network/interfaces` file to configure the unnumbered interface:

   ```
   cumulus@switch:~$ sudo nano /etc/network/interfaces
   ...
   auto lo
   iface lo inet loopback
   address 192.0.2.1/32

   auto swp1
   iface swp1
     address 192.0.2.1/32

   auto swp2
   iface swp2
     address 192.0.2.1/32
   ...
   ```

2. Run the `ifreload -a` command to load the new configuration:

   ```
   cumulus@switch:~$ ifreload -a
   ```

3. From the `vtysh` shell, enable OSPF on an unnumbered interface:

   ```
   cumulus@switch:~$ sudo vtysh

   switch# configure terminal
   switch(config)# interface swp1
   switch(config-if)# ip ospf area 0.0.0.1
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
 ip ospf area 0.0.0.0
...
```

## Apply a Route Map for Route Updates

You can apply a {{<exlink url="http://docs.frrouting.org/en/latest/routemap.html" text="route map">}} to filter route updates from Zebra into the Linux kernel.

{{< tabs "TabID18" >}}

{{< tab "NCLU Commands" >}}

The following example commands apply the route map called `map1`:

```
cumulus@switch:~$ net add routing protocol ospf route-map map1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

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
  ospf router-id 0.0.0.1
  ...
!
ip protocol ospf route-map map1
!
...
```

To apply a route map to redistributed routes:

{{< tabs "TabID20" >}}

{{< tab "NCLU Commands" >}}

The following example commands apply the route map called `map1` to redistributed routes:

```
cumulus@switch:~$ net add ospf redistribute connected route-map map1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

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
 ospf router-id 0.0.0.1
 redistribute connected route-map map1
...
```

## ECMP

During SPF computation for an area, if OSPF finds multiple paths with equal cost, all those paths are used for forwarding. For example, in the reference topology diagram above, R8 uses both R3 and R4 as next hops to reach a destination attached to R9.

## Topology Changes and OSPF Reconvergence

Topology changes usually occur due to router node maintenance or failure, or link maintenance or failure.

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

{{< tabs "TabID22" >}}

{{< tab "NCLU Commands" >}}

```
cumulus@switch:~$ net add interface swp1 ospf cost 65535
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}

{{< tab "vtysh Commands" >}}

```
cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# interface swp1
switch(config-if)# ospf cost 65535
switch(config-if)# end
switch# write memory
switch# exit
cumulus@switch:~$
```

{{< /tab >}}

{{< /tabs >}}

## Troubleshooting

Cumulus Linux provides the following troubleshooting commands for OSPF:

- To show neighbor states, run the NCLU `net show ospf neighbor` command or the vtysh `show ip ospf neighbor` command.
- To verify that the LSDB is synchronized across all routers in the network, run the NCLU `net show ospf database` command or the vtysh `show ip ospf database` command.
- To determine why an OSPF route is not being forwarded correctly, run the NCLU `net show route ospf` command or the vtysh `show ip route ospf` command. These commands show the outcome of the SPF computation downloaded to the forwarding table.
- To capture OSPF packets, run the Linux `sudo tcpdump -v -i swp1 ip proto ospf` command.

The following example shows the `net show route ospf` command output:

```
cumulus@switch:~$ net show route ospf
RIB entry for ospf
==================
Codes: K - kernel route, C - connected, S - static, R - RIP,
       O - OSPF, I - IS-IS, B - BGP, E - EIGRP, N - NHRP,
       T - Table, v - VNC, V - VNC-Direct, A - Babel, D - SHARP,
       F - PBR,
       > - selected route, * - FIB route
O   10.0.0.11/32 [110/0] is directly connected, lo, 00:06:31
O>* 10.0.0.12/32 [110/200] via 10.1.0.0, swp51, 00:06:11
  *                        via 10.1.0.2, swp52, 00:06:11
O>* 10.0.0.13/32 [110/200] via 10.1.0.0, swp51, 00:06:11
  *                        via 10.1.0.2, swp52, 00:06:11
O>* 10.0.0.14/32 [110/200] via 10.1.0.0, swp51, 00:06:11
  *                        via 10.1.0.2, swp52, 00:06:11
O>* 10.0.0.21/32 [110/100] via 10.1.0.0, swp51, 00:06:21
O>* 10.0.0.22/32 [110/100] via 10.1.0.2, swp52, 00:06:21
O   10.1.0.0/31 [110/100] is directly connected, swp51, 00:06:31
O   10.1.0.2/31 [110/100] is directly connected, swp52, 00:06:31
O>* 10.1.0.4/31 [110/200] via 10.1.0.0, swp51, 00:06:21
O>* 10.1.0.6/31 [110/200] via 10.1.0.2, swp52, 00:06:21
O>* 10.1.0.8/31 [110/200] via 10.1.0.0, swp51, 00:06:21
O>* 10.1.0.10/31 [110/200] via 10.1.0.2, swp52, 00:06:21
O>* 10.1.0.12/31 [110/200] via 10.1.0.0, swp51, 00:06:21
O>* 10.1.0.14/31 [110/200] via 10.1.0.2, swp52, 00:06:21
O   172.16.1.0/24 [110/10] is directly connected, br0, 00:06:31
O>* 172.16.2.0/24 [110/210] via 10.1.0.0, swp51, 00:06:11
  *                         via 10.1.0.2, swp52, 00:06:11
O>* 172.16.3.0/24 [110/210] via 10.1.0.0, swp51, 00:06:11
  *                         via 10.1.0.2, swp52, 00:06:11
O>* 172.16.4.0/24 [110/210] via 10.1.0.0, swp51, 00:06:11
  *                         via 10.1.0.2, swp52, 00:06:11
```

For a list all of the OSPF debug options, refer to {{<exlink url="http://docs.frrouting.org/en/latest/ospfd.html#id7" text="Debugging OSPF">}}.

## Related Information

- {{<link url="Bidirectional-Forwarding-Detection-BFD#bfd-in-ospf" text="Bidirectional forwarding detection">}} (BFD) and OSPF
- {{<exlink url="http://en.wikipedia.org/wiki/Open_Shortest_Path_First" text="Wikipedia - Open Shortest Path First">}}
- {{<exlink url="http://docs.frrouting.org/en/latest/ospfd.html" text="FRR OSPFv2">}}
- Perlman, Radia (1999). Interconnections: Bridges, Routers, Switches, and Internetworking Protocols (2 ed.). Addison-Wesley.
- Moy, John T. OSPF: Anatomy of an Internet Routing Protocol. Addison-Wesley.
- {{<exlink url="https://tools.ietf.org/html/rfc2328" text="RFC 2328 OSPFv2">}}
- {{<exlink url="https://tools.ietf.org/html/rfc3101" text="RFC 3101 OSPFv2 Not-So-Stubby Area (NSSA)">}}
