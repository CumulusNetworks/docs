---
title: Cumulus VX Getting Started Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/VX25/Cumulus+VX+Getting+Started+Guide
 - /pages/viewpage.action?pageId=5115387
pageID: 5115387
product: Cumulus VX
version: '2.5'
imgData: cumulus-vx-25
siteSlug: cumulus-vx-25
subsection: true
---
Cumulus VX is free, open source software that provides a virtual
experience enabling cloud and network admins to evaluate Cumulus
Networks’ latest technology easily and risk free. Cumulus VX removes all
organizational and economic barriers for you to get started with open
networking on your own time, at your own pace and in your own
environment.

You can use Cumulus VX to learn about and evaluate Cumulus Linux,
anytime, anywhere. Use it to build sandbox environments for prototyping,
pre-production rollouts and developing scripts.

## <span>Supported Platforms</span>

  - Integrates with [KVM](http://www.linux-kvm.org/page/Downloads),
    [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and
    [VMware](https://my.vmware.com/web/vmware/downloads) hypervisors

  - Runs within [GNS3](http://www.gns3.com) and
    [Vagrant](https://www.vagrantup.com) environments

## <span>About the Virtual Machine</span>

Cumulus VX runs in a virtual machine (VM) on a standard x86 environment.
The VM is a 64-bit operating system, built on the same foundation as
[Cumulus Linux](http://docs.cumulusnetworks.com/display/DOCS), running
the Linux 3.2.65-1+deb7u2+cl2.5+2 kernel, using `virtio` drivers for
network and HDD interfaces as well as the logical volume manager (LVM).

Four versions of the virtual disk image are available for use across
various hypervisors:

  - An OVA disk image for use with VirtualBox.

  - A VMware-specific OVA disk image.

  - A qcow2 disk image for use with KVM.

  - A Box image for use with Vagrant.

## <span>Comparisons with Other Cumulus Networks Products</span>

Cumulus VX is a virtual appliance that simulates a Cumulus Linux or
Cumulus RMP environment. To see how these systems compare, [read this
article](/version/cumulus-vx-25/Comparing_Cumulus_VX_with_Other_Cumulus_Networks_Products).

## <span>Community Support</span>

Cumulus VX is a [community-supported
product](https://support.cumulusnetworks.com/hc/en-us/articles/206382248).
Join the [Cumulus Networks
community](https://community.cumulusnetworks.com/cumulus/categories/cumulus_vx)
and ask for or offer help.

## <span>Downloading the Cumulus VX Image</span>

To get started, you need to download some software as well as the
[Cumulus VX disk
image](https://cumulusnetworks.com/cumulus-vx/download/) (qcow2 or OVA)
that runs with the hypervisor you plan to use with Cumulus VX. Each disk
image contains a single VM for a standalone switch. You can clone this
virtual machine to build out your test network. For more information,
read the appropriate steps below:

  - [Using Cumulus VX with
    VMware](/version/cumulus-vx-25/Using_Cumulus_VX_with_VMware/)

  - [Using Cumulus VX with
    VirtualBox](/version/cumulus-vx-25/Using_Cumulus_VX_with_VirtualBox/)

  - [Using Cumulus VX with
    KVM](/version/cumulus-vx-25/Using_Cumulus_VX_with_KVM)

  - [Using Cumulus VX with
    Vagrant](/version/cumulus-vx-25/Using_Cumulus_VX_with_Vagrant)

  - [Using Cumulus VX with
    GNS3](http://docs.cumulusnetworks.com/display/VX/Using+Cumulus+VX+with+GNS3)

## <span>Logging in to the VM</span>

The Cumulus VX VM has these default login credentials:

  - **User name:** cumulus

  - **Password:** CumulusLinux\!

The cumulus user has `sudo` privileges, just like a Cumulus Linux
switch.

## <span>Useful Links</span>

For more information about Cumulus VX, Cumulus Linux and supported
environments, visit these links:

  - [Cumulus VX release
    notes](https://support.cumulusnetworks.com/hc/en-us/articles/115002082808)

  - [Cumulus Linux
    documentation](http://docs.cumulusnetworks.com/display/DOCS)

  - [Cumulus Networks knowledge
    base](https://support.cumulusnetworks.com/hc/en-us/)

  - [VMware documentation](https://www.vmware.com/support/pubs/)

  - [VirtualBox
    documentation](https://www.virtualbox.org/wiki/Documentation)

  - [KVM documents](http://www.linux-kvm.org/page/Documents)

  - [Vagrant documentation](https://docs.vagrantup.com/v2/)

  - [GNS3
    documentation](https://community.gns3.com/community/software/documentation)

{{% imgOld 0 %}}

## <span>Recently Updated Pages</span>

  - Cumulus VX Getting Started Guide31 minutes ago • updated by [Dan
    Cawley](https://docs.cumulusnetworks.com/display/~dcawley) • [view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=5115387&selectedPageVersions=3&selectedPageVersions=2)

  - Cumulus VX Getting Started GuideJan 31, 2017 • updated by [Pete
    Bratach](https://docs.cumulusnetworks.com/display/~pete) • [view
    change](https://docs.cumulusnetworks.com/pages/diffpagesbyversion.action?pageId=5115387&selectedPageVersions=2&selectedPageVersions=1)

  - [Using Cumulus VX with
    VirtualBox](/version/cumulus-vx-25/Using_Cumulus_VX_with_VirtualBox/)May
    09, 2016 • created by [Pete
    Bratach](https://docs.cumulusnetworks.com/display/~pete)

  - [Using Cumulus VX with
    KVM](/version/cumulus-vx-25/Using_Cumulus_VX_with_KVM)Apr 21, 2016 •
    created by [Tom
    Wells](https://docs.cumulusnetworks.com/display/~tom)

  - [Using Cumulus VX with
    Vagrant](/version/cumulus-vx-25/Using_Cumulus_VX_with_Vagrant)Mar
    31, 2016 • created by [Eric
    Pulvino](https://docs.cumulusnetworks.com/display/~eric)

[Show
More](https://docs.cumulusnetworks.com/plugins/recently-updated/changes.action?theme=concise&pageSize=5&startIndex=5&searchToken=41987&spaceKeys=VX25&contentType=page)

![/images/s/en\_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.240/\_/images/icons/wait.gif](/images/s/en_GB/6210/96b66f73363ad6a4132228b496713b1df46ada86.240/_/images/icons/wait.gif)  
<span class="caption">Please wait</span>

## <span>Space Contributors</span>

  - [Pete Bratach](https://docs.cumulusnetworks.com/display/~pete) (832
    days ago)

  - [Dan Cawley](https://docs.cumulusnetworks.com/display/~dcawley) (31
    minutes ago)
