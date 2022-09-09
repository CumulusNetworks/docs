---
title: Monitor Internet Protocol Service
author: NVIDIA
weight: 940
toc: 3
---

With NetQ, a user can monitor IP (Internet Protocol) addresses, neighbors, and routes, including viewing the current status and the status an earlier point in time.

It helps answer questions such as:

<!-- vale off -->
- Who are the IP neighbors for each switch?
- How many IPv4 and IPv6 addresses am I using in total and on which interface?
- Which routes are owned by which switches?
- When did changes occur to my IP configuration?
<!-- vale on -->

You use the `netq show ip` command to obtain the address, neighbor, and route information from the devices. Its syntax is:

```
netq <hostname> show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [json]
netq show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [subnet|supernet|gateway] [around <text-time>] [json]
netq <hostname> show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [json]
netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
netq <hostname> show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [json]
    
netq <hostname> show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [json]
netq show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [subnet|supernet|gateway] [around <text-time>] [json]
netq <hostname> show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [json]
netq <hostname> show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [json]
```

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

For the `between` option, you can enter the start (`text-time`) and end time (`text-endtime`) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.
{{%/notice%}}

## View IP Address Information

You can view the IPv4 and IPv6 address information for all your devices, including the interface and VRF for each device. Additionally, you can:

- View the information at an earlier point in time
- Filter against a particular device, interface or VRF assignment
- Obtain a count of all addresses

Each of these provides information for troubleshooting potential configuration and communication issues at the layer 3 level.

### View IPv4 Address Information for All Devices

To view only IPv4 addresses, run `netq show ip addresses`. This example shows all IPv4 addresses in the reference topology.

```
cumulus@switch:~$ netq show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.10.10.104/32           spine04           lo                        default         Mon Oct 19 22:28:23 2020
192.168.200.24/24         spine04           eth0                                      Tue Oct 20 15:46:20 2020
10.10.10.103/32           spine03           lo                        default         Mon Oct 19 22:29:01 2020
192.168.200.23/24         spine03           eth0                                      Tue Oct 20 15:19:24 2020
192.168.200.22/24         spine02           eth0                                      Tue Oct 20 15:40:03 2020
10.10.10.102/32           spine02           lo                        default         Mon Oct 19 22:28:45 2020
192.168.200.21/24         spine01           eth0                                      Tue Oct 20 15:59:36 2020
10.10.10.101/32           spine01           lo                        default         Mon Oct 19 22:28:48 2020
192.168.200.38/24         server08          eth0                      default         Mon Oct 19 22:28:50 2020
192.168.200.37/24         server07          eth0                      default         Mon Oct 19 22:28:43 2020
192.168.200.36/24         server06          eth0                      default         Mon Oct 19 22:40:52 2020
10.1.20.105/24            server05          uplink                    default         Mon Oct 19 22:41:08 2020
10.1.10.104/24            server04          uplink                    default         Mon Oct 19 22:40:45 2020
192.168.200.33/24         server03          eth0                      default         Mon Oct 19 22:41:04 2020
192.168.200.32/24         server02          eth0                      default         Mon Oct 19 22:41:00 2020
10.1.10.101/24            server01          uplink                    default         Mon Oct 19 22:40:36 2020
10.255.1.228/24           oob-mgmt-server   vagrant                   default         Mon Oct 19 22:28:20 2020
192.168.200.1/24          oob-mgmt-server   eth1                      default         Mon Oct 19 22:28:20 2020
10.1.20.3/24              leaf04            vlan20                    RED             Mon Oct 19 22:28:47 2020
10.1.10.1/24              leaf04            vlan10-v0                 RED             Mon Oct 19 22:28:47 2020
192.168.200.14/24         leaf04            eth0                                      Tue Oct 20 15:56:40 2020
10.10.10.4/32             leaf04            lo                        default         Mon Oct 19 22:28:47 2020
10.1.20.1/24              leaf04            vlan20-v0                 RED             Mon Oct 19 22:28:47 2020
...
```

### View IPv6 Address Information for All Devices

To view only IPv6 addresses, run `netq show ipv6 addresses`. This example shows all IPv6 addresses in the reference topology.

