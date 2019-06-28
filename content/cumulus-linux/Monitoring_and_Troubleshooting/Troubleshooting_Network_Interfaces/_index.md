---
title: Troubleshooting Network Interfaces
author: Cumulus Networks
weight: 227
aliases:
 - /display/DOCS/Troubleshooting+Network+Interfaces
 - /pages/viewpage.action?pageId=8362603
pageID: 8362603
product: Cumulus Linux
version: 3.7.7
imgData: cumulus-linux
siteSlug: cumulus-linux
---
The following sections describe various ways you can troubleshoot
`ifupdown2`.

## <span>Enable Logging for Networking</span>

The `/etc/default/networking` file contains two settings for logging:

  - To get `ifupdown2` logs when the switch boots (stored in `syslog`)

  - To enable logging when you run `systemctl [start|stop|reload]
    networking.service`

This file also contains an option for excluding interfaces when you boot
the switch or run ` systemctl start|stop|reload networking.service  `.
You can exclude any interface specified in `/etc/network/interfaces`.
These interfaces do not come up when you boot the switch or
start/stop/reload the networking service.

    cumulus@switch:~$ cat /etc/default/networking
    #
    #
    # Parameters for the /etc/init.d/networking script
    #
    #
     
    # Change the below to yes if you want verbose logging to be enabled
    VERBOSE="no"
     
    # Change the below to yes if you want debug logging to be enabled
    DEBUG="no"
     
    # Change the below to yes if you want logging to go to syslog
    SYSLOG="no"
     
    # Exclude interfaces
    EXCLUDE_INTERFACES=

## <span>Use ifquery to Validate and Debug Interface Configurations</span>

You use `ifquery` to print parsed `interfaces` file entries.

To use `ifquery` to pretty print `iface` entries from the `interfaces`
file, run:

    cumulus@switch:~$ sudo ifquery bond0
    auto bond0
    iface bond0
        address 14.0.0.9/30
        address 2001:ded:beef:2::1/64
        bond-slaves swp25 swp26

Use `ifquery --check` to check the current running state of an interface
within the `interfaces` file. It will return exit code *0* or *1* if the
configuration does not match. The line `bond-xmit-hash-policy layer3+7`
below fails because it should read `bond-xmit-hash-policy layer3+4`.

    cumulus@switch:~$ sudo ifquery --check bond0
    iface bond0
        bond-xmit-hash-policy layer3+7  [fail]
        bond-slaves swp25 swp26         [pass]
        address 14.0.0.9/30             [pass]
        address 2001:ded:beef:2::1/64   [pass]

{{%notice note%}}

`ifquery --check` is an experimental feature.

{{%/notice%}}

Use `ifquery --running` to print the running state of interfaces in the
`interfaces` file format:

    cumulus@switch:~$ sudo ifquery --running bond0
    auto bond0
    iface bond0
        bond-slaves swp25 swp26
        address 14.0.0.9/30
        address 2001:ded:beef:2::1/64

`ifquery --syntax-help` provides help on all possible attributes
supported in the `interfaces` file. For complete syntax on the
`interfaces` file, see `man interfaces` and `man
ifupdown-addons-interfaces`.

You can use `ifquery --print-savedstate` to check the `ifupdown2` state
database. `ifdown` works only on interfaces present in this state
database.

    cumulus@leaf1$ sudo ifquery --print-savedstate eth0  
    auto eth0
    iface eth0 inet dhcp

## <span>Mako Template Errors</span>

An easy way to debug and get details about template errors is to use the
`mako-render` command on your interfaces template file or on
`/etc/network/interfaces` itself.

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

## <span>ifdown Cannot Find an Interface that Exists</span>

If you are trying to bring down an interface that you know exists, use
`ifdown` with the `--use-current-config` option to force `ifdown` to
check the current `/etc/network/interfaces` file to find the interface.
This can solve issues where the `ifup` command issues for that interface
was interrupted before it updated the state database. For example:

    cumulus@switch:~$ sudo ifdown br0
    error: cannot find interfaces: br0 (interface was probably never up ?)
     
    cumulus@switch:~$ sudo brctl show
    bridge name bridge id       STP enabled interfaces
    br0     8000.44383900279f   yes     downlink
                                peerlink
     
    cumulus@switch:~$ sudo ifdown br0 --use-current-config 

## <span>Remove All References to a Child Interface</span>

If you have a configuration with a child interface, whether it's a VLAN,
bond or another physical interface, and you remove that interface from a
running configuration, you must remove every reference to it in the
configuration. Otherwise, the interface continues to be used by the
parent interface.

For example, consider the following configuration:

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

Notice that bond1 is a member of br0. If bond1 is removed, you must
remove the reference to it from the br0 configuration. Otherwise, if you
reload the configuration with `ifreload -a`, bond1 is still part of br0.

## <span>MTU Set on a Logical Interface Fails with Error: "Numerical result out of range"</span>

This error occurs when the
[MTU](Switch_Port_Attributes.html#src-8363026_SwitchPortAttributes-mtu)
you are trying to set on an interface is higher than the MTU of the
lower interface or dependent interface. Linux expects the upper
interface to have an MTU less than or equal to the MTU on the lower
interface.

In the example below, the swp1.100 VLAN interface is an upper interface
to physical interface swp1. If you want to change the MTU to 9000 on the
VLAN interface, you must include the new MTU on the lower interface swp1
as well.

    auto swp1.100 
    iface swp1.100 
        mtu 9000 
     
    auto swp1 
    iface swp1  
        mtu 9000

## <span>iproute2 batch Command Failures</span>

`ifupdown2` batches `iproute2` commands for performance reasons. A batch
command contains `ip -force -batch -` in the error message. The command
number that failed is at the end of this line: `Command failed -:1`.

Below is a sample error for the command 1: `link set dev host2 master
bridge`. There was an error adding the bond *host2* to the bridge named
*bridge* because host2 did not have a valid address.

    error: failed to execute cmd 'ip -force -batch - [link set dev host2 master bridge
    addr flush dev host2
    link set dev host1 master bridge
    addr flush dev host1
    ]'(RTNETLINK answers: Invalid argument 
    Command failed -:1) 
    warning: bridge configuration failed (missing ports) 

## <span>"RTNETLINK answers: Invalid argument" Error when Adding a Port to a Bridge</span>

This error can occur when the bridge port does not have a valid hardware
address.

This can typically occur when the interface being added to the bridge is
an incomplete bond; a bond without slaves is incomplete and does not
have a valid hardware address.

## <span>MLAG Peerlink Interface Drops Many Packets</span>

Losing a large number of packets across an MLAG peerlink interface may
not be a problem. Instead this could be occurring in order to prevent
looping of BUM (broadcast, unknown unicast and multicast) packets. For
more information, and how to detect these drops, read the [MLAG
chapter](Multi-Chassis_Link_Aggregation_-_MLAG.html#src-8362677_Multi-ChassisLinkAggregation-MLAG-drops).
