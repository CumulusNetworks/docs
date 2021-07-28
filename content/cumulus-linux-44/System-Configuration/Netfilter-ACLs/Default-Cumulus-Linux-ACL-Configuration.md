---
title: Default Cumulus Linux ACL Configuration
author: NVIDIA
weight: 210
toc: 4
---
The Cumulus Linux default ACL configuration is split into three parts: `iptables`, `ip6tables`, and `ebtables`. The sections below describe the default configurations for each part. You can see the default file by clicking the Default ACL Configuration link:

{{<expand "Default ACL Configuration">}}

```
cumulus@switch:~$ sudo cl-acltool -L all
-------------------------------
Listing rules of type iptables:
-------------------------------
TABLE filter :
Chain INPUT (policy ACCEPT 167 packets, 16481 bytes)
    pkts bytes target     prot opt in     out     source               destination
      0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere
      0     0 DROP       all  --  swp+   any     loopback/8           anywhere
      0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere
      0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere
      0     0 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp dpt:3785 SETCLASS  class:7
      0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:3785 POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp dpt:3784 SETCLASS  class:7
      0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:3784 POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp dpt:4784 SETCLASS  class:7
      0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:4784 POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   ospf --  swp+   any     anywhere             anywhere             SETCLASS  class:7
      0     0 POLICE     ospf --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpt:bgp SETCLASS  class:7
      0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bgp POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp spt:bgp SETCLASS  class:7
      0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp spt:bgp POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpt:5342 SETCLASS  class:7
      0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:5342 POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp spt:5342 SETCLASS  class:7
      0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp spt:5342 POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   icmp --  swp+   any     anywhere             anywhere             SETCLASS  class:2
      1    84 POLICE     icmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:100 burst:40
      0     0 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp dpts:bootps:bootpc SETCLASS  class:2
      0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootps POLICE  mode:pkt rate:100 burst:100
      0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
      0     0 SETCLASS   tcp  --  swp+   any     anywhere             anywhere             tcp dpts:bootps:bootpc SETCLASS  class:2
      0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootps POLICE  mode:pkt rate:100 burst:100
      0     0 POLICE     tcp  --  any    any     anywhere             anywhere             tcp dpt:bootpc POLICE  mode:pkt rate:100 burst:100
      0     0 SETCLASS   udp  --  swp+   any     anywhere             anywhere             udp dpt:10001 SETCLASS  class:3
      0     0 POLICE     udp  --  any    any     anywhere             anywhere             udp dpt:10001 POLICE  mode:pkt rate:2000 burst:2000
      0     0 SETCLASS   igmp --  swp+   any     anywhere             anywhere             SETCLASS  class:6
      1    32 POLICE     igmp --  any    any     anywhere             anywhere             POLICE  mode:pkt rate:300 burst:100
      0     0 POLICE     all  --  swp+   any     anywhere             anywhere             addrtype match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
      0     0 POLICE     all  --  swp+   any     anywhere             anywhere             addrtype match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
      0     0 SETCLASS   all  --  swp+   any     anywhere             anywhere             SETCLASS  class:0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination
      0     0 DROP       all  --  swp+   any     240.0.0.0/5          anywhere
      0     0 DROP       all  --  swp+   any     loopback/8           anywhere
      0     0 DROP       all  --  swp+   any     base-address.mcast.net/8  anywhere
      0     0 DROP       all  --  swp+   any     255.255.255.255      anywhere

Chain OUTPUT (policy ACCEPT 107 packets, 12590 bytes)
    pkts bytes target     prot opt in     out     source               destination

TABLE mangle :
Chain PREROUTING (policy ACCEPT 172 packets, 17871 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain INPUT (policy ACCEPT 172 packets, 17871 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 111 packets, 18134 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain POSTROUTING (policy ACCEPT 111 packets, 18134 bytes)
    pkts bytes target     prot opt in     out     source               destination


TABLE raw :
Chain PREROUTING (policy ACCEPT 173 packets, 17923 bytes)
    pkts bytes target     prot opt in     out     source               destination

    Chain OUTPUT (policy ACCEPT 112 packets, 18978 bytes)
     pkts bytes target     prot opt in     out     source               destination


--------------------------------
Listing rules of type ip6tables:
--------------------------------
TABLE filter :
Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target    prot opt in     out     source               destination
      0     0 DROP       all      swp+   any     ip6-mcastprefix/8    anywhere
      0     0 DROP       all      swp+   any     ::/128               anywhere
      0     0 DROP       all      swp+   any     ::ffff:0.0.0.0/96    anywhere
      0     0 DROP       all      swp+   any     localhost/128        anywhere
      0     0 POLICE     udp      swp+   any     anywhere             anywhere             udp dpt:3785 POLICE  mode:pkt rate:2000 burst:2000 class:7
      0     0 POLICE     udp      swp+   any     anywhere             anywhere             udp dpt:3784 POLICE  mode:pkt rate:2000 burst:2000 class:7
      0     0 POLICE     udp      swp+   any     anywhere             anywhere             udp dpt:4784 POLICE  mode:pkt rate:2000 burst:2000 class:7
      0     0 POLICE     ospf     swp+   any     anywhere             anywhere             POLICE  mode:pkt rate:2000 burst:2000 class:7
      0     0 POLICE     tcp      swp+   any     anywhere             anywhere             tcp dpt:bgp POLICE  mode:pkt rate:2000 burst:2000 class:7
      0     0 POLICE     tcp      swp+   any     anywhere             anywhere             tcp spt:bgp POLICE  mode:pkt rate:2000 burst:2000 class:7
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmp router-solicitation POLICE  mode:pkt rate:100 burst:100 class:2
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmp router-advertisement POLICE  mode:pkt rate:500 burst:500 class:2
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmp neighbour-solicitation POLICE  mode:pkt rate:400 burst:400 class:2
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmp neighbour-advertisement POLICE  mode:pkt rate:400 burst:400 class:2
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmptype 130 POLICE  mode:pkt rate:200 burst:100 class:6
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmptype 131 POLICE  mode:pkt rate:200 burst:100 class:6
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmptype 132 POLICE  mode:pkt rate:200 burst:100 class:6
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             ipv6-icmptype 143 POLICE  mode:pkt rate:200 burst:100 class:6
      0     0 POLICE     ipv6-icmp    swp+   any     anywhere             anywhere             POLICE  mode:pkt rate:64 burst:40 class:2
      0     0 POLICE     udp      swp+   any     anywhere             anywhere             udp dpts:dhcpv6-client:dhcpv6-server POLICE  mode:pkt rate:100 burst:100 class:2
      0     0 POLICE     tcp      swp+   any     anywhere             anywhere             tcp dpts:dhcpv6-client:dhcpv6-server POLICE  mode:pkt rate:100 burst:100 class:2
      0     0 POLICE     all      swp+   any     anywhere             anywhere             addrtype match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
      0     0 POLICE     all      swp+   any     anywhere             anywhere             addrtype match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
      0     0 SETCLASS   all      swp+   any     anywhere             anywhere             SETCLASS  class:0

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target    prot opt in     out     source               destination
      0     0 DROP       all      swp+   any     ip6-mcastprefix/8    anywhere
      0     0 DROP       all      swp+   any     ::/128               anywhere
      0     0 DROP       all      swp+   any     ::ffff:0.0.0.0/96    anywhere
      0     0 DROP       all      swp+   any     localhost/128        anywhere

Chain OUTPUT (policy ACCEPT 5 packets, 408 bytes)
    pkts bytes target     prot opt in     out     source               destination


TABLE mangle :
Chain PREROUTING (policy ACCEPT 7 packets, 718 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain INPUT (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain POSTROUTING (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination


TABLE raw :
Chain PREROUTING (policy ACCEPT 7 packets, 718 bytes)
    pkts bytes target     prot opt in     out     source               destination

Chain OUTPUT (policy ACCEPT 0 packets, 0 bytes)
    pkts bytes target     prot opt in     out     source               destination

-------------------------------
Listing rules of type ebtables:
-------------------------------
TABLE filter :
Bridge table: filter

Bridge chain: INPUT, entries: 16, policy: ACCEPT
-d BGA -i swp+ -j setclass --class 7 , pcnt = 0 -- bcnt = 0
-d BGA -j police --set-mode pkt --set-rate 2000 --set-burst 2000 , pcnt = 0 -- bcnt = 0
-d 1:80:c2:0:0:2 -i swp+ -j setclass --class 7 , pcnt = 0 -- bcnt = 0
-d 1:80:c2:0:0:2 -j police --set-mode pkt --set-rate 2000 --set-burst 2000 , pcnt = 0 -- bcnt = 0
-d 1:80:c2:0:0:e -i swp+ -j setclass --class 6 , pcnt = 0 -- bcnt = 0
-d 1:80:c2:0:0:e -j police --set-mode pkt --set-rate 200 --set-burst 200 , pcnt = 0 -- bcnt = 0
-d 1:0:c:cc:cc:cc -i swp+ -j setclass --class 6 , pcnt = 0 -- bcnt = 0
-d 1:0:c:cc:cc:cc -j police --set-mode pkt --set-rate 200 --set-burst 200 , pcnt = 0 -- bcnt = 0
-p ARP -i swp+ -j setclass --class 2 , pcnt = 0 -- bcnt = 0
-p ARP -j police --set-mode pkt --set-rate 400 --set-burst 100 , pcnt = 0 -- bcnt = 0
-d 1:0:c:cc:cc:cd -i swp+ -j setclass --class 7 , pcnt = 0 -- bcnt = 0
-d 1:0:c:cc:cc:cd -j police --set-mode pkt --set-rate 2000 --set-burst 2000 , pcnt = 0 -- bcnt = 0
-p IPv4 -i swp+ -j ACCEPT , pcnt = 0 -- bcnt = 0
-p IPv6 -i swp+ -j ACCEPT , pcnt = 0 -- bcnt = 0
-i swp+ -j setclass --class 0 , pcnt = 0 -- bcnt = 0
-j police --set-mode pkt --set-rate 100 --set-burst 100 , pcnt = 0 -- bcnt = 0

Bridge chain: FORWARD, entries: 0, policy: ACCEPT

Bridge chain: OUTPUT, entries: 0, policy: ACCEPT
```