```
cumulus@switch:~$ netq show ipv6 addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
fe80::4638:39ff:fe00:16c/ spine04           eth0                                      Mon Oct 19 22:28:23 2020
64
fe80::4638:39ff:fe00:27/6 spine04           swp5                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:2f/6 spine04           swp6                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:17/6 spine04           swp3                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:1f/6 spine04           swp4                      default         Mon Oct 19 22:28:23 2020
4
fe80::4638:39ff:fe00:7/64 spine04           swp1                      default         Mon Oct 19 22:28:23 2020
fe80::4638:39ff:fe00:f/64 spine04           swp2                      default         Mon Oct 19 22:28:23 2020
fe80::4638:39ff:fe00:2d/6 spine03           swp6                      default         Mon Oct 19 22:29:01 2020
4
fe80::4638:39ff:fe00:25/6 spine03           swp5                      default         Mon Oct 19 22:29:01 2020
4
fe80::4638:39ff:fe00:170/ spine03           eth0                                      Mon Oct 19 22:29:01 2020
64
fe80::4638:39ff:fe00:15/6 spine03           swp3                      default         Mon Oct 19 22:29:01 2020
4
...
```

### Filter IP Address Information

You can filter the IP address information by hostname, interface, or VRF.

This example shows the *IPv4* address information for the *eth0* interface on all devices.

```
cumulus@switch:~$ netq show ip addresses eth0
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
192.168.200.24/24         spine04           eth0                                      Tue Oct 20 15:46:20 2020
192.168.200.23/24         spine03           eth0                                      Tue Oct 20 15:19:24 2020
192.168.200.22/24         spine02           eth0                                      Tue Oct 20 15:40:03 2020
192.168.200.21/24         spine01           eth0                                      Tue Oct 20 15:59:36 2020
192.168.200.38/24         server08          eth0                      default         Mon Oct 19 22:28:50 2020
192.168.200.37/24         server07          eth0                      default         Mon Oct 19 22:28:43 2020
192.168.200.36/24         server06          eth0                      default         Mon Oct 19 22:40:52 2020
192.168.200.35/24         server05          eth0                      default         Mon Oct 19 22:41:08 2020
192.168.200.34/24         server04          eth0                      default         Mon Oct 19 22:40:45 2020
192.168.200.33/24         server03          eth0                      default         Mon Oct 19 22:41:04 2020
192.168.200.32/24         server02          eth0                      default         Mon Oct 19 22:41:00 2020
192.168.200.31/24         server01          eth0                      default         Mon Oct 19 22:40:36 2020
192.168.200.14/24         leaf04            eth0                                      Tue Oct 20 15:56:40 2020
192.168.200.13/24         leaf03            eth0                                      Tue Oct 20 15:40:56 2020
192.168.200.12/24         leaf02            eth0                                      Tue Oct 20 15:43:24 2020
192.168.200.11/24         leaf01            eth0                                      Tue Oct 20 16:12:00 2020
192.168.200.62/24         fw2               eth0                                      Tue Oct 20 15:31:29 2020
192.168.200.61/24         fw1               eth0                                      Tue Oct 20 15:56:03 2020
192.168.200.64/24         border02          eth0                                      Tue Oct 20 15:20:23 2020
192.168.200.63/24         border01          eth0                                      Tue Oct 20 15:46:57 2020
```

