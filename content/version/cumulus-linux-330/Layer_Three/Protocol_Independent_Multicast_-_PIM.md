---
title: Protocol Independent Multicast - PIM
author: Cumulus Networks
weight: 187
aliases:
 - /display/CL330/Protocol+Independent+Multicast+-+PIM
 - /pages/viewpage.action?pageId=5866413
pageID: 5866413
product: Cumulus Linux
version: 3.3.0
imgData: cumulus-linux-330
siteSlug: cumulus-linux-330
---
Protocol Independent Multicast (PIM) is a multicast control plane
protocol, that advertises multicast sources and receivers over a routed
layer 3 network. Layer 3 multicast relies on PIM to advertise
information about multicast capable routers and the location of
multicast senders and receivers. For this reason, multicast cannot be
sent through a routed network without PIM.

PIM has two modes of operation: Sparse Mode (PIM-SM) and Dense Mode
(PIM-DM).

{{%notice note%}}

Cumulus Linux only supports PIM Sparse Mode.

{{%/notice%}}

## <span>PIM Overview</span>

{{% imgOld 0 %}}

| Network Element                                   | Description                                                                                                                                                                                                                                                                                                |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| First Hop Router (FHR)                            | The FHR is the first router attached closest to the source. The FHR is responsible for the PIM register process. Each multicast source will have a single FHR.                                                                                                                                             |
| Last Hop Router (LHR)                             | The LHR is the last router in the path, attached to an interested multicast receiver. There is a single LHR for each network subnet with an interested receiver, however multicast groups can have multiple LHRs throughout the network.                                                                   |
| Rendezvous Point (RP)                             | The RP allows for the discovery of multicast sources and multicast receivers. The RP is responsible for sending PIM Register Stop messages to FHRs.                                                                                                                                                        |
| PIM Shared Tree (RP Tree) or (\*,G) Tree          | The Shared Tree is the multicast tree rooted at the RP. When receivers wish to join a multicast group, messages are sent along the shared tree towards the RP.                                                                                                                                             |
| PIM Shortest Path Tree (SPT) or (S,G) Tree        | The SPT is the multicast tree rooted at the multicast source for a given group. Each multicast source will have a unique SPT. The SPT may match the RP Tree, but this is not a requirement. The SPT represents the most efficient way to send multicast traffic from a source to the interested receivers. |
| Outgoing Interface (OIF)                          | The Outgoing interface indicates the interface a PIM or multicast packet should be sent on. OIFs are the interfaces towards the multicast receivers.                                                                                                                                                       |
| Incoming Interface (IIF)                          | The Incoming Interface indicates the interface a PIM or multicast packet should be received on. IIFs can be the interfaces towards the multicast, or towards the RP.                                                                                                                                       |
| Reverse Path Forwarding Interface (RPF Interface) | Reverse Path Forwarding is the unicast route towards a source or receiver.                                                                                                                                                                                                                                 |
| Multicast Route (mroute)                          | A multicast route indicates the multicast source and multicast group as well as associated OIFs, IIFs, and RPF information.                                                                                                                                                                                |
| Star-G mroute (\*,G)                              | The (\*,G) mroute represents the RP Tree. The \* is a wildcard indicating any multicast source. The G is the multicast group. An example (\*,G) would be (\*, 239.1.2.9).                                                                                                                                  |
| S-G mroute (S,G)                                  | This is the mroute representing the SPT. The S is the multicast source IP. The G is the multicast group. An example (S,G) would be (10.1.1.1, 239.1.2.9).                                                                                                                                                  |

### <span>PIM Messages</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>PIM Message</p></th>
<th><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>PIM Hello</p></td>
<td><p>PIM hellos announce the presence of a multicast router on a segment. PIM hellos are sent every 30 seconds by default.</p>
<pre><code>22.1.2.2 &gt; 224.0.0.13: PIMv2, length 34
 Hello, cksum 0xfdbb (correct)
 Hold Time Option (1), length 2, Value: 1m45s
 0x0000: 0069
 LAN Prune Delay Option (2), length 4, Value: 
 T-bit=0, LAN delay 500ms, Override interval 2500ms
 0x0000: 01f4 09c4
 DR Priority Option (19), length 4, Value: 1
 0x0000: 0000 0001
 Generation ID Option (20), length 4, Value: 0x2459b190
 0x0000: 2459 b190</code></pre></td>
