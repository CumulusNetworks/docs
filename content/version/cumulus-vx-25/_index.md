---
title: Cumulus VX Getting Started Guide
author: Cumulus Networks
weight: -25
aliases:
 - /display/VX25/Cumulus+VX+Getting+Started+Guide
 - /pages/viewpage.action?pageId=5115387
pageID: 5115387
subsection: true
cascade:
  product: Cumulus VX
  version: "2.5 ESR"
  imgData: cumulus-vx-25
  siteSlug: cumulus-vx-25
---
Cumulus VX is free, open source software that provides a virtual
experience enabling cloud and network admins to evaluate Cumulus
Networks' latest technology easily and risk free. Cumulus VX removes all
organizational and economic barriers for you to get started with open
networking on your own time, at your own pace and in your own
environment.

You can use Cumulus VX to learn about and evaluate Cumulus Linux,
anytime, anywhere. Use it to build sandbox environments for prototyping,
pre-production rollouts and developing scripts.

## Supported Platforms

  - Integrates with [KVM](http://www.linux-kvm.org/page/Downloads),
    [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and
    [VMware](https://my.vmware.com/web/vmware/downloads) hypervisors
  - Runs within [GNS3](http://www.gns3.com) and
    [Vagrant](https://www.vagrantup.com) environments

## About the Virtual Machine

Cumulus VX runs in a virtual machine (VM) on a standard x86 environment.
The VM is a 64-bit operating system, built on the same foundation as
[Cumulus Linux](/cumulus-linux), running
the Linux 3.2.65-1+deb7u2+cl2.5+2 kernel, using `virtio` drivers for
network and HDD interfaces as well as the logical volume manager (LVM).

Four versions of the virtual disk image are available for use across
various hypervisors:

  - An OVA disk image for use with VirtualBox.
  - A VMware-specific OVA disk image.
  - A qcow2 disk image for use with KVM.
  - A Box image for use with Vagrant.

## Comparisons with Other Cumulus Networks Products

Cumulus VX is a virtual appliance that simulates a Cumulus Linux or
Cumulus RMP environment. To see how these systems compare, [read this
article](/version/cumulus-vx-25/Comparing-Cumulus-VX-with-Other-Cumulus-Networks-Products).

## Community Support

Cumulus VX is a [community-supported product](https://support.cumulusnetworks.com/hc/en-us/articles/206382248).
Join the [Cumulus Networks
community](https://community.cumulusnetworks.com/cumulus/categories/cumulus_vx)
and ask for or offer help.

## Downloading the Cumulus VX Image

To get started, you need to download some software as well as the
[Cumulus VX disk
image](https://cumulusnetworks.com/cumulus-vx/download/) (qcow2 or OVA)
that runs with the hypervisor you plan to use with Cumulus VX. Each disk
image contains a single VM for a standalone switch. You can clone this
virtual machine to build out your test network. For more information,
read the appropriate steps below:

  - [Using Cumulus VX with VMware](/version/cumulus-vx-25/Using-Cumulus-VX-with-VMware/)
  - [Using Cumulus VX with VirtualBox](/version/cumulus-vx-25/Using-Cumulus-VX-with-VirtualBox/)
  - [Using Cumulus VX with KVM](/version/cumulus-vx-25/Using-Cumulus-VX-with-KVM)
  - [Using Cumulus VX with Vagrant](/version/cumulus-vx-25/Using-Cumulus-VX-with-Vagrant)
  - [Using Cumulus VX with GNS3](/version/cumulus-vx-25/Using-Cumulus-VX-with-GNS3/)

## Logging in to the VM

The Cumulus VX VM has these default login credentials:

  - **User name:** cumulus
  - **Password:** CumulusLinux\!

The cumulus user has `sudo` privileges, just like a Cumulus Linux
switch.

## Useful Links

For more information about Cumulus VX, Cumulus Linux and supported
environments, visit these links:

  - [Cumulus VX release notes](https://support.cumulusnetworks.com/hc/en-us/articles/115002082808)
  - [Cumulus Linux documentation](/cumulus-linux)
  - [Cumulus Networks knowledge base](https://support.cumulusnetworks.com/hc/en-us/)
  - [VMware documentation](https://www.vmware.com/support/pubs/)
  - [VirtualBox documentation](https://www.virtualbox.org/wiki/Documentation)
  - [KVM documents](http://www.linux-kvm.org/page/Documents)
  - [Vagrant documentation](https://docs.vagrantup.com/v2/)
  - [GNS3 documentation](https://community.gns3.com/community/software/documentation)

{{% imgOld 0 %}}