This example shows the *IPv6* address information for the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show ipv6 addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
fe80::4638:39ff:febe:efaa leaf01            vlan4002                  BLUE            Mon Oct 19 22:28:22 2020
/64
fe80::4638:39ff:fe00:8/64 leaf01            swp54                     default         Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:59/6 leaf01            vlan10                    RED             Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:59/6 leaf01            vlan20                    RED             Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:59/6 leaf01            vlan30                    BLUE            Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:2/64 leaf01            swp51                     default         Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:4/64 leaf01            swp52                     default         Mon Oct 19 22:28:22 2020
fe80::4638:39ff:febe:efaa leaf01            vlan4001                  RED             Mon Oct 19 22:28:22 2020
/64
fe80::4638:39ff:fe00:6/64 leaf01            swp53                     default         Mon Oct 19 22:28:22 2020
fe80::200:ff:fe00:1c/64   leaf01            vlan30-v0                 BLUE            Mon Oct 19 22:28:22 2020
fe80::200:ff:fe00:1b/64   leaf01            vlan20-v0                 RED             Mon Oct 19 22:28:22 2020
fe80::200:ff:fe00:1a/64   leaf01            vlan10-v0                 RED             Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:59/6 leaf01            peerlink.4094             default         Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:59/6 leaf01            bridge                    default         Mon Oct 19 22:28:22 2020
4
fe80::4638:39ff:fe00:17a/ leaf01            eth0                                      Mon Oct 19 22:28:22 2020
64
```

### View When IP Address Information Last Changed

You can view the last time that address information changed using the `netq show ip/ipv6 addresses` commands.

This example shows the last time *IPv4* address information changed for all devices ago. Note the value in the Last Changed column.

```
cumulus@switch:~$ netq show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.10.10.104/32           spine04           lo                        default         Mon Oct 12 22:28:12 2020
192.168.200.24/24         spine04           eth0                                      Tue Oct 13 15:59:37 2020
10.10.10.103/32           spine03           lo                        default         Mon Oct 12 22:28:23 2020
192.168.200.23/24         spine03           eth0                                      Tue Oct 13 15:33:03 2020
192.168.200.22/24         spine02           eth0                                      Tue Oct 13 16:08:11 2020
10.10.10.102/32           spine02           lo                        default         Mon Oct 12 22:28:30 2020
192.168.200.21/24         spine01           eth0                                      Tue Oct 13 15:47:16 2020
10.10.10.101/32           spine01           lo                        default         Mon Oct 12 22:28:03 2020
192.168.200.38/24         server08          eth0                      default         Mon Oct 12 22:28:41 2020
192.168.200.37/24         server07          eth0                      default         Mon Oct 12 22:28:37 2020
192.168.200.36/24         server06          eth0                      default         Mon Oct 12 22:40:44 2020
10.1.30.106/24            server06          uplink                    default         Mon Oct 12 22:40:44 2020
192.168.200.35/24         server05          eth0                      default         Mon Oct 12 22:40:40 2020
10.1.20.105/24            server05          uplink                    default         Mon Oct 12 22:40:40 2020
10.1.10.104/24            server04          uplink                    default         Mon Oct 12 22:40:33 2020
192.168.200.34/24         server04          eth0                      default         Mon Oct 12 22:40:33 2020
10.1.30.103/24            server03          uplink                    default         Mon Oct 12 22:40:51 2020
192.168.200.33/24         server03          eth0                      default         Mon Oct 12 22:40:51 2020
192.168.200.32/24         server02          eth0                      default         Mon Oct 12 22:40:38 2020
10.1.20.102/24            server02          uplink                    default         Mon Oct 12 22:40:38 2020
192.168.200.31/24         server01          eth0                      default         Mon Oct 12 22:40:33 2020
10.1.10.101/24            server01          uplink                    default         Mon Oct 12 22:40:33 2020
...
```

### Obtain a Count of IP Addresses Used on a Device

If you have concerns that a particular device an overload of addresses in use, you can quickly view the address count using the `count` option.

This example shows the number of *IPv4* and *IPv6* addresses on the *leaf01* switch.

```
cumulus@switch:~$ netq leaf01 show ip addresses count
Count of matching address records: 9

