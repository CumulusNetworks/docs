---
title: Monitor Network Layer Protocols
author: Cumulus Networks
weight: 63
aliases:
 - /display/NETQ141/Monitor+Network+Layer+Protocols
 - /pages/viewpage.action?pageId=10453522
pageID: 10453522
product: Cumulus NetQ
version: 1.4.1
imgData: cumulus-netq-141
siteSlug: cumulus-netq-141
---
With NetQ, a network administrator can monitor OSI Layer 3 network
protocols running on Linux-based hosts, including IP (Internet
Protocol), BGP (Border Gateway Protocol) and OSPF (Open Shortest Path
First). NetQ provides the ability to:

  - Validate protocol configurations
  - Validate layer 3 communication paths

It helps answer questions such as:

  - Who are the IP neighbors for a switch?
  - How many IPv4 and IPv6 addresses am I using?
  - When did changes occur to my IP configuration?
  - Is BGP working as expected?
  - Is OSPF working as expected?
  - Can device A reach device B using IP addresses?

## Monitor IP Configuration

NetQ enables you to view the current status and the status an earlier
point in time. From this information, you can:

  - determine IP addresses of one or more interfaces
  - determine IP neighbors for one or more devices
  - determine IP routes owned by a device
  - identify changes to the IP configuration

The `netq show ip` command is used to obtain the address, neighbor, and
route information from the devices. Its syntax is:

    netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
    netq [<hostname>] show ip addresses [<remote-interface>] [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [around <text-time>] [count] [json]
    netq [<hostname>] show ipv6 addresses [<remote-interface>] [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]
     
    netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
    netq [<hostname>] show ip neighbors [<remote-interface>] [<ipv4>|<ipv4> vrf <vrf>|vrf <vrf>] [<mac>] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] [around <text-time>] [count] [json]
    netq [<hostname>] show ipv6 neighbors [<remote-interface>] [<ipv6>|<ipv6> vrf <vrf>|vrf <vrf>] [<mac>] changes [between <text-time> and <text-endtime>] [json]
     
    netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
    netq [<hostname>] show ip routes [<ipv4>|<ipv4/prefixlen>] [vrf <vrf>] [origin] changes [between <text-time> and <text-endtime>] [json]
    netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] [around <text-time>] [count] [json]
    netq [<hostname>] show ipv6 routes [<ipv6>|<ipv6/prefixlen>] [vrf <vrf>] [origin] changes [between <text-time> and <text-endtime>] [json]

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)
  - h: hour(s)
  - m: minute(s)
  - s: second(s)
  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### View IP Address Information

You can view the IPv4 and IPv6 address information for all of your
devices, including the interface and VRF for each device. Additionally,
you can:

  - view the information at an earlier point in time
  - view changes that have occurred over time
  - filter against a particular device, interface or VRF assignment
  - obtain a count of all of the addresses

Each of these provides information for troubleshooting potential
configuration and communication issues at the layer 3 level.

**Example: View IPv4 address information for all devices**

    cumulus@switch:~$ netq show ip addresses
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    10.0.0.11/32              leaf01            lo                        default         36m:9.186s
    10.0.0.12/32              leaf02            lo                        default         36m:5.412s
    10.0.0.13/32              leaf03            lo                        default         35m:58.302s
    10.0.0.14/32              leaf04            lo                        default         35m:47.537s
    10.0.0.21/32              spine01           lo                        default         35m:53.615s
    10.0.0.22/32              spine02           lo                        default         35m:44.264s
    10.0.0.254/32             oob-mgmt-server   eth0                      default         22d:17h:40m:1s
    172.16.1.1/24             leaf01            br0                       default         36m:6.258s
    172.16.1.101/24           server01          eth1                      default         23m:19.110s
    172.16.2.1/24             leaf02            br0                       default         35m:57.423s
    172.16.2.101/24           server02          eth2                      default         21m:48.101s
    172.16.3.1/24             leaf03            br0                       default         35m:53.635s
    172.16.3.101/24           server03          eth1                      default         21m:21.209s
    172.16.4.1/24             leaf04            br0                       default         35m:45.120s
    172.16.4.101/24           server04          eth2                      default         29m:48.461s
    172.17.0.1/16             oob-mgmt-server   docker0                   default         22d:17h:40m:1s
    192.168.0.11/24           leaf01            eth0                      default         22d:17h:39m:56s
    192.168.0.12/24           leaf02            eth0                      default         22d:17h:40m:9s
    192.168.0.13/24           leaf03            eth0                      default         22d:17h:40m:4s
    192.168.0.14/24           leaf04            eth0                      default         22d:17h:40m:0s
    192.168.0.21/24           spine01           eth0                      default         22d:17h:40m:0s
    192.168.0.22/24           spine02           eth0                      default         22d:17h:40m:3s
    192.168.0.254/24          oob-mgmt-server   eth1                      default         22d:17h:40m:1s
    192.168.0.31/24           server01          eth0                      default         17h:43m:21s
    192.168.0.32/24           server02          eth0                      default         17h:41m:47s
    192.168.0.33/24           server03          eth0                      default         17h:41m:24s
    192.168.0.34/24           server04          eth0                      default         22d:17h:39m:59s

