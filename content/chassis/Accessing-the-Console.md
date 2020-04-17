---
title: Accessing the Console
author: Cumulus Networks
weight: 11
aliases:
 - /display/CHASSIS/Accessing-the-Console
 - /display/CHASSIS/Accessing+the+Console

pageID: 7766291
product: Cumulus Chassis
version: "1.0"
imgData: chassis
siteSlug: chassis
---
Each fabric card has 2 RJ45 console ports, one for each of the CPUs.
Each line card also has 2 console ports, one for each CPU that connect
via a USB type A jack - this requires a special cable from Edgecore in
order to access the line card console ports. By default, the console
connects at 115200 baud 8N1.

Once connected to the line card or fabric card's console port, you see
one of the following:

  - The ONIE prompt, if no operating system is installed.
  - The Cumulus Linux prompt, if Cumulus Linux has been installed.

## Line Card Naming Convention

Each line card and fabric card has a default identifier, which is
displayed in the console. The name is one of the following:

  - *lc101*, for the A side ASIC (the left side in the image below) on
    line card 1.
  - *lc102*, for the B side ASIC on line card 1.
  - *lc201*, for the A side ASIC on line card 2.
  - *lc202*, for the B side ASIC on line card 2.
  - *lc301*, for the A side ASIC on line card 3.
  - *lc302*, for the B side ASIC on line card 3.
  - *lc401*, for the A side ASIC on line card 4.
  - *lc402*, for the B side ASIC on line card 4.
  - *lc501*, for the A side ASIC on line card 5.
  - *lc502*, for the B side ASIC on line card 5.
  - *lc601*, for the A side ASIC on line card 6.
  - *lc602*, for the B side ASIC on line card 6.
  - *lc701*, for the A side ASIC on line card 7.
  - *lc702*, for the B side ASIC on line card 7.
  - *lc801*, for the A side ASIC on line card 8.
  - *lc802*, for the B side ASIC on line card 8.
  - *fc101*, for the A side ASIC (the bottom half of the leftmost fabric
    card in the image below) on fabric card 1.
  - *fc102*, for the B side ASIC on fabric card 1.
  - *fc201*, for the A side ASIC on fabric card 2.
  - *fc202*, for the B side ASIC on fabric card 2.
  - *fc301*, for the A side ASIC on fabric card 3.
  - *fc302*, for the B side ASIC on fabric card 3.
  - *fc401*, for the A side ASIC (the top half of the rightmost fabric
    card in the image below) on fabric card 4.
  - *fc402*, for the B side ASIC on fabric card 4.

Note that fabric cards 3 and 4 are installed upside down relative to
fabric cards 1 and 2.

{{% imgOld 0 %}}
