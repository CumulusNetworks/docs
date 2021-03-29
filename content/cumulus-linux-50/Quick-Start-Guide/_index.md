---
title: Quick Start Guide
author: NVIDIA
weight: 10
toc: 2
---

This quick start guide provides an end-to-end setup process for installing and running Cumulus Linux, as well as a collection of example commands for getting started after installation is complete.

## Prerequisites

Intermediate-level Linux knowledge is assumed for this guide. You need to be familiar with basic text editing, Unix file permissions, and process monitoring. A variety of text editors are pre-installed, including `vi` and `nano`.

You must have access to a Linux or UNIX shell. If you are running Windows, use a Linux environment like {{<exlink url="http://www.cygwin.com/" text="Cygwin">}} as your command line tool for interacting with Cumulus Linux.

## Install Cumulus Linux

To install Cumulus Linux, you use {{<exlink url="https://opencomputeproject.github.io/onie" text="ONIE">}} (Open Network Install Environment), an extension to the traditional U-Boot software that allows for automatic discovery of a network installer image. This facilitates the ecosystem model of procuring switches with an operating system choice, such as Cumulus Linux. The easiest way to install Cumulus Linux with ONIE is with local HTTP discovery:

1. If your host (laptop or server) is IPv6-enabled, make sure it is running a web server. If your host is IPv4-enabled, make sure it is running DHCP in addition to a web server.

2. {{<exlink url="https://cumulusnetworks.com/downloads/" text="Download">}} the Cumulus Linux installation file to the root directory of the web server. Rename this file `onie-installer`.

3. Connect your host using an Ethernet cable to the management Ethernet port of the switch.

4. Power on the switch. The switch downloads the ONIE image installer and boots. You can watch the installation progress in your terminal. After the installation completes, the Cumulus Linux login prompt appears in the terminal window.

{{%notice note%}}
These steps describe a flexible unattended installation method; you do not need a console cable. A fresh install with ONIE using a local web server typically completes in less than ten minutes. However, you have more options for installing Cumulus Linux with ONIE, such as using a local file, FTP or USB. See {{<link url="Installing-a-New-Cumulus-Linux-Image">}} for more options.
{{%/notice%}}

After installing Cumulus Linux, you are ready to:
- Log in to Cumulus Linux on the switch.<!--\- Install the Cumulus Linux license.-->
- Configure Cumulus Linux. This quick start guide provides instructions on configuring switch ports and a loopback interface.

## Get Started

When starting Cumulus Linux for the first time, the management port makes a DHCPv4 request. To determine the IP address of the switch, you can cross reference the MAC address of the switch with your DHCP server. The MAC address is typically located on the side of the switch or on the box in which the unit ships.

### Login Credentials

The default installation includes two accounts:
- The system account (root) has full system privileges. The root account password is locked by default (which prohibits login).
- The user account (cumulus) has `sudo` privileges. The cumulus account is configured with the default password `cumulus`.

   When you log into Cumulus Linux for the first time with the cumulus account, you are prompted to change the default password. After you provide a new password, the SSH session disconnects and you have to reconnect with the new password.

{{%notice note%}}
ONIE includes options that allow you to change the default password for the *cumulus* account automatically when you install a new Cumulus Linux image. Refer to {{<link url="Installing-a-New-Cumulus-Linux-Image#onie-installation-options" text="ONIE Installation Options" >}}. You can also  {{<link url="Zero-Touch-Provisioning-ZTP/#set-the-default-cumulus-user-password" text="change the default password using a ZTP script">}}.
{{%/notice%}}

In this quick start guide, you use the *cumulus* account to configure Cumulus Linux.

All accounts except root are permitted remote SSH login; you can use `sudo` to grant a non-root account root-level access. Commands that change the system configuration require this elevated level of access.

For more information about `sudo`, read {{<link url="Using-sudo-to-Delegate-Privileges" >}}.

### Serial Console Management

You are encouraged to perform management and configuration over the network, either in band or out of band. A serial console is fully supported; however, you might prefer the convenience of network-based management.

Typically, switches ship from the manufacturer with a mating DB9 serial cable. Switches with ONIE are always set to a 115200 baud rate.

### Wired Ethernet Management

