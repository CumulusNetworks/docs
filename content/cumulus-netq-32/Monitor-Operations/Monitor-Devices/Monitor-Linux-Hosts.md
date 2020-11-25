---
title: Monitor Linux Hosts
author: Cumulus Networks
weight: 840
toc: 3
---
Running NetQ on Linux hosts provides unprecedented network visibility, giving the network operator a complete view of the entire infrastructure's network connectivity instead of just from the network devices.

The NetQ Agent is supported on the following Linux hosts:

- CentOS 7
- Red Hat Enterprise Linux 7.1
- Ubuntu 18.04

You need to {{<link url="Install-NetQ" text="install the NetQ Agent">}} on every host you want to monitor with NetQ.

The NetQ Agent monitors the following on Linux hosts:

- netlink
- Layer 2: LLDP and VLAN-aware bridge
- Layer 3: IPv4, IPv6
- Routing on the Host: BGP, OSPF
- systemctl for services
- Docker containers - refer to the {{<link title="Monitor Container Environments Using Kubernetes API Server">}} topic

Using NetQ on a Linux host is the same as using it on a Cumulus Linux switch. For example, if you want to check LLDP neighbor information about a given host, run:

```
cumulus@host:~$ netq server01 show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
server01          eth0                      oob-mgmt-switch   swp2                      Thu Sep 17 20:27:48 2020
server01          eth1                      leaf01            swp1                      Thu Sep 17 20:28:21 2020
server01          eth2                      leaf02            swp1                      Thu Sep 17 20:28:21 2020

```

Then, to see LLDP from the switch perspective:

```
cumulus@switch:~$ netq leaf01 show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
leaf01            eth0                      oob-mgmt-switch   swp10                     Thu Sep 17 20:10:05 2020
leaf01            swp54                     spine04           swp1                      Thu Sep 17 20:26:13 2020
leaf01            swp53                     spine03           swp1                      Thu Sep 17 20:26:13 2020
leaf01            swp49                     leaf02            swp49                     Thu Sep 17 20:26:13 2020
leaf01            swp2                      server02          mac:44:38:39:00:00:34     Thu Sep 17 20:28:14 2020
leaf01            swp51                     spine01           swp1                      Thu Sep 17 20:26:13 2020
leaf01            swp52                     spine02           swp1                      Thu Sep 17 20:26:13 2020
leaf01            swp50                     leaf02            swp50                     Thu Sep 17 20:26:13 2020
leaf01            swp1                      server01          mac:44:38:39:00:00:32     Thu Sep 17 20:28:14 2020
leaf01            swp3                      server03          mac:44:38:39:00:00:36     Thu Sep 17 20:28:14 2020

```

To get the routing table for a server:

```
cumulus@host:~$ netq server01 show ip route
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no     default         0.0.0.0/0                      server01          192.168.200.1: eth0                 Thu Sep 17 20:27:30 2020
yes    default         192.168.200.31/32              server01          eth0                                Thu Sep 17 20:27:30 2020
yes    default         10.1.10.101/32                 server01          uplink                              Thu Sep 17 20:27:30 2020
no     default         10.0.0.0/8                     server01          10.1.10.1: uplink                   Thu Sep 17 20:27:30 2020
yes    default         192.168.200.0/24               server01          eth0                                Thu Sep 17 20:27:30 2020
yes    default         10.1.10.0/24                   server01          uplink                              Thu Sep 17 20:27:30 2020
```
