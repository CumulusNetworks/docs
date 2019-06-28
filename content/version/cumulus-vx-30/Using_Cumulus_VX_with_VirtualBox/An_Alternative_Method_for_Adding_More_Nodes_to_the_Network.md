---
title: An Alternative Method for Adding More Nodes to the Network
author: Cumulus Networks
weight: 53
aliases:
 - /display/VX30/An+Alternative+Method+for+Adding+More+Nodes+to+the+Network
 - /pages/viewpage.action?pageId=5126593
pageID: 5126593
product: Cumulus VX
version: '3.0'
imgData: cumulus-vx-30
siteSlug: cumulus-vx-30
---
Another way you can add a VM to one or more of the internal virtual
networks in VirtualBox is by cloning the VM. However, keep the following
in mind:

  - To quickly set up any configurations that you want across multiple
    nodes on your system, configure the settings on the original VM,
    then clone the VM using **Machine** \> **Clone**.
    
    For example, if you want to include a management VM for the new
    topology you are going to create, you can set the eth0 port to be on
    a virtual network that the management VM is on, so when you clone
    the new VM, it will duplicate this port, giving you an out-of-band
    (OOB) network.

  - When you clone the VM, you save on disk storage by referring to the
    original disk image instead of copying it to the new VM.

  - Always reset your MAC addresses on the virtual NICs, unless you have
    a strong reason not to do so.
