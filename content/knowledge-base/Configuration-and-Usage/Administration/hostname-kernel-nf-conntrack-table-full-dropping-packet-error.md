---
title: hostname kernel nf_conntrack table full, dropping packet Error
author: NVIDIA
weight: 319
toc: 4
---

## Issue

By default, connection tracking is not used in Cumulus Linux. However, it is possible to run commands that would result in the kernel modules being loaded into the running kernel and connection tracking being activated (for example: `iptables -t nat -L`). There is a configurable limit to the number of connections that can be tracked. Once exhausted, this can result in packet drops and the following log messages appearing in `/var/log/syslog`:

    2019-02-25T03:45:03.778502+00:00 hostname kernel: [20763743.334180] nf_conntrack: table full, dropping packet
    2019-02-25T03:45:03.785333+00:00 hostname kernel: [20763743.340564] nf_conntrack: table full, dropping packet
    2019-02-25T03:45:03.787758+00:00 hostname kernel: [20763743.343469] nf_conntrack: table full, dropping packet

## Environment

- Cumulus Linux 3.y.z

## Cause

Connection tracking modules have been activated in the kernel and now all connections visible to the kernel are being tracked. The number of connections that can be tracked is a configurable limit using the `net.netfilter.nf_conntrack_max` sysctl.

To check if the kernel modules are active in the running kernel:

    cumulus@switch:~$ cat proc/modules | grep conn
    nf_conntrack_ipv4 20480 1 - Live 0xffffffffa0474000
    nf_defrag_ipv4 16384 1 nf_conntrack_ipv4, Live 0xffffffffa048d000
    nf_conntrack 94208 3 nf_conntrack_ipv4,nf_nat_ipv4,nf_nat, Live 0xffffffffa045c000

## Resolution

Adjusting the connection tracker limit may help if you are exhausting the limit. However, it is possible to prevent the kernel modules from loading by creating a modules file as follows:

    cumulus@switch:~$ sudo nano /etc/modprobe.d/conntrack.conf
    install nf_conntrack /bin/true
    install nf_conntrack_ipv4 /bin/true
    install nf_nat /bin/true
    install iptable_nat /bin/true

{{%notice note%}}

This prevents any connection tracking features from working and may result in error messages from utilities that expect the modules to be present.

{{%/notice%}}
