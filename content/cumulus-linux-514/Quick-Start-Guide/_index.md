---
title: Quick Start Guide
author: NVIDIA
weight: 10
toc: 2
---

This quick start guide provides an end-to-end setup process for installing and running Cumulus Linux.

## Prerequisites

This guide assumes you have intermediate-level Linux knowledge. You need to be familiar with basic text editing, Unix file permissions, and process monitoring. Cumulus Linux includes a variety of preinstalled text editors, such as `vi` and `nano`.

You must have access to a Linux or UNIX shell. If you are running Windows, use a Linux environment like {{<exlink url="http://www.cygwin.com/" text="Cygwin">}} as your command line tool for interacting with Cumulus Linux.

## Get Started

Cumulus Linux is on the switch by default. To upgrade to a different Cumulus Linux release or reinstall Cumulus Linux, refer to {{<link url="Installation-Management" text="Installation Management">}}. To show the current Cumulus Linux release on the switch, run the NVUE `nv show system` command.

When starting Cumulus Linux for the first time, the management port makes a DHCPv4 request. To determine the IP address of the switch, you can cross reference the serial number of the switch with your DHCP server. The DHCP request from the switch includes the serial number in the client identifier (option 61).

To get started:
- Log in to Cumulus Linux on the switch and change the default credentials.
- Configure Cumulus Linux. This quick start guide provides instructions on changing the hostname of the switch, setting the date and time, and configuring switch ports and a loopback interface.

{{%notice warning%}}
You can choose to configure Cumulus Linux either with NVUE commands **or** Linux commands (with vtysh or by manually editing configuration files). Do **not** run both NVUE configuration commands (such as `nv set`, `nv unset`, `nv action`, `nv config`) and Linux commands to configure the switch. NVUE commands replace the configuration in files such as `/etc/network/interfaces` and `/etc/frr/frr.conf`, and remove any configuration you add manually or with automation tools like Ansible, Chef, or Puppet.

If you choose to configure Cumulus Linux with NVUE, you can configure features that do not yet support the NVUE object model by creating {{<link url="NVUE-Snippets" text="NVUE Snippets">}}.
{{%/notice%}}

### Login Credentials

The default installation includes two accounts:
- The system account (root) has full system privileges. Cumulus Linux locks the root account password, which prohibits login.
- The user account (cumulus) has `sudo` privileges. The cumulus account uses the default password `cumulus`. When you log in for the first time with the cumulus account, Cumulus Linux prompts you to change the default password. After you provide a new password, the SSH session disconnects and you have to reconnect with the new password.

{{%notice note%}}
ONIE includes options that allow you to change the default password for the *cumulus* account automatically when you install a new Cumulus Linux image. Refer to {{<link url="Installing-a-New-Cumulus-Linux-Image-with-ONIE#onie-installation-options" text="ONIE Installation Options" >}}. You can also  {{<link url="Zero-Touch-Provisioning-ZTP/#set-the-default-cumulus-user-password" text="change the default password using a ZTP script">}}.
{{%/notice%}}

In this quick start guide, you use the *cumulus* account to configure Cumulus Linux.

All accounts except root can use remote SSH login; you can use `sudo` to grant a non-root account root-level access. Commands that change the system configuration require this elevated level of access.

For more information about `sudo`, see {{<link url="Using-sudo-to-Delegate-Privileges" >}}.

### Serial Console Management

NVIDIA recommends you perform management and configuration over the network, either in band or out of band. A serial console is fully supported.

Typically, switches ship from the manufacturer with a mating DB9 serial cable. Switches with ONIE are always set to a 115200 baud rate.

### Wired Ethernet Management

A Cumulus Linux switch always provides at least one dedicated Ethernet management port called eth0. This interface is specifically for out-of-band management use. The management interface uses DHCPv4 for addressing by default.

To set a static IP address and gateway address for eth0:

{{< tabs "TabID86 ">}}
{{< tab "NVUE Commands ">}}

```
cumulus@switch:~$ nv unset interface eth0 ip address dhcp
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
{{< tab "NVUE Commands ">}}

Run the `nv set system hostname <hostname>` command. The following example sets the hostname to leaf01:

```
cumulus@switch:~$ nv set system hostname leaf01
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

### Configure the Domain Name

You can configure the domain name on the Cumulus Linux switch, which is critical for accurate DNS resolution, network service integration, and compliance with networking standards. Cumulus Linux adds the domain name to the hostname and displays both the hostname and domain name in the shell prompt (after you log back in).

{{< tabs "TabID135 ">}}
{{< tab "NVUE Commands ">}}