</tr>
<tr class="even">
<td><p>PIM Join/Prune (J/P)</p></td>
<td><p>PIM J/P messages indicate the groups that a multicast router would like to receive or no longer receive. Often PIM Join/Prune messages are described as distinct message types, but are actually a single PIM message with a list of groups to join and a second list of groups to leave. PIM J/P messages can be to join or prune from the SPT or RP trees (also called (*,G) Joins or (S,G) Joins).</p>
<p>{{%notice note%}}</p>
<p>PIM Join/Prune messages are sent to PIM neighbors on individual interfaces. Join/Prune messages are never unicast.</p>
<p>{{%/notice%}}</p>
<p>{{% imgOld 1 %}}</p>
<p>This PIM Join/Prune is for group 239.1.1.9, with 1 Join and 0 Prunes for the group. Join/Prunes for multiple groups can exist in a single packet.</p>
<pre><code>21:49:59.470885 IP (tos 0x0, ttl 255, id 138, offset 0, flags [none], proto PIM (103), length 54)
 22.1.2.2 &gt; 224.0.0.13: PIMv2, length 34
 Join / Prune, cksum 0xb9e5 (correct), upstream-neighbor: 22.1.2.1
 1 group(s), holdtime: 3m30s
 group #1: 225.1.0.0, joined sources: 0, pruned sources: 1
 pruned source #1: 33.1.1.1(S)</code></pre></td>
</tr>
<tr class="odd">
<td><p>PIM Register</p></td>
<td><p>PIM register messages are unicast packets sent from a FHR destined to the RP to advertise a new multicast group. The FHR fully encapsulates the original multicast packet in a PIM register messages. The RP is responsible for decapsulating the PIM register message and forwarding it along the (*,G) tree towards the receivers.</p></td>
</tr>
<tr class="even">
<td><p>PIM Null Register</p></td>
<td><p>PIM Null Register is a special type of PIM Register message where the "Null-Register" flag is set within the packet. Null Register messages are used for a FHR to signal to an RP that a source is still sending multicast traffic. Unlike normal PIM Register messages Null Register messages do not encapsulate the original data packet.</p></td>
</tr>
<tr class="odd">
<td><p>PIM Register Stop</p></td>
<td><p>PIM Register Stop messages are sent by an RP to the FHR to indicate that PIM Register messages should no longer be sent.</p>
<pre><code>21:37:00.419379 IP (tos 0x0, ttl 255, id 24, offset 0, flags [none], proto PIM (103), length 38)
 100.1.2.1 &gt; 33.1.1.10: PIMv2, length 18
 Register Stop, cksum 0xd8db (correct) group=225.1.0.0 source=33.1.1.1</code></pre></td>
</tr>
<tr class="even">
<td><p>IGMP Membership Report (IGMP Join)</p></td>
<td><p>IGMP Membership Reports are sent by multicast receivers to tell multicast routers of their interest in a specific multicast group. IGMP Join messages trigger PIM *,G Joins. IGMP version 2 messages are sent to the All Hosts multicast address, 224.0.0.1. IGMP version 3 messages are sent to an IGMP v3 specific multicast address, 224.0.0.22.</p></td>
</tr>
<tr class="odd">
<td><p>IGMP Leave</p></td>
<td><p>IGMP Leaves tell a multicast router that a multicast receiver no longer wants the multicast group. IGMP Leave messages trigger PIM *,G Prunes.</p></td>
</tr>
</tbody>
</table>

### <span>PIM Neighbors</span>

When PIM is configured on an interface, `PIM Hello` messages are sent to
the link local multicast group 224.0.0.13. Any other router configured
with PIM on the segment that hears the PIM Hello messages will build a
PIM neighbor with the sending device.

{{%notice note%}}

PIM neighbors are stateless. No confirmation of neighbor relationship is
exchanged between PIM endpoints.

{{%/notice%}}

## <span>PIM Sparse Mode (PIM-SM)</span>

PIM Sparse Mode (PIM-SM) is a "pull" multicast distribution method. This
means that multicast traffic is only sent through the network if
receivers explicitly ask for it. When a receiver "pulls" multicast
traffic, the network must be periodically notified that the receiver
wishes to continue the multicast stream.

{{%notice note%}}

This behavior is in contrast to PIM Dense Mode (PIM-DM), where traffic
is flooded, and the network must be periodically notified that the
receiver wishes to stop receiving the multicast stream.

{{%/notice%}}

PIM-SM has three configuration options: Any-source Multicast (ASM),
Bi-directional Multicast (BiDir), and Source Specific Multicast (SSM):

  - Any-source Mulitcast (ASM) is the traditional, and most commonly
    deployed PIM implementation. ASM relies on Rendevous Points to
    connect multicast senders and receivers that then dynamically
    determine the shortest path through the network between source and
    receiver, to efficiently send multicast traffic.

  - Bidirectional PIM (BiDir) forwards all traffic through the multicast
    Rendezvous Point (RP), rather than tracking multicast source IPs,
    allowing for greater scale, while resulting in inefficient
    forwarding of network traffic.

  - Source Specific Multicast (SSM) requires multicast receivers to know
    exactly which source they wish to receive multicast traffic from,
    rather than relying on multicast Rendezvous Points. SSM requires the
    use of IGMPv3 on the multicast clients.

