---
title: Using netshow to Troubleshoot Your Network Configuration
author: Cumulus Networks
weight: 345
aliases:
 - /display/CL31/Using+netshow+to+Troubleshoot+Your+Network+Configuration
 - /pages/viewpage.action?pageId=5121953
pageID: 5121953
product: Cumulus Linux
version: 3.1.2
imgData: cumulus-linux-312
siteSlug: cumulus-linux-312
---
`netshow` is a tool in Cumulus Linux that quickly returns a lot of
information about your network configuration. It's a tool designed by
network operators for network troubleshooters since existing command
line tools have too many options. `netshow` addresses this by leveraging
the network troubleshooting experience from a wide group of
troubleshooters and boiling it down to just a few important options.
`netshow` quickly aggregates basic network information on Linux devices
with numerous interfaces. `netshow` intelligently informs the
administrator what network type an interface belongs to, and shows the
most relevant information to a network administrator.

`netshow` can be used on any distribution of Linux, not just Cumulus
Linux.

## <span>Installing netshow</span>

`netshow` is installed by default in Cumulus Linux.

### <span>Installing netshow on a Linux Server or in OpenStack</span>

To install `netshow` on a Linux server, run:

    root@host:~# pip install netshow-linux-lib

{{%notice note%}}

Debian and Red Hat packages will be available in the near future.

{{%/notice%}}

## <span>Using netshow</span>