Run the `nv set system dns domain <domain>` command. The following example sets the domain name to nvidia.com:

```
cumulus@switch:~$ nv set system dns domain nvidia.com
cumulus@switch:~$ nv config apply
```

To unset the domain name, run the `nv unset system dns domain` command.

To show the configured domain name, run the `nv show system dns` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

In the `/etc/hosts` file, add the domain to the IP address 127.0.1.1 and hostname:

```
cumulus@switch:~$ sudo nano /etc/hosts
...
127.0.1.1       leaf01.nvidia.com leaf01
```

{{< /tab >}}
{{< /tabs >}}

### Configure the Time Zone

The default time zone on the switch is UTC (Coordinated Universal Time). Change the time zone on your switch to be the time zone for your location.

To update the time zone:

{{< tabs "TabID19 ">}}
{{< tab "NVUE Commands ">}}
<!-- vale off -->
Run the `nv set system timezone <timezone>` command. To see all the available time zones, run `nv set system timezone` and press the Tab key. The following example sets the time zone to US/Eastern:

```
cumulus@switch:~$ nv set system timezone US/Eastern
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Follow the Guided Wizard ">}}

1. In a terminal, run the following command:

    ```
    cumulus@switch:~$ sudo dpkg-reconfigure tzdata
    ```

2. Follow the on screen menu options to select the geographic area and region.

{{< /tab >}}
{{< /tabs >}}

{{%notice note%}}
Programs that are already running (including log files) and logged in users, do not see time zone changes. To set the time zone for all services and daemons, reboot the switch.
{{%/notice%}}

### Verify the System Time

Verify that the date and time on the switch are correct. If the date and time are incorrect, the switch does not synchronize with automation tools, such as Puppet, and returns errors after you restart `switchd`.

{{< tabs "TabID166 ">}}
{{< tab "NVUE Commands ">}}

To show the current date and time, run the `nv show system time` command:

```
cumulus@switch:~$ nv show system time
                           operational                  
-------------------------  -----------------------------
local-time                 Wed 2024-08-21 17:39:44 EDT
universal-time             Wed 2024-08-21 21:39:44 UTC
rtc-time                   Fri 2024-08-16 16:50:06    
time-zone                  US/Eastern (EDT, -0400)    
system-clock-synchronized  no                         
ntp-service                n/a                        
rtc-in-local-tz            no                         
unix-time                  1724276384.1403222
```

To set the software clock according to the configured time zone, run the `nv action change system time <YYYY-MM-DD> <HH:MM:SS>` command; for example:

```
cumulus@switch:~$ nv action change system time 2023-12-04 2:33:30
System Date-time changed successfully
Local Time is now Mon 2023-12-04 02:33:30 UTC
Action succeeded
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

To show the current date and time on the switch, run the `date` command:

```
cumulus@switch:~$ date
Wed 11 Oct 2023 12:18:33 PM UTC
```

To set the software clock according to the configured time zone, run the `sudo date -s` command:

```
cumulus@switch:~$ sudo date -s "Tue Jan 26 00:37:13 02021"
```

{{< /tab >}}
{{< /tabs >}}

For more information about setting the system time, see {{<link url="Setting-the-Date-and-Time" text="Setting the Date and Time">}}.

### NTP and PTP

- NTP starts at boot by default on the switch and the NTP configuration includes default servers. To customize NTP, see {{<link url="Network-Time-Protocol-NTP" text="NTP">}}.
- PTP is off by default on the switch. To configure PTP, see {{<link url="Precision-Time-Protocol-PTP" text="PTP">}}.

## Configure Breakout Ports with Splitter Cables

If you are using 4x10G DAC or AOC cables, or you want to break out (split) switch ports, configure the breakout ports; see {{<link url="Switch-Port-Attributes/#breakout-ports">}}.

## Test Cable Connectivity

By default, Cumulus Linux disables all data plane ports (every Ethernet port except the management interface, eth0). To test cable connectivity, administratively enable physical ports.

{{< tabs "TabID260 ">}}
{{< tab "NVUE Commands ">}}

To enable a port administratively, run the `nv set interface <interface>` command:

```
cumulus@switch:~$ nv set interface swp1
cumulus@switch:~$ nv config apply
```

To enable all physical ports administratively on a switch that has ports numbered from swp1 to swp52:

```
cumulus@switch:~$ nv set interface swp1-52
cumulus@switch:~$ nv config apply
```

To view link status, run the `nv show interface` command.

{{< /tab >}}
{{< tab "Linux Commands ">}}

To enable a port administratively, edit the `/etc/network/interfaces` file to add the port, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

