---
title: Routing on the Host
author: Cumulus Networks
weight: 1
aliases:
 - /display/ROH/Routing+on+the+Host
 - /pages/viewpage.action?pageId=5116581
pageID: 5116581
product: Routing on the Host
version: '0.5'
imgData: routing-on-the-host
siteSlug: routing-on-the-host
subsection: true
---
In a typical data center, connections between servers and the leaf or
top of rack switches are often done at layer 2. In order to build more
resilient data centers, many Cumulus Networks customers are leveraging
the Linux ecosystem to run routing protocols directly to their servers,
running layer 3 protocols like
[OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) (Open
Shortest Path First) or
[BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) (Border
Gateway Protocol) directly on the hosts, so the hosts can participate
directly in the routing fabric. This is often referred to as *Routing on
the Host*.

In Cumulus Linux 3.0 and later, Routing on the Host works on server
hosts in a number of different environments:

  - Ubuntu 12.04, 14.04 and 16.04

  - Red Hat Enterprise Linux 7

  - Docker containers

Routing on the Host provides you with:

  - Simplified, modern data center design

  - Subnet freedom and mobility

  - Enhanced redundancy and flexibility

  - Stateless load balancing with anycast

In the illustration below, the data center architecture looks like a
standard Clos leaf/spine design. However, notice the layer 3 connections
between the leaf and spine switches as well as between the leafs and the
server hosts.

{{% imgOld 0 %}}

## <span>Simple, Modern Data Center Design</span>

Cloud data centers are going through a once-in-a-decade transition in
the way applications get built and deployed with the adoption of
microservices and containers. This is a similar paradigm shift to what
happened when organizations moved from deploying applications on bare
metal hardware to server virtualization a decade ago. This impacts how
networks get designed and built, and the kind of network services that
get deployed for these applications.

Routing on the Host enables a simplified and modern design for data
centers, aimed at cloud-native applications running industry-standard
protocols — such as BGP and OSPF — and open technologies like Linux,
containers and OpenStack.

Routing on the Host provides you with interoperability, so you can avoid
vendor lock-in with legacy or proprietary solutions like MLAG — if you
have devices from different vendors, they can't act as an MLAG pair.
However, by using layer 3 protocols like OSPF or BGP on the hosts, the
network adheres to open standards that have been around a long time.
OSPF and BGP interoperability is highly tested, very scalable and has a
track record of success.

Routing on the Host also reduces the complexity of managing a layer 2
network with protocols like STP, by eliminating or reducing the number
of VLANs to the host and by providing automatic layer 2 segmentation.

## <span>Subnet Freedom and Mobility</span>

With Routing on the Host, IP addresses are independent of the rack or
subnet; only the subnet on the connection between the leaf and the
router on the host needs to be configured on the leaf. All containers,
subnets and so forth are advertised into the fabric automatically. This
greatly increases host mobility by allowing minimal configuration on the
leaf switch, so you can deploy and move any host, anywhere. Or
dynamically move containers across the data center as needed without
changing their IP addresses. All the leaf switch has to do is peer with
the server.

If security is a concern, the host can be forced to authenticate to
allow BGP or OSPF adjacencies to occur. Consider the following diagram:

{{% imgOld 1 %}}

In the above diagram the Quagga configuration does not need to change,
no matter what leaf you plug it into. The only configuration that needs
to change is the subnet on swp1 and eth0 (configured under
`/etc/network/interfaces`, which is not shown here). This greatly
reduces configuration complexity and allows for easy host mobility.

### <span>BGP and OSPF Unnumbered Interfaces</span>