A Cumulus Linux switch always provides at least one dedicated Ethernet management port, which is named eth0. This interface is geared specifically for out-of-band management use. The management interface uses DHCPv4 for addressing by default.

To set a static IP address:

{{< tabs "TabID86 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface eth0 ip address 192.0.2.42/24
cumulus@switch:~$ cl set interface eth0 ip gateway 192.0.2.1
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

Set the static IP address with the `interface address` and `interface gateway` NCLU commands:

```
cumulus@switch:~$ net add interface eth0 ip address 192.0.2.42/24
cumulus@switch:~$ net add interface eth0 ip gateway 192.0.2.1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

Set a static IP address by editing the `/etc/network/interfaces` file:

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

### Configure the Hostname and Timezone

Configure the hostname and timezone for your switch. The hostname identifies the switch; make sure you configure the hostname to be unique and descriptive.

{{%notice note%}}
Do not use an underscore (_), apostrophe ('), or non-ASCII character in the hostname.
{{%/notice%}}

To change the hostname:

{{< tabs "TabID131 ">}}
{{< tab "CUE Commands ">}}

The following example sets the hostname to leaf01:

```
cumulus@switch:~$ cl set system hostname leaf01
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

The following example command configures the hostname to be leaf01:

```
cumulus@switch:~$ net add hostname leaf01
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

1. Edit the `/etc/hostname` file with the desired hostname:

    ```
    cumulus@switch:~$ sudo nano /etc/hostname
    ```

2. In `/etc/hosts` file, replace the 127.0.1.1 IP address with the new hostname:

    ```
    cumulus@switch:~$ sudo nano /etc/hosts
    ```

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
The command prompt in the terminal does not reflect the new hostname until you either log out of the switch or start a new shell.
{{%/notice%}}

The default timezone on the switch is UTC (Coordinated Universal Time). Change the timezone on your switch to be the timezone for your location.

To update the timezone, use NTP interactive mode:

1. In a terminal, run the following command:

    ```
    cumulus@switch:~$ sudo dpkg-reconfigure tzdata
    ```

2. Follow the on screen menu options to select the geographic area and region.

{{%notice note%}}
Programs that are already running (including log files) and users currently logged in, do not see timezone changes made with interactive mode. To set the timezone for all services and daemons, reboot the switch.
{{%/notice%}}

### Verify the System Time

Verify that the date and time on the switch are correct, and {{<link url="Setting-Date-and-Time" text="correct the date and time">}} if necessary. If the date and time is incorrect, the switch might not be able to synchronize with Puppet or might return errors after you restart `switchd`:

```
Warning: Unit file of switchd.service changed on disk, 'systemctl daemon-reload' recommended.
```

<!--### Install the License

Cumulus Linux is licensed on a per-instance basis. Each network system is fully operational, enabling any capability to be utilized on the switch with the exception of forwarding on switch panel ports. Only eth0 and console ports are activated on an unlicensed instance of Cumulus Linux. Enabling front panel ports requires a license.

You receive a license key from NVIDIA or an authorized reseller. Here is a sample license key:

```
user@company.com|thequickbrownfoxjumpsoverthelazydog312
```

There are three ways to install the license onto the switch:

- Copy the license from a local server. Create a text file with the license and copy it to a server accessible from the switch. On the switch, use the following command to transfer the file directly on the switch, then install the license file:

    ```
    cumulus@switch:~$ scp user@my_server:/home/user/my_license_file.txt .
    cumulus@switch:~$ sudo cl-license -i my_license_file.txt
    ```

- Copy the file to an HTTP server (not HTTPS), then reference the URL when you run `cl-license`:

    ```
    cumulus@switch:~$ sudo cl-license -i <URL>
    ```

- Copy and paste the license key into the `cl-license` command:

    ```
    cumulus@switch:~$ sudo cl-license -i
    <paste license key>
    ^+d
    ```

Check that your license is installed with the `cl-license` command.

    cumulus@switch:~$ cl-license
    user@example.com|$ampleL1cen$et3xt

{{%notice note%}}
It is not necessary to reboot the switch to activate the switch ports. After you install the license, restart the `switchd` service. All front panel ports become active and show up as swp1, swp2, and so on.

{{<cl/restart-switchd>}}

If a license is not installed on a Cumulus Linux switch, the `switchd` service does not start. After you install the license, start `switchd` as described above.
{{%/notice%}}-->

## Configure Breakout Ports with Splitter Cables

If you are using 4x10G DAC or AOC cables, or want to break out 100G or 40G switch ports, configure the breakout ports. For more details, see {{<link url="Switch-Port-Attributes">}}.

## Test Cable Connectivity

By default, all data plane ports (every Ethernet port except the management interface, eth0) are disabled.

To administratively enable a port:

{{< tabs "TabID260 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface swp1 link state up
cumulus@switch:~$ cl config apply
```

To administratively enable all physical ports, run the following command, where swp1-52 represents a switch with ports numbered from swp1 to swp52:

```
cumulus@switch:~$ cl set interface swp1-52 link state up
cumulus@switch:~$ cl config apply
```

To view link status, use the `cl show interface` command:

```
cumulus@switch:~$ cl show interface
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add interface swp1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To administratively enable all physical ports, run the following command, where swp1-52 represents a switch with switch ports numbered from swp1 to swp52:

```
cumulus@switch:~$ net add interface swp1-52
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

To view link status, use the `net show interface all` command:

```
cumulus@switch:~$ net show interface all
State  Name     Spd  MTU    Mode           LLDP                    Summary
-----  -------  ---  -----  -------------  ----------------------  -------------------------
UP     lo       N/A  65536  Loopback                               IP: 127.0.0.1/8
       lo                                                          IP: ::1/128
UP     eth0     1G   1500   Mgmt           oob-mgmt-switch (swp8)  Master: mgmt(UP)
       eth0                                                        IP: 192.168.0.13/24(DHCP)
UP     swp1     1G   9216   Default
UP     swp2     1G   9216   Default
ADMDN  swp45    N/A  1500   NotConfigured
ADMDN  swp46    N/A  1500   NotConfigured
ADMDN  swp47    N/A  1500   NotConfigured
ADMDN  swp48    N/A  1500   NotConfigured
UP     swp49    1G   9216   Default
UP     swp50    1G   9216   Default
UP     swp51    1G   9216   Default        spine01 (swp3)
ADMDN  swp52    N/A  1500   NotConfigured
UP     mgmt     N/A  65536  VRF                                    IP: 127.0.0.1/8
       mgmt                                                        IP: ::1/128
ADMDN  vagrant  N/A  1500   NotConfigured
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To enable a port, run the `ip link set <interface> up` command. For example:

```
cumulus@switch:~$ sudo ip link set swp1 up
```

As root, run the following bash script to administratively enable all physical ports:
```
cumulus@switch:~$ sudo su -
cumulus@switch:~$ for i in /sys/class/net/*; do iface=`basename $i`; if [[ $iface == swp* ]]; then ip link set $iface up fi done
```

To view link status, use the `ip link show` command. The following examples show the output of a port in *down* and *up* mode:

```
# Administratively Down
swp1: <BROADCAST,MULTICAST> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 1000

# Administratively Up but Layer 1 protocol is Down
swp1: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc pfifo_fast state DOWN mode DEFAULT qlen 500

# Administratively Up, Layer 1 protocol is Up
swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT qlen 500
```

{{< /tab >}}
{{< /tabs >}}

## Configure Switch Ports

This section describes how to configure switch ports, such as create a bridge.

### Layer 2 Port Configuration

Cumulus Linux does not put all ports into a bridge by default. To create a bridge and configure one or more front panel ports as members of the bridge, use the following examples as a guide.

{{< tabs "TabID367 ">}}
{{< tab "CUE Commands ">}}

In the following configuration example, the front panel port swp1 is placed into a bridge called `br_default`.

```
cumulus@switch:~$ cl set interface swp1 bridge domain br_default
cumulus@switch:~$ cl config apply
```

You can add a range of ports in one command. For example, to add swp1 through swp10, swp12, and swp14 through swp20 to the bridge:

```
cumulus@switch:~$ cl set interface swp1,swp12,swp14-20 bridge domain br_default
cumulus@switch:~$ cl config apply
```

To show the bridges configured on the switch, use the `cl show bridge` command:

```
cumulus@switch:~$ cl show bridge
          running     applied      description
--------  -------     ----------   --------------
[domain]  br_default  br_default   Bridge domains
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

In the following configuration example, the front panel port swp1 is placed into a bridge called *bridge*.

```
cumulus@switch:~$ net add bridge bridge ports swp1
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

You can add a range of ports in one command. For example, to add swp1 through swp10, swp12, and swp14 through swp20 to the bridge:

```
cumulus@switch:~$ net add bridge bridge ports swp1-10,12,14-20
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the following configuration example, the front panel port swp1 is placed into the bridge `br_default`:

```
...
auto br_default
iface br_default
    bridge-ports swp1
...
```

To put a range of ports into a bridge, use the `glob` keyword. For example, to add swp1 through swp10, swp12, and swp14 through swp20 to `br_default`:

```
...
auto br_default
iface br_default
    bridge-ports glob swp1-10 swp12 glob swp14-20
...
```

To activate or apply the configuration to the kernel:

```
# First, check for typos:
cumulus@switch:~$ sudo ifquery -a

# Then activate the change if no errors are found:
cumulus@switch:~$ sudo ifup -a
```

{{< /tab >}}
{{< /tabs >}}

### Layer 3 Port Configuration

You can configure a front panel port or bridge interface as a layer 3 port.

{{< tabs "TabID437 ">}}
{{< tab "CUE Commands ">}}

In the following configuration example, the front panel port swp1 is configured as a layer 3 access port:

```
cumulus@switch:~$ cl set interface swp1 ip address 10.1.1.1/30
cumulus@switch:~$ cl config apply
```

To add an IP address to a bridge interface, you must put it into a VLAN interface. If you want to use a VLAN other than the native one, set the bridge PVID:

```
cumulus@switch:~$ cl set interface swp1-2 bridge domain br_default
cumulus@switch:~$ cl set bridge domain br_default vlan 100
cumulus@switch:~$ cl set interface vlan100 ip address 10.2.2.1/24
cumulus@switch:~$ cl set bridge domain br_default untagged 100
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

In the following configuration example, the front panel port swp1 is configured as a layer 3 access port:

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
{{< tab "Linux Commands ">}}

In the following configuration example, the front panel port swp1 is configured as a layer 3 access port:

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

To activate or apply the configuration to the kernel:

```
# First check for typos:
cumulus@switch:~$ sudo ifquery -a

# Then activate the change if no errors are found:
cumulus@switch:~$ sudo ifup -a
```

{{< /tab >}}
{{< /tabs >}}

## Configure a Loopback Interface

Cumulus Linux has a loopback interface preconfigured in the `/etc/network/interfaces` file. When the switch boots up, it has a loopback interface, called *lo*, which is up and assigned an IP address of 127.0.0.1.

{{%notice note%}}
The loopback interface *lo* must always exist on the switch and must always be up.
{{%/notice%}}

To see the status of the loopback interface (lo), run the CUE `cl show interface lo` command or the Linux `ip addr show lo` command.

To add an IP address to a loopback interface:

{{< tabs "TabID538 ">}}
{{< tab "CUE Commands ">}}

```
cumulus@switch:~$ cl set interface lo ip address 10.10.10.1/32
cumulus@switch:~$ cl config apply
```

{{< /tab >}}
{{< tab "NCLU Commands ">}}

```
cumulus@switch:~$ net add loopback lo ip address 10.10.10.1/32
cumulus@switch:~$ net pending
cumulus@switch:~$ net commit
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
If an IP address is configured without a mask, the IP address becomes a /32. For example, 10.10.10.1 is 10.10.10.1/32.
{{%/notice%}}

You can add multiple loopback addresses. See {{<link url="Interface-Configuration-and-Management#configure-multiple-loopbacks" text="Configure Multiple Loopbacks">}} for more details.

## Reboot the Switch

After you complete the configuration in this section, reboot the switch.

{{%notice info%}}
If you run CUE commands to configure the switch, run the `cl config save` command before you reboot to save the applied configuration to the startup configuration so that the changes persist after the reboot.

```
cumulus@switch:~$ cl config save
```
{{%/notice%}}

```
cumulus@switch:~$ sudo reboot
```
