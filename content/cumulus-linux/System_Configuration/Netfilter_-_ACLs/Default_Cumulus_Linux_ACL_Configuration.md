---
title: Default Cumulus Linux ACL Configuration
author: Cumulus Networks
weight: 295
aliases:
 - /display/DOCS/Default+Cumulus+Linux+ACL+Configuration
 - /pages/viewpage.action?pageId=8362574
pageID: 8362574
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The Cumulus Linux default ACL configuration is split into three parts,
as outlined in the [netfilter ACL
documentation](/cumulus-linux/System_Configuration/Netfilter_-_ACLs/):
IP tables, IPv6 tables, and EB tables. The sections below describe the
default configurations for each part. You can see the default file by
clicking the Default ACL Configuration link:

Default ACL Configuration

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
        0     0 POLICE     all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
        0     0 POLICE     all  --  swp+   any     anywhere             anywhere             ADDRTYPE match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
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
     pkts bytes target     prot opt in     out     source               destination         
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
        0     0 POLICE     all      swp+   any     anywhere             anywhere             ADDRTYPE match dst-type LOCAL POLICE  mode:pkt rate:1000 burst:1000 class:0
        0     0 POLICE     all      swp+   any     anywhere             anywhere             ADDRTYPE match dst-type IPROUTER POLICE  mode:pkt rate:400 burst:100 class:0
        0     0 SETCLASS   all      swp+   any     anywhere             anywhere             SETCLASS  class:0
     
    Chain FORWARD (policy ACCEPT 0 packets, 0 bytes)
     pkts bytes target     prot opt in     out     source               destination         
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

## <span>IP Tables</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Action/Value</p></th>
<th><p>Protocol/IP Address</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Drop</p>
<p>Destination IP: Any</p></td>
<td><p>Source IPv4:</p>
<ul>
<li><p>240.0.0.0/5</p></li>
<li><p>loopback/8</p></li>
<li><p>224.0.0.0/4</p></li>
<li><p>255.255.255.255</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 7</p>
<p>Police: Packet rate 2000 burst 2000</p>
<p>Source IP: Any</p>
<p>Destination IP: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>UDP/BFD Echo</p></li>
<li><p>UDP/BFD Control</p></li>
<li><p>UDP BFD Multihop Control</p></li>
<li><p>OSPF</p></li>
<li><p>TCP/BGP (spt dpt 179)</p></li>
<li><p>TCP/MLAG (spt dpt 5342)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Set Class: 6</p>
<p>Police: Rate 300 burst 100</p>
<p>Source IP: Any</p>
<p>Destination IP: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>IGMP</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 2</p>
<p>Police: Rate 100 burst 40</p>
<p>Source IP : Any</p>
<p>Destination IP: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>ICMP</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Set class: 2</p>
<p>Police: Rate 100 burst 100</p>
<p>Source IP: Any</p>
<p>Destination IP: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>UDP/bootpc, bootps</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 3</p>
<p>Police: Rate 2000 burst:2000</p>
<p>Source IP: Any</p>
<p>Destination IP: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>UDP/LNV</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Set class: 0</p>
<p>Police: Rate 1000 burst 1000</p>
<p>Source IP: Any</p>
<p>Destination IP: Any</p></td>
<td><p>ADDRTYPE match dst-type LOCAL</p>
<p>{{%notice note%}}</p>
<p>LOCAL is any local address -&gt; Receiving a packet with a destination matching a local IP address on the switch will go to the CPU.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>Set class: 0</p>
<p>Police: Rate 400 burst 100</p>
<p>Source IP: Any</p>
<p>Destination IP: Any</p></td>
<td><p>ADDRTYPE match dst-type IPROUTER</p>
<p>{{%notice note%}}</p>
<p>IPROUTER is any unresolved address -&gt; On a l2/l3 boundary receiving a packet from L3 and needs to go to CPU in order to ARP for the destination.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td><p>Set class 0</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

Set class is internal to the switch - it does not set any precedence
bits.

{{%/notice%}}

