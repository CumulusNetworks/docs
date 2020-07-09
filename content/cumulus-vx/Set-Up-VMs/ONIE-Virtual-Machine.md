---
title: ONIE Virtual Machine
author: Cumulus Networks
weight: 24
toc: 2
---
Cumulus VX images now include the GRUB boot loader and {{<exlink url="(http://onie.org/" text="Open Network Install Environment (ONIE)">}} preinstalled. You can install Cumulus Linux on switch hardware using a binary image. You can test this process by installing a Cumulus VX binary image with ONIE in a virtual environment.

{{%notice note%}}

Installation via ONIE is supported in Cumulus VX 3.x and later.

{{%/notice%}}

This section assumes that you have downloaded and installed a hypervisor, {{<exlink url="https://cumulusnetworks.com/products/cumulus-vx/download/" text="downloaded the Cumulus VX binary image" >}}, and configured the VM.

1. After booting the VM, reboot into ONIE Rescue mode using one of two methods:
   - Select ONIE Rescue mode on next reboot and reboot the VM with the `cumulus@switch:$ sudo onie-select -rf && sudo reboot` command.
   - Reboot and during the first 5 seconds on the GRUB menu, change the boot image to `ONIE`, then select `ONIE Rescue Mode` using the GRUB menu.

2. To install Cumulus VX, run the following command:

   ```
   cumulus@switch:~$ onie-nos-install <URL to cumulus-linux-vx-amd64.bin>
   ```

   Refer to {{<exlink url="https://docs.cumulusnetworks.com/cumulus-linux/Installation-Management/Installing-a-New-Cumulus-Linux-Image" text="Installing a New Cumulus Linux Image">}} or the
   {{<exlink url="https://github.com/opencomputeproject/onie/wiki/Quick-Start-Guide" text="ONIE Quick Start Guide">}} for more specific instructions.

During the ONIE boot sequence, ONIE attempts to start DHCP and timeout on every configured interface. If the VM has numerous configured interfaces, this can take a while to complete.

After the installation process is complete, GRUB redirects you to the installed Cumulus VX instance.