{{</expand>}}

## iptables

|Action/Value <img width=250/>|Protocol/IP Address<img width=450/>|
|---------------------------- |---------------------------------- |
| Drop<br>Destination IP: Any | Source IPv4:<br>240.0.0.0/5<br>loopback/8<br>224.0.0.0/4<br>255.255.255.255|
| Set class: 7<br>Police: Packet rate 2000 burst 2000<br>Source IP: Any<br>Destination IP: Any | Protocol:<br>UDP/BFD Echo<br>UDP/BFD Control<br>UDP BFD Multihop Control<br>OSPF<br>TCP/BGP (spt dpt 179)<br>TCP/MLAG (spt dpt 5342)|
| Set Class: 6<br>Police: Rate 300 burst 100<br>Source IP: Any<br>Destination IP: Any | Protocol:<br>IGMP |
| Set class: 2<br>Police: Rate 100 burst 40<br>Source IP : Any<br>Destination IP: Any | Protocol:<br>ICMP |
| Set class: 2<br>Police: Rate 100 burst 100<br>Source IP: Any<br>Destination IP: Any | Protocol:<br>UDP/bootpc, bootps |
| Set class: 0<br>Police: Rate 1000 burst 1000<br>Source IP: Any<br>Destination IP: Any | addrtype match dst-type LOCAL <br>**Note**: LOCAL is any local address -> Receiving a packet with a destination matching a local IP address on the switch goes to the CPU. |
| Set class: 0<br>Police: Rate 400 burst 100<br>Source IP: Any<br>Destination IP: Any | addrtype match dst-type IPROUTER <br>**Note**: IPROUTER is any unresolved address -> On a layer 2 or layer3 boundary receiving a packet from layer 3 and needs to go to CPU to ARP for the destination. |
| Set class 0 | All |

