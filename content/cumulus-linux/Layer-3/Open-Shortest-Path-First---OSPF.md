---
title: Open Shortest Path First - OSPF
author: Cumulus Networks
weight: 1815
aliases:
 - /display/CL3740/Open-Shortest-Path-First---OSPF
 - /pages/viewpage.action?pageId=83629226646
pageID: 83629226646
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
<details>

OSPF maintains the view of the network topology conceptually as a
directed graph. Each router represents a vertex in the graph. Each link
between neighboring routers represents a unidirectional edge and each
link has an 
associated weight (called cost) that is either automatically
 derived 
from its bandwidth or administratively assigned. Using the
 weighted 
topology graph, each router computes a shortest path tree (SPT)
 with 
itself as the root, and applies the results to build its forwarding
table. The computation is generally referred to as *SPF computation* and
the resultant tree as the *SPF tree*.

An LSA (*link-state advertisement*) is the fundamental quantumpiece of
information that OSPF routers exchange with each other. It seeds the
graph building process on the node and triggers SPF computation. LSAs
originated by a node are distributed to all the other nodes in the
network through a mechanism called *flooding*. Flooding is done
hop-by-hop. OSPF ensures reliability by using link state acknowledgement
packets. The set of LSAs in a router’s memory is termed *link-state
database* (LSDB), and is a representation of the network graph. Therefore, OSPF
ensures a consistent view of the LSDB on each node in the network in a
distributed fashion (eventual consistency model); this, which is key to the
 protocol’s correctness.