cumulus@switch:~$ netq leaf01 show ipv6 addresses count
Count of matching address records: 17
```

## View IP Neighbor Information

You can view the IPv4 and IPv6 neighbor information for all your devices, including the interface port, MAC address, VRF assignment, and whether it learns the MAC address from the peer (remote=yes).

Additionally, you can:

- View the information at an earlier point in time
- Filter against a particular device, interface, address or VRF assignment
- Obtain a count of all addresses

Each of these provides information for troubleshooting potential configuration and communication issues at the layer 3 level.

### View IP Neighbor Information for All Devices

You can view neighbor information for all devices running IPv4 or IPv6 using the `netq show ip/ipv6 neighbors` command.

This example shows all neighbors for devices running IPv4.

```
cumulus@switch:~$ netq show ip neighbors
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
169.254.0.1               spine04           swp1                      44:38:39:00:00:08  default         no     Mon Oct 19 22:28:23 2020
169.254.0.1               spine04           swp6                      44:38:39:00:00:30  default         no     Mon Oct 19 22:28:23 2020
169.254.0.1               spine04           swp5                      44:38:39:00:00:28  default         no     Mon Oct 19 22:28:23 2020
192.168.200.1             spine04           eth0                      44:38:39:00:00:6d                  no     Tue Oct 20 17:39:25 2020
169.254.0.1               spine04           swp4                      44:38:39:00:00:20  default         no     Mon Oct 19 22:28:23 2020
169.254.0.1               spine04           swp3                      44:38:39:00:00:18  default         no     Mon Oct 19 22:28:23 2020
169.254.0.1               spine04           swp2                      44:38:39:00:00:10  default         no     Mon Oct 19 22:28:23 2020
192.168.200.24            spine04           mgmt                      c6:b3:15:1d:84:c4                  no     Mon Oct 19 22:28:23 2020
192.168.200.250           spine04           eth0                      44:38:39:00:01:80                  no     Mon Oct 19 22:28:23 2020
169.254.0.1               spine03           swp1                      44:38:39:00:00:06  default         no     Mon Oct 19 22:29:01 2020
169.254.0.1               spine03           swp6                      44:38:39:00:00:2e  default         no     Mon Oct 19 22:29:01 2020
169.254.0.1               spine03           swp5                      44:38:39:00:00:26  default         no     Mon Oct 19 22:29:01 2020
192.168.200.1             spine03           eth0                      44:38:39:00:00:6d                  no     Tue Oct 20 17:25:19 2020
169.254.0.1               spine03           swp4                      44:38:39:00:00:1e  default         no     Mon Oct 19 22:29:01 2020
169.254.0.1               spine03           swp3                      44:38:39:00:00:16  default         no     Mon Oct 19 22:29:01 2020
169.254.0.1               spine03           swp2                      44:38:39:00:00:0e  default         no     Mon Oct 19 22:29:01 2020
192.168.200.250           spine03           eth0                      44:38:39:00:01:80                  no     Mon Oct 19 22:29:01 2020
169.254.0.1               spine02           swp1                      44:38:39:00:00:04  default         no     Mon Oct 19 22:28:46 2020
169.254.0.1               spine02           swp6                      44:38:39:00:00:2c  default         no     Mon Oct 19 22:28:46 2020
169.254.0.1               spine02           swp5                      44:38:39:00:00:24  default         no     Mon Oct 19 22:28:46 2020
...
```

### Filter IP Neighbor Information

You can filter the list of IP neighbor information to show only neighbors for a particular device, interface, address or VRF assignment.

This example shows the *IPv6* neighbors for *leaf02* switch.

```
cumulus@switch$ netq leaf02 show ipv6 neighbors
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
ff02::16                  leaf02            eth0                      33:33:00:00:00:16                  no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:32   leaf02            vlan10-v0                 44:38:39:00:00:32  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:febe:efaa leaf02            vlan4001                  44:38:39:be:ef:aa  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:3a   leaf02            vlan20-v0                 44:38:39:00:00:34  RED             no     Mon Oct 19 22:28:30 2020
ff02::1                   leaf02            mgmt                      33:33:00:00:00:01                  no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:3c   leaf02            vlan30                    44:38:39:00:00:36  BLUE            no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:59   leaf02            peerlink.4094             44:38:39:00:00:59  default         no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:59   leaf02            vlan20                    44:38:39:00:00:59  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:42   leaf02            vlan30-v0                 44:38:39:00:00:42  BLUE            no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:9    leaf02            swp51                     44:38:39:00:00:09  default         no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:44   leaf02            vlan10                    44:38:39:00:00:3e  RED             yes    Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:3c   leaf02            vlan30-v0                 44:38:39:00:00:36  BLUE            no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:32   leaf02            vlan10                    44:38:39:00:00:32  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:59   leaf02            vlan30                    44:38:39:00:00:59  BLUE            no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:190  leaf02            eth0                      44:38:39:00:01:90                  no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:40   leaf02            vlan20-v0                 44:38:39:00:00:40  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:44   leaf02            vlan10-v0                 44:38:39:00:00:3e  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:3a   leaf02            vlan20                    44:38:39:00:00:34  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:180  leaf02            eth0                      44:38:39:00:01:80                  no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:40   leaf02            vlan20                    44:38:39:00:00:40  RED             yes    Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:f    leaf02            swp54                     44:38:39:00:00:0f  default         no     Mon Oct 19 22:28:30 2020
```

This example shows all *IPv4* neighbors using the *RED* VRF. Note that the VRF name is case sensitive.

```
cumulus@switch:~$ netq show ip neighbors vrf RED
Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
10.1.10.2                 leaf04            vlan10                    44:38:39:00:00:5d  RED             no     Mon Oct 19 22:28:47 2020
10.1.20.2                 leaf04            vlan20                    44:38:39:00:00:5d  RED             no     Mon Oct 19 22:28:47 2020
10.1.10.3                 leaf03            vlan10                    44:38:39:00:00:5e  RED             no     Mon Oct 19 22:28:18 2020
10.1.20.3                 leaf03            vlan20                    44:38:39:00:00:5e  RED             no     Mon Oct 19 22:28:18 2020
10.1.10.2                 leaf02            vlan10                    44:38:39:00:00:59  RED             no     Mon Oct 19 22:28:30 2020
10.1.20.2                 leaf02            vlan20                    44:38:39:00:00:59  RED             no     Mon Oct 19 22:28:30 2020
10.1.10.3                 leaf01            vlan10                    44:38:39:00:00:37  RED             no     Mon Oct 19 22:28:22 2020
10.1.20.3                 leaf01            vlan20                    44:38:39:00:00:37  RED             no     Mon Oct 19 22:28:22 2020
```

This example shows all *IPv6* neighbors using the *vlan10* interface.

```
cumulus@netq-ts:~$ netq show ipv6 neighbors vlan10