**Example: View IPv6 address information for all devices**

    cumulus@switch:~$ netq show ipv6 addresses 
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    fe80::203:ff:fe11:1101/64 server01          eth1                      default         47m:55.917s
    fe80::203:ff:fe22:2202/64 server02          eth2                      default         46m:24.908s
    fe80::203:ff:fe33:3301/64 server03          eth1                      default         45m:58.184s
    fe80::203:ff:fe44:4402/64 server04          eth2                      default         54m:25.264s
    fe80::4638:39ff:fe00:18/6 leaf02            br0                       default         1h:0m:31s
    fe80::4638:39ff:fe00:1b/6 leaf03            swp52                     default         1h:0m:32s
    fe80::4638:39ff:fe00:1c/6 spine02           swp3                      default         1h:0m:19s
    fe80::4638:39ff:fe00:23/6 leaf03            br0                       default         1h:0m:26s
    fe80::4638:39ff:fe00:24/6 leaf01            swp52                     default         1h:0m:44s
    fe80::4638:39ff:fe00:25/6 spine02           swp1                      default         1h:0m:19s
    fe80::4638:39ff:fe00:28/6 leaf02            swp51                     default         1h:0m:42s
    fe80::4638:39ff:fe00:29/6 spine01           swp2                      default         1h:0m:29s
    fe80::4638:39ff:fe00:2c/6 leaf04            br0                       default         1h:0m:18s
    fe80::4638:39ff:fe00:3/64 leaf01            br0                       default         1h:0m:39s
    fe80::4638:39ff:fe00:3b/6 leaf04            swp51                     default         1h:0m:23s
    fe80::4638:39ff:fe00:3c/6 spine01           swp4                      default         1h:0m:27s
    fe80::4638:39ff:fe00:46/6 leaf04            swp52                     default         1h:0m:22s
    fe80::4638:39ff:fe00:47/6 spine02           swp4                      default         1h:0m:19s
    fe80::4638:39ff:fe00:4f/6 leaf03            swp51                     default         1h:0m:36s
    fe80::4638:39ff:fe00:50/6 spine01           swp3                      default         1h:0m:29s
    fe80::4638:39ff:fe00:53/6 leaf01            swp51                     default         1h:0m:44s
    fe80::4638:39ff:fe00:54/6 spine01           swp1                      default         1h:0m:29s
    fe80::4638:39ff:fe00:57/6 oob-mgmt-server   eth1                      default         22d:18h:4m:38s
    fe80::4638:39ff:fe00:5d/6 leaf02            swp52                     default         1h:0m:40s
    fe80::4638:39ff:fe00:5e/6 spine02           swp2                      default         1h:0m:19s
    fe80::5054:ff:fe77:c277/6 oob-mgmt-server   eth0                      default         22d:18h:4m:38s
    fe80::a200:ff:fe00:11/64  leaf01            eth0                      default         22d:18h:4m:33s
    fe80::a200:ff:fe00:12/64  leaf02            eth0                      default         22d:18h:4m:46s
    fe80::a200:ff:fe00:13/64  leaf03            eth0                      default         22d:18h:4m:41s
    fe80::a200:ff:fe00:14/64  leaf04            eth0                      default         22d:18h:4m:36s
    fe80::a200:ff:fe00:21/64  spine01           eth0                      default         22d:18h:4m:37s
    fe80::a200:ff:fe00:22/64  spine02           eth0                      default         22d:18h:4m:40s
    fe80::a200:ff:fe00:31/64  server01          eth0                      default         18h:7m:58s
    fe80::a200:ff:fe00:32/64  server02          eth0                      default         18h:6m:23s
    fe80::a200:ff:fe00:33/64  server03          eth0                      default         18h:6m:1s
    fe80::a200:ff:fe00:34/64  server04          eth0                      default         22d:18h:4m:36s

**Example: Filter IP Address Information for a Specific Interface**

This example shows the IPv4 address information for the *eth0* interface
on all devices.

    cumulus@switch:~$ netq show ip addresses eth0
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    10.0.0.254/32             oob-mgmt-server   eth0                      default         22d:17h:40m:1s
    192.168.0.11/24           leaf01            eth0                      default         22d:17h:39m:56s
    192.168.0.12/24           leaf02            eth0                      default         22d:17h:40m:9s
    192.168.0.13/24           leaf03            eth0                      default         22d:17h:40m:4s
    192.168.0.14/24           leaf04            eth0                      default         22d:17h:40m:0s
    192.168.0.21/24           spine01           eth0                      default         22d:17h:40m:0s
    192.168.0.22/24           spine02           eth0                      default         22d:17h:40m:3s
    192.168.0.31/24           server01          eth0                      default         17h:43m:21s
    192.168.0.32/24           server02          eth0                      default         17h:41m:47s
    192.168.0.33/24           server03          eth0                      default         17h:41m:24s
    192.168.0.34/24           server04          eth0                      default         22d:17h:39m:59s

**Example: Filter IP Address Information for a Specific Device**

This example shows the IPv6 address information for the *leaf01* switch.

    cumulus@switch:~$ netq leaf01 show ipv6 addresses 
    Matching address records:
    Address                   Hostname          Interface                 VRF             Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------------------------
    fe80::4638:39ff:fe00:24/6 leaf01            swp52                     default         4h:18m:49s
    fe80::4638:39ff:fe00:3/64 leaf01            br0                       default         4h:18m:45s
    fe80::4638:39ff:fe00:53/6 leaf01            swp51                     default         4h:18m:50s
    fe80::a200:ff:fe00:11/64  leaf01            eth0                      default         22d:21h:22m:39s

**Example: View Changes to IP Address Information**

This example shows the IPv4 address information that changed for all
devices between 7 and 30 days ago.

    cumulus@switch:~$ netq show ip addresses changes between 7d and 30d 
    Matching address records:
    Address                   Hostname          Interface                 VRF             DB State Last Changed
    ------------------------- ----------------- ------------------------- --------------- -------- -------------------------
    192.168.0.11/24           leaf01            eth0                      default         Add      22d:20h:52m:30s
    10.255.5.134/24           leaf01            vagrant                   default         Add      22d:20h:52m:30s
    192.168.0.34/24           server04          eth0                      default         Add      22d:20h:52m:33s
    192.168.0.14/24           leaf04            eth0                      default         Add      22d:20h:52m:34s
    192.168.0.21/24           spine01           eth0                      default         Add      22d:20h:52m:35s
    172.17.0.1/16             oob-mgmt-server   docker0                   default         Add      22d:20h:52m:35s
    192.168.0.254/24          oob-mgmt-server   eth1                      default         Add      22d:20h:52m:35s
    10.255.5.226/24           oob-mgmt-server   eth0                      default         Add      22d:20h:52m:35s
    192.168.0.22/24           spine02           eth0                      default         Add      22d:20h:52m:37s
    192.168.0.13/24           leaf03            eth0                      default         Add      22d:20h:52m:38s
    10.255.5.191/24           leaf03            vagrant                   default         Add      22d:20h:52m:38s
    192.168.0.12/24           leaf02            eth0                      default         Add      22d:20h:52m:43s
    10.255.5.32/24            leaf02            vagrant                   default         Add      22d:20h:52m:43s

