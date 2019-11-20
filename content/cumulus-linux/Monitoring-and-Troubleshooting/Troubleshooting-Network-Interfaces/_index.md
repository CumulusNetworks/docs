---
title: Troubleshooting Network Interfaces
author: Cumulus Networks
weight: 225
aliases:
 - /display/DOCS/Troubleshooting+Network+Interfaces
 - /pages/viewpage.action?pageId=8366324
product: Cumulus Linux
version: '4.0'
---
The following sections describe various ways you can troubleshoot `ifupdown2`.

## Enable Logging for Networking

To obtain verbose logs when you run `systemctl` \[`start`|`restart`\] `networking.service` as well as when the switch boots, create an overrides file with the `systemctl edit networking.service` command and add the following lines:

```
[Service]
# remove existing ExecStart rule
ExecStart=
# start ifup with verbose option
ExecStart=/sbin/ifup -av
```

{{%notice note%}}

When you run the `systemctl edit` command, you do *not* need to run `systemctl daemon-reload`.

{{%/notice%}}

To disable logging, either:

- Remove the overrides file. Run the `systemctl cat networking` command to show the name of the overrides file.
- Run the `systemctl edit networking.service` command and remove the lines you added.

## Exclude Certain Interfaces from Coming Up

To exclude an interface so that it does not come up when you boot the switch or start/stop/reload the networking service:

1. Create a file in the `/etc/systemd/system/networking.service.d` directory (for example, `/etc/systemd/system/networking.service.d/override.conf`).
2. Add the following lines to the file, where `<interface>` is the interface you want to exclude (such as eth0).

```
[Service]
ExecStart=
ExecStart=/sbin/ifup -a -X <interface>
ExecStop=
ExecStop=/sbin/ifdown -a -X <interface>
```

You can exclude any interface specified in the `/etc/network/interfaces` file.

## Use ifquery to Validate and Debug Interface Configurations

You use `ifquery` to print parsed `interfaces` file entries.

To use `ifquery` to pretty print `iface` entries from the `interfaces` file, run:

```
cumulus@switch:~$ sudo ifquery bond0
auto bond0
iface bond0
    address 14.0.0.9/30
    address 2001:ded:beef:2::1/64
    bond-slaves swp25 swp26
```

Use `ifquery --check` to check the current running state of an interface within the `interfaces` file. It will return exit code *0* or *1* if the configuration does not match. The line `bond-xmit-hash-policy layer3+7` below fails because it should read `bond-xmit-hash-policy layer3+4`.

```
cumulus@switch:~$ sudo ifquery --check bond0
iface bond0
    bond-xmit-hash-policy layer3+7  [fail]
    bond-slaves swp25 swp26         [pass]
    address 14.0.0.9/30             [pass]
    address 2001:ded:beef:2::1/64   [pass]
```

{{%notice note%}}

`ifquery --check` is an experimental feature.

{{%/notice%}}

Use `ifquery --running` to print the running state of interfaces in the `interfaces` file format:

```
cumulus@switch:~$ sudo ifquery --running bond0
auto bond0
iface bond0
    bond-slaves swp25 swp26
    address 14.0.0.9/30
    address 2001:ded:beef:2::1/64
```

`ifquery --syntax-help` provides help on all possible attributes supported in the `interfaces` file. For complete syntax on the `interfaces` file, see `man interfaces` and `man ifupdown-addons-interfaces`.

You can use `ifquery --print-savedstate` to check the `ifupdown2` state database. `ifdown` works only on interfaces present in this state database.

```
cumulus@leaf1$ sudo ifquery --print-savedstate eth0  
auto eth0
iface eth0 inet dhcp
```

## Mako Template Errors

An easy way to debug and get details about template errors is to use the `mako-render` command on your interfaces template file or on `/etc/network/interfaces` itself.

