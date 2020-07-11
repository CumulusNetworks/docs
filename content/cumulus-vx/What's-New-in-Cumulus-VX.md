---
title: What's New in Cumulus VX
author: Cumulus Networks
weight: 11
pageID: 5126710
product: Cumulus VX
version: '3.7'
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
  - The VX image comes with a GRUB Menu
    containing ONIE and CL. To simulate the install process on real
    hardware, you can install Cumulus Linux binaries from ONIE. 
  - Cumulus VX is a *platform*; to report real-world data, you can run most 
    of the same monitoring tools (such as `sensors`, `decode-syseeprom`, 
    `smonctl`, and  `platform-detect`)  on the VX that run on hardware. 
  - Cumulus VX now runs the same packages
    as Cumulus Linux, excluding packages that are specific to the
    networking ASIC. This is as close as you can get to software parity
    with Cumulus Linux. 
  - Cumulus VX is now released alongside Cumulus Linux; as a customer,
    you can use VX images before you roll out newer Cumulus Linux
    releases.