{{%notice note%}}

Cumulus Linux only supports ASM and SSM. PIM BiDir is not currently
supported.

{{%/notice%}}

### <span>Any-source Multicast Routing</span>

Multicast routing behaves differently depending on whether the source is
sending before receivers request the multicast stream, or if a receiver
tries to join a stream before there are any sources.

#### <span>Receiver Joins First</span>

When a receiver joins a group, an IGMP Membership Join message is sent
to the IGMPv3 multicast group, 224.0.0.22. The PIM multicast router for
the segment, listening to the IGMPv3 group, receives the IGMP Membership
Join message, and becomes an LHR for this group.

{{% imgOld 2 %}}

This creates a (\*,G) mroute, with an OIF of the interface on which the
IGMP Membership Report was received and an IIF of the RPF interface for
the RP.

The LHR generates a PIM (\*,G) Join message, and sends it from the
interface towards the RP. Each multicast router between the LHR and the
RP will build a (\*,G) mroute with the OIF being the interface on which
the PIM Join message was received and an Incoming Interface of the
Reverse Path Forwarding interface for the RP.

{{% imgOld 3 %}}

{{%notice note%}}

When the RP receives the (\*,G) Join message, it will not send any
additional PIM Join messages. The RP will maintain a (\*,G) state as
long as the receiver wishes to receive the multicast group.

{{%/notice%}}

{{%notice note%}}

Unlike multicast receivers, multicast sources do not send IGMP (or PIM)
messages to the FHR. A multicast source begins sending and the FHR will
receive the traffic and build both a (\*,G) and an (S,G) mroute. The FHR
will then begin the PIM Register process.

{{%/notice%}}

##### <span>PIM Register Process</span>

When a First Hop Router (FHR) receives a multicast data packet from a
source, the FHR does not know if there are any interested multicast
receivers in the network. The FHR encapsulates the data packet in a
unicast PIM register message. This packet is sourced from the FHR and
destined to the RP address. The RP will build an (S,G) mroute and
decapsulate the multicast packet and forward it along the (\*,G) tree.

As the unencapsulated multicast packet travels down the (\*,G) tree
towards the interested receivers. At the same time, the RP will send a
PIM (S,G) Join towards the FHR. This will build an (S,G) state on each
multicast router between the RP and FHR.

When the FHR receives a PIM (S,G) Join, it will continue encapsulating
and sending PIM Register messages, but will also make a copy of the
packet and send it along the (S,G) mroute.

The RP then receives the multicast packet along the (S,G) tree and sends
a PIM Register Stop to the FHR to end the register process.

{{% imgOld 4 %}}

{{% imgOld 5 %}}

##### <span>PIM SPT Switchover</span>

When the LHR receives the first multicast packet, in order to
efficiently forward traffic through the network, it will send a PIM
(S,G) Join towards the FHR. This builds the Shortest Path Tree (SPT), or
the tree that is the shortest path to the source.

When the traffic arrives over the SPT, a PIM (S,G) RPT Prune will be
sent up the Shared Tree towards the RP. This removes multicast traffic
from the shared tree; multicast data will only be sent over the SPT.

The LHR will now send both (\*,G) Joins and (S,G) RPT Prune messages
towards the RP.

1.  Create the necessary prefix-lists using the Quagga CLI:
    
        cumulus@switch:~$ sudo vtysh
        switch# configure terminal
        switch(config)# ip prefix-list ssm-range permit 232.0.0.0/8 ge 32
        switch(config)# ip prefix-list ssm-range permit 238.0.0.0/8 ge 32

2.  Configure SPT switchover for the `ssm-range` prefix-list:
    
        switch(config)# ip pim spt-switchover infinity-and-beyond prefix-list ssm-range
        switch(config)# ip prefix-list ssm-range seq 5 deny 238.0.0.0/32

The configured prefix-list can be viewed with the `show ip mroute`
command:

    cumulus@switch:~$ show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    *               232.0.0.0       IGMP   swp31s0    pimreg     1    00:03:3
                                    IGMP              br1        1    00:03:38
    *               238.0.0.0       IGMP   swp31s0    br1        1    00:02:08

In the example above, `232.0.0.0` has been configured for SPT
switchover, identified by `pimreg`.

#### <span>Sender Starts Before Receivers Join</span>

As previously mentioned, a multicast sender can send multicast data
without any additional IGMP or PIM signaling. When the FHR receives the
multicast traffic it will encapsulate it and send a PIM Register to the
Rendezvous Point (RP).

When the RP receives the PIM Register, it will build an (S,G) mroute;
however, there is no (\*,G) mroute and no interested receivers.

