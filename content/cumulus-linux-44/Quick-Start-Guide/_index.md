---
title: Quick Start Guide
author: NVIDIA
weight: 10
toc: 2
---

This quick start guide provides an end-to-end setup process for installing and running Cumulus Linux.

## Prerequisites

This guide assumes you have intermediate-level Linux knowledge. You need to be familiar with basic text editing, Unix file permissions, and process monitoring. A variety of text editors are pre-installed, including `vi` and `nano`.

You must have access to a Linux or UNIX shell. If you are running Windows, use a Linux environment like {{<exlink url="http://www.cygwin.com/" text="Cygwin">}} as your command line tool for interacting with Cumulus Linux.

## Install Cumulus Linux

To install Cumulus Linux, you use {{<exlink url="https://opencomputeproject.github.io/onie" text="ONIE">}} (Open Network Install Environment), an extension to the traditional U-Boot software that allows for automatic discovery of a network installer image. This facilitates the ecosystem model of procuring switches with an operating system choice, such as Cumulus Linux. The easiest way to install Cumulus Linux with ONIE is with local HTTP discovery:

1. If your host (laptop or server) is IPv6-enabled, make sure it is running a web server. If your host is IPv4-enabled, make sure it is running DHCP in addition to a web server.

2. {{<exlink url="https://enterprise-support.nvidia.com/s/downloader" text="Download">}} the Cumulus Linux installation file to the root directory of the web server. Rename this file `onie-installer`.

3. Connect your host using an Ethernet cable to the management Ethernet port of the switch.

4. Power on the switch. The switch downloads the ONIE image installer and boots. You can watch the installation progress in your terminal. After the installation completes, the Cumulus Linux login prompt appears in the terminal window.

{{%notice note%}}
These steps describe a flexible unattended installation method; you do not need a console cable. A fresh install with ONIE using a local web server typically completes in less than ten minutes. However, you have more options for installing Cumulus Linux with ONIE, such as using a local file, FTP or USB. See {{<link url="Installing-a-New-Cumulus-Linux-Image">}} for more options.
{{%/notice%}}

After installing Cumulus Linux, you are ready to:
- Log in to Cumulus Linux on the switch.<!--\- Install the Cumulus Linux license.-->
- Configure Cumulus Linux. This quick start guide provides instructions on configuring switch ports and a loopback interface.

## Get Started

When starting Cumulus Linux for the first time, the management port makes a DHCPv4 request. To determine the IP address of the switch, you can cross reference the MAC address of the switch with your DHCP server. The MAC address is typically located on the side of the switch or on the <!-- vale off -->box<!-- vale on --> in which the unit ships.

### Login Credentials

The default installation includes two accounts:
- The system account (root) has full system privileges. Cumulus Linux locks the root account password by default (which prohibits login).
- The user account (cumulus) has `sudo` privileges. The cumulus account uses the default password `cumulus`.

   When you log in for the first time with the cumulus account, Cumulus Linux prompts you to change the default password. After you provide a new password, the SSH session disconnects and you have to reconnect with the new password.

{{%notice note%}}
ONIE includes options that allow you to change the default password for the *cumulus* account automatically when you install a new Cumulus Linux image. Refer to {{<link url="Installing-a-New-Cumulus-Linux-Image#onie-installation-options" text="ONIE Installation Options" >}}. You can also  {{<link url="Zero-Touch-Provisioning-ZTP/#set-the-default-cumulus-user-password" text="change the default password using a ZTP script">}}.
{{%/notice%}}

In this quick start guide, you use the *cumulus* account to configure Cumulus Linux.

All accounts except root can use remote SSH login; you can use `sudo` to grant a non-root account root-level access. Commands that change the system configuration require this elevated level of access.

For more information about `sudo`, see {{<link url="Using-sudo-to-Delegate-Privileges" >}}.

### Serial Console Management

NVIDIA recommends you perform management and configuration over the network, either in band or out of band. A serial console is fully supported.

Typically, switches ship from the manufacturer with a mating DB9 serial cable. Switches with ONIE are always set to a 115200 baud rate.

### Wired Ethernet Management

A Cumulus Linux switch always provides at least one dedicated Ethernet management port called eth0. This interface is specifically for out-of-band management use. The management interface uses DHCPv4 for addressing by default.

To set a static IP address:

