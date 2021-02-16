---
title: Hardware-enabled DDOS Protection
author: NVIDIA
weight: 330
toc: 4
---
It is crucial to protect the control plane on the switch to ensure that the proper control plane applications have access to the CPU. Failure to do so increases vulnerabilities to a Denial of Service (DOS attack. Cumulus Linux provides control plane protection by default. In addition, you can configure DDOS protection to protect data plane, control plane, and management plane traffic on the switch. You can  configure Cumulus Linux to drop packets that match one or more of the following criteria while incurring no performance impact:

- Source IP address matches the destination address for IPv4 and IPv6 packets
- Source MAC address matches the destination MAC address
- Unfragmented or first fragment SYN packets with a source port of 0-1023
- TCP packets with control flags =0 and seq number == 0
- TCP packets with FIN, URG and PSH bits set and seq number == 0
- TCP packets with both SYN and FIN bits set
- TCP source PORT matches the destination port
- UDP source PORT matches the destination port
- First TCP fragment with partial TCP header
- TCP header has fragment offset value of 1
- ICMPv6 ping packets payload larger than programmed value of ICMP max size
- ICMPv4 ping packets payload larger than programmed value of ICMP max size
- Fragmented ICMP packet
- IPv6 fragment lower than programmed minimum IPv6 packet size

{{%notice note%}}

DDOS protection is not supported on Broadcom Hurricane2 and Mellanox Spectrum ASICs.

{{%/notice%}}

## Configure DDOS Protection

1. Open the `/etc/cumulus/datapath/traffic.conf` file in a text editor.

2. Enable DOS prevention checks by setting the `dos_enable` value to `true`:

    ```
    # To turn on/off Denial of Service (DOS) prevention checks
    dos_enable = true
    ```

3. Open the `/usr/lib/python2.7/dist-packages/cumulus/__chip_config/bcm/datapath.conf` file in a text editor. Set any of the DOS checks to *true*. For example:

    ```
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
    ```

    {{%notice note%}}

Configuring any of the following settings affects the {{<link url="Bidirectional-Forwarding-Detection-BFD/#echo-function" text="BFD echo">}} function. For example, if you enable `dos.udp_ports_eq`, all the BFD packets are dropped because the BFD protocol uses the same source and destination UDP ports.

```  
dos.sip_eq_dip
dos.smac_eq_dmac
dos.tcp_ctrl0_seq0
dos.tcp_flags_fup_seq0
dos.tcp_flags_syn_fin
dos.tcp_ports_eq
dos.tcp_syn_frag
dos.udp_ports_eq
```

    {{%/notice%}}

4. Restart `switchd`:

   {{<cl/restart-switchd>}}
