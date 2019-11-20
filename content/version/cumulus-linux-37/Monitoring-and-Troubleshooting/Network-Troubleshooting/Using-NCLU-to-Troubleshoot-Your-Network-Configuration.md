---
title: Using NCLU to Troubleshoot Your Network Configuration
author: Cumulus Networks
weight: 471
aliases:
 - /display/DOCS/Using+NCLU+to+Troubleshoot+Your+Network+Configuration
 - /pages/viewpage.action?pageId=8362599
pageID: 8362599
product: Cumulus Linux
version: 3.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The [network command line
utility](../../../System-Configuration/Network-Command-Line-Utility-NCLU/)
(NCLU) can quickly return a lot of information about your network
configuration.

## net show Commands

Running `net show` and pressing TAB displays all available command line
arguments usable by `net`. The output looks like this:

    cumulus@switch:~$ net show <TAB>
        bgp            :  Border Gateway Protocol
        bridge         :  A layer2 bridge
        clag           :  Multi-Chassis Link Aggregation
        commit         :  apply the commit buffer to the system
        configuration  :  Settings, configuration state, etc
        counters       :  show netstat counters
        hostname       :  System hostname
        igmp           :  Internet Group Management Protocol
        interface      :  An interface such as swp1, swp2, etc
        ip             :  Internet Protocol version 4
        ipv6           :  Internet Protocol version 6
        lldp           :  Link Layer Discovery Protocol
        lnv            :  Lightweight Network Virtualization
        mroute         :  Configure static unicast route into MRIB for multicast RPF lookup
        msdp           :  Multicast Source Discovery Protocol
        ospf           :  Open Shortest Path First (OSPFv2)
        ospf6          :  Open Shortest Path First (OSPFv3)
        pim            :  Protocol Independent Multicast
        rollback       :  revert to a previous configuration state
        route          :  Static routes
        route-map      :  Route-map
        system         :  System information
        version        :  Version number

## Show Interfaces

To show all available interfaces that are physically UP, run `net show
interface`:

    cumulus@switch:~$ net show interface
     
        Name    Speed    MTU    Mode           Summary
    --  ------  -------  -----  -------------  --------------------------------------
    UP  lo      N/A      65536  Loopback       IP: 10.0.0.11/32, 127.0.0.1/8, ::1/128
    UP  eth0    1G       1500   Mgmt           IP: 192.168.0.11/24(DHCP)
    UP  swp1    1G       1500   Access/L2      Untagged: br0
    UP  swp2    1G       1500   NotConfigured
    UP  swp51   1G       1500   NotConfigured
    UP  swp52   1G       1500   NotConfigured
    UP  blue    N/A      65536  NotConfigured
    UP  br0     N/A      1500   Bridge/L3      IP: 172.16.1.1/24
                                               Untagged Members: swp1
                                               802.1q Tag: Untagged
                                               STP: RootSwitch(32768)
    UP  red     N/A      65536  NotConfigured

Whereas `net show interface all` displays every interface regardless of
state:

    cumulus@switch:~$ net show interface all
           Name     Speed    MTU    Mode           Summary
    -----  -------  -------  -----  -------------  --------------------------------------
    UP     lo       N/A      65536  Loopback       IP: 10.0.0.11/32, 127.0.0.1/8, ::1/128
    UP     eth0     1G       1500   Mgmt           IP: 192.168.0.11/24(DHCP)
    UP     swp1     1G       1500   Access/L2      Untagged: br0
    UP     swp2     1G       1500   NotConfigured
    ADMDN  swp45    0M       1500   NotConfigured
    ADMDN  swp46    0M       1500   NotConfigured
    ADMDN  swp47    0M       1500   NotConfigured
    ADMDN  swp48    0M       1500   NotConfigured
    ADMDN  swp49    0M       1500   NotConfigured
    ADMDN  swp50    0M       1500   NotConfigured
    UP     swp51    1G       1500   NotConfigured
    UP     swp52    1G       1500   NotConfigured
    UP     blue     N/A      65536  NotConfigured
    UP     br0      N/A      1500   Bridge/L3      IP: 172.16.1.1/24
                                                   Untagged Members: swp1
                                                   802.1q Tag: Untagged
                                                   STP: RootSwitch(32768)
    UP     red      N/A      65536  NotConfigured
    ADMDN  vagrant  0M       1500   NotConfigured

You can get information about the switch itself by running `net show
system`:

    cumulus@switch:~$ net show system
    Hostname......... celRED
     
    Build............ Cumulus Linux 3.7.4~1551312781.35d3264
    Uptime........... 8 days, 12:24:01.770000

    Model............ Cel REDSTONE
    CPU.............. x86_64 Intel Atom C2538 2.4 GHz
    Memory........... 4GB
    Disk............. 14.9GB
    ASIC............. Broadcom Trident2 BCM56854
    Ports............ 48 x 10G-SFP+ & 6 x 40G-QSFP+
    Base MAC Address. a0:00:00:00:00:50
    Serial Number.... A1010B2A011212AB000001

## Other Useful Features

NCLU uses the [python
network-docopt](https://pypi.python.org/pypi/network-docopt) package.
This is inspired by [docopt](https://github.com/docopt/docopt) and
provides the ability to specify partial commands, without tab completion
and running the complete option. For example:

`net show int` runs `netshow interface`  
`net show sys` runs `netshow system`

## Install netshow on a Linux Server

`netshow` is a tool developed by Cumulus Networks for troubleshooting
networks. In Cumulus Linux, it's been replaced by NCLU. However, NCLU is
not available on Linux hosts at this time, so Cumulus Networks
recommends you use `netshow` to help troubleshoot servers. To install
`netshow` on a Linux server, run:

    root@host:~# pip install netshow-linux-lib

{{%notice note%}}

Debian and Red Hat packages will be available in the near future.

{{%/notice%}}