The RP will drop the PIM Register message and immediately send a PIM
Register Stop message to the FHR.

Receiving a PIM Register Stop without any associated PIM Joins leaves
the FHR without any outgoing interfaces. The FHR will drop this
multicast traffic until a PIM Join is received.

{{%notice note%}}

PIM Register messages are sourced from the interface that received the
multicast traffic and are destined to the RP address. The PIM Register
is not sourced from the interface towards the RP.

{{%/notice%}}

### <span>PIM Null-Register</span>

In order to notify the RP that multicast traffic is still flowing when
the RP has no receiver, or if the RP is not on the SPT tree, the FHR
will periodically send PIM Null Register messages. The FHR sends a PIM
Register with the Null-Register flag set, but without any data. This
special PIM Register notifies the RP that a multicast source is still
sending, should any new receivers come online.

After receiving a PIM Null-Register, the RP immediately sends a PIM
Register Stop to acknowledge the reception of the PIM Null Register
message.

### <span>PIM and ECMP</span>

PIM uses the RPF procedure to choose an upstream interface in order to
build a forwarding state. If equal-cost multipaths (ECMP) are
configured, PIM can use choose the RPF based on ECMP using hash
algorithms. The `ip pim ecmp rebalance` command can be used to rebalance
the traffic across the paths, allowing for all RPFs to be reconfigured,
even if their nexthop is still valid.

    cumulus@switch:~$ sudo vtysh
    switch# configure terminal
    switch(config)# ip pim ecmp rebalance

The `show ip pim nexthop` can be used to review which nexthop will be
selected for a specific source/group:

    cumulus@switch:~$ sudo vtysh
    switch# show ip pim nexthop 
    Number of registered addresses: 3 
    Address         Interface      Nexthop
    -------------------------------------------
    6.0.0.9         swp31s0        169.254.0.9 
    6.0.0.9         swp31s1        169.254.0.25 
    6.0.0.11        lo             0.0.0.0 
    6.0.0.10        swp31s0        169.254.0.9 
    6.0.0.10        swp31s1        169.254.0.25 

## <span>Configuration</span>

### <span>Getting Started</span>

PIM is included in the Quagga package. To configure PIM on a switch:

1.  Open `/etc/quagga/daemons` in a text editor.

2.  Add the following line to the end of the file to enable `pimd`, and
    save the file:
    
        zebra=yes
        pimd=yes

3.  Run the `systemctl restart` command to restart Quagga:
    
        cumulus@switch:~$ sudo systemctl restart quagga

4.  In a terminal, run the `vtysh` command to start the Quagga CLI on
    the switch.
    
        cumulus@switch:~$ sudo vtysh
        cumulus# 

5.  Run the following commands to configure the PIM interfaces:
    
        cumulus# configure terminal
        cumulus(config)# int swp1
        cumulus(config-if)# ip pim sm
    
    {{%notice note%}}
    
    PIM must be enabled on all interfaces facing multicast sources or
    multicast receivers, as well as on the interface where the RP
    address is configured.
    
    {{%/notice%}}

6.  Run the following commands to enable either IGMPv2 or IGMPv3 on the
    interfaces with hosts attached:
    
        cumulus# configure terminal
        cumulus(config)# int swp1 
        cumulus(config-if)# ip igmp version 3
    
    {{%notice note%}}
    
    IGMP must be configured on all interfaces where multicast receivers
    exist.
    
    {{%/notice%}}

7.  Configure a group mapping for a static RP:
    
        cumulus# configure terminal 
        cumulus(config)# ip pim rp 192.168.0.1 224.0.0.0/4
    
    {{%notice note%}}
    
    Each PIM-SM enabled device must configure a static RP to a group
    mapping, and all PIM-SM enabled devices must have the same RP to
    group mapping configuration.
    
    {{%/notice%}}

Complete Multicast Network Configuration Example

The following is example configuration

    RP# show run
    Building configuration...
    Current configuration:
    !
    log syslog
    ip multicast-routing
    ip pim rp 192.168.0.1 224.0.0.0/4
    username cumulus nopassword
    !
    !
    interface lo
     description RP Address interface
     ip ospf area 0.0.0.0
     ip pim sm
    !
    interface swp1
     description interface to FHR
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    interface swp2
     description interface to LHR
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    router ospf
     ospf router-id 192.168.0.1
    !
    line vty
    !
    end

    FHR# show run
    !
    log syslog
    ip multicast-routing
    ip pim rp 192.168.0.1 224.0.0.0/4
    username cumulus nopassword
    !
    interface bridge10.1
     description Interface to multicast source
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    interface lo
     ip ospf area 0.0.0.0
     ip pim sm
    !
    interface swp49
     description interface to RP
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    interface swp50
     description interface to LHR
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    router ospf
     ospf router-id 192.168.1.1
    !
    line vty
    !
    end

    LHR# show run
    !
    log syslog
    ip multicast-routing
    ip pim rp 192.168.0.1 224.0.0.0/4
    username cumulus nopassword
    !
    interface bridge10.1
     description interface to multicast receivers
     ip igmp
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    interface lo
     ip ospf area 0.0.0.0
     ip pim sm
    !
    interface swp49
     description interface to RP
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    interface swp50
     description interface to FHR
     ip ospf area 0.0.0.0
     ip ospf network point-to-point
     ip pim sm
    !
    router ospf
     ospf router-id 192.168.2.2
    !
    line vty
    !
    end

