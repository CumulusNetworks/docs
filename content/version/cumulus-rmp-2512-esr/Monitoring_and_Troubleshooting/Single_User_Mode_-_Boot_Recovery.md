---
title: Single User Mode - Boot Recovery
author: Cumulus Networks
weight: 85
aliases:
 - /display/RMP25ESR/Single+User+Mode+-+Boot+Recovery
 - /pages/viewpage.action?pageId=5116335
pageID: 5116335
product: Cumulus RMP
version: 2.5.12 ESR
imgData: cumulus-rmp-2512-esr
siteSlug: cumulus-rmp-2512-esr
---
Use single user mode to assist in troubleshooting system boot issues or
for password recovery. Entering single user mode is
[platform-specific](http://cumulusnetworks.com/hcl/), so follow the
appropriate steps for your x86 or PowerPC switch.

## <span>Entering Single User Mode on a PowerPC Switch</span>

1.  From the console, boot the switch, interrupting the U-Boot countdown
    to enter the U-Boot prompt. Enter the following:
    
        => setenv lbootargs init=/bin/sh  
        => boot

2.  After the system boots, the shell command prompt appears. In this
    mode, you can change the root password or test a boot service that
    is hanging the boot process.

3.  Reboot the system.
    
        cumulus@switch:~$ sudo reboot -f  
        Restarting the system.

## <span>Entering Single User Mode on an x86 Switch</span>

From the console, boot the switch. At the GRUB menu, select the image
slot you wish to boot into with a password:

``` 
                  GNU GRUB  version 1.99-27+deb7u2
 +-----------------------------------------------------------------------+
 |Cumulus RMP 2.5.3-be24dc3-201412021541-build - slot 1                  |
 |Cumulus RMP 2.5.3-be24dc3-201412021541-build - slot 1 (recovery mode)  |
 |Cumulus RMP 2.5.3-b1bb3b7-201412090640-build - slot 2                  |
 |Cumulus RMP 2.5.3-b1bb3b7-201412090640-build - slot 2 (recovery mode)  |
 |ONIE                                                                   |
 +-----------------------------------------------------------------------|
```

In this example, you are selecting the slot2 image. Under the `linux`
option, add *init=/bin/bash*:

``` 
           GNU GRUB  version 1.99-27+deb7u2
 +-------------------------------------------------------------------------+
 | insmod part_gpt                                                         |^
 | insmod ext2                                                             |
 | set root='(hd0,gpt3)'                                                   |
 | search --no-floppy --fs-uuid --set=root c42be287-5321-4e77-975f-54e237a\|
 | d72b0                                                                   |
 | echo 'Loading Linux  ...'                                               |
 | linux /cl-vmlinuz-3.2.60-1+deb7u1+cl2.5-slot-2 root=UUID=f01a2d40-d2fe-\|
 | 435b-b3d1-7edc1eb0c42f console=ttyS0,115200n8 cl_platform=dell_s6000_s1\|
 | 220 quiet active=2 init=/bin/bash                                       |
 | echo 'Loading initial ramdisk ...' A                                    |
 | initrd /cl-initrd.img-3.2.60-1+deb7u1+cl2.5-slot-2                      |
 |                                                                         | 
 +-------------------------------------------------------------------------+
```

Type Ctrl+x or F10 to boot with this change.

When you are done making changes as a single user, run `reboot -f` to
boot the switch back to a normal state:

    Begin: Running /scripts/init-bottom ... done.
    bash: cannot set terminal process group (-1): Inappropriate ioctl for device
    bash: no job control in this shell
    cumulus@switch:/# sudo reboot -f