{{< tabs "TabID86 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface eth0 ip address 192.0.2.42/24
cumulus@switch:~$ net add interface eth0 ip gateway 192.0.2.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface eth0 ip address 192.0.2.42/24
cumulus@switch:~$ nv set interface eth0 ip gateway 192.0.2.1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Edit the `/etc/network/interfaces` file:

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
# Management interface
auto eth0
iface eth0
    address 192.0.2.42/24
    gateway 192.0.2.1
```

{{< /tab >}}
{{< /tabs >}}

### Configure the Hostname

The hostname identifies the switch; make sure you configure the hostname to be unique and descriptive.

{{%notice note%}}
Do not use an underscore (_), apostrophe ('), or non-ASCII characters in the hostname.
{{%/notice%}}

To change the hostname:

{{< tabs "TabID131 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add hostname leaf01
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

The above command modifies both the `/etc/hostname` and `/etc/hosts` files.

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set platform hostname value leaf01
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Change the hostname with the `hostnamectl` command; for example:

   ```
   cumulus@switch:~$ sudo hostnamectl set-hostname leaf01
   ```

2. In the `/etc/hosts` file, replace the host for IP address 127.0.1.1 with the new hostname:

    ```
    cumulus@switch:~$ sudo nano /etc/hosts
    ...
    127.0.1.1       leaf01
    ```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The command prompt in the terminal does not reflect the new hostname until you either log out of the switch or start a new shell.
{{%/notice%}}

### Configure the Time Zone

The default time zone on the switch is UTC (Coordinated Universal Time). Change the time zone on your switch to be the time zone for your location.

To update the time zone, use NTP interactive mode:

1. In a terminal, run the following command:

    ```
    cumulus@switch:~$ sudo dpkg-reconfigure tzdata
    ```

2. Follow the on screen menu options to select the geographic area and region.

{{%notice note%}}
Programs that are already running (including log files) and logged in users, do not see time zone changes made with interactive mode. To set the time zone for all services and daemons, reboot the switch.
{{%/notice%}}

### Verify the System Time

Verify that the date and time on the switch are correct, and {{<link url="Setting-the-Date-and-Time" text="correct the date and time">}} if necessary. If the date and time is incorrect, the switch does not synchronize with Puppet and returns errors after you restart `switchd`:

```
Warning: Unit file of switchd.service changed on disk, 'systemctl daemon-reload' recommended.
```

## Configure Breakout Ports with Splitter Cables

If you are using 4x10G DAC or AOC cables, or you want to break out 100G or 40G switch ports, configure the breakout ports. For more details, see {{<link url="Switch-Port-Attributes/#breakout-ports">}}.

## Test Cable Connectivity

By default, Cumulus Linux disables all data plane ports (every Ethernet port except the management interface, eth0). To test cable connectivity, administratively enable physical ports.

{{< tabs "TabID260 ">}}
{{< tab "NCLU Commands ">}}

To administratively enable a port:

```
cumulus@switch:~$ net add interface swp1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To administratively enable all physical ports on a switch that has ports numbered from swp1 to swp52:

```
cumulus@switch:~$ net add interface swp1-52
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To view link status, run the `net show interface all` command.

{{< /tab >}}
{{< tab "NVUE Commands ">}}

To administratively enable a port:

```
cumulus@switch:~$ nv set interface swp1
cumulus@switch:~$ nv config apply
```

To administratively enable all physical ports on a switch that has ports numbered from swp1 to swp52:

```
cumulus@switch:~$ nv set interface swp1-52
cumulus@switch:~$ nv config apply
```

To view link status, run the `nv show interface` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

To administratively enable a port:

```
cumulus@switch:~$ sudo ip link set swp1 up
```

To administratively enable all physical ports, run the following bash script:

```
cumulus@switch:~$ sudo su -
cumulus@switch:~$ for i in /sys/class/net/*; do iface=`basename $i`; if [[ $iface == swp* ]]; then ip link set $iface up fi done
```

To view link status, run the `ip link show` command.

{{< /tab >}}
{{< /tabs >}}

## Configure Layer 2 Ports

Cumulus Linux does not put all ports into a bridge by default. To create a bridge and configure one or more front panel ports as members of the bridge:

{{< tabs "TabID367 ">}}
{{< tab "NCLU Commands ">}}

In the following configuration example, the front panel port swp1 is in a bridge called *bridge*.

```
cumulus@switch:~$ net add bridge bridge ports swp1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can add a range of ports in one command. For example, to add swp1 through swp10, swp12, and swp14 through swp20 to bridge:

```
cumulus@switch:~$ net add bridge bridge ports swp1-10,12,14-20
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

The following configuration example places the front panel port swp1 into the default bridge called `br_default`.

```
cumulus@switch:~$ nv set interface swp1 bridge domain br_default
cumulus@switch:~$ nv config apply
```

You can add a range of ports in one command. For example, to add swp1 through swp3, swp10, and swp14 through swp20 to the bridge:

```
cumulus@switch:~$ nv set interface swp1-3,swp6,swp14-20 bridge domain br_default
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following configuration example places the front panel port swp1 into the default bridge called `br_default`:

```
...
auto br_default
iface br_default
    bridge-ports swp1
...
```

To put a range of ports into a bridge, use the `glob` keyword. For example, to add swp1 through swp10, swp12, and swp14 through swp20 to the bridge called `br_default`:

```
...
auto br_default
iface br_default
    bridge-ports glob swp1-10 swp12 glob swp14-20
...
```

To apply the configuration, check for typos:

```
cumulus@switch:~$ sudo ifquery -a
```

If there are no errors, run the following command:

```
cumulus@switch:~$ sudo ifup -a
```

{{< /tab >}}
{{< /tabs >}}

For more information about Ethernet bridges, see {{<link url="Ethernet-Bridging-VLANs" text="Ethernet Bridging - VLANs">}}.

## Configure Layer 3 Ports

You can configure a front panel port or bridge interface as a layer 3 port.

{{< tabs "TabID437 ">}}
{{< tab "NCLU Commands ">}}

In the following configuration example, the front panel port swp1 is a layer 3 access port:

```
cumulus@switch:~$ net add interface swp1 ip address 10.1.1.1/30
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To add an IP address to a bridge interface, you must put it into a VLAN interface. If you want to use a VLAN other than the native one, set the bridge PVID:

```
cumulus@switch:~$ net add vlan 100 ip address 10.2.2.1/24
cumulus@switch:~$ net add bridge bridge pvid 100
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

The following configuration example configures the front panel port swp1 as a layer 3 access port:

```
cumulus@switch:~$ nv set interface swp1 ip address 10.1.1.1/30
cumulus@switch:~$ nv config apply
```

To add an IP address to a bridge interface, you must put it into a VLAN interface. If you want to use a VLAN other than the native one, set the bridge PVID:

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 100
cumulus@switch:~$ nv set interface vlan100 ip address 10.2.2.1/24
cumulus@switch:~$ nv set bridge domain br_default untagged 100
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following configuration example configures the front panel port swp1 as a layer 3 access port:

```
auto swp1
iface swp1
  address 10.1.1.1/30
```

To add an IP address to a bridge interface, include the address under the `iface` stanza in the `/etc/network/interfaces` file. If you want to use a VLAN other than the native one, set the bridge PVID:

```
auto br_default
iface br_default
    address 10.2.2.1/24
    bridge-ports glob swp1-10 swp12 glob swp14-20
    bridge-pvid 100
```

To apply the configuration, check for typos:

```
cumulus@switch:~$ sudo ifquery -a
```

If there are no errors, run the following command:

```
cumulus@switch:~$ sudo ifup -a
```

{{< /tab >}}
{{< /tabs >}}

## Configure a Loopback Interface

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface, called *lo*, is up and assigned an IP address of 127.0.0.1.

{{%notice note%}}
The loopback interface *lo* must always exist on the switch and must always be up.
{{%/notice%}}

To check the status of the loopback interface:

{{< tabs "TabID473 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net show interface lo
    Name    MAC                Speed    MTU    Mode
--  ------  -----------------  -------  -----  --------
UP  lo      00:00:00:00:00:00  N/A      65536  Loopback

Alias
-----
loopback interface
IP Details
-------------------------  --------------------
IP:                        127.0.0.1/8, ::1/128
IP Neighbor(ARP) Entries:  0
```

The loopback is up with the IP address 127.0.0.1.

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv show interface lo
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

```
cumulus@switch:~$ ip addr show lo
```

{{< /tab >}}
{{< /tabs >}}

To add an IP address to a loopback interface, configure the *lo* interface:

{{< tabs "TabID510 ">}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add loopback lo ip address 10.1.1.1/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv set interface lo ip address 10.10.10.1/32
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Add the IP address directly under the `iface lo inet loopback` definition in the `/etc network/interfaces` file:

```
auto lo
iface lo inet loopback
    address 10.10.10.1
```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
If you configure an IP address without a subnet mask, it becomes a /32 IP address. For example, 10.10.10.1 is 10.10.10.1/32.
{{%/notice%}}

You can add multiple loopback addresses. For more information, see {{<link url="Interface-Configuration-and-Management/#loopback-interface" text="Interface Configuration and Management">}}.

{{%notice info%}}
If you run NVUE Commands to configure the switch, run the `nv config save` command before you reboot to save the applied configuration to the startup configuration so that the changes persist after the reboot.

```
cumulus@switch:~$ nv config save
```
{{%/notice%}}