```
cumulus@switch:~$ sudo mako-render /etc/network/interfaces
# This file describes the network interfaces available on your system
# and how to activate them. For more information, see interfaces(5).

# The loopback network interface
auto lo
iface lo inet loopback

# The primary network interface
auto eth0
iface eth0 inet dhcp
#auto eth1
#iface eth1 inet dhcp

# Include any platform-specific interface configuration
source /etc/network/interfaces.d/*.if

# ssim2 added
auto swp45
iface swp45

auto swp46
iface swp46

cumulus@switch:~$ sudo mako-render /etc/network/interfaces.d/<interfaces_stub_file>
```

## ifdown Cannot Find an Interface that Exists

If you are trying to bring down an interface that you know exists, use `ifdown` with the `--use-current-config` option to force `ifdown` to check the current `/etc/network/interfaces` file to find the interface. This can solve issues where the `ifup` command issues for that interface are interrupted before it updates the state database. For example:

```
cumulus@switch:~$ sudo ifdown br0
error: cannot find interfaces: br0 (interface was probably never up ?)

cumulus@switch:~$ sudo brctl show
bridge name   bridge id      STP enabled interfaces
br0      8000.44383900279f   yes     downlink
                             peerlink

cumulus@switch:~$ sudo ifdown br0 --use-current-config 
```

## Remove All References to a Child Interface

If you have a configuration with a child interface, whether it is a VLAN, bond, or another physical interface and you remove that interface from a running configuration, you must remove every reference to it in the configuration. Otherwise, the parent interface continues to use the interface.

For example, consider the following configuration:

```
auto lo
iface lo inet loopback

auto eth0
iface eth0 inet dhcp

auto bond1
iface bond1
    bond-slaves swp2 swp1

auto bond3
iface bond3
    bond-slaves swp8 swp6 swp7

auto br0
iface br0
    bridge-ports swp3 swp5 bond1 swp4 bond3
    bridge-pathcosts  swp3=4 swp5=4 swp4=4
    address 11.0.0.10/24
    address 2001::10/64
```

Notice that bond1 is a member of br0. If bond1 is removed, you must remove the reference to it from the br0 configuration. Otherwise, if you reload the configuration with `ifreload -a`, bond1 is still part of br0.

## MTU Set on a Logical Interface Fails with Error: "Numerical result out of range"

This error occurs when the [MTU](../../Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes/) you are trying to set on an interface is higher than the MTU of the lower interface or dependent interface. Linux expects the upper interface to have an MTU less than or equal to the MTU on the lower interface.

In the example below, the swp1.100 VLAN interface is an upper interface to physical interface swp1. If you want to change the MTU to 9000 on the VLAN interface, you must include the new MTU on the lower interface swp1 as well.

```
auto swp1.100
iface swp1.100
    mtu 9000

auto swp1 
iface swp1  
    mtu 9000
```

## iproute2 batch Command Failures

`ifupdown2` batches `iproute2` commands for performance reasons. A batch command contains `ip -force -batch -` in the error message. The command number that failed is at the end of this line: `Command failed -:1`.

Below is a sample error for the command 1: `link set dev host2 master bridge`. There was an error adding the bond *host2* to the bridge named *bridge* because host2 did not have a valid address.

```
error: failed to execute cmd 'ip -force -batch - [link set dev host2 master bridge
addr flush dev host2
link set dev host1 master bridge
addr flush dev host1
]'(RTNETLINK answers: Invalid argument
Command failed -:1)
warning: bridge configuration failed (missing ports)
```

## "RTNETLINK answers: Invalid argument" Error when Adding a Port to a Bridge

This error can occur when the bridge port does not have a valid hardware address.

This occurs typically when the interface being added to the bridge is an incomplete bond; a bond without slaves is incomplete and does not have a valid hardware address.

## MLAG Peerlink Interface Drops Many Packets

Losing a large number of packets across an MLAG peerlink interface might not be a problem. This can occur to prevent looping of BUM (broadcast, unknown unicast and multicast) packets. For more details, and for information on how to detect these drops, read the [MLAG chapter](../../Layer-2/Multi-Chassis-Link-Aggregation-MLAG/).
