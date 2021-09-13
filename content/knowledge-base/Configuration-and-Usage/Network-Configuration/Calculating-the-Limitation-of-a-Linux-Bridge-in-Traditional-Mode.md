---
title: Calculating the Limitation of a Linux Bridge in Traditional Mode
author: NVIDIA
weight: 391
toc: 4
---

This article covers where the 200 VLAN limit for a Linux bridge in traditional mode comes from, and why a user might want to use the VLAN-aware bridge. Comparisons of VLAN-aware versus traditional mode bridges are available {{<link url="Compare-Traditional-Bridge-Mode-to-VLAN-aware-Bridge-Mode" text="here">}}.

## Interface Scale

Through testing, the soft limit for configured interfaces (including subinterfaces, bridges, VXLANs, and so forth) is around 9600. Above 9600, the boot time increases; however, as the acceptable boot time is up to the operator, this is only a soft limit. While the limit is not unique to Cumulus Linux, NVIDIA tested various NVIDIA-supported switches with various processors and RAM.

## Configured Interfaces

Configured interfaces include:

- Subinterfaces (swp1.5, swp1.10, swp1.30)
- Bridges
- VXLANs

{{%notice note%}}

As the bridge in traditional mode has no concept of VLANs, it has to use subinterfaces to tag traffic to 802.1q compliance, so any interface configured with `auto` and `inet` in `/etc/network/interfaces` gets counted.

{{%/notice%}}

## The 200 VLAN Limit

The limit of 200 VLANs derives from the scenario when a user configures all 48 ports of a leaf switch as trunks, reaching the interface soft limit of 9600 (48\*200=9600).

The interface equation is:

*(VLANS\*INTERFACES)* + *VLANS* + *VXLANS* + *1 eth0* + *1 LO* = *INTERFACES*

For example:

    (200*48) + 200 + 0 + 1 + 1 = 9802

This equation is close enough to the 9600 soft limit to not affect the boot time.

However, it is possible to configure a setup using more than 200 VLANs. For example, if you configure swp1-20 with 200 VLANs total, and swp21-40 have a separate set of 200 VLANs, then you have a total of 400 VLANs, while the total ports is only 40. This is technically within the limit (as shown in the equation below), even though the number of bridges is double the recommended maximum:

    (20 swp * 200 VLANs) + (20 swp * 200 VLANs) + 400 VLANs + 0 VXLANs + 1 eth0 + 1 lo = 8402

### Example One

#### Requirements

One trunk (physical port), with two VLANs each. It does not require any VXLANs.

#### Equation

    (2 * 1) + 2 + 0 + 1 + 1 = 6 interfaces

The example below shows the configuration:

    auto lo
    iface lo inet loopback
    
    auto eth0
    iface eth0 inet dhcp
    
    auto swp1.10
    iface swp1.10
    
    auto swp1.20
    iface swp1.20
    
    bridge br-10
    iface br-10
      bridge-ports swp1.10
    
    bridge br-20
    iface br-20
      bridge-ports swp1.20

### Example Two

#### Requirements

Two trunks (physical ports) with three VLANs and one VXLAN.

#### Equation

    (3 * 2) + 3 + 1 + 1 + 1 = 12 interfaces

The example below shows the configuration:

    auto lo
    iface lo inet loopback
    
    auto eth0
    iface eth0 inet dhcp
    
    auto swp1.10
    iface swp1.10
    
    auto swp1.20
    iface swp1.20
    
    auto swp1.30
    iface swp1.30
    
    auto swp2.10
    iface swp2.10
    
    auto swp2.20
    iface swp2.20
    
    auto swp2.30
    iface swp2.30
    
    auto br-10
    iface br-10
      bridge_ports swp1.10 swp2.10
    
    auto br-20
    iface br-20
      bridge_ports swp1.20 swp2.20
    
    auto br-30
    iface br-30
      bridge_ports swp1.30 swp2.30
    
    auto VXLAN10
    iface VXLAN10
      vxlan-id 10

## Additional Information

{{%notice note%}}

A requirement of 2000 VLANs on all 52 ports does not work, as it takes too long to boot.

    (2000*52) + 2000 + 0 + 1 + 1 = 106,002

{{%/notice%}}

The Linux bridge in VLAN-aware mode uses a single bridge with VLANs configured in the bridge, which means that it only counts towards one configured interface (out of the maximum of 9600). This means that you  can configure thousands of VLANs, while only using one of the 9600 interfaces, before the boot time increases. This approach is much more scalable if you are using 200 or more VLANs, and is also easy to configure with {{<exlink url="https://github.com/CumulusNetworks/ifupdown2" text="ifupdown2">}} or [NCLU]({{<ref "/cumulus-linux-43/System-Configuration/Network-Command-Line-Utility-NCLU" >}}).