Cumulus Networks enhanced Quagga with the ability to implement
[RFC 5549](https://tools.ietf.org/html/rfc5549), so you can configure
[BGP](/display/ROH/Border+Gateway+Protocol+-+BGP) or
[OSPF](/display/ROH/Open+Shortest+Path+First+-+OSPF) unnumbered
interfaces on Cumulus Linux switches, and now, with Routing on the Host,
on server hosts and containers as well. In addition to the benefits of
not having to configure every subnet described above, you do not have to
configure anything specific on the leaf switch at all, so you don't have
to configure an IPv4 address in `/etc/network/interfaces` for peering.

BGP unnumbered interfaces enables IPv6 link-local addresses to be
utilized for IPv4 BGP adjacencies. Link-local addresses are
automatically configured with SLAAC (StateLess Address
AutoConfiguration). This address is derived from an interface's MAC
address and is unique to each layer 3 adjacency. DAD (Duplicate Address
Detection) keeps duplicate addresses from being configured. This means
the configuration remains the same no matter where the host resides.
There is no specific subnet used on the Ethernet connection between the
host and the switch.

{{% imgOld 2 %}}

Along with implementation of RFC 5549, Quagga has a simpler
configuration, allowing novice users the ability to quickly configure,
understand and troubleshoot BGP configurations within the data center.
The following illustration shows a single attached host using BGP
unnumbered interfaces:

{{% imgOld 3 %}}

## <span>Enhanced Redundancy and Flexibility</span>

Routing on the Host provides enhanced redundancy since the hosts can
connect to as many leafs as you want. They're not limited to a pair of
switches, like they would be in an MLAG scenario. This is useful for
high density server configurations or hyper-converged infrastructure
deployments, where it is common to see more than two NICs per host. With
Routing on the Host, three or more leaf (or ToR — top of rack) switches
can be configured, giving much more redundancy. If one leaf fails, you
only lose 1/total leaf switches, whereas with a layer 2 MLAG solution,
you lose 50% of your bandwidth.

{{% imgOld 4 %}}

Another benefit of Routing on the Host is the ability to gracefully
remove a leaf switch from the fabric for maintenance. With layer 2 only
(like MLAG), you cannot influence routes without being disruptive (that
is, some traffic loss must occur). With
[OSPF](/display/ROH/Open+Shortest+Path+First+-+OSPF) and
[BGP](/display/ROH/Border+Gateway+Protocol+-+BGP), there are multiple
load balanced routes via
[ECMP](/display/ROH/Equal+Cost+Multipath+Load+Sharing+-+Hardware+ECMP)
(Equal Cost Multipath) routing. Since there is routing, it is possible
to change these routes dynamically.

For OSPF, you can increase the cost of all the links making the network
node less preferable.

With BGP, there are multiple ways to change the routes, but the most
common is prepending your BGP AS to make the switch less preferable.

Both BGP and OSPF make the leaf switch less preferable, removing it as
an ECMP choice for both protocols. However, the link doesn't get turned
off. Unlike layer 2, where the link must be shut down and all traffic
currently being transmitted is lost, a routing solution notifies the
rest of the network to no longer send traffic to this switch. By
watching interface counters you can determine when traffic is no longer
being sent to the device under maintenance, so you can safely remove it
from the network with no impact on traffic.

Because Routing on the Host uses three or more leafs, this reduces the
impact of a leaf being removed from service, either due to expected
maintenance or unexpected network failure. So, instead of losing 50% of
bandwidth in a two leaf MLAG deployment, the bandwidth loss can be
reduced to 33% with three leafs or 25% with four.

{{% imgOld 5 %}}

The redundancy with layer 3 networks is very significant. In the image
above, the network on the right, with Routing on the Host and ECMP, can
still operate even if 3 out of 4 leaf switches are down. This is known
as *[N-way
redundancy](https://en.wikipedia.org/wiki/Active_redundancy#Principle)*
. The best case for the network using MLAG on the left is 2-way
redundancy, no matter what vendor you choose. Layer 3 allows
applications to have much more uptime with no risk for outages.

## <span>Stateless Load Balancing with Anycast</span>

Routing on the Host provides for the ability to load balance between
servers without the need for a separate expensive load balancer. Routing
on the Host advertises the same IPv4 address from multiple hosts. By
assigning the same IP address to two or more servers, and using ECMP
routing, you can distribute the load between the servers automatically.
Each switch in the path performs a hashing and determines the exit point
from the switch, which does not change during the flow. This ensures the
flow remains with the same server. Resilient hashing ensures if a link
goes down, the flows won’t be rehashed.

{{%notice tip%}}

Using Routing on the Host for load balancing is recommended for
stateless applications only.

{{%/notice%}}

{{% imgOld 6 %}}

## <span>Getting Started</span>

To get started with Routing on the Host:

  - [Download and
    install](Installing_the_Cumulus_Quagga_Package_on_a_Host_Server.html)
    Cumulus Quagga

  - [Configure](Configuring_Cumulus_Quagga.html) Cumulus Quagga

  - Learn how to
    [troubleshoot](Troubleshooting_Routing_on_the_Host.html) Routing on
    the Host
