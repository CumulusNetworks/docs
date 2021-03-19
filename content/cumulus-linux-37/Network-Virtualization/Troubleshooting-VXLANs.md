---
title: Troubleshooting VXLANs
author: NVIDIA
weight: 155
pageID: 9014338
---
This topic discusses various ways you can verify and troubleshoot
VXLANs.

## Verify the Registration Node Daemon

Use the `vxrdctl vxlans` command to see the configured VNIs, the
local address being used to source the VXLAN tunnel, and the service
node being used.

```
cumulus@leaf1:~$ vxrdctl vxlans
VNI     Local Addr       Svc Node
===     ==========       ========
 10      10.2.1.1        10.2.1.3
 30      10.2.1.1        10.2.1.3
2000      10.2.1.1        10.2.1.3
```

```
cumulus@leaf2:~$ vxrdctl vxlans
VNI     Local Addr       Svc Node
===     ==========       ========
 10      10.2.1.2        10.2.1.3
 30      10.2.1.2        10.2.1.3
2000      10.2.1.2        10.2.1.3
```

Use the `vxrdctl peers` command to see configured VNIs and all VTEPs
(leaf switches) within the network that have them configured.

```
cumulus@leaf1:~$ vxrdctl peers
VNI         Peer Addrs
===         ==========
10          10.2.1.1, 10.2.1.2
30          10.2.1.1, 10.2.1.2
2000        10.2.1.1, 10.2.1.2
```

```
cumulus@leaf2:~$ vxrdctl peers
VNI         Peer Addrs
===         ==========
10          10.2.1.1, 10.2.1.2
30          10.2.1.1, 10.2.1.2
2000        10.2.1.1, 10.2.1.2
```

{{%notice note%}}

When head end replication mode is disabled, the command does not work.

Use the `vxrdctl peers` command to see the other VTEPs (leaf switches)
and the VNIs with which they are associated. This does not show anything
unless you enabled head end replication mode by setting the `head_rep`
option to *True*. Otherwise, replication is done by the service node.

    cumulus@leaf2:~$ vxrdctl peers
    Head-end replication is turned off on this device.
    This command will not provide any output

{{%/notice%}}

## Verify the Service Node Daemon

Use the `vxsndctl fdb` command to verify which VNIs belong to which VTEP
(leaf switches).

    cumulus@spine1:~$ vxsndctl fdb
    VNI    Address     Ageout
    ===    =======     ======
     10    10.2.1.1        82
     10    10.2.1.2        77
     30    10.2.1.1        82
     30    10.2.1.2        77
    2000    10.2.1.1        82
    2000    10.2.1.2        77

## Verify Traffic Flow and Check Counters

VXLAN transit traffic information is stored in a flat file located in
`/cumulus/switchd/run/stats/vxlan/all`.

    cumulus@leaf1:~$ cat /cumulus/switchd/run/stats/vxlan/all
    VNI                             : 10
    Network In Octets               : 1090
    Network In Packets              : 8
    Network Out Octets              : 1798
    Network Out Packets             : 13
    Total In Octets                 : 2818
    Total In Packets                : 27
    Total Out Octets                : 3144
    Total Out Packets               : 39
    VN Interface                    : vni: 10, swp32s0.10
    Total In Octets                 : 1728
    Total In Packets                : 19
    Total Out Octets                : 552
    Total Out Packets               : 18
    VNI                             : 30
    Network In Octets               : 828
    Network In Packets              : 6
    Network Out Octets              : 1224
    Network Out Packets             : 9
    Total In Octets                 : 2374
    Total In Packets                : 23
    Total Out Octets                : 2300
    Total Out Packets               : 32
    VN Interface                    : vni: 30, swp32s0.30
    Total In Octets                 : 1546
    Total In Packets                : 17
    Total Out Octets                : 552
    Total Out Packets               : 17
    VNI                             : 2000
    Network In Octets               : 676
    Network In Packets              : 5
    Network Out Octets              : 1072
    Network Out Packets             : 8
    Total In Octets                 : 2030
    Total In Packets                : 20
    Total Out Octets                : 2042
    Total Out Packets               : 30
    VN Interface                    : vni: 2000, swp32s0.20
    Total In Octets                 : 1354
    Total In Packets                : 15
    Total Out Octets                : 446

## Ping to Test Connectivity

To test the connectivity across the VXLAN tunnel with an ICMP echo
request (ping), make sure to ping from the server rather than the switch
itself.