### <span>Source Specific Multicast Mode (SSM)</span>

The source-specific multicast method uses prefix-lists to configure a
receiver to only allow traffic to a multicast address from a single
source. This removes the need for an RP, as the source must be known
before traffic can be accepted. The default range is `232.0.0.0/8`, and
be configured by setting a prefix-list.

The example process below configures a prefix-list named `ssm-range`,
and prefix-lists permitting traffic from `230.0.0.0/8` and
`238.0.0.0/8`, for prefixes longer than 32.

{{%notice warning%}}

PIM considers `232.0.0.0/8` the default range if the ssm range is not
configured. If this default is overridden with a prefix-list, **all**
ranges that should be considered must be in the prefix-list

{{%/notice%}}

    cumulus@switch:~$ net add routing prefix-list ipv4 ssm-range permit 232.0.0.0/8 ge 32
    cumulus@switch:~$ net add routing prefix-list ipv4 ssm range permit 
    cumulus@switch:~$ net add pim ssm prefix-list ssm-range
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This configuration can also be done with the Quagga CLI:

    cumulus@switch:~$ sudo vtysh
    switch# conf t
    switch(config)# ip prefix-list ssm-range seq 5 permit 238.0.0.0/8 ge 32
    switch(config)# ip pim prefix-list ssm-range
    switch(config)# exit
    switch# write mem

To view the existing prefix-lists, use the `net show ip` command:

    cumulus@switch:~S net show ip prefix-list ssm-range
    ZEBRA: ip prefix-list ssm-range: 2 entries
        seq 5 permit 232.0.0.0/8 ge 32
        seq 10 permit 238.0.0.0/8 ge 32
    OSPF: ip prefix-list ssm-range: 2 entries
        seq 5 permit 232.0.0.0/8 ge 32
        seq 10 permit 238.0.0.0/8 ge 32
    PIM: ip prefix-list ssm-range: 2 entries
        seq 5 permit 232.0.0.0/8 ge 32
        seq 10 permit 238.0.0.0/8 ge 32

### <span>Multicast Source Discovery Protocol (MSDP)</span>

The Multicast Source Discovery Protocol (MSDP) is used to connect
multiple PIM-SM multicast domains together, using the PIM-SM RPs. By
configuring any cast RPs with the same IP address on multiple multicast
switches (primarily on the loopback interface), the PIM-SM limitation of
only one RP per multicast group is relaxed. This allows for an increase
in both failover and load-balancing throughout.

When an RP discovers a new source (typically a PIM-SM register message
via TCP), a source-active (SA) message is sent to each MSDP peer. The
peer then determines if any receivers are interested.

{{%notice note%}}

Cumulus Linux MSDP support is primarily for anycast-RP configuration,
rather than multiple multicast domains. Each MSDP peer must be
configured in a full mesh, as SA messages are not received and
re-forwarded.

{{%/notice%}}

{{%notice note%}}

Cumulus Linux currently only supports one MSDP mesh-group.

{{%/notice%}}

#### <span>Configuration</span>

The steps below cover configuring a Cumulus switch to use the MSDP

1.  Add an anycast IP address to the loopback interface for each RP in
    the domain:
    
        cumulus@switch:$ net add loopback lo ip address 10.1.1.1/32
        cumulus@switch:$ net add loopback lo ip address 10.1.1.100/32
        cumulus@switch:$ net pending
        cumulus@switch:$ net commit

2.  On every multicast switch, configure the group to RP mapping using
    the anycast address:
    
        cumulus@switch:$ net add pim rp 100.1.1.100 224.0.0.0/4
        cumulus@switch:$ net pending
        cumulus@switch:$ net commit

3.  Log into the Quagga CLI:
    
        cumulus@switch:$ sudo vtysh

4.  Configure the MSDP mesh group for all active RPs:
    
    {{%notice note%}}
    
    The mesh group should include all RPs in the domain as members, with
    a unique address as the source. This configuration will result in
    MSDP peerings between all RPs.
    
    {{%/notice%}}
    
        switch# conf t
        switch(config)# ip msdp mesh-group cumulus source 100.1.1.1
        switch(config)# ip msdp mesh-group cumulus source 100.1.1.2
        switch(config)# ip msdp mesh-group cumulus source 100.1.1.3

