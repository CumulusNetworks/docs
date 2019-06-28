---
title: Chassis User Guide
author: Cumulus Networks
weight: 1
aliases:
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
chassis form factor. There are two different types of chassis available
currently:

  - Cumulus Express Backpack chassis

  - Cumulus Express CX-10256-S chassis, also known as the Edgecore
    OMP-800 chassis

## <span>Getting to Know the Chassis</span>

Each chassis type differs somewhat from the other.

### <span>About the Backpack Chassis</span>

The Backpack chassis is like an 8 leaf/4 spine Clos network in a single
chassis, so it's more complex than configuring Cumulus Linux on a single
top of rack switch. This guide walks you through the details to get you
up and running.

Backpack comprises a number of components. The components pertinent to
this guide are:

  - 2 chassis management modules (CMMs), one primary and one standby.
    It's a good idea to connect cables to both CMMs; in the event the
    primary CMM is removed, the standby takes its place. Otherwise, the
    standby CMM is idle; it can get link but won't receive any traffic.

  - 4 line cards, each with two Tomahawk ASICs and 32 100G ports each.
    The line cards are similar to leaf switches in a Clos network. Each
    line card runs 2 instances of Cumulus Linux, one for each ASIC. In
    the image below, the line cards are labeled LC1, LC2, LC3 and LC4
    from top to bottom; the left half of each line card has a white
    silkscreen around the ports, while the right half has a black
    silkscreen.

  - 4 fabric cards, each with a Tomahawk ASIC and 32 100G fabric ports.
    Fabric cards are similar to spine switches in a Clos network,
    although the fabric cards do not connect to nodes outside the
    chassis. Each fabric card runs 1 instance of Cumulus Linux. The
    fabric cards do not appear in the image below, except for the system
    controller modules that connect to them.

  - 8 system controller modules (SCMs), one for each line card (labeled
    SCM-LC1 through SCM-LC4 in the image below) and one for each fabric
    card (labeled SCM-FC1 through SCM-FC4 in the image below). The SCMs
    are interdependent on their corresponding line or fabric cards, so
    if line card 1 goes down, for example, SCM-LC1 goes down as well.

In addition, Backpack contains horizontal and vertical control planes, a
bus bar assembly, a fan control board, 4 power supply units (PSUs) and a
power distribution board (PDB), but this is all beyond the scope of this
guide.

{{% imgOld 0 %}}

### <span>About the CX-10256-S/OMP-800 Chassis</span>

Both the CX-10256-S/Edgecore OMP-800 chassis are like a 16 leaf/8 spine
Clos network in a single chassis. The chassis comprises a number of
components. The components pertinent to this guide are:

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

In addition, the chassis contains horizontal and vertical control
planes, a bus bar assembly, a fan control board, 6 power supply units
(PSUs) and a power distribution board (PDB), but this is all beyond the
scope of this guide.

The chassis fits into a 21" rack that is 10 RU in height.

{{% imgOld 1 %}}

The CX-10256-S/OMP-800 is essentially a double-sized Backpack chassis;
they all have 2 Tomahawk ASICs and 2 Cumulus Linux instances per line
card.

However, the CX-10256-S and OMP-800 differ from the Backpack chassis in
the following ways:

  - They lack CMMs, SCMs and BMCs. All CPUs are located on their
    respective line or fabric cards.

  - The fabric cards each have 2 Tomahawk ASICs and 2 Cumulus Linux
    instances per card.

  - All line cards, fabric cards and PSUs are accessible from the front.

  - Their 16 fan modules are accessible from the rear.

## <span>Recent activity</span>

  - ![/images/s/en\_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.241/\_/images/icons/profilepics/default.png](/images/s/en_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.241/_/images/icons/profilepics/default.png)  
    <span class="caption">dcawley</span>
    
    [Dan Cawley](https://docs.cumulusnetworks.com/display/~dcawley)

  - Chassis User Guideupdated 28 minutes ago[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=6488345&selectedPageVersions=9&selectedPageVersions=8)

<!-- end list -->

  - [![/images/download/attachments/1704089/pete-27211-pp-profilepic.jpg](/images/download/attachments/1704089/pete-27211-pp-profilepic.jpg)](https://docs.cumulusnetworks.com/display/~pete)
    
    [Pete Bratach](https://docs.cumulusnetworks.com/display/~pete)

  - [Chassis-specific
    Commands](/chassis/Chassis-specific_Commands)created Mar 26, 2018

  - Chassis User Guideupdated Mar 26, 2018[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=6488345&selectedPageVersions=8&selectedPageVersions=7)

  - [Accessing the Console](/chassis/Accessing_the_Console)updated Mar
    26, 2018[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7766291&selectedPageVersions=3&selectedPageVersions=2)

  - [Monitoring and Troubleshooting a
    Chassis](/chassis/Monitoring_and_Troubleshooting_a_Chassis)updated
    Mar 26, 2018[view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=7113871&selectedPageVersions=4&selectedPageVersions=3)

[Show
More](https://docs.cumulusnetworks.com/plugins/recently-updated/changes.action?theme=social&pageSize=5&startIndex=5&searchToken=41987&spaceKeys=CHASSIS&contentType=page,%20comment,%20blogpost)

![/images/s/en\_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.240/\_/images/icons/wait.gif](/images/s/en_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.240/_/images/icons/wait.gif)  
<span class="caption">Please wait</span>

## <span>Space contributors</span>

  - [Dan Cawley](https://docs.cumulusnetworks.com/display/~dcawley) (28
    minutes ago)

  - [Pete Bratach](https://docs.cumulusnetworks.com/display/~pete) (412
    days ago)
