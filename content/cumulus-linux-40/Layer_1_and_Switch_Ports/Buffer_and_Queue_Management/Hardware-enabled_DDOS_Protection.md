---
title: Hardware-enabled DDOS Protection
author: Cumulus Networks
weight: 323
aliases:
 - /display/DOCS/Hardware-enabled+DDOS+Protection
 - /pages/viewpage.action?pageId=8363034
pageID: 8363034
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
It is crucial to also protect a switch’s control plane to ensure the
proper control plane applications have access to the switch’s CPU.
Failure to do so could increase vulnerabilities to a Denial of Service
(DOS) attack. Cumulus Linux provides control plane protection by
default. It also offers a DDOS protection mechanism, which protects data
plane, control plane and management plane traffic in the switch. It
drops any packets that match one or more of the following criteria while
incurring no performance impact:

  - Source IP address matches the destination address for IPv4 and IPv6
    packets

  - Source MAC address matches the destination MAC address

  - Unfragmented or first fragment SYN packets with a source port of
    0-1023

  - TCP packets with control flags =0 and seq number == 0

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

## <span>Supported ASICs</span>

DDOS protection is available for the following Broadcom ASICs:

  - Helix4

  - Maverick

  - Tomahawk

  - Tomahawk+

  - Trident

  - Trident-II

  - Trident-II+

  - Trident3

Cumulus Networks recommends enabling this feature when deploying a
switch with one of the above mentioned ASICs, as hardware-based DDOS
protection is disabled by default. Although Cumulus recommends enabling
all of the above criteria, they can be individually enabled if desired.
None of them are enabled by default.

DDOS protection is not supported on Broadcom Hurricane2 and Mellanox
Spectrum ASICs.

## <span>Configure Persistent DDOS Protection</span>

1.  Open the `/etc/cumulus/datapath/traffic.conf` file in a text editor.

2.  Enable DOS prevention checks by changing the following value to
    `true`, and save the file:
    
        # To turn on/off Denial of Service (DOS) prevention checks
        dos_enable = true

3.  Open the
    `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf`
    file in a text editor and set the following checks to *true*, and
    save the file:
    
        cumulus@switch:~$ sudo nano /usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf
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
    
    {{%notice note%}}
    
    Configuring any of the following settings affects the [BFD
    echo](/cumulus-linux/Layer_3/Bidirectional_Forwarding_Detection_-_BFD)
    function. For example, if you enable `dos.udp_ports_eq`, all the BFD
    packets will get dropped because the BFD protocol uses the same
    source and destination UDP ports.
    
    dos.sip\_eq\_dip
    
    dos.smac\_eq\_dmac
    
    dos.tcp\_ctrl0\_seq0
    
    dos.tcp\_flags\_fup\_seq0
    
    dos.tcp\_flags\_syn\_fin
    
    dos.tcp\_ports\_eq
    
    dos.tcp\_syn\_frag
    
    dos.udp\_ports\_eq
    
    {{%/notice%}}

4.  Restart `switchd` to enable DDOS protection:
    
        cumulus@switch:~$ sudo systemctl restart switchd.service
