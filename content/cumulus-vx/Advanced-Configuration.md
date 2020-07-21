---
title: Advanced Configuration
author: Cumulus Networks
weight: 46
---
INTRO

## Install an ONIE Virtual Machine

Cumulus VX images include the GRUB boot loader and Open Network Install Environment (ONIE) preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

After booting the VM, reboot into ONIE Rescue mode using one of two methods:

- Select ONIE Rescue mode on next reboot and reboot the VM with the `sudo onie-select -rf && sudo reboot` command.
- Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

To install Cumulus VX, run the `onie-nos-install <URL to cumulus-linux-vx-amd64.bin>` command.
