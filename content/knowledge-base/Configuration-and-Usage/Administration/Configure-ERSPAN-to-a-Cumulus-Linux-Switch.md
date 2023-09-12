---
title: Configure ERSPAN to a Cumulus Linux Switch
author: NVIDIA
weight: 312
toc: 4
---

## Issue

This article applies to the following issues:

- A SPAN destination is not available.
- The interface type or types prevent using a laptop as a SPAN destination.

{{%notice note%}}

The control plane has to process this data, which impacts the CPU of the destination switch.

{{%/notice%}}

## Environment

- Cumulus Linux, all versions

## Resolution

Normal ERSPAN setup rules apply; see the [Network Troubleshooting chapter]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Network-Troubleshooting/#configure-erspan" >}}) for details.

1.  Create rules for SPAN source; for example:  

        cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/span.rules
        [iptables]
        -A FORWARD --in-interface swp50 -j ERSPAN --src-ip 192.168.0.1 --dst-ip 192.168.0.2
        -A FORWARD --out-interface swp50 -j ERSPAN --src-ip 192.168.0.1 --dst-ip 192.168.0.2

2.  Install the rules:  

        cumulus@switch:~$ sudo cl-acltool -i

3.  Verify you installed the SPAN rules:  

        cumulus@switch:~$ cl-acltool -L all | grep SPAN
        41229 4368K ERSPAN all -- swp50 any anywhere anywhere ERSPAN src-ip:192.168.0.1 dst-ip:192.168.0.2
        17540 1126K ERSPAN all -- any swp50 anywhere anywhere ERSPAN src-ip:192.168.0.1 dst-ip:192.168.0.2

{{%notice note%}}

The destination switch does not expect the ERSPAN packets, so it generates ICMP destination unreachable packets as a result. Any capture you take includes these packets.

{{%/notice%}}

To remove these packets, add an ACL like the following to the destination switch:

    cumulus@switch:~$ cat /etc/cumulus/acl/policy.d/span.rules
    [iptables]
    -A OUTPUT --out-interface swp3 -p icmp --icmp-type destination-unreachable -j DROP

<!-- ## Comments

**Rodney Olesak** June 26, 2020 16:52

To see the ERSPAN traffic at the destination IP using Wireshark, when selecting the interface to listen to, enter the following for protocol/filter:

    ip proto 0x2f

Once you start the capture, you will see the traffic from the device, without the GRE tunnel on you local wireshark. -->
