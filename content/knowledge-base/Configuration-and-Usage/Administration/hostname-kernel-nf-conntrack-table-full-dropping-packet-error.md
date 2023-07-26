---
title: hostname kernel nf_conntrack table full, dropping packet Error
author: NVIDIA
weight: 319
toc: 4
---

## Issue

By default, Cumulus Linux does not use connection tracking. However, it is possible to run commands that would result in loading the kernel modules into the running kernel and activating connection tracking (for example: `iptables -t nat -L`). There is a configurable limit to the number of connections you can track. After you reach this limit, this can result in packet drops and the following log messages appearing in `/var/log/syslog`:

    2019-02-25T03:45:03.778502+00:00 hostname kernel: [20763743.334180] nf_conntrack: table full, dropping packet
    2019-02-25T03:45:03.785333+00:00 hostname kernel: [20763743.340564] nf_conntrack: table full, dropping packet
    2019-02-25T03:45:03.787758+00:00 hostname kernel: [20763743.343469] nf_conntrack: table full, dropping packet

## Environment

- Cumulus Linux 3.y.z

## Cause

This issue occurs due to the activation of connection tracking modules in the kernel, which initiates tracking of all connections visible to the kernel. The number of connections to track is a configurable limit using the `net.netfilter.nf_conntrack_max` sysctl.

To check if the kernel modules are active in the running kernel:

    cumulus@switch:~$ cat proc/modules | grep conn
    nf_conntrack_ipv4 20480 1 - Live 0xffffffffa0474000
    nf_defrag_ipv4 16384 1 nf_conntrack_ipv4, Live 0xffffffffa048d000
    nf_conntrack 94208 3 nf_conntrack_ipv4,nf_nat_ipv4,nf_nat, Live 0xffffffffa045c000

## Resolution

Adjusting the connection tracker limit can help if you are exhausting the limit. However, it is possible to prevent the kernel modules from loading by creating a modules file as follows:

    cumulus@switch:~$ sudo nano /etc/modprobe.d/conntrack.conf
    install nf_conntrack /bin/true
    install nf_conntrack_ipv4 /bin/true
    install nf_nat /bin/true
    install iptable_nat /bin/true

{{%notice note%}}

This prevents any connection tracking features from working and can result in error messages from utilities that expect the modules to be present.

{{%/notice%}}