This topic describes OSPFv2, which is a [link-state routing
protocol](http://en.wikipedia.org/wiki/Link-state_routing_protocol) for
IPv4. For IPv6 commands, refer to [Open Shortest Path First v3 -
OSPFv3](/version/cumulus-linux-377/Layer-3display/CL40/Open-+Shortest-+Path-+First-+v3---+-+OSPFv3).

## <span>Scalability and Areas</span>

An increase in the number of nodes affects:

  - Memory footprint to hold the entire network topology

  - Flooding performance

  - SPF computation efficiency

The OSPF protocol advocates hierarchy as a *divide and conquer* approach
to achieve high scale. You can divide the topology into areas, resulting
in a two-level hierarchy. Area 0 (or 0.0.0.0), called the backbone area,
is the top level of the hierarchy. Packets traveling from one non-zero
area to another must go through the backbone area. For example, you can
divide the leaf-spine topology into the following areas:

{{% imgOld 0 %}}

{{%notice note%}}

  - Routers R3, R4, R5, R6 are *area border routers* (ABRs). These
    routers have links to multiple areas and perform a set of
    specialized tasks, such as SPF computation per area and
    summarization of routes across areas.

  - Most of the LSAs have an area-level flooding scope. These include
    router LSA, network LSA, and summary LSA.

  - Where ABRs do not connect to multiple non-zero areas, you can use
    the same area address.

{{%/notice%}}

## <span>Configure OSPFv2</span>

To configure OSPF, you need to:

  - Enable the OSPF daemon

  - Configure OSPF

  - Define custom OSPF parameters on the interfaces

### <span>Enable the OSPF and Zebra Daemons</span>

To enable OSPF, enable the `zebra` and `ospf` daemons, as described in
[Configuring
FRRouting](/version/cumulus-linux-377/Layer-3/Configuring-FRRouting/),
then start the FRRouting service:

    cumulus@switch:~$ sudo systemctl enable frr.service
    cumulus@switch:~$ sudo systemctl start frr.service

### <span>Configure OSPF</span>

Before you configure OSPF, you need to identify:

  - Which router has the router ID

  - With which device the router communicates

  - What information to advertise (the prefix reachability)

To configure OSPF, you specify the router ID, an IP subnet prefix, and an
area 
address. All the interfaces on the router whose IP address matches
 the 
`network` subnet are put into the specified area. The OSPF process
starts bringing up peering adjacency on those interfaces. It also
advertises the interface IP addresses formatted into LSAs (of various
types) to the neighbors for proper reachability.

If you do not want to bring up OSPF adjacency on certain interfaces, you
can configure the interfaces as *passive interfaces*. For example, in a
data center topology, the host-facing interfaces do not need to run
OSPF, however, the corresponding IP addresses still need to be
advertised to neighbors.

{{%notice note%}}

The subnets can be as coarsinclusive as possible to cover the most number of
interfaces on the router that should run OSPF.

    cumulus@switch:~$ net add ospf router-id 0.0.0.1
    cumulus@switch:~$ net add ospf network 10.0.0.0/16 area 0.0.0.0
    cumulus@switch:~$ net add ospf network 192.0.2.0/16 area 0.0.0.1

{{%notice note%}}

You can configure OSPF per interface instead of usinghighest number
of interfaces on the router that run OSPF.

{{%/notice%}}

The example commands below perform the following configuration:

  - Set the router ID to 0.0.0.1

  - Put all the interfaces on the router whose IP address matches subnet
    10.0.0/16 into area 0.0.0.0.

  - Put all interfaces on the router whose IP address matches subnet
    192.0.2.0/16 into area 0.0.0.1.

  - Set swp10 and swp11 as passive interfaces.

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add ospf router-id 0.0.0.1
    cumulus@switch:~$ net add ospf network 10.0.0.0/16 area 0.0.0.0
    cumulus@switch:~$ net add ospf network 192.0.2.0/16 area 0.0.0.1
    cumulus@switch:~$ net add ospf passive-interface swp10
    cumulus@switch:~$ net add ospf passive-interface swp11
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

Instead of configuring the IP subnet prefix with an area address per
network with the `net add ospf`
 `network` command, you can configure
OSPF *per interface* with the `net add interface` command. However, you 
cannot use both configuration methods at
 the same time. Here is an 
example of configuring OSPF per interface:

    cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.0  

{{%/notice%}}

There may be interfaces where it is undesirable toYou can use the `net add ospf` `passive-interface default` command to
set all interfaces as *passive* and the `net del ospf`
`passive-interface <interface>` command to selectively bring up OSPFprotocol
adjacency. For example, in a data center topology, the host-facing
interfaces do not need to run OSPF; however the corresponding IP
addresses still need to be advertised to neighbors. In this scenario,
you can use the `passive-interface` option.

    cumulus@switch:~$ net add ospf passive-interface swp10
    cumulus@switch:~$ net add ospf passive-interface swp11

As an alternative, y only on certain interfaces:

    cumulus@switch:~$ net add ospf passive-interface default
    cumulus@switch:~$ net del ospf passive-interface swp1

To redistribute protocol routes, run the `net add ospf redistribute
<connected|bgp|zebra>` command. Redistribution loads the database
unnecessarily with type-5 LSAs. Only use this method to generate real
external prefixes (type-5 LSAs). For example:

    cumulus@switch:~$ net add ospf redistribute connected
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

1.  Enable the `zebra` and `ospf` daemons, then start the FRRouting
    service. See [Configuring
    FRRouting](/version/cumulus-linux-40/Layer-3/Configuring-FRRouting/).

2.  From the vtysh shell, configure OSPF.
    
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

{{%notice note%}}

Instead of configuring the IP subnet prefix and area address per network
with the `router ospf` `network` command, you can configure OSPF *per
interface* with the `interface` command. However, you cannot use both
configuration methods at the same time. Here is an example of
configuring OSPF per interface:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# interface swp1
    switch(config-if)# ip ospf area 0.0.0.0
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

{{%/notice%}}

You can use the `passive-interface default` command
 to puset all 
interfaces as *passive* and selectively removebring up protocol adjacency only
on certain
 interfaces:

    R3# configure terminal
    R3switch(config)# router ospf
    R3switch(config-router)# passive-interface default
    R3switch(config-router)# no passive-interface swp1

To specify what information to advertise (the prefix reachability), you
can useredistribute protocol routes, run the `redistribution methoe
<connected|bgp|zebra>` command. Redistribution loads the database
unnecessarily with type-5 LSAs. Only use this method to generate real
external prefixes (for example, prefixes learned from BGP). Generate
local prefixes using `network` and/or `type-5 LSAs). For example:

    switch(config)# router ospf
    switch(config-router)# redistribute connected

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf
     router-id 0.0.0.1
     network 10.0.0.0/30 area 0.0.0.0
     network 192.0.2.0/16 area 0.0.0.1
     passive-interface` statements.

    cumulus@switch:~$ net add ospf redistribute connectedwp10
     passive-interface swp11
    ...

### <span>Define Custom OSPF Parameters on the Interfaces</span>

You can define additional custom parameters for OSPF per interface, such 
as the
 network type (point-to-point or broadcast) and the timer tuning, such as
a hello interval.interval
between hello packets that OSPF sends on the interface.

Cumulus Networks recommends that you configure the interface as
point-to-point unless you intend to use the Ethernet media as a LAN with
multiple connected routers. Point-to-point has the additional advantage
of a simplified adjacency state machine; there is no need for DR/BDR
election and *LSA reflection*. See
[RFC5309](http://tools.ietf.org/rfc/rfc5309) for a more information.

The following command example sets the network type to point-to-point
and the hello interval to 5 seconds. The hello interval can be any value
between 1 and 65535 seconds.

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add interface swp1 ospf network point-to-point
    cumulus@switch:~$  net add interface swp1 ospf hello-interval 5

The OSPF configuration is saved in the `/etc/frr/frr.conf` file    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# interface swp1
    switch(config-if)# ospf network point-to-point
    switch(config-if)# ospf network hello-interval 5
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example

    ...
    interface swp1
     ip ospf area 0.0.0.1
     ip ospf hello-interval 5
     ip ospf network point-to-point
    ...

### <span>OSPF SPF Timer Defaults</span>

OSPF uses the following default timers to prevent consecutive SPFs from
overburdening the CPU:

  - 0 milliseconds from the initial event until SPF runs

  - 50 milliseconds between consecutive SPF runs (the number doubles
    with each
    SPF, until it reaches the value of C)

  - 5000 milliseconds maximum between SPFs

### <span>Configure MD5 Authentication for OSPF Neighbors</span>

Simple text passwords have largely been deprecated in FRRouting, in
favor of MD5 hash aThe following example commands change the number of milliseconds from
the initial event until SPF runs to 80, the number of milliseconds
between consecutive SPF runs to 100, and the maximum number of
milliseconds between SPFs to 6000.

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add ospf timers throttle spf 80 100 6000 
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf
    switch(config-router)# timers throttle spf 80 100 6000
    switch(config-router)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf
     router-id 0.0.0.1
     timers throttle spf 80 100 6000
    ...

<span style="color: #36424a;"> Configure MD5 Authentication. </span>

To configure MD5 authentication:

1.  C on the switch, you need to create a key 
and a key ID for MD5 with the `net add interface
    <interface> ospf message-digest-key <KEY, then enable MD5 authentication. The *key ID>* md5 <KEY>` command.  
    `KEYID` is a ust be a
value between 1 and 255 that represents the key used to
    create the 
message digest. This value must be consistent across all
    routers on a 
link.  
    `KEY` isThe *key* must be a value withat has an upper range of 16 characters 
(longer
    strings are truncated) andthat represents the actual message 
digest key
    that is associated with the given `KEYID`.  
    .

The following example commands creates key ID *1*1 with the message
    digest key *__thisisthekey:  
    __*
    
        cumulus@switch:~$ net add interface swp1 ospf message-digest-key 1 md5 thisisthekey
    
    key
`thisisthekey` and enable MD5 authentication on swp1.

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add interface swp1 ospf message-digest-key 1 md5 thisisthekey
    cumulus@switch:~$ net add interface swp1 ospf authentication message-digest
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice info%}}
    
    
You can remove existing MD5 authentication hashes with the `net del
    interface <`
