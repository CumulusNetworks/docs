---
title: Getting Started
author: Cumulus Networks
weight: 15
pageID: 5126687
---
This section provides an installation process overview with next step links for each supported hypervisor or development environment.

To install Cumulus VX:

1. Download and install the preferred hypervisor platform or development environment.
2. Download the appropriate Cumulus VX image from the Cumulus website.
3. Configure the VMs (import the VX image to create the VMs).

## Download and Install the Hypervisor and Developer Environment

To download and install the preferred hypervisor or development environment, follow the relevant links below. Detailed installation instructions are available on the download websites:

| <div style="width:150px">Hypervisor | Download Location |
| ------------------- | --------------------------------------------------------------- |
| VMware vSphere ESXi | {{<exlink url="http://www.vmware.com/products/vsphere.html" >}} |
| VirtualBox          | {{<exlink url="https://www.virtualbox.org/wiki/Downloads" >}}   |
| KVM                 | {{<exlink url="http://www.qemu-project.org/download/" >}}       |

| <div style="width:150px">Development Environment | Download Location | Supported Hypervisors |
| ---------| ---------------------------------------------------------------| --------------- |
| Vagrant  | {{<exlink url="https://www.vagrantup.com/downloads.html" >}}   | VirtualBox      |
| GNS3     | {{<exlink url="https://community.gns3.com/software" >}}        | KVM, VirtualBox |

## Download the Cumulus VX Image

Cumulus VX images for all supported platforms are available from the [Cumulus Networks website](https://cumulusnetworks.com/products/cumulus-vx/download/). Each disk image contains a single VM for a standalone switch. You can clone the image to build the test network.

Five versions of the virtual disk image are available for use across various hypervisors:

- OVA disk image for use with VirtualBox
- VMware-specific OVA disk image
- qcow2 disk image for use with KVM
- Box image for use with Vagrant
- Binary image for ONIE installations

## Configure the VMs

After you have downloaded the hypervisor or development environment and the Cumulus VX image, follow the relevant link below to configure the VMs:

- [VMware vSphere ESXi](VMware-vSphere-ESXi-5.5/)
- [VirtualBox](VirtualBox/)
- [Libvirt and KVM - QEMU](Libvirt-and-KVM-QEMU/)