## <span>IPv6 Tables</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Action/Value</p></th>
<th><p>Protocol/IP Address</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Drop</p></td>
<td><p>Source IPv6:</p>
<ul>
<li><p>ff00::/8</p></li>
<li><p>::</p></li>
<li><p>::ffff:0.0.0.0/96</p></li>
<li><p>localhost</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 7</p>
<p>Police: Packet rate 2000 burst 2000</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>UDP/BFD Echo</p></li>
<li><p>UDP/BFD Control</p></li>
<li><p>UDP BFD Multihop Control</p></li>
<li><p>OSPF</p></li>
<li><p>TCP/BGP (spt dpt 179)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Set class: 6</p>
<p>Police: Packet Rte: 200 burst 100</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>Multicast Listener Query (MLD)</p></li>
<li><p>Multicast Listener Report (MLD)</p></li>
<li><p>Multicast Listener Done (MLD)</p></li>
<li><p>Multicast Listener Report V2</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 2</p>
<p>Police: Packet rate: 100 burst 100</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>ipv6-icmp router-solicitation</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Set class: 2</p>
<p>Police: Packet rate: 500 burst 500</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>ipv6-icmp router-advertisement POLICE</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 2</p>
<p>Police: Packet rate: 400 burst 400</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>ipv6-icmp neighbour-solicitation</p></li>
<li><p>ipv6-icmp neighbour-advertisement</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><p>Set class: 2</p>
<p>Police: Packet rate: 64 burst: 40</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<ul>
<li><p>Ipv6 icmp</p></li>
</ul></td>
</tr>
<tr class="even">
<td><p>Set class: 2</p>
<p>Police: Packet rate: 100 burst: 100</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>Protocol:</p>
<p>UDP/dhcpv6-client:dhcpv6-server (Spts &amp; dpts)</p></td>
</tr>
<tr class="odd">
<td><p>Police: Packet rate: 1000 burst 1000</p>
<p>Source IPv6: Any</p>
<p>Destination IPv6: Any</p></td>
<td><p>ADDRTYPE match dst-type LOCAL</p>
<p>{{%notice note%}}</p>
<p>LOCAL is any local address -&gt; Receiving a packet with a destination matching a local IPv6 address on the switch will go to the CPU.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="even">
<td><p>Set class: 0</p>
<p>Police: Packet rate: 400 burst 100</p></td>
<td><p>ADDRTYPE match dst-type IPROUTER</p>
<p>{{%notice note%}}</p>
<p>IPROUTER is an unresolved address -&gt; On a l2/l3 boundary receiving a packet from L3 and needs to go to CPU in order to ARP for the destination.</p>
<p>{{%/notice%}}</p></td>
</tr>
<tr class="odd">
<td><p>Set class 0</p></td>
<td><p>All</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

Set class is internal to the switch - it does not set any precedence
bits.

{{%/notice%}}

## <span>EB Tables</span>

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Action/Value</p></th>
<th><p>Protocol/MAC Address</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Set Class: 7</p>
<p>Police: packet rate: 2000 burst rate:2000</p>
<p>Any switchport input interface</p></td>
<td><p>BDPU</p>
<p>LACP</p>
<p>Cisco PVST</p></td>
</tr>
<tr class="even">
<td><p>Set Class: 6</p>
<p>Police: packet rate: 200 burst rate: 200</p>
<p>Any switchport input inteface</p></td>
<td><p>LLDP</p>
<p>CDP</p></td>
</tr>
<tr class="odd">
<td><p>Set Class: 2</p>
<p>Police: packet rate: 400 burst rate: 100</p>
<p>Any switchport input interface</p></td>
<td><p>ARP</p></td>
</tr>
<tr class="even">
<td><p>Catch All:</p>
<p>Allow all traffic</p>
<p>Any switchport input interface</p></td>
<td><p>IPv4</p>
<p>IPv6</p></td>
</tr>
<tr class="odd">
<td><p>Catch All (applied at end):</p>
<p>Set class: 0</p>
<p>Police: packet rate 100 burst rate 100</p>
<p>Any switchport</p></td>
<td><p>ALL OTHER</p></td>
</tr>
</tbody>
</table>

{{%notice note%}}

Set class is internal to the switch. It does not set any precedence
bits.

{{%/notice%}}