**Example: Obtain a Count of IP Addresses Used in Network**

This example shows the number of IPv4 and IPv6 addresses in the network.

    cumulus@switch:~$ netq show ip addresses count
    Count of matching address records: 33
     
    cumulus@switch:~$ netq show ipv6 addresses count
    Count of matching address records: 42

### View IP Neighbor Information

You can view the IPv4 and IPv6 neighbor information for all of your
devices, including the interface port, MAC address, VRF assignment, and
whether it learns the MAC address from the peer (remote=yes).
Additionally, you can:

  - view the information at an earlier point in time
  - view changes that have occurred over time
  - filter against a particular device, interface, address or VRF
    assignment
  - obtain a count of all of the addresses

Each of these provides information for troubleshooting potential
configuration and communication issues at the layer 3 level.

**Example: View IPv4 Neighbor Information for All Devices**

    cumulus@switch:~$ netq show ip neighbors
    Matching neighbor records:
    IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
    ------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
    10.255.5.1                oob-mgmt-server   eth0                      52:54:00:0f:79:30  default         no     22d:21h:26m:33s
    169.254.0.1               leaf01            swp51                     44:38:39:00:00:54  default         no     4h:6m:17s
    169.254.0.1               leaf01            swp52                     44:38:39:00:00:25  default         no     4h:6m:18s
    169.254.0.1               leaf02            swp51                     44:38:39:00:00:29  default         no     4h:6m:16s
    169.254.0.1               leaf02            swp52                     44:38:39:00:00:5e  default         no     4h:6m:18s
    169.254.0.1               leaf03            swp51                     44:38:39:00:00:50  default         no     4h:6m:16s
    169.254.0.1               leaf03            swp52                     44:38:39:00:00:1c  default         no     4h:6m:17s
    169.254.0.1               leaf04            swp51                     44:38:39:00:00:3c  default         no     4h:6m:16s
    169.254.0.1               leaf04            swp52                     44:38:39:00:00:47  default         no     4h:6m:17s
    169.254.0.1               spine01           swp1                      44:38:39:00:00:53  default         no     4h:6m:17s
    169.254.0.1               spine01           swp2                      44:38:39:00:00:28  default         no     4h:6m:16s
    169.254.0.1               spine01           swp3                      44:38:39:00:00:4f  default         no     4h:6m:16s
    169.254.0.1               spine01           swp4                      44:38:39:00:00:3b  default         no     4h:6m:16s
    169.254.0.1               spine02           swp1                      44:38:39:00:00:24  default         no     4h:6m:8s
    169.254.0.1               spine02           swp2                      44:38:39:00:00:5d  default         no     4h:6m:8s
    169.254.0.1               spine02           swp3                      44:38:39:00:00:1b  default         no     4h:6m:7s
    169.254.0.1               spine02           swp4                      44:38:39:00:00:46  default         no     4h:6m:7s
    192.168.0.11              oob-mgmt-server   eth1                      a0:00:00:00:00:11  default         no     22d:21h:26m:33s
    192.168.0.12              oob-mgmt-server   eth1                      a0:00:00:00:00:12  default         no     22d:21h:26m:33s
    192.168.0.13              oob-mgmt-server   eth1                      a0:00:00:00:00:13  default         no     22d:21h:26m:33s
    192.168.0.14              oob-mgmt-server   eth1                      a0:00:00:00:00:14  default         no     22d:21h:26m:33s
    192.168.0.21              oob-mgmt-server   eth1                      a0:00:00:00:00:21  default         no     22d:21h:26m:33s
    192.168.0.22              oob-mgmt-server   eth1                      a0:00:00:00:00:22  default         no     22d:21h:26m:33s
    192.168.0.253             oob-mgmt-server   eth1                      a0:00:00:00:00:50  default         no     22d:21h:26m:33s
    192.168.0.254             leaf01            eth0                      44:38:39:00:00:57  default         no     22d:21h:26m:29s
    192.168.0.254             leaf02            eth0                      44:38:39:00:00:57  default         no     22d:21h:26m:41s
    ...

**Example: View IPv6 Neighbor Information for a Given Device.**

This example shows the IPv6 neighbors for *leaf02* switch.

    cumulus@switch$ netq leaf02 show ipv6 neighbors
    Matching neighbor records:
    IP Address                Hostname          Interface                 MAC Address        VRF             Remote Last Changed
    ------------------------- ----------------- ------------------------- ------------------ --------------- ------ -------------------------
    fe80::203:ff:fe22:2202    leaf02            br0                       00:03:00:22:22:02  default         no     4h:37m:59s
    fe80::4638:39ff:fe00:29   leaf02            swp51                     44:38:39:00:00:29  default         no     4h:41m:59s
    fe80::4638:39ff:fe00:4    leaf02            eth0                      44:38:39:00:00:04  default         no     22d:21h:46m:29s
    fe80::4638:39ff:fe00:5e   leaf02            swp52                     44:38:39:00:00:5e  default         no     4h:41m:58s
    fe80::a200:ff:fe00:31     leaf02            eth0                      a0:00:00:00:00:31  default         no     4h:37m:43s
    fe80::a200:ff:fe00:32     leaf02            eth0                      a0:00:00:00:00:32  default         no     4h:37m:56s
    fe80::a200:ff:fe00:33     leaf02            eth0                      a0:00:00:00:00:33  default         no     4h:37m:8s
    fe80::a200:ff:fe00:34     leaf02            eth0                      a0:00:00:00:00:34  default         no     4h:36m:40s

