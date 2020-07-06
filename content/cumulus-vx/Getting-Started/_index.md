---
title: Getting Started
author: Cumulus Networks
weight: 17
pageID: 5126687
---
To install Cumulus VX, first download and install the preferred
hypervisor platform or development environment, then download the
appropriate Cumulus VX image from the Cumulus website. After you have
downloaded both the preferred hypervisor and Cumulus VX image, you can
import the VX image to create the necessary VMs. This section provides
an installation process overview, with next step links for each
supported hypervisor or development environment.

## Download the Cumulus VX Image

Cumulus VX images for all supported platforms are available from the
[Cumulus Networks website](https://cumulusnetworks.com/products/cumulus-vx/download/).

{{%notice info%}}

Each disk image contains a single VM for a standalone switch. You can
clone the image to build the test network.

{{%/notice%}}

## Download and Install the Hypervisor/Developer Environment

{{%notice note%}}

If the preferred hypervisor or developer environment is already
installed, go to Configure the VMs, below.

{{%/notice%}}

To download and install the preferred hypervisor or development
environment, follow the relevant links below. Detailed installation
instructions are available on the download websites:

| Hypervisor                | Download Location     |
| ------------------------- | ------------------------------------ |
| VMware vSphere - ESXi     | <http://www.vmware.com/products/vsphere.html>  |
| VirtualBox                | <https://www.virtualbox.org/wiki/Downloads> |
| KVM                       | For package installation instructions, refer to <http://www.qemu-project.org/download/> |

&nbsp;

| Development Environment | Download Location                          | Supported Hypervisors |
| ----------------------- | ------------------------------------------ | --------------------- |
| Vagrant                 | <https://www.vagrantup.com/downloads.html> | VirtualBox            |
| GNS3                    | <https://community.gns3.com/software>      | KVM, VirtualBox       |

## Configure the VMs

After you have downloaded the hypervisor or development environment and
the Cumulus VX image, follow the relevant link below for detailed setup
instructions:

  - [VMware vSphere - ESXi](VMware-vSphere-ESXi-5.5/)
  - [VirtualBox](VirtualBox/)
  - [Libvirt and KVM - QEMU](Libvirt-and-KVM-QEMU/)
