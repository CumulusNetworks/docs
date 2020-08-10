---
title: Advanced Configuration
author: Cumulus Networks
weight: 46
---
This section describes advanced procedures that you can follow to get more out of Cumulus VX.

- Run the conversion script on your switches so that you can take the self-paced labs in the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Virtual Test Drive">}}.
- Run the topology converter to convert a topology file into a Vagrantfile so you can create a topology of your choice.
- Test the Cumulus Linux upgrade process in your virtual environment by installing a Cumulus VX binary image with ONIE.

## Run the Conversion Script

The self-paced labs in the {{<exlink url="https://cumulusnetworks.com/lp/cumulus-linux-on-demand/" text="Virtual Test Drive">}} use the following topology:

IMAGE

To run the labs, you need to first run a script to update the port configuration. 

## Run the Topology Converter

To create a topolgy of your choice, you can use the topology converter to convert a `topology.dot` (DOT-specified network graph) file to a Vagrantfile. The `topology.dot` file describes the network topology link-by-link.

## Install an ONIE Virtual Machine

Cumulus VX images include the GRUB boot loader and Open Network Install Environment (ONIE) preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

After booting the VM, reboot into ONIE Rescue mode using one of two methods:

- Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
- Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

To install Cumulus VX, run the `onie-nos-install <URL to cumulus-linux-vx-amd64.bin>` command.