**Example: View Changes to IP Neighbors for All Devices**

This example shows changes to the IP neighbors for all devices in the
last 5 days. If you want to see changes since the devices were added,
remove the between keyword and values. If no changes are found, a *No
matching neighbor records found* message shows as the result.

    cumulus@switch:~$ netq show ip neighbors changes between now and 5d
    Matching neighbor records:
    IP Address                Hostname          Interface                 MAC Address        VRF             Remote DB State   Last Changed
    ------------------------- ----------------- ------------------------- ------------------ --------------- ------ ---------- -------------------------
    169.254.0.1               exit02            swp51                     44:38:39:00:00:22  default         no     Add        4d:20h:38m:6s
    169.254.0.1               exit02            swp52                     44:38:39:00:00:56  default         no     Add        4d:20h:38m:6s
    169.254.0.1               exit02            swp44                     44:38:39:00:00:3e  vrf1            no     Add        4d:20h:38m:6s
    192.168.0.254             exit02            eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:38m:6s
    192.168.0.254             exit02            eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:38m:14s
    10.255.0.1                exit02            vagrant                   52:54:00:09:40:06  default         no     Del        4d:20h:38m:14s
    169.254.0.1               exit01            swp44                     44:38:39:00:00:07  vrf1            no     Add        4d:20h:38m:30s
    192.168.0.254             exit01            eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:38m:30s
    169.254.0.1               exit01            swp52                     44:38:39:00:00:5b  default         no     Add        4d:20h:38m:30s
    169.254.0.1               exit01            swp51                     44:38:39:00:00:0a  default         no     Add        4d:20h:38m:30s
    192.168.0.254             exit01            eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:38m:38s
    10.255.0.1                exit01            vagrant                   52:54:00:09:40:06  default         no     Del        4d:20h:38m:38s
    169.254.0.1               spine02           swp30                     44:38:39:00:00:5a  default         no     Add        4d:20h:39m:30s
    169.254.0.1               spine02           swp29                     44:38:39:00:00:55  default         no     Add        4d:20h:39m:30s
    192.168.0.254             spine02           eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:39m:30s
    192.168.0.254             spine02           eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:39m:38s
    169.254.0.1               spine01           swp29                     44:38:39:00:00:21  default         no     Add        4d:20h:39m:58s
    192.168.0.254             spine01           eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:39m:58s
    169.254.0.1               spine01           swp30                     44:38:39:00:00:09  default         no     Add        4d:20h:39m:58s
    192.168.0.254             spine01           eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:40m:6s
    192.168.0.254             leaf04            eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:40m:41s
    169.254.1.1               leaf04            peerlink.4094             44:38:39:00:00:2e  default         no     Add        4d:20h:40m:41s
    192.168.0.254             leaf04            eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:40m:49s
    192.168.0.11              leaf03            eth0                      a0:00:00:00:00:11  mgmt            no     Add        4d:20h:44m:2s
    169.254.1.2               leaf03            peerlink.4094             44:38:39:00:00:2f  default         no     Add        4d:20h:44m:2s
    192.168.0.254             leaf03            eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:44m:2s
    192.168.0.254             leaf03            eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:44m:10s
    192.168.0.254             leaf02            eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:20h:44m:51s
    169.254.1.1               leaf02            peerlink.4094             44:38:39:00:00:10  default         no     Add        4d:20h:44m:51s
    192.168.0.254             leaf02            eth0                      44:38:39:00:00:57  default         no     Del        4d:20h:44m:59s
    192.168.0.254             leaf01            eth0                      44:38:39:00:00:57  mgmt            no     Add        4d:21h:31m:30s
    169.254.1.2               leaf01            peerlink.4094             44:38:39:00:00:11  default         no     Add        4d:21h:31m:30s
    192.168.0.13              leaf01            eth0                      a0:00:00:00:00:13  mgmt            no     Add        4d:21h:31m:30s
    192.168.0.254             leaf01            eth0                      44:38:39:00:00:57  default         no     Del        4d:21h:31m:38s

### View IP Routes Information

You can view the IPv4 and IPv6 routes for all of your devices, including
the IP address (with or without mask), the destination (by hostname) of
the route, next hops available, VRF assignment, and whether a host is
the owner of the route or MAC address. Additionally, you can:

  - view the information at an earlier point in time
  - view changes that have occurred over time
  - filter against a particular address or VRF assignment
  - obtain a count of all of the routes

Each of these provides information for troubleshooting potential
configuration and communication issues at the layer 3 level.

**Example: View IP Routes for All Devices**

