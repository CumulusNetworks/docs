---
title: Installation Management
author: NVIDIA
weight: 200
product: SONiC
version: 202012
siteSlug: sonic
---

Before you install SONiC on your switch, make sure the switch is {{<exlink url="https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms" text="supported">}}.

This topic describes installing SONiC onto an {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html" text="ONIE-enabled">}} NVIDIA Spectrum switch with a Spectrum-family ASIC. If you plan on installing SONiC onto a switch from a different manufacturer, you can get the image from the {{<exlink url="https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms" text="Azure GitHub site">}}. But the installation steps are the same.

The installation uses {{<exlink url="https://opencomputeproject.github.io/onie/user-guide/index.html" text="ONIE">}}, the Open Network Install Environment, which is a boot loader for installing open network operating systems.

The NVIDIA Mellanox install images are available through your NVIDIA sales team. Once you get the image, you can install SONiC from a USB drive or over the network.

{{%notice tip%}}

If you need more control over the install image, you can build your own Pure (vendor independent) SONiC image. {{<exlink url="https://sonic-build.azurewebsites.net/ui/sonic/pipelines" text="Download an image">}} that is automatically built from the SONiC development pipeline, then read this post from the NVIDIA developer blog on {{<exlink url="https://developer.nvidia.com/blog/building-pure-sonic-image/" text="how to build it">}}.

{{%/notice%}}

## Prepare to Install the SONiC Image

The switch may already have ONIE or another network operating system installed. In order to install SONiC on it, follow the preparatory steps below before you start installing SONiC.

Using a SONiC release earlier than 201811 might require upgrades to the BIOS and ONIE. For instructions, please contact your switch manufacturer.

1. Verify your switch model is {{<exlink url="https://github.com/Azure/SONiC/wiki/Supported-Devices-and-Platforms" text="supported">}}.
1. Connect to the switch via the serial console.
1. If the switch has a network operating system installed, uninstall the existing NOS first before installing SONiC. To do so, simply boot into ONIE and select **Uninstall OS**:

       GNU GRUB version 2.02-beta3
       +-----------------------------------
       | ONIE: Install OS
       | ONIE: Rescue
       | *ONIE: Uninstall OS
       | ONIE: Update ONIE
       | ONIE: Embed ONIE

1. Reboot the switch into ONIE and select **Install OS**.

1. A discovery process starts automatically, searching for the OS to install. Stop the ONIE discovery by running:

       onie:$ onie-stop
1. Verify SMIBIOS parameters by running:

       onie:$ dmidecode -t1 -t2 | grep "Product Name"
       Product Name: MSN2700
       Product Name: VMOD0001

## Install Using the RJ-45 Console

1. Connect the host PC to the console (RJ-45) port of the switch system using the supplied cable.

   {{%notice info%}}

Make sure to connect to the console RJ-45 port of the switch and not to the management port.

   {{%/notice%}}

2. Configure a serial terminal with the settings described below.

   The baud rate might be different based on the BIOS or ONIE version.

   | Parameter | Setting |
   | --------- | ------- |
   | Baud Rate | 115200 |
   | Data bits | 8 |
   | Flow Control | None |
   | Parity | None |
   | Stop bits | 1 |

## Install Using the Management IP

DHCP is enabled by default over the management port. Therefore, if you configured your DHCP server and connected an RJ-45 cable to the management port, you can log in using the designated IP address.

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
