---
title: What's New in Cumulus VX
author: Cumulus Networks
weight: 11
aliases:
 - /display/VX/What's+New+in+Cumulus+VX
 - /pages/viewpage.action?pageId=5126710
pageID: 5126710
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
Cumulus Networks has made major enhancements for Cumulus VX 3.x to
produce a true learning, testing, and pre-production tool. These
enhancements include:

  - In Cumulus VX 3.4.0, [FRRouting](https://frrouting.org) replaces
    Quagga as the routing suite. The new configuration file
    `/etc/frr/frr.conf` replaces `/etc/quagga/Quagga.conf` and the
    `daemons` file is now located in `/etc/frr/daemons`.

  - Cumulus VX now includes ONIE with `onie-nos-install` support to show
    the installation steps.

  - <span style="color: #212121;"> The VX image comes with a GRUB Menu
    containing ONIE and CL. To simulate the install process on real
    hardware, you can install Cumulus Linux binaries from ONIE. </span>

  - <span style="color: #212121;"> Cumulus VX is a *platform*;
    <span style="color: #212121;"> to report real-world data, </span>
    you can run most of the same monitoring tools
    <span style="color: #212121;"> (such as </span> `sensors`
    <span style="color: #212121;"> , </span> `decode-syseeprom`
    <span style="color: #212121;"> , </span> `smonctl`
    <span style="color: #212121;"> , and </span> `platform-detect`
    <span style="color: #212121;"> ) </span> on the VX that run on
    hardware. </span>

  - <span style="color: #212121;"> Cumulus VX now runs the same packages
    as Cumulus Linux, excluding packages that are specific to the
    networking ASIC. This is as close as you can get to software parity
    with Cumulus Linux. </span>

  - <span style="color: #212121;"> <span style="color: #212121;">
    Cumulus VX is now released alongside Cumulus Linux; as a customer,
    you can use VX images before you roll out newer Cumulus Linux
    releases. </span> </span>
