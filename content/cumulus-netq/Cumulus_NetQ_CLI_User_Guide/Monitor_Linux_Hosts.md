---
title: Monitor Linux Hosts
author: Cumulus Networks
weight: 45
aliases:
 - /display/NETQ/Monitor+Linux+Hosts
 - /pages/viewpage.action?pageId=10456369
pageID: 10456369
product: Cumulus NetQ
version: '2.1'
imgData: cumulus-netq
siteSlug: cumulus-netq
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
metapack](https://docs.cumulusnetworks.com/pages/viewpage.action?pageId=10456209)
on every host you want to monitor with NetQ.

The NetQ Agent monitors the following on Linux hosts:

  - netlink

  - Layer 2: LLDP and VLAN-aware bridge

  - Layer 3: IPv4, IPv6

  - Routing on the Host: BGP, OSPF

  - systemctl for services

  - Docker containers — refer to the [Monitor Container
    Environments](/cumulus-netq/Cumulus_NetQ_CLI_User_Guide/Monitor_Container_Environments)
    topic

Using NetQ on a Linux host is the same as using it on a Cumulus Linux
switch. For example, if you want to check LLDP neighbor information
about a given host, run:

    cumulus@switch:~$ netq server01 show lldp 
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    server01          eth0                      oob-mgmt-switch   swp2                      Fri Feb  8 01:50:59 2019
    server01          eth1                      leaf01            swp1                      Fri Feb  8 01:50:59 2019
    server01          eth2                      leaf02            swp1                      Fri Feb  8 01:50:59 2019

Then, to see LLDP from the switch's perspective:

    cumulus@switch:~$ netq leaf01 show lldp
    Matching lldp records:
    Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ----------------- ------------------------- -------------------------
    leaf01            eth0                      oob-mgmt-switch   swp6                      Thu Feb  7 18:31:26 2019
    leaf01            swp1                      server01          eth1                      Thu Feb  7 18:31:26 2019
    leaf01            swp2                      server02          eth1                      Thu Feb  7 18:31:26 2019
    leaf01            swp49                     leaf02            swp49                     Thu Feb  7 18:31:26 2019
    leaf01            swp50                     leaf02            swp50                     Thu Feb  7 18:31:26 2019
    leaf01            swp51                     spine01           swp1                      Thu Feb  7 18:31:26 2019
    leaf01            swp52                     spine02           swp1                      Thu Feb  7 18:31:26 2019

To get the routing table for a server:

    cumulus@server01:~$ netq server01 show ip route
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         10.2.4.0/24                    server01          10.1.3.1: uplink                    Fri Feb  8 01:50:49 2019
    no     default         172.16.1.0/24                  server01          10.1.3.1: uplink                    Fri Feb  8 01:50:49 2019
    yes    default         10.1.3.0/24                    server01          uplink                              Fri Feb  8 01:50:49 2019
    yes    default         10.1.3.101/32                  server01          uplink                              Fri Feb  8 01:50:49 2019
    yes    default         192.168.0.0/24                 server01          eth0                                Fri Feb  8 01:50:49 2019
    yes    default         192.168.0.31/32                server01          eth0                                Fri Feb  8 01:50:49 2019
