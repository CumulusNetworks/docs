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

Using NetQ on a Linux host is the same as using it on a Cumulus Linux switch. For example, if you want to check LLDP neighbor information for a given host, run {{<link title="show/#netq show lldp" text="netq show lldp">}} and specify the hostname:

```
nvidia@host:~$ netq server01 show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
server01          eth0                      oob-mgmt-switch   swp2                      Mon Dec  2 21:22:55 2024
server01          eth1                      leaf01            swp1                      Mon Dec  2 21:22:55 2024
server01          eth2                      leaf02            swp1                      Mon Dec  2 21:22:55 2024
```

Then, to see LLDP from the switch perspective run the same command, specifying the hostname of the switch:

```
nvidia@switch:~$ netq leaf01 show lldp
Matching lldp records:
Hostname          Interface                 Peer Hostname     Peer Interface            Last Changed
----------------- ------------------------- ----------------- ------------------------- -------------------------
leaf01            eth0                      oob-mgmt-switch   swp10                     Mon Dec  2 20:54:07 2024
leaf01            swp1                      server01          mac:48:b0:2d:22:00:2d     Mon Dec  2 20:54:07 2024
leaf01            swp2                      server02          mac:48:b0:2d:46:72:25     Mon Dec  2 20:54:07 2024
leaf01            swp3                      server03          mac:48:b0:2d:48:f3:9e     Mon Dec  2 20:54:07 2024
leaf01            swp49                     leaf02            swp49                     Mon Dec  2 20:54:07 2024
leaf01            swp50                     leaf02            swp50                     Mon Dec  2 20:54:07 2024
leaf01            swp52                     spine02           swp1                      Mon Dec  2 20:54:07 2024
leaf01            swp53                     spine03           swp1                      Mon Dec  2 20:54:07 2024
leaf01            swp54                     spine04           swp1                      Mon Dec  2 20:54:07 2024
```

To view the routing table for a server, run {{<link title="show/#netq show ip routes" text="netq show ip routes">}}:

```
nvidia@host:~$ netq server01 show ip routes
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Protocol     Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- ------------ -------------------------
false  default         0.0.0.0/0                      server01          192.168.200.1: eth0                 boot         Tue Oct  8 15:53:27 2024
false  default         0.0.0.0/0                      server01          192.168.200.1: eth0                 dhcp         Mon Dec  2 21:22:57 2024
false  default         10.0.0.0/8                     server01          10.1.10.1: uplink                   boot         Mon Dec  2 21:22:57 2024
true   default         10.1.10.0/24                   server01          uplink                              kernel       Mon Dec  2 21:22:57 2024
true   default         10.1.10.101/32                 server01          uplink                              kernel       Mon Dec  2 21:22:57 2024
false  default         10.188.0.0/16                  server01          192.168.200.1: eth0                 boot         Mon Dec  2 21:22:57 2024
true   default         192.168.200.0/24               server01          eth0                                kernel       Mon Dec  2 21:22:57 2024
false  default         192.168.200.1/32               server01          eth0                                dhcp         Mon Dec  2 21:22:57 2024
true   default         192.168.200.31/32              server01          eth0                                kernel       Mon Dec  2 21:22:57 2024
```
## Related Information

- {{<link title="Host Inventory">}}