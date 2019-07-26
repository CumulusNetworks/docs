---
title: Monitor Linux Hosts
author: Cumulus Networks
weight: 67
aliases:
 - /display/NETQ141/Monitor+Linux+Hosts
 - /pages/viewpage.action?pageId=10453490
pageID: 10453490
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
Running NetQ on Linux hosts provides unprecedented network visibility,
giving the network operator a complete view of the entire
infastrucutre’s network connectivity instead of just from the network
devices.

The NetQ Agent is supported on the following Linux hosts:

  - CentOS 7

  - Red Hat Enterprise Linux 7.1

  - Ubuntu 16.04

You need to [install the OS-specific NetQ
metapack](/version/cumulus-netq-141/Cumulus-NetQ-Deployment-Guide/Install-NetQ)
on every host you want to monitor with NetQ.

The NetQ Agent monitors the following on Linux hosts:

  - netlink

  - Layer 2: LLDP and VLAN-aware bridge

  - Layer 3: IPv4, IPv6

  - Routing on the Host: BGP, OSPF

  - systemctl for services

  - Docker containers — refer to the [Monitor Container
    Environments](/version/cumulus-netq-141/Cumulus-NetQ-Telemetry-User-Guide/Monitor-Container-Environments)
    topic

Using NetQ on a Linux host is the same as using it on a Cumulus Linux
switch. For example, if you want to check LLDP neighbor information
about a given host, run:

    cumulus@switch:~$ netq server01 show lldp 
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    server01          eth0                      oob-mgmt-switch   swp2                      5d:22h:44m:44s
    server01          eth1                      leaf01            swp1                      3d:23h:30m:37s
    server01          eth2                      leaf02            swp1                      3d:23h:28m:50s

Then, to see LLDP from the switch's perspective:

    cumulus@switch:~$ netq leaf01 show lldp
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    leaf01            eth0                      oob-mgmt-switch   swp6                      5d:22h:45m:35s
    leaf01            swp1                      server01          eth1                      5d:22h:39m:53s
    leaf01            swp2                      server02          eth1                      3d:19h:23m:9s
    leaf01            swp49                     leaf02            swp49                     4d:0h:30m:34s
    leaf01            swp50                     leaf02            swp50                     4d:0h:30m:34s
    leaf01            swp51                     spine01           swp1                      5d:22h:40m:24s
    leaf01            swp52                     spine02           swp1                      5d:22h:40m:24s

To get the routing table for a server:

    cumulus@server01:~$ netq server01 show ip route
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         10.2.4.0/24                    server01          10.1.3.1: uplink                    3d:23h:31m:8s
    no     default         172.16.1.0/24                  server01          10.1.3.1: uplink                    3d:23h:31m:8s
    yes    default         10.1.3.0/24                    server01          uplink                              3d:23h:31m:8s
    yes    default         10.1.3.101/32                  server01          uplink                              3d:23h:31m:8s
    yes    default         192.168.0.0/24                 server01          eth0                                3d:23h:31m:8s
    yes    default         192.168.0.31/32                server01          eth0                                3d:23h:31m:8s

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