This example shows the IPv4 and IPv6 routes for all devices in the
network.

    cumulus@switch:~$ netq show ipv6 routes 
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    yes    default         ::/0                           server04          lo                                  6h:1m:52s
    yes    default         ::/0                           server03          lo                                  6h:1m:53s
    yes    default         ::/0                           server01          lo                                  6h:1m:54s
    yes    default         ::/0                           server02          lo                                  6h:1m:53s
     
    cumulus@switch:~$ netq show ip routes 
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         0.0.0.0/0                      server02          192.168.0.254: eth0                 6h:8m:55s
    no     default         0.0.0.0/0                      server04          192.168.0.254: eth0                 6h:8m:54s
    no     default         0.0.0.0/0                      server01          192.168.0.254: eth0                 6h:8m:55s
    no     default         10.0.0.0/8                     server03          172.16.3.1: eth1                    6h:8m:54s
    no     default         10.0.0.0/8                     server02          172.16.2.1: eth2                    6h:8m:55s
    no     default         10.0.0.0/8                     server04          172.16.4.1: eth2                    6h:8m:54s
    no     default         10.0.0.0/8                     server01          172.16.1.1: eth1                    6h:8m:55s
    no     default         10.0.0.11/32                   leaf04            169.254.0.1: swp51,                 6h:15m:41s
                                                                            169.254.0.1: swp52
    no     default         10.0.0.11/32                   spine02           169.254.0.1: swp1                   6h:15m:42s
    no     default         10.0.0.11/32                   spine01           169.254.0.1: swp1                   6h:15m:48s
    no     default         10.0.0.12/32                   spine02           169.254.0.1: swp2                   6h:15m:42s
    no     default         10.0.0.12/32                   leaf04            169.254.0.1: swp51,                 6h:15m:41s
                                                                            169.254.0.1: swp52
    no     default         10.0.0.12/32                   spine01           169.254.0.1: swp2                   6h:15m:48s
    no     default         10.0.0.13/32                   leaf04            169.254.0.1: swp51,                 6h:15m:41s
                                                                            169.254.0.1: swp52
    no     default         10.0.0.13/32                   leaf01            169.254.0.1: swp51,                 6h:15m:41s
    ...

**Example: View IP Routes for a Given IP Address**

This example shows the routes available for an IP address of
10.0.0.12/32.

    cumulus@switch:~$ netq show ip routes 10.0.0.12
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         10.0.0.12/32                   leaf03            10.0.0.21: swp51, 10.0.0.22: swp52  5h:39m:57s
    no     default         10.0.0.12/32                   leaf01            10.0.0.21: swp51, 10.0.0.22: swp52  5h:39m:57s
    no     default         10.0.0.12/32                   leaf04            10.0.0.21: swp51, 10.0.0.22: swp52  5h:39m:57s
    no     default         10.0.0.12/32                   spine02           10.0.0.12: swp2                     5h:40m:1s
    no     default         10.0.0.12/32                   spine01           10.0.0.12: swp2                     5h:39m:56s
    yes    default         10.0.0.12/32                   leaf02            lo                                  5h:40m:21s

**Example: View IP Routes Owned by a Given Device**

This example shows the IPv4 routes that are owned by spine01 switch.

    cumulus@switch:~$ netq spine01 show ip routes origin 
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    yes    default         10.0.0.21/32                   spine01           lo                                  23h:47m:23s
    yes    default         192.168.0.0/24                 spine01           eth0                                23d:16h:51m:28s
    yes    default         192.168.0.21/32                spine01           eth0                                23d:16h:51m:28s

**Example: View IP Routes for a Given Device at a Prior Time**

This example show the IPv4 routes for spine01 switch about 24 hours ago.

    cumulus@switch:~$ netq spine01 show ip routes around 24h
    Matching routes records:
    Origin VRF             Prefix                         Hostname          Nexthops                            Last Changed
    ------ --------------- ------------------------------ ----------------- ----------------------------------- -------------------------
    no     default         10.0.0.11/32                   spine01           169.254.0.1: swp1                   3h:30m:12s
    no     default         10.0.0.12/32                   spine01           169.254.0.1: swp2                   3h:30m:12s
    no     default         10.0.0.13/32                   spine01           169.254.0.1: swp3                   3h:30m:11s
    no     default         10.0.0.14/32                   spine01           169.254.0.1: swp4                   3h:30m:11s
    no     default         172.16.1.0/24                  spine01           169.254.0.1: swp1                   3h:30m:13s
    no     default         172.16.2.0/24                  spine01           169.254.0.1: swp2                   3h:30m:13s
    no     default         172.16.3.0/24                  spine01           169.254.0.1: swp3                   3h:30m:13s
    no     default         172.16.4.0/24                  spine01           169.254.0.1: swp4                   3h:30m:13s
    yes    default         10.0.0.21/32                   spine01           lo                                  3h:46m:28s
    yes    default         192.168.0.0/24                 spine01           eth0                                22d:20h:50m:33s
    yes    default         192.168.0.21/32                spine01           eth0                                22d:20h:50m:33s

**Example: View the Number of IP Routes in Network**

This example shows the total number of IP routes for all devices in the
network.

    cumulus@switch:~$ netq show ip routes count
    Count of matching routes records: 125
     
    cumulus@switch:~$ netq show ipv6 routes count
    Count of matching routes records: 5

## Monitor BGP Configuration

If you have BGP running on your switches and hosts, you can monitor its
operation using the NetQ CLI. For each device, you can view its
associated neighbors, ASN (autonomous system number), peer ASN, receive
IP or EVPN address prefixes, and VRF assignment. Additionally, you can:

  - view the information at an earlier point in time
  - view changes that have occurred over time
  - filter against a particular device, ASN, or VRF assignment
  - validate it is operating correctly across the network

The `netq show bgp` command is used to obtain the BGP configuration
information from the devices. The `netq check bgp` command is used to
validate the configuration. The syntax of these commands is:

    netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] [around <text-time>] [json]
    netq [<hostname>] show bgp [<bgp-session>|asn <number-asn>] [vrf <vrf>] changes [between <text-time> and <text-endtime>] [json]
     
    netq check bgp [vrf <vrf>] [around <text-time>] [json]

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)
  - h: hour(s)
  - m: minute(s)
  - s: second(s)
  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### View BGP Configuration Information

NetQ enables you to view the BGP configuration of a single device or
across all of your devices at once. You can filter the results based on
an ASN, BGP session (IP address or interface name), or VRF assignment.
You can view the configuration in the past and view changes made to the
configuration within a given timeframe.

**Example: View BGP Configuration Information Across Network**

