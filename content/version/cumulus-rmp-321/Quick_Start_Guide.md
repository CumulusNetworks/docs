---
title: Quick Start Guide
author: Cumulus Networks
weight: 11
aliases:
 - /display/RMP321/Quick+Start+Guide
 - /pages/viewpage.action?pageId=5127535
pageID: 5127535
product: Cumulus RMP
version: 3.2.1
imgData: cumulus-rmp-321
siteSlug: cumulus-rmp-321
---
This quick start guide provides an end-to-end setup process for
installing and running Cumulus RMP, as well as a collection of example
commands for getting started once installation is complete.

{{%notice info%}}

**Prerequisites**

Prior intermediate Linux knowledge is assumed for this guide. You should
be familiar with basic text editing, Unix file permissions, and process
monitoring. A variety of text editors are pre-installed, including `vi`
and `nano`.

You must have access to a Linux or UNIX shell. If you are running
Windows, you should use a Linux environment like
[Cygwin](http://www.cygwin.com/) as your command line tool for
interacting with Cumulus RMP.

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

If you're a networking engineer but are unfamiliar with Linux concepts,
refer to [this reference
guide](https://support.cumulusnetworks.com/hc/en-us/articles/201787636)
for examples of the Cumulus Linux CLI and configuration options, and
their equivalent Cisco Nexus 3000 NX-OS commands and settings for
comparison. You can also [watch a series of short
videos](http://cumulusnetworks.com/technical-videos/) introducing you to
Linux in general and some Cumulus Linux-specific concepts in particular.

{{%/notice%}}

{{%/notice%}}

## <span>Setting up a Cumulus RMP Switch</span>

Setting up a Cumulus RMP switch is simple and straightforward. It
involves:

1.  Racking the switch and connecting it to power.

2.  Cabling all the ports.

3.  Logging in and changing the default password.

4.  Configuring switch ports and a loopback interface, if needed.

This quick start guide walks you through the steps necessary for getting
your Cumulus RMP switch up and running after you remove it from the box.

## <span>Upgrading Cumulus RMP</span>

If you are running a Cumulus RMP version earlier than 3.0.0, you must
perform a [complete
install](/version/cumulus-rmp-321/System_Configuration/Installation_Upgrading_and_Package_Management/).
If you already have Cumulus Linux 3.0.0 or later installed on your
switch, read [Upgrading Cumulus
RMP](/version/cumulus-rmp-321/System_Configuration/Installation_Upgrading_and_Package_Management/Managing_Cumulus_RMP_Disk_Images)
for considerations before start the process.

## <span>Getting Started</span>

When bringing up Cumulus RMP for the first time, the management port
makes a DHCPv4 request. To determine the IP address of the switch, you
can cross reference the MAC address of the switch with your DHCP server.
The MAC address should be located on the side of the switch or on the
box in which the unit was shipped.

### <span>Login Credentials</span>

The default installation includes one system account, *root*, with full
system privileges, and one user account, *cumulus*, with `sudo`
privileges. The *root* account password is set to null by default (which
prohibits login), while the *cumulus* account is configured with this
default password:

    CumulusLinux!

In this quick start guide, you will use the *cumulus* account to
configure Cumulus RMP.

{{%notice warning%}}

For best security, you should change the default password (using the
` passwd  `command) before you configure Cumulus RMP on the switch.

{{%/notice%}}

All accounts except `root` are permitted remote SSH login; `sudo` may be
used to grant a non-root account root-level access. Commands which
change the system configuration require this elevated level of access.

For more information about sudo, read [Using sudo to Delegate
Privileges](/version/cumulus-rmp-321/System_Configuration/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges).

### <span>Serial Console Management</span>

Users are encouraged to perform management and configuration over the
network, either in band or out of band. Use of the serial console is
fully supported; however, many customers prefer the convenience of
network-based management.

Typically, switches will ship from the manufacturer with a mating DB9
serial cable. Switches with ONIE are always set to a 115200 baud rate.

### <span>Wired Ethernet Management</span>

Switches supported in Cumulus RMP contain a number of dedicated Ethernet
management ports, the first of which is named *eth0*. These interfaces
are geared specifically for out-of-band management use. The management
interface uses DHCPv4 for addressing by default. While it is generally
recommended to **not** assign an address to eth0, you can set a static
IP address with the Network Command Line Utility
([NCLU](/version/cumulus-rmp-321/System_Configuration/Network_Command_Line_Utility)).

{{%notice info%}}

**Example IP Configuration**

Set the static IP address with the `interface address` and `interface
gateway` NCLU commands:

    cumulus@switch:~$ net add interface eth0 ip address 192.0.2.42/24
    cumulus@switch:~$ net add interface eth0 ip gateway 192.0.2.1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

These commands produce the following snippet in the
[/etc/network/interfaces](http://manpages.debian.net/man/5/interfaces)
file:

    auto eth0
    iface eth0
        address 192.0.2.42/24
        gateway 192.0.2.1

{{%/notice%}}

### <span>In-Band Ethernet Management</span>

All traffic that goes to the RMP switch via an interface called *vlan.1*
is marked for in-band management. DHCP is enabled on this interface by
default, and you can confirm the IP address at the command line.
However, if you want to set a static IP address, change the
configuration for vlan.1 in `/etc/network/interfaces`:

    auto vlan.1
    iface vlan.1
        address 10.0.1.1/24
        gateway 10.0.2.1

### <span>Configuring the Hostname and Time Zone</span>

To change the hostname, run `net add hostname`, which modifies both the
` /etc/hostname  `and `/etc/hosts` files with the desired hostname.

    cumulus@switch:~$ net add hostname <hostname>
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

The command prompt in the terminal doesn't reflect the new hostname
until you either log out of the switch or start a new shell.

{{%/notice%}}

To update the time zone, update the `/etc/timezone` file with the
[correct
timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
run `dpkg-reconfigure --frontend noninteractive tzdata`, then reboot the
switch:

    cumulus@switch:~$ sudo nano /etc/timezone
    cumulus@switch:~$ sudo dpkg-reconfigure --frontend noninteractive tzdata
    cumulus@switch:~$ sudo reboot

### <span>Testing Cable Connectivity</span>

By default, all data plane ports and the management interface are
enabled.

    cumulus@switch:~$ net add interface swp1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To administratively enable all physical ports, run the following
command, where swp1-52 represents a switch with switch ports numbered
from swp1 to swp52:

    cumulus@switch:~$ net add interface swp1-52
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To view link status, use `net show interface all`. The following
examples show the output of ports in "admin down", "down" and "up"
modes:

    cumulus@switch:~$ net show interface all
           Name                      Speed    MTU    Mode           Summary
    -----  ------------------------  -------  -----  -------------  --------------------------------------
    UP     lo                        N/A      65536  Loopback       IP: 10.0.0.11/32, 127.0.0.1/8, ::1/128
    UP     eth0                      1G       1500   Mgmt           IP: 192.168.0.11/24(DHCP)
    UP     swp1 (hypervisor_port_1)  1G       1500   Access/L2      Untagged: br0
    UP     swp2                      1G       1500   NotConfigured
    ADMDN  swp45                     0M       1500   NotConfigured
    ADMDN  swp46                     0M       1500   NotConfigured
    ADMDN  swp47                     0M       1500   NotConfigured
    ADMDN  swp48                     0M       1500   NotConfigured
    ADMDN  swp49                     0M       1500   NotConfigured
    ADMDN  swp50                     0M       1500   NotConfigured
    UP     swp51                     1G       1500   BondMember     Master: bond0(DN)
    UP     blue                      N/A      65536  NotConfigured
    DN     bond0                     N/A      1500   Bond           Bond Members: swp51(UN)
    UP     br0                       N/A      1500   Bridge/L3      IP: 172.16.1.1/24
                                                                    Untagged Members: swp1
                                                                    802.1q Tag: Untagged
                                                                    STP: RootSwitch(32768)
    UP     red                       N/A      65536  NotConfigured
    ADMDN  rename13                  0M       1500   NotConfigured
    ADMDN  vagrant                   0M       1500   NotConfigured

## <span>Configuring Switch Ports</span>

### <span>Layer 2 Port Configuration</span>

Cumulus RMP does not put all ports into a bridge by default. To
configure a front panel port or create a bridge, edit the
`/etc/network/interfaces` file. After saving the file, to activate the
change, use the `ifup` command.

#### <span>Examples</span>

{{%notice info%}}

**Example One**

In the following configuration example, the front panel port swp1 is
placed into a bridge called `bridge`. The NCLU commands are:

    cumulus@switch:~$ net add bridge bridge ports swp1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The commands above produce the following `/etc/network/interfaces`
snippet:

    auto bridge
    iface bridge
        bridge-ports swp1
        bridge-vlan-aware yes

{{%/notice%}}

{{%notice info%}}

**Example Two**

A range of ports can be added in one command. For example, add swp1
through swp10, swp12, and swp14 through swp20 to bridge:

    cumulus@switch:~$ net add bridge bridge ports swp1-10,12,14-20
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This creates the following `/etc/network/interfaces` snippet:

    auto bridge
    iface bridge
        bridge-ports swp1 swp2 swp3 swp4 swp5 swp6 swp7 swp8 swp9 swp10 swp12 swp14 swp15 swp16 swp17 swp18 swp19 swp20
        bridge-vlan-aware yes

{{%/notice%}}

To view the changes in the kernel, use the `brctl` command:

    cumulus@switch:~$ brctl show
    bridge name     bridge id              STP enabled     interfaces
    br0             8000.089e01cedcc2       yes              swp1

{{%notice note%}}

A script is available to generate a configuration that [places all
physical ports in a single
bridge](https://support.cumulusnetworks.com/hc/en-us/articles/203508477).

{{%/notice%}}

### <span>Layer 3 Port Configuration</span>

To configure a front panel port or bridge interface as a layer 3 port,
use
[NCLU](/version/cumulus-rmp-321/System_Configuration/Network_Command_Line_Utility).

In the following configuration example, the front panel port swp1 is
configured as a layer 3 access port:

    cumulus@switch:~$ net add interface swp1 ip address 10.1.1.1/30
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This creates the following `/etc/network/interfaces` snippet:

    auto swp1
    iface swp1
      address 10.1.1.1/30

To add an IP address to a bridge interface, it must be put into a VLAN
interface:

    cumulus@switch:~$ net add vlan ip address 10.2.2.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This creates the following `/etc/network/interfaces snippet`:

    auto bridge
    iface bridge
        bridge-vids 100
        bridge-vlan-aware yes
     
    auto vlan100
    iface vlan100
        address 192.168.10.1/24
        vlan-id 100
        vlan-raw-device bridge

To view the changes in the kernel use the `ip addr show` command:

    cumulus@switch:~$ ip addr show
    ...
     
    4. swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bridge state UP group default qlen 1000
        link/ether 44:38:39:00:6e:fe brd ff:ff:ff:ff:ff:ff
    ...
      
    14: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
        link/ether 44:38:39:00:00:04 brd ff:ff:ff:ff:ff:ff
        inet6 fe80::4638:39ff:fe00:4/64 scope link
           valid_lft forever preferred_lft forever
    ...

## <span>Configuring a Loopback Interface</span>

Cumulus RMP has a loopback preconfigured in `/etc/network/interfaces`.
When the switch boots up, it has a loopback interface, called *lo*,
which is up and assigned an IP address of 127.0.0.1.

{{%notice tip%}}

The loopback interface *lo* must always be specified in
`/etc/network/interfaces` and must always be up.

{{%/notice%}}

To see the status of the loopback interface (lo), use the `net show
interface lo` command:

    cumulus@switch:~$ net show interface lo
     
        Name    MAC                Speed      MTU  Mode
    --  ------  -----------------  -------  -----  --------
    UP  lo      00:00:00:00:00:00  N/A      65536  Loopback
     
    IP Details
    -------------------------  --------------------
    IP:                        127.0.0.1/8, ::1/128
    IP Neighbor(ARP) Entries:  0

Note that the loopback is up and is assigned an IP address of 127.0.0.1.

To add an IP address to a loopback interface, configure the lo interface
with NCLU:

    cumulus@switch:~$ net add loopback lo ip address 10.1.1.1/32
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

Multiple loopback addresses can be configured by adding additional
`address` lines:

    cumulus@switch:~$ net add loopback lo ip address 172.16.2.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

This creates the following snippet in `/etc/network/interfaces`:

    auto lo
    iface lo inet loopback
        address 10.1.1.1/32
        address 172.16.2.1/24