{{%notice note%}}

SVIs (switch VLAN interfaces) are not supported when using VXLAN. There
cannot be an IP address on the bridge that also contains a VXLAN.

{{%/notice%}}

Following is the IP address information used in this example
configuration.

| VNI  | server1    | server2    |
| ---- | ---------- | ---------- |
| 10   | 10.10.10.1 | 10.10.10.2 |
| 2000 | 10.10.20.1 | 10.10.20.2 |
| 30   | 10.10.30.1 | 10.10.30.2 |

Test connectivity between VNI 10 connected servers by pinging from
server1:

    cumulus@server1:~$ ping 10.10.10.2
    PING 10.10.10.2 (10.10.10.2) 56(84) bytes of data.
    64 bytes from 10.10.10.2: icmp_seq=1 ttl=64 time=3.90 ms
    64 bytes from 10.10.10.2: icmp_seq=2 ttl=64 time=0.202 ms
    64 bytes from 10.10.10.2: icmp_seq=3 ttl=64 time=0.195 ms
    ^C
    --- 10.10.10.2 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2002ms
    rtt min/avg/max/mdev = 0.195/1.432/3.900/1.745 ms
    cumulus@server1:~$

The other VNIs were also tested and can be viewed in the expanded output
below.

Test connectivity between VNI-2000 connected servers by pinging from
server1:

    cumulus@server1:~$ ping 10.10.20.2
    PING 10.10.20.2 (10.10.20.2) 56(84) bytes of data.
    64 bytes from 10.10.20.2: icmp_seq=1 ttl=64 time=1.81 ms
    64 bytes from 10.10.20.2: icmp_seq=2 ttl=64 time=0.194 ms
    64 bytes from 10.10.20.2: icmp_seq=3 ttl=64 time=0.206 ms
    ^C
    --- 10.10.20.2 ping statistics ---
    3 packets transmitted, 3 received, 0% packet loss, time 2000ms
    rtt min/avg/max/mdev = 0.194/0.739/1.819/0.763 ms

Test connectivity between VNI-30 connected servers by pinging from
server1:

    cumulus@server1:~$ ping 10.10.30.2
    PING 10.10.30.2 (10.10.30.2) 56(84) bytes of data.
    64 bytes from 10.10.30.2: icmp_seq=1 ttl=64 time=1.85 ms
    64 bytes from 10.10.30.2: icmp_seq=2 ttl=64 time=0.239 ms
    64 bytes from 10.10.30.2: icmp_seq=3 ttl=64 time=0.185 ms
    64 bytes from 10.10.30.2: icmp_seq=4 ttl=64 time=0.212 ms
    ^C
    --- 10.10.30.2 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3000ms
    rtt min/avg/max/mdev = 0.185/0.622/1.853/0.711 ms

## Troubleshoot with MAC Addresses

Because there is no SVI, there is no way to ping from the server to the
directly attached leaf (top of rack) switch without cabling the switch
to itself. The easiest way to see if the server can reach the leaf
switch is to check the MAC address table of the leaf switch.

First, obtain the MAC address of the server:

    cumulus@server1:~$ ip addr show eth3.10 | grep ether
        link/ether 90:e2:ba:55:f0:85 brd ff:ff:ff:ff:ff:ff

Next, check the MAC address table of the leaf switch:

    cumulus@leaf1:~$ brctl showmacs br-10
    port name mac addr      vlan    is local?   ageing timer
    vni-10    46:c6:57:fc:1f:54 0   yes        0.00
    swp32s0.10 90:e2:ba:55:f0:85    0   no        75.87
    vni-10    90:e2:ba:7e:a9:c1 0   no        75.87
    swp32s0.10 ec:f4:bb:fc:67:a1    0   yes        0.00

*90:e2:ba:55:f0:85* appears in the MAC address table, which indicates
that connectivity is occurring between leaf1 and server1.

## Check the Service Node Configuration

Use the `ip -d link show` command to verify the service node, VNI, and
administrative state of a particular logical VNI interface:

    cumulus@leaf1:~$ ip -d link show vni-10
    35: vni-10: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master br-10 state UNKNOWN mode DEFAULT
        link/ether 46:c6:57:fc:1f:54 brd ff:ff:ff:ff:ff:ff
        vxlan id 10 remote 10.2.1.3 local 10.2.1.1 srcport 32768 61000 dstport 4789 ageing 1800 svcnode 10.2.1.3
        bridge_slave
