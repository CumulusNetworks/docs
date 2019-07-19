---
title: Cumulus VX Getting Started Guide
author: Cumulus Networks
weight: 1
aliases:
 - /display/VX30/Cumulus+VX+Getting+Started+Guide
 - /pages/viewpage.action?pageId=5126578
pageID: 5126578
product: Cumulus VX
version: '3.0'
imgData: cumulus-vx-30
siteSlug: cumulus-vx-30
subsection: true
---
Cumulus VX is a free virtual environment for cloud and network
administrators to test the latest technology from Cumulus Networks,
removing all organizational and economic barriers to getting started
with open networking in your own time, at your own pace, and within your
own environment.

The environment can be used to learn about, and evaluate, Cumulus Linux,
anytime and anywhere, producing sandbox environments for prototype
assessment, pre-production rollouts, and script development.

## What's New

Major enhancements have been made for Cumulus VX 3.0 with the goal of
producing a true learning, testing, and pre-production tool. These
enhancements include:

  - [Cumulus VX now includes ONIE with `onie-nos-install`
    support](#src-5126578) to show the installation steps.

  - The VX image comes with a GRUB Menu
    containing ONIE and CL. To simulate the install process on real
    hardware, Cumulus Linux binaries can be installed from ONIE.

  - Cumulus VX is being treated as a
    "platform"; most monitoring tools that would be run on hardware can
    now be run on VX (for example, sensors, decode-syseeprom, smonctl
    and platform-detect).

  - Cumulus VX now runs the same packages
    as Cumulus Linux, excluding those that are specific to the
    networking ASIC. This is as close as things can be to software
    parity with Cumulus Linux.

The goal for Cumulus VX is to create an environment that feels and
behaves like a real switch. For that reason, tools like
`platform-detect`, `decode-syseeprom`, `smonctl`, `sensors`, `pwmd`, and
`ledmgrd` will report real world data. In addition, Cumulus VX will now
be built alongside Cumulus Linux, rather than with a staggered delay, to
allow for testing ahead of a production upgrade.

## Supported Platforms

  - Integrates with [KVM](http://www.linux-kvm.org/page/Downloads),
    [VirtualBox](https://www.virtualbox.org/wiki/Downloads) and
    [VMware](https://my.vmware.com/web/vmware/downloads) hypervisors

  - Runs within [GNS3](http://www.gns3.com) and
    [Vagrant](https://www.vagrantup.com) environments

## About the Virtual Machine

Cumulus VX runs in a virtual machine (VM) on a standard x86 environment.
The VM is a 64-bit operating system, built on the same foundation as
[Cumulus Linux](/cumulus-linux), running the Linux 3.2.65-1+deb7u2+cl2.5+2 kernel,
using `virtio` drivers for
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
article](/version/cumulus-vx-30/Comparing-Cumulus-VX-with-Other-Cumulus-Networks-Products).

## Community Support

Cumulus VX is a [community-supported
product](https://support.cumulusnetworks.com/hc/en-us/articles/206382248).
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

  - [Using Cumulus VX with VMware](/version/cumulus-vx-30/Using-Cumulus-VX-with-VMware/)

  - [Using Cumulus VX with VirtualBox](/version/cumulus-vx-30/Using-Cumulus-VX-with-VirtualBox/)

  - [Using Cumulus VX with KVM](/version/cumulus-vx-30/Using-Cumulus-VX-with-KVM)

  - [Using Cumulus VX with Vagrant](/version/cumulus-vx-30/Using-Cumulus-VX-with-Vagrant)

  - [Using Cumulus VX with GNS3](/version/cumulus-vx-30/Using-Cumulus-VX-with-GNS3/)

## Logging in to the VM

The Cumulus VX VM has these default login credentials:

  - **User name:** cumulus

  - **Password:** CumulusLinux\!

The cumulus user has `sudo` privileges, just like a Cumulus Linux
switch.

## Useful Links

For more information about Cumulus VX, Cumulus Linux and supported
environments, visit these links:

  - [Cumulus VX release notes](https://support.cumulusnetworks.com/hc/en-us/articles/219623788)

  - [Cumulus Linux documentation](/cumulus-linux)

  - [Cumulus Networks knowledge base](https://support.cumulusnetworks.com/hc/en-us/)

  - [VMware documentation](https://www.vmware.com/support/pubs/)

  - [VirtualBox documentation](https://www.virtualbox.org/wiki/Documentation)

  - [KVM documents](http://www.linux-kvm.org/page/Documents)

  - [Vagrant documentation](https://docs.vagrantup.com/v2/)

  - [GNS3 documentation](https://community.gns3.com/community/software/documentation)

{{% imgOld 0 %}}
