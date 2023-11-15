---
title: Create an ACL to Block New TCP Sessions Using TCP Flags
author: NVIDIA
weight: 313
toc: 4
---

## Issue
<!-- vale off -->
How do I apply an access control list (ACL) to allow already established TCP session traffic and block new TCP sessions on an ingress port based on TCP flags?
<!-- vale on -->
## Environment

- Cumulus Linux, all versions

## Overview

This solution operates on the theory that a TCP session gets established using the three-way handshake consisting of SYN, SYN-ACK, and ACK. Only SYN might exist in a new connection. ACK, FIN, and RST are not allowed in a new connection. For existing sessions, SYN might exist but only with an ACK.

By default, Cumulus Linux codes the ACL rules for the switch in multiple `*.rules` files under the default directory `/etc/cumulus/acl/policy.d`. Cumulus Linux processes the \*.rules files in sorted file order. Each ACL policy rules file might contain `iptables`, `ip6tables`, and `etables` categories under the tags `[iptables]`, `[ip6tables]`, and `[etables]` respectively. Note that you only use the `etables` category for layer 2, so the example below does not reference them.

After coding the rules, use `cl-acltool` to install and sync them in hardware.

The example solution below creates rules on the INPUT and FORWARD chains to drop ingress IPv4 and IPv6 TCP packets when the SYN bit is set and the RST, ACK, and FIN bits are reset. The default for the INPUT and FORWARD chains allows all other packets. `cl-acltool` applies the ACL to ports swp20 and swp21. Configuring this ACL prevents the creation of new TCP sessions that originate from ingress ports swp20 and swp21. The ACL does all for the creation of TCP sessions that originate from any other port.

## Configure the ACL Rules

Create `/etc/cumulus/acl/policy.d/50tcp_established.rules` and add the following configuration:

    INGRESS_INTF = swp20,swp21
    
    [iptables]
    -A INPUT,FORWARD --in-interface $INGRESS_INTF -p tcp --syn -j DROP
    [ip6tables]
    -A INPUT,FORWARD --in-interface $INGRESS_INTF -p tcp --syn -j DROP

The `--syn` flag in the above rule matches packets with the SYN bit set and the ACK, RST, and FIN bits cleared.

It is equivalent to using `-tcp-flags SYN,RST,ACK,FIN SYN.` For example, the above rule could be re-written as:

    -A INPUT,FORWARD --in-interface $INGRESS_INTF -p tcp --tcp-flags SYN,RST,ACK,FIN SYN -j DROP

Run `cl-acltool -i` to install the rules. If Cumulus Linux detects no errors, it installs the rules and syncs with the hardware. The following output indicates that `cl-acltool` installed the rules successfully:

    Reading rule file /etc/cumulus/acl/policy.d/50tcp_established.rules ...
    Processing rules in file /etc/cumulus/acl/policy.d/50tcp_established.rules ...
    Installing acl policy
    done.

## Verify the Rules

After installing the rules, use `cl-acltool -L all` to check that the rules are present and the packet and byte counters are incrementing as expected.

    Chain FORWARD (policy ACCEPT 41224 packets, 4653K bytes)
     pkts bytes target prot opt in out source destination 
     29 1856 DROP tcp -- swp20 any anywhere anywhere tcpflags: FIN,SYN,RST,ACK/SYN
     0 0 DROP tcp -- swp21 any anywhere anywhere tcpflags: FIN,SYN,RST,ACK/SYN