Running `netshow` with no arguments displays all available command line
arguments usable by `netshow`. (Running `netshow --help` gives you the
same information.) The output looks like this:

    cumulus@switch:~$ netshow
    Usage:
        netshow system [--json | -j ]
        netshow counters [errors] [all] [--json | -j | -l | --legend ]
        netshow lldp [--json | -j | -l | --legend ]
        netshow interface [<iface>] [all] [--mac | -m ] [--oneline | -1 | --json | -j | -l | --legend ]
        netshow access [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow bridges [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow bonds [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow bondmems [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow mgmt [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow l2 [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow l3 [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow trunks [all] [--mac | -m ] [--oneline | -1  | --json | -j | -l | --legend ]
        netshow (--version | -V)
     
    Help:
        * default is to show intefaces only in the UP state.
        counters                  summary of physical port counters.
        interface                 summary info of all interfaces
        access                    summary of physical ports with l2 or l3 config
        bonds                     summary of bonds
        bondmems                  summary of bond members
        bridges                   summary of ports with bridge members
        mgmt                      summary of mgmt ports
        l3                        summary of ports with an IP.
        l2                        summary of access, trunk and bridge interfaces
        phy                       summary of physical ports  
        trunks                    summary of trunk interfaces
        lldp                      physical device neighbor information
        interface <iface>         list summary of a single interface
        system                    system information
     
    Options:
        all        show all ports include those are down or admin down
        --mac      show inteface MAC in output
        --version  netshow software version
        --oneline  output each entry on one line
        -1         alias for --oneline
        --json     print output in json
        -l         alias for --legend
        --legend   print legend key explaining abbreviations

A Linux administrator can quickly see the few options available with the
tool. One core tenet of `netshow` is for it to have a small number of
command options. `netshow` is not designed to solve your network
problem, but to help answer this simple question: "What is the basic
network setup of my Linux device?" By helping to answer that question, a
Linux administrator can spend more time troubleshooting the specific
network problem instead of spending most of their time understanding the
basic network state.

Originally developed for Cumulus Linux, `netshow` works on Debian-based
servers and switches and Red Hat-based Linux systems.

`netshow` is designed by network operators, which has rarely occurred in
the networking industry, where most command troubleshooting tools are
designed by developers and are most useful in the network application
development process.

## <span>Showing Interfaces</span>

To show all available interfaces that are physically UP, run `netshow
interface`:

    cumulus@switch:~$ netshow interface
    --------------------------------------------------------------------
    To view the legend,  rerun "netshow" cmd with the  "--legend" option
    --------------------------------------------------------------------
        Name    Speed      MTU  Mode    Summary
    --  ------  -------  -----  ------  -------------------------
    UP  eth0    1G        1500  Mgmt    IP: 192.168.0.12/24(DHCP)
    UP  lo      N/A      16436  Mgmt    IP: 127.0.0.1/8, ::1/128

Whereas `netshow interface all` displays every interface regardless of
state:

    cumulus@switch:~$ netshow interface all
           Name     Speed        Mtu  Mode      Summary
    -----  -------  ---------  -----  --------  --------------------------
    UP     lo       N/A        16436  Loopback  IP: 127.0.0.1/8, ::1/128
    UP     eth0     1G          1500  Mgmt      IP: 192.168.0.11/24 (DHCP)
    ADMDN  swp1s0   10G(4x10)   1500  Unknwn
    ADMDN  swp1s1   10G(4x10)   1500  Unknwn
    ADMDN  swp1s2   10G(4x10)   1500  Unknwn
    ADMDN  swp1s3   10G(4x10)   1500  Unknwn
    ADMDN  swp2     40G(QSFP)   1500  Unknwn
    ADMDN  swp3     40G(QSFP)   1500  Unknwn
    ADMDN  swp4     40G(QSFP)   1500  Unknwn
    ADMDN  swp5     40G(QSFP)   1500  Unknwn
    ADMDN  swp6     40G(QSFP)   1500  Unknwn
    ADMDN  swp7     40G(QSFP)   1500  Unknwn
    ADMDN  swp8     40G(QSFP)   1500  Unknwn
    ADMDN  swp9     40G(QSFP)   1500  Unknwn
    ADMDN  swp10    40G(QSFP)   1500  Unknwn
    ADMDN  swp11    40G(QSFP)   1500  Unknwn
    ADMDN  swp12    40G(QSFP)   1500  Unknwn
    ADMDN  swp13    40G(QSFP)   1500  Unknwn
    ADMDN  swp14    40G(QSFP)   1500  Unknwn
    ADMDN  swp15    40G(QSFP)   1500  Unknwn
    ADMDN  swp16    40G(QSFP)   1500  Unknwn
    ADMDN  swp17    40G(QSFP)   1500  Unknwn
    ADMDN  swp18    40G(QSFP)   1500  Unknwn
    ADMDN  swp19    40G(QSFP)   1500  Unknwn
    ADMDN  swp20    40G(QSFP)   1500  Unknwn
    ADMDN  swp21    40G(QSFP)   1500  Unknwn
    ADMDN  swp22    40G(QSFP)   1500  Unknwn
    ADMDN  swp23    40G(QSFP)   1500  Unknwn
    ADMDN  swp24    40G(QSFP)   1500  Unknwn
    ADMDN  swp25    40G(QSFP)   1500  Unknwn
    ADMDN  swp26    40G(QSFP)   1500  Unknwn
    ADMDN  swp27    40G(QSFP)   1500  Unknwn
    ADMDN  swp28    40G(QSFP)   1500  Unknwn
    ADMDN  swp29    40G(QSFP)   1500  Unknwn
    ADMDN  swp30    40G(QSFP)   1500  Unknwn
    ADMDN  swp31    40G(QSFP)   1500  Unknwn
    ADMDN  swp32s0  10G(4x10)   1500  Unknwn
    ADMDN  swp32s1  10G(4x10)   1500  Unknwn
    ADMDN  swp32s2  10G(4x10)   1500  Unknwn
    ADMDN  swp32s3  10G(4x10)   1500  Unknwn

You can get information about the switch itself by running `netshow
system`:

    cumulus@switch:~$ netshow system
     
    Dell S6000-ON
    Cumulus Version 3.0.0~1462473422.02602ac
    Build: Cumulus Linux 3.0.0~1462473422.02602ac
     
    Chipset: Broadcom Trident2 BCM56850
     
    Port Config: 32 x 40G-QSFP+
     
    CPU: (x86_64) Intel Atom S1220 1.60GHz
     
    Uptime: 3 days, 6:29:44

## <span>Troubleshooting Example: OpenStack</span>

Looking at an OpenStack Environment, here is the physical diagram:

{{% imgOld 0 %}}

For server2, `netshow` can help us see the OpenStack network
configuration. The `netshow` output below shows an summary of a
Kilo-based OpenStack server running 3 tenants.

    [root@host ~]# netshow int
    --------------------------------------------------------------------
    To view the legend,  rerun "netshow" cmd with the  "--legend" option
    --------------------------------------------------------------------
        Name            Speed    MTU    Mode            Summary
    --  --------------  -------  -----  --------------  ---------------------------------------------------------------------
    UP  brq0b6f10c7-42  N/A      1500   Bridge/L2       802.1q Tag: 141
                                                        STP: Disabled
                                                        Untagged Members: tap079cf993-c7
                                                        Tagged Members: eth1.141
    UP  brq8cdc0589-9b  N/A      1500   Bridge/L2       802.1q Tag: 155
                                                        STP: Disabled
                                                        Untagged Members: tap5353b20a-68
                                                        Tagged Members: eth1.155
    UP  brq8ff99102-29  N/A      1500   Bridge/L2       802.1q Tag: 168
                                                        STP: Disabled
                                                        Untagged Members: tapfc2203e4-5b
                                                        Tagged Members: eth1.168
    UP  eth0            N/A      1500   Interface/L3    IP: 192.168.0.105/24
    UP  eth1            N/A      1500   IntTypeUnknown
    UP  eth1            N/A      1500   Trunk/L2        Bridge Membership:
                                                        Tagged: brq0b6f10c7-42(141), brq8cdc0589-9b(155), brq8ff99102-29(168)
    UP  lo              N/A      65536  Loopback        IP: 127.0.0.1/8, ::1/128
    UP  tap079cf993-c7  10M      1500   Access/L2       Untagged: brq0b6f10c7-42
    UP  tap5353b20a-68  10M      1500   Access/L2       Untagged: brq8cdc0589-9b
    UP  tapfc2203e4-5b  10M      1500   Access/L2       Untagged: brq8ff99102-29

OpenStack interface numbering is not the easiest read, but here
`netshow` can quickly show you:

  - A list of all the interfaces in admin UP state and carrier UP state

  - 3 bridges

  - That STP is disabled for all the bridges

  - An uplink trunk interface with 3 VLANs configured on it

  - Many tap interfaces, most likely the virtual machines

This output took about 5 seconds to get and another 1 minute to analyze.
To get this same level of understanding using traditional tools such as:

  - ip link show

  - brctl show

  - ip addr show

... could take about 10 minutes. This is a significant improvement in
productivity\!

`netshow` uses a plugin architecture and can be easily expanded. An
OpenStack interface discovery module is currently in development. If
`netshow` is run on a hypervisor with OpenStack Keystone login
environment variables like `OS_TENANT_NAME`, `netshow` should show the
above output with a better interface discovery state, where `netshow`
collects from OpenStack information from `libvirt`, `nova` and `neutron`
to overlay the virtual machine and tenant subnet information over the
interface kernel state information.

Interface discovery is one of the most powerful features of `netshow`.
The ability to expand its interface discovery capabilities further
simplifies understanding basic network troubleshooting, making the Linux
administrator more productive and improving time to resolution while
investigating network problems.

## <span>Other Useful netshow Features</span>

`netshow` uses the [python
network-docopt](https://pypi.python.org/pypi/network-docopt) package.
This is inspired by [docopt](https://github.com/docopt/docopt) and
provides the ability to specify partial commands, without tab completion
and running the complete option. For example:

`netshow int` runs `netshow interface`  
`netshow sys` runs `netshow system`

`netshow` will eventually support interface name autocompletion. In the
near future, if you run `netshow int tap123` and there is only one
interface starting with `tap123`, `netshow` will autocomplete the
command option with the full interface.

## <span>Contributions Welcome\!</span>

`netshow` is an open source project licensed under GPLv2. To contribute
please contact Cumulus Networks through the [Cumulus Community
Forum](https://community.cumulusnetworks.com/cumulus) or the [Netshow
Linux Provider Github Repository
Home](https://github.com/CumulusNetworks/netshow-linux-lib/). You can
find developer documentation at
[netshow.readthedocs.org](http://netshow.readthedocs.org/). The
documentation is still under development.
