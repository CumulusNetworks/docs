---
title: Chassis Default Configurations
author: Cumulus Networks
weight: 15
aliases:
 - /display/CHASSIS/Chassis+Default+Configurations
 - /pages/viewpage.action?pageId=7113477
pageID: 7113477
product: Cumulus Chassis
version: '1.0'
imgData: chassis
siteSlug: chassis
---
A number of configuration files are automatically applied to all the
nodes in the chassis the first time you boot it after installing Cumulus
Linux on the nodes. These following actions are also performed:

  - Enable Zebra and `bgpd` for FRR in the `/etc/frr/daemons` file.

  - Create the default FRR configuration in the `/etc/frr/frr.conf`
    file; iBGP is used. The default configuration uses the ASN
    *4242424242* to make it easy to recognize. The router ID is set to
    *42.42.42.\<slot number\>*. Line cards redistribute connected routes
    and fabric cards are route reflectors.

  - Enable and start the `cumulus-chassisd` service.

  - Edit the `/etc/hosts` file to add host names for the IPv4 and IPv6
    link local addresses that are assigned to the eth0.4088 interfaces
    of all CPUs in the chassis.

  - Enable and start the `cumulus-chassis-ssh` service. This service
    provides for SSH from one chassis card to another without a
    password.

  - Create the following two files in the `/etc/network/interfaces.d`
    directory, which are sourced by the `/etc/network/interfaces` file:
    
      - The first file — called `chassismgmt.intf` — creates the
        eth0.4088 interface and assigns it IPv4 and IPv6 link local
        addresses via a post-up script. This interface is used for
        intra-chassis communication.
    
      - The second file — called `fabric.intf` — configures the fabric
        interfaces. It uses Mako templates to iterate over all of the
        fabric interfaces and set the interface properties. The
        parameters of the `range` function vary, depending on whether
        the file is installed on a fabric card or a line card. See the
        default configuration files below for the content of all of
        these files.

You can modify these files to suit your needs after the chassis is
running.

## <span>Default Routing Configuration</span>