{{%notice note%}}
Set class is internal to the switch - it does not set any precedence bits.
{{%/notice%}}

## ip6tables

| Action/Value <img width=300/> | Protocol/IP Address <img width=400/> |
|------------------------------ |------------------------------------- |
| Drop | Source IPv6:<br>ff00::/8<br>::<br>::ffff:0.0.0.0/96<br>localhost |
| Set class: 7<br>Police: Packet rate 2000 burst 2000<br>Source IPv6: Any<br>Destination IPv6: Any |Protocol:<br>UDP/BFD Echo<br>UDP/BFD Control<br>UDP BFD Multihop Control<br>OSPF<br>TCP/BGP (spt dpt 179) |
| Set class: 6<br>Police: Packet Rte: 200 burst 100<br>Source IPv6: Any<br>Destination IPv6: Any |Protocol:<br>Multicast Listener Query (MLD)<br>Multicast<br>Listener Report (MLD)<br>Multicast Listener Done (MLD<br>Multicast Listener Report V2 |
| Set class: 2<br>Police: Packet rate: 100 burst 100<br>Source IPv6: Any<br>Destination IPv6: Any | Protocol:<br>ipv6-icmp router-solicitation |
| Set class: 2<br>Police: Packet rate: 500 burst 500<br>Source IPv6: Any<br>Destination IPv6: Any |Protocol:<br>ipv6-icmp router-advertisement POLICE |
| Set class: 2<br>Police: Packet rate: 400 burst 400<br>Source IPv6: Any<br>Destination IPv6: Any |Protocol:<br>ipv6-icmp neighbour-solicitation<br>ipv6-icmp neighbour-advertisement |
| Set class: 2<br>Police: Packet rate: 64 burst: 40<br>Source IPv6: Any<br>Destination IPv6: Any |Protocol:<br>Ipv6 icmp |
| Set class: 2<br>Police: Packet rate: 100 burst: 100<br>Source IPv6: Any<br>Destination IPv6: Any |Protocol:<br>UDP/dhcpv6-client:dhcpv6-server (Spts & dpts) |
| Police: Packet rate: 1000 burst 1000<br>Source IPv6: Any<br>Destination IPv6: Any | addrtype match dst-type LOCAL<br> **Note**: LOCAL is any local address -> Receiving a packet with a destination matching a local IPv6 address on the switch goes to the CPU. |
| Set class: 0<br>Police: Packet rate: 400 burst 100 | addrtype match dst-type IPROUTER<br> **Note:** IPROUTER is an unresolved address -> On a layer 2 or layer 3 boundary receiving a packet from layer 3 and needs to go to CPU to ARP for the destination. |
| Set class 0 | All |

{{%notice note%}}
Set class is internal to the switch - it does not set any precedence bits.
{{%/notice%}}

## ebtables

| Action/Value<img width=300/> | Protocol/MAC Address<img width=400/> |
|----------------------------- |------------------------------------- |
| Set Class: 7<br>Police: packet rate: 2000 burst rate:2000<br>Any switchport input interface |BDPU<br>LACP=<br>Cisco PVST |
| Set Class: 6<br>Police: packet rate: 200 burst rate: 200<br>Any switchport input inteface | LLDP<br>CDP |
| Set Class: 2<br>Police: packet rate: 400 burst rate: 100<br>Any switchport input interface | ARP |
| Catch All:<br>Allow all traffic<br>Any switchport input interface | IPv4<br>IPv6 |
| Catch All (applied at end):<br>Set class: 0<br>Police: packet rate 100 burst rate 100<br>Any switchport | ALL OTHER |

{{%notice note%}}
Set class is internal to the switch. It does not set any precedence bits.
{{%/notice%}}