This example shows the BGP configuration across all of your switches. In
this scenario, BGP routing is configured between two spines and four
leafs. Each leaf switch has a unique ASN and the spine switches share an
ASN. The PfxRx column indicates that these devices have IPv4 address
prefixes. The second and third values in this column indicate IPv6 and
EVPN address prefixes when configured. This configuration was changed
just over one day ago.

    cumulus@switch:~$ netq show bgp
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    leaf01            swp51(spine01)               default         65011      65020      7/-/-        1d:3h:53m:22s
    leaf01            swp52(spine02)               default         65011      65020      7/-/-        1d:3h:37m:20s
    leaf02            swp51(spine01)               default         65012      65020      7/-/-        1d:3h:37m:30s
    leaf02            swp52(spine02)               default         65012      65020      7/-/-        1d:3h:37m:21s
    leaf03            swp51(spine01)               default         65013      65020      7/-/-        1d:3h:37m:30s
    leaf03            swp52(spine02)               default         65013      65020      7/-/-        1d:3h:37m:21s
    leaf04            swp51(spine01)               default         65014      65020      7/-/-        1d:3h:37m:29s
    leaf04            swp52(spine02)               default         65014      65020      7/-/-        1d:3h:37m:20s
    spine01           swp1(leaf01)                 default         65020      65011      2/-/-        1d:3h:53m:22s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/-        1d:3h:53m:22s
    spine01           swp3(leaf03)                 default         65020      65013      2/-/-        1d:3h:53m:22s
    spine01           swp4(leaf04)                 default         65020      65014      2/-/-        1d:3h:53m:22s
    spine02           swp1(leaf01)                 default         65020      65011      2/-/-        1d:3h:37m:20s
    spine02           swp2(leaf02)                 default         65020      65012      2/-/-        1d:3h:37m:20s
    spine02           swp3(leaf03)                 default         65020      65013      2/-/-        1d:3h:37m:20s
    spine02           swp4(leaf04)                 default         65020      65014      2/-/-        1d:3h:37m:19s

**Example: View BGP Configuration Information for a Given Device**

This example shows the BGP configuration information for the spine02
switch. The switch is peered with swp1 on leaf01, swp2 on leaf02, and so
on. Spine02 has an ASN of 65020 and each of the leafs have unique ASNs.

    cumulus@switch:~$ netq spine02 show bgp 
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    spine02           swp1(leaf01)                 default         65020      65011      2/-/-        1d:4h:55m:0s
    spine02           swp2(leaf02)                 default         65020      65012      2/-/-        1d:4h:55m:0s
    spine02           swp3(leaf03)                 default         65020      65013      2/-/-        1d:4h:55m:0s
    spine02           swp4(leaf04)                 default         65020      65014      2/-/-        1d:4h:54m:59s

**Example: View BGP Configuration Information for a Given ASN**

This example shows the BGP configuration information for ASN of *65013*.
This ASN is associated with leaf03 and so the results show the BGP
neighbors for that switch.

    cumulus@switch:~$ netq show bgp asn 65013 
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    leaf03            swp51(spine01)               default         65013      65020      7/-/-        1d:4h:54m:31s
    leaf03            swp52(spine02)               default         65013      65020      7/-/-        1d:4h:54m:22s

**Example: View BGP Configuration Information for a Prior Time**

This example shows the BGP configuration information as it was 12 hours
earlier.

    cumulus@switch:~$ netq show bgp around 12h
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ -------------------------
    leaf01            swp51(spine01)               default         65011      65020      7/-/-        17h:29m:26s
    leaf01            swp52(spine02)               default         65011      65020      7/-/-        17h:13m:24s
    leaf02            swp51(spine01)               default         65012      65020      7/-/-        17h:13m:34s
    leaf02            swp52(spine02)               default         65012      65020      7/-/-        17h:13m:25s
    leaf03            swp51(spine01)               default         65013      65020      7/-/-        17h:13m:34s
    leaf03            swp52(spine02)               default         65013      65020      7/-/-        17h:13m:25s
    leaf04            swp51(spine01)               default         65014      65020      7/-/-        17h:13m:33s
    leaf04            swp52(spine02)               default         65014      65020      7/-/-        17h:13m:24s
    spine01           swp1(leaf01)                 default         65020      65011      2/-/-        17h:29m:26s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/-        17h:29m:26s
    spine01           swp3(leaf03)                 default         65020      65013      2/-/-        17h:29m:26s
    spine01           swp4(leaf04)                 default         65020      65014      2/-/-        17h:29m:26s
    spine02           swp1(leaf01)                 default         65020      65011      2/-/-        17h:13m:24s
    spine02           swp2(leaf02)                 default         65020      65012      2/-/-        17h:13m:24s
    spine02           swp3(leaf03)                 default         65020      65013      2/-/-        17h:13m:24s
    spine02           swp4(leaf04)                 default         65020      65014      2/-/-        17h:13m:23s

**Example: View BGP Configuration Changes**

This example shows that BGP configuration changes were made about five
days ago on this network.

    cumulus@switch:~$ netq show bgp changes
    Matching bgp records:
    Hostname          Neighbor                     VRF             ASN        Peer ASN   PfxRx        DBState    Last Changed
    ----------------- ---------------------------- --------------- ---------- ---------- ------------ ---------- -------------------------
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Del        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Del        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Del        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Del        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Del        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Del        5d:1h:41m:31s
    spine01           swp2(leaf02)                 default         65020      65012      2/-/10       Add        5d:1h:41m:31s
    ...

### Validate BGP Operation

A single command enables you to validate that all configured route
peering is established across the network. The command checks for
duplicate router IDs and sessions that are in an unestablished state.
Either of these conditions trigger a configuration check failure. When a
failure is found, the reason is identified in the output along with the
time the issue occurred.

This example shows a check on the BGP operations that found no failed
sessions.

    cumulus@switch:~/$ netq check bgp
    Total Nodes: 15, Failed Nodes: 0, Total Sessions: 16, Failed Sessions: 0