command. For example, `net del interface> swp1 ospf message-digest-key <KEYID> md5 <KEY>`
    command.
    
    {{%/notice%}}

2.  Enable authorization with the `net add interface <interface> ospf
    authentication message-digest` comma1
md5 thisisthekey`

{{%/notice%}}

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# interface swp1
    switch(config-if)# ip ospf authentication message-digest
    switch(config-if)# ip ospf message-digest-key 1 md5 thisisthekey
    switch(config-if)# end.
    
        cumulus@switch:~$ net add interface swp1 ospf authentication message-digest
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit
    
    These commands creates the followingswitch# write memory
    switch# exit
    cumulus@switch:~$

{{%notice info%}}

You can remove existing MD5 authentication hashes with the `no ip ospf
message-digest-key` command. For example, `no ip ospf
message-digest-key 1 md5 thisisthekey`

{{%/notice%}}

The NCLU and `vtysh` commands save the configuration in the
    `/etc/frr/frr.conf` file:
    
        cumulus@switch:~$ sudo cat /etc/frr/frr.conf 
    . For example:

    ... 
        interface swp1
         ip ospf area 0.0.0.0
         ip ospf authentication message-digest
         ip ospf message-digest-key 1 md5 thisisthekey
         ip ospf network point-to-point
         ...

## <span>Scaling Tips</span>

Here are some tips for how to scale out OSPF.

# ...

## <span>Summarization</span>

By default, an ABR creates a summary (type-3) LSA for each route in an
area and advertises it in adjacent areas. Prefix range configuration
optimizes this behavior by creating and advertising one summary LSA for
multiple routes.

To configure a rangehe following example commands create a summary route for all the routes
in the range 30.0.0.0/8 in area 0.0.0.1:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf
    switch(config-router)# area 0.0.0.1 range 30.0.0.0/8
    switch(config-router)# exit
    switch(config)# exitnd
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

{{%notice tip%}}

Summarize in the direction toThe `vtysh` commands save the configuration in the `/etc/frr/frr.conf`
file. For example:

    ... 
    router ospf
     router-id 0.0.0.1
     area 0.0.0.1 range 30.0.0.0/8
    ...

{{%notice tip%}}

Make sure you configure the summary towards the backbone. The backbone 
receives
 summarized routes and injects them to other areas already 
summarized.

{{%/notice%}}

{{%notice note%}}

Summarization can cause *non-optimal* forwarding of packets during
failures. Here is an example scenario:

{{%/notice%}}

{{% imgOld 1 %}}

As shown in the diagram, t:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>{{% imgOld 1 %}}</p></td>
<td><p>The ABRs in the right non-zero area summarize
 the host prefixes as 10.1.0.0/16. </p>
<p>When the link between R5 and R10
 fails, R5 will sends a worse metric for the summary route (the metric for the
 summary route is the maximum of the metrics of intra-area routes that
 are covered by the summary route). Upon failure of the R5-R10 link, the
The metric for 10.1.2.0/24 goes higherincreases at R5 as the path is R5-R9-R6-R10).
 As a result, other backbone routers shift traffic destined to
 10.1.0.0/16 towards R6. This breaks ECMP and is an under-utilization of
 network capacity for traffic destined to 10.1.1.0/24.

### <span>Stub Areas</span>

Nodes in an area receive and store intra-area routing information and
summarized information about other areas from the ABRs. In particular, a
good summarization practice about inter-area routes through prefix range
configuration helps scale the routers and keeps the network stable.

Then there are external routes. </p></td>
</tr>
</tbody>
</table>

## <span>Stub Areas</span>

External routes are the routes
 redistributed into OSPF from another 
protocol. They have an AS-wide
 flooding scope. In many cases, external 
link states make up a large
 percentage of the LSDB.

*S S*tub **areas* alleviate this scaling problem. A stub area is an area
that does not receive ex
reduce the link-state database size by not flooding AS-external LSAs.

To configure a stub area:

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add ospf area 0.0.0.1 stub
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal route advertisements.

To configure a stub area:

    cumulus@switch:~$ net add ospf
    switch(config)# router ospf
    switch(config-router)# area 0.0.0.1 stub
    switch(config-router)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf
     router-id 0.0.0.1
     area 0.0.0.1 stub
    ...

Stub areas still receive information about networks that belong to other
areas of the same OSPF domain. Especially, iIf summarization is not
 configured (or is 
not comprehensive), the information can be
 overwhelming for the nodes. 
*Totally stubby areas* address this issue.
 Routers in totally stubby 
areas keep in their LSDB information about
 routing within their area, plus the default route in their LSDB.

To configure a totally stubby area:

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add ospf area 0.0.0.1 stub no-summary
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf
    switch(config-router)# area 0.0.0.1 stub no-summary
    switch(config-router)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf
     router-id 0.0.0.1
     area 0.0.0.1 stub no-summary
    ...

Here is a brief tabular summary of the area type differences:

| Type                  | Behavior                                                                            |
| --------------------- | ----------------------------------------------------------------------------------- |
| Normal non- zero area | LSA types 1, 2, 3, 4 area-scoped, type 5 externals, inter-area routes summarized    |
| Stub area             | LSA types 1, 2, 3, 4 area-scoped, Nno type 5 externals, inter-area routes summarized |
| Totally stubby area   | LSA types 1, 2 area-scoped, default summary, Nno type 3, 4, 5 LSA types allowed      |

### <span id="src-83629226646_OpenShortestPathFirst-OSPF-multi-instance" class="confluence-anchor-link"></span><span>Multiple ospfd Instances</span>

The `ospfd` daemon can have multiplup to five independent processes.

{{%notice note%}}

  - Multiple `ospfd` processes are only supported in the default VRF.

  - You can run multiple `ospfd` instances with OSPFv2 only.

  - FRRouting supports up to five instances and the instance ID must be
    a value between 1 and 65535, where each
OSPF instance has its own routing table isolated from the others. Each
instance must have an ID (any value between 1 and 65535).

{{%notice note%}}

Multiple `ospfd` instances (processes) are supported with:

  - The default VRF.

  - OSPFv2 only.

{{%/notice%}}

To configure multi-instance OSPF:

1.  Edit the `/etc/frr/daemons` andfile to add *`ospfd\_instances="instance1
    instance2 ..."` ** to the
    `ospfd` line, s. Specifying an instance ID for
    each separate instance. For
    example, the following configuration has
    OSPF enabled with 2enables two `ospfd` instances,
    11 and 22:
    
        cumulus@switch:~$ cat /etc/frr/daemons
        zebra=yes
        bgpd=no
        ospfd=yes ospfd_instances="11 22"
        ospf6d=no
        ripd=no
        ripngd=no
        isisd=no