Matching neighbor records:
IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
fe80::4638:39ff:fe00:44   leaf04            vlan10                    44:38:39:00:00:3e  RED             no     Mon Oct 19 22:28:47 2020
fe80::4638:39ff:fe00:5d   leaf04            vlan10                    44:38:39:00:00:5d  RED             no     Mon Oct 19 22:28:47 2020
fe80::4638:39ff:fe00:32   leaf04            vlan10                    44:38:39:00:00:32  RED             yes    Mon Oct 19 22:28:47 2020
fe80::4638:39ff:fe00:44   leaf03            vlan10                    44:38:39:00:00:3e  RED             no     Mon Oct 19 22:28:18 2020
fe80::4638:39ff:fe00:5e   leaf03            vlan10                    44:38:39:00:00:5e  RED             no     Mon Oct 19 22:28:18 2020
fe80::4638:39ff:fe00:32   leaf03            vlan10                    44:38:39:00:00:32  RED             yes    Mon Oct 19 22:28:18 2020
fe80::4638:39ff:fe00:44   leaf02            vlan10                    44:38:39:00:00:3e  RED             yes    Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:32   leaf02            vlan10                    44:38:39:00:00:32  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:59   leaf02            vlan10                    44:38:39:00:00:59  RED             no     Mon Oct 19 22:28:30 2020
fe80::4638:39ff:fe00:44   leaf01            vlan10                    44:38:39:00:00:3e  RED             yes    Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:32   leaf01            vlan10                    44:38:39:00:00:32  RED             no     Mon Oct 19 22:28:22 2020
fe80::4638:39ff:fe00:37   leaf01            vlan10                    44:38:39:00:00:37  RED             no     Mon Oct 19 22:28:22 2020
```

## View IP Routes Information

You can view the IPv4 and IPv6 routes for all your devices, including the IP address (with or without mask), the destination (by hostname) of the route, next hops available, VRF assignment, and whether a host is the owner of the route or MAC address. Additionally, you can:

- View the information at an earlier point in time
- Filter against a particular address or VRF assignment
- Obtain a count of all routes

Each of these provides information for troubleshooting potential configuration and communication issues at the layer 3 level.

### View IP Routes for All Devices

This example shows the IPv4 and IPv6 routes for all devices in the network.

```
cumulus@switch:~$ netq show ip routes
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no     default         10.0.1.2/32                    spine04           169.254.0.1: swp3,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.4/32                  spine04           169.254.0.1: swp3,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.3/32                  spine04           169.254.0.1: swp3,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.2/32                  spine04           169.254.0.1: swp1,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp2
no     default         10.10.10.1/32                  spine04           169.254.0.1: swp1,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp2
yes                    192.168.200.0/24               spine04           eth0                                Mon Oct 19 22:28:23 2020
yes                    192.168.200.24/32              spine04           eth0                                Mon Oct 19 22:28:23 2020
no     default         10.0.1.1/32                    spine04           169.254.0.1: swp1,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp2
yes    default         10.10.10.104/32                spine04           lo                                  Mon Oct 19 22:28:23 2020
no                     0.0.0.0/0                      spine04           Blackhole                           Mon Oct 19 22:28:23 2020
no     default         10.10.10.64/32                 spine04           169.254.0.1: swp5,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp6
no     default         10.10.10.63/32                 spine04           169.254.0.1: swp5,                  Mon Oct 19 22:28:23 2020
                                                                        169.254.0.1: swp6