This example shows a check on the BGP operations that found two failed
sessions. The results indicate that BGP peering on leaf03 that connects
to spine01 failed four minutes ago. The failure was caused by an
interface failure on leaf03 which has lead to BGP hold timer expiration
on spine01.

    cumulus@switch:~$ netq check bgp
    Total Sessions: 8 , Failed Sessions: 2
    Node     Neighbor    Peer ID    Reason              Time
    -------  ----------  ---------  ------------------  -------
    leaf03   swp51       spine01    Interface down      4m ago
    spine01  swp3        leaf03     Hold Timer Expired  4m ago

This example shows two failed BGP sessions because an interface is down
and possibly because an RA was not configured.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 10, Failed Nodes: 2, Total Sessions: 28 , Failed Sessions: 2, 
    Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
    ----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
    mlx-2700-03       default         uplink-1          spine-1           RA not configured(?)                          0.116739s
    spine-1           default         downlink-5        mlx-2700-03       Interface down                                0.116793s

This example shows four failed BGP sessions because peers are not
configured and possibly because an RA was not configured.

    cumulus@switch:~$ netq check bgp
    Total Nodes: 10, Failed Nodes: 3, Total Sessions: 28 , Failed Sessions: 4, 
    Hostname          VRF             Peer Name         Peer Hostname     Reason                                        Last Changed
    ----------------- --------------- ----------------- ----------------- --------------------------------------------- -------------------------
    mlx-2700-03       default         uplink-1          spine-1           Peer not configured                           4.59256s
    mlx-2700-03       default         uplink-2          unknown           RA not configured(?)                          4.63093s
    spine-1           default         downlink-5        mlx-2700-03       Peer not configured                           0.155377s
    spine-2           default         downlink-5        mlx-2700-03       Peer not configured                           0.155410s

## Monitor OSPF Configuration

If you have OSPF running on your switches and hosts, you can monitor its
operation using the NetQ CLI. For each device, you can view its
associated interfaces, areas, peers, state, and type of OSPF running
(numbered or unnumbered). Additionally, you can:

  - view the information at an earlier point in time
  - view changes that have occurred over time
  - filter against a particular device, interface, or area
  - validate it is operating correctly across the network

The `netq show ospf` command is used to obtain the OSPF configuration
information from the devices. The `netq check ospf` command is used to
validate the configuration. The syntax of these commands is:

    netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] [around <text-time>] [json]
    netq [<hostname>] show ospf [<remote-interface>] [area <area-id>] changes [between <text-time> and <text-endtime>] [json]
     
    netq check ospf [around <text-time>] [json] 

{{%notice note%}}

When entering a time value, you must include a numeric value *and* the
unit of measure:

  - d: day(s)
  - h: hour(s)
  - m: minute(s)
  - s: second(s)
  - now

For time ranges, the `<text-time>` is the most recent time and the
`<text-endtime>` is the oldest time. The values do not have to have the
same unit of measure.

{{%/notice%}}

### View OSPF Configuration Information

NetQ enables you to view the OSPF configuration of a single device or
across all of your devices at once. You can filter the results based on
a device, interface, or area. You can view the configuration in the past
and view changes made to the configuration within a given timeframe.

**Example: View OSPF Configuration Information Across the Network**

This example shows all devices included in OSPF unnumbered routing, the
assigned areas, state, peer and interface, and the last time this
information was changed.

    cumulus@switch:~$ netq show ospf
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      27.914477s
    leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      27.910094s
    leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      36.816204s
    leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      36.815804s
    leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      34.547961s
    leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      34.547727s
    leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      27.332121s
    leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      27.331475s
    spine01           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp51                     37.647986s
    spine01           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp51                     37.647565s
    spine01           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp51                     37.647786s
    spine01           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp51                     37.648211s
    spine02           swp1                      0.0.0.0      Unnumbered       Full       leaf01            swp52                     37.840344s
    spine02           swp2                      0.0.0.0      Unnumbered       Full       leaf02            swp52                     37.839967s
    spine02           swp3                      0.0.0.0      Unnumbered       Full       leaf03            swp52                     37.840188s
    spine02           swp4                      0.0.0.0      Unnumbered       Full       leaf04            swp52                     37.840626s

**Example: View OSPF Configuration Information for a Given Device>**

This example show the OSPF configuration
information for leaf01.

    cumulus@switch:~$ netq leaf01 show ospf
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      8m:58.461s
    leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      8m:58.457s

**Example: View OSPF Configuration Information for a Given Interface**

This example shows the OSPF configuration for all devices with the swp51
interface.

    cumulus@switch:~$ netq show ospf swp51 
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      11m:10.639s
    leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      11m:19.540s
    leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      11m:17.272s
    leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      11m:10.567s

**Example: View OSPF Configuration Information at a Prior Time**

This example shows the OSPF configuration
for all leaf switches about five minutes ago.

    cumulus@switch:~$ netq leaf* show ospf around 5m
     
    Matching ospf records:
    Hostname          Interface                 Area         Type             State      Peer Hostname     Peer Interface            Last Changed
    ----------------- ------------------------- ------------ ---------------- ---------- ----------------- ------------------------- -------------------------
    leaf01            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp1                      9m:10.128s
    leaf01            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp1                      9m:10.124s
    leaf02            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp2                      9m:19.305s
    leaf02            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp2                      9m:19.301s
    leaf03            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp3                      9m:16.762s
    leaf03            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp3                      9m:16.762s
    leaf04            swp51                     0.0.0.0      Unnumbered       Full       spine01           swp4                      9m:9.546s
    leaf04            swp52                     0.0.0.0      Unnumbered       Full       spine02           swp4                      9m:9.545s

### Validate OSPF Operation

A single command, `netq check ospf`, enables you to validate that all
configured route peering is established across the network. The command
checks for:

  - router ID conflicts, such as duplicate IDs
  - links that are down, or have mismatched MTUs
  - mismatched session parameters (hello timer, dead timer, area ids,
    and network type)

When peer information is not available, the command verifies whether
OSPF is configured on the peer and if so, whether the service is
disabled, shutdown, or not functioning.