2.  After you modify the `daemons` file, rRestart FRRouting:
    
        cumulus@switch:~$ sudo systemctl restart frr.service

3.  Configure each instance:Assign and enable an OSPF interface for each instance:
    
    <summary>NCLU Commands </summary>
    
        cumulus@switch:~$ net add interface swp1 ospf instance-id 11  
        cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.0 
        cumulus@switch:~$ net add ospf router-id 1.1.1.1
        cumulus@switch:~$ net add interface swp2 ospf instance-id 22
        cumulus@switch:~$ net add interface swp2 ospf area 0.0.0.0
        cumulus@switch:~$ net add ospf router-id 1.1.1.1

4.  Confirm the configuration:
    
        cumulus@switch:~$ net show configuration ospf
         
        hostname zebra
        log file /var/log/frr/zebra.log
        username cumulus nopassword
         
        service integrated-vtysh-config
        cumulus@switch:~$ net pending
        cumulus@switch:~$ net commit
    
    <summary>vtysh Commands </summary>
    
        cumulus@switch:~$ sudo vtysh
          
        interface eth0
         ipv6 nd suppress-ra
         link-detect
         
        interface lo
         link-detect
         
       switch# configure terminal
        switch(config)# interface swp1
        switch(config-if)#  ip ospf 11 area 0.0.0.0
         link-detect
         
        interface swp2
         ip ospf 22 area 0.0.0.0
         link-detectswitch(config-if)# router ospf 11
        switch(config-router)# ospf router-id 0.0.0.1
         ...
        interface swp45
         link-detect
         
        interface swp46
         link-detect
         
       switch(config)# interface swp472
         link-detect
         
        interface swp48
         link-detect
         
        interface swp49
         link-detect
         
        interface swp50
         link-detect
         
        interface swp51
         link-detect
         
        interface swp52
         link-detect
         
        interface vagrant
         link-detect
         
        router ospf 11
        switch(config-if)#  ip ospf 22 area 0.0.0.0
        switch(config-if)# router ospf 22
        switch(config-router)# ospf router-id 1.1.10.0.0.1
         
        router ospf 22
         ospf router-id 1.1.1.1
         
        ip forwarding
        ipv6 forwarding
         
        line vty
         
        end

