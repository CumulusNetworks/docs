---
title: Cumulus Host Pack
author: Cumulus Networks
weight: 1
aliases:
 - /display/HOSTPACK/Cumulus+Host+Pack
 - /pages/viewpage.action?pageId=5868785
pageID: 5868785
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
subsection: true
---
Pete Bratach

[Cumulus Host Pack](https://cumulusnetworks.com/products/netq/) brings
the host to the network for fabric-wide *visibility* and *connectivity*.

Host Pack removes the barriers to deploying a web-scale network to
support containers and microservices. While completely supporting
popular layer 2 overlay networks, Host Pack enhances network scalability
and connectivity by running layer 3 protocols like
[OSPF](https://en.wikipedia.org/wiki/Open_Shortest_Path_First) (Open
Shortest Path First) or
[BGP](https://en.wikipedia.org/wiki/Border_Gateway_Protocol) (Border
Gateway Protocol) directly on the hosts, so the hosts can participate
directly in the routing fabric.

Host networking challenges have impeded the simplicity and scalability
possible with web-scale networking designs. Web-scale efficiency can be
achieved with improved connectivity and with consistent, telemetry-based
visibility into network infrastructure, host networking, and the
information about container workloads.

Cumulus Host Pack enables a web-scale network by providing connectivity
through **FRRouting on the Host** and **Container Advertiser** and
visibility through **NetQ on the Host**.

[](https://cumulusnetworks.com/products/host-pack/)

[{{% imgOld 0 %}}](https://cumulusnetworks.com/products/host-pack/)

[](https://cumulusnetworks.com/products/host-pack/)

## <span>Web-scale Connectivity</span>

[FRRouting on the Host](https://frrouting.org) — the suite of routing
protocols in Cumulus Linux — delivers layer 3 routing on host servers;
it also enables the
[BGP](/display/HOSTPACK/Border+Gateway+Protocol+-+BGP) unnumbered
interfaces standard to be implemented in both the network infrastructure
and in host networking, eliminating the issues that can be posed by a
layer 2 network and enabling you to move to layer 3 from the container
to the data center network core on your own schedule. FRR also runs in
containers, so you can connect your containers over layer 3 as well.

Container Advertiser uses address announcement and advertising services
in conjunction with FRRouting on Docker Engine- and Mesos Universal
Container Runtime-based containers to enable the network to deliver
automatic layer 3 connectivity as microservices are spun up and torn
down. Using container event-based announcement for unnumbered interfaces
advertises container IP addresses into a routed fabric automatically,
introducing the next level of network automation and taking operations
past the first step of automated configuration management.

{{% imgOld 1 %}}

{{% imgOld 2 %}}

  
***Host Pack connectivity is provided through FRRouting on the Host and
Container Advertiser***

## <span>Web-scale Visibility</span>

In addition to enhanced connectivity support, Host Pack ensures
real-time reliability and uptime to hosts and containers with visibility
provided by [Cumulus NetQ on the
Host](https://cumulusnetworks.com/products/netq/). Cumulus NetQ, coupled
with NetQ on the Host, unifies visibility of the entire network,
including the hosts and containers within one system.

{{% imgOld 3 %}}

***Host Pack visibility is provided through NetQ on the Host***

Running the NetQ on the Host provides unprecedented visibility into the
server side of the data center network, giving the network operator a
complete view of the entire infrastructure's network connectivity. The
NetQ Agent monitors the following services on Linux hosts:

  - FRRouting: BGP, OSPF

  - Kernel netlink events

  - Layer 2: LLDP and VLAN-aware bridges

  - Layer 3: IPv4, IPv6

  - systemctl for services

NetQ on the Host monitors containers through host-based telemetry
including:

  - Identity: NetQ on the Host tracks every container's IP and MAC
    address, name, image and more. NetQ on the Host can locate
    containers across the fabric based on a container's name, image, IP
    or MAC address, and protocol and port pair.

  - Port mapping on a network: NetQ on the Host tracks protocol and
    ports exposed by a container. NetQ on the Host can identify
    containers exposing a specific protocol and port pair on a network.

  - Connectivity: NetQ on the Host can provide information on network
    connectivity for a container, including adjacency, and can identify
    containers that can be affected by a top of rack switch.

## <span>Supported Environments</span>

Host Pack requires Cumulus Linux 3.3 and later and is supported on the
following hosts and systems:

Host Pack Feature

Ubuntu

Red Hat

Container

**Connectivity**

**FRRouting on the Host**

Ubuntu 16.04, 14.04

Red Hat Enterprise Linux 7

CentOS 7

Docker Engine

Docker Swarm

**FRRouting in a c**ontainer****

Ubuntu 16.04

Red Hat Enterprise Linux 7

CentOS 7

Docker Engine

Mesos Universal Container Runtime

**Container Advertiser**

Ubuntu 16.04

Red Hat Enterprise Linux 7

CentOS 7

Docker Engine

Mesos Universal Container Runtime

**Visibility**

**NetQ on the Host**

Ubuntu 16.04

Red Hat Enterprise Linux 7

CentOS 7

Docker Engine

Docker Swarm

## <span>Getting Started</span>

Where you get started with Host Pack depends upon which features you
intend to use.

  - If you want to use routing on your servers, or with the containers
    on a host, you need to
    [install](/host-pack/Installing_FRRouting_on_the_Host) and
    [configure](/host-pack/Configuring_FRRouting_on_the_Host) FRRouting
    on the Host.

  - If you are using containers on your host servers, make sure [Docker
    is installed](/host-pack/Installing_Docker).

  - If you want to use Container Advertiser, you need to [install and
    configure](/host-pack/Configuring_Container_Advertiser) it.

  - If you plan on using NetQ on the Host to monitor the hosts and
    containers, you need to
    [install](/host-pack/Installing_NetQ_on_the_Host) and
    [configure](/host-pack/Configuring_NetQ_on_the_Host) it.
