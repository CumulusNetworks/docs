---
title: Monitoring Linux Hosts with NetQ
author: Cumulus Networks
weight: 23
aliases:
 - /display/HOSTPACK/Monitoring+Linux+Hosts+with+NetQ
 - /pages/viewpage.action?pageId=7110958
pageID: 7110958
product: Cumulus Host Pack
version: '1.0'
imgData: host-pack
siteSlug: host-pack
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
metapack](/host-pack/Installing_NetQ_on_the_Host) on every host you want
to monitor with NetQ.

The NetQ Agent monitors the following on Linux hosts:

  - netlink

  - Layer 2: LLDP and VLAN-aware bridge

  - Layer 3: IPv4, IPv6

  - Routing on the Host: BGP, OSPF

  - systemctl for services

  - Docker containers — see [Monitoring Container Environments with
    NetQ](/host-pack/Monitoring_Container_Environments_with_NetQ)

Using NetQ on a Linux host is the same as using it on a Cumulus Linux
switch. For example, if you want to check LLDP neighbor information
about a given host, run:

    cumulus@server01:~$ netq server01 show lldp 
    LLDP peer info for server01:*
    Node      Interface    LLDP Peer        Peer Int    Last Changed
    --------  -----------  ---------------  ----------  --------------
    server01  eth0         oob-mgmt-switch  swp2        10m ago
    server01  eth1         leaf01           swp1        10m ago
    server01  eth2         leaf02           swp1        10m ago

Then, to see LLDP from the switch's perspective:

    cumulus@server01:~$ netq leaf01 show lldp
    LLDP peer info for leaf01:*
    Node    Interface    LLDP Peer        Peer Int               Last Changed
    ------  -----------  ---------------  ---------------------  --------------
    leaf01  eth0         oob-mgmt-switch  swp6                   18m ago
    leaf01  swp1         server01         mac:44:38:39:00:00:03  18m ago
    leaf01  swp2         server02         mac:44:38:39:00:00:15  18m ago
    leaf01  swp49        leaf02           swp49                  18m ago
    leaf01  swp50        leaf02           swp50                  18m ago
    leaf01  swp51        spine01          swp1                   18m ago
    leaf01  swp52        spine02          swp1                   18m ago

To get the routing table for a server:

    cumulus@server01:~$ netq server01 show ip route
    Matching IP route records are:
    Origin Table            IP               Node             Nexthops                   Last Changed
    ------ ---------------- ---------------- ---------------- -------------------------- ----------------
    0      default          0.0.0.0/0        server01         192.168.0.254: eth0        10m ago
    1      default          10.1.20.0/24     server01         bond0                      10m ago
    1      default          10.1.20.1/32     server01         bond0                      10m ago
    1      default          192.168.0.0/24   server01         eth0                       10m ago
    1      default          192.168.0.31/32  server01         eth0                       10m ago