The chassis has a default routing configuration that uses
[FRRouting](https://frrouting.org/) (FRR). You can modify this
configuration to suit your needs. The configuration includes:

  - Unnumbered iBGP

  - Redistribute connected routes on the line cards and route reflectors

FRR can pass routes from one line card to another.

A firstboot script alters the `/etc/frr/daemons` file to enable zebra
and BGP; the script also alters `/etc/frr/frr.conf` to enable the
example configuration, where the ASN is *4242424242* and the router ID
is *42.42.42.\<slot\>*.

The default `frr.conf` file contents for fabric cards and line cards for
each type of chassis appears below.

### <span>Backpack VRF Automatic Configurations</span>

On a Backpack chassis, VRFs created on a line card are automatically
propagated throughout the fabric, so you don't have to configure the
same VRF on each node in the fabric individually. The VRFs are also
added to the FRR configuration.

You need to choose which interfaces to enslave. Fabric VLAN
subinterfaces are enslaved to the VRF and are named something like
fp.1000. You won’t see much as the VRFs just pass traffic through them;
there are no available ports to access it.

You can disable this automatic configuration by doing the following:

1.  Copy `cumulus-chassisd.service` to `/etc/systemd/system`:
    
        cumulus@backpack-lc202:~$ sudo cp /lib/systemd/system/cumulus-chassisd.service /etc/systemd/system

2.  Edit the `/etc/systemd/system/cumulus-chassisd.service` file, adding
    the `--noAutoVrf` option on the ExecStart line:
    
        cumulus@backpack-lc202:~$ sudo nano /etc/systemd/system/cumulus-chassisd.service…[Service]Type=simpleSyslogIdentifier=chassisdExecStart=/usr/sbin/cumulus-chassisd --noAutoVrf...

3.  Reload the daemon file and restart `cumulus-chassisd.service`:
    
        cumulus@backpack-lc202:~$ sudo systemctl daemon-reloadcumulus@backpack-lc202:~$ sudo systemctl restart cumulus-chassisd.service

### <span>Avoid Layer 2 Networks</span>

The chassis is not a layer 2 device. Connections between line cards and
fabric cards don't lend themselves well to a layer 2 network. You cannot
create a bridge between the 2 CPUs in a line card, so while the one
side's ports are for one CPU and can be in a bridge, the other side's
ports cannot be members of that bridge.

If you need to extend a layer 2 network between two line cards, use
VXLANs with EVPN, for example. See the Cumulus Linux user guide for
details.

## <span>Facebook Backpack Default Configurations</span>

### <span>interfaces File</span>

The `/etc/network/interfaces` file has the same content on both line
cards and fabric cards.

    cumulus@backpack-lc102:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    source /etc/network/interfaces.d/*.intf
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
     
    iface usb0 inet dhcp

### <span>chassismgmt.intf File</span>

The `/etc/network/interfaces.d/chassismgmt.intf` file has the same
content on both line cards and fabric cards.

    cumulus@backpack-lc102:~$ cat /etc/network/interfaces.d/chassismgmt.intf 
    #
    # This file contains the interface configuration of the chassis management VLAN
    # interface. The traffic on this VLAN is not ever forwarded out of the chassis.
    #
     
    auto eth0.4088
    iface eth0.4088
        post-up /usr/lib/cumulus/setchassismgmtipaddr $IFACE

### <span>fabric.intf File</span>

The `/etc/network/interfaces.d/fabric.intf` file has the same content on
both line cards and fabric cards, with one exception: on a fabric card
the range of interfaces is *0,32*, while the range of interfaces on a
line card is *0,16*.

    cumulus@backpack-lc102:~$ cat /etc/network/interfaces.d/fabric.intf 
    #
    # This file contains the interface configuration of the fabric ports. All fabric
    # ports are brought up.
    #
     
    #
    # The defaults for fabric interfaces
    #
    <%def name="fabric_defaults()">
        link-speed 100000
        link-duplex full
        link-autoneg off
        mtu 9216
    </%def>
     
    #
    # All of the fabric interfaces
    #
    % for i in range(0,16):
    auto fp${i}
    iface fp${i}
    ${fabric_defaults()}
    % endfor

### <span>frr.conf File on a Fabric Card</span>

    cumulus@backpack-fc4:~$ cat /etc/frr/frr.conf
    log file /var/log/frr/frr.log
    log timestamp precision 6
    !!! BEGIN AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION
    !
    ! Default Chassis Fabric configuration
    !
    ! Added on Mon Jul 24 21:50:32 UTC 2017 by /usr/lib/cumulus/firstboot.d/10_chassis_frr.firstboot
    !
    router bgp 4242424242
     bgp router-id 42.42.42.4
     neighbor FABRIC peer-group
     neighbor FABRIC remote-as internal
     neighbor fp0 interface peer-group FABRIC
     neighbor fp1 interface peer-group FABRIC
     neighbor fp2 interface peer-group FABRIC
     neighbor fp3 interface peer-group FABRIC
     neighbor fp4 interface peer-group FABRIC
     neighbor fp5 interface peer-group FABRIC
     neighbor fp6 interface peer-group FABRIC
     neighbor fp7 interface peer-group FABRIC
     neighbor fp8 interface peer-group FABRIC
     neighbor fp9 interface peer-group FABRIC
     neighbor fp10 interface peer-group FABRIC
     neighbor fp11 interface peer-group FABRIC
     neighbor fp12 interface peer-group FABRIC
     neighbor fp13 interface peer-group FABRIC
     neighbor fp14 interface peer-group FABRIC
     neighbor fp15 interface peer-group FABRIC
     neighbor fp16 interface peer-group FABRIC
     neighbor fp17 interface peer-group FABRIC
     neighbor fp18 interface peer-group FABRIC
     neighbor fp19 interface peer-group FABRIC
     neighbor fp20 interface peer-group FABRIC
     neighbor fp21 interface peer-group FABRIC
     neighbor fp22 interface peer-group FABRIC
     neighbor fp23 interface peer-group FABRIC
     neighbor fp24 interface peer-group FABRIC
     neighbor fp25 interface peer-group FABRIC
     neighbor fp26 interface peer-group FABRIC
     neighbor fp27 interface peer-group FABRIC
     neighbor fp28 interface peer-group FABRIC
     neighbor fp29 interface peer-group FABRIC
     neighbor fp30 interface peer-group FABRIC
     neighbor fp31 interface peer-group FABRIC
    !
     address-family ipv4 unicast
      neighbor FABRIC route-reflector-client
     exit-address-family
    !
     address-family ipv6 unicast
      neighbor FABRIC activate
      neighbor FABRIC route-reflector-client
     exit-address-family
    !
    !!! END AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION

### <span>frr.conf File on a Line Card</span>

    cumulus@backpack-lc102:~$ cat /etc/frr/frr.conf
    log file /var/log/frr/frr.log
    log timestamp precision 6
    !!! BEGIN AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION
    !
    ! Default Chassis Fabric configuration
    !
    ! Added on Mon Jul 24 21:50:40 UTC 2017 by /usr/lib/cumulus/firstboot.d/10_chassis_frr.firstboot
    !
    router bgp 4242424242
     bgp router-id 42.42.42.6
     neighbor FABRIC peer-group
     neighbor FABRIC remote-as internal
     neighbor fp0 interface peer-group FABRIC
     neighbor fp1 interface peer-group FABRIC
     neighbor fp2 interface peer-group FABRIC
     neighbor fp3 interface peer-group FABRIC
     neighbor fp4 interface peer-group FABRIC
     neighbor fp5 interface peer-group FABRIC
     neighbor fp6 interface peer-group FABRIC
     neighbor fp7 interface peer-group FABRIC
     neighbor fp8 interface peer-group FABRIC
     neighbor fp9 interface peer-group FABRIC
     neighbor fp10 interface peer-group FABRIC
     neighbor fp11 interface peer-group FABRIC
     neighbor fp12 interface peer-group FABRIC
     neighbor fp13 interface peer-group FABRIC
     neighbor fp14 interface peer-group FABRIC
     neighbor fp15 interface peer-group FABRIC
    !
     address-family ipv4 unicast
      distance bgp 20 19 1
      redistribute connected
     exit-address-family
    !
     address-family ipv6 unicast
      neighbor FABRIC activate
      distance bgp 20 19 1
      redistribute connected
     exit-address-family
    !
    !!! END AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION

### <span>ports.conf File on a Line Card</span>

    cumulus@backpack-lc102:~$ cat /etc/cumulus/ports.conf 
    # ports.conf --
    #
    # The Celestica BigStone-G Right Linecard has:
    #
    #     16 QSFP28 ports numbered 1-16
    #     These ports are configurable as 100G, 50G, 40G, 2x50G, 4x25G, 4x10G
    #     or disabled.
    #
    # If you make changes to this file, you must restart switchd for the
    # changes to take effect.
     
    # QSFP28 ports
    #
    # <port label 1-16> = [4x10G|4x25G|2x50G|40G|50G|100G|disabled]
    1=100G
    2=100G
    3=100G
    4=100G
    5=100G
    6=100G
    7=100G
    8=100G
    9=100G
    10=100G
    11=100G
    12=100G
    13=100G
    14=100G
    15=100G
    16=100G

{{%notice info%}}

The Facebook Backpack fabric card has no user configurable ports, so the
`ports.conf` file has no content.

{{%/notice%}}

## <span>Celestica OMP-800 Default Configurations</span>

### <span>interfaces File</span>

The `/etc/network/interfaces` file has the same content on both line
cards and fabric cards.

    cumulus@omp-800-fc402:~$ cat /etc/network/interfaces
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).
     
    source /etc/network/interfaces.d/*.intf
     
    # The loopback network interface
    auto lo
    iface lo inet loopback
     
    # The primary network interface
    auto eth0
    iface eth0 inet dhcp
     
    iface eth1 inet dhcp
     
    iface eth2 inet dhcp

### <span>chassismgmt.intf File</span>

The `/etc/network/interfaces.d/chassismgmt.intf` file has the same
content on both line cards and fabric cards.

    cumulus@omp-800-fc402:~$ cat /etc/network/interfaces.d/chassismgmt.intf 
    #
    # This file contains the interface configuration of the chassis management VLAN
    # interface. The traffic on this VLAN is not ever forwarded out of the chassis.
    #
     
    auto eth0.4088
    iface eth0.4088
        post-up /usr/lib/cumulus/setchassismgmtipaddr $IFACE

### <span>fabric.intf File</span>

The `/etc/network/interfaces.d/fabric.intf` file has the same content on
both line cards and fabric cards, with one exception: on a fabric card
the range of interfaces is *0,32*, while the range of interfaces on a
line card is *0,16*.

    cumulus@omp-800-fc402:~$ cat /etc/network/interfaces.d/fabric.intf 
    #
    # This file contains the interface configuration of the fabric ports. All fabric
    # ports are brought up.
    #
     
    #
    # The defaults for fabric interfaces
    #
    <%def name="fabric_defaults()">
        link-speed 100000
        link-duplex full
        link-autoneg off
        mtu 9216
    </%def>
     
    #
    # All of the fabric interfaces
    #
    % for i in range(0,32):
    auto fp${i}
    iface fp${i}
    ${fabric_defaults()}
    % endfor

### <span>frr.conf File on a Fabric Card</span>

    cumulus@omp-800-fc402:~$ cat /etc/frr/frr.conf 
    # default to using syslog. /etc/rsyslog.d/45-frr.conf places the log
    # in /var/log/frr/frr.log
    log syslog informational
    !!! BEGIN AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION
    !
    ! Default Chassis Fabric configuration
    !
    ! Added on Wed Jan  3 16:57:00 UTC 2018 by /usr/lib/cumulus/firstboot.d/10_chassis_frr.firstboot
    !
    router bgp 4242424242
     bgp router-id 42.42.42.40
     neighbor FABRIC peer-group
     neighbor FABRIC remote-as internal
     neighbor fp0 interface peer-group FABRIC
     neighbor fp1 interface peer-group FABRIC
     neighbor fp2 interface peer-group FABRIC
     neighbor fp3 interface peer-group FABRIC
     neighbor fp4 interface peer-group FABRIC
     neighbor fp5 interface peer-group FABRIC
     neighbor fp6 interface peer-group FABRIC
     neighbor fp7 interface peer-group FABRIC
     neighbor fp8 interface peer-group FABRIC
     neighbor fp9 interface peer-group FABRIC
     neighbor fp10 interface peer-group FABRIC
     neighbor fp11 interface peer-group FABRIC
     neighbor fp12 interface peer-group FABRIC
     neighbor fp13 interface peer-group FABRIC
     neighbor fp14 interface peer-group FABRIC
     neighbor fp15 interface peer-group FABRIC
     neighbor fp16 interface peer-group FABRIC
     neighbor fp17 interface peer-group FABRIC
     neighbor fp18 interface peer-group FABRIC
     neighbor fp19 interface peer-group FABRIC
     neighbor fp20 interface peer-group FABRIC
     neighbor fp21 interface peer-group FABRIC
     neighbor fp22 interface peer-group FABRIC
     neighbor fp23 interface peer-group FABRIC
     neighbor fp24 interface peer-group FABRIC
     neighbor fp25 interface peer-group FABRIC
     neighbor fp26 interface peer-group FABRIC
     neighbor fp27 interface peer-group FABRIC
     neighbor fp28 interface peer-group FABRIC
     neighbor fp29 interface peer-group FABRIC
     neighbor fp30 interface peer-group FABRIC
     neighbor fp31 interface peer-group FABRIC
    !
     address-family ipv4 unicast
      neighbor FABRIC route-reflector-client
     exit-address-family
    !
     address-family ipv6 unicast
      neighbor FABRIC activate
      neighbor FABRIC route-reflector-client
     exit-address-family
    !
    !!! END AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION

### <span>frr.conf File on a Line Card</span>

    cumulus@omp-800-lc102:~$ cat /etc/frr/frr.conf 
    # default to using syslog. /etc/rsyslog.d/45-frr.conf places the log
    # in /var/log/frr/frr.log
    log syslog informational
    !!! BEGIN AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION
    !
    ! Default Chassis Fabric configuration
    !
    ! Added on Wed Jan  3 16:56:46 UTC 2018 by /usr/lib/cumulus/firstboot.d/10_chassis_frr.firstboot
    !
    router bgp 4242424242
     bgp router-id 42.42.42.2
     neighbor FABRIC peer-group
     neighbor FABRIC remote-as internal
     neighbor fp0 interface peer-group FABRIC
     neighbor fp1 interface peer-group FABRIC
     neighbor fp2 interface peer-group FABRIC
     neighbor fp3 interface peer-group FABRIC
     neighbor fp4 interface peer-group FABRIC
     neighbor fp5 interface peer-group FABRIC
     neighbor fp6 interface peer-group FABRIC
     neighbor fp7 interface peer-group FABRIC
     neighbor fp8 interface peer-group FABRIC
     neighbor fp9 interface peer-group FABRIC
     neighbor fp10 interface peer-group FABRIC
     neighbor fp11 interface peer-group FABRIC
     neighbor fp12 interface peer-group FABRIC
     neighbor fp13 interface peer-group FABRIC
     neighbor fp14 interface peer-group FABRIC
     neighbor fp15 interface peer-group FABRIC
    !
     address-family ipv4 unicast
      distance bgp 20 19 1
      redistribute connected
     exit-address-family
    !
     address-family ipv6 unicast
      neighbor FABRIC activate
      distance bgp 20 19 1
      redistribute connected
     exit-address-family
    !
    !!! END AUTO-ADDED LINES FOR CHASSIS FABRIC CONFIGURATION

### <span>ports.conf File on a Line Card</span>

The `ports.conf` file has different contents depending on whether the
line card is even or odd-numbered. Here is the configuration for line
card 1:

    cumulus@omp-800-lc101:~$ cat /etc/cumulus/ports.conf 
    # ports.conf --
    #
    # The Accton OMP800 Linecard A has:
    #
    #     16 QSFP28 ports numbered 1-16
    #     These ports are configurable as 100G, 50G, 40G, 2x50G, 4x25G, 4x10G
    #     or disabled.
    #
    # If you make changes to this file, you must restart switchd for the
    # changes to take effect.
     
    # QSFP28 ports
    #
    # <port label 1-16> = [4x10G|4x25G|2x50G|40G|50G|100G|disabled]
    1=100G
    2=100G
    3=100G
    4=100G
    5=100G
    6=100G
    7=100G
    8=100G
    9=100G
    10=100G
    11=100G
    12=100G
    13=100G
    14=100G
    15=100G
    16=100G

Here is the configuration for line card 2:

    cumulus@omp-800-lc102:~$ cat /etc/cumulus/ports.conf 
    # ports.conf --
    #
    # The Accton OMP800 Linecard B has:
    #
    #     16 QSFP28 ports numbered 17-32
    #     These ports are configurable as 100G, 50G, 40G, 2x50G, 4x25G, 4x10G
    #     or disabled.
    #
    # If you make changes to this file, you must restart switchd for the
    # changes to take effect.
     
    # QSFP28 ports
    #
    # <port label 17-32> = [4x10G|4x25G|2x50G|40G|50G|100G|disabled]
    17=100G
    18=100G
    19=100G
    20=100G
    21=100G
    22=100G
    23=100G
    24=100G
    25=100G
    26=100G
    27=100G
    28=100G
    29=100G
    30=100G
    31=100G
    32=100G

{{%notice info%}}

The Accton OMP800 **fabric card** has no user configurable ports, so the
`ports.conf` file has no content.

{{%/notice%}}
