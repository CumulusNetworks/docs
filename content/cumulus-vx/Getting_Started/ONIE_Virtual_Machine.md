---
title: ONIE Virtual Machine
author: Cumulus Networks
weight: 47
aliases:
 - /display/VX/ONIE+Virtual+Machine
 - /pages/viewpage.action?pageId=5126699
pageID: 5126699
product: Cumulus VX
version: 3.4.0
imgData: cumulus-vx
siteSlug: cumulus-vx
---
Cumulus VX images now include the GRUB boot loader and [Open Network
Install Environment (ONIE)](http://onie.org/) preinstalled. You can
install Cumulus Linux on switch hardware using a binary image. You can
test this process by installing a Cumulus VX binary image with ONIE in a
virtual environment.

{{%notice note%}}

Installation via ONIE is supported in Cumulus VX 3.x and later versions.

{{%/notice%}}

{{%notice note%}}

This section assumes that you have downloaded and installed a
hypervisor, [downloaded the Cumulus VX binary
image](https://cumulusnetworks.com/products/cumulus-vx/download/), and
configured the VM.

{{%/notice%}}

1.  After booting the VM, reboot into ONIE Rescue mode using one of two
    methods:
    
    1.  Select ONIE Rescue mode on next reboot and reboot the VM:
        
            cumulus@switch:$ sudo onie-select -rf && sudo reboot
    
    2.  Reboot and during the first 5 seconds on the GRUB menu, change
        the boot image to `ONIE`, then select `ONIE Rescue Mode` using
        the GRUB menu.

2.  To install Cumulus VX, run the following command:
    
        cumulus@switch:~$ onie-nos-install <URL to cumulus-linux-vx-amd64.bin>
    
    Refer to [Installing a New Cumulus Linux
    Image](/display/VX/Installing+a+New+Cumulus+Linux+Image) or the
    [ONIE Quick Start
    Guide](https://github.com/opencomputeproject/onie/wiki/Quick-Start-Guide)
    for specific instructions on various install methods.

{{%notice note%}}

During the ONIE boot sequence, ONIE attempts to start DHCP and timeout
on every configured interface. If the VM has numerous configured
interfaces, this can take a while to complete. This behavior will be
addressed in the future.

{{%/notice%}}

After the installation process is complete, GRUB redirects you to the
installed Cumulus VX instance.
