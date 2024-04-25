---
title: Link on Physical Switch Port Does not Come Up
author: NVIDIA
weight: 413
toc: 4
---

## Issue

The link on a physical switch port &mdash; an interface starting with "swp" &mdash; does not come up.

## Environment

- Cumulus Linux, all versions

## Resolution

Here is a list of things to check:

### Ensure Your Cumulus Linux License Is Valid

Until you install a valid Cumulus Linux license, none of the physical switch ports come up, so they do not appear in the output of `ip link show`.

    $ sudo cl-license
    No license installed!

Read {{<link url="Physical-Ports-Missing-from-ip-link-show-Output-switchd-Failure" text="this article">}} for additional details on how to address this.

### Bring the Link Up with ip link set

Check the output of `ip link show`, you should see the following:

- Physical state: UP
- Admin state: UP
- LOWER\_UP

    cumulus@switch$ ip link show swp1
    3: swp1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc pfifo_fast state UP mode DEFAULT qlen 500
       link/ether c4:54:44:4f:ab:00 brd ff:ff:ff:ff:ff:ff

If the physical switch port shows as DOWN instead of UP, configure the interface to be UP with the `ip link set` command:

    cumulus@switch$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST> mtu 9000 qdisc pfifo_fast master vlan5 state DOWN mode DEFAULT qlen 500 
        link/ether c4:54:44:4f:ab:00 brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ sudo ip link set swp3 up  
    cumulus@switch$ ip link show swp3
    5: swp3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc pfifo_fast master vlan5 state UP mode DEFAULT qlen 500 
        link/ether c4:54:44:4f:ab:00 brd ff:ff:ff:ff:ff:ff

To make this persistent after reboot so the port is up, define the swp in the `/etc/network/interfaces` file (using `net add interface swp3 link up`); you can also automate this with Mako, as documented in {{<link url="Configure-the-interfaces-File-with-Mako" text="this article">}}.

    cumulus@switch$ net add interface swp3 link up
    cumulus@switch$ net commit

### Ensure Physical Connections Are Good

In the output of `ip link show`, if you see NO\_CARRIER instead of LOWER\_UP, there is no physical link.

    cumulus@switch$ ip link show swp21
    23: swp21: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 9000 qdisc pfifo_fast master vlan5 state DOWN mode DEFAULT qlen 500
        link/ether c4:54:44:4f:ab:12 brd ff:ff:ff:ff:ff:ff

Check your connections, reseat the pluggable and verify cables.

### Explicitly Configure the Port Speed, Duplex Mode, Auto Negotiation Settings

You might need to explicitly configure the physical switch port attributes, especially in scenarios where ports might allow different types of pluggables or where someone reconfigured the attribute. The following attributes might need to be explicitly configured:

- link-speed
- link-duplex
- link-autoneg

For example, you can configure the following in `/etc/network/interfaces`:

    auto swp1
    iface swp1   
        address 10.1.1.1/24   
        mtu 9000  
        link-speed 10000
        link-duplex full
        link-autoneg off

Note that if the interface name starts with swp and ends with \_sX, where X is a number between 0 and 3, then this is a 10G connection in a breakout Twinax or AOC cable.

    cumulus@switch$ ip link show swp32s0
    37: swp32s0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT qlen 500 
        link/ether 00:e0:ec:27:ab:9b brd ff:ff:ff:ff:ff:ff
    cumulus@switch$ grep swp32s0 /var/lib/cumulus/porttab 
    swp32s0 xe34    0   0
    cumulus@switch$ grep xe34 /etc/bcm.d/config.bcm 
    port_init_speed_xe34=10000
    port_init_autoneg_xe34=0
    serdes_if_type_xe34=9

Read [Switch Port Attributes]({{<ref "/cumulus-linux-43/Layer-1-and-Switch-Ports/Interface-Configuration-and-Management/Switch-Port-Attributes" >}}) for more details on how to configure the physical switch port attributes.

### Validate Hardware Settings with ethtool

The `ethtool` command enables you to query or control the network driver and hardware settings. It takes the device name (like swp1) as an argument, for example:

    cumulus@switch$ ethtool swp1

    cumulus@switch$ sudo ethtool -m swp1

Read [Monitoring Interfaces and Transceivers Using ethtool]({{<ref "/cumulus-linux-43/Monitoring-and-Troubleshooting/Troubleshooting-Network-Interfaces/Monitoring-Interfaces-and-Transceivers-Using-ethtool" >}}) for more details on `ethtool`.
<!-- vale off -->
### Force the Interface Configurations to Be Pushed to Hardware
<!-- vale on -->
Ensure the configuration in `/etc/network/interfaces` gets pushed to hardware. Run the following command:

    cumulus@switch$ sudo ifreload -a