...
```

```
cumulus@switch:~$ netq show ipv6 routes
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no                     ::/0                           spine04           Blackhole                           Mon Oct 19 22:28:23 2020
no                     ::/0                           spine03           Blackhole                           Mon Oct 19 22:29:01 2020
no                     ::/0                           spine02           Blackhole                           Mon Oct 19 22:28:46 2020
no                     ::/0                           spine01           Blackhole                           Mon Oct 19 22:28:48 2020
no     RED             ::/0                           leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no                     ::/0                           leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no     BLUE            ::/0                           leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no     RED             ::/0                           leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no                     ::/0                           leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no     BLUE            ::/0                           leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no     RED             ::/0                           leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
no                     ::/0                           leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
no     BLUE            ::/0                           leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
no     RED             ::/0                           leaf01            Blackhole                           Mon Oct 19 22:28:22 2020
no                     ::/0                           leaf01            Blackhole                           Mon Oct 19 22:28:22 2020
no     BLUE            ::/0                           leaf01            Blackhole                           Mon Oct 19 22:28:22 2020
no                     ::/0                           fw2               Blackhole                           Mon Oct 19 22:28:22 2020
no                     ::/0                           fw1               Blackhole                           Mon Oct 19 22:28:10 2020
no     RED             ::/0                           border02          Blackhole                           Mon Oct 19 22:28:38 2020
no                     ::/0                           border02          Blackhole                           Mon Oct 19 22:28:38 2020
no     BLUE            ::/0                           border02          Blackhole                           Mon Oct 19 22:28:38 2020
no     RED             ::/0                           border01          Blackhole                           Mon Oct 19 22:28:34 2020
no                     ::/0                           border01          Blackhole                           Mon Oct 19 22:28:34 2020
no     BLUE            ::/0                           border01          Blackhole                           Mon Oct 19 22:28:34 2020
```

### Filter IP Route Information

You can filter the IP route information listing for a particular device, interface address, VRF assignment or route origination.

This example shows the routes available for an IP address of *10.0.0.12*. The result shows nine available routes.

```
cumulus@switch:~$ netq show ip routes 10.0.0.12
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no                     0.0.0.0/0                      spine04           Blackhole                           Mon Oct 19 22:28:23 2020
no                     0.0.0.0/0                      spine03           Blackhole                           Mon Oct 19 22:29:01 2020
no                     0.0.0.0/0                      spine02           Blackhole                           Mon Oct 19 22:28:46 2020
no                     0.0.0.0/0                      spine01           Blackhole                           Mon Oct 19 22:28:48 2020
no     default         0.0.0.0/0                      server08          192.168.200.1: eth0                 Mon Oct 19 22:28:50 2020
no     default         0.0.0.0/0                      server07          192.168.200.1: eth0                 Mon Oct 19 22:28:43 2020
no     default         10.0.0.0/8                     server06          10.1.30.1: uplink                   Mon Oct 19 22:40:52 2020
no     default         10.0.0.0/8                     server05          10.1.20.1: uplink                   Mon Oct 19 22:41:08 2020
no     default         10.0.0.0/8                     server04          10.1.10.1: uplink                   Mon Oct 19 22:40:45 2020
no     default         10.0.0.0/8                     server03          10.1.30.1: uplink                   Mon Oct 19 22:41:04 2020
no     default         10.0.0.0/8                     server02          10.1.20.1: uplink                   Mon Oct 19 22:41:00 2020
no     default         10.0.0.0/8                     server01          10.1.10.1: uplink                   Mon Oct 19 22:40:36 2020
no     default         0.0.0.0/0                      oob-mgmt-server   10.255.1.1: vagrant                 Mon Oct 19 22:28:20 2020
no     BLUE            0.0.0.0/0                      leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no                     0.0.0.0/0                      leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no     RED             0.0.0.0/0                      leaf04            Blackhole                           Mon Oct 19 22:28:47 2020
no     BLUE            0.0.0.0/0                      leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no                     0.0.0.0/0                      leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no     RED             0.0.0.0/0                      leaf03            Blackhole                           Mon Oct 19 22:28:18 2020
no     BLUE            0.0.0.0/0                      leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
no                     0.0.0.0/0                      leaf02            Blackhole                           Mon Oct 19 22:28:30 2020
...
```

This example shows all *IPv4* routes owned by *spine01* switch.

```
cumulus@switch:~$ netq spine01 show ip routes origin
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
yes                    192.168.200.0/24               spine01           eth0                                Mon Oct 19 22:28:48 2020
yes                    192.168.200.21/32              spine01           eth0                                Mon Oct 19 22:28:48 2020
yes    default         10.10.10.101/32                spine01           lo                                  Mon Oct 19 22:28:48 2020
```

### View IP Routes for a Given Device at a Prior Time

As with most NetQ CLI commands, you can view a characteristic for a time in the past. The same is true with IP routes.

This example show the *IPv4* routes for *spine01* switch about *24* hours ago.

```
cumulus@switch:~$ netq spine01 show ip routes around 24h
Matching routes records:
Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
no     default         10.0.1.2/32                    spine01           169.254.0.1: swp3,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.4/32                  spine01           169.254.0.1: swp3,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.3/32                  spine01           169.254.0.1: swp3,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp4
no     default         10.10.10.2/32                  spine01           169.254.0.1: swp1,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp2
no     default         10.10.10.1/32                  spine01           169.254.0.1: swp1,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp2
yes                    192.168.200.0/24               spine01           eth0                                Sun Oct 18 22:28:41 2020
yes                    192.168.200.21/32              spine01           eth0                                Sun Oct 18 22:28:41 2020
no     default         10.0.1.1/32                    spine01           169.254.0.1: swp1,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp2
yes    default         10.10.10.101/32                spine01           lo                                  Sun Oct 18 22:28:41 2020
no                     0.0.0.0/0                      spine01           Blackhole                           Sun Oct 18 22:28:41 2020
no     default         10.10.10.64/32                 spine01           169.254.0.1: swp5,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp6
no     default         10.10.10.63/32                 spine01           169.254.0.1: swp5,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp6
no     default         10.0.1.254/32                  spine01           169.254.0.1: swp5,                  Sun Oct 18 22:28:41 2020
                                                                        169.254.0.1: swp6