All of these conditions trigger a configuration check failure. When a
failure is found, the reason is identified in the output along with the
time the issue occurred.

This example shows a check on the OSPF
operations that found no failed sessions.

    cumulus@switch:~$ netq check ospf
    Total Sessions: 16, Failed Sessions: 0

This example shows a check on the OSPF operations that found two failed
sessions. The results indicate the reason for the failure is a
mismatched MTU for two links .

    cumulus@switch:~$ netq check ospf
    Total Nodes: 21, Failed Nodes: 2, Total Sessions: 40 , Failed Sessions: 2,
    Hostname          Interface                 PeerID                    Peer IP                   Reason                                        Last Changed
    ----------------- ------------------------- ------------------------- ------------------------- --------------------------------------------- -------------------------
    spine-3           swp6                      0.0.0.23                  27.0.0.23                 mtu mismatch, mtu mismatch                    4.915650s
    torc-22           swp5                      0.0.0.17                  27.0.0.17                 mtu mismatch, mtu mismatch                    11.452045s

## View Paths between Devices

You can view the available paths between
two devices on the network currently and at a time in the past using
their IPv4 or IPv6 addresses. You can perform the trace in only one direction
or both, and view the output in one of three formats (*json,
pretty,* and *detail*). JSON output provides the output in a
JSON file format for ease of importing to other applications or
software. Pretty output lines up the paths in a pseudo-graphical manner
to help visualize multiple paths. Detail output is the default when not
specified, and is useful for traces with higher hop counts where the
pretty output wraps lines, making it harder to interpret the results.
The detail output displays a table with a row per hop and a set of rows
per path.

To view the paths, first identify the addresses for the source and destination
devices using the `netq show ip addresses` command (see syntax above), and then use
the `netq trace` command to see the available paths between those devices.

The trace command syntax is:

    netq trace <ip> from (<src-hostname>|<ip-src>) [vrf <vrf>] [around <text-time>] [bidir] [json|detail|pretty] [debug]

{{%notice note%}}

The syntax requires the destination device address first, *\<ip\>*, and
then the source device address or hostname.

The tracing function only knows about addresses that have already been
learned. If you find that a path is invalid or incomplete, you may need
to ping the identified device so that its address becomes known.

{{%/notice%}}

### View Paths between Two Switches with Pretty Output

This example first determines the IP addresses of the leaf01 and leaf03
switches, then shows the available paths between them. The results
include a summary of the trace, including the total number of paths
available, those with errors and warnings, and the MTU of the paths. In
this case, the results are displayed in pseudo-graphical output.

```
cumulus@switch:~$ netq leaf01 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.0.0.11/32              leaf01            lo                        default         27m:3.870s
10.0.0.11/32              leaf01            swp51                     default         27m:3.898s
10.0.0.11/32              leaf01            swp52                     default         27m:3.877s
172.16.1.1/24             leaf01            br0                       default         27m:3.653s
192.168.0.11/24           leaf01            eth0                      default         33m:59.368s
 
cumulus@switch:~$ netq leaf03 show ip addresses
Matching address records:
Address                   Hostname          Interface                 VRF             Last Changed
------------------------- ----------------- ------------------------- --------------- -------------------------
10.0.0.13/32              leaf03            lo                        default         55m:43.224s
10.0.0.13/32              leaf03            swp51                     default         55m:43.250s
10.0.0.13/32              leaf03            swp52                     default         55m:43.230s
172.16.3.1/24             leaf03            br0                       default         55m:43.754s
192.168.0.13/24           leaf03            eth0                      default         1h:2m:47s
 
cumulus@switch:~$ netq trace 10.0.0.13 from 10.0.0.11 pretty
Number of Paths: 2
Number of Paths with Errors: 0
Number of Paths with Warnings: 0
Path MTU: 1500
 
 leaf01 swp52 -- swp1 spine02 swp3 -- swp52 leaf03 <lo>  
        swp51 -- swp1 spine01 swp3 -- swp51 leaf03 <lo>  
```

### View Forward and Reverse Paths between Two Switches with Pretty Output

Like the previous example, this shows the paths between leaf01 and
leaf03 switches, but by adding the *bidir* keyword both the forward and
reverse paths are presented. Optionally, you can use the source device's
hostname to achieve the same results.

    cumulus@switch:~$ netq trace 10.0.0.13 from 10.0.0.11 bidir pretty
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 1500
     
     leaf01 swp52 -- swp1 spine02 swp3 -- swp52 leaf03 <lo>  
            swp51 -- swp1 spine01 swp3 -- swp51 leaf03 <lo>  
     
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 1500
     
     leaf03 swp52 -- swp3 spine02 swp1 -- swp52 leaf01 <lo>  
            swp51 -- swp3 spine01 swp1 -- swp51 leaf01 <lo>  

### View Paths between Two Switches with Detailed Output

This example provides the same path information as the pretty output,
but displays the information in a tabular output. In this case there, no
VLAN is configured, so the related fields are left blank.

    cumulus@switch:~$ netq trace 10.0.0.13 from 10.0.0.11 detail
    Number of Paths: 2
    Number of Paths with Errors: 0
    Number of Paths with Warnings: 0
    Path MTU: 1500
     
    Id  Hop Hostname        InPort          InVlan InTunnel              InRtrIf         InVRF           OutRtrIf        OutVRF          OutTunnel             OutPort         OutVlan
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    1   1   leaf01                                                                                       swp52           default                               swp52
        2   spine02         swp1                                         swp1            default         swp3            default                               swp3
        3   leaf03          swp52                                        swp52           default         lo
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
    2   1   leaf01                                                                                       swp51           default                               swp51
        2   spine01         swp1                                         swp1            default         swp3            default                               swp3
        3   leaf03          swp51                                        swp51           default         lo
    --- --- --------------- --------------- ------ --------------------- --------------- --------------- --------------- --------------- --------------------- --------------- -------
