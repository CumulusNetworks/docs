---
title: Quick Start Guide
author: Cumulus Networks
weight: 11
aliases:
 - /display/CL36/Quick+Start+Guide
 - /pages/viewpage.action?pageId=8362037
pageID: 8362037
product: Cumulus Linux
version: '3.6'
imgData: cumulus-linux-36
siteSlug: cumulus-linux-36
---
This quick start guide provides an end-to-end setup process for
installing and running Cumulus Linux, as well as a collection of example
commands for getting started after installation is complete.

{{%notice info%}}

**Prerequisites**

Intermediate-level Linux knowledge is assumed for this guide. You should
be familiar with basic text editing, Unix file permissions, and process
monitoring. A variety of text editors are pre-installed, including `vi`
and `nano`.

You must have access to a Linux or UNIX shell. If you are running
Windows, use a Linux environment like [Cygwin](http://www.cygwin.com/)
as your command line tool for interacting with Cumulus Linux.

<span class="admonition-icon confluence-information-macro-icon"></span>

{{%notice info%}}

If you are a networking engineer but are unfamiliar with Linux concepts,
refer to [this reference
guide](https://support.cumulusnetworks.com/hc/en-us/articles/201787636)
to compare the Cumulus Linux CLI and configuration options, and their
equivalent Cisco Nexus 3000 NX-OS commands and settings. You can also
[watch a series of short
videos](http://cumulusnetworks.com/technical-videos/) introducing you to
Linux and Cumulus Linux-specific concepts.

{{%/notice%}}

{{%/notice%}}

### <span>Installation</span>

To install Cumulus Linux, you use
[ONIE](https://github.com/opencomputeproject/onie/wiki) (Open Network
Install Environment), an extension to the traditional U-Boot software
that allows for automatic discovery of a network installer image. This
facilitates the ecosystem model of procuring switches, with a user's own
choice of operating system loaded, such as Cumulus Linux.

{{%notice note%}}

If Cumulus Linux 3.0.0 or later is already installed on your switch and
you need to upgrade the software only, you can skip to [Upgrading
Cumulus Linux](#src-8362037_QuickStartGuide-upgrading-cumulus-linux)
below.

{{%/notice%}}

The easiest way to install Cumulus Linux with ONIE is with local HTTP
discovery:

1.  If your host (like a laptop or server) is IPv6-enabled, make sure it
    is running a web server. If the host is IPv4-enabled, make sure it
    is running DHCP as well as a web server.

2.  [Download](http://cumulusnetworks.com/downloads/) the Cumulus Linux
    installation file to the root directory of the web server. Rename
    this file `onie-installer`.

3.  Connect your host using an Ethernet cable to the management Ethernet
    port of the switch.

4.  Power on the switch. The switch downloads the ONIE image installer
    and boots. You can watch the progress of the install in your
    terminal. After the installation completes, the Cumulus Linux login
    prompt appears in the terminal window.

{{%notice note%}}

These steps describe a flexible unattended installation method. You do
not need a console cable. A fresh install with ONIE using a local web
server typically completes in less than ten minutes.

You have more options for installing Cumulus Linux with ONIE. Read
[Installing a New Cumulus Linux
Image](/version/cumulus-linux-36/Installation_Management/Installing_a_New_Cumulus_Linux_Image)
to install Cumulus Linux using ONIE in the following ways:

  - DHCP/web server with and without DHCP options

  - Web server without DHCP

  - FTP or TFTP without a web server

  - Local file

  - USB

{{%/notice%}}

ONIE supports many other discovery mechanisms using USB (copy the
installer to the root of the drive), DHCPv6 and DHCPv4, and image copy
methods including HTTP, FTP, and TFTP. For more information on these
discovery methods, refer to the [ONIE
documentation](https://github.com/opencomputeproject/onie/wiki/Design-Spec-SW-Image-Discovery).

After installing Cumulus Linux, you are ready to:

  - Log in to Cumulus Linux on the switch.

  - Install the Cumulus Linux license.

  - Configure Cumulus Linux. This quick start guide provides
    instructions on configuring switch ports and a loopback interface.

#### <span id="src-8362037_QuickStartGuide-upgrading-cumulus-linux" class="confluence-anchor-link"></span><span>Upgrade to the Latest Version</span>

If you are running a Cumulus Linux version earlier than 3.0.0, you must
perform a complete install, as [described
above](#src-8362037_QuickStartGuide-install). If you already have
Cumulus Linux 3.0.0 or later installed on your switch, read [Upgrading
Cumulus
Linux](Managing_Cumulus_Linux_Disk_Images.html#src-8362129_ManagingCumulusLinuxDiskImages-upgrade)
for considerations before starting the process.

### <span>Getting Started</span>

When starting Cumulus Linux for the first time, the management port
makes a DHCPv4 request. To determine the IP address of the switch, you
can cross reference the MAC address of the switch with your DHCP server.
The MAC address is typically located on the side of the switch or on the
box in which the unit ships.

#### <span>Login Credentials</span>

The default installation includes one system account, *root*, with full
system privileges, and one user account, *cumulus*, with `sudo`
privileges. The *root* account password is set to null by default (which
prohibits login), while the *cumulus* account is configured with this
default password:

    CumulusLinux!

In this quick start guide, you use the *cumulus* account to configure
Cumulus Linux.

{{%notice warning%}}

For optimum security, change the default password (using the `passwd`
command) before you configure Cumulus Linux on the switch.

{{%/notice%}}

All accounts except `root` are permitted remote SSH login; you can use
`sudo` to grant a non-root account root-level access. Commands that
change the system configuration require this elevated level of access.

For more information about `sudo`, read [Using sudo to Delegate
Privileges](/version/cumulus-linux-36/System_Configuration/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges).

#### <span>Serial Console Management</span>

You are encouraged to perform management and configuration over the
network, [either in band or out of
band](Upgrading_Cumulus_Linux.html#src-8362142_UpgradingCumulusLinux-outofband).
Use of the serial console is fully supported; however, many customers
prefer the convenience of network-based management.

Typically, switches ship from the manufacturer with a mating DB9 serial
cable. Switches with ONIE are always set to a 115200 baud rate.

#### <span>Wired Ethernet Management</span>

Switches supported in Cumulus Linux always contain at least one
dedicated Ethernet management port, which is named eth0. This interface
is geared specifically for out-of-band management use. The management
interface uses DHCPv4 for addressing by default. You can set a static IP
address with the Network Command Line Utility (NCLU).

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

#### <span>Configuring the Hostname and Timezone</span>

To change the hostname, run `net add hostname`, which modifies both
the`  /etc/hostname  `and `/etc/hosts` files with the desired hostname.

    cumulus@switch:~$ net add hostname <hostname>
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

{{%notice note%}}

The command prompt in the terminal does not reflect the new hostname
until you either log out of the switch or start a new shell.

{{%/notice%}}

{{%notice note%}}

When you use this NCLU command to set the hostname, DHCP **does not**
override the hostname when you reboot the switch. However, if you
disable the hostname setting with NCLU, DHCP **does** override the
hostname the next time you reboot the switch.

{{%/notice%}}

To update the timezone, use the NTP interactive mode:

1.  Run the following command in a terminal:
    
        sudo dpkg-reconfigure tzdata

2.  Follow the on screen menu options to select the geographic area and
    region.

{{%notice note%}}

Programs that are already running (including log files) and users
currently logged in, do not see timezone changes made with interactive
mode. To have the timezone set for all services and daemons, a reboot is
required.

{{%/notice%}}

#### <span>Verifying the System Time</span>

Before you install the license, verify that the date and time on the
switch are correct. You must [correct the date and
time](/version/cumulus-linux-36/System_Configuration/Setting_Date_and_Time)
if they are incorrect. The wrong date and time can have impacts on the
switch, such as the inability to synchronize with Puppet or return
errors like this one after you restart `switchd`:

> Warning: Unit file of switchd.service changed on disk, 'systemctl
> daemon-reload' recommended.

#### <span>Installing the License</span>

Cumulus Linux is licensed on a per-instance basis. Each network system
is fully operational, enabling any capability to be utilized on the
switch with the exception of forwarding on switch panel ports. Only eth0
and console ports are activated on an unlicensed instance of Cumulus
Linux. Enabling front panel ports requires a license.

You receive a license key from Cumulus Networks or an authorized
reseller. Here is a sample license key:

    user@company.com|thequickbrownfoxjumpsoverthelazydog312

There are three ways to install the license onto the switch:

  - Copy the license from a local server. Create a text file with the
    license and copy it to a server accessible from the switch. On the
    switch, use the following command to transfer the file directly on
    the switch, then install the license file:
    
        cumulus@switch:~$ scp user@my_server:/home/user/my_license_file.txt .
        cumulus@switch:~$ sudo cl-license -i my_license_file.txt

  - Copy the file to an HTTP server (not HTTPS), then reference the URL
    when you run `cl-license`:
    
        cumulus@switch:~$ sudo cl-license -i <URL>

  - Copy and paste the license key into the `cl-license` command:
    
        cumulus@switch:~$ sudo cl-license -i
        <paste license key>
        ^+d

{{%notice note%}}

It is not necessary to reboot the switch to activate the switch ports.
After you install the license, restart the `switchd` service. All front
panel ports become active and show up as swp1, swp2, and so on.

    cumulus@switch:~$ sudo systemctl restart switchd.service

{{%/notice%}}

{{%notice note%}}

If a license is not installed on a Cumulus Linux switch, the `switchd`
service does not start. After you install the license, start `switchd`
as described above.

{{%/notice%}}

### <span>Configuring Breakout Ports with Splitter Cables</span>

If you are using 4x10G DAC or AOC cables, or want to break out 100G or
40G switch ports, configure the breakout ports. For more details, see
[Layer 1 and Switch Port
Attributes](Switch_Port_Attributes.html#src-8362492_SwitchPortAttributes-breakout).

### <span>Testing Cable Connectivity</span>

By default, all data plane ports (every Ethernet port except the
management interface, eth0) are disabled.

To test cable connectivity, administratively enable a port:

    cumulus@switch:~$ net add interface swp1
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To administratively enable all physical ports, run the following
command, where swp1-52 represents a switch with switch ports numbered
from swp1 to swp52:

    cumulus@switch:~$ net add interface swp1-52
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

To view link status, use the `net show interface all` command. The
following examples show the output of ports in `admin down`, `down`, and
`up` modes:

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

### <span>Configuring Switch Ports</span>

#### <span>Layer 2 Port Configuration</span>

Cumulus Linux does not put all ports into a bridge by default. To create
a bridge and configure one or more front panel ports as members of the
bridge, use the following examples as guides.

##### <span>Examples</span>

{{%notice info%}}

**Example One**

In the following configuration example, the front panel port swp1 is
placed into a bridge called *bridge*. The NCLU commands are:

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

You can add a range of ports in one command. For example, add swp1
through swp10, swp12, and swp14 through swp20 to bridge:

    cumulus@switch:~$ net add bridge bridge ports swp1-10,12,14-20
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The commands above produce the following snippet in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-ports swp1 swp2 swp3 swp4 swp5 swp6 swp7 swp8 swp9 swp10 swp12 swp14 swp15 swp16 swp17 swp18 swp19 swp20
        bridge-vlan-aware yes

{{%/notice%}}

To view the changes in the kernel, use the `brctl` command:

    cumulus@switch:~$ brctl show
    bridge name     bridge id              STP enabled     interfaces
    bridge          8000.443839000004      yes             swp1
                                                           swp2

#### <span>Layer 3 Port Configuration</span>

You can also use NCLU to configure a front panel port or bridge
interface as a layer 3 port.

In the following configuration example, the front panel port swp1 is
configured as a layer 3 access port:

    cumulus@switch:~$ net add interface swp1 ip address 10.1.1.1/30
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The commands above produce the following snippet in the
`/etc/network/interfaces` file:

    auto swp1
    iface swp1
      address 10.1.1.1/30

To add an IP address to a bridge interface, you must put it into a VLAN
interface:

    cumulus@switch:~$ net add vlan 100 ip address 10.2.2.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The commands above produce the following snippet in the
`/etc/network/interfaces` file:

    auto bridge
    iface bridge
        bridge-vids 100
        bridge-vlan-aware yes
     
    auto vlan100
    iface vlan100
        address 192.168.10.1/24
        vlan-id 100
        vlan-raw-device bridge

To view the changes in the kernel, use the `ip addr show` command:

    cumulus@switch:~$ ip addr show
    ...
     
    4. swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast master bridge state UP group default qlen 1000
        link/ether 44:38:39:00:6e:fe brd ff:ff:ff:ff:ff:ff
     
    ...
     
    14: bridge: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default 
        link/ether 44:38:39:00:00:04 brd ff:ff:ff:ff:ff:ff
        inet6 fe80::4638:39ff:fe00:4/64 scope link 
           valid_lft forever preferred_lft forever
    ...

### <span>Configuring a Loopback Interface</span>

Cumulus Linux has a loopback preconfigured in the
`/etc/network/interfaces` file. When the switch boots up, it has a
loopback interface, called *lo*, which is up and assigned an IP address
of 127.0.0.1.

{{%notice tip%}}

The loopback interface *lo* must always be specified in the
`/etc/network/interfaces` file and must always be up.

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

To add an IP address to a loopback interface, configure the *lo*
interface with NCLU:

    cumulus@switch:~$ net add loopback lo ip address 10.1.1.1/32
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

You can configure multiple loopback addresses by adding additional
`address` lines:

    cumulus@switch:~$ net add loopback lo ip address 172.16.2.1/24
    cumulus@switch:~$ net pending
    cumulus@switch:~$ net commit

The commands above produce the following snippet in the
`/etc/network/interfaces` file:

    auto lo
    iface lo inet loopback
        address 10.1.1.1/32
        address 172.16.2.1/24