```

### View the Number of IP Routes

You can view the total number of IP routes on all devices or for those on a particular device.

This example shows the total number of IPv4 and IPv6 routes for all devices on a the leaf01 switch.

```
cumulus@switch:~$ netq leaf01 show ip routes count
Count of matching routes records: 27
    
cumulus@switch:~$ netq leaf01 show ipv6 routes count
Count of matching routes records: 3
```

## View the History of an IP Address

It is useful when debugging to be able to see when the IP address configuration changed for an interface. The `netq show address-history` command makes this information available. It enables you to see:

- Each change made chronologically.
- Changes made between two points in time, using the `between` option.
- Only the difference between to points in time using the `diff` option.
- To order the output by selected output fields using the `listby` option.
- Each change made for the IP address on a particular interface, using the `ifname` option.

And as with many NetQ commands, the default time range used is now to one hour ago. You can view the output in JSON format as well.

The syntax of the command is:

```
netq [<hostname>] show address-history <text-prefix> [ifname <text-ifname>] [vrf <text-vrf>] [diff] [between <text-time> and <text-endtime>] [listby <text-list-by>] [json]
```

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

For the `between` option, you can enter the start (`text-time`) and end time (`text-endtime`) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{%/notice%}}

This example shows how to view a full chronology of changes for an IP address. If a caret (^) notation appeared, it would indicate that there was no change in this value from the row above.

```
cumulus@switch:~$ netq show address-history 10.1.10.2/24

Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Sep 29 15:35:21 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 15:35:24 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:07 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:08 2020  leaf01            vlan10       10.1.10.2                      24       RED
```

This example shows how to view the history of an IP address by hostname. If a caret (^) notation appeared, it would indicate that there was no change in this value from the row above.

```
cumulus@switch:~$ netq show address-history 10.1.10.2/24 listby hostname

Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Sep 29 17:25:08 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:07 2020  leaf03            vlan10       10.1.10.2                      24       RED
```

This example shows how to view the history of an IP address between now and two hours ago. If a caret (^) notation appeared, it would indicate that there was no change in this value from the row above.

```
cumulus@switch:~$ netq show address-history 10.1.10.2/24 between 2h and now

