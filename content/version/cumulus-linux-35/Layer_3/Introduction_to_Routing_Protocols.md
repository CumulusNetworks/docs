---
title: Introduction to Routing Protocols
author: Cumulus Networks
weight: 165
aliases:
 - /display/CL35/Introduction+to+Routing+Protocols
 - /pages/viewpage.action?pageId=8357709
pageID: 8357709
product: Cumulus Linux
version: '3.5'
imgData: cumulus-linux-35
siteSlug: cumulus-linux-35
---
This chapter discusses the various routing protocols, and how to
configure them.

## <span>Defining Routing Protocols</span>

A *routing protocol* dynamically computes reachability between various
end points. This enables communication to work around link and node
failures, and additions and withdrawals of various addresses.

*IP routing protocols* are typically distributed; that is, an instance
of the routing protocol runs on each of the routers in a network.

{{%notice note%}}

Cumulus Linux does **not** support running multiple instances of the
same protocol on a router.

{{%/notice%}}

*Distributed routing protocols* compute reachability between end points
by disseminating relevant information and running a routing algorithm on
this information to determine the routes to each end station. To scale
the amount of information that needs to be exchanged, routes are
computed on address prefixes rather than on every end point address.

## <span>Configuring Routing Protocols</span>

A routing protocol needs to know three pieces of information, at a
minimum:

  - Who am I (my identity)

  - To whom to disseminate information

  - What to disseminate

Most routing protocols use the concept of a router ID to identify a
node. Different routing protocols answer the last two questions
differently.

The way they answer these questions affects the network design and
thereby configuration. For example, in a link-state protocol such as
OSPF (see [Open Shortest Path First (OSPF)
Protocol](/version/cumulus-linux-35/Layer_3/Open_Shortest_Path_First_-_OSPF_-_Protocol))
or IS-IS, complete local information (links and attached address
prefixes) about a node is disseminated to every other node in the
network. Since the state that a node has to keep grows rapidly in such a
case, link-state protocols typically limit the number of nodes that
communicate this way. They allow for bigger networks to be built by
breaking up a network into a set of smaller subnetworks (which are
called areas or levels), and by advertising summarized information about
an area to other areas.

Besides the two critical pieces of information mentioned above,
protocols have other parameters that can be configured. These are
usually specific to each protocol.

## <span>Protocol Tuning</span>

Most protocols provide certain tunable parameters that are specific to
convergence during changes.

Wikipedia defines
[convergence](http://en.wikipedia.org/wiki/Convergence_%28routing%29) as
the “state of a set of routers that have the same topological
information about the network in which they operate”. It is imperative
that the routers in a network have the same topological state for the
proper functioning of a network. Without this, traffic can be
blackholed, and thus not reach its destination. It is normal for
different routers to have differing topological states during changes,
but this difference should vanish as the routers exchange information
about the change and recompute the forwarding paths. Different protocols
converge at different speeds in the presence of changes.

A key factor that governs how quickly a routing protocol converges is
the time it takes to detect the change. For example, how quickly can a
routing protocol be expected to act when there is a link failure.
Routing protocols classify changes into two kinds: hard changes such as
link failures, and soft changes such as a peer dying silently. They’re
classified differently because protocols provide different mechanisms
for dealing with these failures.

It is important to configure the protocols to be notified immediately on
link changes. This is also true when a node goes down, causing all of
its links to go down.

Even if a link doesn’t fail, a routing peer can crash. This causes that
router to usually delete the routes it has computed or worse, it makes
that router impervious to changes in the network, causing it to go out
of sync with the other routers in the network because it no longer
shares the same topological information as its peers.

The most common way to detect a protocol peer dying is to detect the
absence of a heartbeat. All routing protocols send a heartbeat (or
“hello”) packet periodically. When a node does not see a consecutive
set of these hello packets from a peer, it declares its peer dead and
informs other routers in the network about this. The period of each
heartbeat and the number of heartbeats that need to be missed before a
peer is declared dead are two popular configurable parameters.

If you configure these timers very low, the network can quickly descend
into instability under stressful conditions when a router is not able to
keep sending the heartbeats quickly as it is busy computing routing
state; or the traffic is so much that the hellos get lost. Alternately,
configuring this timer to very high values also causes blackholing of
communication because it takes much longer to detect peer failures.
Usually, the default values initialized within each protocol are good
enough for most networks. Cumulus Networks recommends you do not adjust
these settings.
