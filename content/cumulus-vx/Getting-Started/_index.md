---
title: Getting Started
author: Cumulus Networks
weight: 15
toc: 2
---
This section provides an installation process overview with next step links for each supported hypervisor or development environment.

To install Cumulus VX:

1. Download and install the preferred hypervisor platform.
2. Download the appropriate Cumulus VX image from the Cumulus website.
3. Configure the VMs.

## Download and Install the Hypervisor Platform

To download and install the preferred hypervisor platform, follow the relevant links below. Detailed installation instructions are available on the download websites:

| Hypervisor          | Download Location |
| ------------------- | ---------------------------------------------------------------  |
| VMware vSphere ESXi | {{<exlink url="http://www.vmware.com/products/vsphere.html" >}}  |
| VirtualBox          | {{<exlink url="https://www.virtualbox.org/wiki/Downloads" >}}    |
| KVM                 | {{<exlink url="http://www.qemu-project.org/download/" >}}        |
| Vagrant             | {{<exlink url="https://www.vagrantup.com/downloads.html" >}}     |
| GNS3                | {{<exlink url="https://community.gns3.com/software" >}}          |

Vagrant is supported with VirtualBox and KVM. GNS3 is supported with VirtualBox.

## Download the Cumulus VX Image

Cumulus VX images for all supported platforms are available from the {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="Cumulus Networks website">}}. Each disk image contains a single VM for a standalone switch. You can clone the image to build the test network.

All virtual disk images are available for use across various platforms:

- OVA disk image for use with VirtualBox
- VMware-specific OVA disk image
- qcow2 disk image for use with KVM
- Box image for use with Vagrant
- GNS3 appliance for use with VirtualBox
- Binary image for ONIE installations

## Configure the VMs

Follow the relevant link below to configure the VMs:

- {{<link url="VirtualBox" text="VirtualBox">}}
- {{<link url="VMware-vSphere-ESXi" text="VMware vSphere ESXi">}}
- {{<link url="KVM" text="KVM">}}
- {{<link url="Vagrant-and-VirtualBox" text="Vagrant and VirtualBox">}}
- {{<link url="Vagrant-and-KVM" text="Vagrant and KVM">}}
- {{<link url="GNS3-and-VirtualBox" text="GNS3 and VirtualBox">}}
