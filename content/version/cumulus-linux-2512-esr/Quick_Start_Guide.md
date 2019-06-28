---
title: Quick Start Guide
author: Cumulus Networks
weight: 11
aliases:
 - /display/CL25ESR/Quick+Start+Guide
 - /pages/viewpage.action?pageId=5115897
pageID: 5115897
product: Cumulus Linux
version: 2.5.12 ESR
imgData: cumulus-linux-2512-esr
siteSlug: cumulus-linux-2512-esr
---
This chapter helps you get up and running with Cumulus Linux quickly and
easily.

## <span>What's New in Cumulus Linux 2.5.12</span>

Cumulus Linux 2.5.12 is part of Cumulus Linux 2.5 ESR and as such,
contains bug fixes only. The [release
notes](https://support.cumulusnetworks.com/hc/en-us/articles/115001896847)
contain information about the release as well as the fixed and known
issues.

## <span>Open Source Contributions</span>

Cumulus Networks has forked various software projects, like CFEngine,
Netdev and some Puppet Labs packages in order to implement various
Cumulus Linux features. The forked code resides in the Cumulus Networks
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
interacting with Cumulus Linux.

{{%notice tip%}}

If you're a networking engineer but are unfamiliar with Linux concepts,
use [this reference
guide](https://support.cumulusnetworks.com/hc/en-us/articles/201787636)
to see examples of the Cumulus Linux CLI and configuration options, and
their equivalent Cisco Nexus 3000 NX-OS commands and settings for
comparison. You can also [watch a series of short
videos](http://cumulusnetworks.com/technical-videos/) introducing you to
Linux in general and some Cumulus Linux-specific concepts in particular.

{{%/notice%}}

## <span>Hardware Compatibility List</span>

You can find the most up to date hardware compatibility list (HCL)
[here](http://cumulusnetworks.com/hcl/). Use the HCL to confirm that
your switch model is supported by Cumulus Networks. The HCL is updated
regularly, listing products by port configuration, manufacturer, and SKU
part number.

<span id="src-5115897_QuickStartGuide-install"></span>

## <span>Installing Cumulus Linux</span>

This quick start guide walks you through the steps necessary for getting
Cumulus Linux up and running on your switch, which includes:

1.  Powering on the switch and entering ONIE, the Open Network Install
    Environment.

2.  Installing Cumulus Linux on the switch via ONIE.

3.  Booting into Cumulus Linux and installing the license.

4.  Rebooting the switch to activate the switch ports.

5.  Configuring switch ports and a loopback interface.

To install Cumulus Linux, you use
[ONIE](https://github.com/opencomputeproject/onie) (Open Network Install
Environment), an extension to the traditional U-Boot software that
allows for automatic discovery of a network installer image. This
facilitates the ecosystem model of procuring switches, with a user's own
choice of operating system loaded, such as Cumulus Linux.

{{%notice note%}}

If Cumulus Linux is already installed on your switch, and you need to
upgrade the software only, you can skip to [Upgrading Cumulus
Linux](#src-5115897_QuickStartGuide-upgrading-cumulus-linux) below.

{{%/notice%}}

The easiest way to install Cumulus Linux with ONIE is via local HTTP
discovery:

1.  If your host (like a laptop or server) is IPv6-enabled, make sure it
    is running a Web server.
    
    If the host is IPv4-enabled, make sure it is running DHCP as well as
    a Web server.

2.  [Download](http://cumulusnetworks.com/downloads/) the Cumulus Linux
    installation file to the root directory of the Web server. Rename
    this file `onie-installer`.

3.  Connect your host via Ethernet cable to the management Ethernet port
    of the switch.

4.  Power on the switch. The switch downloads the ONIE image installer
    and boots it. You can watch the progress of the install in your
    terminal. After the installation finishes, the Cumulus Linux login
    prompt appears in the terminal window.

{{%notice note%}}

These steps describe a flexible unattended installation method. You
should not need a console cable. A fresh install via ONIE using a local
Web server should generally complete in less than 10 minutes.

You have more options for installing Cumulus Linux with ONIE. Read
[Installing a New Cumulus Linux
Image](/version/cumulus-linux-2512-esr/Installation_Upgrading_and_Package_Management/Managing_Cumulus_Linux_Disk_Images/Installing_a_New_Cumulus_Linux_Image)
to install Cumulus Linux using ONIE in the following ways:

  - DHCP/Web server with and without DHCP options

  - Web server without DHCP

  - FTP or TFTP without a Web server

  - Local file

  - USB

{{%/notice%}}

ONIE supports many other discovery mechanisms using USB (copy the
installer to the root of the drive), DHCPv6 and DHCPv4, and image copy
methods including HTTP, FTP, and TFTP. For more information on these
discovery methods, refer to the [ONIE
documentation](https://opencomputeproject.github.io/onie/design-spec/discovery.html#installer-discovery-method).

After installing Cumulus Linux, you are ready to:

  - Log in to Cumulus Linux on the switch.

  - Install the Cumulus Linux license.

  - Configure Cumulus Linux. This quick start guide provides
    instructions on configuring switch ports and a loopback interface.

## <span id="src-5115897_QuickStartGuide-upgrading-cumulus-linux" class="confluence-anchor-link"></span><span>Upgrading Cumulus Linux</span>

If you already have Cumulus Linux installed on your switch and are
upgrading to a maintenance release (X.Y.Z, like 2.5.1) from an earlier
release in the same major and minor release family **only** (like 2.2.1
to 2.2.2, or 2.5.0 to 2.5.1), you can use various methods, including
`apt-get,` to upgrade to the new version instead. See [Upgrading Cumulus
Linux](Managing_Cumulus_Linux_Disk_Images.html#src-5115988_ManagingCumulusLinuxDiskImages-upgrade)
for details.

## <span>Configuring Cumulus Linux</span>

When bringing up Cumulus Linux for the first time, the management port
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
configure Cumulus Linux.

{{%notice warning%}}

For best security, you should change the default password (using the
` passwd  `command) before you configure Cumulus Linux on the switch.

{{%/notice%}}

All accounts except root are permitted remote SSH login; sudo may be
used to grant a non-root account root-level access. Commands which
change the system configuration require this elevated level of access.

For more information about sudo, read [Using sudo to Delegate
Privileges](/version/cumulus-linux-2512-esr/System_Management/Authentication_Authorization_and_Accounting/Using_sudo_to_Delegate_Privileges).

### <span>Serial Console Management</span>

Users are encouraged to perform management and configuration over the
network, either in band or out of band. Use of the serial console is
fully supported; however, many customers prefer the convenience of
network-based management.

Typically, switches will ship from the manufacturer with a mating DB9
serial cable. Switches with ONIE are always set to a 115200 baud rate.

### <span>Wired Ethernet Management</span>

Switches supported in Cumulus Linux always contain at least one
dedicated Ethernet management port, which is named eth0. This interface
is geared specifically for out-of-band management use. The management
interface uses DHCPv4 for addressing by default. You can set a static IP
address in the
[/etc/network/interfaces](http://manpages.debian.net/man/5/interfaces)
file:

    auto eth0
    iface eth0
        address 192.0.2.42/24
        gateway 192.0.2.1

### <span>Configuring the Hostname and Time Zone</span>

To change the hostname, modify the `/etc/hostname` and `/etc/hosts`
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

### <span>Installing the License</span>

Cumulus Linux is licensed on a per-instance basis. Each network system
is fully operational, enabling any capability to be utilized on the
switch with the exception of forwarding on switch panel ports. Only eth0
and console ports are activated on an unlicensed instance of Cumulus
Linux. Enabling front panel ports requires a license.

You should have received a license key from Cumulus Networks or an
authorized reseller. Here is a sample license key:

    user@company.com|thequickbrownfoxjumpsoverthelazydog312

There are three ways to install the license onto the switch:

  - Copy it from a local server. Create a text file with the license and
    copy it to a server accessible from the switch. On the switch, use
    the following command to transfer the file directly on the switch,
    then install the license file:
    
        cumulus@switch:~$ scp user@my_server:/home/user/my_license_file.txt .
        cumulus@switch:~$ sudo cl-license -i my_license_file.txt

  - Copy the file to an HTTP server (not HTTPS), then reference the URL
    when you run `cl-license`:
    
        cumulus@switch:~$ sudo cl-license -i <URL>

  - Copy and paste the license key into the `cl-license` command:
    
        cumulus@switch:~$ sudo cl-license -i
        <paste license key>
        ^+d

Once the license is installed successfully, reboot the system:

    cumulus@switch:~$ sudo reboot

After the switch reboots, all front panel ports will be active. The
front panel ports are identified as switch ports, and show up as swp1,
swp2, and so forth.

## <span>Configuring 4x10G Port Configuration (Splitter Cables)</span>

If you are using 4x10G DAC or AOC cables, edit the
`/etc/cumulus/ports.conf` to enable support for these cables then
[restart the `switchd`
service](Configuring_switchd.html#src-5115907_Configuringswitchd-restartswitchd)
using the `sudo service switchd restart` command. For more details, see
[Layer 1 and Switch Port
Attributes](/version/cumulus-linux-2512-esr/Configuring_and_Managing_Network_Interfaces/Layer_1_and_Switch_Port_Attributes).

## <span>Testing Cable Connectivity</span>

By default, all data plane ports (every Ethernet port except the
management interface, eth0) are disabled.

To test cable connectivity, administratively enable a port using `ip
link set <interface> up`:

    cumulus@switch:~$ sudo ip link set swp1 up

Run the following bash script, as root, to administratively enable all
physical ports:

    cumulus@switch:~$ sudo su -
    cumulus@switch:~$ for i in /sys/class/net/*; do iface=`basename $i`; if [[ $iface == swp* ]]; then ip link set $iface up; fi done

To view link status, use `ip link show`. The following examples show the
output of a port in "admin down", "down" and "up" mode, respectively:

    # Administratively Down
    swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 1000
    
    # Administratively Up but Layer 2 protocol is Down
    swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500
    
    # Administratively Up, Layer 2 protocol is Up
    swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500

## <span>Configuring Switch Ports</span>

### <span>Layer 2 Port Configuration</span>

Cumulus Linux does not put all ports into a bridge by default. To
configure a front panel port or create a bridge, edit the
`/etc/network/interfaces` file. After saving the file, to activate the
change, use the `ifup` command.

#### <span>Examples</span>

In the following configuration example, the front panel port swp1 is
placed into a bridge called br0:

    auto br0
    iface br0
      bridge-ports swp1
      bridge-stp on

To put a range of ports into a bridge, use the `glob` keyword. For
example, add swp1 through swp10, swp12, and swp14 through swp20 to br0:

    auto br0
    iface br0
      bridge-ports glob swp1-10 swp12 glob swp14-20
      bridge-stp on

To activate or apply the configuration to the kernel:

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

To add an IP address to a bridge interface, include the address under
the `iface` configuration in `/etc/network/interfaces`:

    auto br0
    iface br0
      address 10.2.2.1/24
      bridge-ports glob swp1-10 swp12 glob swp14-20
      bridge-stp on

To activate or apply the configuration to the kernel:

    # First check for typos:
    cumulus@switch:~$ sudo ifquery -a
    
    # Then activate the change if no errors are found:
    cumulus@switch:~$ sudo ifup -a

To view the changes in the kernel use the `ip addr show` command:

    br0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 00:02:00:00:00:28 brd ff:ff:ff:ff:ff:ff
    inet 10.2.2.1/24 scope global br0
    
    swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP
    link/ether 44:38:39:00:6e:fe brd ff:ff:ff:ff:ff:ff
    inet 10.1.1.1/30 scope global swp1

## <span>Configuring a Loopback Interface</span>

Cumulus Linux has a loopback preconfigured in `/etc/network/interfaces`.
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