5.  Cswitch(config-router)# end
        switch# write memory
        switch# exit
        cumulus@switch:~$ 

To confirm that all the OSPF instances are running:
    
        cumulus@switch:~$ ps -ax | grep ospf
        21135 ?        S<s    0:00 /usr/lib/frr/ospfd --daemon -A 127.0.0.1 -n 11
        21139 ?        S<s    0:00 /usr/lib/frr/ospfd --daemon -A 127.0.0.1 -n 22
        21160 ?        S<s    0:01 /usr/lib/frr/watchfrr -adz -r /usr/sbin/servicebBfrrbBrestartbB%s -s /usr/sbin/servicebBquaggabBstartbB%s -k /usr/sbin/servicebBfrrbBstopbB%s -b bB -t 30 zebra ospfd-11 ospfd-22 pimd
        22021 pts/3    S+     0:00 grep ospf

#### <span>Caveats</span>

You can use the `redistribute ospf` option with the instance ID in your 
`frr.conf` file works
with this so you can route between the instances. Specify the instance
ID for the other OSPF instanceto route between the instances. For example:

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
     ospf router-id 1.1.10.0.0.1
    !
    router ospf 22
     ospf router-id 1.1.10.0.0.1
     redistribute ospf 11
    !
     
    ...

{{%notice note%}}

Don't specify a process ID unless you are using multi-instance OSPF.

{{%/notice%}}

{{%notice note%}}

