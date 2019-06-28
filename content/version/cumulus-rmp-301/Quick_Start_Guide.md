---
title: Quick Start Guide
author: Cumulus Networks
weight: 13
aliases:
 - /display/RMP30/Quick+Start+Guide
 - /pages/viewpage.action?pageId=5118670
pageID: 5118670
product: Cumulus RMP
version: 3.0.1
imgData: cumulus-rmp-301
siteSlug: cumulus-rmp-301
---
This chapter helps you get up and running with Cumulus RMP quickly and
easily.

## <span>What's New in Cumulus RMP 3.0.1</span>

Cumulus RMP 3.0.1 contains bug fixes only. The [release
not](https://support.cumulusnetworks.com/hc/en-us/articles/222871348-Cumulus-RMP-3-0-1-Release-Notes)[release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/222871348)[es](https://support.cumulusnetworks.com/hc/en-us/articles/222871348-Cumulus-RMP-3-0-1-Release-Notes)
contain information about the new features and known issues in this
release.

## <span>Open Source Contributions</span>

Cumulus Networks has forked various software projects, like CFEngine,
Netdev and some Puppet Labs packages in order to implement various
Cumulus RMP features. The forked code resides in the Cumulus Networks
[GitHub repository](https://github.com/CumulusNetworks).

Cumulus Networks developed and released as open source some new
applications as well.

The list of open source projects is on the [open source
software](http://oss.cumulusnetworks.com) page.

## <span>Prerequisites</span>

Prior intermediate Linux knowledge is assumed for this guide. You should
be familiar with basic text editing, Unix file permissions, and process
monitoring. A variety of text editors are pre-installed, including `vi`
and `nano`.

You must have access to a Linux or UNIX shell. If you are running
Windows, you should use a Linux environment like
[Cygwin](http://www.cygwin.com) as your command line tool for
interacting with Cumulus RMP.

{{%notice tip%}}

If you're a networking engineer but are unfamiliar with Linux concepts,
use [this reference
guide](https://support.cumulusnetworks.com/hc/en-us/articles/201787636)
to see examples of the Cumulus RMP CLI and configuration options, and
their equivalent Cisco Nexus 3000 NX-OS commands and settings for
comparison. You can also [watch a series of short
videos](http://cumulusnetworks.com/technical-videos/) introducing you to
Linux in general and some Cumulus Linux-specific concepts in particular.

{{%/notice%}}

## <span>Supported Hardware</span>

You can find the most up to date list of supported switches
[here](http://cumulusnetworks.com/rmp/how-to-buy/). Use this page to
confirm that your switch model is supported by Cumulus Networks. The
page is updated regularly, listing products by port configuration,
manufacturer, and SKU part number.

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

If you already have Cumulus RMP installed on your switch and are
upgrading to a maintenance release (X.Y.Z, like 2.5.7) from an earlier
release in the same major and minor release family **only** (like 2.5.4
to 2.5.7), you can use various methods, including `apt-get,` to upgrade
to the new version instead. See [Upgrading Cumulus
RMP](/version/cumulus-rmp-301/System_Management/Installation_Upgrading_and_Package_Management/Managing_Cumulus_RMP_Disk_Images)
for details.

## <span>Configuring Cumulus RMP</span>

When bringing up Cumulus RMP for the first time, the management port
makes a DHCPv4 request. To determine the IP address of the switch, you
can cross reference the MAC address of the switch with your DHCP server.
The MAC address should be located on the side of the switch or on the
box in which the unit was shipped.

### <span>Login Credentials</span>

The default installation includes one system account, *root*, with full
system privileges, and one user account, *cumulus*, with sudo
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

All accounts except root are permitted remote SSH login; sudo may be
used to grant a non-root account root-level access. Commands which
change the system configuration require this elevated level of access.

For more information about sudo, read [Using sudo to Delegate
Privileges](/version/cumulus-rmp-301/System_Management/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges).

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
IP address in the
[/etc/network/interfaces](http://manpages.debian.net/man/5/interfaces)
file:

    auto eth0
    iface eth0
        address 192.0.2.42/24
        gateway 192.0.2.1

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

To change the hostname, modify the ` /etc/hostname  `and `/etc/hosts`
files with the desired hostname and reboot the switch. First, edit
`/etc/hostname`:

    cumulus@switch:~$ sudo vi /etc/hostname

Then replace the 127.0.1.1 IP address in `/etc/hosts` with the new
hostname:

    cumulus@switch:~$ sudo vi /etc/hosts

Reboot the switch:

    cumulus@switch:~$ sudo reboot

To update the time zone, update the `/etc/timezone` file with the
[correct
timezone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones),
run `dpkg-reconfigure --frontend noninteractive tzdata`, then reboot the
switch:

    cumulus@switch:~$ sudo vi /etc/timezone
    cumulus@switch:~$ sudo dpkg-reconfigure --frontend noninteractive tzdata
    cumulus@switch:~$ sudo reboot

{{%notice note%}}

It is possible to change the hostname without a reboot via a script
available on [Cumulus Networks GitHub
site](https://github.com/CumulusNetworks/customer-scripts/blob/master/change_hostname.sh).

{{%/notice%}}

### <span>Testing Cable Connectivity</span>

By default, all data plane ports and the management interface are
enabled.

To test cable connectivity, administratively enable a port using `ip
link set <interface> up`:

    cumulus@switch:~$ sudo ip link set swp1 up

To view link status, use `ip link show` . The following examples show
the output of a port in "admin down", "down" and "up" mode,
respectively:

    # Administratively Down
    swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 1000
    
    # Administratively Up but Layer 2 protocol is Down
    swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500
    
    # Administratively Up, Layer 2 protocol is Up
    swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500

## <span>Configuring Switch Ports</span>

### <span>Layer 2 Port Configuration</span>

By default, all the front panel ports (swp1 through swp52) are members
of a bridge called *vlan*, as seen in `/etc/network/interfaces` below.
The `glob` keyword is used to put the complete range of ports into the
bridge:

    # The loopback network interface
    auto lo
    iface lo inet loopback
            
    auto eth0
    iface eth0 inet dhcp
    
    auto vlan
    iface vlan
         bridge-vlan-aware yes
         # needs to scale to large port count     
         bridge-ports glob swp1-52
         bridge-stp on
    
    auto vlan.1
    # update with v6 configuration
      iface vlan.1 inet dhcp

If you modify the configuration at all, you need to activate or apply
the configuration to the kernel:

    # First, check for typos:
    cumulus@switch:~$ sudo ifquery -a
    
    # Then activate the change if no errors are found:
    cumulus@switch:~$ sudo ifup -a

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

To configure a front panel port or bridge interface as a Layer 3 port,
edit the `/etc/network/interfaces` file.

In the following configuration example, the front panel port swp1 is
configured a Layer 3 access port:

    auto swp1
    iface swp1
      address 10.1.1.1/30

To add an IP address to a bridge interface, remove the DHCP statement
from the existing interface and include the address under the `iface`
configuration in `/etc/network/interfaces`:

    auto vlan.1
    iface vlan.1
      address 10.2.2.1/24

To activate or apply the configuration to the kernel:

    # First check for typos:
    cumulus@switch:~$ sudo ifquery -a
    
    # Then activate the change if no errors are found:
    cumulus@switch:~$ sudo ifup -a

To view the changes in the kernel use the `ip addr show` command:

    vlan.1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 00:02:00:00:00:28 brd ff:ff:ff:ff:ff:ff
    inet 10.2.2.1/24 scope global br0
    
    swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 44:38:39:00:6e:fe brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.1/30 scope global swp1

## <span>Configuring a Loopback Interface</span>

Cumulus RMP has a loopback preconfigured in `/etc/network/interfaces`.
When the switch boots up, it has a loopback interface, called *lo* ,
which is up and assigned an IP address of 127.0.0.1.

To see the status of the loopback interface (lo), use the `ip addr show
lo` command:

    cumulus@switch:~$ ip addr show lo
    1: lo: <LOOPBACK,UP,LOWER_UP> mtu 16436 qdisc noqueue state UNKNOWN
        link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
        inet 127.0.0.1/8 scope host lo
        inet6 ::1/128 scope host
           valid_lft forever preferred_lft forever

Note that the loopback is up and is assigned an IP address of 127.0.0.1.

To add an IP address to a loopback interface, add it directly under the
`iface lo inet loopback` definition in `/etc/network/interfaces`:

    auto lo
    iface lo inet loopback
        address 10.1.1.1

{{%notice note%}}

If an IP address is configured without a mask, as shown above, the IP
address becomes a /32. So, in the above case, 10.1.1.1 is actually
10.1.1.1/32.

{{%/notice%}}

Multiple loopback addresses can be configured by adding additional
`address` lines:

    auto lo
    iface lo inet loopback
        address 10.1.1.1
        address 172.16.2.1/24
