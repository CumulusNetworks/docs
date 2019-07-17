---
title: Using NCLU to Troubleshoot Your Network Configuration
author: Cumulus Networks
weight: 4471
aliases:
 - /display/CL3740/Using-NCLU-to-Troubleshoot-Your-Network-Configuration
 - /pages/viewpage.action?pageId=83625996320
pageID: 83625996320
product: Cumulus Linux
version: 3.7.7'4.0'
imgData: cumulus-linux-37740
siteSlug: cumulus-linux-37740
---
The [network command line
utility](/version/cumulus-linux-37740/System-Configuration/Network-Command-Line-Utility---NCLU)
(NCLU) can quickly return a lot of information about your network
configuration.

## <span>net show Commands</span>

Running `net show` and pressing TAB displays all available command line
arguments usable by `net`. The output looks like this:

    cumulus@switch:~$ net show <TAB> 
        bfd            :  Bidirectional forwarding detection
        bgp            :  Border Gateway Protocol
        bridge         :  Aa layer2 bridge
        clag           :  Multi-Chassis Link Aggregation
        commit         :  apply the commit buffer to the system
        configuration  :  Ssettings, configuration state, etc
        counters       :  net show netstat counters
        debugs         :  Debugs
        dot1x          :  Configure, Enable, Delete or Show IEEE 802.1X EAPOL
        evpn           :  Ethernet VPN
        hostname       :  Systemlocal hostname
        igmp           :  Internet Group Management Protocol
        interface      :  An interface, such as swp1, swp2, etc.
        ip             :  Internet Protocol version 4/6
        ipv6           :  Internet Protocol version 6
        lldp           :  Link Layer Discovery Protocol
        lnv mpls           :  Lightweight Network VirtualizationMultiprotocol Label Switching
        mroute         :  Configure sStatic unicast routes into MRIB for multicast RPF lookup
        msdp           :  Multicast Source Discovery Protocol
        ospf           :  Open Shortest Path First (OSPFv2)
        ospf6          :  Open Shortest Path First (OSPFv3)
        package        :  A Cumulus Linux package name
        pbr            :  Policy Based Routing
        pim            :  Protocol Independent Multicast
        ptp            :  Precision Time Protocol
        rollback       :  revert to a previous configuration state
        route          :  Static routes
        route-map      :  Route-map
        snmp-server    :  Configure the SNMP server
        system         :  System information
        time           :  Time
        version        :  Version number
        vrf            :  Virtual Routing and Forwarding
        vrrp           :  Virtual Router Redundancy Protocol

## <span>Show Interfaces</span>

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

Whereas `net show interface all` displaysTo show every interface regardless of
 state, run `net show interface
all`:

    cumulus@switchleaf01:~$ net show interface all 
         State  Name     Speed    MTU    Mode           LLDP                    Summary
    -----  -------  -------  -----  -------------  ----------------------  -------------------------
    UP     lo       N/A      65536  Loopback                               IP: 1027.0.0.11/32, 127.0.0.1/8,/8
           lo                                                          IP: 10.0.0.11/32
           lo                                                          IP: ::1/128
    UP     eth0     1G       1500   Mgmt           oob-mgmt-switch (swp6)  IP: 192.168.0.11/24(DHCP)
    UP     swp1     1G       1500   Access/L2      Untagged: br0
    UP   server01 (eth1)         Master: br0(UP)
    ADMDN  swp2     1G     N/A  1500   NotConfigured
    ADMDN  swp45    0M     N/A  1500   NotConfigured
    ADMDN  swp46    0M     N/A  1500   NotConfigured
    ADMDN  swp47    0M     N/A  1500   NotConfigured
    ADMDN  swp48    0M     N/A  1500   NotConfigured
    ADMDN  swp49    0M     N/A  1500   NotConfigured
    ADMDN  swp50    0M     N/A  1500   NotConfigured
    UP     swp51    1G       1500   NotConfiguredDefault        spine01 (swp1)
    UP     swp52    1G       1500   NotConfigured
    UP     blue     N/A      65536  NotConfiguredDefault        spine02 (swp1)
    UP     br0      N/A      1500   Bridge/L3      IP: 172.16.1.1/24
                                                   Untagged Members: swp1
                                                   802.1q Tag: Untagged
                                                   STP: RootSwitch(32768)
    UP     red      N/A      65536  NotConfigured                        IP: 172.16.1.1/24
    ADMDN  vagrant  0M     N/A  1500   NotConfigured

You canTo get information about the switch itself by, running `net show
 system`:

    cumulus@switch:~$ net show system
    Hostname......... celRED
     
    Build............ Cumulus Linux 3.7.44.0.0~15551312781.35d3264370771.772c26b6
    Uptime........... 8 days, 12:24:01.770000
     
    Model............ Cel REDSTONE
    CPU.............. x86_64 Intel Atom C2538 2.4 GHz
    Memory........... 4GB
    Disk............. 14.9GB
    ASIC............. Broadcom Trident2 BCM56854
    Ports............ 48 x 10G-SFP+ & 6 x 40G-QSFP+
    Base MAC Address. a0:00:00:00:00:50
    Serial Number.... A1010B2A011212AB000001

## <span>Other Useful Featuresnetwork-docopt Package</span>

NCLU uses the [python
network-docopt](https://pypi.python.org/pypi/network-docopt) package.
This is inspired by [docopt](https://github.com/docopt/docopt) and
provides the abilityenables you to specify partial commands, without tab completion
and  or
running the complete option. For example:

`net show int` runs `netshow interface`  
`net show sys` runs `netshow system`

## <span>Install netshow on a Linux Server</span>

`netshow` is a tool developed by Cumulu    cumulus@switch~:$ net show int runs Nnetworks for troubleshooting
networks. In Cumulus Linux, it's been replaced by NCLU. However, NCLU is
not available on Linux hosts at this time, so Cumulus Networks
recommends you use `netshow` to help troubleshoot servers. To install
`show interface
    cumulus@switch~:$ net show` on a Linux server, run:

    root@host:~# pip install netshow-linux-lib

{{%notice note%}}

Debian and Red Hat packages will be available in the near future.

{{%/notice%}} sys runs netshow system

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
<!--stackedit_data:
eyJoaXN0b3J5IjpbLTc0MDAzNzIyMV19
-->