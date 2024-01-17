---
title: Hosts
author: NVIDIA
weight: 830
toc: 3
---

The NetQ Agent monitors the following on Linux hosts:

- netlink
- Layer 2: LLDP and VLAN-aware bridge
- Layer 3: IPv4, IPv6
- systemctl for services
- Docker containers (refer to {{<link title="Monitor Container Environments Using Kubernetes API Server">}} for more information)

Using NetQ on a Linux host is the same as using it on a Cumulus Linux switch. For example, if you want to check LLDP neighbor information for a given host, run {{<link title="show/#netq show lldp" text="netq show lldp">}} and specify the hostname:

```
cumulus@host:~$ netq server01 show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
server01          eth0                      oob-mgmt-switch   swp2                      Thu Sep 17 20:27:48 2020
server01          eth1                      leaf01            swp1                      Thu Sep 17 20:28:21 2020
server01          eth2                      leaf02            swp1                      Thu Sep 17 20:28:21 2020
```

Then, to see LLDP from the switch perspective run the same command, specifying the hostname of the switch:

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

To view the routing table for a server, run {{<link title="show/#netq show ip routes" text="netq show ip routes">}}:

```
cumulus@host:~$ netq server01 show ip routes
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
## Related Information

- {{<link title="Host Inventory">}}