5.  Inject the anycast IP address into the domain's IGP.

{{%notice note%}}

If the network is unnumbered and uses unnumbered BGP as the IGP, avoid
using the anycast IP address for establishing unicast or multicast
peerings. For PIM-SM, ensure that the unique address is used as the PIM
hello source by setting the source:

    cumulus@switch:$ sudo vtysh
    switch# conf t
    switch(config)# interface lo
    switch(config-if)# ip pim use-source 100.1.1.1

{{%/notice%}}

### <span>Verifying PIM</span>

{{%notice note%}}

The following outputs are based on the [Cumulus Reference
Topology](https://github.com/CumulusNetworks/cldemo-vagrant) with
cldemo-pim.

{{%/notice%}}

#### <span>Source Starts First</span>

On the FHR, an mroute is built, but the upstream state is "Prune". The
FHR flag is set on the interface receiving multicast.

Use the `show ip mroute` command to review detailed output for the FHR:

    exit01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    172.16.5.105    239.1.1.1       none   br0        none       0    --:--:--
    !
    exit01# show ip pim upstream
    Iif Source Group State Uptime JoinTimer RSTimer KATimer RefCnt
    br0 172.16.5.105 239.1.1.1 Prune 00:07:40 --:--:-- 00:00:36 00:02:50 1
    !
    exit01# show ip pim upstream-join-desired
    Interface Source          Group           LostAssert Joins PimInclude JoinDesired EvalJD
    !
    exit01# show ip pim interface
    Interface  State          Address  PIM Nbrs           PIM DR  FHR
    br0           up       172.16.5.1         0            local    1
    swp51         up        10.1.0.17         1            local    0
    swp52         up        10.1.0.19         0            local    0
    !
    exit01# show ip pim state
    Source           Group            IIF    OIL
    172.16.5.105     239.1.1.1        br0
    !
    exit01# show ip pim int detail
    Interface : br0
    State     : up
    Address   : 172.16.5.1
    Designated Router
    -----------------
    Address   : 172.16.5.1
    Priority  : 1
    Uptime    : --:--:--
    Elections : 2
    Changes   : 0
     
    FHR - First Hop Router
    ----------------------
    239.1.1.1 : 172.16.5.105 is a source, uptime is 00:27:43

On the spine, no mroute state is created, but the `show ip pim upstream`
output includes the S,G:

    spine01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    !
    spine01# show ip pim upstream
    Iif       Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
    swp30     172.16.5.105    239.1.1.1       Prune       00:00:19 --:--:--  --:--:--  00:02:46       1

As a receiver joins the group, the mroute output interface on the FHR
transitions from "none" to the RPF interface of the RP:

    exit01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    172.16.5.105    239.1.1.1       PIM    br0        swp51      1    00:05:40
    !
    exit01# show ip pim upstream
    Iif       Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
    br0       172.16.5.105    239.1.1.1       Prune       00:48:23 --:--:--  00:00:00  00:00:37       2
    !
    exit01# show ip pim upstream-join-desired
    Interface Source          Group           LostAssert Joins PimInclude JoinDesired EvalJD
    swp51     172.16.5.105    239.1.1.1       no         yes   no         yes         yes
    !
    exit01# show ip pim state
    Source           Group            IIF    OIL
    172.16.5.105     239.1.1.1        br0    swp51

    spine01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    *               239.1.1.1       PIM    lo         swp1       1    00:09:59
    172.16.5.105    239.1.1.1       PIM    swp30      swp1       1    00:09:59
    !
    spine01# show ip pim upstream
    Iif       Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
    lo        *               239.1.1.1       Joined      00:10:01 00:00:59  --:--:--  --:--:--       1
    swp30     172.16.5.105    239.1.1.1       Joined      00:00:01 00:00:59  --:--:--  00:02:35       1
    !
    spine01# show ip pim upstream-join-desired
    Interface Source          Group           LostAssert Joins PimInclude JoinDesired EvalJD
    swp1      *               239.1.1.1       no         yes   no         yes         yes
    !
    spine01# show ip pim state
    Source           Group            IIF    OIL
    *                239.1.1.1        lo     swp1
    172.16.5.105     239.1.1.1        swp30  swp1

#### <span>Receiver Joins First</span>

On the LHR attached to the receiver:

    leaf01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    *               239.2.2.2       IGMP   swp51      br0        1    00:01:19
    !
    leaf01# show ip pim local-membership
    Interface Address         Source          Group           Membership
    br0       172.16.1.1      *               239.2.2.2       INCLUDE
    !
    leaf01# show ip pim state
    Source           Group            IIF    OIL
    *                239.2.2.2        swp51  br0
    !
    leaf01# show ip pim upstream
    Iif       Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
    swp51     *               239.2.2.2       Joined      00:02:07 00:00:53  --:--:--  --:--:--       1
    !
    leaf01# show ip pim upstream-join-desired
    Interface Source          Group           LostAssert Joins PimInclude JoinDesired EvalJD
    br0       *               239.2.2.2       no         no    yes        yes         yes
    !
    leaf01# show ip igmp groups
    Interface Address         Group           Mode Timer    Srcs V Uptime
    br0       172.16.1.1      239.2.2.2       EXCL 00:04:02    1 3 00:04:12
    !
    leaf01# show ip igmp sources
    Interface Address         Group           Source          Timer Fwd Uptime
    br0       172.16.1.1      239.2.2.2       *               03:54   Y 00:04:21

On the RP:

    spine01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    *               239.2.2.2       PIM    lo         swp1       1    00:00:03
    !
    spine01# show ip pim state
    Source           Group            IIF    OIL
    *                239.2.2.2        lo     swp1
    !
    spine01# show ip pim upstream
    Iif       Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
    lo        *               239.2.2.2       Joined      00:05:17 00:00:43  --:--:--  --:--:--       1
    !
    spine01# show ip pim upstream-join-desired
    Interface Source          Group           LostAssert Joins PimInclude JoinDesired EvalJD
    swp1      *               239.2.2.2       no         yes   no         yes         yes

## <span>Troubleshooting PIM</span>

### <span>FHR Stuck in Registering Process</span>

When a multicast source starts, the FHR sends unicast PIM register
messages from the RPF interface towards the source. After the PIM
register is received by the RP, a `PIM register stop` message is sent
from the RP to the FHR to end the register process. If an issue with
this communication, the FHR will remain stuck in the registering
process, which can result in high CPU, as PIM register packets are
generated by the FHR CPU, and sent to the RP CPU.

To assess this issue:

  - Review the FHR. The output interface of `pimreg` can be seen here.
    If this does not change to an interface within a few seconds, the
    FHR is likely stuck.
    
        exit01# show ip mroute
        Source          Group           Proto  Input      Output     TTL  Uptime
        172.16.5.105    239.2.2.3       PIM    br0        pimreg     1    00:03:59

To troubleshoot the issue:

1.  Validate that the FHR can reach the RP. If the RP and FHR can not
    communicate, the Registration process will fail:
    
        cumulus@exit01:~$ ping 10.0.0.21 -I br0
        PING 10.0.0.21 (10.0.0.21) from 172.16.5.1 br0: 56(84) bytes of data.
        ^C
        --- 10.0.0.21 ping statistics ---
        4 packets transmitted, 0 received, 100% packet loss, time 3000ms

2.  On the RP, use `tcpdump` to see if the PIM Register packets are
    arriving:
    
        cumulus@spine01:~$ sudo tcpdump -i swp30
        tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
        listening on swp30, link-type EN10MB (Ethernet), capture size 262144 bytes
        23:33:17.524982 IP 172.16.5.1 > 10.0.0.21: PIMv2, Register, length 66

3.  If PIM Registration packets are being received, verify that they are
    seen by PIM by issuing `debug pim packets` from within Quagga:
    
        cumulus@spine01:~$ sudo vtysh -c "debug pim packets"
        PIM Packet debugging is on
         
        cumulus@spine01:~$ sudo tail /var/log/quagga/quagga.log
        2016/10/19 23:46:51 PIM: Recv PIM REGISTER packet from 172.16.5.1 to 10.0.0.21 on swp30: ttl=255 pim_version=2 pim_msg_size=64 checksum=a681

4.  Repeat the process on the FHR to see if PIM Register Stop messages
    are being received on the FHR and passed to the PIM process:
    
        cumulus@exit01:~$ sudo tcpdump -i swp51
        23:58:59.841625 IP 172.16.5.1 > 10.0.0.21: PIMv2, Register, length 28
        23:58:59.842466 IP 10.0.0.21 > 172.16.5.1: PIMv2, Register Stop, length 18
         
        cumulus@exit01:~$ sudo vtysh -c "debug pim packets"
        PIM Packet debugging is on
         
        cumulus@exit01:~$ sudo tail -f /var/log/quagga/quagga.log
        2016/10/19 23:59:38 PIM: Recv PIM REGSTOP packet from 10.0.0.21 to 172.16.5.1 on swp51: ttl=255 pim_version=2 pim_msg_size=18 checksum=5a39

### <span>No \*,G Is Built on LHR</span>

The most common reason for a \*,G to not be built on a LHR is for both
PIM **and** IGMP to not be enabled on an interface facing a receiver.

    leaf01# show run
    !
    interface br0
     ip igmp
     ip ospf area 0.0.0.0
     ip pim sm

To troubleshoot this issue:

1.  If both PIM and IGMP are enabled, ensure that IGMPv3 Joins are being
    sent by the receiver:
    
        cumulus@leaf01:~$ sudo tcpdump -i br0 igmp
        tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
        listening on br0, link-type EN10MB (Ethernet), capture size 262144 bytes
        00:03:55.789744 IP 172.16.1.101 > igmp.mcast.net: igmp v3 report, 1 group record(s)

### <span>No mroute Created on FHR</span>

To troubleshoot this issue:

1.  Verify that multicast traffic is being received:
    
        cumulus@exit01:~$ sudo tcpdump -i br0
        tcpdump: verbose output suppressed, use -v or -vv for full protocol decode
        listening on br0, link-type EN10MB (Ethernet), capture size 262144 bytes
        00:11:52.944745 IP 172.16.5.105.51570 > 239.2.2.9.1000: UDP, length 9

2.  Verify that PIM is configured on the interface facing the source:
    
        exit01# show run
        !
        interface br0
         ip ospf area 0.0.0.0
         ip pim sm
    
    1.  If PIM is configured, verify that the RPF interface for the
        source matches the interface the multicast traffic is received
        on:
        
            exit01# show ip rpf 172.16.5.105
            Routing entry for 172.16.5.0/24 using Multicast RIB
              Known via "connected", distance 0, metric 0, best
              * directly connected, br0

3.  Verify that an RP is configured for the multicast group:
    
        exit01# show ip pim rp-info
        RP address       group/prefix-list   OIF         I am RP
        10.0.0.21        224.0.0.0/4         swp51       no

### <span>No S,G on RP for an Active Group</span>

An RP will not build an mroute when there are no active receivers for a
multicast group, even though the mroute was created on the FHR:

    spine01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    spine01#

    exit01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    172.16.5.105    239.2.2.9       none   br0        none       0    --:--:--

This is expected behavior. The active source can be seen on the RP with
`show ip pim upstream`:

    spine01# show ip pim upstream
    Iif       Source          Group           State       Uptime   JoinTimer RSTimer   KATimer   RefCnt
    swp30     172.16.5.105    239.2.2.9       Prune       00:08:03 --:--:--  --:--:--  00:02:20       1
    !
    spine01# show ip mroute
    Source          Group           Proto  Input      Output     TTL  Uptime
    spine01#

### <span>No mroute Entry Present in Hardware</span>

Please verify that the hardware IP multicast entry is the maximum value
already, using the `cl-resource-query` command:

    cumulus@switch:~$ cl-resource-query  | grep Mcast
       Total Mcast Routes:         450,   0% of maximum value    450

For Mellanox chipsets, please refer to [TCAM Resource Profiles for
Mellanox Switches](Routing.html#src-5866425_Routing-tcam).

### <span>Verify MSDP Session State</span>

Run the following commands to verify the state of MSDP sessions:

    switch# show ip msdp mesh-group 
    Mesh group : pod1
      Source : 100.1.1.1
      Member                 State
      100.1.1.2        established
      100.1.1.3        established
    spine-1# show ip msdp peer       
    Peer                       Local        State    Uptime   SaCnt
    100.1.1.2              100.1.1.1  established  00:07:21       0
    100.1.1.3              100.1.1.1  established  00:07:21       0
    spine-1# 

### <span>View the Active Sources</span>

Review the active sources learned locally (via PIM registers) and from
MSDP peers:

    switch# show ip msdp sa   
    Source                     Group               RP  Local  SPT    Uptime
    44.1.11.2              239.1.1.1        100.1.1.1      n    n  00:00:40
    44.1.11.2              239.1.1.2        100.1.1.1      n    n  00:00:25
    spine-2# 

## <span>Caveats and Errata</span>

  - Cumulus Linux 3.2.0 only supports PIM Sparse Mode - Any-source
    Multicast (PIM-SM ASM) and Source-specific Multicast (SSM). Dense
    Mode and Bidirectional Multicast are not supported.

  - S,G mroutes are not built on routers that are not the Rendezvous
    Point (RP) or the First-hop Router (FHR). S,G PIM Joins will be
    sent, but only \*,G mroutes are built. As a result, all traffic will
    flow over the \*,G tree, similar to PIM Bidirectional Multicast.

  - Non-native forwarding (register decapsulation) is not supported.
    Initial packet loss is expected while the PIM \*,G tree is built
    from the Rendezvous Point (RP) to the First-hop Router (FHR) to
    trigger native forwarding.

  - Cumulus Linux does not currently build an S,G mroute when forwarding
    over an \*,G tree.
