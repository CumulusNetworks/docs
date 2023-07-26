---
title: PIM Overview
weight: 310
---
This article describes PIM network elements and PIM messages, and provides an overview of the PIM-SM configuration options, [ASM](## "Any-source Mulitcast") and [SSM](## "Source Specific Multicast"). For information on configuring PIM, refer to {{<kb_link latest="cl" url="Layer-3/Protocol-Independent-Multicast-PIM.md" text="Protocol Independent Multicast - PIM">}}

{{%notice note%}}
Cumulus Linux supports [PIM-SM](## "Sparse Mode") mode only.
{{%/notice%}}

## PIM Network Elements

| <div style="width:200px">Network Element | Description |
|---------------- |-------------|
| First Hop Router (FHR) | The router attached to the source. The FHR controls the PIM register process. |
| Last Hop Router (LHR) | The last router in the path, attached to an interested multicast receiver. There is a single LHR for each network subnet with an interested receiver, however multicast groups can have multiple LHRs throughout the network. |
| Rendezvous Point (RP) | Allows for the discovery of multicast sources and multicast receivers. The RP sends PIM Register Stop messages to FHRs. <br><br> <p>{{%notice warning%}}</p> <ul> <li><code>zebra</code> does not resolve the next hop for the RP through the default route. To prevent multicast forwarding from failing, either provide a specific route to the RP or specify the following command to be able to resolve the next hop for the RP through the default route:<pre>cumulus@switch:~$ sudo vtysh
switch# configure terminal
switch(config)# ip nht resolve-via-default
switch(config)# exit
switch# write memory</li><li><p>NVIDIA recommends you <b>not</b> use a spine switch as an RP when using eBGP in a Clos network. In an eBGP Clos network, the most common way to avoid BGP Path Hunting is to allocate the same ASN for all the spine nodes. This is done so each spine doesn't see duplicate routes from other spines.</p><p>In a multicast fabric, an RP should be able to route to a multicast source at all times. So, when a spine node is configured as an RP, it is important that the RP always has a path to reach any multicast source leaf node. But if the direct link between a spine RP and a leaf fails, there is no alternate way for the RP to route to that leaf &mdash; because one spine doesn't route to a leaf via another spine.</p></li><p>{{%/notice%}}</p> |
| PIM Shared Tree (RP Tree) or (*,G) Tree | The multicast tree rooted at the RP. When receivers want to join a multicast group, they send join messages along the shared tree towards the RP.|
|PIM Shortest Path Tree (SPT) or (S,G) Tree|The multicast tree rooted at the multicast source for a given group. Each multicast source has a unique SPT. The SPT can match the RP Tree, but this is not a requirement. The SPT represents the most efficient way to send multicast traffic from a source to the interested receivers. |
| Outgoing Interface (OIF) | Indicates the interface on which to send out a PIM or multicast packet. OIFs are the interfaces towards the multicast receivers. |
| Incoming Interface (IIF) | Indicates the interface on which to receive a multicast packet. An IIF can be the interface towards the source or towards the RP. |
| Reverse Path Forwarding Interface (RPF Interface) | The path used to reach the RP or source. There must be a valid PIM neighbor to determine the RPF unless directly connected to source. |
| Multicast Route (mroute) | Indicates the multicast source and multicast group as well as associated OIFs, IIFs, and RPF information. |
| Star-G mroute (\*,G) | Represents the RP Tree. \* is a wildcard indicating any multicast source. G is the multicast group. For example, (\*,G) is (\*, 239.1.2.9). |
| S-G mroute (S,G) | This is the mroute representing the source entry. S is the multicast source IP. G is the multicast group. For example, (S,G) is (10.1.1.1, 239.1.2.9). |

## PIM Messages

| <div style="width:200px">PIM Message | Description |
|------------ |------------ |
| PIM Hello | Announce the presence of a multicast router on a segment. PIM hellos send every 30 seconds by default. For example:<pre>22.1.2.2 > 224.0.0.13<br>PIMv2, length 34<br>Hello, cksum 0xfdbb (correct)<br>Hold Time Option (1), length 2, Value: 1m45s<br>0x0000: 0069<br>LAN Prune Delay Option (2), length 4, Value: <br>T-bit=0, LAN delay 500ms, Override interval 2500ms<br>0x0000: 01f4 09c4<br>DR Priority Option (19), length 4, Value: 1<br>0x0000: 0000 0001<br>Generation ID Option (20), length 4, Value<br>0x2459b190<br>0x0000: 2459 b190</pre> |
| PIM Join/Prune (J/P) | Indicate the groups that a multicast router wants to receive or no longer receive. A PIM join or prune message is a single PIM message with a list of groups to join and a second list of groups to leave. The messages can ask to join or prune from the SPT or RP trees (also called (*,G) joins or (S,G) joins).<br><br>**Note**: PIM sends join and prune messages to PIM neighbors on individual interfaces. The messages are never unicast.<br>{{< figure src = "/images/cumulus-linux/pim-join-prune.png" >}}<br>This PIM join and prune is for group 239.1.1.9, with 1 join and 0 prunes for the group.<br>Join and prunes for multiple groups can exist in a single packet.<br> The following shows an S,G Prune example:<pre>21:49:59.470885 IP (tos 0x0, ttl 255, id 138, offset 0, flags [none], proto PIM (103), length 54)<br>22.1.2.2 > 224.0.0.13: PIMv2, length 34<br>Join / Prune, cksum 0xb9e5 (correct), upstream-neighbor: 22.1.2.1<br>1 group(s), holdtime: 3m30s<br>group #1: 225.1.0.0, joined sources: 0, pruned sources:<br>1 pruned source #1: 33.1.1.1(S)</pre> |
| PIM Register | Unicast packets from an FHR destined to the RP to advertise a multicast group. The FHR fully encapsulates the original multicast packet in PIM register messages. The RP decapsulates the PIM register message and forwards it along the (*,G) tree towards the receivers. |
| PIM Null Register |A special type of PIM register message where the Null-Register flag is in the packet. An FHR uses null register messages to signal to an RP that a source is still sending multicast traffic. Unlike normal PIM register messages, null register messages do not encapsulate the original data packet. |
| PIM Register Stop | An RP sends PIM register stop messages to the FHR to stop sending messages. For example:<pre>21:37:00.419379 IP (tos 0x0, ttl 255, id 24, offset 0, flags [none], proto PIM (103), length 38)<br>100.1.2.1 > 33.1.1.10: PIMv2, length 18<br>Register Stop, cksum 0xd8db (correct) group=225.1.0.0 source=33.1.1.1</pre> |
| IGMP Membership Report (IGMP Join) | Multicast receivers send IGMP membership report messages to multicast routers to indicate their interest in a specific multicast group. IGMP join messages trigger PIM *,G joins. IGMP version 2 queries go to the multicast address, 224.0.0.1 on all hosts. IGMP version 2 reports (joins) go to the multicast address of the group. IGMP version 3 messages go to an IGMP v3 specific multicast address, 224.0.0.22. |
| IGMP Leave | Tell a multicast router that a multicast receiver no longer wants the multicast group. IGMP leave messages trigger PIM *,G prunes. |

## ASM Overview

Multicast routing behaves differently depending on whether the source sends before receivers request the multicast stream, or if a receiver tries to join a stream before there are any sources.

### Receiver Joins First

When a receiver joins a group, it sends an IGMP membership join message to the IGMPv3 multicast group, 224.0.0.22. The PIM multicast router for the segment that is listening to the IGMPv3 group receives the IGMP membership join message and becomes an LHR for this group.

{{< img src = "/images/cumulus-linux/pim-igmp.png" >}}

This creates a (\*,G) mroute with an OIF of the interface that receives the IGMP Membership Report and an IIF of the RPF interface for the RP.

The LHR generates a PIM (\*,G) join message and sends it from the interface towards the RP. Each multicast router between the LHR and the RP builds a (\*,G) mroute with the OIF being the interface that receives the PIM join message and an Incoming Interface of the reverse path forwarding interface for the RP.

{{< img src = "/images/cumulus-linux/pim-join.png" >}}

{{%notice note%}}
- When the RP receives the (\*,G) Join message, it does not send any additional PIM join messages. The RP maintains a (\*,G) state as long as the receiver wants to receive the multicast group.
- Unlike multicast receivers, multicast sources do not send IGMP (or PIM) messages to the FHR. A multicast source begins sending, and the FHR receives the traffic and builds both a (\*,G) and an (S,G) mroute. The FHR then begins the PIM register process.
{{%/notice%}}

#### PIM Register Process

When a first hop router (FHR) receives a multicast data packet from a source, the FHR does not know if there are any interested multicast receivers in the network. The FHR encapsulates the data packet in a unicast PIM register message. The FHR is the source of this packet and the RP address is the destination. The RP builds an (S,G) mroute, decapsulates the multicast packet, and forwards it along the (\*,G) tree.

As the unencapsulated multicast packet travels down the (\*,G) tree towards the interested receivers, at the same time, the RP sends a PIM (S,G) join towards the FHR. This builds an (S,G) state on each multicast router between the RP and FHR.

When the FHR receives a PIM (S,G) join, it continues encapsulating and sending PIM register messages, but also makes a copy of the packet and sends it along the (S,G) mroute.

The RP then receives the multicast packet along the (S,G) tree and sends a PIM register stop to the FHR to end the register process.

<table border="0">
<tr>
<td> {{< img src = "/images/cumulus-linux/pim-data.png" >}} </td><td> {{< img src = "/images/cumulus-linux/pim-register.png" >}} </td>
</tr>
</table>

### Sender Starts Before Receivers Join

A multicast sender can send multicast data without any additional IGMP or PIM signaling. When the FHR receives the multicast traffic, it encapsulates it and sends a PIM register to the rendezvous point (RP).

When the RP receives the PIM register, it builds an (S,G) mroute; however, there is no (\*,G) mroute and no interested receivers.

The RP drops the PIM register message, then sends a PIM register stop message to the FHR.
<!-- vale off -->
<!-- "leaves the FHR" matches house style of leafs -->
Receiving a PIM register stop without any associated PIM joins leaves the FHR without any outgoing interfaces. The FHR drops this multicast traffic until a PIM join is received.
<!-- vale on -->
{{%notice note%}}
Cumulus Linux sends PIM register messages from the interface that receives the multicast traffic to the RP address.
{{%/notice%}}

<!-- vale off -->
<!-- vale.ai Issue #253 -->
#### PIM Null-Register
<!-- vale on -->
To notify the RP that multicast traffic is still flowing when the RP has no receiver, or if the RP is not on the SPT tree, the FHR periodically sends PIM null register messages. The FHR sends a PIM register with the Null-Register flag set, but without any data. This special PIM register notifies the RP that a multicast source is still sending, in case any new receivers come online.

After receiving a PIM Null-Register, the RP sends a PIM register stop to acknowledge that it receives the PIM null register message.

For additional information, see {{<exlink url="https://tools.ietf.org/html/rfc7761" text="RFC 7761 - Protocol Independent Multicast - Sparse Mode">}}.

## SSM Overview

### Receiver Joins First

When a receiver sends an IGMPv3 Join with the source defined, the LHR builds an S,G entry and sends a PIM S,G join to the PIM neighbor closest to the source, according to the routing table. The full path between LHR and FHR contains an S,G state, although no multicast traffic is flowing. Periodic IGMPv3 joins between the receiver and LHR, as well as PIM S,G joins between PIM neighbors, maintain this state. When the sender starts sending traffic, it flows over the pre-built SPT from the sender to the receiver.

### Sender Starts Before Receivers Join

In SSM when a sender starts sending traffic, the FHR does not have any existing mroutes. The traffic drops and nothing further happens until a receiver joins. SSM does not rely on an RP and there is no PIM Register process.

## Differences Between ASM and SSM
SSM differs from ASM multicast in the following ways:

- SSM does not use an RP. SSM does not require an RP because receivers always know the addresses of the senders.
- SSM does not use *,G PIM Join messages. The multicast sender is always known so the PIM Join messages in SSM are always S,G Join messages.
- SSM does not use a Shared Tree or *,G tree. The PIM join message always goes towards the source, building the SPT along the way.
- SSM requires IGMPv3. ASM allows for receivers to specify only the group they want to join without knowledge of the sender. You can use both IGMPv2 and IGMPv3. With IGMPv3, you can request a specific source for a multicast group (send a S,G IGMP join).
- SSM does not use the PIM Register process or SPT Switchover. Without a shared tree or RP, there is no need for the PIM register process. S,G joins go directly towards the FHR.
