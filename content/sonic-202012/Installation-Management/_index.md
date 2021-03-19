---
title: Installation Management
author: Cumulus Networks
weight: 200
product: SONiC
version: 201911_MUR5
siteSlug: sonic
---

Before you install SONiC on your switch, make sure the switch is {{<exlink url="https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms" text="supported">}}.

This topic describes installing SONiC onto an {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html" text="ONIE-enabled">}} Mellanox switch with a Spectrum-family ASIC. If you plan on installing SONiC onto a switch from a different manufacturer, you can get the image from the {{<exlink url="https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms" text="Azure GitHub site">}}. But the installation steps are the same.

The installation uses {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html" text="ONIE">}}, the Open Network Install Environment, which is a boot loader for installing open network operating systems.

The Mellanox install image is available {{<exlink url="https://sonic-jenkins.westus2.cloudapp.azure.com/job/mellanox/job/buildimage-mlnx-all/lastSuccessfulBuild/artifact/target/sonic-mellanox.bin" text="here">}}. Once you download the image, you can install SONiC from a USB drive or over the network.

{{%notice tip%}}

If you need to build your own Pure (vendor independent) SONiC image, read this post on the {{<exlink url="https://developer.nvidia.com/blog/building-pure-sonic-image/" text="NVIDIA developer blog">}}.

{{%/notice%}}

## Install over USB

These steps assume you are using an Ubuntu 18.04 host. The drive paths and formatting might be different on your system and operating system.

To install over USB, do the following:

1. Insert a formatted USB drive into the system where you downloaded the SONiC install image.

1. Copy the install image to the root directory of a USB drive, naming it `onie-installer`.

       ubuntu:~$ sudo mkdir /mnt/usb
       ubuntu:~$ sudo mount /dev/sdb1 /mnt/usb
       ubuntu:~$ sudo cp sonic-mellanox.bin /mnt/usb/onie-installer
       ubuntu:~$ sudo umount /mnt/usb

1. Remove the USB drive from your system and insert it into the USB port on the switch, then power on the switch. ONIE discovers the `onie-installer` file on the root of the USB drive and executes it.

## Install over the Network

To install SONiC over the network, make sure the SONiC installer image is available on the network over HTTP. The simplest network installation is when the web/HTTP server is directly connected to the Ethernet management port on the switch where you want to install SONiC.

To install SONiC, do the following:

1. Install and configure an HTTP server, like {{<exlink url="https://httpd.apache.org/" text="Apache">}} or {{<exlink url="https://nginx.org/" text="NGINX">}}.
1. Copy the SONiC installer image to the root directory of the HTTP server, then create a symlink to `onie_installer.bin` so ONIE can easily find the installer. For Apache on Ubuntu, the root directory is `/var/www`.

       image-server:~$ sudo cp sonic_installer.bin /var/www
       image-server:~$ sudo ln -s sonic_installer.bin ./onie_installer.bin

1. Using `wget` or `curl` on a different system, verify the SONiC installer download from the HTTP server.

   ubuntu_server:~$ curl http://<Your HTTP Server>/onie_installer.bin

1. Power on the switch. ONIE discovers the IP address (either IPv6 or IPv4) of the link local Web server. For more information on how ONIE discovers its link local neighbors, see {{<exlink url="https://opencomputeproject.github.io/onie/design-spec/discovery.html#discover-neighbors" text="the ONIE documentation">}}.

   After neighbor discovery, ONIE makes HTTP requests for a series of default installer image file names as described in the {{<exlink url="https://opencomputeproject.github.io/onie/design-spec/discovery.html#default-file-name" text="ONIE documentation">}}.

   Next, ONIE applies the default file name conventions, then it makes HTTP requests looking for an installer image. In our example, ONIE should find the `onie_installer.bin` disk image and start the install.
