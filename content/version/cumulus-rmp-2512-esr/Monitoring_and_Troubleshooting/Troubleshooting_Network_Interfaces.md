---
title: Troubleshooting Network Interfaces
author: Cumulus Networks
weight: 99
aliases:
 - /display/RMP25ESR/Troubleshooting+Network+Interfaces
 - /pages/viewpage.action?pageId=5116334
pageID: 5116334
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
The following sections describe various ways you can troubleshoot
`ifupdown2`.

## <span>Enabling Logging for Networking</span>

The `/etc/default/networking` file contains two settings for logging:

  - To get `ifupdown2` logs when the switch boots (stored in `syslog`)

  - To enable logging when you run `service networking
    [start|stop|reload]`

This file also contains an option for excluding interfaces when you boot
the switch or run `service networking start|stop|reload`. You can
exclude any interface specified in `/etc/network/interfaces`. These
interfaces do not come up when you boot the switch or start/stop/reload
the networking service.

    $cat /etc/default/networking
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
    
    # Set to 'yes' if you want to skip ifdown during system reboot
    # and shutdown. This is of interest in large scale interface
    # deployments where you dont want to wait for interface
    # deconfiguration to speed up shutdown/reboot
    SKIP_DOWN_AT_SYSRESET="yes"

## <span>Using ifquery to Validate and Debug Interface Configurations</span>

You use `ifquery` to print parsed `interfaces` file entries.

To use `ifquery` to pretty print `iface` entries from the `interfaces`
file, run:

    cumulus@switch:~$ sudo ifquery swp1
    auto swp1
    iface swp1 inet static
       address 10.168.26.1/24

Use `ifquery --check` to check the current running state of an interface
within the `interfaces` file. It returns exit code *0* or *1* if the
configuration does not match:

    cumulus@switch:~$ sudo ifquery --check swp26
    auto swp1
    iface swp1 inet static                                             [pass]
       address 10.168.26.1/24                                      [pass]

{{%notice note%}}

`ifquery --check` is an experimental feature.

{{%/notice%}}

Use `ifquery --running` to print the running state of interfaces in the
`interfaces` file format:

    cumulus@switch:~$ sudo ifquery --running swp1
    auto swp1
    iface swp1
     address 10.168.26.1/24

`ifquery --syntax-help` provides help on all possible attributes
supported in the `interfaces` file. For complete syntax on the
`interfaces` file, see `man interfaces` and `man
ifupdown-addons-interfaces`.

`ifquery` can dump information in JSON format:

    cumulus@switch:~$ sudo ifquery --format=json swp1
    [
        {
            "auto": true,
            "config": {
                "address": "10.168.26.1/24"
            },
            "addr_method": "static",
            "name": "swp1",
            "addr_family": "inet"
        }
    ]

You can use `ifquery --print-savedstate` to check the `ifupdown2` state
database. `ifdown` works only on interfaces present in this state
database.

``` highlight-python
cumulus@leaf1$ sudo ifquery --print-savedstate eth0  
auto eth0
iface eth0 inet dhcp
```

## <span>Debugging Mako Template Errors</span>

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
    bridge name  bridge id       STP enabled interfaces
    br0       8000.44383900279f   yes     downlink
                                peerlink
    
    cumulus@switch:~$ sudo ifdown br0 --use-current-config 

## <span>MTU Set on a Logical Interface Fails with Error: "Numerical result out of range"</span>

This error occurs when the MTU you are trying to set on an interface is
higher than the MTU of the lower interface or dependent interface. Linux
expects the upper interface to have an MTU less than or equal to the MTU
on the lower interface.

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

## <span>Interpreting iproute2 batch Command Failures</span>

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

## <span>Understanding the "RTNETLINK answers: Invalid argument" Error when Adding a Port to a Bridge</span>

This error can occur when the bridge port does not have a valid hardware
address.

This can typically occur when the interface being added to the bridge is
an incomplete bond; a bond without slaves is incomplete and does not
have a valid hardware address.
