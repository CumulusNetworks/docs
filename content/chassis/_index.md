---
title: Chassis User Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/CHASSIS/Chassis-User-Guide
 - /display/CHASSIS/Chassis+User+Guide
 - /pages/viewpage.action?pageId=6488345
pageID: 6488345
product: Cumulus Chassis
version: '1.0'
imgData: chassis
siteSlug: chassis
subsection: true
---
The Cumulus Express chassis is a self-contained Clos network in a single
chassis form factor. The chassis available currently is the Cumulus
Express CX-10256-S chassis, also known as the Edgecore OMP-800 chassis.

{{%notice warning%}}

These chassis only run Cumulus Linux 3.x; they cannot run Cumulus Linux 4.0.0 or later.

{{%/notice%}}

The chassis is like a 16 leaf/8 spine Clos network in a single 10RU
housing. The chassis comprises a number of components. The components
pertinent to this guide are:

  - 8 line cards, each with 2 Tomahawk ASICs, 2 Intel Atom C2538 4 core
    2.40GHz CPUs, and 32 100G fabric ports. The line cards are similar
    to leaf switches in a Clos network. Each line card runs 2 instances
    of Cumulus Linux, one for each ASIC. In the image below, the line
    cards are in the middle of the chassis, flanked by two fabric cards
    on each side. Line card 1 is at the top of the image and line card 8
    is at the bottom.
  - 4 fabric cards, each with 2 Tomahawk ASICs, 2 Intel Atom C2538 4
    core 2.40GHz CPUs, and 32 100G fabric ports. Fabric cards are
    similar to spine switches in a Clos network, although the fabric
    cards do not connect to nodes outside the chassis. Each fabric card
    runs 2 instances of Cumulus Linux, one for each ASIC. The fabric
    cards flank the line cards in the image below. Fabric card 1 is the
    leftmost card and fabric card 4 is the rightmost card.
  - 16 fan modules, accessible from the rear.
  - All line cards, fabric cards and power supplies are accessible from
    the front.
  - All CPUs are located on their respective line or fabric cards. There
    are no chassis management modules (CMMs), system control modules
    (SCMs) or baseboard management controllers (BMCs).

In addition, the chassis contains horizontal and vertical control
planes, a bus bar assembly, a fan control board, 6 power supply units
(PSUs) and a power distribution board (PDB), but this is all beyond the
scope of this guide.

The chassis fits into a 21" rack that is 10 RU in height.

{{% imgOld 0 %}}