To enable all physical ports administratively, edit the `/etc/network/interfaces` file to add all the interfaces, then run the `ifreload -a` command.

```
cumulus@switch:~$ sudo nano /etc/network/interfaces
...
auto swp1
iface swp1

auto swp2
iface swp2

auto swp3
iface swp3
...
```

```
cumulus@switch:~$ sudo ifreload -a
```

To view link status, run the `ip link show` command.

{{< /tab >}}
{{< /tabs >}}

## Configure Layer 2 Ports

Cumulus Linux does not put all ports into a bridge by default. To create a bridge and configure one or more front panel ports as members of the bridge, run the following commands.

{{< tabs "TabID367 ">}}
{{< tab "NVUE Commands ">}}

The following example places the front panel port swp1 into the default bridge called `br_default`.

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

The following example places the front panel port swp1 into the default bridge called `br_default`:

```
...
auto br_default
iface br_default
    bridge-ports swp1
...
```

The following example adds swp1 through swp3, swp10, and swp14 through swp20 to the bridge:

```
...
auto br_default
iface br_default
    bridge-ports swp1 swp2 swp3 swp6 swp14 swp15 swp16 swp17 swp18 swp19 swp20
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
{{< tab "NVUE Commands ">}}

The following example configures the front panel port swp1 as a layer 3 access port:

```
cumulus@switch:~$ nv set interface swp1 ip address 10.0.0.0/31
cumulus@switch:~$ nv config apply
```

To add an IP address to a bridge interface, you must put it into a VLAN interface. If you want to use a VLAN other than the native one, set the bridge PVID:

```
cumulus@switch:~$ nv set interface swp1-2 bridge domain br_default
cumulus@switch:~$ nv set bridge domain br_default vlan 10
cumulus@switch:~$ nv set interface vlan10 ip address 10.1.10.2/24
cumulus@switch:~$ nv set bridge domain br_default untagged 1
cumulus@switch:~$ nv config apply
```

{{< /tab >}}
{{< tab "Linux Commands ">}}

The following example configures the front panel port swp1 as a layer 3 access port:

```
auto swp1
iface swp1
  address 10.0.0.0/31
```

To add an IP address to a bridge interface, include the address under the `iface` stanza in the `/etc/network/interfaces` file. If you want to use a VLAN other than the native one, set the bridge PVID:

```
auto vlan10
iface vlan10
    address 10.1.10.2/24
    vlan-raw-device br_default
    vlan-id 10
auto br_default
iface br_default
    bridge-ports swp1 swp2
    hwaddress 44:38:39:22:01:78
    bridge-vlan-aware yes
    bridge-vids 10
    bridge-pvid 1
    bridge-stp yes
    bridge-mcsnoop no
    mstpctl-forcevers rstp
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

Cumulus Linux has a preconfigured loopback interface. When the switch boots up, the loopback interface, called `lo`, is up and assigned an IP address of 127.0.0.1.

{{%notice note%}}
The loopback interface `lo` must always exist on the switch and must always be up. To check the status of the loopback interface, run the NVUE `nv show interface lo` command or the Linux `ip addr show lo` command.
{{%/notice%}}

The following example sets the loopback IP address to 10.10.10.1/32.

{{< tabs "TabID510 ">}}
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
    address 10.10.10.1/32
```

{{< /tab >}}
{{< /tabs >}}

You can add multiple loopback addresses. For more information, see {{<link url="Interface-Configuration-and-Management/#loopback-interface" text="Interface Configuration and Management">}}.

## Show Platform and System Settings

- To show the hostname of the switch, the time zone, and the Cumulus Linux version, run the NVUE `nv show system` command.
- To show the Cumulus Linux kernel and image version, and the build date and time, run the `nv show system version` command.
- To show switch platform information, such as the system MAC address, manufacturer, ASIC model, CPU, hard disk drive size, RAM size, and port layout, run the NVUE `nv show platform` command.

## Next Steps

You are now ready to configure the switch according to your needs. This guide provides separate sections that describe how to configure {{<link url="System-Configuration" text="system">}}, {{<link url="Layer-1-and-Switch-Ports" text="layer 1">}}, {{<link url="Layer-2" text="layer 2">}}, {{<link url="Layer-3" text="layer 3">}}, and {{<link url="Network-Virtualization" text="network virtualization">}} settings. Each section includes example configurations and {{<link url="Try-It-Pre-built-Demos" text="pre-built demos">}}.

For a deep dive into the NVUE object model that provides a CLI to simplify configuration, see {{<link url="NVIDIA-User-Experience-NVUE" text="NVUE">}}.
