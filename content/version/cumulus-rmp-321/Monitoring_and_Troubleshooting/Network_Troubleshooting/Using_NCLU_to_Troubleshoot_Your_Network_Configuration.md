---
title: Using NCLU to Troubleshoot Your Network Configuration
author: Cumulus Networks
weight: 209
aliases:
 - /display/RMP321/Using+NCLU+to+Troubleshoot+Your+Network+Configuration
 - /pages/viewpage.action?pageId=5127563
pageID: 5127563
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
The [Network Command Line
Utility](/version/cumulus-rmp-321/System_Configuration/Network_Command_Line_Utility)
(NCLU) can quickly return a lot of information about your network
configuration.

## <span>Using net show Commands</span>

Running `net show` and pressing TAB displays all available command line
arguments usable by `net`. The output looks like this:

    cumulus@switch$ net show <TAB>
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

## <span>Showing Interfaces</span>

To show all available interfaces that are physically UP, run `netshow
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

    cumulus@switch:~$ netshow system
    Arctica 4804IP
    Cumulus Version 3.2.0
    Build: Cumulus RMP 3.2.0
    Uptime: 2 days, 21:31:00

## <span>Other Useful netshow Features</span>

`netshow` uses the [python
network-docopt](https://pypi.python.org/pypi/network-docopt) package.
This is inspired by [docopt](https://github.com/docopt/docopt) and
provides the ability to specify partial commands, without tab completion
and running the complete option. For example:

`net show int` runs `net show interface`  
`net show sys` runs `net show system`