Matching addresshistory records:
Last Changed              Hostname          Ifname       Prefix                         Mask     Vrf
------------------------- ----------------- ------------ ------------------------------ -------- ---------------
Tue Sep 29 15:35:21 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 15:35:24 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:24:59 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:05 2020  leaf01            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:07 2020  leaf03            vlan10       10.1.10.2                      24       RED
Tue Sep 29 17:25:08 2020  leaf01            vlan10       10.1.10.2                      24       RED
```

## View the Neighbor History for an IP Address

It is useful when debugging to be able to see when the neighbor configuration changed for an IP address. The `netq show neighbor-history` command makes this information available. It enables you to see:

- Each change that made chronologically.
- Changes made between two points in time, using the `between` option.
- Only the difference between to points in time using the `diff` option.
- To order the output by selected output fields using the `listby` option.
- Each change made for the IP address on a particular interface, using the `ifname` option.

And as with many NetQ commands, the default time range used is now to one hour ago. You can view the output in JSON format as well.

The syntax of the command is:

```
netq [<hostname>] show neighbor-history <text-ipaddress> [ifname <text-ifname>] [diff] [between <text-time> and <text-endtime>] [listby <text-list-by>] [json]
```

{{%notice note%}}
When entering a time value, you must include a numeric value *and* the unit of measure:

- **w**: weeks
- **d**: days
- **h**: hours
- **m**: minutes
- **s**: seconds
- **now**

For the `between` option, you can enter the start (`text-time`) and end time (`text-endtime`) values as most recent first and least recent second, or vice versa. The values do not have to have the same unit of measure.

{{%/notice%}}

This example shows how to view a full chronology of changes for an IP address neighbor. If a caret (^) notation appeared, it would indicate that there was no change in this value from the row above.

```
cumulus@switch:~$ netq show neighbor-history 10.1.10.2

Matching neighborhistory records:
Last Changed              Hostname          Ifname       Vrf             Remote Ifindex        Mac Address        Ipv6     Ip Address
------------------------- ----------------- ------------ --------------- ------ -------------- ------------------ -------- -------------------------
Tue Sep 29 17:25:08 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:17 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
```

This example shows how to view the history of an IP address neighbor by hostname. If a caret (^) notation appeared, it would indicate that there was no change in this value from the row above.

```
cumulus@switch:~$ netq show neighbor-history 10.1.10.2 listby hostname

Matching neighborhistory records:
Last Changed              Hostname          Ifname       Vrf             Remote Ifindex        Mac Address        Ipv6     Ip Address
------------------------- ----------------- ------------ --------------- ------ -------------- ------------------ -------- -------------------------
Tue Sep 29 17:25:08 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:17 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
```

This example shows show to view the history of an IP address neighbor between now and two hours ago. If a caret (^) notation appeared, it would indicate that there was no change in this value from the row above.

```
cumulus@switch:~$ netq show neighbor-history 10.1.10.2 between 2h and now

Matching neighborhistory records:
Last Changed              Hostname          Ifname       Vrf             Remote Ifindex        Mac Address        Ipv6     Ip Address
------------------------- ----------------- ------------ --------------- ------ -------------- ------------------ -------- -------------------------
Tue Sep 29 15:35:18 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 15:35:22 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
Tue Sep 29 17:25:00 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:08 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
Tue Sep 29 17:25:08 2020  leaf02            vlan10       RED             no     24             44:38:39:00:00:59  no       10.1.10.2
Tue Sep 29 17:25:14 2020  leaf04            vlan10       RED             no     24             44:38:39:00:00:5d  no       10.1.10.2
```
