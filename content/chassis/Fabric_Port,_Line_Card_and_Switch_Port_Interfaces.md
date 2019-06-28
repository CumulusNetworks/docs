---
title: 'Fabric Port, Line Card and Switch Port Interfaces'
author: Cumulus Networks
weight: 13
aliases:
 - '/display/CHASSIS/Fabric+Port,+Line+Card+and+Switch+Port+Interfaces'
 - /pages/viewpage.action?pageId=7766298
pageID: 7766298
product: Cumulus Chassis
version: '1.0'
imgData: chassis
siteSlug: chassis
---
Each line card in the chassis contains 64 100G ports, broken down into
32 switch ports, which connect to an external network, and 32 fabric
ports, which connect to the fabric cards. Because each line card has two
Tomahawk ASICs, each line card actually is two switches. On the Backpack
chassis, one ASIC is on the left side of the line card and one is on the
right side; each half of the line card has half of the switch ports and
half of the fabric ports. On the CX-10256-S/OMP-800 chassis, one ASIC is
on the "A" side of the line card and one is on the "B" side.

On the Backpack chassis, Cumulus Linux sees the switch ports in both
sides of the line card as swp1 through swp16. On the CX-10256-S/OMP-800
chassis, each side of the line card has half of the switch ports and
half of the fabric ports. The A side swp ports are numbered swp1-swp16
and the B side swp ports are numbered swp17-swp32, which matches the
physical port labeling on the front of the line card.

However, Cumulus Linux sees the fabric ports as fp0, fp1 and so on until
fp15 on both sides of the line card.

On the Backpack chassis, the fabric cards contain 32 100G fabric ports,
named fp0 through fp31.

On the CX-10256-S/OMP-800 chassis, like the line cards, each fabric card
is actually two switches, with an A side and a B side; the A side is the
side that contains the RJ45 Ethernet management port. Each side of the
fabric card contains 32 100G fabric ports, named fp0 through fp31.

Cumulus Linux and FRR commands interact with fabric port interfaces as
they would with any switch port interface.

You cannot break out the fabric ports into 4x25G, 2x50G, 1x40G or 4x10G
ports, while you can break out the switch ports to 2x50G, 4x25G, 1x40G
or 4x10G as desired.

The fabric ports are configured and brought up automatically. Their
configuration is 100G, full-duplex and MTU 9216, with auto-negotiation
off. The configuration is stored in the
/etc/network/interfaces.d/fabric.intf file.

## <span>Internal Network</span>

All chassis CPUs are connected via an internal management network
comprising a number of 1G switches. This configuration provides a single
external connection to access the eth0 interface on every CPU in the
fabric. On a Backpack chassis, the eth0 interface always shows as UP,
even when no cable is attached.

VLAN 4088 is internal to the chassis and is used for chassis management.
Traffic over this VLAN is never forwarded out of the chassis. An
eth0.4088 interface is created with IPv4 and IPv6 link local addresses
that are based on card type (line or fabric) and slot number; however,
IPv6 is of marginal value because they are link local addresses. Entries
for these addresses are written to the /etc/hosts file by a firstboot
script:

    cumulus@chassis-lc202:~$ cat /etc/hosts
    127.0.0.1 localhost
    ::1 localhost ip6-localhost ip6-loopback
    ff02::1 ip6-allnodes
    ff02::2 ip6-allrouters
     
    127.0.1.1 cumulus-lc101
    ### BEGIN AUTO-ADDED LINES FOR CHASSIS HOSTS
     
    #
    # Hostnames for internal management network
    #
    # Added on Mon Oct 16 22:00:00 UTC 2017 by /usr/lib/cumulus/firstboot.d/10_chassis_hosts.firstboot
    #
     
    # IPv4 Addresses
    169.254.251.1 lc101 lc101.chassis
    169.254.251.2 lc102 lc102.chassis
    169.254.251.3 lc201 lc201.chassis
    169.254.251.4 lc202 lc202.chassis
    169.254.251.5 lc301 lc301.chassis
    169.254.251.6 lc302 lc302.chassis
    169.254.251.7 lc401 lc401.chassis
    169.254.251.8 lc402 lc402.chassis
    169.254.251.9 lc501 lc501.chassis
    169.254.251.10 lc502 lc502.chassis
    169.254.251.11 lc601 lc601.chassis
    169.254.251.12 lc602 lc602.chassis
    169.254.251.13 lc701 lc701.chassis
    169.254.251.14 lc702 lc702.chassis
    169.254.251.15 lc801 lc801.chassis
    169.254.251.16 lc802 lc802.chassis
    169.254.251.33 fc101 fc101.chassis
    169.254.251.34 fc102 fc102.chassis
    169.254.251.35 fc201 fc201.chassis
    169.254.251.36 fc202 fc202.chassis
    169.254.251.37 fc301 fc301.chassis
    169.254.251.38 fc302 fc302.chassis
    169.254.251.39 fc401 fc401.chassis
    169.254.251.40 fc402 fc402.chassis
     
    # IPv6 Addresses
    fe80::101:2 fc101-v6 fc101-v6.chassis
    fe80::102:2 fc102-v6 fc102-v6.chassis
    fe80::201:2 fc201-v6 fc201-v6.chassis
    fe80::202:2 fc202-v6 fc202-v6.chassis
    fe80::301:2 fc301-v6 fc301-v6.chassis
    fe80::302:2 fc302-v6 fc302-v6.chassis
    fe80::401:2 fc401-v6 fc401-v6.chassis
    fe80::402:2 fc402-v6 fc402-v6.chassis
     
    ...

The interface configuration is stored in the
`/etc/network/interfaces.d/chassismgmt.intf` file. See [Chassis Default
Configurations](/chassis/Chassis_Default_Configurations) for the
contents.
