---
title: Configuring Hardware-enabled DDOS Protection
author: Cumulus Networks
weight: 287
aliases:
 - /display/CL321/Configuring+Hardware-enabled+DDOS+Protection
 - /pages/viewpage.action?pageId=5127006
pageID: 5127006
product: Cumulus Linux
version: 3.2.1
imgData: cumulus-linux-321
siteSlug: cumulus-linux-321
---
The DDOS protection mechanism protects data plane, control plane and
management plane traffic in the switch. It drops any packets that match
one or more of the following criteria while incurring no performance
impact:

  - Source IP address matches the destination address for IPv4 and IPv6
    packets

  - Source MAC address matches the destination MAC address

  - Unfragmented or first fragment SYN packets with a source port of
    0-1023

  - TCP packets with control flags = 0 and seq number == 0

  - TCP packets with FIN, URG and PSH bits set and seq number == 0

  - TCP packets with both SYN and FIN bits set

  - TCP source PORT matches the destination PORT

  - UDP source PORT matches the destination PORT

  - First TCP fragment with partial TCP header

  - TCP header has fragment offset value of 1

  - ICMPv6 ping packets payload larger than programmed value of ICMP max
    size

  - ICMPv4 ping packets payload larger than programmed value of ICMP max
    size

  - Fragmented ICMP packet

  - IPv6 fragment lower than programmed minimum IPv6 packet size

{{%notice note%}}

This configuration option is only available for Broadcom Trident,
Trident II, and Tomahawk chipsets.

{{%/notice%}}

Cumulus Networks recommends enabling this feature when deploying a
switch with the above mentioned ASICs, as hardware-based DDOS protection
is disabled by default. Although Cumulus recommends enabling all of the
above criteria, they can be individually enabled if desired.

## <span>Configure Persistent DDOS Protection</span>

1.  Open the `/etc/cumulus/datapath/traffic.conf` file in a text editor.

2.  Enable DOS prevention checks by changing the following value to
    `true`, and save the file:
    
        # To turn on/off Denial of Service (DOS) prevention checks
        dos_enable = true

3.  Open the
    `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf`
    file (on a Broadcom-based switch) or
    `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/datapath.conf`
    file (on a Mellanox-based switch) in a text editor.

4.  Set the following checks to `true`, and save the file:
    
        # Enabling/disabling Denial of service (DOS) prevetion checks
        # To change the default configuration:
        # enable/disable the individual DOS checks.
        dos.sip_eq_dip = true
        dos.smac_eq_dmac = true
        dos.tcp_hdr_partial = true
        dos.tcp_syn_frag = true
        dos.tcp_ports_eq = true
        dos.tcp_flags_syn_fin = true
        dos.tcp_flags_fup_seq0 = true
        dos.tcp_offset1 = true
        dos.tcp_ctrl0_seq0 = true
        dos.udp_ports_eq = true
        dos.icmp_frag = true
        dos.icmpv4_length = true
        dos.icmpv6_length = true
        dos.ipv6_min_frag = true

5.  Restart switchd to enable DOS protection:
    
        cumulus@switch:~$ sudo systemctl restart switchd.service
