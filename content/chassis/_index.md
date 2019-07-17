---
title: Chassis User Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/CHASSIS/Chassis-User-Guide
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

## <span>Recent activity</span>

  - [![/images/download/attachments/1704089/pete-27211-pp-profilepic.jpg](/images/download/attachments/1704089/pete-27211-pp-profilepic.jpg)](https://docs.cumulusnetworks.com/display/~pete)
    
    [Pete Bratach](https://docs.cumulusnetworks.com/display/~pete)

  - [Fabric Port, Line Card and Switch Port
    Interfaces](/version/chassis/Fabric-Port-Line-Card-and-Switch-Port-Interfaces)updated
    Jul 02, 2019[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7766298&selectedPageVersions=2&selectedPageVersions=1)

  - [Chassis Default
    Configurations](/version/chassis/Chassis-Default-Configurations)updated
    Jul 02, 2019[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7113477&selectedPageVersions=9&selectedPageVersions=8)

  - [Monitoring and Troubleshooting a
    Chassis](/version/chassis/Monitoring-and-Troubleshooting-a-Chassis)updated
    Jul 02, 2019[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7113871&selectedPageVersions=5&selectedPageVersions=4)

  - [Chassis-specific
    Commands](/version/chassis/Chassis-specific-Commands)updated Jul 02,
    2019[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7766308&selectedPageVersions=2&selectedPageVersions=1)

  - [Accessing the
    Console](/version/chassis/Accessing-the-Console)updated Jul 02,
    2019[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7766291&selectedPageVersions=4&selectedPageVersions=3)

[Show
More](https://docs.cumulusnetworks.com/plugins/recently-updated/changes.action?theme=social&pageSize=5&startIndex=5&searchToken=78349&spaceKeys=CHASSIS&contentType=page,%20comment,%20blogpost)

![/images/s/en\_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.241/\_/images/icons/wait.gif](/images/s/en_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.241/_/images/icons/wait.gif)  
<span class="caption">Please wait</span>

## <span>Space contributors</span>

  - [Pete Bratach](https://docs.cumulusnetworks.com/display/~pete) (8
    days ago)

  - [Dan Cawley](https://docs.cumulusnetworks.com/display/~dcawley) (58
    days ago)

<article id="html-search-results" class="ht-content" style="display: none;">

</article>

<footer id="ht-footer">

</footer>
