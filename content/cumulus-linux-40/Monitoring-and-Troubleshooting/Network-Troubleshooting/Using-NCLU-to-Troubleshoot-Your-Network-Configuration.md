---
title: Using NCLU to Troubleshoot Your Network Configuration
author: NVIDIA
weight: 1050
toc: 4
---
The {{<link url="Network-Command-Line-Utility-NCLU" text="Network Command Line Utility">}} (NCLU) can quickly return a lot of information about your network configuration.

## net show Commands

Running `net show` and pressing TAB displays all available command line arguments usable by `net`. The output looks like this:

```
cumulus@switch:~$ net show <TAB>
bfd            :  Bidirectional forwarding detection
bgp            :  Border Gateway Protocol
bridge         :  a layer2 bridge
clag           :  Multi-Chassis Link Aggregation
commit         :  apply the commit buffer to the system
configuration  :  settings, configuration state, etc
counters       :  net show counters
debugs         :  Debugs
dot1x          :  Configure, Enable, Delete or Show IEEE 802.1X EAPOL
evpn           :  Ethernet VPN
hostname       :  local hostname
igmp           :  Internet Group Management Protocol
interface      :  An interface, such as swp1, swp2, etc.
ip             :  Internet Protocol version 4/6
ipv6           :  Internet Protocol version 6
lldp           :  Link Layer Discovery Protocol
mpls           :  Multiprotocol Label Switching
mroute         :  Static unicast routes in MRIB for multicast RPF lookup
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
```

## Show Interfaces

To show all available interfaces that are physically UP, run `net show interface`:

```
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
```

To show every interface regardless of state, run `net show interface all`:

```
cumulus@leaf01:~$ net show interface all
State  Name     Spd  MTU    Mode           LLDP                    Summary
-----  -------  ---  -----  -------------  ----------------------  -------------------------
UP     lo       N/A  65536  Loopback                               IP: 127.0.0.1/8
        lo                                                         IP: 10.0.0.11/32
        lo                                                         IP: ::1/128
UP     eth0     1G   1500   Mgmt           oob-mgmt-switch (swp6)  IP: 192.168.0.11/24(DHCP)
UP     swp1     1G   1500   Access/L2      server01 (eth1)         Master: br0(UP)
ADMDN  swp2     N/A  1500   NotConfigured
ADMDN  swp45    N/A  1500   NotConfigured
ADMDN  swp46    N/A  1500   NotConfigured
ADMDN  swp47    N/A  1500   NotConfigured
ADMDN  swp48    N/A  1500   NotConfigured
ADMDN  swp49    N/A  1500   NotConfigured
ADMDN  swp50    N/A  1500   NotConfigured
UP     swp51    1G   1500   Default        spine01 (swp1)
UP     swp52    1G   1500   Default        spine02 (swp1)
UP     br0      N/A  1500   Bridge/L3                               IP: 172.16.1.1/24
ADMDN  vagrant  N/A  1500   NotConfigured
```

To get information about the switch itself, run `net show system`:

```
cumulus@switch:~$ net show system
Hostname......... celRED

Build............ Cumulus Linux 4.0.0~1555370771.772c26b6
Uptime........... 8 days, 12:24:01.770000

Model............ Cel REDSTONE
CPU.............. x86_64 Intel Atom C2538 2.4 GHz
Memory........... 4GB
Disk............. 14.9GB
ASIC............. Broadcom Trident2 BCM56854
Ports............ 48 x 10G-SFP+ & 6 x 40G-QSFP+
Base MAC Address. a0:00:00:00:00:50
Serial Number.... A1010B2A011212AB000001
```

## network-docopt Package

NCLU uses the `{{<exlink url="https://pypi.python.org/pypi/network-docopt" text="python network-docopt">}}` package. This is inspired by `{{<exlink url="https://github.com/docopt/docopt" text="docopt">}}` and enables you to specify partial commands without tab completion or running the complete option. For example, `net show int` runs the `net show interface` command and `net show sys` runs the `net show system` command.