If you disabled the
[integrated](Configuring-FRRouting.html#src-83629196643_ConfiguringFRRouting-integrated_cfg)
FRRouting configuration, you must create a separate `ospfd`
configuration file for each instance. The `ospfd.conf` file must include
the instance ID in the file name. Continuing with ouFor example, you would
create 
`/etc/frr/ospfd-11.conf` and `/etc/frr/ospfd-22.conf`.

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
    !
    interface swp47
     link-detect
    !
    interface swp48
     link-detect
    !
    interface swp49
     link-detect
    !
    interface swp50
     link-detect
    !
    interface swp51
     link-detect
    !
    interface swp52
     link-detect
    !
    interface vagrant
     link-detect...
    !
    router ospf 11
     ospf router-id 1.1.10.0.0.1
    !
    router ospf 22
     ospf router-id 1.1.10.0.0.1
    !
    ip forwarding
    ipv6 forwarding
    !
    line vty
    !

{{%/notice%}}

### <span id="src-83629226646_OpenShortestPathFirst-OSPF-acrb" class="confluence-anchor-link"></span><span>Auto-cost Reference Bandwidth</span>

*AWhen you set the *auto-cost reference bandwidth,* provides the ability to Cumulus Linux
dynamically
 calculates the OSPF interface cost to cater for higher speed links. You
specify the bandwidth in Mbps and this value is used to calculate the
link speed
links. The default value is *100000*, for 100Gbps link speed. The
 cost of 
interfaces with link speeds lower than 100Gbps is higher.

{{%notice tip%}}

It is a good idea to specify that the bandwidth setting should be a
To avoid routing loops, set the bandwidth to a consistent value across 
all OSPF routers; otherwise routing loops can
occur.

{{%/notice%}}

To.

{{%/notice%}}

The following example commands configure the auto-cost reference 
bandwidth for 90Gbps, run the
following commands: link speed:

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add ospf auto-cost reference-bandwidth 90000
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands create the following configuration in the
`/etc/frr/frr.conf` file:

    cumulus@switch:~$ cat /etc/frr/frr.conf
     <summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# router ospf
    switch(config-router)# auto-cost reference-bandwidth 90000
    switch(config-router)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
     
    router ospf
    auto-cost reference-bandwidth 90000
     
    ...

## <span id="src-8362922_OpenShortestPathFirst-OSPF-ospf_unnum" class="confluence-anchor-link"></span><span>Unnumbered Interfaces</span>

Unnumbered interfaces are interfaces without unique IP addresses. In
OSPFv2, configuring unnumbered interfaces reduces the links between
routers into pure topological elements, which dramatically simplifies
network configuration and reconfiguration. In addition, the routing
database contains only the real networks, so the memory footprint is
reduced and SPF is faster.

{{%notice note%}}

Unnumbered is usable for point-to-point interfaces only.

{{%/notice%}}

{{%notice warning%}}

If there is a `network <network number>/<mask> area <area ID>` command
present in the FRRouting configuration, the `ip ospf area <area ID>`
command is rejected with the error “Please remove network command
first.” This prevents you from configuring other areas on some of the
unnumbered interfaces. You can use either the `network area` command or
the `ospf area` command in the configuration, but not both.

{{%/notice%}}

{{%notice tip%}}

Unless the Ethernet media is intended to be used as a LAN with multiple
connected routers, we recommend configuring the interface as
point-to-point. It has the additional advantage of a simplified
adjacency state machine; there is no need for DR/BDR election and *LSA
reflection*. See [RFC5309](http://tools.ietf.org/rfc/rfc5309) for a more
detailed discussion.

{{%/notice%}}

To configure an unnumbered interface, take the IP address of another
interface (called the *anchor*) and use that as the IP address of the
unnumbered interface:

    cumulus@switch:~$ net add loopback lo ip address 192.0.2.1/32
    cumulus@switch:~$ net add interface swp1 ip address 192.0.2.1/32
    cumulus@switch:~$ net add interface swp2 ip address 192.0.2.1/32

These commands create the following configuration in the
`/etc/network/interfaces` file:

    auto lo
    iface lo inet loopback
      address 192.0.2.1/32
     
    auto swp1
    iface swp1
      address 192.0.2.1/32
     
    auto swp2
    iface swp2
      address 192.0.2.1/32

To enable OSPF on an unnumbered interface:

    cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.1

## <span>Apply a Route Map for Route Updates</span>

To apply a [route map](https://frrouting.org/user-guide/routemap.html)
to filter route updates from Zebra into the Linux kernel:

    cumulus@switch:$ net add routing protocol ospf route-map <route-map-name>

## <span>ECMP</span>

During SPF computation for an area, if OSPF finds multiple paths with
equal cost (metric), all those paths are used for forwarding. For
example, in the reference topology diagram, R8 uses both R3 and R4 as
next hops to reach a destination attached to R9.

## <span>Topology Changes and OSPF Reconvergence</span>

Topology changes usually occur due to one of four events:

1.  Maintenance of a router node

2.  Maintenance of a link

3.  Failure of a router node

4.  Failure of a link

For the maintenance events, operators typically raise the OSPF
administrative weight of the link(s) to ensure that all traffic is
diverted from the link or the node (referred to as *costing out*). The
speed of reconvergence does not matter. Indeed, changing the OSPF cost
causes LSAs to be reissued, but the links remain in service during the
SPF computation process of all routers in the network.

For the failure events, traffic may be lost during reconvergence; that
is, until SPF on all nodes computes an alternative path around the
failed link or node to each of the destinations. The reconvergence
depends on layer 1 failure detection capabilities and at the worst case
*DeadInterval* OSPF timer.

**Example configuration for event 1, using `vtysh`**:

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# router ospf
    switch(config-router)# max-metric router-lsa administrative
    switch(config-router)# exit
    switch(config)# exit
    switch# write mem
    switch# exit
    cumulus@switch:~$ 

**Example configuration for event 2**:

    cumulus@switch:~$ net add interface swp1 ospf cost 65535

## <span id="src-8362922_OpenShortestPathFirst-OSPF-ospf_debug" class="confluence-anchor-link"></span><span>Troubleshooting</span>

  - To debug neighbor states, run the `net show ospf neighbor` command.

  - To capture OSPF packets, run the `sudo tcpdump -v -i swp1 ip proto
    ospf` command.

  - To verify that the LSDB is synchronized across all routers in the
    network, run the `net show ospf database` command.

  - To debug why an OSPF route is not being forwarded correctly, run the
    `net show route ospf` command. This command shows the outcome of the
    SPF computation downloaded to the forwarding table.

[Debugging-OSPF](http://docs.frrouting.org/en/latest/ospfd.html#id7)
lists all of the OSPF debug options.

## <span>Related Information</span>

  - [Bidirectional forwarding
    detection](/version/cumulus-linux-377 router-id 0.0.0.1 
     auto-cost reference-bandwidth 90000 
    ...

## <span id="src-8366646_OpenShortestPathFirst-OSPF-ospf_unnum" class="confluence-anchor-link"></span><span>Unnumbered Interfaces</span>

Unnumbered interfaces are interfaces without unique IP addresses. In
OSPFv2, configuring unnumbered interfaces reduces the links between
routers into pure topological elements, which simplifies network
configuration and reconfiguration. In addition, the routing database
contains only the real networks, so the memory footprint is reduced and
SPF is faster.

{{%notice note%}}

Unnumbered is supported with point-to-point interfaces only.

{{%/notice%}}

To configure an unnumbered interface, take the IP address of another
interface (called the *anchor*) and use that as the IP address of the
unnumbered interface:

<summary>NCLU Commands </summary>

Configure the unnumbered interface:

    cumulus@switch:~$ net add loopback lo ip address 192.0.2.1/32
    cumulus@switch:~$ net add interface swp1 ip address 192.0.2.1/32
    cumulus@switch:~$ net add interface swp2 ip address 192.0.2.1/32

Enable OSPF on the unnumbered interface:

    cumulus@switch:~$ net add interface swp1 ospf area 0.0.0.1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>Linux and vtysh Commands </summary>

1.  Edit the `/etc/network/interfaces` file to configure the unnumbered
    interface:
    
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

2.  Run the `ifreload -a` command to load the new configuration:
    
        cumulus@switch:~$ ifreload -a

3.  From the `vtysh` shell, enable OSPF on an unnumbered interface:
    
        cumulus@switch:~$ sudo vtysh
         
        switch# configure terminal
        switch(config)# interface swp1
        switch(config-if)# ip ospf area 0.0.0.1
        switch(config-if)# end
        switch# write memory
        switch# exit
        cumulus@switch:~$ 

The NCLU and `vtysh` commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    interface swp1
     ip ospf area 0.0.0.0
    ...

## <span>Apply a Route Map for Route Updates</span>

You can apply a [route
map](https://frrouting.org/user-guide/routemap.html) to filter route
updates from Zebra into the Linux kernel.

<summary>NCLU Commands </summary>

The following example commands apply the route map called `map1`:

    cumulus@switch:~$ net add routing protocol ospf route-map map1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

The following example commands apply the route map called `map1`:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# ip protocol ospf route-map map1
    switch(config)# exit
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The NCLU and vtysh commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf
      ospf router-id 0.0.0.1
     ...
    !
    ip protocol ospf route-map map1
    !
    ...

To apply a route map to redistributed routes:

<summary>NCLU Commands </summary>

The following example commands apply the route map called `map1` to
redistributed routes:

    cumulus@switch:~$ net add ospf redistribute connected route-map map1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

The following example commands apply the route map called `map1` to
redistributed routes:

    cumulus@switch:~$ sudo vtysh
     
    switch# configure terminal
    switch(config)# redistribute connected route-map map1
    switch(config)# exit
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

The NCLU and vtysh commands save the configuration in the
`/etc/frr/frr.conf` file. For example:

    ...
    router ospf
      ospf router-id 0.0.0.1
      redistribute connected route-map map1
    ...

## <span>ECMP</span>

During SPF computation for an area, if OSPF finds multiple paths with
equal cost, all those paths are used for forwarding. For example, in the
reference topology diagram above, R8 uses both R3 and R4 as next hops to
reach a destination attached to R9.

## <span>Topology Changes and OSPF Reconvergence</span>

Topology changes usually occur due to router node maintenance or
failure, or link maintenance or failure.

For maintenance events, you can raise the OSPF administrative weight of
the links to ensure that all traffic is diverted from the link or the
node (referred to as *costing out*). The speed of reconvergence does not
matter. Changing the OSPF cost causes LSAs to be reissued, but the links
remain in service during the SPF computation process of all routers in
the network.

For failure events, traffic might be lost during reconvergence (until
SPF on all nodes computes an alternative path around the failed link or
node to each of the destinations). The reconvergence depends on layer 1
failure detection capabilities and the *DeadInterval* OSPF timer.

Example configuration for router maintenance:

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# router ospf
    switch(config-router)# max-metric router-lsa administrative
    switch(config-router)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

Example configuration for link maintenance:

<summary>NCLU Commands </summary>

    cumulus@switch:~$ net add interface swp1 ospf cost 65535
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

<summary>vtysh Commands </summary>

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# interface swp1
    switch(config-if)# ospf cost 65535
    switch(config-if)# end
    switch# write memory
    switch# exit
    cumulus@switch:~$ 

## <span id="src-8366646_OpenShortestPathFirst-OSPF-ospf_debug" class="confluence-anchor-link"></span><span>Troubleshooting</span>

<span style="color: #36424a;"> Cumulus Linux provides the following
troubleshooting commands for OSPF: </span>

  - To show neighbor states, run the NCLU `net show ospf neighbor`
    command or the vtysh `show ip ospf neighbor` command.

  - To verify that the LSDB is synchronized across all routers in the
    network, run the NCLU `net show ospf database` command or the vtysh
    `show ip ospf database` command.

  - To determine why an OSPF route is not being forwarded correctly, run
    the NCLU `net show route ospf` command or the vtysh `show ip route
    ospf` command. These commands show the outcome of the SPF
    computation downloaded to the forwarding table.

  - To capture OSPF packets, run the Linux `sudo tcpdump -v -i swp1 ip
    proto ospf` command.

The following example shows the `net show route ospf` command output:

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

For a list all of the OSPF debug options, refer to
[Debugging-OSPF](http://docs.frrouting.org/en/latest/ospfd.html#id7).

## <span>Related Information</span>

  - [Bidirectional forwarding
    detection](/version/cumulus-linux-40/Layer-3/Bidirectional-Forwarding-Detection---BFD)
    (BFD) and OSPF

  - [en.wikipedia.org/wiki/Open\_Shortest\_Path\_First](http://en.wikipedia.org/wiki/Open_Shortest_Path_First)

  - [FRR OSPFv2](https://frrouting.org/user-guide://docs.frrouting.org/en/latest/ospfd.html)

  - Perlman, Radia (1999). Interconnections: Bridges, Routers, Switches,
    and Internetworking Protocols (2 ed.). Addison-Wesley.

  - Moy, John T. OSPF: Anatomy of an Internet Routing Protocol.
    Addison-Wesley.

  - [RFC 2328 OSPFv2](https://tools.ietf.org/html/rfc2328)

  - [RFC 3101 OSPFv2 Not-So-Stubby Area
    (NSSA)](https://tools.ietf.org/html/rfc3101)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>

</details>
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTYwODY1MTg4NF19
-->